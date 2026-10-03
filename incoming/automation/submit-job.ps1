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
    [Parameter(Mandatory = $true, Position = 0)][string]$Paper,
    [string]$Title,
    [ValidateSet('analyze', 'deepdive')][string]$Type = 'analyze',
    [string]$Question,
    [switch]$Append, [switch]$DryRun, [switch]$Force,
    [string]$Source = 'laptop',
    [switch]$RunNow
)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'pipeline-lib.ps1')
$path = New-QueueJob -Paper $Paper -Title $Title -Type $Type -Question $Question -Append:$Append -DryRun:$DryRun -Force:$Force -Source $Source
Write-Host "Queued: $path"
if ($RunNow) {
    $t = Get-ScheduledTask -TaskName 'PhysicsWiki-PaperQueue' -ErrorAction SilentlyContinue
    if ($t) { Start-ScheduledTask -TaskName 'PhysicsWiki-PaperQueue'; Write-Host 'Started scheduled task PhysicsWiki-PaperQueue.' }
    else { Write-Host 'Scheduled task not found; run queue-worker.ps1 manually.' }
}
