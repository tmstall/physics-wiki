# export_read_ids.ps1 - export "already read" paper identifiers for the phys.org picks tool.
# Read-only against the wiki; writes ONLY incoming\automation\read_ids.txt.
# Usage (from anywhere):  powershell -ExecutionPolicy Bypass -File "C:\Users\tmsta\Documents\Physics-Wiki\incoming\automation\export_read_ids.ps1"
# Output lines (tab-separated):
#   ID      <token>   <source>        token = doi-10.xxxx-... | arxiv-NNNN.NNNNN | doi:10.xxxx/... (from text)
#   TITLE   <slug>    <title>         wiki/papers slug + H1 title, and analysis filename slugs
#   RECENT  <filename>                15 most recent dated analysis filenames (for the "recent spurt" boost)
param([string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path)
$ErrorActionPreference = 'SilentlyContinue'
$out = New-Object System.Collections.Generic.List[string]
$out.Add("# generated $(Get-Date -Format s) from $Root")
$names = @()
$names += Get-ChildItem (Join-Path $Root 'raw\analyses') -File -Recurse | % { $_.Name }
$names += Get-ChildItem (Join-Path $Root 'incoming\md') -File -Recurse -Filter *.md | % { $_.Name }
$names += Get-ChildItem (Join-Path $Root 'incoming\New') -File -Recurse | % { $_.Name }
$papers = Get-ChildItem (Join-Path $Root 'wiki\papers') -File -Filter *.md
foreach ($p in $papers) {
  $head = Get-Content $p.FullName -TotalCount 25 -Encoding UTF8
  foreach ($l in $head) {
    if ($l -match '^source_analysis:\s*"?([^"]+)') { $names += (Split-Path $Matches[1] -Leaf) }
    foreach ($m in [regex]::Matches($l, '10\.\d{4,9}/[^\s"\)\],;]+')) { $out.Add("ID`tdoi:$($m.Value.TrimEnd('.'))`twiki/papers/$($p.Name)") }
    foreach ($m in [regex]::Matches($l, '(?i)arxiv[:\s/]*(\d{4}\.\d{4,5})')) { $out.Add("ID`tarxiv-$($m.Groups[1].Value)`twiki/papers/$($p.Name)") }
  }
  $t = ($head | ? { $_ -match '^# ' } | Select-Object -First 1) -replace '^# ',''
  $out.Add("TITLE`t$($p.BaseName)`t$t")
}
foreach ($n in ($names | Sort-Object -Unique)) {
  foreach ($m in [regex]::Matches($n, '(?i)(doi-10\.[^_ ]+|arxiv-\d{4}\.\d{4,5})')) { $out.Add("ID`t$($m.Value)`t$n") }
  if ($n -match '^(?:[a-z]+_)?\d{4}-\d{2}-\d{2}_[^_]+_(.+?)\.md$') { $out.Add("TITLE`t$($Matches[1])`t") }
}
Get-ChildItem (Join-Path $Root 'raw\analyses'), (Join-Path $Root 'incoming\md') -File -Recurse -Filter *.md |
  ? { $_.Name -match '^\d{4}-\d{2}-\d{2}_' } | % { $_.Name } | Sort-Object -Unique -Descending | Select-Object -First 15 |
  % { $out.Add("RECENT`t$_") }
$dest = Join-Path $Root 'incoming\automation\read_ids.txt'
[IO.File]::WriteAllLines($dest, ($out | Select-Object -Unique), (New-Object Text.UTF8Encoding $false))
Write-Output "wrote $dest ($((Get-Content $dest).Count) lines)"