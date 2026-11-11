"""Full AGENTS lint snapshot for 2026-08-29 READY_QUEUE wave close."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WIKI = ROOT / "wiki"
PAPERS = WIKI / "papers"
CONCEPTS = WIKI / "concepts"
SYNTH = WIKI / "synthesis"
INDEX = WIKI / "index.md"

NEW_SLUGS = [
    "tracking-baryon-number-nuclear-collisions",
    "coupling-free-electrons-trapped-ion",
    "correlated-electrons-xray-hhg",
    "particle-view-nn-wavefunction",
    "43gev-gamma-ray-line-clusters",
    "emergent-social-conventions-llm-populations",
    "gw-ori-streamer-misalignment",
    "oasis-million-agent-social-simulator",
    "atomic-scale-double-slit-si",
    "equilibrated-fraction-oo-qcd",
    "astrid-z0-mbh-lss",
]

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def slugs_in(dirpath: Path) -> set[str]:
    return {p.stem for p in dirpath.glob("*.md")}


def index_slugs(text: str) -> set[str]:
    return {m.group(1).strip() for m in WIKILINK.finditer(text)}


def all_targets() -> set[str]:
    return slugs_in(PAPERS) | slugs_in(CONCEPTS) | slugs_in(SYNTH) | {"index", "log"}


def unresolved_links() -> list[tuple[str, str]]:
    known = all_targets()
    bad: list[tuple[str, str]] = []
    for folder in (PAPERS, CONCEPTS, SYNTH):
        for path in folder.glob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            for m in WIKILINK.finditer(text):
                target = m.group(1).strip()
                if target not in known:
                    bad.append((path.relative_to(WIKI).as_posix(), target))
    return bad


def orphans() -> list[str]:
    """Pages never linked from another wiki page (excluding self/index)."""
    known_pages = slugs_in(PAPERS) | slugs_in(CONCEPTS) | slugs_in(SYNTH)
    inbound: dict[str, int] = {s: 0 for s in known_pages}
    for folder in (PAPERS, CONCEPTS, SYNTH):
        for path in folder.glob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            src = path.stem
            for m in WIKILINK.finditer(text):
                t = m.group(1).strip()
                if t in inbound and t != src:
                    inbound[t] += 1
    # also count index
    for m in WIKILINK.finditer(INDEX.read_text(encoding="utf-8", errors="replace")):
        t = m.group(1).strip()
        if t in inbound:
            inbound[t] += 1
    # orphan = zero inbound from other content pages (index alone doesn't count as "connected")
    # Redefine: linked only from index or not at all among content peers
    peer_inbound: dict[str, int] = {s: 0 for s in known_pages}
    for folder in (PAPERS, CONCEPTS, SYNTH):
        for path in folder.glob("*.md"):
            text = path.read_text(encoding="utf-8", errors="replace")
            src = path.stem
            for m in WIKILINK.finditer(text):
                t = m.group(1).strip()
                if t in peer_inbound and t != src:
                    peer_inbound[t] += 1
    return sorted([s for s, n in peer_inbound.items() if n == 0])


def has_synth_mention(slug: str) -> bool:
    text = (PAPERS / f"{slug}.md").read_text(encoding="utf-8", errors="replace")
    synths = slugs_in(SYNTH)
    for m in WIKILINK.finditer(text):
        if m.group(1).strip() in synths:
            return True
    return False


INTENTIONAL_NO_SYNTH = {
    "emergent-social-conventions-llm-populations",
    "oasis-million-agent-social-simulator",
}


def main() -> None:
    papers = slugs_in(PAPERS)
    concepts = slugs_in(CONCEPTS)
    synths = slugs_in(SYNTH)
    idx = INDEX.read_text(encoding="utf-8", errors="replace")
    indexed = index_slugs(idx)

    missing_from_index = sorted(papers - indexed)
    extra_index_papers = sorted(
        s for s in indexed if s not in papers and s not in concepts and s not in synths
    )
    # filter extras that are intentional non-page links — keep only likely broken paper refs
    unresolved = unresolved_links()
    orph = orphans()
    new_synth = {s: has_synth_mention(s) for s in NEW_SLUGS if s in papers}

    lines = []
    lines.append("# Wiki lint report — 2026-08-29 (full AGENTS lint after READY_QUEUE wave)")
    lines.append("")
    lines.append(f"**Catalog:** **{len(papers)} papers · {len(concepts)} concepts · {len(synths)} synthesis**")
    lines.append("**Trigger:** End of READY_QUEUE ingest (11 papers this wave).")
    lines.append("**`raw/` untouched.**")
    lines.append("")
    lines.append("## Snapshot")
    lines.append("")
    lines.append("| Check | Result |")
    lines.append("| --- | --- |")
    lines.append(f"| Index lists all papers | {'**Pass**' if not missing_from_index else f'**Fail** ({len(missing_from_index)} missing)'} |")
    lines.append(f"| Unresolved wikilink targets | **{len(unresolved)}** |")
    synth_yes = sum(1 for s, v in new_synth.items() if v or s in INTENTIONAL_NO_SYNTH)
    lines.append(
        f"| New ingest pages with ≥1 Synthesis link (or intentional defer) | **{synth_yes}/{len(new_synth)}** |"
    )
    lines.append(f"| Content orphans (no peer inbound link) | **{len(orph)}** |")
    lines.append("")

    if missing_from_index:
        lines.append("## Papers missing from index")
        lines.append("")
        for s in missing_from_index:
            lines.append(f"- `{s}`")
        lines.append("")

    lines.append("## New wave synth coverage")
    lines.append("")
    for s, ok in new_synth.items():
        if ok:
            status = "yes"
        elif s in INTENTIONAL_NO_SYNTH:
            status = "deferred (multi-agent hub — next work plan)"
        else:
            status = "**NO synth link**"
        lines.append(f"- [[{s}]]: {status}")
    lines.append("")

    lines.append("## Orphans (peer-inbound = 0; index alone does not count)")
    lines.append("")
    if not orph:
        lines.append("_None._")
    else:
        for s in orph:
            kind = "paper" if s in papers else ("concept" if s in concepts else "synthesis")
            lines.append(f"- [[{s}]] ({kind})")
    lines.append("")

    if unresolved:
        lines.append("## Unresolved wikilinks (first 40)")
        lines.append("")
        for src, t in unresolved[:40]:
            lines.append(f"- `{src}` → `[[{t}]]`")
        if len(unresolved) > 40:
            lines.append(f"- … +{len(unresolved) - 40} more")
        lines.append("")

    lines.append("## Spot-checks (new wave)")
    lines.append("")
    lines.append("- [[astrid-z0-mbh-lss]]: DF framed as subgrid, not resolved final-parsec; BHAD >1 dex named.")
    lines.append("- [[equilibrated-fraction-oo-qcd]]: linked to [[alice-oo-nene-nuclear-geometry-flow]] (geometry vs core/corona).")
    lines.append("- [[43gev-gamma-ray-line-clusters]]: ~4.3σ global / evidence not discovery; GC non-detection tension noted on page.")
    lines.append("- [[tracking-baryon-number-nuclear-collisions]]: disfavors valence-only; does not claim quarks carry zero $B$.")
    lines.append("- Multi-agent trio ([[ai-agents-majority-following]], [[emergent-social-conventions-llm-populations]], [[oasis-million-agent-social-simulator]]) cross-linked; no longer a singleton island.")
    lines.append("")
    lines.append("## Deferred (non-blocking; next work plan)")
    lines.append("")
    lines.append("- Widen wiki charter + promote Multi-agent section out of Islands.")
    lines.append("- Island graduation policy.")
    lines.append("- Thorough multi-agent / collective-AI synthesis (only after charter).")
    lines.append("- Exhaustive paper↔paper rlink asymmetries (historical backlog).")
    lines.append("")

    out = ROOT / "LINT_REPORT_2026-08-29.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out)
    print(f"papers={len(papers)} missing_index={len(missing_from_index)} unresolved={len(unresolved)} orphans={len(orph)}")
    print("new_synth", new_synth)


if __name__ == "__main__":
    main()
