# pipeline-lib.ps1 - shared functions for the Physics-Wiki paper pipeline (Phase 3).
# Dot-source it:  . (Join-Path $PSScriptRoot 'pipeline-lib.ps1')
# Keep this file ASCII-only (Windows PowerShell 5.1 reads BOM-less scripts as ANSI).

$script:AutoDir    = $PSScriptRoot
$script:RepoRoot   = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$script:ScratchDir = Join-Path $script:AutoDir 'scratch'
$script:WorkRoot   = Join-Path $script:ScratchDir 'work'
$script:QueueDir   = Join-Path $script:AutoDir 'queue'
$script:DriveBase  = 'G:\My Drive\Technical Papers'
$script:DriveAnalyses = Join-Path $script:DriveBase 'Analyses'
$script:DriveQueue    = Join-Path $script:DriveBase 'Queue'
$script:DriveDeepDives = Join-Path $script:DriveBase 'Deep Dives'
$script:MdDir      = Join-Path $script:RepoRoot 'incoming\md'
$script:PapersLog  = Join-Path $script:AutoDir 'papers-analyzed-log.md'
$script:FrameworkDir = 'C:\Users\tmsta\Desktop\Gold\Prompts'
$script:Utf8NoBom  = New-Object System.Text.UTF8Encoding($false)
function Get-PipelineConfigValue([string]$Key, [string]$Default) {
    # Reads 'key: value' (first match, trailing '# comment' dropped) from pipeline-config.md; falls back to $Default.
    $cfg = Join-Path $script:AutoDir 'pipeline-config.md'
    if (Test-Path -LiteralPath $cfg) {
        foreach ($l in [IO.File]::ReadAllLines($cfg)) {
            if ($l -match ('^\s*' + [regex]::Escape($Key) + ':\s*([^#]+?)\s*(#.*)?$')) { return $Matches[1].Trim() }
        }
    }
    return $Default
}
# To Read: recent analyses for reading on phone/tablet (Drive -> DriveSync Pro -> Obsidian). Pruned after N days.
$script:ToReadDir  = Get-PipelineConfigValue 'to_read_dir' 'G:\My Drive\To Read'
$script:ToReadDays = [int](Get-PipelineConfigValue 'to_read_retention_days' '14')
$script:CompareRule = 'Extra rule for this run: when you compare with other papers (prior work, competing or independent results), check the latest arXiv version of each such paper via its arXiv abs page or listing (which shows the version history and the current abstract), and cite which version you used; do not rely on a tool summary of an older version. If you could only see an older version or a summary, say so explicitly.'

function Initialize-PipelineEnv {
    $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')
    try { [Console]::OutputEncoding = $script:Utf8NoBom } catch { }
    $global:OutputEncoding = $script:Utf8NoBom
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
}

function Write-Utf8File([string]$Path, [string]$Text) {
    [IO.File]::WriteAllText($Path, $Text, $script:Utf8NoBom)
}
function Add-Utf8Line([string]$Path, [string]$Line) {
    [IO.File]::AppendAllText($Path, $Line + "`r`n", $script:Utf8NoBom)
}
function Write-Log([string]$Msg, [string]$LogFile) {
    $line = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss') + '  ' + $Msg
    Write-Host $line
    if ($LogFile) { try { Add-Utf8Line $LogFile $line } catch { } }
}

# ---------- paper references and metadata ----------

function Resolve-PaperRef([string]$Ref) {
    $r = $Ref.Trim()
    $o = [ordered]@{ input = $r; arxiv = $null; doi = $null }
    if ($r -match '(?i)arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5})') { $o.arxiv = $Matches[1] }
    elseif ($r -match '(?i)^(?:arxiv:\s*)?([0-9]{4}\.[0-9]{4,5})(?:v\d+)?$') { $o.arxiv = $Matches[1] }
    elseif ($r -match '(?i)10\.48550/arxiv\.([0-9]{4}\.[0-9]{4,5})') { $o.arxiv = $Matches[1] }
    elseif ($r -match '(?i)(10\.\d{4,9}/[^\s"<>?#]+)') { $o.doi = $Matches[1].TrimEnd('.', ')', ']', ',') }
    return [pscustomobject]$o
}

function Get-IdLabel($Meta) {
    if ($Meta.arxiv) { return 'arxiv-' + $Meta.arxiv }
    if ($Meta.doi) { return 'doi-' + (($Meta.doi -replace '[^A-Za-z0-9.\-]', '-')) }
    if ($Meta.slug) { return [string]$Meta.slug }
    return 'paper-' + (Get-Date -Format 'HHmmss')
}

function Get-Slug([string]$Title, [int]$MaxWords = 7) {
    $stop = @('a','an','the','of','in','on','for','and','or','to','with','by','at','from','as','is','are','via','its','into','using')
    $w = ($Title.ToLowerInvariant() -replace '[^a-z0-9 ]', ' ') -split '\s+' | Where-Object { $_ -and ($stop -notcontains $_) }
    $s = ($w | Select-Object -First $MaxWords) -join '-'
    if (-not $s) { $s = 'paper' }
    return $s
}

function Get-ArxivEntry([string]$Query) {
    $url = 'https://export.arxiv.org/api/query?' + $Query
    $resp = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 60 -UserAgent 'physics-wiki-pipeline/1.0'
    [xml]$x = $resp.Content
    $ns = New-Object Xml.XmlNamespaceManager($x.NameTable)
    $ns.AddNamespace('a', 'http://www.w3.org/2005/Atom')
    $ns.AddNamespace('ax', 'http://arxiv.org/schemas/atom')
    $out = @()
    foreach ($e in $x.SelectNodes('//a:entry', $ns)) {
        $idUrl = $e.SelectSingleNode('a:id', $ns).InnerText
        if ($idUrl -notmatch 'abs/([0-9]{4}\.[0-9]{4,5})v(\d+)') { continue }
        $doiNode = $e.SelectSingleNode('ax:doi', $ns); $jrNode = $e.SelectSingleNode('ax:journal_ref', $ns)
        $out += [pscustomobject]@{
            arxiv = $Matches[1]; version = [int]$Matches[2]
            title = (($e.SelectSingleNode('a:title', $ns).InnerText) -replace '\s+', ' ').Trim()
            authors = @($e.SelectNodes('a:author/a:name', $ns) | ForEach-Object { $_.InnerText })
            doi = $(if ($doiNode) { $doiNode.InnerText } else { $null })
            journal = $(if ($jrNode) { $jrNode.InnerText } else { $null })
        }
    }
    return $out
}

function Get-PaperMeta([string]$Ref, [string]$Title) {
    $p = Resolve-PaperRef $Ref
    $m = [ordered]@{ input = $Ref; arxiv = $p.arxiv; doi = $p.doi; version = $null; title = $Title; authors = @(); journal = $null; notes = @() }
    if (-not $p.arxiv -and -not $p.doi) { throw "Could not read an arXiv ID or DOI from '$Ref'. Give an arXiv ID/URL or a DOI/doi.org URL." }
    if ($p.doi -and -not $p.arxiv) {
        try {
            $cr = Invoke-RestMethod -Uri ('https://api.crossref.org/works/' + [uri]::EscapeDataString($p.doi)) -TimeoutSec 60 -UserAgent 'physics-wiki-pipeline/1.0 (mailto:none)'
            if (-not $m.title -and $cr.message.title) { $m.title = [string]$cr.message.title[0] }
            if ($cr.message.author) { $m.authors = @($cr.message.author | ForEach-Object { ($_.given + ' ' + $_.family).Trim() }) }
            if ($cr.message.'container-title') { $m.journal = [string]$cr.message.'container-title'[0] }
            $pre = $cr.message.relation.'has-preprint'
            foreach ($r in @($pre)) { if ($r.id -match '([0-9]{4}\.[0-9]{4,5})') { $m.arxiv = $Matches[1]; $m.notes += 'arXiv ID from Crossref has-preprint' ; break } }
        } catch { $m.notes += "Crossref lookup failed: $($_.Exception.Message)" }
        if (-not $m.arxiv -and $m.title) {
            try {
                $words = (($m.title -replace '[^A-Za-z0-9 ]', ' ') -split '\s+' | Where-Object { $_.Length -gt 3 } | Select-Object -First 8)
                $q = 'search_query=' + [uri]::EscapeDataString((($words | ForEach-Object { 'ti:' + $_ }) -join ' AND ')) + '&max_results=5'
                $norm = { param($t) (($t.ToLowerInvariant()) -replace '[^a-z0-9]', '') }
                foreach ($e in (Get-ArxivEntry $q)) {
                    if ((& $norm $e.title) -eq (& $norm $m.title) -or ($e.doi -and $e.doi -ieq $p.doi)) { $m.arxiv = $e.arxiv; $m.notes += 'arXiv ID found by exact title match'; break }
                }
            } catch { $m.notes += "arXiv title search failed: $($_.Exception.Message)" }
        }
    }
    if ($m.arxiv) {
        $e = @(Get-ArxivEntry ('id_list=' + $m.arxiv)) | Select-Object -First 1
        if ($e) {
            $m.version = $e.version
            if (-not $Title) { $m.title = $e.title }
            if ($e.authors.Count) { $m.authors = $e.authors }
            if ($e.doi -and -not $m.doi) { $m.doi = $e.doi }
            if ($e.journal) { $m.journal = $e.journal }
        } else { $m.notes += 'arXiv API returned no entry' }
    }
    if (-not $m.title) { $m.title = '(title unknown)' }
    return [pscustomobject]$m
}

# ---------- duplicate check ----------

function Find-PaperDuplicates($Meta, [string]$LogFile = $script:PapersLog, [string[]]$Dirs) {
    if (-not $Dirs) { $Dirs = @((Join-Path $script:RepoRoot 'wiki\papers'), (Join-Path $script:RepoRoot 'raw\analyses'), $script:MdDir) }
    $patterns = @()
    if ($Meta.arxiv) { $patterns += $Meta.arxiv }
    if ($Meta.doi) { $patterns += $Meta.doi; $patterns += ('doi-' + ($Meta.doi -replace '[^A-Za-z0-9.\-]', '-')) }
    $namePats = @()
    if ($Meta.arxiv) { $namePats += ('arxiv-' + $Meta.arxiv) }
    if ($Meta.doi) { $namePats += ('doi-' + ($Meta.doi -replace '[^A-Za-z0-9.\-]', '-')) }
    if ($Meta.slug) { $namePats += [string]$Meta.slug; $patterns += [string]$Meta.slug }
    $titlePat = $null
    if ($Meta.title -and $Meta.title.Length -ge 25 -and $Meta.title -ne '(title unknown)') { $titlePat = $Meta.title }
    $hits = New-Object System.Collections.ArrayList
    $files = @()
    foreach ($d in $Dirs) { if (Test-Path $d) { $files += Get-ChildItem -Path $d -Recurse -File -Filter *.md -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\\.obsidian\\' } } }
    foreach ($f in $files) {
        foreach ($np in $namePats) { if ($f.Name.IndexOf($np, [StringComparison]::OrdinalIgnoreCase) -ge 0) { [void]$hits.Add([pscustomobject]@{ strength = 'strong'; path = $f.FullName; line = 0; why = "filename contains $np" }) } }
    }
    $allPats = @($patterns); if ($titlePat) { $allPats += $titlePat }
    if ($allPats.Count -and $files.Count) {
        $ss = $files | Select-String -SimpleMatch -Encoding UTF8 -Pattern $allPats -ErrorAction SilentlyContinue
        foreach ($s in $ss) {
            $isTitle = $titlePat -and ($s.Line.IndexOf($titlePat, [StringComparison]::OrdinalIgnoreCase) -ge 0)
            $strength = $(if ($isTitle -or $s.LineNumber -le 40) { 'strong' } else { 'weak' })
            $snip = $s.Line.Trim(); if ($snip.Length -gt 160) { $snip = $snip.Substring(0, 160) }
            [void]$hits.Add([pscustomobject]@{ strength = $strength; path = $s.Path; line = $s.LineNumber; why = $(if ($isTitle) { 'title match: ' } else { 'id match: ' }) + $snip })
        }
    }
    if ($LogFile -and (Test-Path $LogFile) -and $allPats.Count) {
        foreach ($s in (Select-String -Path $LogFile -SimpleMatch -Pattern $allPats -ErrorAction SilentlyContinue)) {
            [void]$hits.Add([pscustomobject]@{ strength = 'strong'; path = $s.Path; line = $s.LineNumber; why = 'papers log row' })
        }
    }
    # one entry per file, strongest first
    $byFile = $hits | Group-Object path | ForEach-Object { $_.Group | Sort-Object @{ e = { if ($_.strength -eq 'strong') { 0 } else { 1 } } } | Select-Object -First 1 }
    return @($byFile)
}

# ---------- PDF download ----------

function Get-ArxivPdf($Meta, [string]$WorkDir) {
    $ErrorActionPreference = 'Continue'   # native stderr must not throw
    $v = $(if ($Meta.version) { 'v' + $Meta.version } else { '' })
    $pdf = Join-Path $WorkDir ('arxiv-' + $Meta.arxiv + $v + '.pdf')
    Invoke-WebRequest -Uri ('https://arxiv.org/pdf/' + $Meta.arxiv + $v) -OutFile $pdf -UseBasicParsing -TimeoutSec 180 -UserAgent 'Mozilla/5.0 (physics-wiki-pipeline)'
    $len = (Get-Item $pdf).Length
    $head = [Text.Encoding]::ASCII.GetString([IO.File]::ReadAllBytes($pdf), 0, [Math]::Min(5, $len))
    if ($len -lt 20000 -or $head -ne '%PDF-') { throw "Downloaded file is not a valid PDF ($len bytes)" }
    $pages = $null; $txt = $null
    if (Get-Command pdfinfo -ErrorAction SilentlyContinue) {
        $info = & pdfinfo $pdf 2>$null
        $pl = $info | Where-Object { $_ -match '^Pages:\s+(\d+)' } | Select-Object -First 1
        if ($pl -match '(\d+)') { $pages = [int]$Matches[1] }
    }
    if (Get-Command pdftotext -ErrorAction SilentlyContinue) {
        $txt = [IO.Path]::ChangeExtension($pdf, $null).TrimEnd('.') + '_fulltext.txt'
        & pdftotext -layout $pdf $txt 2>$null
        if (-not (Test-Path $txt)) { $txt = $null }
    }
    return [pscustomobject]@{ pdf = $pdf; bytes = $len; pages = $pages; txt = $txt }
}

function Get-LocalPdf([string]$Path, [string]$WorkDir, [string]$Slug) {
    # -LocalPdf runs: verified copy into the work dir; scanned = no usable text layer (page images only)
    $ErrorActionPreference = 'Continue'   # native stderr must not throw
    $head = [Text.Encoding]::ASCII.GetString((Get-FileHead $Path 5))
    if ($head -ne '%PDF-') { throw "Not a PDF: $Path" }
    $pdf = Join-Path $WorkDir ($Slug + '.pdf')
    $len = Copy-Verified $Path $pdf
    $pages = $null; $txt = $null; $scanned = $null
    if (Get-Command pdfinfo -ErrorAction SilentlyContinue) {
        $info = & pdfinfo $pdf 2>$null
        $pl = $info | Where-Object { $_ -match '^Pages:\s+(\d+)' } | Select-Object -First 1
        if ($pl -match '(\d+)') { $pages = [int]$Matches[1] }
    }
    if (Get-Command pdftotext -ErrorAction SilentlyContinue) {
        $txt = [IO.Path]::ChangeExtension($pdf, $null).TrimEnd('.') + '_fulltext.txt'
        & pdftotext -layout $pdf $txt 2>$null
        if (-not (Test-Path $txt)) { $txt = $null }
        $chars = $(if ($txt) { ([IO.File]::ReadAllText($txt) -replace '\s', '').Length } else { 0 })
        $scanned = ($chars -lt 200 -or ($pages -and $chars -lt 100 * $pages))
    }
    return [pscustomobject]@{ pdf = $pdf; bytes = $len; pages = $pages; txt = $txt; scanned = $scanned }
}

# ---------- figures (arXiv source first, then PDF page renders / embedded images) ----------
# Output: <work>\figures\ with <prefix>_figN.png (N = figure number), pages\page-NN.png, pdfimages\, FIGURES.md.
# The analysis embeds them as figures/<file>; delivery copies the embedded ones to incoming\md\figures\ and Drive.

function Get-FigurePrefix($Meta) {
    if ($Meta.slug) { return [string]$Meta.slug }
    $w = Get-Slug "$($Meta.title)" 1
    if (-not $w -or $w -eq 'title') { $w = 'paper' }
    $id = $(if ($Meta.arxiv) { $Meta.arxiv } elseif ($Meta.doi) { ($Meta.doi -replace '[^A-Za-z0-9.\-]', '-') } else { Get-Date -Format 'HHmmss' })
    return ($w + '-' + $id)
}

function Get-FileHead([string]$Path, [int]$Count) {
    $fs = [IO.File]::OpenRead($Path)
    try { $b = New-Object byte[] $Count; $n = $fs.Read($b, 0, $Count); return $b[0..([Math]::Max(0, $n - 1))] } finally { $fs.Close() }
}

function Get-PngSize([string]$Path) {
    try {
        $b = Get-FileHead $Path 24
        if ($b.Count -lt 24 -or $b[1] -ne 0x50 -or $b[2] -ne 0x4E -or $b[3] -ne 0x47) { return $null }
        $w = ([int]$b[16] -shl 24) -bor ([int]$b[17] -shl 16) -bor ([int]$b[18] -shl 8) -bor [int]$b[19]
        $h = ([int]$b[20] -shl 24) -bor ([int]$b[21] -shl 16) -bor ([int]$b[22] -shl 8) -bor [int]$b[23]
        return [pscustomobject]@{ w = $w; h = $h }
    } catch { return $null }
}

function Remove-TexComments([string]$Text) { return [regex]::Replace($Text, '(?m)(?<!\\)%.*$', '') }

function Expand-TexInputs([string]$Text, [string]$Dir, [int]$Depth = 0) {
    if ($Depth -gt 3) { return $Text }
    $ev = [Text.RegularExpressions.MatchEvaluator] {
        param($m)
        $n = $m.Groups[1].Value.Trim()
        foreach ($c in @($n, ($n + '.tex'))) {
            $p = Join-Path $Dir $c
            if (Test-Path -LiteralPath $p -PathType Leaf) { return (Expand-TexInputs (Remove-TexComments ([IO.File]::ReadAllText($p))) $Dir ($Depth + 1)) }
        }
        return $m.Value
    }
    return [regex]::Replace($Text, '\\(?:input|include)\s*\{([^}]+)\}', $ev)
}

function Get-TexBraceArg([string]$Text, [int]$Start) {
    # Text[Start] must be '{'; returns the balanced content
    if ($Start -lt 0 -or $Start -ge $Text.Length -or $Text[$Start] -ne '{') { return $null }
    $depth = 0
    for ($i = $Start; $i -lt $Text.Length; $i++) {
        $ch = $Text[$i]
        if ($ch -eq '\') { $i++; continue }
        if ($ch -eq '{') { $depth++ } elseif ($ch -eq '}') { $depth--; if ($depth -eq 0) { return $Text.Substring($Start + 1, $i - $Start - 1) } }
    }
    return $null
}

function ConvertTo-PlainCaption([string]$Tex, [int]$Max = 240) {
    $s = [regex]::Replace($Tex, '\\label\s*\{[^}]*\}', '')
    $s = [regex]::Replace($s, '\\(?:cite[tp]?|ref|eqref)\s*\{[^}]*\}', '[ref]')
    $s = [regex]::Replace($s, '\\[A-Za-z]+\*?', ' ')
    $s = ($s -replace '[{}$~\\]', ' ' -replace '\s+', ' ').Trim()
    if ($s.Length -gt $Max) { $s = $s.Substring(0, $Max) + '...' }
    return $s.Replace('|', '/')
}

function Resolve-TexGraphic([string]$Ref, [string]$SrcDir) {
    $r = $Ref.Trim().Trim('"').Replace('/', '\').TrimStart('.', '\')
    if ($r -match '\.\.') { return $null }
    $exts = @('', '.pdf', '.png', '.jpg', '.jpeg', '.eps', '.ps')
    foreach ($e in $exts) { $p = Join-Path $SrcDir ($r + $e); if (Test-Path -LiteralPath $p -PathType Leaf) { return (Get-Item -LiteralPath $p) } }
    $leaf = Split-Path $r -Leaf
    $all = @(Get-ChildItem -LiteralPath $SrcDir -Recurse -File -ErrorAction SilentlyContinue)
    foreach ($e in $exts) { $hit = $all | Where-Object { $_.Name -ieq ($leaf + $e) } | Select-Object -First 1; if ($hit) { return $hit } }
    return $null
}

function Convert-FigureFile($File, [string]$OutBase) {
    $ErrorActionPreference = 'Continue'
    $ext = $File.Extension.ToLowerInvariant()
    if ($ext -eq '.png') { Copy-Item -LiteralPath $File.FullName -Destination ($OutBase + '.png') -Force; return ($OutBase + '.png') }
    if ($ext -eq '.jpg' -or $ext -eq '.jpeg') { Copy-Item -LiteralPath $File.FullName -Destination ($OutBase + '.jpg') -Force; return ($OutBase + '.jpg') }
    if ($ext -eq '.pdf' -and (Get-Command pdftoppm -ErrorAction SilentlyContinue)) {
        & pdftoppm -png -scale-to 1600 -f 1 -l 1 -singlefile $File.FullName $OutBase 2>$null
        if (Test-Path -LiteralPath ($OutBase + '.png')) { return ($OutBase + '.png') }
    }
    return $null   # .eps/.ps (no Ghostscript) or a failed render: use the page render instead
}

function Get-TexFigures([string]$SrcDir, [string]$FigDir, [string]$Prefix) {
    $rows = @()
    $main = $null
    $readme = Join-Path $SrcDir '00README.json'
    if (Test-Path -LiteralPath $readme) {
        try {
            $j = [IO.File]::ReadAllText($readme) | ConvertFrom-Json
            $tl = @($j.sources | Where-Object { $_.usage -eq 'toplevel' }) | Select-Object -First 1
            if ($tl) { $p = Join-Path $SrcDir $tl.filename; if (Test-Path -LiteralPath $p) { $main = Get-Item -LiteralPath $p } }
        } catch { }
    }
    if (-not $main) {
        $main = Get-ChildItem -LiteralPath $SrcDir -Recurse -File -Filter *.tex -ErrorAction SilentlyContinue |
            Where-Object { [IO.File]::ReadAllText($_.FullName) -match '\\documentclass' } | Sort-Object Length -Descending | Select-Object -First 1
    }
    if (-not $main) { return $rows }
    $tex = Expand-TexInputs (Remove-TexComments ([IO.File]::ReadAllText($main.FullName))) $main.DirectoryName
    $n = 0
    foreach ($m in [regex]::Matches($tex, '\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}', 'Singleline')) {
        $n++
        $body = $m.Groups[1].Value
        $refs = @()
        foreach ($g in [regex]::Matches($body, '\\includegraphics\*?\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}')) { $refs += $g.Groups[1].Value }
        foreach ($g in [regex]::Matches($body, '\\(?:plotone|fig)\s*\{([^}]+)\}')) { $refs += $g.Groups[1].Value }
        foreach ($g in [regex]::Matches($body, '\\plottwo\s*\{([^}]+)\}\s*\{([^}]+)\}')) { $refs += $g.Groups[1].Value; $refs += $g.Groups[2].Value }
        $cap = ''
        $ci = $body.IndexOf('\caption')
        if ($ci -ge 0) {
            $k = $ci + 8
            while ($k -lt $body.Length -and ($body[$k] -eq ' ' -or $body[$k] -eq '*')) { $k++ }
            if ($k -lt $body.Length -and $body[$k] -eq '[') { $k = $body.IndexOf(']', $k) + 1; while ($k -lt $body.Length -and $body[$k] -eq ' ') { $k++ } }
            $arg = Get-TexBraceArg $body $k
            if ($arg) { $cap = ConvertTo-PlainCaption $arg }
        }
        $label = $(if ($body -match '\\label\s*\{([^}]+)\}') { $Matches[1] } else { '' })
        $files = @(); $missing = @()
        for ($i = 0; $i -lt $refs.Count; $i++) {
            $suffix = $(if ($refs.Count -gt 1) { [string][char](97 + [Math]::Min($i, 25)) } else { '' })
            $f = Resolve-TexGraphic $refs[$i] $SrcDir
            $out = $null
            if ($f) { $out = Convert-FigureFile $f (Join-Path $FigDir ('{0}_fig{1}{2}' -f $Prefix, $n, $suffix)) }
            if ($out) { $files += (Split-Path $out -Leaf) } else { $missing += $refs[$i] }
        }
        $rows += [pscustomobject]@{ fig = $n; files = $files; missing = $missing; caption = $cap; label = $label }
    }
    return $rows
}

function Get-PaperFigures($Meta, $PdfInfo, [string]$WorkDir, [string]$Prefix) {
    $ErrorActionPreference = 'Continue'   # native stderr must not throw
    $figDir = Join-Path $WorkDir 'figures'
    New-Item -ItemType Directory -Path $figDir -Force | Out-Null
    $res = [ordered]@{ dir = $figDir; prefix = $Prefix; manifest = (Join-Path $figDir 'FIGURES.md'); source = 'none'; figures = @(); pages = @(); pdfimages = @(); notes = @() }
    # 1. arXiv source tarball: the authors' own figure files are the best copies
    if ($Meta.arxiv) {
        $v = $(if ($Meta.version) { 'v' + $Meta.version } else { '' })
        $bin = Join-Path $WorkDir 'arxiv-source.bin'; $srcDir = Join-Path $WorkDir 'src'
        try {
            Invoke-WebRequest -Uri ('https://arxiv.org/e-print/' + $Meta.arxiv + $v) -OutFile $bin -UseBasicParsing -TimeoutSec 180 -UserAgent 'Mozilla/5.0 (physics-wiki-pipeline)'
            $hd = [Text.Encoding]::ASCII.GetString((Get-FileHead $bin 5))
            if ($hd -eq '%PDF-') { $res.notes += 'arXiv has no LaTeX source for this paper (PDF-only submission)' }
            else {
                New-Item -ItemType Directory -Path $srcDir -Force | Out-Null
                & tar -xf $bin -C $srcDir 2>$null
                if (-not @(Get-ChildItem -LiteralPath $srcDir -Recurse -File -ErrorAction SilentlyContinue).Count) { $res.notes += 'arXiv source is a single file, not an archive (no figure files)' }
            }
        } catch { $res.notes += "arXiv source download failed: $($_.Exception.Message)" }
        if ((Test-Path -LiteralPath $srcDir) -and @(Get-ChildItem -LiteralPath $srcDir -Recurse -File -ErrorAction SilentlyContinue).Count) {
            try { $res.figures = @(Get-TexFigures $srcDir $figDir $Prefix) } catch { $res.notes += "LaTeX figure parse failed: $($_.Exception.Message)" }
            if (@($res.figures | Where-Object { $_.files.Count }).Count) { $res.source = 'arXiv source (' + $srcDir + ')' }
            foreach ($r in $res.figures) { if ($r.missing.Count) { $res.notes += "Fig. $($r.fig): not converted ($($r.missing -join ', ')) - use the page render" } }
        }
    }
    # 2. page renders of the pages that carry figure captions (context + crop source)
    if ($PdfInfo -and $PdfInfo.pdf -and (Get-Command pdftoppm -ErrorAction SilentlyContinue)) {
        $capPages = @{}
        if ($PdfInfo.txt -and (Test-Path -LiteralPath $PdfInfo.txt)) {
            $pg = [IO.File]::ReadAllText($PdfInfo.txt) -split "`f"
            for ($i = 0; $i -lt $pg.Count; $i++) {
                foreach ($cm in [regex]::Matches($pg[$i], '(?m)(?:^|\s{2,})(?:FIG\.|Fig\.|FIGURE|Figure)\s*(\d+)\s*[\.:|]')) {
                    $p = $i + 1; if (-not $capPages.ContainsKey($p)) { $capPages[$p] = @() }
                    if ($capPages[$p] -notcontains $cm.Groups[1].Value) { $capPages[$p] += $cm.Groups[1].Value }
                }
            }
        }
        $pagesDir = Join-Path $figDir 'pages'
        New-Item -ItemType Directory -Path $pagesDir -Force | Out-Null
        foreach ($p in (@($capPages.Keys) | Sort-Object | Select-Object -First 20)) {
            $base = Join-Path $pagesDir ('page-{0:D2}' -f $p)
            & pdftoppm -png -r 150 -f $p -l $p -singlefile $PdfInfo.pdf $base 2>$null
            if (Test-Path -LiteralPath ($base + '.png')) { $res.pages += [pscustomobject]@{ page = $p; file = ('pages/page-{0:D2}.png' -f $p); figs = ($capPages[$p] -join ', ') } }
        }
        # 3. raw embedded images, only when the source gave no figure files (often fragments; filtered by size)
        if (-not @($res.figures | Where-Object { $_.files.Count }).Count -and (Get-Command pdfimages -ErrorAction SilentlyContinue)) {
            $rawDir = Join-Path $figDir 'pdfimages'
            New-Item -ItemType Directory -Path $rawDir -Force | Out-Null
            & pdfimages -png -p $PdfInfo.pdf (Join-Path $rawDir 'img') 2>$null
            foreach ($f in @(Get-ChildItem -LiteralPath $rawDir -File -Filter *.png -ErrorAction SilentlyContinue)) {
                $s = Get-PngSize $f.FullName
                if (-not $s -or $s.w -lt 300 -or $s.h -lt 200 -or $f.Length -lt 15000) { Remove-Item -LiteralPath $f.FullName -Force }
                else { $res.pdfimages += ('pdfimages/' + $f.Name + " ($($s.w)x$($s.h))") }
            }
            if (-not $capPages.Count) {
                # no captions found in the text either: render the pages that hold large images
                $imgPages = @($res.pdfimages | ForEach-Object { if ($_ -match 'img-(\d+)-') { [int]$Matches[1] } } | Select-Object -Unique | Select-Object -First 20)
                foreach ($p in $imgPages) {
                    $base = Join-Path $pagesDir ('page-{0:D2}' -f $p)
                    & pdftoppm -png -r 150 -f $p -l $p -singlefile $PdfInfo.pdf $base 2>$null
                    if (Test-Path -LiteralPath ($base + '.png')) { $res.pages += [pscustomobject]@{ page = $p; file = ('pages/page-{0:D2}.png' -f $p); figs = '?' } }
                }
            }
        }
    }
    # 4. manifest for Claude
    $L = New-Object System.Collections.Generic.List[string]
    $L.Add("# Figures for: $($Meta.title)"); $L.Add('')
    $L.Add("Folder: $figDir"); $L.Add("File-name prefix: $Prefix (embed in the analysis as figures/<file name>)"); $L.Add("Figure-file source: $($res.source)"); $L.Add('')
    $L.Add('## Figure files'); $L.Add('')
    if (@($res.figures).Count) {
        $L.Add('Numbered by the order of figure environments in the LaTeX source, which normally matches the published numbering; check it against the captions in the PDF (appendix figures may be numbered differently). Vector figures were rendered to PNG (longest side 1600 px).'); $L.Add('')
        $L.Add('| Fig. | file(s) | LaTeX label | caption (start) |'); $L.Add('| --- | --- | --- | --- |')
        foreach ($r in $res.figures) { $L.Add('| ' + $r.fig + ' | ' + $(if ($r.files.Count) { $r.files -join ', ' } else { '(not converted: ' + ($r.missing -join ', ') + ')' }) + ' | ' + $r.label + ' | ' + $r.caption + ' |') }
    } else { $L.Add('None from the arXiv source. Use the page renders below (crop the figure out with Python/Pillow, see ANALYZE_HEADLESS.md section 5) or the raw embedded images.') }
    $L.Add(''); $L.Add('## Page renders (150 dpi; pages whose text has a figure caption)'); $L.Add('')
    if (@($res.pages).Count) { $L.Add('| page | file | captions found on page |'); $L.Add('| --- | --- | --- |'); foreach ($p in $res.pages) { $L.Add('| ' + $p.page + ' | ' + $p.file + ' | ' + $p.figs + ' |') } } else { $L.Add('None.') }
    if (@($res.pdfimages).Count) { $L.Add(''); $L.Add('## Raw embedded images (pdfimages; name = img-<page>-<n>; may be fragments or panels)'); $L.Add(''); foreach ($x in $res.pdfimages) { $L.Add('- ' + $x) } }
    if (@($res.notes).Count) { $L.Add(''); $L.Add('## Notes'); $L.Add(''); foreach ($x in $res.notes) { $L.Add('- ' + $x) } }
    Write-Utf8File $res.manifest (($L -join "`r`n") + "`r`n")
    return [pscustomobject]$res
}

function Get-EmbeddedFigures([string]$Path) {
    # Relative image embeds of the form ![..](figures/...) or ![[figures/...]] in an analysis
    $t = [IO.File]::ReadAllText($Path)
    $rels = @()
    foreach ($m in [regex]::Matches($t, '!\[[^\]]*\]\(\s*<?(figures/[^)>\s]+)>?(?:\s+"[^"]*")?\s*\)')) { $rels += $m.Groups[1].Value }
    foreach ($m in [regex]::Matches($t, '!\[\[(figures/[^\]|#]+)')) { $rels += $m.Groups[1].Value }
    $out = @()
    foreach ($r in ($rels | ForEach-Object { [uri]::UnescapeDataString($_) } | Select-Object -Unique)) {
        if ($r -match '\.\.|[:*?"<>|]') { throw "Unsafe figure path in analysis: $r" }
        $out += $r
    }
    return $out
}

# ---------- Claude Code run ----------

function Invoke-ClaudeRun([string]$Prompt, [string]$JsonlPath, [string[]]$ExtraAddDirs) {
    $ErrorActionPreference = 'Continue'   # native stderr must not throw
    # Windows PowerShell 5.1 does not escape embedded double quotes for native exes: strip them.
    $Prompt = $Prompt.Replace('"', "'")
    $scratchRule = '//c/Users/tmsta/Documents/Physics-Wiki/incoming/automation/scratch/**'
    $claudeArgs = @('-p', $Prompt, '--model', 'opus', '--verbose', '--output-format', 'stream-json', '--permission-mode', 'dontAsk',
        '--add-dir', $script:FrameworkDir)
    foreach ($d in $ExtraAddDirs) { $claudeArgs += @('--add-dir', $d) }
    $claudeArgs += @('--allowedTools', 'WebFetch', 'WebSearch', 'Read', 'Glob', 'Grep',
        "Write($scratchRule)", "Edit($scratchRule)",
        'Bash(python:*)', 'Bash(python *)', 'PowerShell(python *)', 'PowerShell(python:*)')
    $runner = Join-Path $script:AutoDir 'run-claude.ps1'
    $start = Get-Date
    Push-Location $script:RepoRoot
    try {
        & $runner @claudeArgs 2>&1 | ForEach-Object { "$_" } | Out-File $JsonlPath -Encoding utf8
        $code = $LASTEXITCODE
    } finally { Pop-Location }
    $res = Read-ClaudeJsonl $JsonlPath
    $res | Add-Member -NotePropertyName exitCode -NotePropertyValue $code -Force
    $res | Add-Member -NotePropertyName elapsed -NotePropertyValue ((Get-Date) - $start).ToString('hh\:mm\:ss') -Force
    return $res
}

function Read-ClaudeJsonl([string]$JsonlPath) {
    $r = [ordered]@{ result = $null; isError = $false; costUsd = $null; durationMs = $null; turns = $null; model = $null
        usageFirst = $null; usageLast = $null; limitHit = $false; resetsAt = $null; denials = @(); writes = @(); rawErrors = @() }
    if (-not (Test-Path $JsonlPath)) { $r.isError = $true; $r.rawErrors += 'no jsonl'; return [pscustomobject]$r }
    foreach ($line in [IO.File]::ReadLines($JsonlPath)) {
        if ($line.Length -lt 2 -or $line[0] -ne '{') {
            if ($line -match '(?i)usage limit|hit your limit|limit reached|rate limit') { $r.limitHit = $true; $r.rawErrors += $line }
            elseif ($line -match '(?i)error') { $r.rawErrors += $line }
            continue
        }
        if ($line.Contains('"rate_limit_event"')) {
            try {
                $j = $line | ConvertFrom-Json
                $w = $j.rate_limit_info.unifiedWindows
                $u = [pscustomobject]@{ fiveHour = $w.five_hour.utilization; weekly = $w.seven_day.utilization; status = $j.rate_limit_info.status; resetsAt = $j.rate_limit_info.resetsAt }
                if (-not $r.usageFirst) { $r.usageFirst = $u }
                $r.usageLast = $u
                if ($u.status -and $u.status -ne 'allowed' -and $u.status -ne 'allowed_warning') { $r.limitHit = $true; $r.resetsAt = $u.resetsAt }
            } catch { }
        }
        elseif ($line.Contains('"type":"result"')) {
            try {
                $j = $line | ConvertFrom-Json
                $r.result = $j.result; $r.isError = [bool]$j.is_error; $r.costUsd = $j.total_cost_usd; $r.durationMs = $j.duration_ms; $r.turns = $j.num_turns
                if ($j.modelUsage) { $r.model = ($j.modelUsage.PSObject.Properties.Name | Where-Object { $_ -match 'opus|sonnet' } | Select-Object -First 1) }
                if ($j.permission_denials) { $r.denials = @($j.permission_denials) }
                if ($r.isError -and ("$($j.result)" -match '(?i)usage limit|hit your limit|limit reached|rate limit|out of (extra )?usage')) { $r.limitHit = $true }
                if ("$($j.api_error_status)" -eq '429') { $r.limitHit = $true }
            } catch { }
        }
        elseif ($line.Contains('"type":"assistant"') -and $line.Contains('"name":"Write"')) {
            try {
                $j = $line | ConvertFrom-Json
                foreach ($c in @($j.message.content)) { if ($c.type -eq 'tool_use' -and $c.name -eq 'Write') { $r.writes += [pscustomobject]@{ path = $c.input.file_path; content = $c.input.content } } }
            } catch { }
        }
        elseif (-not $r.model -and $line.Contains('"subtype":"init"')) {
            try { $r.model = ($line | ConvertFrom-Json).model } catch { }
        }
    }
    return [pscustomobject]$r
}

function Restore-AnalysisFromJsonl($Run, [string]$WorkDir) {
    # Recover the analysis text when the Write was blocked: permission_denials first, then any Write tool_use.
    $cands = @()
    foreach ($d in $Run.denials) { if ($d.tool_name -eq 'Write' -and "$($d.tool_input.file_path)" -match '\.md$') { $cands += [pscustomobject]@{ path = $d.tool_input.file_path; content = $d.tool_input.content } } }
    foreach ($w in $Run.writes) { if ("$($w.path)" -match '\.md$') { $cands += $w } }
    $best = $cands | Where-Object { $_.content -and $_.content.Length -gt 5000 } | Select-Object -Last 1
    if (-not $best) { return $null }
    $leaf = Split-Path $best.path -Leaf
    $dest = Join-Path $WorkDir $leaf
    Write-Utf8File $dest $best.content
    return $dest
}

function Get-WordCount([string]$Path) {
    $t = [IO.File]::ReadAllText($Path)
    return @([regex]::Matches($t, '[\p{L}\p{N}][\p{L}\p{N}''\-\.]*')).Count
}

# ---------- delivery ----------

function Copy-Verified([string]$Src, [string]$Dest) {
    $parent = Split-Path $Dest
    if ($parent -and -not (Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Path $parent -Force | Out-Null }
    Copy-Item -LiteralPath $Src -Destination $Dest -Force
    $a = (Get-Item -LiteralPath $Src).Length; $b = (Get-Item -LiteralPath $Dest).Length
    if ($a -ne $b) { throw "Size mismatch after copy: $Src ($a) -> $Dest ($b)" }
    $ha = (Get-FileHash -LiteralPath $Src -Algorithm SHA256).Hash; $hb = (Get-FileHash -LiteralPath $Dest -Algorithm SHA256).Hash
    if ($ha -ne $hb) { throw "Hash mismatch after copy: $Src -> $Dest" }
    return $b
}

function Wait-DriveMount([string]$Dir, [int]$Seconds = 120) {
    $root = [IO.Path]::GetPathRoot($Dir)
    if (Test-Path $root) { return $true }
    $exe = Get-ChildItem 'C:\Program Files\Google\Drive File Stream\*\GoogleDriveFS.exe' -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($exe -and -not (Get-Process GoogleDriveFS -ErrorAction SilentlyContinue)) { Start-Process $exe.FullName }
    $t = 0; while ($t -lt $Seconds) { Start-Sleep 5; $t += 5; if (Test-Path $root) { Start-Sleep 5; return $true } }
    return $false
}

function Copy-ToRead([string]$MdFile, [string]$ToReadDir = $script:ToReadDir, [string]$Name) {
    # Copies an analysis .md (optionally under a new name) and the images it embeds (figures/<file>, relative
    # to the .md) into the To Read folder, keeping the same relative paths so the links resolve there.
    # LastWriteTime is set to now so the retention clock (prune-to-read.ps1) starts at arrival.
    if (-not $ToReadDir) { return 'skipped (no to_read_dir configured)' }
    if (-not (Test-Path -LiteralPath $ToReadDir)) { New-Item -ItemType Directory -Path $ToReadDir -Force | Out-Null }
    if (-not $Name) { $Name = Split-Path $MdFile -Leaf }
    $srcDir = Split-Path $MdFile
    $figs = @()
    foreach ($rel in @(Get-EmbeddedFigures $MdFile)) {
        $from = Join-Path $srcDir $rel.Replace('/', '\')
        if (-not (Test-Path -LiteralPath $from)) { throw "embedded figure $rel not found next to $MdFile" }
        $figs += [pscustomobject]@{ from = $from; to = (Join-Path $ToReadDir $rel.Replace('/', '\')) }
    }
    foreach ($f in $figs) { [void](Copy-Verified $f.from $f.to); (Get-Item -LiteralPath $f.to).LastWriteTime = Get-Date }
    $dest = Join-Path $ToReadDir $Name
    [void](Copy-Verified $MdFile $dest); (Get-Item -LiteralPath $dest).LastWriteTime = Get-Date
    return "$dest + $($figs.Count) figure(s)"
}

function Get-InboxCount([string]$Dir = $script:MdDir) {
    return @(Get-ChildItem -Path $Dir -File -Filter *.md -ErrorAction SilentlyContinue).Count
}

function Get-RelPath([string]$Root, [string]$Path) {
    $r = (Resolve-Path $Root).Path.TrimEnd('\') + '\'
    $p = (Resolve-Path -LiteralPath $Path).Path
    if (-not $p.StartsWith($r, [StringComparison]::OrdinalIgnoreCase)) { throw "$Path is not inside $Root" }
    return $p.Substring($r.Length).Replace('\', '/')
}

function Invoke-Git([string]$Repo, [string[]]$GitArgs) {
    $ErrorActionPreference = 'Continue'   # native stderr must not throw
    $out = & git -C $Repo @GitArgs 2>&1 | ForEach-Object { "$_" }
    return [pscustomobject]@{ code = $LASTEXITCODE; out = ($out -join "`n") }
}

function Invoke-Delivery {
    param(
        [Parameter(Mandatory)][string]$SourceFile,
        [Parameter(Mandatory)]$Meta,
        [string]$Model = 'opus',
        [string]$MdDir = $script:MdDir,
        [string]$DriveDir = $script:DriveAnalyses,
        [string]$LogFile = $script:PapersLog,
        [string]$RepoRoot = $script:RepoRoot,
        [string]$PdfTodo = (Join-Path $script:QueueDir 'pdf-todo.txt'),
        [string]$ToReadDir = $script:ToReadDir,   # '' = skip the To Read copy
        [switch]$NoGit, [switch]$NoPush, [switch]$Force, [string]$RunLog,
        [switch]$Replace,   # replace the existing log row for this paper (re-run) instead of appending one
        [string]$Note       # appended to the model column of the log row, e.g. 're-run 2026-10-03, framework v3.13'
    )
    $d = [ordered]@{ file = (Split-Path $SourceFile -Leaf); bytes = $null; words = $null; md = $null; figures = @(); drive = $null; toRead = $null; pdf = $null; log = $null; git = $null; push = $null; inbox = $null; warnings = @() }
    $src = Get-Item -LiteralPath $SourceFile
    $d.bytes = $src.Length
    if ($src.Length -lt 15000) { throw "Analysis file is only $($src.Length) bytes; a full nine-section analysis should be tens of KB. Not delivering." }
    $d.words = Get-WordCount $SourceFile
    Write-Log "Delivery: $($d.file) ($($d.bytes) bytes, ~$($d.words) words)" $RunLog

    # figures embedded in the analysis (figures/<file>, relative to the .md) travel with it; check them all first
    $srcDirOfMd = Split-Path $SourceFile
    $figRels = @(Get-EmbeddedFigures $SourceFile)
    $figPairs = @()
    foreach ($rel in $figRels) {
        $from = [IO.Path]::GetFullPath((Join-Path $srcDirOfMd $rel.Replace('/', '\')))
        $to = [IO.Path]::GetFullPath((Join-Path $MdDir $rel.Replace('/', '\')))
        if (-not (Test-Path -LiteralPath $from) -and -not (Test-Path -LiteralPath $to)) { throw "The analysis embeds $rel, but that file is in neither $srcDirOfMd nor $MdDir. Not delivering." }
        $figPairs += [pscustomobject]@{ rel = $rel; from = $from; to = $to }
    }
    if ($figPairs.Count) { Write-Log "  figures embedded: $($figPairs.Count) ($(($figPairs | ForEach-Object { Split-Path $_.rel -Leaf }) -join ', '))" $RunLog }

    # a. incoming\md
    if (-not (Test-Path $MdDir)) { New-Item -ItemType Directory -Path $MdDir | Out-Null }
    $mdDest = Join-Path $MdDir $d.file
    if ((Test-Path -LiteralPath $mdDest) -and -not $Force) {
        if ((Get-FileHash -LiteralPath $mdDest).Hash -ne (Get-FileHash -LiteralPath $SourceFile).Hash) { throw "$mdDest already exists with different content; not overwriting (use -Force)." }
    }
    $n = Copy-Verified $SourceFile $mdDest
    $d.md = "$mdDest ($n bytes, verified)"; Write-Log "  a. md   -> $($d.md)" $RunLog
    foreach ($f in $figPairs) {
        if ((Test-Path -LiteralPath $f.from) -and ($f.from -ne $f.to)) { [void](Copy-Verified $f.from $f.to) }
        $d.figures += $f.to
    }
    if ($figPairs.Count) { Write-Log "  a. figs -> $($figPairs.Count) file(s) in $(Join-Path $MdDir 'figures') (verified)" $RunLog }

    # b. Drive (synced folder) + PDF
    if (Wait-DriveMount $DriveDir) {
        if (-not (Test-Path $DriveDir)) { New-Item -ItemType Directory -Path $DriveDir -Force | Out-Null }
        $driveDest = Join-Path $DriveDir $d.file
        $n = Copy-Verified $SourceFile $driveDest
        $d.drive = "$driveDest ($n bytes, verified)"
        foreach ($f in $figPairs) { [void](Copy-Verified $f.to (Join-Path $DriveDir $f.rel.Replace('/', '\'))) }
        if ($figPairs.Count) { $d.drive += " + $($figPairs.Count) figure(s) in $(Join-Path $DriveDir 'figures')" }
    } else {
        $d.drive = 'FAILED: Google Drive (G:) not mounted'; $d.warnings += $d.drive
        Add-Utf8Line (Join-Path (Split-Path $PdfTodo) 'drive-retry.txt') ($mdDest + "`t" + $DriveDir)
        foreach ($f in $figPairs) { Add-Utf8Line (Join-Path (Split-Path $PdfTodo) 'drive-retry.txt') ($f.to + "`t" + (Split-Path (Join-Path $DriveDir $f.rel.Replace('/', '\')))) }
    }
    Write-Log "  b. drive-> $($d.drive)" $RunLog
    if ((Get-Command pandoc -ErrorAction SilentlyContinue) -and (Get-Command xelatex -ErrorAction SilentlyContinue) -and $d.drive -notlike 'FAILED*') {
        $pdfOut = Join-Path $DriveDir ([IO.Path]::ChangeExtension($d.file, '.pdf'))
        & pandoc $mdDest -o $pdfOut --pdf-engine=xelatex --resource-path=$MdDir -f markdown-implicit_figures+lists_without_preceding_blankline -V geometry:margin=2.2cm 2>$null
        if ((Test-Path $pdfOut) -and (Get-Item $pdfOut).Length -gt 20000) { $d.pdf = "$pdfOut ($((Get-Item $pdfOut).Length) bytes)" } else { $d.pdf = 'pandoc failed'; $d.warnings += 'PDF build failed' }
    } else {
        $d.pdf = 'not built on laptop (no pandoc/xelatex); queued in pdf-todo.txt for the box' + $(if ($figPairs.Count) { ' (needs the figures/ files next to the .md)' } else { '' })
        Add-Utf8Line $PdfTodo ((Get-Date -Format 'yyyy-MM-dd') + "`t" + $d.file)
    }
    Write-Log "  b. pdf  -> $($d.pdf)" $RunLog

    # b2. To Read folder (phone/tablet reading copy) - non-fatal
    if ($ToReadDir) {
        try {
            if (-not (Wait-DriveMount $ToReadDir 30)) { throw "the drive for $ToReadDir is not mounted" }
            $d.toRead = Copy-ToRead $mdDest $ToReadDir
            Write-Log "  b2. to-read -> $($d.toRead)" $RunLog
        } catch {
            $d.toRead = 'FAILED (non-fatal): ' + $_.Exception.Message; $d.warnings += ('To Read copy failed: ' + $_.Exception.Message)
            Write-Log "  WARNING: To Read copy failed (delivery continues): $($_.Exception.Message)" $RunLog
        }
    } else { $d.toRead = 'skipped' }

    # c. papers-analyzed log
    if (-not (Test-Path $LogFile)) {
        Write-Utf8File $LogFile ("# Papers analyzed log`r`n`r`nOne row per delivered analysis (written by incoming/automation/analyze-paper.ps1).`r`n`r`n| date | title | arXiv/DOI | file | model | words |`r`n| --- | --- | --- | --- | --- | --- |`r`n")
    }
    $ids = @(); if ($Meta.arxiv) { $ids += ('arXiv:' + $Meta.arxiv) }; if ($Meta.doi) { $ids += ('doi:' + $Meta.doi) }
    if (-not $ids.Count -and $Meta.slug) { $ids += ('local:' + $Meta.slug) }
    $title = ("$($Meta.title)" -replace '\|', '/' -replace '\s+', ' ').Trim()
    $modelCol = $(if ($Note) { $Model + ' (' + ($Note -replace '\|', '/') + ')' } else { $Model })
    $row = '| ' + (Get-Date -Format 'yyyy-MM-dd') + ' | ' + $title + ' | ' + ($ids -join ' / ') + ' | ' + $d.file + ' | ' + $modelCol + ' | ' + $d.words + ' |'
    $before = (Get-Item $LogFile).Length
    $replaced = $false
    if ($Replace) {
        $lines = [IO.File]::ReadAllLines($LogFile)
        for ($i = 0; $i -lt $lines.Count; $i++) {
            $l = $lines[$i]
            if ($l.StartsWith('| ') -and ($l.Contains(' ' + $d.file + ' ') -or ($Meta.arxiv -and $l.Contains('arXiv:' + $Meta.arxiv + ' ')) -or ($Meta.doi -and $l.Contains('doi:' + $Meta.doi + ' ')))) {
                $lines[$i] = $row; $replaced = $true; break
            }
        }
        if ($replaced) { Write-Utf8File $LogFile (($lines -join "`r`n") + "`r`n") }
    }
    if (-not $replaced) { Add-Utf8Line $LogFile $row }
    $after = (Get-Item $LogFile).Length
    if ((-not $replaced -and $after -le $before) -or -not ([IO.File]::ReadAllText($LogFile).Contains($row))) { throw "Log update could not be verified ($LogFile)" }
    $d.log = "$LogFile ($(if ($replaced) { 'row replaced' } else { 'row appended' }), $before -> $after bytes)"; Write-Log "  c. log  -> $($d.log)" $RunLog

    # d. git commit (analysis + log only) and push
    if ($NoGit) { $d.git = 'skipped (-NoGit)' }
    else {
        $relMd = Get-RelPath $RepoRoot $mdDest; $relLog = Get-RelPath $RepoRoot $LogFile
        $paths = @($relMd, $relLog) + @($d.figures | ForEach-Object { Get-RelPath $RepoRoot $_ })
        $g = Invoke-Git $RepoRoot (@('add', '--') + $paths)
        if ($g.code -ne 0) { throw "git add failed: $($g.out)" }
        $msg = $(if ($Replace) { 'Replace analysis' + $(if ($Note) { ' (' + $Note + ')' } else { '' }) + ': ' } else { 'Add analysis: ' }) + $title + ' (' + ($ids -join ', ') + ')'
        $g = Invoke-Git $RepoRoot (@('commit', '-m', $msg.Replace('"', "'"), '--') + $paths)
        if ($g.code -ne 0) { throw "git commit failed: $($g.out)" }
        $d.git = (Invoke-Git $RepoRoot @('rev-parse', '--short', 'HEAD')).out.Trim()
        if ($NoPush) { $d.push = 'skipped (-NoPush)' }
        else {
            $remote = (Invoke-Git $RepoRoot @('remote')).out.Trim()
            if (-not $remote) { $d.push = 'skipped (no remote)' }
            else {
                $p = Invoke-Git $RepoRoot @('push', 'origin', 'HEAD')
                if ($p.code -eq 0) { $d.push = 'pushed' } else { $d.push = 'FAILED (will retry on next worker run): ' + $p.out; $d.warnings += 'git push failed' }
            }
        }
    }
    Write-Log "  d. git  -> commit $($d.git), push: $($d.push)" $RunLog

    # 5. pending ingest count
    $d.inbox = Get-InboxCount $MdDir
    Write-Log "Pending ingest: $($d.inbox) .md file(s) in $MdDir (root)" $RunLog
    return [pscustomobject]$d
}

function Save-Result([string]$Path, $Obj) {
    if ($Path) { Write-Utf8File $Path ($Obj | ConvertTo-Json -Depth 6) }
}

# ---------- queue ----------
# Job files: queue\<yyyyMMdd-HHmmss>_<label>.<status>.json, status = pending|running|done|failed|limit

function New-QueueJob {
    param([Parameter(Mandatory)][string]$Paper, [string]$Title, [string]$Type = 'analyze', [string]$Question,
        [switch]$Append, [switch]$DryRun, [switch]$Force, [string]$Source = 'laptop', [string]$QueueDir = $script:QueueDir, [string]$Framework, [string]$LocalPdf, [string]$Slug)
    if (-not (Test-Path $QueueDir)) { New-Item -ItemType Directory -Path $QueueDir | Out-Null }
    if ($Type -eq 'deepdive' -and -not $Question) { throw 'A deepdive job needs a question.' }
    $label = ($Paper -replace '^(?i)https?://', '' -replace '[^A-Za-z0-9.\-]', '-').Trim('-')
    if ($label.Length -gt 50) { $label = $label.Substring($label.Length - 50) }
    $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $path = Join-Path $QueueDir ($stamp + '_' + $Type + '_' + $label + '.pending.json')
    $i = 1; while (Test-Path $path) { $path = Join-Path $QueueDir ($stamp + '-' + $i + '_' + $Type + '_' + $label + '.pending.json'); $i++ }
    $job = [ordered]@{ type = $Type; paper = $Paper; title = $Title; question = $Question; append = [bool]$Append; dryRun = [bool]$DryRun; force = [bool]$Force
        source = $Source; submitted = (Get-Date).ToString('s'); attempts = 0; retryAfter = $null; finished = $null; result = $null }
    if ($Framework) { $job.framework = $Framework }; if ($LocalPdf) { $job.localPdf = $LocalPdf }; if ($Slug) { $job.slug = $Slug }
    Write-Utf8File $path ($job | ConvertTo-Json -Depth 6)
    return $path
}

function Read-JobSpecFile([string]$Path) {
    # Accepts the JSON job schema, or a text file: 'key: value' lines (paper/title/type/question/append/dryRun/force)
    # or plain lines (line 1 = arXiv ID/DOI/URL, line 2 = optional title).
    $raw = [IO.File]::ReadAllText($Path).Trim([char]0xFEFF).Trim()
    if (-not $raw) { throw 'empty file' }
    if ($raw.StartsWith('{')) { $j = $raw | ConvertFrom-Json; return $j }
    $spec = @{}; $plain = @()
    foreach ($l in ($raw -split "`r?`n")) {
        $t = $l.Trim(); if (-not $t -or $t.StartsWith('#')) { continue }
        if ($t -match '^(?i)(paper|title|type|question|append|dryrun|dry-run|force|framework|pdf|slug)\s*:\s*(.+)$') { $spec[$Matches[1].ToLower().Replace('-', '')] = $Matches[2].Trim() }
        else { $plain += $t }
    }
    if (-not $spec.paper -and $plain.Count) { $spec.paper = $plain[0] }
    if (-not $spec.title -and $plain.Count -gt 1) { $spec.title = $plain[1] }
    if (-not $spec.paper -and $spec.pdf) { $spec.paper = $(if ($spec.slug) { $spec.slug } else { Get-Slug $(if ($spec.title) { $spec.title } else { [IO.Path]::GetFileNameWithoutExtension($spec.pdf) }) }) }
    if (-not $spec.paper) { throw 'no paper reference found' }
    return [pscustomobject]@{ paper = $spec.paper; title = $spec.title; type = $(if ($spec.type) { $spec.type } else { 'analyze' }); question = $spec.question
        append = ($spec.append -match '^(?i)(1|true|yes)$'); dryRun = ($spec.dryrun -match '^(?i)(1|true|yes)$'); force = ($spec.force -match '^(?i)(1|true|yes)$'); framework = $spec.framework; localPdf = $spec.pdf; slug = $spec.slug }
}
