#!/usr/bin/env python3
"""Full reverse-link audit for Physics Wiki (167 papers)."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "wiki"
OUT = Path(__file__).resolve().parent

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]+)?\]\]")


def slugify(s: str) -> str:
    s = s.strip()
    # Obsidian may use display titles; prefer path-like stems
    s = s.replace("\\", "/")
    if "/" in s:
        s = s.split("/")[-1]
    return s.strip().lower().replace(" ", "-")


def parse_file(p: Path) -> tuple[set[str], set[str], str]:
    text = p.read_text(encoding="utf-8")
    links = {slugify(m.group(1)) for m in WIKILINK.finditer(text)}
    rp: set[str] = set()
    # Inline: related_papers: [a, b, c]
    m_inline = re.search(r"^related_papers:\s*\[([^\]]*)\]", text, re.M)
    if m_inline:
        for part in m_inline.group(1).split(","):
            val = part.strip().strip('"').strip("'")
            if val:
                rp.add(slugify(val))
    # Block list:
    # related_papers:
    #   - a
    #   - [[b]]
    m = re.search(r"^related_papers:\s*\n((?:[ \t]*-[ \t]*.+\n)*)", text, re.M)
    if m:
        for line in m.group(1).splitlines():
            lm = re.match(r'\s*-\s*["\']?\[\[([^\]|#]+)', line)
            if not lm:
                lm = re.match(r'\s*-\s*["\']?([^"\'\n]+)', line)
            if lm:
                val = lm.group(1).strip().strip('"').strip("'")
                if val:
                    rp.add(slugify(val))
    return links, rp, text


def main() -> None:
    papers = sorted((ROOT / "papers").glob("*.md"))
    concepts = sorted((ROOT / "concepts").glob("*.md"))
    synths = sorted((ROOT / "synthesis").glob("*.md"))
    print(f"counts: papers={len(papers)} concepts={len(concepts)} synth={len(synths)}")

    paper_slugs = {p.stem.lower() for p in papers}
    concept_slugs = {p.stem.lower() for p in concepts}
    synth_slugs = {p.stem.lower() for p in synths}

    out_all: dict[str, set[str]] = {}
    out_papers: dict[str, set[str]] = {}
    inbound: dict[str, set[str]] = defaultdict(set)
    by_stem: dict[str, Path] = {}

    for p in papers + concepts + synths:
        links, rp, _ = parse_file(p)
        stem = p.stem.lower()
        by_stem[stem] = p
        outs = links | rp
        out_all[stem] = outs
        if p.parent.name == "papers":
            out_papers[stem] = outs
        for t in outs:
            inbound[t].add(stem)

    # Paper↔paper asymmetries
    asym = []
    for a, outs in sorted(out_papers.items()):
        for b in sorted(outs):
            if b in paper_slugs and b != a:
                if a not in out_papers.get(b, set()):
                    asym.append({"from": a, "to": b})

    print(f"paper-paper asymmetries: {len(asym)}")

    # True orphans
    orphans = []
    for s in sorted(paper_slugs):
        inn = {x for x in inbound.get(s, set()) if x not in (s, "index", "log")}
        if not inn:
            orphans.append(s)
    print(f"true orphans: {len(orphans)}")
    if orphans:
        print(" ", orphans)

    # paper→concept missing reverse
    concept_gaps = []
    for a, outs in sorted(out_papers.items()):
        for c in sorted(outs):
            if c in concept_slugs and a not in out_all.get(c, set()):
                concept_gaps.append({"paper": a, "concept": c})
    print(f"paper->concept missing reverse: {len(concept_gaps)}")

    # paper→synth missing reverse
    synth_gaps = []
    for a, outs in sorted(out_papers.items()):
        for s in sorted(outs):
            if s in synth_slugs and a not in out_all.get(s, set()):
                synth_gaps.append({"paper": a, "synth": s})
    print(f"paper->synth missing reverse: {len(synth_gaps)}")
    for g in synth_gaps:
        print(" ", g)

    # synth→paper missing reverse on paper side
    synth_to_paper_missing = []
    for s in sorted(synth_slugs):
        for t in sorted(out_all.get(s, set())):
            if t in paper_slugs and s not in out_papers.get(t, set()):
                synth_to_paper_missing.append({"synth": s, "paper": t})
    print(f"synth->paper missing reverse: {len(synth_to_paper_missing)}")
    for g in synth_to_paper_missing[:30]:
        print(" ", g)
    if len(synth_to_paper_missing) > 30:
        print(f"  ... +{len(synth_to_paper_missing)-30} more")

    # Broken links (targets that don't exist)
    broken = []
    known = paper_slugs | concept_slugs | synth_slugs | {"index", "log"}
    for stem, outs in sorted(out_all.items()):
        for t in sorted(outs):
            if t not in known and not t.startswith("http"):
                # allow entity/subfield stubs that don't exist yet
                broken.append({"from": stem, "to": t})
    print(f"unresolved wikilink targets: {len(broken)}")

    payload = {
        "counts": {
            "papers": len(papers),
            "concepts": len(concepts),
            "synthesis": len(synths),
        },
        "asym": asym,
        "orphans": orphans,
        "concept_gaps": concept_gaps,
        "synth_gaps": synth_gaps,
        "synth_to_paper_missing": synth_to_paper_missing,
        "broken_sample": broken[:50],
        "broken_count": len(broken),
    }
    out_path = OUT / "_rlink_verify.json"
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
