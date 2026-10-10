<#
.SYNOPSIS
  Add a job to incoming\automation\queue\ (and optionally start the worker now).
.EXAMPLE
  .\submit-job.ps1 2605.16504
  .\submit-job.ps1 10.1103/pz3y-3lv5 -Title 'Neutrino flavor ...' -RunNow
  .\submit-job.ps1 2605.16504 -Type deepdive -Question 'Why does deep mixing hurt 20 Msun stars?' -Append
  .\submit-job.ps1 2602.03456 -DryRun -RunNow
#>
param(
    [Parameter(Position = 0)][string]$Paper,
    [string]$Title,
    [ValidateSet('analyze', 'deepdive')][string]$Type = 'analyze',
    [string]$Question,
    [switch]$Append, [switch]$DryRun, [switch]$Force,
    [string]$Source = 'laptop',
    [switch]$RunNow,
    [string]$Framework, [string]$LocalPdf, [string]$Slug   # optional: explicit framework file; local PDF (no arXiv/DOI) + its id slug
)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'pipeline-lib.ps1')
if ($LocalPdf) {
    $LocalPdf = (Resolve-Path -LiteralPath $LocalPdf).Path
    if (-not $Slug) { $Slug = Get-Slug $(if ($Title) { $Title } else { [IO.Path]::GetFileNameWithoutExtension($LocalPdf) }) }
    if (-not $Paper) { $Paper = $Slug }
}
if ($Framework) { $Framework = (Resolve-Path -LiteralPath $Framework).Path }
if (-not $Paper) { throw 'Give a paper (arXiv ID/DOI/URL) or -LocalPdf.' }
$path = New-QueueJob -Paper $Paper -Title $Title -Type $Type -Question $Question -Append:$Append -DryRun:$DryRun -Force:$Force -Source $Source -Framework $Framework -LocalPdf $LocalPdf -Slug $Slug
Write-Host "Queued: $path"
if ($RunNow) {
    $t = Get-ScheduledTask -TaskName 'PhysicsWiki-PaperQueue' -ErrorAction SilentlyContinue
    if ($t) { Start-ScheduledTask -TaskName 'PhysicsWiki-PaperQueue'; Write-Host 'Started scheduled task PhysicsWiki-PaperQueue.' }
    else { Write-Host 'Scheduled task not found; run queue-worker.ps1 manually.' }
}
