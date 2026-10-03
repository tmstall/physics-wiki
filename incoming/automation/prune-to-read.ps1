<#
.SYNOPSIS
  Prunes the To Read folder (to_read_dir in pipeline-config.md, default G:\My Drive\To Read):
  deletes .md files whose LastWriteTime is older than to_read_retention_days (default 14), then
  deletes files in figures\ that no remaining .md embeds. Never touches README.md or other folders.
  Run daily by queue-worker.ps1 (at most once per calendar day); safe to run by hand.

.EXAMPLE
  .\prune-to-read.ps1 -DryRun      # list what would be deleted, delete nothing
  .\prune-to-read.ps1              # delete
  .\prune-to-read.ps1 -Dir T:\toread -Days 1 -DryRun
#>
param([switch]$DryRun, [string]$Dir, [int]$Days = 0, [string]$LogFile)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'pipeline-lib.ps1')
if (-not $Dir) { $Dir = $ToReadDir }
if ($Days -le 0) { $Days = $ToReadDays }
$tag = $(if ($DryRun) { 'DRY RUN: would delete' } else { 'deleted' })
if (-not (Test-Path -LiteralPath $Dir)) { Write-Log "prune-to-read: folder not found: $Dir (nothing to do)" $LogFile; exit 0 }
$cut = (Get-Date).AddDays(-$Days)
Write-Log "prune-to-read: $Dir, retention $Days days (cut-off $($cut.ToString('yyyy-MM-dd HH:mm'))$(if ($DryRun) { ', dry run' }))" $LogFile

$mds = @(Get-ChildItem -LiteralPath $Dir -File -Filter '*.md' | Where-Object { $_.Name -ne 'README.md' })
$old = @($mds | Where-Object { $_.LastWriteTime -lt $cut })
$keep = @($mds | Where-Object { $_.LastWriteTime -ge $cut })
foreach ($f in $old) {
    Write-Log "  $tag $($f.Name) (last written $($f.LastWriteTime.ToString('yyyy-MM-dd HH:mm')))" $LogFile
    if (-not $DryRun) { Remove-Item -LiteralPath $f.FullName -Force }
}

# figures still referenced by a remaining .md (figures/<file>, relative to the folder)
$refs = New-Object 'System.Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($f in $keep) {
    try { foreach ($rel in @(Get-EmbeddedFigures $f.FullName)) { [void]$refs.Add([IO.Path]::GetFullPath((Join-Path $Dir $rel.Replace('/', '\')))) } }
    catch { Write-Log "  WARNING: could not read embeds in $($f.Name): $($_.Exception.Message); keeping all figures this run" $LogFile; $refs = $null; break }
}
$figDir = Join-Path $Dir 'figures'
$orphans = @()
if ($refs -and (Test-Path -LiteralPath $figDir)) {
    $orphans = @(Get-ChildItem -LiteralPath $figDir -File -Recurse | Where-Object { -not $refs.Contains($_.FullName) })
    foreach ($g in $orphans) {
        Write-Log "  $tag figures\$($g.FullName.Substring($figDir.Length + 1)) (not referenced by any remaining .md)" $LogFile
        if (-not $DryRun) { Remove-Item -LiteralPath $g.FullName -Force }
    }
}
Write-Log "prune-to-read: $($old.Count) .md and $($orphans.Count) figure(s) $(if ($DryRun) { 'would be deleted' } else { 'deleted' }); $($keep.Count) .md kept" $LogFile
