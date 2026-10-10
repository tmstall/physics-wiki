<#
.SYNOPSIS
  Phase 4: stage waiting incoming\md analyses (+ embedded figures) into raw/analyses,
  then run a headless Grok wiki ingest.

.DESCRIPTION
  1) Staging follows incoming/prompts/COPY.md (copy -> verify -> archive -> READY_QUEUE pending),
     and also copies each analysis's embedded figures/<file> into raw/analyses/figures/
     (inbox figures are left in place; never deleted).
  2) Ingest runs C:\Users\tmsta\.grok\bin\grok.exe with incoming/automation/INGEST_HEADLESS.md
     (INGEST.md rules + no human pauses).

.EXAMPLE
  .\ingest-wiki.ps1
  .\ingest-wiki.ps1 -DryRun
  .\ingest-wiki.ps1 -StageOnly
  .\ingest-wiki.ps1 -IngestOnly -NoPush
#>
param(
    [switch]$DryRun,
    [switch]$StageOnly,
    [switch]$IngestOnly,
    [switch]$Force,
    [switch]$NoGit,
    [switch]$NoPush,
    [int]$MaxTurns = 600,
    [string]$GrokExe = 'C:\Users\tmsta\.grok\bin\grok.exe',
    [string]$ResultFile
)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'pipeline-lib.ps1')
Initialize-PipelineEnv

# Single-instance lock (auto-ingest + manual share queue\ingest.lock)
$ingestLockPath = Join-Path $script:QueueDir 'ingest.lock'
New-Item -ItemType Directory -Path $script:QueueDir -Force | Out-Null
try {
    $script:IngestLock = [IO.File]::Open($ingestLockPath, 'OpenOrCreate', 'ReadWrite', 'None')
} catch {
    Write-Host "ingest-wiki: another ingest holds ingest.lock; exiting."
    if ($ResultFile) {
        (@{ status = 'busy'; error = 'ingest.lock held' } | ConvertTo-Json) | Set-Content -LiteralPath $ResultFile -Encoding UTF8
    }
    exit 4
}
$script:IngestLock.SetLength(0)
$lb = [Text.Encoding]::ASCII.GetBytes("pid $PID ingest-wiki $(Get-Date -Format s)")
$script:IngestLock.Write($lb, 0, $lb.Length); $script:IngestLock.Flush()
try {

$MdDir = $script:MdDir
$RepoRoot = $script:RepoRoot
$AutoDir = $script:AutoDir
$RawDir = Join-Path $RepoRoot 'raw\analyses'
$RawFigDir = Join-Path $RawDir 'figures'
$ArchiveDir = Join-Path $MdDir 'archive'
$FigDir = Join-Path $MdDir 'figures'
$QueuePath = Join-Path $RepoRoot 'incoming\READY_QUEUE.md'
$StatusPath = Join-Path $RepoRoot 'incoming\_PIPELINE_STATUS.md'
$HeadlessPath = Join-Path $AutoDir 'INGEST_HEADLESS.md'
$ScratchRoot = Join-Path $AutoDir 'scratch\work'
$started = Get-Date
$today = Get-Date -Format 'yyyy-MM-dd'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$runDir = Join-Path $ScratchRoot ($stamp + '_ingest')
New-Item -ItemType Directory -Path $runDir -Force | Out-Null
$runLog = Join-Path $runDir 'run.log'
$grokOut = Join-Path $runDir 'grok-out.txt'

$result = [ordered]@{
    status = 'failed'; started = $started.ToString('s'); dryRun = [bool]$DryRun
    staged = @(); skippedExists = @(); failed = @(); figuresCopied = @()
    pendingBefore = 0; pendingAfterStage = 0; inboxBefore = 0; inboxAfter = 0
    grokExit = $null; elapsed = $null; preIngestSha = $null; error = $null
    runDir = $runDir
}

function Write-RunLog([string]$Msg) { Write-Log $Msg $runLog }

function Get-InboxMd {
    Get-ChildItem -LiteralPath $MdDir -Filter '*.md' -File | Sort-Object Name
}

function Get-EmbeddedFigures([string]$MdPath) {
    $text = [IO.File]::ReadAllText($MdPath)
    $rx = New-Object System.Text.RegularExpressions.Regex 'figures/([^\s\)\]\"'']+)'
    $names = foreach ($m in $rx.Matches($text)) { $m.Groups[1].Value }
    $names | Select-Object -Unique
}

function Get-FileSha([string]$Path) {
    (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Update-ReadyQueue([string[]]$CopiedNames) {
    if (-not (Test-Path -LiteralPath $QueuePath)) {
        $hdr = @"
# READY_QUEUE

staged_at: $today
notes: Staged by automation ingest-wiki.ps1.

| status | filename | staged_at | notes |
| --- | --- | --- | --- |
"@
        Write-Utf8File $QueuePath ($hdr.TrimEnd() + "`r`n")
    }
    $raw = [IO.File]::ReadAllText($QueuePath)
    if ($raw -match '(?m)^staged_at:\s*.*$') {
        $raw = [regex]::Replace($raw, '(?m)^staged_at:\s*.*$', "staged_at: $today", 1)
    }
    if ($raw -match '(?m)^notes:\s*.*$') {
        $raw = [regex]::Replace($raw, '(?m)^notes:\s*.*$', "notes: Staged by automation ingest-wiki.ps1 ($today). Build/Grok consumes pending rows.", 1)
    }
    $existing = @{}
    foreach ($line in ($raw -split "`r?`n")) {
        if ($line -match '^\|\s*(\w+)\s*\|\s*([^|]+?)\s*\|') {
            $st = $Matches[1].Trim(); $fn = $Matches[2].Trim()
            if ($fn -and $fn -ne 'filename' -and $fn -ne '---') { $existing[$fn] = $st }
        }
    }
    $toAppend = @()
    foreach ($name in $CopiedNames) {
        if ($existing.ContainsKey($name)) {
            $st = $existing[$name]
            if ($st -in @('done','skipped_duplicate','skipped','failed','failed_missing_raw','pending')) {
                Write-RunLog "READY_QUEUE: keep existing status=$st for $name"
                continue
            }
        }
        $toAppend += "| pending | $name | $today | |"
        $existing[$name] = 'pending'
    }
    if ($toAppend.Count) {
        $raw = $raw.TrimEnd() + "`r`n" + ($toAppend -join "`r`n") + "`r`n"
    }
    Write-Utf8File $QueuePath $raw
}

function Count-PendingQueue {
    if (-not (Test-Path -LiteralPath $QueuePath)) { return 0 }
    $n = 0
    foreach ($line in [IO.File]::ReadLines($QueuePath)) {
        if ($line -match '^\|\s*pending\s*\|') { $n++ }
    }
    return $n
}

function Invoke-Stage {
    Write-RunLog '=== STAGE (COPY.md + figures) ==='
    New-Item -ItemType Directory -Path $RawDir, $ArchiveDir, $RawFigDir -Force | Out-Null
    $inbox = @(Get-InboxMd)
    $result.inboxBefore = $inbox.Count
    Write-RunLog "Inbox root .md count: $($inbox.Count)"
    if (-not $inbox.Count) {
        Write-RunLog 'Inbox empty - nothing to stage.'
        return
    }
    $copied = New-Object System.Collections.Generic.List[string]
    foreach ($f in $inbox) {
        $name = $f.Name
        $dest = Join-Path $RawDir $name
        if ((Test-Path -LiteralPath $dest) -and -not $Force) {
            Write-RunLog "skipped_exists: $name"
            $result.skippedExists += $name
            continue
        }
        if ($DryRun) {
            Write-RunLog "DRYRUN would copy: $name"
            $copied.Add($name) | Out-Null
            $result.staged += $name
            foreach ($fig in (Get-EmbeddedFigures $f.FullName)) {
                Write-RunLog "DRYRUN would copy figure: $fig"
            }
            continue
        }
        try {
            Copy-Item -LiteralPath $f.FullName -Destination $dest -Force:$Force
            $srcLen = (Get-Item -LiteralPath $f.FullName).Length
            $dstLen = (Get-Item -LiteralPath $dest).Length
            if ($srcLen -ne $dstLen) { throw "size mismatch src=$srcLen dest=$dstLen" }
            $srcHash = Get-FileSha $f.FullName
            $dstHash = Get-FileSha $dest
            if ($srcHash -ne $dstHash) { throw 'sha256 mismatch' }
            foreach ($fig in (Get-EmbeddedFigures $f.FullName)) {
                $figSrc = Join-Path $FigDir $fig
                if (-not (Test-Path -LiteralPath $figSrc)) {
                    Write-RunLog "WARNING: missing figure $fig for $name"
                    continue
                }
                $figDest = Join-Path $RawFigDir $fig
                if ((Test-Path -LiteralPath $figDest) -and -not $Force) {
                    if ((Get-FileSha $figSrc) -eq (Get-FileSha $figDest)) {
                        Write-RunLog "figure exists (same hash): $fig"
                    } else {
                        Write-RunLog "WARNING: figure exists with different hash, leaving: $fig"
                    }
                } else {
                    Copy-Item -LiteralPath $figSrc -Destination $figDest -Force:$Force
                    if ((Get-FileSha $figSrc) -ne (Get-FileSha $figDest)) { throw "figure sha mismatch $fig" }
                    $result.figuresCopied += $fig
                    Write-RunLog "copied figure: $fig"
                }
            }
            $archDest = Join-Path $ArchiveDir $name
            if (Test-Path -LiteralPath $archDest) {
                $stem = [IO.Path]::GetFileNameWithoutExtension($name)
                $ext = [IO.Path]::GetExtension($name)
                $suffix = $today -replace '-',''
                $archDest = Join-Path $ArchiveDir ("$stem.copied-$suffix$ext")
                Write-RunLog "archive collision -> $(Split-Path $archDest -Leaf)"
            }
            Move-Item -LiteralPath $f.FullName -Destination $archDest -Force
            $copied.Add($name) | Out-Null
            $result.staged += $name
            Write-RunLog "copied+archived: $name"
        } catch {
            Write-RunLog "failed: $name - $($_.Exception.Message)"
            $result.failed += "$name ($($_.Exception.Message))"
        }
    }
    if (-not $DryRun) {
        Update-ReadyQueue @($copied)
    }
    $result.pendingAfterStage = Count-PendingQueue
    $result.inboxAfter = @(Get-InboxMd).Count
    Write-Host ''
    Write-Host '## Staging report (copy)'
    Write-Host ''
    Write-Host '| Result | Count |'
    Write-Host '| --- | --- |'
    Write-Host "| copied | $($result.staged.Count) |"
    Write-Host "| skipped_exists | $($result.skippedExists.Count) |"
    Write-Host "| failed | $($result.failed.Count) |"
    Write-Host "| figures_copied | $($result.figuresCopied.Count) |"
    Write-Host ''
    if ($result.staged.Count) {
        Write-Host '### Copied -> raw/analyses/'
        $result.staged | ForEach-Object { Write-Host "- $_" }
        Write-Host ''
    }
    if ($result.skippedExists.Count) {
        Write-Host '### Skipped (already in raw/analyses/)'
        $result.skippedExists | ForEach-Object { Write-Host "- $_" }
        Write-Host ''
    }
    if ($result.failed.Count) {
        Write-Host '### Failed'
        $result.failed | ForEach-Object { Write-Host "- $_" }
        Write-Host ''
    }
    Write-Host "READY_QUEUE pending: $($result.pendingAfterStage)"
    Write-Host "Inbox remaining: $($result.inboxAfter)"
}

function Update-StatusCard([string]$Notes) {
    $inbox = @(Get-InboxMd).Count
    $pending = Count-PendingQueue
    $body = @"
# Pipeline status (Wiki)

Human or Grok Build may update after ``copy`` / ``ingest``. **Bot may read; must not invent numbers.**

| Field | Value |
| --- | --- |
| updated_at | $today |
| inbox_count_incoming_md_root | $inbox |
| inbox_notify_threshold | 5 |
| READY_QUEUE pending | $pending |
| last_copy | $today |
| last_ingest | $Notes |
| notes | Phase 4 automation ingest-wiki.ps1. Dual-analysis compare policy unchanged. |

## Paths

- Local: ``Physics-Wiki/incoming/_PIPELINE_STATUS.md``
- Drive: ``Technical Papers/Analyses/_PIPELINE_STATUS.md``
- Never place under ``incoming/md/``.

"@
    Write-Utf8File $StatusPath $body
}

function Invoke-GrokIngest {
    Write-RunLog '=== INGEST (Grok headless) ==='
    if (-not (Test-Path -LiteralPath $GrokExe)) { throw "grok.exe not found: $GrokExe" }
    if (-not (Test-Path -LiteralPath $HeadlessPath)) { throw "missing $HeadlessPath" }
    $pending = Count-PendingQueue
    $result.pendingBefore = $pending
    if ($pending -le 0) {
        Write-RunLog 'No pending READY_QUEUE rows - nothing to ingest.'
        return
    }
    $promptPath = Join-Path $runDir 'prompt.md'
    $prompt = @"
Read and follow ``incoming/automation/INGEST_HEADLESS.md`` in full, then execute the ingest now.

Also follow ``incoming/prompts/INGEST.md`` and repo-root ``AGENTS.md`` for wiki structure. Headless overrides in INGEST_HEADLESS.md win over pause/triage tokens.

There are currently $pending pending rows in ``incoming/READY_QUEUE.md``. Ingest all of them. Do not pause. Do not ask questions. Write wiki pages under ``wiki/``, update READY_QUEUE statuses, update ``wiki/index.md`` and ``wiki/log.md``, run lints as specified, update ``incoming/_PIPELINE_STATUS.md``, and finish with the final summary required by INGEST_HEADLESS.md.

Working directory is the Physics-Wiki repo root.
"@
    Write-Utf8File $promptPath $prompt
    if ($DryRun) {
        Write-RunLog "DRYRUN would run: $GrokExe --cwd $RepoRoot --prompt-file $promptPath --always-approve --permission-mode bypassPermissions --max-turns $MaxTurns --output-format plain"
        return
    }
    $grokArgs = @(
        '--cwd', $RepoRoot,
        '--prompt-file', $promptPath,
        '--always-approve',
        '--permission-mode', 'bypassPermissions',
        '--max-turns', "$MaxTurns",
        '--output-format', 'plain',
        '--disable-web-search'
    )
    Write-RunLog ('Running grok: ' + ($grokArgs -join ' '))
    Push-Location $RepoRoot
    try {
        $prevEap = $ErrorActionPreference
        $ErrorActionPreference = 'Continue'
        & $GrokExe @grokArgs 2>&1 | ForEach-Object { "$_" } | Tee-Object -FilePath $grokOut
        $result.grokExit = $LASTEXITCODE
        $ErrorActionPreference = $prevEap
    } finally {
        Pop-Location
    }
    Write-RunLog "grok exit: $($result.grokExit)"
}

function Invoke-GitCommit {
    $ErrorActionPreference = 'Continue'   # git prints LF/CRLF warnings on stderr; under 'Stop' with 2>&1 that aborted the commit (2026-10-09). Function-scoped.
    if ($NoGit -or $DryRun) { Write-RunLog 'Skipping git (NoGit/DryRun)'; return }
    Write-RunLog '=== GIT COMMIT (explicit paths) ==='
    Push-Location $RepoRoot
    try {
        $paths = New-Object System.Collections.Generic.List[string]
        foreach ($p in @(
            'incoming/automation/ingest-wiki.ps1',
            'incoming/automation/INGEST_HEADLESS.md',
            'incoming/automation/README.md',
            'incoming/automation/pipeline-config.md',
            'incoming/READY_QUEUE.md',
            'incoming/_PIPELINE_STATUS.md',
            'incoming/PIPELINE.md'
        )) {
            if (Test-Path -LiteralPath (Join-Path $RepoRoot $p)) { $paths.Add($p) | Out-Null }
        }
        foreach ($name in $result.staged) {
            $paths.Add(('raw/analyses/' + $name)) | Out-Null
        }
        foreach ($fig in ($result.figuresCopied | Select-Object -Unique)) {
            $paths.Add(('raw/analyses/figures/' + $fig)) | Out-Null
        }
        # Archived originals (recoverable) + remove former inbox-root paths from the index
        foreach ($name in $result.staged) {
            $arch = Join-Path $ArchiveDir $name
            if (Test-Path -LiteralPath $arch) { $paths.Add(('incoming/md/archive/' + $name)) | Out-Null }
            $oldInbox = Join-Path $MdDir $name
            if (-not (Test-Path -LiteralPath $oldInbox)) {
                git rm --ignore-unmatch --quiet -- ('incoming/md/' + $name) 2>&1 | ForEach-Object { Write-RunLog "git rm inbox: $_" }
            }
        }
        if (Test-Path 'wiki') {
            git add -A -- 'wiki' 2>&1 | ForEach-Object { Write-RunLog "git: $_" }
        }
        Get-ChildItem -LiteralPath $RepoRoot -Filter "LINT_REPORT_$today*.md" -File -ErrorAction SilentlyContinue | ForEach-Object {
            $paths.Add($_.Name) | Out-Null
        }
        Get-ChildItem -LiteralPath $RepoRoot -Filter "LINT_LIGHT_$today*.md" -File -ErrorAction SilentlyContinue | ForEach-Object {
            $paths.Add($_.Name) | Out-Null
        }
        foreach ($p in $paths) {
            git add -- $p 2>&1 | ForEach-Object { Write-RunLog "git add $p : $_" }
        }
        git reset HEAD -- .gitignore 2>$null | Out-Null
        git status --short | ForEach-Object { Write-RunLog "status: $_" }
        $stagedNames = @(git diff --cached --name-only)
        if (-not $stagedNames.Count) {
            Write-RunLog 'Nothing staged to commit.'
            return
        }
        $msg = "Phase 4 ingest: stage + wiki ingest ($($result.staged.Count) staged)"
        git commit -m $msg 2>&1 | ForEach-Object { Write-RunLog "$_" }
        if (-not $NoPush) {
            git push origin main 2>&1 | ForEach-Object { Write-RunLog "$_" }
            git push origin 'pre-ingest-phase4-2026-10-05' 2>&1 | ForEach-Object { Write-RunLog "tag push: $_" }
        } else {
            Write-RunLog 'NoPush set - commit local only'
        }
    } finally { Pop-Location }
}

try {
    Write-RunLog 'Phase 4 ingest-wiki start'
    Write-RunLog "Repo: $RepoRoot"
    Push-Location $RepoRoot
    $result.preIngestSha = (git rev-parse HEAD).Trim()
    Pop-Location
    Write-RunLog "pre-ingest SHA: $($result.preIngestSha) (tag pre-ingest-phase4-2026-10-05)"

    if (-not $IngestOnly) { Invoke-Stage }
    else {
        $result.inboxBefore = @(Get-InboxMd).Count
        $result.pendingAfterStage = Count-PendingQueue
        Write-RunLog "IngestOnly: pending=$($result.pendingAfterStage) inbox=$($result.inboxBefore)"
    }

    if (-not $StageOnly) { Invoke-GrokIngest }
    else { Write-RunLog 'StageOnly: skipping grok ingest' }

    if (-not $DryRun) {
        $pendingNow = Count-PendingQueue
        if (-not $StageOnly) {
            Update-StatusCard "$today (automation ingest-wiki.ps1)"
        } else {
            Update-StatusCard "(unchanged; stage only $today)"
        }
        Write-RunLog "READY_QUEUE pending after run: $pendingNow"
    }

    Invoke-GitCommit

    $result.elapsed = ((Get-Date) - $started).ToString('hh\:mm\:ss')
    if ($result.failed.Count -and -not $result.staged.Count -and -not $IngestOnly) {
        $result.status = 'failed'
    } elseif ($DryRun) {
        $result.status = 'dry-run'
    } else {
        $result.status = 'ok'
    }
    Write-RunLog "Done status=$($result.status) elapsed=$($result.elapsed)"
    $result | Format-List
    if ($ResultFile) {
        ($result | ConvertTo-Json -Depth 6) | Set-Content -LiteralPath $ResultFile -Encoding UTF8
    }
    if ($result.status -eq 'failed') { $script:IngestExitCode = 1 } else { $script:IngestExitCode = 0 }
} catch {
    $result.error = $_.Exception.Message
    $result.elapsed = ((Get-Date) - $started).ToString('hh\:mm\:ss')
    Write-RunLog "ERROR: $($result.error)"
    if ($ResultFile) { ($result | ConvertTo-Json -Depth 6) | Set-Content -LiteralPath $ResultFile -Encoding UTF8 }
    $script:IngestExitCode = 1
    throw
}
} finally {
    if ($script:IngestLock) { try { $script:IngestLock.Close() } catch { } }
}
if ($null -eq $script:IngestExitCode) { $script:IngestExitCode = 1 }
exit $script:IngestExitCode
