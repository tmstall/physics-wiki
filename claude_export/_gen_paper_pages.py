"""Generate compact wiki paper pages from batch extract snippets + metadata."""
from pathlib import Path
import re
import json

root = Path(__file__).resolve().parent.parent
ext = root / "claude_export" / "_batch_extracts"
papers = root / "wiki" / "papers"

# slug, source file, tags, related, one-line if auto fails
META = [
    # batch 3
    ("radio-changing-look-agn", "2026-07-05_the-black-hole-that-flipped-its-radio-switch-and-left-it-on_9b801f92.md",
     ["papers", "agn", "black-holes", "radio"],
     ["jwst-filament-cnd-ngc4696", "category-79-quasar-wind", "mrk501-double-jet-smbbh", "bh-recoils-agn-survey"],
     "A nearby galaxy's central black hole boosted radio output >23× between 2000–2017 and held that level for years with almost no multiwavelength fingerprint — first long-duration radio changing-look AGN."),
    ("glimpse-17775-cocoon", "2026-06-10_glimpse-17775-inside-the-cocoon_73204815.md",
     ["papers", "star-formation", "infrared-astronomy"],
     ["dr21-magnetic-accretion", "interstellar-glaciers-spherex"],
     "Infrared study of GLIMPSE-17775 resolves structure inside a star-forming cocoon / massive YSO environment."),
    ("mot-metal-hydride", "2026-06-26_magneto-optical-trapping-of-metal-hydride-molecules_a175fb0e.md",
     ["papers", "cold-molecules", "atomic-physics"],
     ["molecular-rotation-superfluid-he", "problem-of-time-cold-atoms"],
     "Magneto-optical trapping of metal hydride molecules extends cold-molecule control beyond alkalis."),
    ("molecular-rotation-superfluid-he", "2026-07-04_molecular-rotation-control-in-superfluid-helium_bb64afb7.md",
     ["papers", "cold-molecules", "superfluid-helium"],
     ["mot-metal-hydride", "fractional-fermi-sea-1d-bosons"],
     "Controlled molecular rotation inside superfluid helium nanodroplets / matrix — coherent rotor dynamics in a quantum solvent."),
    ("droplet-rewrites-ring", "2026-06-26_the-droplet-that-rewrites-the-ring_69f8581e.md",
     ["papers", "quantum-optics", "nonlinear-optics"],
     ["photonic-supersolid", "quantum-state-sculptor", "freeze-fiber-brillouin"],
     "A nonlinear optical droplet / cavity state rewrites ring-mode structure — non-Hermitian or dissipative pattern formation in light."),
    # batch 4
    ("nucleus-tells-on-itself", "2026-07-26_the-nucleus-tells-on-itself_edc2587e.md",
     ["papers", "nuclear-physics", "nuclear-structure"],
     ["nucleus-shell-src-memory", "thorium-229-nuclear-clock"],
     "Nuclear self-spectroscopy / internal probes that let the nucleus report its own structure without external projectiles alone."),
    ("confinement-stiffening-films", "2026-06-16_confinement-stiffening-in-nanoscale-ballistic-films_6b9b99ac.md",
     ["papers", "soft-matter", "nanomechanics"],
     ["light-as-friction-brake", "3d-electron-diffraction-osc"],
     "Nanoscale ballistic films (graphene, GO, polymers) get tougher as they thin — nonaffine elasticity under confinement explains the rise."),
    ("metal-fall-apart-on-purpose", "2026-07-09_letting-a-metal-fall-apart-on-purpose_6609c393.md",
     ["papers", "materials", "metallurgy"],
     ["quantum-metallurgy-cdw", "confinement-stiffening-films"],
     "Deliberate controlled disintegration / dealloying / phase separation of a metal engineered as a feature for function."),
    ("topo-chirality-structured-light", "2026-04-30_topological-control-of-chirality-and-spin-with-structured-li_c172b505.md",
     ["papers", "structured-light", "chirality", "spin"],
     ["twisted-light-chiral-ms", "ciss-homochirality", "snte-light-topological-inversion"],
     "Structured light topologically steers chirality and spin degrees of freedom in matter."),
    ("color-space-geometry", "2026-06-09_color-space-has-potholes_0a5c3ef4.md",
     ["papers", "perception", "geometry", "foundations"],
     ["weak-values"],
     "Los Alamos team repairs Schrödinger's color geometry: non-Riemannian geodesics fix hue/lightness and rigorously define the gray axis."),
    # batch 5 QG series + instantons
    ("qg-deep-dive-1-mergers-emission", "2026-06-25_quantum-gravity-deep-dive-1-from-black-hole-mergers-to-spont_0b25cbf8.md",
     ["papers", "quantum-gravity", "black-holes", "synthesis-ingest"],
     ["horizon-direct-wave-gw250114", "entropy-maximization-bh-mergers", "black-hole-third-law-violation", "qg-deep-dive-2-info-holography"],
     "Multi-paper quantum-gravity deep dive part 1: from black-hole mergers / ringdown to spontaneous emission analogies in curved spacetime."),
    ("qg-deep-dive-2-info-holography", "2026-06-27_quantum-gravity-deep-dive-2-outside-project-from-information_5c0fdae0.md",
     ["papers", "quantum-gravity", "information-paradox", "holography"],
     ["qg-deep-dive-1-mergers-emission", "qg-deep-dive-3-holographic-codes", "black-hole-evaporation-energy-conditions"],
     "Deep dive part 2: information paradox → holographic encoding; outside-project framing of bulk reconstruction ingredients."),
    ("qg-deep-dive-3-holographic-codes", "2026-06-28_quantum-gravity-deep-dive-3-holographic-codes-and-bulk-recon_447ad3f1.md",
     ["papers", "quantum-gravity", "quantum-error-correction", "holography"],
     ["qg-deep-dive-2-info-holography", "qg-deep-dive-4-de-sitter", "shor-algorithm-budget"],
     "Deep dive part 3: holographic quantum error-correcting codes and bulk reconstruction."),
    ("qg-deep-dive-4-de-sitter", "2026-06-29_quantum-gravity-deep-dive-4-de-sitter-holography-and-quantum_cea522d1.md",
     ["papers", "quantum-gravity", "de-sitter", "cosmology"],
     ["qg-deep-dive-3-holographic-codes", "topological-cosmological-constant", "universe-gas-pedal-leaky"],
     "Deep dive part 4: de Sitter holography and quantum gravity in accelerating cosmologies."),
    ("mass-instantons-zero-modes", "2026-04-08_mass-and-instatons-zero-modes_7b9a60cf.md",
     ["papers", "qft", "instantons", "topology"],
     ["eta-prime-mesic-nucleus", "color-superconductivity-qcd", "qg-deep-dive-2-info-holography"],
     "Mass generation, instantons, and fermion zero modes — topology of the QCD / QFT vacuum."),
    # batch 6
    ("cryptochrome-ascorbate-compass", "2026-07-26_todd-intended-the-spin-quiet-partner-that-almost-never-shows_de8ad8dd.md",
     ["papers", "quantum-biology", "spin-chemistry"],
     ["ciss-homochirality"],
     "Radical-pair avian compass: ascorbate radical is magnetically quiet but almost never available at physiological concentration — negative result that strengthens flavin–tryptophan cryptochrome."),
    ("ultrafast-chemical-shifts", "2026-03-12_ultrafast-chemical-shifts-analysis_653e2cb3.md",
     ["papers", "ultrafast", "spectroscopy", "chemistry"],
     ["hot-electron-coherent-phonons-ptcu", "attosecond-stm-lightwave"],
     "Ultrafast chemical-shift / spectroscopic tracking of nuclear environments on femtosecond–picosecond scales."),
    ("two-lasers-one-reaction", "2026-07-03_two-lasers-one-reaction_942df2d8.md",
     ["papers", "photochemistry", "ultrafast"],
     ["ultrafast-chemical-shifts", "two-clocks-one-laser"],
     "Two-laser control of a single reaction pathway — coherent or sequential photonic control of chemistry."),
    ("gpu-mass-spectrometry", "2026-06-06_the-gpu-moment-for-mass-spectrometry_d44aa7e3.md",
     ["papers", "mass-spectrometry", "instrumentation", "islands"],
     ["twisted-light-chiral-ms"],
     "GPU-scale acceleration of mass-spectrometry analysis / acquisition pipelines — computational inflection for MS."),
    ("bond-breaking-discount", "2026-07-09_the-bond-breaking-discount_30ce2966.md",
     ["papers", "chemistry", "catalysis", "islands"],
     ["ruthenium-atom-catalysis", "one-bond-inductive-effect"],
     "Energetic 'discount' on bond breaking under catalytic / electrochemical / photochemical conditions."),
    # batch 7
    ("millisecond-pharma-factory", "2026-06-03_millisecond-pharma-factory-drug-scaffold-rings-built-in-mida_20cc3e4b.md",
     ["papers", "chemistry", "synthesis", "islands"],
     ["boronate-velcro-synthetic-cells", "magnesium-benzidine-rearrangement"],
     "Millisecond gas-phase / midair construction of drug-scaffold rings without traditional catalysts."),
    ("ruthenium-atom-catalysis", "2026-07-04_a-single-ruthenium-atom-that-both-lights-the-match-and-bends_9beb4c8d.md",
     ["papers", "catalysis", "single-atom", "islands"],
     ["bond-breaking-discount", "hot-electron-coherent-phonons-ptcu"],
     "Single ruthenium atom both initiates and steers a catalytic bond transformation."),
    ("water-rna-polymerase", "2026-05-01_water-molecules-in-rna-polymerase-ii-catalysis_90d5cce7.md",
     ["papers", "biophysics", "enzymology", "islands"],
     ["water-double-life-nanoconfinement"],
     "Structural/functional role of water molecules in RNA polymerase II catalysis."),
    ("molecular-bias-point", "2026-07-22_finding-the-bias-point-where-a-molecule-stops-listening_1bb5fc5d.md",
     ["papers", "molecular-electronics", "islands"],
     ["ito-nanocrystal-fieldoscopy", "ciss-homochirality"],
     "Bias / operating point where a molecule stops responding to external fields — molecular electronics threshold."),
    ("interstellar-sulfur-ice", "2026-06-17_paper-analysis-on-sulfur-chemistry-in-interstellar-ice_d08f1727.md",
     ["papers", "astrochemistry", "islands"],
     ["interstellar-glaciers-spherex", "dr21-magnetic-accretion"],
     "Sulfur chemistry pathways in interstellar ice mantles."),
    # batch 8 (remainder)
    ("one-bond-inductive-effect", "2026-07-12_one-bond-and-done_b51aa206.md",
     ["papers", "chemistry", "electronic-structure", "islands"],
     ["bond-breaking-discount"],
     "DFT challenge to textbook inductive effect: in neutral molecules electronegative groups affect mainly the bonded carbon; hyperconjugation dominates beyond."),
    ("enzyme-resistance-tax", "2026-07-26_todd-actual-the-resistance-tax-how-breaking-the-one-enzyme-t_93719d40.md",
     ["papers", "biochemistry", "evolution", "islands"],
     ["water-rna-polymerase", "cryptochrome-ascorbate-compass"],
     "Evolutionary/enzymatic 'resistance tax' — cost of breaking the one enzyme pathway that dodges a pressure."),
]


def extract_claims(text: str, max_bullets=5):
    bullets = []
    # takeaway numbered lines
    for m in re.finditer(r"(?m)^\*?\*?(\d+)\.?\*?\*?\s+\*\*([^*]+)\*\*[—:\-–]?\s*(.+)$", text):
        bullets.append(m.group(2).strip() + " — " + m.group(3).strip()[:200])
        if len(bullets) >= max_bullets:
            break
    if len(bullets) < 3:
        for m in re.finditer(r"(?m)^[-*]\s+\*\*([^*]+)\*\*[:\s]+(.+)$", text):
            bullets.append(m.group(1).strip() + ": " + m.group(2).strip()[:180])
            if len(bullets) >= max_bullets:
                break
    # fallback: sentences from hook section
    if len(bullets) < 2:
        m = re.search(r"(?is)one-sentence hook.{0,80}?\n+(.{100,600})", text)
        if m:
            s = re.sub(r"\s+", " ", m.group(1)).strip()
            bullets.append(s[:300])
    return bullets[:max_bullets]


def extract_title(text: str, fallback: str):
    m = re.search(r"(?m)^#+\s+\*?\*?(.+?)\*?\*?\s*$", text)
    if m:
        t = re.sub(r"[#*_]", "", m.group(1)).strip()
        if 8 < len(t) < 120 and "Human" not in t and "Assistant" not in t:
            return t
    for m in re.finditer(r"(?m)^#+\s+(.+)$", text):
        t = re.sub(r"[#*_\"']", "", m.group(1)).strip()
        if 10 < len(t) < 120 and not t.startswith("Analysis") and "Human" not in t:
            return t
    return fallback


def extract_intuition(text: str):
    for pat in [
        r"(?is)##\s*2\.\s*Big-Picture Context\s*\n+(.{200,900})",
        r"(?is)##\s*Section 2[^\n]*\n+(.{200,900})",
        r"(?is)Physical intuition[^\n]*\n+(.{200,700})",
        r"(?is)##\s*3\.\s*Necessary Background.{0,200}?\n+(.{200,700})",
    ]:
        m = re.search(pat, text)
        if m:
            s = re.sub(r"\s+", " ", m.group(1))
            s = re.sub(r"!\[.*?\]\(.*?\)", "", s)
            return s[:700].strip()
    # first long paragraph
    paras = re.split(r"\n\s*\n", text)
    for p in paras:
        p = re.sub(r"\s+", " ", p).strip()
        if len(p) > 250 and "Human" not in p[:40] and "Assistant" not in p[:40]:
            return p[:700]
    return "See source analysis for full physical picture."


def extract_limits(text: str):
    m = re.search(r"(?is)##\s*\d*\.?\s*Limitations[^\n]*\n+(.{100,800})", text)
    if m:
        s = re.sub(r"\s+", " ", m.group(1))
        # split into bullets roughly
        parts = re.split(r"\*\*[^*]{3,80}\*\*", s)
        return [p.strip()[:200] for p in parts if len(p.strip()) > 40][:4]
    return [
        "Analysis-based ingest: verify claims against the primary paper.",
        "Export analysis may be secondary / incomplete; numerical claims provisional.",
    ]


def make_page(slug, src_file, tags, related, summary_fallback):
    extract_path = ext / f"{slug}.txt"
    if extract_path.exists():
        text = extract_path.read_text(encoding="utf-8", errors="replace")
    else:
        # try raw
        raw = root / "claude_export" / "extracted-analyses" / src_file
        text = raw.read_text(encoding="utf-8", errors="replace")[:12000] if raw.exists() else ""

    title = extract_title(text, slug.replace("-", " ").title())
    claims = extract_claims(text)
    if not claims:
        claims = [summary_fallback]
    intuition = extract_intuition(text)
    limits = extract_limits(text)
    related_links = ", ".join(f"[[{r}]]" for r in related)

    # clean title quotes
    title = title.strip('"').strip()

    body = f"""---
tags: [{', '.join(tags)}]
last_updated: 2026-08-02
status: analysis-ingest
related_papers: [{', '.join(related)}]
source_analysis: "claude_export/extracted-analyses/{src_file}"
---

# {title}

**One-line summary:** {summary_fallback}

## Key claims and results

"""
    for c in claims:
        body += f"- {c}\n"
    body += f"""
## Physical intuition

{intuition}

## Limitations and assumptions

"""
    for L in limits:
        body += f"- {L}\n"
    body += f"""- Analysis-based ingest from Claude export; confirm against primary literature.

## Connections

- Related: {related_links}

## Source

- `claude_export/extracted-analyses/{src_file}`
"""
    outp = papers / f"{slug}.md"
    outp.write_text(body, encoding="utf-8")
    return outp


def main():
    written = []
    for item in META:
        p = make_page(*item)
        written.append(item[0])
        print("wrote", item[0])
    (root / "claude_export" / "new_papers_wave2_remainder.json").write_text(
        json.dumps(written, indent=2), encoding="utf-8"
    )
    print("TOTAL", len(written))


if __name__ == "__main__":
    main()
