"""Inventory + pilot candidate scan for SpaceX/xAI Grok export."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(r"C:\Users\tmsta\Documents\Physics-Wiki")
BACKEND = (
    ROOT
    / "SpaceX_exported_data"
    / "ttl"
    / "30d"
    / "export_data"
    / "0b555e90-6d15-442d-a448-aaaf8951e557"
    / "prod-grok-backend.json"
)
OUT = ROOT / "spacex_export"
OUT.mkdir(exist_ok=True)

PHYS = re.compile(
    r"quantum|black.?hole|cosmo|gravit|photon|entangl|plasma|nuclear|relativ|"
    r"field.?theory|condensed|superconduct|particle|hawking|clock|metrology|"
    r"spin|qubit|QFT|QCD|MOND|dark.?energy|dark.?matter|neutron|electron|atom|"
    r"molecule|fusion|laser|optics|thermodynam|entropy|holograph|decoherence|"
    r"measurement problem|AGN|quasar|cosmic|spacetime|einstein|string theory|"
    r"loop quantum|Bose|fermion|gauge|symmetry|vacuum|Casimir|Bell test|"
    r"Shor|cavity|ion trap|nanodroplet|Brillouin|gamma|UHECR|JWST|LIGO|"
    r"general relativity|special relativity|wavefunction|Schrodinger|"
    r"Schrödinger|Hilbert|Hamiltonian|Lagrangian|path integral|renormal|"
    r"topo(logical)?|chirality|magnon|phonon|qubit|qubit|superfluid|"
    r"neutron star|pulsar|CMB|baryon|lepton|hadron|meson|gluon|"
    r"Hawking|Penrose|Everett|Bohm|Born rule|collapse model|CSL|"
    r"proper time|weak value|NOON|Ramsey|interferom",
    re.I,
)
NONPHYS = re.compile(
    r"obsidian|karpathy wiki|billing|invoice|recipe|travel|stock|crypto wallet|"
    r"game|meme|image gen|draw me|write a story|email|resume|marketing|"
    r"python script|javascript|typescript|react|next\.js|docker|kubernetes",
    re.I,
)
NOISE_IN_MSG = re.compile(
    r"https?://|web_search|browse_page|tool_use|function_call|Thinking\.\.\.|"
    r"<xai:|citation|\[\d+\]|OpenGraph|cookie|Accept-Language",
    re.I,
)


def main() -> None:
    # file inventory
    export_root = ROOT / "SpaceX_exported_data"
    files = list(export_root.rglob("*"))
    file_only = [f for f in files if f.is_file()]
    ext_counts: Counter[str] = Counter()
    for f in file_only:
        ext = f.suffix.lower() or "(no extension)"
        if f.name == "content":
            ext = "(asset content)"
        ext_counts[ext] += 1

    data = json.loads(BACKEND.read_text(encoding="utf-8"))
    convs = data["conversations"]

    sender_counts: Counter[str] = Counter()
    toolish = webish = 0
    rows = []
    metadata_key_examples: Counter[str] = Counter()

    for c in convs:
        meta = c["conversation"]
        title = meta.get("title") or ""
        resps = c.get("responses") or []
        human_chars = asst_chars = 0
        has_tool = has_web = False
        sample_blob = title + " "
        for r in resps:
            resp = r.get("response") or {}
            sender = resp.get("sender") or ""
            sender_counts[sender] += 1
            msg = resp.get("message") or ""
            if sender == "human":
                human_chars += len(msg)
            else:
                asst_chars += len(msg)
            md = resp.get("metadata") or {}
            if md:
                has_tool = True
                for k in md.keys():
                    metadata_key_examples[k] += 1
            if NOISE_IN_MSG.search(msg):
                has_web = True
            if len(sample_blob) < 1500:
                sample_blob += msg[:300]
        if has_tool:
            toolish += 1
        if has_web:
            webish += 1

        score = 0
        if PHYS.search(title):
            score = 2
        elif PHYS.search(sample_blob):
            score = 1
        if NONPHYS.search(title) and score == 0:
            score = -1

        rows.append(
            {
                "id": meta["id"],
                "id8": meta["id"][:8],
                "title": title,
                "n": len(resps),
                "human": human_chars,
                "asst": asst_chars,
                "score": score,
                "create": (meta.get("create_time") or "")[:10],
                "starred": bool(meta.get("starred")),
                "has_tool": has_tool,
                "has_web": has_web,
            }
        )

    # write inventory
    lines = []
    lines.append("# SpaceX / xAI export inventory\n")
    lines.append(f"**Scanned:** 2026-08-04  \n")
    lines.append(f"**Source root:** `SpaceX_exported_data/`  \n")
    lines.append(f"**Primary payload:** `prod-grok-backend.json` (~{BACKEND.stat().st_size/1e6:.1f} MB)\n")
    lines.append("\n## Tree layout\n")
    lines.append("```\n")
    lines.append("SpaceX_exported_data/\n")
    lines.append("  list.txt                 # recursive path listing\n")
    lines.append("  ttl/30d/export_data/<user_uuid>/\n")
    lines.append("    prod-grok-backend.json  # conversations + projects + media_posts\n")
    lines.append("    prod-mc-auth-mgmt-api.json\n")
    lines.append("    prod-mc-billing.json\n")
    lines.append("    prod-mc-asset-server/   # profile pics + binary content blobs\n")
    lines.append("```\n")
    lines.append("\n## File counts\n")
    lines.append(f"- **Total files:** {len(file_only)}\n")
    lines.append(f"- **Total size:** ~{sum(f.stat().st_size for f in file_only)/1e6:.1f} MB\n")
    lines.append("\n| Extension / kind | Count |\n| --- | ---: |\n")
    for ext, n in ext_counts.most_common():
        lines.append(f"| `{ext}` | {n} |\n")
    lines.append("\n## Conversations\n")
    lines.append(f"- **Conversations:** {len(convs)}\n")
    lines.append(f"- **Projects:** {len(data.get('projects') or [])}\n")
    lines.append(f"- **Media posts:** {len(data.get('media_posts') or [])}\n")
    lines.append(f"- **Tasks:** {len(data.get('tasks') or [])}\n")
    lines.append(f"- **Sender histogram:** {dict(sender_counts)}\n")
    lines.append(f"- **Conversations with non-empty response.metadata:** {toolish}\n")
    lines.append(f"- **Conversations with URL/tool/chrome-like message text:** {webish}\n")
    if metadata_key_examples:
        lines.append(f"- **Metadata keys seen:** {dict(metadata_key_examples.most_common(30))}\n")
    else:
        lines.append("- **Metadata keys seen:** (none — metadata objects empty in this export)\n")
    lines.append("\n### Physics-ish scoring (title/sample heuristic)\n")
    lines.append(f"- score 2 (title physics keywords): {sum(1 for r in rows if r['score']==2)}\n")
    lines.append(f"- score 1 (body sample physics keywords): {sum(1 for r in rows if r['score']==1)}\n")
    lines.append(f"- score 0 (neutral/unknown): {sum(1 for r in rows if r['score']==0)}\n")
    lines.append(f"- score -1 (non-physics title cues): {sum(1 for r in rows if r['score']==-1)}\n")
    lines.append("\n### Top physics candidates (by assistant character volume)\n")
    lines.append("| Date | Msgs | Asst chars | Title |\n| --- | ---: | ---: | --- |\n")
    phys = sorted([r for r in rows if r["score"] >= 1], key=lambda r: -r["asst"])
    for r in phys[:40]:
        title = r["title"].replace("|", "\\|")
        lines.append(f"| {r['create']} | {r['n']} | {r['asst']} | {title} |\n")
    lines.append("\n### Structural notes vs Claude export\n")
    lines.append("- Claude: top-level array of conversations with `chat_messages` / structured `content[]` blocks (text/thinking/tool_use).\n")
    lines.append("- Grok: `{conversations:[{conversation, responses:[{response, share_link}]}]}`; message is a plain `message` string; `sender` is `human` or `assistant`.\n")
    lines.append("- Titles are first-class (`conversation.title`).\n")
    lines.append("- Asset server holds mostly binary `content` blobs + webp avatars — **not** analysis text.\n")
    lines.append("- Auth/billing JSON are non-content noise for physics extraction.\n")
    lines.append("\n### Noise assessment\n")
    lines.append("- Tool/metadata noise appears **lighter** than Claude in this dump (empty metadata objects).\n")
    lines.append("- Web URLs and citation-like patterns appear in some assistant messages when Grok browsed.\n")
    lines.append("- Non-physics material present (wiki tooling, general chat); filter by title/keywords + substance length.\n")
    lines.append("- Duplicates: not hard-moved yet; soft overlaps with Claude-export wiki topics expected (same research interests).\n")

    inv = OUT / "INVENTORY.md"
    inv.write_text("".join(lines), encoding="utf-8")
    print("Wrote", inv)
    print("convs", len(convs), "phys>=1", len(phys), "toolish", toolish, "webish", webish)

    # save pilot candidate list (top 15 physics by substance)
    pilot = phys[:20]
    (OUT / "pilot_candidates.json").write_text(
        json.dumps(pilot, indent=2), encoding="utf-8"
    )
    print("pilot candidates", len(pilot))
    for r in pilot[:15]:
        print(f"  {r['score']} {r['asst']:7d} {r['title'][:80]}")


if __name__ == "__main__":
    main()
