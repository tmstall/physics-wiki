"""Scan extracts + wiki for duplicate triage inputs."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\tmsta\Documents\Physics-Wiki")
papers = ROOT / "wiki" / "papers"
extracts = ROOT / "spacex_export" / "extracted-analyses"

wiki = []
for p in sorted(papers.glob("*.md")):
    t = p.read_text(encoding="utf-8", errors="replace")[:3000]
    title = ""
    m = re.search(r"(?m)^#\s+(.+)$", t)
    if m:
        title = m.group(1).strip()
    sm = re.search(r"\*\*One-line summary:\*\*\s*(.+)", t)
    summary = sm.group(1).strip()[:220] if sm else ""
    wiki.append({"slug": p.stem, "title": title, "summary": summary})

exts = []
for p in sorted(extracts.glob("*.md")):
    t = p.read_text(encoding="utf-8", errors="replace")
    head = t[:5000]
    title = ""
    m = re.search(r'(?m)^title:\s*"(.*)"\s*$', head)
    if m:
        title = m.group(1)
    else:
        m2 = re.search(r"(?m)^#\s+(.+)$", head)
        if m2:
            title = m2.group(1).strip()
    body = re.sub(r"^---.*?---\s*", "", t, count=1, flags=re.S)
    first_lines = "\n".join(body.splitlines()[:70])
    # also grab punchy hook if present
    hook = ""
    hm = re.search(
        r"(?is)(?:Punchy Title|One-Sentence Hook|one-sentence hook).{0,40}\n+(.{80,400})",
        body,
    )
    if hm:
        hook = re.sub(r"\s+", " ", hm.group(1))[:350]
    exts.append(
        {
            "file": p.name,
            "title": title,
            "size": p.stat().st_size,
            "chars": len(t),
            "head": first_lines[:2800],
            "hook": hook,
        }
    )

(ROOT / "spacex_export" / "_wiki_index.json").write_text(
    json.dumps(wiki, indent=2), encoding="utf-8"
)
(ROOT / "spacex_export" / "_extract_heads.json").write_text(
    json.dumps(exts, indent=2, ensure_ascii=False), encoding="utf-8"
)
print("wiki", len(wiki), "extracts", len(exts))
