# run-claude.ps1 - launches the newest Claude Code exe bundled with Claude Desktop, passing all args through.
$base = Join-Path $env:LOCALAPPDATA 'Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude-code'
$exe = Get-ChildItem -Path (Join-Path $base '*\*\claude.exe') -ErrorAction SilentlyContinue |
  Sort-Object @{Expression={ try { [version]$_.Directory.Parent.Name } catch { [version]'0.0' } }}, LastWriteTime -Descending |
  Select-Object -First 1
if (-not $exe) { Write-Error "claude.exe not found under $base"; exit 1 }
& $exe.FullName @args
exit $LASTEXITCODE
