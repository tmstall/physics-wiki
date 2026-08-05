"""Full extraction of physics conversations from SpaceX/xAI Grok export."""
from __future__ import annotations

import hashlib
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
OUT_DIR = ROOT / "spacex_export" / "extracted-analyses"
OUT_DIR.mkdir(parents=True, exist_ok=True)
SPACEX = ROOT / "spacex_export"

# --- cleaning (same discipline as pilot) ---
URL_LINE = re.compile(r"^\s*https?://\S+\s*$", re.M)
MULTI_URL = re.compile(r"https?://\S+")
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
GROK_RENDER = re.compile(
    r"(?is)<grok:render\b[^>]*>.*?</grok:render>|<grok:render\b[^/]*/>"
)
GROK_TAGS = re.compile(r"(?is)</?grok:[^>]+>")
MULTI_NL = re.compile(r"\n{4,}")
CITATION_JUNK = re.compile(r"\[\d{1,3}\]\s*https?://\S+")

# --- denylist (title + sample) ---
DENY = re.compile(
    r"(?i)"
    r"("
    r"digestive|constipat|electrolyte|transplant|cardio|heart failure|"
    r"imodium|catheter|hypothyroid|restless leg|palliative|medication list|"
    r"medicare|psychosocial evaluation|high-protein diet|water intake|"
    r"celtic salt|low-residue|gi management|personal medical|mack.?s recovery|"
    r"medicine\s*-\s*transplant|"
    # music / audio
    r"\bMSL\b|master set list|audiophile|playlist|sonus|rotel|sacred vocal|"
    r"genesis lamb|harmonic frequency relationships|harmonics vs fundamental|"
    r"music\s*-|immersive sound|sphere\b.*sound|"
    # consumer / tesla / chrome
    r"tesla|model 3|garage door|pixel 9|lenovo|chrome true key|true key|"
    r"bitwarden|netflix|roon usb|samsung t7|browseros|wifi remote|"
    r"office chair|le creuset|food cart|apple|novara rei|jacket|"
    r"epstein|kaitlyn|claire mckinley|cat microchip|kitty discussion|"
    r"ohm hrv|resonance lamp|"
    # pure tooling / wiki meta / non-physics agent work
    r"obsidian|grok build|grok project|grok custom instructions|"
    r"custom instructions|prompt engineering|prompt (fix|update|improvement)|"
    r"framework for analyzing|technical paper analysis framework|"
    r"paper analysis framework|msl v3|working with grok|"
    r"wsl ubuntu|open browser|convert odt|markdown to pdf|python script md|"
    r"gmail connector|context rot|preventing context rot|j-space in large language|"
    r"exporting passwords|mounting usb|ubuntu|"
    r"empty conversation|audio conversation|continuing previous chat|"
    r"custom physics analyzer (agent|prompt)|"  # meta prompt work, not physics content
    r"netfix suggestions|"
    r"american style tai chi|cognitive diffusion|engineers.? research on anxiety|"
    r"ai rising|meaning of tallulah|diet\b"
    r")"
)

# Strong physics title cues (prefer keep if title matches and not denied)
PHYS_TITLE = re.compile(
    r"(?i)"
    r"("
    r"quantum|qft|qed|qcd|qgp|quark|gluon|black.?hole|hawking|cosmo|gravit|"
    r"relativity|riemann|einstein|spacetime|photon|entangl|plasma|nuclear|"
    r"neutron|proton|hadron|baryon|lepton|meson|anyon|superconduct|superfluid|"
    r"bec\b|bose|fermion|condensed|metallurgy|cdw|magnon|phonon|spin network|"
    r"spin foam|holograph|decoherence|measurement|collapse|proper.?time|"
    r"ion clock|schr.?dinger|noon|tunnel|casimir|bell |shor|cavity|"
    r"jwst|ligo|pulsar|magnetar|quasar|agn|blazar|mond|dark matter|"
    r"dark energy|axion|cmb|cosmic web|supernova|pulsar|lmc |"
    r"warp drive|warp |metric|gauge|symmetry|vacuum|instanton|eta.?prime|"
    r"mesic|theta.?vacua|θ-vacua|perovskite|moir|motte|graphene|nickelate|"
    r"diamond|siv |snv |tin-vacancy|attosecond|femtosecond|photoemission|"
    r"evanescent|brillouin|optical|laser pulse|carrier-envelope|"
    r"astrophys|particle physics|field theory|high-pT|high-pt|isr |"
    r"rhic|net-proton|emc effect|ionization|ulirg|fuor|iras |"
    r"heliknoton|dust shield|clathrate|trinity test|calcium monohydride|"
    r"hydroamination|electro-viscoelastic|microfluidic|"
    r"1d anyon|momentum tails|squeezed state|two-mode|"
    r"photonic supersolid|truncated photon|cluster tunneling|"
    r"materials science|semiconductor|nanostructure|"
    r"nuclear magnetization|massive gravity|cooper pair|"
    r"delayed-choice|quantum eraser|positronium|antimatter|"
    r"fractional charge|anyon-trion|supermoir|trilayer|"
    r"error-correcting cosmolog|holographic universe|"
    r"temporal imbalance|spin-momentum|virtual particle|"
    r"color vision|schrödinger.?s geometric|"
    r"general physics|physics\b|chemistry\b|biology/microscopy|"
    r"astronomy|cosmology advances|"
    r"qmm\b|quantum memory matrix|"
    r"neural net cosmolog|programmable kinetic|"  # borderline
    r"euclid images technical|"
    r"analyze paper|paper analysis request|"
    r"technical paper discussion|"
    r"recent quantum mechanics|"
    r"vector potential|five-dimensional classical gravity|"
    r"liquids pin bio-friendly|"  # physics of constants
    r"symmetry stretches attosecond|"
    r"generation v3\.4|v3\.4\.[0-9].*holographic|v3\.4\.[0-9].*evanescent|"
    r"prompt improvement.*photoemission|"  # often paper analysis with framework
    r"loki:|chondrite|pressure bump|"  # wiki-related science
    r"boronate|cas13a|"  # may be chemistry islands - still technical
    r"magnesium-promoted benzidine|"
    r"sub-2.*cryo-em|"
    r"rna polymerase|"
    r"flexible electrodynamic dust|"
    r"laboratory suppression of blazar|"
    r"long-term timing of psr|"
    r"muse captures|"
    r"ice core traces supernova|"
    r"early universe ionization|"
    r"black holes evaporate|"
    r"evaporating charged|"
    r"ultramassive black hole|"
    r"siv centers|"
    r"photonic supersolid|"
    r"quantum metallurgy|"
    r"quantum proper time|"
    r"collapse, gravity|"
    r"high-pt jets|"
    r"cosmic web|"
    r"single pressure bump|"
    r"η'|eta-prime|theta-vacua|θ-vacua"
    r")"
)

# Body sample physics (weaker) — require more substance
PHYS_BODY = re.compile(
    r"(?i)(hamiltonian|lagrangian|hilbert|schrödinger|schrodinger|"
    r"wavefunction|path integral|renormaliz|feynman|gauge field|"
    r"event horizon|schwarzschild|kerr |metric tensor|"
    r"hawking temperature|bogoliubov|einstein equation|"
    r"quantum field|condensed matter|superconduct|anyon|"
    r"lattice qcd|quark-gluon|neutron star|pulsar timing|"
    r"arXiv|Phys\. Rev|Nature |Science |PRL )"
)

MIN_ASST_CHARS = 2500  # after clean
MIN_MSGS = 2


def slugify(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"^->\s*", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return (s.strip("-") or "untitled")[:60]


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
    t = URL_LINE.sub("", t)
    t = MULTI_URL.sub("[url]", t)
    t = MULTI_NL.sub("\n\n", t)
    return t.strip()


def extract_messages(conv_obj: dict) -> list[tuple[str, str]]:
    items = []
    for r in conv_obj.get("responses") or []:
        resp = r.get("response") or {}
        sender = (resp.get("sender") or "unknown").strip().lower()
        if sender in ("assistant", "grok", "bot", "model", "grok-4"):
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
    items.sort(key=lambda x: (x[0] == "", x[0]))
    out = []
    for _, sender, msg in items:
        cleaned = clean_text(msg)
        if not cleaned:
            continue
        if sender == "assistant" and len(cleaned) < 40 and not re.search(
            r"\$|equation|theorem|paper|energy|quantum|field", cleaned, re.I
        ):
            continue
        if sender == "human" and len(cleaned) < 5:
            continue
        out.append((sender, cleaned))
    return out


def topic_tags(title: str, sample: str) -> list[str]:
    blob = (title + " " + sample[:2000]).lower()
    tags = []
    rules = [
        ("qft", r"quantum field|qft|qed|virtual particle|feynman|gauge"),
        ("gravity-bh", r"black.?hole|hawking|horizon|gravastar|kerr|schwarzschild|evaporat"),
        ("relativity", r"relativity|riemann|einstein|spacetime|metric|warp"),
        ("cosmology", r"cosmo|dark energy|dark matter|cmb|jwst|cosmic web|inflation|holographic cosm"),
        ("condensed-matter", r"superconduct|cdw|graphene|moir|nickelate|magnon|phonon|bec|superfluid|anyons"),
        ("quantum-foundations", r"collapse|measurement|decoherence|everett|bohm|born|proper.?time|weak value"),
        ("quantum-info", r"entangl|qubit|squeez|bell |shor|quantum information"),
        ("nuclear-particle", r"nuclear|quark|gluon|qgp|hadron|rhic|meson|eta.?prime|high-pt|isr"),
        ("astro", r"pulsar|magnetar|supernova|quasar|agn|blazar|neutron star|lmc|fuor"),
        ("amo-optics", r"laser|attosecond|femtosecond|photon|optical|ion clock|cavity|siv |snv "),
        ("materials", r"materials|semiconductor|nanostructure|diamond|perovskite|clathrate"),
        ("math-methods", r"homology|topology|spin network|spin foam|matrix"),
        ("chemistry", r"chemistry|hydroamination|benzidine|polymerase|cas13a|boronate"),
        ("biophysics", r"cryo-em|microscopy|biology"),
    ]
    for tag, pat in rules:
        if re.search(pat, blob, re.I):
            tags.append(tag)
    return tags or ["physics-general"]


def classify(title: str, sample: str, asst_chars: int) -> tuple[str | None, str]:
    """Return (keep_reason or None, discard_reason)."""
    t = title or ""
    blob = t + "\n" + sample[:3000]

    if DENY.search(t):
        return None, "denylist-title"
    if DENY.search(sample[:1500]) and not PHYS_TITLE.search(t):
        # body looks medical/tooling and title not physics
        if re.search(
            r"(?i)constipat|electrolyte|transplant|digestive|playlist|tesla model",
            sample[:2000],
        ):
            return None, "denylist-body"

    # explicit empty / noise
    if re.search(r"(?i)^empty conversation|^audio conversation$", t.strip()):
        return None, "empty-or-audio"
    if asst_chars < MIN_ASST_CHARS:
        return None, "too-thin"

    if PHYS_TITLE.search(t):
        return "title-physics", ""
    if PHYS_BODY.search(blob) and asst_chars >= 5000:
        return "body-physics-substance", ""
    if re.search(r"(?i)^->\s+", t) and asst_chars >= MIN_ASST_CHARS:
        # paper-analysis style arrows — keep if not denied
        if not DENY.search(blob[:800]):
            return "arrow-paper-analysis", ""

    return None, "not-physics"


def already_extracted_ids() -> set[str]:
    ids = set()
    for p in OUT_DIR.glob("*.md"):
        head = p.read_text(encoding="utf-8", errors="replace")[:800]
        m = re.search(r"conversation_id:\s*(\S+)", head)
        if m:
            ids.add(m.group(1).strip())
    return ids


def write_md(meta: dict, messages: list[tuple[str, str]], n_raw: int, pilot: bool) -> Path:
    cid = meta["id"]
    title = meta.get("title") or "untitled"
    create = (meta.get("create_time") or "")[:10] or "undated"
    h = hashlib.sha1(cid.encode()).hexdigest()[:8]
    fname = f"{create}_{slugify(title)}_{h}.md"
    path = OUT_DIR / fname
    # avoid overwrite of different id same slug
    if path.exists():
        old = path.read_text(encoding="utf-8", errors="replace")[:500]
        if cid not in old:
            fname = f"{create}_{slugify(title)}_{h}b.md"
            path = OUT_DIR / fname

    lines = [
        "---",
        "source: spacex_export",
        f"conversation_id: {cid}",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f"created_at: {meta.get('create_time')}",
        f"updated_at: {meta.get('modify_time')}",
        f"n_responses: {n_raw}",
        "platform: grok/xAI",
        f"pilot: {str(pilot).lower()}",
        "---",
        "",
        f"# {title}",
        "",
    ]
    for sender, msg in messages:
        role = "Human" if sender == "human" else "Assistant"
        lines.append(f"## {role}")
        lines.append("")
        lines.append(msg)
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> None:
    data = json.loads(BACKEND.read_text(encoding="utf-8"))
    convs = data["conversations"]
    existing = already_extracted_ids()

    manifest_entries = []
    discard_reasons: Counter[str] = Counter()
    topic_counter: Counter[str] = Counter()
    kept = discarded = 0
    new_files = 0
    pilot_in_manifest = 0

    # Include existing pilot files in manifest
    for p in sorted(OUT_DIR.glob("*.md")):
        head = p.read_text(encoding="utf-8", errors="replace")
        m_id = re.search(r"conversation_id:\s*(\S+)", head)
        m_title = re.search(r'(?m)^title:\s*"(.*)"\s*$', head)
        m_pilot = re.search(r"(?m)^pilot:\s*(\w+)", head)
        cid = m_id.group(1) if m_id else ""
        title = m_title.group(1) if m_title else p.stem
        body = re.sub(r"^---.*?---\s*", "", head, count=1, flags=re.S)
        clean_chars = len(body)
        tags = topic_tags(title, body)
        for t in tags:
            topic_counter[t] += 1
        is_pilot = (m_pilot.group(1).lower() == "true") if m_pilot else True
        if is_pilot:
            pilot_in_manifest += 1
        manifest_entries.append(
            {
                "conversation_id": cid,
                "original_title": title,
                "cleaned_filename": p.name,
                "topic_tags": tags,
                "raw_chars": None,  # filled if we re-scan
                "clean_chars": clean_chars,
                "file_bytes": p.stat().st_size,
                "pilot": is_pilot,
                "status": "already_on_disk",
            }
        )

    existing_files = {e["cleaned_filename"] for e in manifest_entries}
    existing_ids = {e["conversation_id"] for e in manifest_entries if e["conversation_id"]}

    for c in convs:
        meta = c["conversation"]
        cid = meta["id"]
        title = meta.get("title") or ""
        resps = c.get("responses") or []
        n_raw = len(resps)

        # raw char count
        raw_chars = sum(len((r.get("response") or {}).get("message") or "") for r in resps)

        # sample for classification
        sample_parts = []
        for r in resps[:8]:
            sample_parts.append((r.get("response") or {}).get("message") or "")
        sample = "\n".join(sample_parts)

        # quick asst estimate after clean on sample + full if needed
        messages = extract_messages(c)
        asst_chars = sum(len(m) for s, m in messages if s == "assistant")
        clean_chars = sum(len(m) for _, m in messages)

        keep_reason, discard_reason = classify(title, sample, asst_chars)

        if cid in existing_ids:
            # update raw_chars on existing manifest entry
            for e in manifest_entries:
                if e["conversation_id"] == cid:
                    e["raw_chars"] = raw_chars
                    e["clean_chars"] = clean_chars or e["clean_chars"]
                    e["keep_reason"] = "pilot-or-prior"
                    e["frac_removed"] = (
                        round(1 - (e["clean_chars"] / raw_chars), 4) if raw_chars else 0
                    )
                    break
            kept += 1
            continue

        if not keep_reason:
            discarded += 1
            discard_reasons[discard_reason] += 1
            continue

        if len(messages) < MIN_MSGS or asst_chars < MIN_ASST_CHARS:
            discarded += 1
            discard_reasons["too-thin-after-clean"] += 1
            continue

        path = write_md(meta, messages, n_raw, pilot=False)
        new_files += 1
        kept += 1
        tags = topic_tags(title, "\n".join(m for _, m in messages[:5]))
        for t in tags:
            topic_counter[t] += 1
        frac = round(1 - (clean_chars / raw_chars), 4) if raw_chars else 0.0
        manifest_entries.append(
            {
                "conversation_id": cid,
                "original_title": title,
                "cleaned_filename": path.name,
                "topic_tags": tags,
                "raw_chars": raw_chars,
                "clean_chars": clean_chars,
                "file_bytes": path.stat().st_size,
                "frac_removed": frac,
                "n_messages_kept": len(messages),
                "n_responses_raw": n_raw,
                "keep_reason": keep_reason,
                "pilot": False,
                "status": "extracted",
                "create_time": meta.get("create_time"),
            }
        )
        print(f"OK {path.name} tags={tags} rm={frac:.1%}")

    # totals examined
    total = len(convs)
    # recompute kept as unique extracted files on disk
    on_disk = list(OUT_DIR.glob("*.md"))
    n_disk = len(on_disk)

    # fill raw_chars for pilot entries missing it
    id_to_raw = {}
    for c in convs:
        cid = c["conversation"]["id"]
        raw = sum(len((r.get("response") or {}).get("message") or "") for r in c.get("responses") or [])
        id_to_raw[cid] = raw
    for e in manifest_entries:
        if e.get("raw_chars") is None and e.get("conversation_id") in id_to_raw:
            e["raw_chars"] = id_to_raw[e["conversation_id"]]
            if e["raw_chars"] and e.get("clean_chars"):
                e["frac_removed"] = round(1 - e["clean_chars"] / e["raw_chars"], 4)

    manifest = {
        "source": "SpaceX_exported_data / prod-grok-backend.json",
        "extracted_at": "2026-08-04",
        "total_conversations_examined": total,
        "kept_count": n_disk,
        "newly_extracted_this_run": new_files,
        "discarded_count": discarded,
        "discard_reasons": dict(discard_reasons),
        "topic_distribution": dict(topic_counter.most_common()),
        "entries": sorted(
            manifest_entries,
            key=lambda e: (e.get("create_time") or e.get("cleaned_filename") or ""),
        ),
    }
    (SPACEX / "FULL_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # report
    avg_rm = []
    for e in manifest_entries:
        if e.get("frac_removed") is not None:
            avg_rm.append(e["frac_removed"])
        elif e.get("raw_chars") and e.get("clean_chars"):
            avg_rm.append(1 - e["clean_chars"] / e["raw_chars"])

    lines = []
    lines.append("# SpaceX export — full extraction report\n\n")
    lines.append("**Date:** 2026-08-04  \n")
    lines.append("**Scope:** Full physics extraction (no wiki ingest).  \n")
    lines.append("**Source:** `SpaceX_exported_data/.../prod-grok-backend.json`  \n")
    lines.append("**Output:** `spacex_export/extracted-analyses/`  \n")
    lines.append("**Manifest:** `spacex_export/FULL_MANIFEST.json`\n\n")
    lines.append("## Counts\n\n")
    lines.append(f"| Metric | Count |\n| --- | ---: |\n")
    lines.append(f"| Conversations examined | {total} |\n")
    lines.append(f"| Kept (files on disk) | {n_disk} |\n")
    lines.append(f"| Newly extracted this run | {new_files} |\n")
    lines.append(f"| Pilot files already present | {pilot_in_manifest} |\n")
    lines.append(f"| Discarded this run | {discarded} |\n")
    lines.append("\n### Discard reasons\n\n")
    lines.append("| Reason | Count |\n| --- | ---: |\n")
    for reason, n in discard_reasons.most_common():
        lines.append(f"| {reason} | {n} |\n")
    lines.append("\n### Topic distribution (tag hits; multi-tag per file)\n\n")
    lines.append("| Tag | Count |\n| --- | ---: |\n")
    for tag, n in topic_counter.most_common():
        lines.append(f"| {tag} | {n} |\n")
    if avg_rm:
        lines.append(f"\n## Cleaning quality\n\n")
        lines.append(f"- Mean fraction removed (where measured): **{sum(avg_rm)/len(avg_rm):.1%}**\n")
        lines.append(
            "- Same pilot discipline: role normalization (`ASSISTANT`→assistant), "
            "`<grok:render>` strip, URL/chrome cleanup, thin-ack drop.\n"
        )
    lines.append("\n## Filter policy\n\n")
    lines.append("**Keep:** title physics cues, arrow paper-analyses, or strong body physics + substance.  \n")
    lines.append(
        "**Discard:** medical/digestive/transplant/electrolyte, music/MSL, Tesla/consumer, "
        "pure tooling/Obsidian/Grok Build/prompt meta, empty/audio, too-thin.\n"
    )
    lines.append("\n## Structural notes / surprises\n\n")
    lines.append(
        "- Sender case split (`assistant` vs `ASSISTANT`) remains real; full extract normalizes both.\n"
    )
    lines.append(
        "- Deepsearch metadata is common but not required for cleaning; science lives in `message` strings.\n"
    )
    lines.append(
        "- Mega-threads (astro, QFT learning series) stay as **one file per conversation** "
        "(no section split in this pass).\n"
    )
    lines.append(
        "- Soft wiki overlaps expected (Hawking shell, ion clocks, cats, supersolid, CDW, η′, etc.) — "
        "left for **ingest-time** dedupe.\n"
    )
    lines.append(
        "- Chemistry/biotech islands kept when clearly technical (e.g. benzidine, cryo-EM) "
        "and not medical protocol series.\n"
    )
    lines.append("\n## Status\n\n")
    lines.append("**Extraction complete.** Wiki directory was not modified.\n")
    lines.append("Ready for a separate ingest pass on approval.\n")

    (SPACEX / "FULL_EXTRACTION_REPORT.md").write_text("".join(lines), encoding="utf-8")
    print("---")
    print("examined", total, "on_disk", n_disk, "new", new_files, "discarded", discarded)
    print("report", SPACEX / "FULL_EXTRACTION_REPORT.md")


if __name__ == "__main__":
    main()
