<#
.SYNOPSIS
  Deliver an existing analysis .md (verified copies): incoming\md, Drive Analyses (+PDF if a converter
  exists), papers-analyzed log, git commit + push. Images it embeds as figures/<file> (relative to the
  .md) are copied to incoming\md\figures\ and Drive Analyses\figures\ and committed with it.
  The .md and its figures are also copied to the To Read folder (to_read_dir in pipeline-config.md; non-fatal). analyze-paper.ps1 calls the same code.
  Overrides exist so it can be tested against a throwaway folder / repo.

.EXAMPLE
  .\deliver-analysis.ps1 -File scratch\work\...\2026-10-03_arxiv-2605.16504_x.md -Paper 2605.16504
  # test into a temp location (no real inbox/Drive/log):
  .\deliver-analysis.ps1 -File x.md -Paper 2605.16504 -MdDir T:\repo\incoming\md -DriveDir T:\drive -LogFile T:\repo\log.md -RepoRoot T:\repo -ToReadDir T:\toread -NoPush
  # -NoToRead skips the To Read copy (target folder = to_read_dir in pipeline-config.md)
#>
param(
    [Parameter(Mandatory = $true)][string]$File,
    [Parameter(Mandatory = $true)][string]$Paper,
    [string]$Title,
    [string]$Model = 'opus',
    [string]$MdDir, [string]$DriveDir, [string]$LogFile, [string]$RepoRoot, [string]$PdfTodo, [string]$ToReadDir,
    [switch]$NoToRead,
    [switch]$NoGit, [switch]$NoPush, [switch]$Force,
    [switch]$Replace, [string]$Note   # re-delivery: replace the paper's log row; Note goes into the model column
)
$ErrorActionPreference = 'Stop'
# Stash the overrides BEFORE dot-sourcing: the lib sets script-scope $MdDir/$RepoRoot, which would overwrite them.
$ov = @{ MdDir = $MdDir; DriveDir = $DriveDir; LogFile = $LogFile; RepoRoot = $RepoRoot; PdfTodo = $PdfTodo; ToReadDir = $ToReadDir }
. (Join-Path $PSScriptRoot 'pipeline-lib.ps1')
Initialize-PipelineEnv
$meta = Get-PaperMeta $Paper $Title
$p = @{ SourceFile = (Resolve-Path -LiteralPath $File).Path; Meta = $meta; Model = $Model; NoGit = $NoGit; NoPush = $NoPush; Force = $Force; Replace = $Replace; Note = $Note }
foreach ($k in @($ov.Keys)) { if ($ov[$k]) { $p[$k] = $ov[$k] } }
if ($NoToRead) { $p['ToReadDir'] = '' }
$d = Invoke-Delivery @p
$d | Format-List
