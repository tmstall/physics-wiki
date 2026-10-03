<#
.SYNOPSIS
  One-command paper analysis: duplicate check -> latest arXiv PDF -> Claude Code (Opus) with
  ANALYZE_HEADLESS.md (newest framework auto-resolved) -> verified delivery (incoming\md, Drive,
  papers log, git commit + push).

.EXAMPLE
  .\analyze-paper.ps1 2605.16504
  .\analyze-paper.ps1 https://arxiv.org/abs/2605.16504 -Title 'Neutrino flavor conversion ...'
  .\analyze-paper.ps1 10.1103/pz3y-3lv5
  .\analyze-paper.ps1 2602.03456 -DryRun        # no Claude call, no delivery

  Exit codes: 0 done (or dry run ok), 1 failed, 2 duplicate (skipped), 3 usage limit (stopped cleanly).
#>
param(
    [Parameter(Mandatory = $true, Position = 0)][string]$Paper,
    [string]$Title,
    [switch]$DryRun,       # metadata + duplicate check + PDF download + prompt only; no Claude, no delivery
    [switch]$NoDeliver,    # run Claude but leave the output in the work folder
    [switch]$NoPush,       # commit but do not push
    [switch]$Force,        # ignore duplicate hits / overwrite identical names
    [string]$ResultFile,   # JSON result for the queue worker
    [string]$JobId
)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'pipeline-lib.ps1')
Initialize-PipelineEnv

$result = [ordered]@{ status = 'failed'; paper = $Paper; jobId = $JobId; started = (Get-Date).ToString('s'); title = $null; arxiv = $null; doi = $null
    workDir = $null; output = $null; words = $null; bytes = $null; model = $null; elapsed = $null; costUsd = $null
    usageBefore = $null; usageAfter = $null; resetsAt = $null; recovered = $false; duplicates = @(); delivery = $null; error = $null }
$runLog = $null
try {
    # 1. metadata
    $meta = Get-PaperMeta $Paper $Title
    $result.title = $meta.title; $result.arxiv = $meta.arxiv; $result.doi = $meta.doi
    $idLabel = Get-IdLabel $meta
    New-Item -ItemType Directory -Path $WorkRoot -Force | Out-Null
    $workDir = Join-Path $WorkRoot ((Get-Date -Format 'yyyyMMdd-HHmmss') + '_' + $idLabel)
    New-Item -ItemType Directory -Path $workDir -Force | Out-Null
    $result.workDir = $workDir
    $runLog = Join-Path $workDir 'run.log'
    Write-Log "Paper: $($meta.title)" $runLog
    Write-Log "  arXiv: $($meta.arxiv) v$($meta.version)  DOI: $($meta.doi)  journal: $($meta.journal)" $runLog
    foreach ($n in $meta.notes) { Write-Log "  note: $n" $runLog }

    # 2. duplicate check
    $dups = Find-PaperDuplicates $meta
    $result.duplicates = @($dups | ForEach-Object { "$($_.strength): $($_.path):$($_.line) - $($_.why)" })
    foreach ($h in $dups) { Write-Log "  dup-check $($h.strength): $($h.path):$($h.line)  $($h.why)" $runLog }
    $strong = @($dups | Where-Object { $_.strength -eq 'strong' })
    if ($strong.Count -and -not $Force) {
        $result.status = 'duplicate'
        Write-Log "DUPLICATE: already analyzed (strong match in $($strong.Count) file(s)). Stopping. Use -Force to override." $runLog
        Save-Result $ResultFile $result; exit 2
    }
    if (-not $dups.Count) { Write-Log '  dup-check: no matches in wiki/papers, raw/analyses, incoming/md or the papers log' $runLog }

    # 3. full text
    $pdfInfo = $null
    if ($meta.arxiv) {
        $pdfInfo = Get-ArxivPdf $meta $workDir
        Write-Log "  PDF: $($pdfInfo.pdf) ($($pdfInfo.bytes) bytes, $($pdfInfo.pages) pages)" $runLog
    } else { Write-Log '  No arXiv version found: Claude will retrieve the text via the DOI (ANALYZE_HEADLESS.md section 3).' $runLog }

    # 4. prompt
    $desc = "Paper to analyze: $($meta.title)"
    if ($meta.authors.Count) { $au = ($meta.authors | Select-Object -First 4) -join ', '; if ($meta.authors.Count -gt 4) { $au += ' et al.' }; $desc += " by $au" }
    if ($meta.arxiv) { $desc += "; arXiv $($meta.arxiv) (https://arxiv.org/abs/$($meta.arxiv))" }
    if ($meta.doi) { $desc += "; DOI $($meta.doi)" }
    if ($meta.journal) { $desc += "; published as $($meta.journal)" }
    $desc += '.'
    if ($pdfInfo) {
        $text = "The full paper PDF (arXiv v$($meta.version), the latest version, $($pdfInfo.pages) pages) is at $($pdfInfo.pdf) - read it directly with the Read tool (poppler is installed; use page ranges of at most 20 pages)."
        if ($pdfInfo.txt) { $text += " Backup: full-text extraction at $($pdfInfo.txt)." }
        $text += ' Read the whole paper including any appendices and supplementary material (if the supplement is a separate file, fetch it as ANALYZE_HEADLESS.md section 3 describes).'
    } else {
        $text = 'No local PDF was available: get the full text yourself as ANALYZE_HEADLESS.md section 3 describes (DOI landing page / open-access version).'
    }
    $prompt = 'Read incoming/automation/ANALYZE_HEADLESS.md and follow it exactly (the framework itself defines the depth target, full-paper reading, claim check and referee pass). Then resolve and read the newest framework in ' + $FrameworkDir + ' as ANALYZE_HEADLESS.md section 1 describes, and apply it. ' +
        $desc + ' ' + $text + ' Python is available for numeric checks (run python only; put any scripts in the work directory). ' + $CompareRule + ' ' +
        'Work directory for this run: ' + $workDir + ' - write the finished analysis there using the filename convention in ANALYZE_HEADLESS.md (id ' + $idLabel + ', no suffix). Write nowhere else; the pipeline script does the delivery.'
    Write-Utf8File (Join-Path $workDir 'prompt.txt') $prompt
    if ($DryRun) {
        $result.status = 'dry-run'
        Write-Log "DRY RUN: skipped the Claude call and delivery. Prompt saved to $workDir\prompt.txt" $runLog
        Save-Result $ResultFile $result; exit 0
    }

    # 5. Claude Code on Opus
    $jsonl = Join-Path $workDir 'claude.jsonl'
    Write-Log "Running Claude Code (opus); log $jsonl" $runLog
    $run = Invoke-ClaudeRun $prompt $jsonl
    $result.model = $run.model; $result.elapsed = $run.elapsed; $result.costUsd = $run.costUsd
    $result.usageBefore = $run.usageFirst; $result.usageAfter = $run.usageLast
    $fmt = { param($u) if ($u) { '5h ' + [int]([double]$u.fiveHour * 100) + '% / week ' + [int]([double]$u.weekly * 100) + '%' } else { 'n/a' } }
    Write-Log "Claude finished: exit $($run.exitCode), $($run.elapsed), turns $($run.turns), cost `$$($run.costUsd), model $($run.model)" $runLog
    Write-Log "  usage before: $(& $fmt $run.usageFirst)  after: $(& $fmt $run.usageLast)" $runLog
    if ($run.limitHit) {
        $result.status = 'limit'; $result.resetsAt = $run.resetsAt
        Write-Log "USAGE LIMIT hit (resetsAt $($run.resetsAt)). Stopping cleanly; job stays queued as 'limit'." $runLog
        Save-Result $ResultFile $result; exit 3
    }

    # 6. find (or recover) the output
    $out = Get-ChildItem -Path $workDir -File -Filter '*.md' | Where-Object { $_.Name -match '^\d{4}-\d{2}-\d{2}_' } | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if (-not $out) {
        Write-Log 'No analysis file in the work folder; trying to recover it from the jsonl log.' $runLog
        $rec = Restore-AnalysisFromJsonl $run $workDir
        if ($rec) { $out = Get-Item $rec; $result.recovered = $true; Write-Log "  recovered $rec from the jsonl" $runLog }
    }
    if (-not $out) { throw "Claude produced no analysis file. Result: $($run.result)" }
    $first = ([IO.File]::ReadAllLines($out.FullName) | Select-Object -First 2) -join ' '
    if ($first -notmatch 'v\d+\.\d+') { Write-Log "  WARNING: header lines do not show a framework version: $first" $runLog }

    # normalize filename: today's date + id label
    $today = Get-Date -Format 'yyyy-MM-dd'
    $name = $out.Name
    if ($name -notmatch ('^' + [regex]::Escape($today) + '_' + [regex]::Escape($idLabel) + '_.+\.md$')) {
        $slug = $(if ($name -match '^\d{4}-\d{2}-\d{2}_(?:arxiv|doi)-[^_]+_(.+)\.md$') { $Matches[1] } else { Get-Slug $meta.title })
        $name = $today + '_' + $idLabel + '_' + $slug + '.md'
        Rename-Item -LiteralPath $out.FullName -NewName $name
        $out = Get-Item (Join-Path $workDir $name)
        Write-Log "  renamed output to $name" $runLog
    }
    $result.output = $out.FullName; $result.bytes = $out.Length; $result.words = Get-WordCount $out.FullName
    Write-Log "Output: $($out.FullName) ($($out.Length) bytes, ~$($result.words) words)" $runLog

    # 7. delivery
    if ($NoDeliver) { $result.status = 'done-undelivered'; Write-Log 'NoDeliver: output left in the work folder.' $runLog }
    else {
        $model = $(if ($run.model) { $run.model } else { 'opus' })
        $result.delivery = Invoke-Delivery -SourceFile $out.FullName -Meta $meta -Model $model -NoPush:$NoPush -Force:$Force -RunLog $runLog
        $result.status = 'done'
    }
    Write-Log "DONE: $($result.status)" $runLog
    Save-Result $ResultFile $result; exit 0
}
catch {
    $result.status = 'failed'; $result.error = $_.Exception.Message
    Write-Log ("FAILED: " + $_.Exception.Message + ' @ ' + $_.InvocationInfo.PositionMessage) $runLog
    Save-Result $ResultFile $result; exit 1
}
