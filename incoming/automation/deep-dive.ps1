<#
.SYNOPSIS
  Deep dive on an already-analyzed paper with Claude Code (Opus). Loads the analysis, the paper PDF
  and DEEPDIVE_HEADLESS.md, writes the answer to incoming\deep-dives\ and Drive 'Technical Papers\Deep Dives'.
  -Append also appends it to the analysis in incoming\md (DEEP_DIVE.md session format) and re-syncs
  that analysis to Drive Analyses.
.EXAMPLE
  .\deep-dive.ps1 2605.16504 'Why does flavor equipartition below the neutrinosphere cool the gain region?'
  .\deep-dive.ps1 neutrino-flavor 'Re-derive the 1.9x / 2.6x rate deficits' -Append
  Exit codes: 0 done, 1 failed, 3 usage limit.
#>
param(
    [Parameter(Mandatory = $true, Position = 0)][string]$Paper,      # arXiv ID / DOI / URL / unique filename substring
    [Parameter(Mandatory = $true, Position = 1)][string]$Question,
    [switch]$Append, [switch]$DryRun, [switch]$NoPush,
    [string]$ResultFile
)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'pipeline-lib.ps1')
Initialize-PipelineEnv
$DeepDiveDir = Join-Path $RepoRoot 'incoming\deep-dives'
$result = [ordered]@{ status = 'failed'; paper = $Paper; question = $Question; analysis = $null; output = $null; drive = $null; appended = $null; git = $null; elapsed = $null; usageBefore = $null; usageAfter = $null; resetsAt = $null; error = $null }
$runLog = $null
try {
    # 1. find the analysis
    $ref = Resolve-PaperRef $Paper
    $pats = @()
    if ($ref.arxiv) { $pats += ('arxiv-' + $ref.arxiv) }
    if ($ref.doi) { $pats += ('doi-' + ($ref.doi -replace '[^A-Za-z0-9.\-]', '-')) }
    if (-not $pats.Count) { $pats += $Paper }
    $roots = @(@{ p = $MdDir; r = $false; rank = 0 }, @{ p = $MdDir; r = $true; rank = 1 }, @{ p = (Join-Path $RepoRoot 'raw\analyses'); r = $true; rank = 2 })
    $cands = @()
    foreach ($ro in $roots) {
        if (-not (Test-Path $ro.p)) { continue }
        $fs = Get-ChildItem -Path $ro.p -File -Filter *.md -Recurse:([bool]$ro.r) -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\(\.obsidian|_to_delete)\\' }
        foreach ($f in $fs) { foreach ($pt in $pats) { if ($f.Name.IndexOf($pt, [StringComparison]::OrdinalIgnoreCase) -ge 0) { $cands += [pscustomobject]@{ f = $f; rank = $ro.rank } } } }
        if ($cands.Count) { break }
    }
    $cands = @($cands | Sort-Object { $_.f.FullName } -Unique | Sort-Object rank, @{ e = { $_.f.Name -match '^(g_|sonnet_)' } }, @{ e = { $_.f.LastWriteTime }; Descending = $true })
    if (-not $cands.Count) { throw "No analysis found for '$Paper' in incoming\md or raw\analyses." }
    $analysis = $cands[0].f
    if ($cands.Count -gt 1) { Write-Host ("Several matches; using the first:`n  " + (($cands | ForEach-Object { $_.f.FullName }) -join "`n  ")) }
    $result.analysis = $analysis.FullName
    $idLabel = $(if ($analysis.Name -match '^(?:g_|sonnet_)?\d{4}-\d{2}-\d{2}_((?:arxiv|doi)-[^_]+)_') { $Matches[1] } else { Get-Slug $analysis.BaseName 4 })
    $arxiv = $(if ($ref.arxiv) { $ref.arxiv } elseif ($idLabel -match '^arxiv-(.+)$') { $Matches[1] } else { $null })

    $workDir = Join-Path $WorkRoot ((Get-Date -Format 'yyyyMMdd-HHmmss') + '_dd_' + $idLabel)
    New-Item -ItemType Directory -Path $workDir -Force | Out-Null
    $runLog = Join-Path $workDir 'run.log'
    Write-Log "Deep dive on $($analysis.FullName)" $runLog
    Write-Log "Question: $Question" $runLog

    # 2. PDF (reuse a downloaded one, else fetch the latest arXiv version)
    $pdf = $null
    if ($arxiv) {
        $pdf = Get-ChildItem -Path $ScratchDir -Recurse -File -Filter ("arxiv-$arxiv*.pdf") -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        if ($pdf) { $pdf = $pdf.FullName }
        else { try { $m = Get-PaperMeta $arxiv; $pdf = (Get-ArxivPdf $m $workDir).pdf } catch { Write-Log "  PDF download failed: $($_.Exception.Message)" $runLog } }
    }
    Write-Log "  PDF: $pdf" $runLog
    $wf = @((Join-Path $AutoDir 'deep-dive-workflow.md'), (Join-Path $RepoRoot 'incoming\prompts\deep-dive-workflow.md'), (Join-Path $FrameworkDir 'deep-dive-workflow.md')) | Where-Object { Test-Path $_ } | Select-Object -First 1

    # 3. prompt
    $qslug = Get-Slug $Question 6
    $outName = (Get-Date -Format 'yyyy-MM-dd') + '_' + $idLabel + '_dd-' + $qslug + '.md'
    $prompt = 'Read incoming/automation/DEEPDIVE_HEADLESS.md and follow it exactly. Existing analysis: ' + $analysis.FullName + '. ' +
        $(if ($pdf) { 'Paper PDF: ' + $pdf + ' (read the relevant parts directly with the Read tool, at most 20 pages per call). ' } else { 'No local PDF is available; use the analysis and, if needed, the paper online (arXiv HTML/PDF or DOI page). ' }) +
        $(if ($wf) { 'Also read the deep-dive workflow at ' + $wf + '. ' } else { '' }) +
        'Question: ' + $Question.Replace('"', "'") + ' ' + $CompareRule + ' Work directory: ' + $workDir + ' - write the answer there as ' + $outName + ' and nowhere else.'
    Write-Utf8File (Join-Path $workDir 'prompt.txt') $prompt
    if ($DryRun) { $result.status = 'dry-run'; Write-Log "DRY RUN: prompt saved, no Claude call." $runLog; Save-Result $ResultFile $result; exit 0 }

    # 4. Claude
    $run = Invoke-ClaudeRun $prompt (Join-Path $workDir 'claude.jsonl')
    $result.elapsed = $run.elapsed; $result.usageBefore = $run.usageFirst; $result.usageAfter = $run.usageLast
    Write-Log "Claude finished: exit $($run.exitCode), $($run.elapsed), cost `$$($run.costUsd)" $runLog
    if ($run.limitHit) { $result.status = 'limit'; $result.resetsAt = $run.resetsAt; Write-Log 'USAGE LIMIT hit; stopping cleanly.' $runLog; Save-Result $ResultFile $result; exit 3 }
    $out = Join-Path $workDir $outName
    if (-not (Test-Path $out)) {
        $cand = Get-ChildItem $workDir -File -Filter '*.md' | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        if ($cand) { Move-Item $cand.FullName $out } else {
            $rec = Restore-AnalysisFromJsonl $run $workDir
            if ($rec) { Move-Item $rec $out -Force; Write-Log '  recovered the answer from the jsonl' $runLog }
        }
    }
    if (-not (Test-Path $out) -or (Get-Item $out).Length -lt 1500) { throw "No usable deep-dive answer was written. Result: $($run.result)" }

    # 5. deliver: incoming\deep-dives + Drive Deep Dives
    New-Item -ItemType Directory -Path $DeepDiveDir -Force | Out-Null
    $dest = Join-Path $DeepDiveDir $outName
    $n = Copy-Verified $out $dest
    $result.output = "$dest ($n bytes, verified)"; Write-Log "  answer -> $($result.output)" $runLog
    $commitPaths = @((Get-RelPath $RepoRoot $dest))
    if (Wait-DriveMount $DriveDeepDives) {
        New-Item -ItemType Directory -Path $DriveDeepDives -Force | Out-Null
        $n2 = Copy-Verified $out (Join-Path $DriveDeepDives $outName); $result.drive = "$DriveDeepDives\$outName ($n2 bytes, verified)"
    } else { $result.drive = 'FAILED: G: not mounted'; Add-Utf8Line (Join-Path $QueueDir 'drive-retry.txt') ($dest + "`t" + $DriveDeepDives) }
    Write-Log "  drive  -> $($result.drive)" $runLog

    # 6. optional append to the analysis (only for an analysis in incoming\md root, per DEEP_DIVE.md)
    if ($Append) {
        if ((Split-Path $analysis.FullName) -ne $MdDir) { Write-Log "  -Append skipped: the analysis is not in incoming\md root (DEEP_DIVE.md only appends there)." $runLog; $result.appended = 'skipped (not in incoming\md root)' }
        else {
            $ans = [IO.File]::ReadAllText($out)
            $i = $ans.IndexOf('### Q:'); if ($i -lt 0) { $i = 0 }
            $body = $ans.Substring($i).TrimEnd()
            $atext = [IO.File]::ReadAllText($analysis.FullName)
            $session = ([regex]::Matches($atext, '(?m)^## Deep Dive - ')).Count + 1
            $stamp = Get-Date -Format 'yyyy-MM-ddTHH:mm'
            $sec = "`n`n---`n`n## Deep Dive - $(Get-Date -Format 'yyyy-MM-dd') (session $session)`n`n**Status:** closed`n**Analyzer:** Claude (headless, Opus)`n**Started:** $stamp (local)`n**Ended:** $stamp (local)`n**Source analysis:** ``$($analysis.Name)```n`n$body`n"
            $before = $analysis.Length
            [IO.File]::AppendAllText($analysis.FullName, $sec, $Utf8NoBom)
            $after = (Get-Item $analysis.FullName).Length
            if ($after -le $before) { throw 'Append to the analysis could not be verified.' }
            $result.appended = "$($analysis.FullName) session $session ($before -> $after bytes)"
            if (Wait-DriveMount $DriveAnalyses) { $n3 = Copy-Verified $analysis.FullName (Join-Path $DriveAnalyses $analysis.Name); $result.appended += "; Drive Analyses re-synced ($n3 bytes)" }
            if ((Invoke-Git $RepoRoot @('ls-files', '--error-unmatch', (Get-RelPath $RepoRoot $analysis.FullName))).code -eq 0) { $commitPaths += (Get-RelPath $RepoRoot $analysis.FullName) }
            Write-Log "  append -> $($result.appended)" $runLog
        }
    }

    # 7. git
    $g = Invoke-Git $RepoRoot (@('add', '--') + $commitPaths)
    if ($g.code -eq 0) {
        $g = Invoke-Git $RepoRoot (@('commit', '-m', ('Add deep dive: ' + $outName), '--') + $commitPaths)
        if ($g.code -eq 0) {
            $result.git = (Invoke-Git $RepoRoot @('rev-parse', '--short', 'HEAD')).out.Trim()
            if (-not $NoPush) { $p = Invoke-Git $RepoRoot @('push', 'origin', 'HEAD'); $result.git += $(if ($p.code -eq 0) { ' pushed' } else { ' (push failed; worker retries)' }) }
        } else { $result.git = 'commit failed: ' + $g.out }
    } else { $result.git = 'add failed: ' + $g.out }
    Write-Log "  git    -> $($result.git)" $runLog
    $result.status = 'done'
    Save-Result $ResultFile $result; exit 0
}
catch {
    $result.error = $_.Exception.Message
    Write-Log ('FAILED: ' + $_.Exception.Message) $runLog
    Save-Result $ResultFile $result; exit 1
}
