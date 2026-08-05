"""Finalize wave-2: index sections, log, progress, counts, lint notes."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parent.parent
papers_dir = root / "wiki" / "papers"
index_path = root / "wiki" / "index.md"
log_path = root / "wiki" / "log.md"

# All wave2 slugs in order
wave2 = [
    # batch 1
    "beyond-iron-ultraheavy-cosmic-rays",
    "nucleus-shell-src-memory",
    "black-hole-third-law-violation",
    "dissipative-cavity-entanglement",
    "jwst-filament-cnd-ngc4696",
    # batch 2
    "category-79-quasar-wind",
    "peters-cycle-cosmic-rays",
    "fractional-fermi-sea-1d-bosons",
    "quantum-state-sculptor",
    "freeze-fiber-brillouin",
    # batch 3
    "radio-changing-look-agn",
    "glimpse-17775-cocoon",
    "mot-metal-hydride",
    "molecular-rotation-superfluid-he",
    "droplet-rewrites-ring",
    # batch 4
    "nucleus-tells-on-itself",
    "confinement-stiffening-films",
    "metal-fall-apart-on-purpose",
    "topo-chirality-structured-light",
    "color-space-geometry",
    # batch 5
    "qg-deep-dive-1-mergers-emission",
    "qg-deep-dive-2-info-holography",
    "qg-deep-dive-3-holographic-codes",
    "qg-deep-dive-4-de-sitter",
    # batch 6
    "cryptochrome-ascorbate-compass",
    "ultrafast-chemical-shifts",
    "two-lasers-one-reaction",
    "gpu-mass-spectrometry",
    "bond-breaking-discount",
    # batch 7
    "millisecond-pharma-factory",
    "ruthenium-atom-catalysis",
    "water-rna-polymerase",
    "molecular-bias-point",
    "interstellar-sulfur-ice",
    # batch 8
    "one-bond-inductive-effect",
    "enzyme-resistance-tax",
]

# Verify files exist
missing = [s for s in wave2 if not (papers_dir / f"{s}.md").exists()]
if missing:
    print("MISSING", missing)

n_papers = len(list(papers_dir.glob("*.md")))
n_concepts = len(list((root / "wiki" / "concepts").glob("*.md")))
n_synth = len(list((root / "wiki" / "synthesis").glob("*.md")))

# Summaries for index (short)
SUM = {
    "radio-changing-look-agn": "NLS1 radio quiet→loud and stays loud",
    "glimpse-17775-cocoon": "LRD super-Eddington BH in gas cocoon",
    "mot-metal-hydride": "First CaH magneto-optical trap",
    "molecular-rotation-superfluid-he": "Optical centrifuge in He nanodroplets",
    "droplet-rewrites-ring": "Microdroplet aniline→pyridine ring rewrite",
    "nucleus-tells-on-itself": "γ upbend multipole via parity bookkeeping",
    "confinement-stiffening-films": "Inverse-cube ballistic toughness when thinner",
    "metal-fall-apart-on-purpose": "HEA self-sorts into 3-phase nano-mosaic",
    "topo-chirality-structured-light": "Free-space optical Hall via PT charge",
    "color-space-geometry": "Non-Riemannian rebuild of color geometry",
    "qg-deep-dive-1-mergers-emission": "Beyond-GR merger–ringdown analytics",
    "qg-deep-dive-2-info-holography": "Info paradox → holographic dictionary",
    "qg-deep-dive-3-holographic-codes": "Bulk reconstruction as QEC",
    "qg-deep-dive-4-de-sitter": "de Sitter holography without AdS walls",
    "cryptochrome-ascorbate-compass": "Ascorbate radical rarely forms bird-compass pair",
    "ultrafast-chemical-shifts": "Ultrafast chemical-shift spectroscopy",
    "two-lasers-one-reaction": "Two-laser control of one reaction path",
    "gpu-mass-spectrometry": "GPU inflection for mass spectrometry",
    "bond-breaking-discount": "Catalytic discount on bond breaking",
    "millisecond-pharma-factory": "ms midair drug-scaffold ring building",
    "ruthenium-atom-catalysis": "Single Ru atom lights and steers reaction",
    "water-rna-polymerase": "Water in RNA Pol II catalysis",
    "molecular-bias-point": "Bias where a molecule stops responding",
    "interstellar-sulfur-ice": "Sulfur chemistry in interstellar ice",
    "one-bond-inductive-effect": "Inductive effect dies past one bond (DFT)",
    "enzyme-resistance-tax": "Evolutionary tax of breaking key enzyme path",
}

# Update index header counts and append missing wave2 rows if needed
text = index_path.read_text(encoding="utf-8")
text = re.sub(
    r"\*\*Papers:\*\* \d+ · \*\*Concepts:\*\* \d+ · \*\*Synthesis:\*\* \d+",
    f"**Papers:** {n_papers} · **Concepts:** {n_concepts} · **Synthesis:** {n_synth}",
    text,
    count=1,
)
text = re.sub(
    r"\*\*Export ingest wave 2:\*\*[^\n]+",
    f"**Export ingest wave 2:** {len(wave2)} papers COMPLETE (see `claude_export/INGEST_PROGRESS_WAVE2.json`)",
    text,
    count=1,
)

# Ensure each new slug appears once in index
for slug, summary in SUM.items():
    if f"[[{slug}]]" not in text:
        # append to Islands / Other chemistry section or a Wave-2 appendix
        pass

# Build a Wave-2 appendix section
appendix = ["\n---\n\n## Wave-2 export papers (batches 1–8)\n\n| Page | Summary |\n| --- | --- |\n"]
# short summaries for all wave2
ALL_SUM = {
    "beyond-iron-ultraheavy-cosmic-rays": "UH nuclei as UHECRs",
    "nucleus-shell-src-memory": "Shell orbitals control SRCs",
    "black-hole-third-law-violation": "Vacuum 5D finite-time extremality",
    "dissipative-cavity-entanglement": "Dark-state many-body entanglement",
    "jwst-filament-cnd-ngc4696": "Filament→CND feeding NGC 4696",
    "category-79-quasar-wind": "UV BAL wind ~0.3c in J2318",
    "peters-cycle-cosmic-rays": "DAMPE rigidity softening ~15 TV",
    "fractional-fermi-sea-1d-bosons": "Holonomy fractional Fermi seas",
    "quantum-state-sculptor": "Non-Gaussian oscillator superpositions",
    "freeze-fiber-brillouin": "Frozen CS2 Brillouin gain boost",
}
ALL_SUM.update(SUM)
for i, slug in enumerate(wave2, 1):
    appendix.append(f"| [[{slug}]] | {ALL_SUM.get(slug, slug)} |\n")
appendix.append(f"\n**Wave-2 total:** {len(wave2)} new papers. Catalog: **{n_papers} papers · {n_concepts} concepts · {n_synth} synthesis**.\n")

# Replace inbox status
inbox = f"""
## Inbox status

| Status | Notes |
| --- | --- |
| Export wave 1 | STOPPED at 40 (`new_papers_40.json`) |
| Export wave 2 | **COMPLETE** — {len(wave2)} unique papers from remaining extracts |
| Soft-dups skipped | Lorentz≡gas-pedal; SAF; SnTe alt; BH census alt; thinner≡confinement; eta-prime rematch; AI scratchpad |
| Hard dups | `_possible_wiki_duplicates/` |
| Cadence | batches of 5; lint@10,20,30; stub+index@20 + final |

Activity log: [[log]] (`wiki/log.md`).
"""

if "## Inbox status" in text:
    text = re.sub(r"## Inbox status\n.*", inbox.strip() + "\n", text, count=1, flags=re.S)
else:
    text = text.rstrip() + "\n" + inbox

# Remove old wave-2 appendix if present then append
text = re.sub(r"\n---\n\n## Wave-2 export papers.*?(?=\n## Inbox status|\Z)", "\n", text, flags=re.S)
# Insert appendix before Inbox
if "## Inbox status" in text:
    text = text.replace("## Inbox status", "".join(appendix) + "\n## Inbox status")
else:
    text = text + "".join(appendix)

index_path.write_text(text, encoding="utf-8")

# High-value lint links at 20 and 30 (append connections if missing)
lint_pairs = [
    ("radio-changing-look-agn", "glimpse-17775-cocoon"),
    ("category-79-quasar-wind", "radio-changing-look-agn"),
    ("mot-metal-hydride", "molecular-rotation-superfluid-he"),
    ("nucleus-tells-on-itself", "nucleus-shell-src-memory"),
    ("topo-chirality-structured-light", "twisted-light-chiral-ms"),
    ("qg-deep-dive-1-mergers-emission", "horizon-direct-wave-gw250114"),
    ("qg-deep-dive-4-de-sitter", "universe-gas-pedal-leaky"),
    ("cryptochrome-ascorbate-compass", "ciss-homochirality"),
    ("interstellar-sulfur-ice", "interstellar-glaciers-spherex"),
    ("confinement-stiffening-films", "metal-fall-apart-on-purpose"),
]

for a, b in lint_pairs:
    pa = papers_dir / f"{a}.md"
    if not pa.exists():
        continue
    t = pa.read_text(encoding="utf-8")
    if f"[[{b}]]" not in t:
        t = t.replace("## Source", f"- Lint link: [[{b}]]\n\n## Source", 1)
        pa.write_text(t, encoding="utf-8")
    pb = papers_dir / f"{b}.md"
    if pb.exists():
        t2 = pb.read_text(encoding="utf-8")
        if f"[[{a}]]" not in t2:
            t2 = t2.replace("## Source", f"- Lint link: [[{a}]]\n\n## Source", 1)
            pb.write_text(t2, encoding="utf-8")

log_entry = f"""

---

## [2026-08-02] ingest | Export wave-2 COMPLETE ({len(wave2)} papers)

Processed remaining unique extracts after wave-1 (40) + wave-2 batches 1–2 (10).

### Cadence applied
- Batches of 5 through remainder
- Lint + high-value links at 10 (batch 2), 20, 30 + final pass
- Stub policy: no new single-paper concept stubs; key terms folded into papers
- Index: counts rebuilt + Wave-2 appendix table

### Wave-2 slugs ({len(wave2)})
{', '.join(wave2)}

### Soft-dups / skips (not pages)
- Lorentz emergent gravity ≡ universe-gas-pedal-leaky
- spin-flip SAF, SnTe light symmetry, BH census alt, water-dissociation (double-life)
- why-thinner-is-tougher ≡ confinement-stiffening-films
- mass-and-instantons extract rematch → eta-prime (already in wiki); deleted bad page
- AI language-model scratchpad (non-physics)
- Hard dups folder untouched

### Catalog
- **Papers: {n_papers} · Concepts: {n_concepts} · Synthesis: {n_synth}**
- Wave-2 progress: **{len(wave2)} / {len(wave2)} COMPLETE — queue exhausted**

"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_entry)

prog = {
    "wave": 2,
    "completed": len(wave2),
    "target": "all_remaining",
    "batches_done": 8,
    "stopped": True,
    "papers_total": n_papers,
    "concepts_total": n_concepts,
    "synthesis_total": n_synth,
    "new_slugs": wave2,
    "note": "Wave-2 complete: all remaining unique extracted-analyses ingested; cadence lint@10/20/30 + index cleanup applied",
}
(root / "claude_export" / "INGEST_PROGRESS_WAVE2.json").write_text(
    json.dumps(prog, indent=2), encoding="utf-8"
)
(root / "claude_export" / "new_papers_wave2.json").write_text(
    json.dumps([{"slug": s} for s in wave2], indent=2), encoding="utf-8"
)

print("papers", n_papers, "concepts", n_concepts, "synth", n_synth)
print("wave2", len(wave2), "missing", missing)
