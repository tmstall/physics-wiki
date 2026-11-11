#!/usr/bin/env python3
"""Apply paper↔paper Reverse-link patches from _rlink_verify.json."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAPERS = ROOT / "wiki" / "papers"


def ensure_connections(text: str) -> str:
    if re.search(r"^## Connections\s*$", text, re.M):
        return text
    for heading in (r"^## Open questions\s*$", r"^## Source\s*$", r"^## References\s*$"):
        m = re.search(heading, text, re.M)
        if m:
            return text[: m.start()] + "## Connections\n\n" + text[m.start() :]
    if not text.endswith("\n"):
        text += "\n"
    return text + "\n## Connections\n\n"


def has_wikilink_to(text: str, slug: str) -> bool:
    pat = rf"\[\[[^\]]*?{re.escape(slug)}(?:[|#][^\]]*)?\]\]"
    if re.search(pat, text, re.I):
        return True
    m = re.search(r"^related_papers:\s*\[([^\]]*)\]", text, re.M)
    if m:
        parts = [
            p.strip().strip("\"'").lower().replace(" ", "-")
            for p in m.group(1).split(",")
        ]
        if slug.lower() in parts:
            return True
    return False


def add_line_under_connections(text: str, line: str) -> str:
    text = ensure_connections(text)
    m = re.search(r"^## Connections\s*$", text, re.M)
    assert m
    start = m.end()
    rest = text[start:]
    m2 = re.search(r"^## ", rest, re.M)
    block = rest if not m2 else rest[: m2.start()]
    after = "" if not m2 else rest[m2.start() :]
    if line.strip() in {ln.strip() for ln in block.splitlines()}:
        return text
    lines = block.splitlines(keepends=True)
    last_special = -1
    for i, ln in enumerate(lines):
        if ln.startswith("- Reverse-link:") or ln.startswith("- Synthesis:"):
            last_special = i
    if last_special >= 0:
        before = "".join(lines[: last_special + 1])
        after_block = "".join(lines[last_special + 1 :])
        if not before.endswith("\n"):
            before += "\n"
        new_block = before + line + "\n" + after_block
    else:
        new_block = "\n" + line + "\n" + block.lstrip("\n")
    return text[:start] + new_block + after


def main() -> None:
    data = json.loads((ROOT / "_rlink_verify.json").read_text(encoding="utf-8"))
    changed: set[str] = set()
    actions: list[str] = []
    for item in data.get("asym", []):
        src = item["from"]
        dst = item["to"]
        path = PAPERS / f"{dst}.md"
        if not path.exists():
            actions.append(f"SKIP missing {dst}")
            continue
        text = path.read_text(encoding="utf-8")
        if has_wikilink_to(text, src):
            actions.append(f"SKIP already {dst} <- {src}")
            continue
        new_text = add_line_under_connections(text, f"- Reverse-link: [[{src}]]")
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed.add(dst)
            actions.append(f"ADD {dst} <- {src}")
    report = {"n_changed": len(changed), "changed": sorted(changed), "actions": actions}
    (ROOT / "_rlink_fix_report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    print(f"changed_files={len(changed)}")
    for a in actions:
        print(a)


if __name__ == "__main__":
    main()
