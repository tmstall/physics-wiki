"""Pilot extract: clean 15 physics-heavy Grok conversations → markdown."""
from __future__ import annotations

import hashlib
import json
import re
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
OUT_DIR = ROOT / "spacex_export" / "extracted-analyses"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Exact titles for pilot (prefer long technical analyses)
PILOT_TITLES = [
    "I - Astrophysics (and Black Holes)",
    "I - Quantum Mechanics & Quantum Field Theory",
    "Quantum Field Theory ",
    "Massive Gravity/Gluon Magic",
    "Nuclear Magnetization Observation Breakthrough",
    "Materials Science (Semiconductors & Nanostructures)",
    "-> Hawking Radiation from Charged Shell",
    "Quark-gluon plasma Discussion",
    "-> Collapse, Gravity & Proper-Time Uncertainty",
    "-> Quantum Proper Time Signatures in Ion Clocks",
    "Cluster Tunneling Forges Scalable Schrödinger Cats",
    "Photon Truncation Creates Infinite Particle Zoo",
    "Einstein and Riemann Geometry in Relativity",
    "BEC, superfluid He4",
    "-> Photonic Supersolid Nature Paper",
    # extras if some fail (still pilot-scoped)
    "-> Quantum Metallurgy: CDW Electron Crystals Melt",
    "Quantum Field Theory Basics -  car",
    "Cooper Pairs in Superconductivity Explained",
    "η'-Mesic Nuclei Discovery at GSI",
]

# Cleaning patterns
URL_LINE = re.compile(r"^\s*https?://\S+\s*$", re.M)
MULTI_URL = re.compile(r"https?://\S+")
# strip common web chrome blocks
CHROME_BLOCKS = re.compile(
    r"(?is)(?:Open in app|Accept (?:all )?cookies|Cookie Policy|"
    r"Sign in|Subscribe|Advertisement|Related articles|"
    r"Skip to content|Share this article).{0,200}"
)
THINKING = re.compile(r"(?is)Thinking\.\.\..{0,500}?(?=\n\n|\Z)")
TOOL_MARKERS = re.compile(
    r"(?is)<xai:[^>]+>|web_search\(|browse_page\(|tool_use|function_call|"
    r"```(?:json)?\s*\{[^}]{0,200}\"tool\""
)
# Grok image/search cards embedded as XML-ish tags
GROK_RENDER = re.compile(r"(?is)<grok:render\b[^>]*>.*?</grok:render>|<grok:render\b[^/]*/>")
GROK_TAGS = re.compile(r"(?is)</?grok:[^>]+>")
MULTI_NL = re.compile(r"\n{4,}")
CITATION_JUNK = re.compile(r"\[\d{1,3}\]\s*https?://\S+")


def slugify(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"^->\s*", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:60] or "untitled"


def clean_text(text: str) -> str:
    if not text:
        return ""
    t = text.replace("\r\n", "\n")
    t = GROK_RENDER.sub("", t)
    t = GROK_TAGS.sub("", t)
    t = THINKING.sub("", t)
    t = TOOL_MARKERS.sub("", t)
    t = CHROME_BLOCKS.sub("", t)
    t = CITATION_JUNK.sub("", t)
    # collapse bare URL-only lines
    t = URL_LINE.sub("", t)
    # shorten long URL runs but keep one if mid-sentence? drop bare urls
    t = MULTI_URL.sub("[url]", t)
    t = MULTI_NL.sub("\n\n", t)
    return t.strip()


def extract_messages(conv_obj: dict) -> list[tuple[str, str]]:
    """Return list of (sender, cleaned_message) in path order if possible."""
    resps = conv_obj.get("responses") or []
    # Build by create time when available
    items = []
    for r in resps:
        resp = r.get("response") or {}
        sender = (resp.get("sender") or "unknown").strip().lower()
        # normalize roles
        if sender in ("assistant", "grok", "bot", "model"):
            sender = "assistant"
        elif sender in ("human", "user"):
            sender = "human"
        msg = resp.get("message") or ""
        ct = resp.get("create_time")
        if isinstance(ct, dict):
            ts = str(ct.get("$date") or ct.get("date") or ct)
        elif ct is None:
            ts = ""
        else:
            ts = str(ct)
        items.append((ts, sender, msg))
    # stable order: sort by timestamp string; empty timestamps keep relative order
    items.sort(key=lambda x: (x[0] == "", x[0]))
    out = []
    for _, sender, msg in items:
        cleaned = clean_text(msg)
        if not cleaned:
            continue
        # drop pure chit-chat ultra-short assistant acks
        if sender == "assistant" and len(cleaned) < 40 and not re.search(
            r"\$|equation|theorem|paper|energy|quantum|field", cleaned, re.I
        ):
            continue
        if sender == "human" and len(cleaned) < 5:
            continue
        out.append((sender, cleaned))
    return out


def is_usable(messages: list[tuple[str, str]], min_asst_chars: int = 3000) -> bool:
    asst = sum(len(m) for s, m in messages if s == "assistant")
    return asst >= min_asst_chars and len(messages) >= 2


def main() -> None:
    data = json.loads(BACKEND.read_text(encoding="utf-8"))
    by_title = {}
    for c in data["conversations"]:
        title = (c["conversation"].get("title") or "").strip()
        by_title[title] = c
        # also store without trailing space variants
        by_title[title.rstrip()] = c

    report = {
        "pilot_requested": 15,
        "found": 0,
        "usable": 0,
        "files": [],
        "skipped": [],
        "noise_stats": [],
    }

    for title in PILOT_TITLES:
        if report["usable"] >= 15:
            break
        c = by_title.get(title) or by_title.get(title.strip())
        if not c:
            # fuzzy
            hits = [k for k in by_title if title.strip().lower() in k.lower()]
            c = by_title[hits[0]] if hits else None
            title_used = hits[0] if hits else title
        else:
            title_used = title

        if not c:
            report["skipped"].append({"title": title, "reason": "not found"})
            continue

        report["found"] += 1
        meta = c["conversation"]
        cid = meta["id"]
        create = (meta.get("create_time") or "")[:10]
        raw_msgs = c.get("responses") or []
        raw_chars = sum(len((r.get("response") or {}).get("message") or "") for r in raw_msgs)
        messages = extract_messages(c)
        clean_chars = sum(len(m) for _, m in messages)
        removed = max(0, raw_chars - clean_chars)
        frac_removed = (removed / raw_chars) if raw_chars else 0

        if not is_usable(messages):
            report["skipped"].append(
                {
                    "title": title_used,
                    "reason": "thin after clean",
                    "asst_chars": sum(len(m) for s, m in messages if s == "assistant"),
                }
            )
            report["noise_stats"].append(
                {
                    "title": title_used,
                    "raw_chars": raw_chars,
                    "clean_chars": clean_chars,
                    "frac_removed": round(frac_removed, 3),
                    "usable": False,
                }
            )
            continue

        h = hashlib.sha1(cid.encode()).hexdigest()[:8]
        slug = slugify(title_used)
        fname = f"{create}_{slug}_{h}.md"
        path = OUT_DIR / fname

        # build markdown
        lines = [
            "---",
            "source: spacex_export",
            f"conversation_id: {cid}",
            f'title: "{title_used.replace(chr(34), chr(39))}"',
            f"created_at: {meta.get('create_time')}",
            f"updated_at: {meta.get('modify_time')}",
            f"n_responses: {len(raw_msgs)}",
            "platform: grok/xAI",
            "pilot: true",
            "---",
            "",
            f"# {title_used}",
            "",
        ]
        for sender, msg in messages:
            role = "Human" if sender == "human" else "Assistant"
            lines.append(f"## {role}")
            lines.append("")
            lines.append(msg)
            lines.append("")

        path.write_text("\n".join(lines), encoding="utf-8")
        report["usable"] += 1
        report["files"].append(
            {
                "file": fname,
                "title": title_used,
                "bytes": path.stat().st_size,
                "raw_chars": raw_chars,
                "clean_chars": clean_chars,
                "frac_removed": round(frac_removed, 3),
                "n_messages_kept": len(messages),
            }
        )
        report["noise_stats"].append(
            {
                "title": title_used,
                "raw_chars": raw_chars,
                "clean_chars": clean_chars,
                "frac_removed": round(frac_removed, 3),
                "usable": True,
            }
        )
        print("OK", fname, f"removed={frac_removed:.1%}", f"bytes={path.stat().st_size}")

    # quality report
    avg_rm = 0.0
    if report["noise_stats"]:
        avg_rm = sum(x["frac_removed"] for x in report["noise_stats"]) / len(
            report["noise_stats"]
        )

    qr = []
    qr.append("# SpaceX export pilot — quality report\n\n")
    qr.append("**Date:** 2026-08-04  \n")
    qr.append("**Scope:** Pilot only (15 targeted physics conversations). No wiki ingest.\n\n")
    qr.append("## Counts\n\n")
    qr.append(f"- Requested pilot titles: {report['pilot_requested']}\n")
    qr.append(f"- Found in export: {report['found']}\n")
    qr.append(f"- Usable analyses written: {report['usable']}\n")
    qr.append(f"- Skipped: {len(report['skipped'])}\n")
    qr.append(f"- Output dir: `spacex_export/extracted-analyses/`\n\n")
    qr.append("## Noise removal\n\n")
    qr.append(f"- Mean fraction of characters removed by cleaning: **{avg_rm:.1%}**\n")
    qr.append(
        "- Cleaning removed: bare URL lines, `[n] url` citation tails, Thinking blocks, "
        "tool-marker stubs, common web chrome phrases; collapsed excess blank lines.\n"
    )
    qr.append(
        "- This Grok dump has **empty response.metadata** objects — little structured tool noise "
        "compared to Claude `content[]` thinking/tool_use blocks. Residual noise is mostly "
        "URLs and browse leftovers inside assistant prose.\n\n"
    )
    qr.append("## Structural differences from Claude export\n\n")
    qr.append("| | Claude export | Grok / SpaceX export |\n| --- | --- | --- |\n")
    qr.append("| Payload | `conversations.json` array | `prod-grok-backend.json` object |\n")
    qr.append("| Message shape | `content[]` typed blocks | flat `message` string |\n")
    qr.append("| Roles | user/assistant via messages | `sender`: human/assistant |\n")
    qr.append("| Titles | often in `name` | `conversation.title` |\n")
    qr.append("| Assets | rare | large `prod-mc-asset-server` binary tree |\n")
    qr.append("| Auth/billing | n/a | separate small JSON (ignored) |\n\n")
    qr.append("## Files written\n\n")
    qr.append("| File | Title | Clean chars | % removed |\n| --- | --- | ---: | ---: |\n")
    for f in report["files"]:
        qr.append(
            f"| `{f['file']}` | {f['title'].replace('|','/')} | {f['clean_chars']} | {100*f['frac_removed']:.1f}% |\n"
        )
    if report["skipped"]:
        qr.append("\n## Skipped\n\n")
        for s in report["skipped"]:
            qr.append(f"- {s}\n")
    qr.append("\n## Notes for full extraction (pending approval)\n\n")
    qr.append(
        "- Full pass should use a **title + body classifier** that excludes medical/digestive, "
        "music/MSL, pure tooling (Obsidian/Grok Build), and Tesla/consumer chat.\n"
    )
    qr.append(
        "- Many physics titles already overlap wiki topics (Hawking shell, ion clocks, cats, supersolid) — "
        "dedupe against `wiki/papers/` at ingest time, not at extract time.\n"
    )
    qr.append(
        "- Large multi-topic mega-chats (`I - Astrophysics`, `I - QM & QFT`) may need "
        "section-splitting later; pilot keeps one file per conversation.\n"
    )
    qr.append("\n**STOP:** Pilot complete. Await explicit approval before full extraction.\n")

    (ROOT / "spacex_export" / "PILOT_REPORT.md").write_text("".join(qr), encoding="utf-8")
    (ROOT / "spacex_export" / "PILOT_MANIFEST.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )
    print("Usable:", report["usable"])
    print("Report: spacex_export/PILOT_REPORT.md")


if __name__ == "__main__":
    main()
