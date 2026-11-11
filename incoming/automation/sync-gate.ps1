# Read-only gate for MyWiki's "Physics-Wiki GitHub sync (safety net)" routine.
# Never stages, commits, pushes, fetches, or changes anything.
# Exit 0  = nothing to do (or ingest running): routine stays silent.
# Exit 10 = scoped changes or unpushed commits: routine does its full sync.
# Exit 20 = can't see the repo or git: routine falls back to its full manual check.
param([string]$Repo = 'C:\Users\tmsta\Documents\Projects\Physics-Wiki')
$ErrorActionPreference = 'Stop'
try {
    if (-not (Test-Path (Join-Path $Repo '.git'))) { Write-Output 'GATE: repo not found'; exit 20 }
    if (Test-Path (Join-Path $Repo 'incoming\automation\queue\ingest.lock')) { Write-Output 'GATE: ingest running, skip'; exit 0 }
    Set-Location $Repo
    $lint = @(Get-ChildItem -Path $Repo -Filter 'LINT_REPORT_*.md' -File -ErrorAction SilentlyContinue | ForEach-Object { $_.Name })
    $paths = @('wiki/', 'AGENTS.md') + $lint
    $status = git status --porcelain -- $paths 2>$null
    if ($LASTEXITCODE -ne 0) { Write-Output 'GATE: git status failed'; exit 20 }
    $changed = @($status | Where-Object { $_ -and $_.Trim() }).Count
    $ahead = git rev-list --count origin/main..main 2>$null
    if ($LASTEXITCODE -ne 0) { Write-Output 'GATE: git rev-list failed'; exit 20 }
    $ahead = [int]$ahead
    Write-Output ("GATE: changed={0} ahead={1}" -f $changed, $ahead)
    if ($changed -gt 0 -or $ahead -gt 0) { exit 10 }
    exit 0
} catch {
    Write-Output ("GATE: error {0}" -f $_.Exception.Message); exit 20
}
