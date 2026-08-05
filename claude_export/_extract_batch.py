"""Extract body heads for a named batch of sources."""
import re, sys, json
from pathlib import Path

root = Path(__file__).resolve().parent
src = root / "extracted-analyses"
out = root / "_batch_extracts"
out.mkdir(exist_ok=True)

# slug -> filename
BATCHES = {
    "b3": {
        "radio-changing-look-agn": "2026-07-05_the-black-hole-that-flipped-its-radio-switch-and-left-it-on_9b801f92.md",
        "glimpse-17775-cocoon": "2026-06-10_glimpse-17775-inside-the-cocoon_73204815.md",
        "mot-metal-hydride": "2026-06-26_magneto-optical-trapping-of-metal-hydride-molecules_a175fb0e.md",
        "molecular-rotation-superfluid-he": "2026-07-04_molecular-rotation-control-in-superfluid-helium_bb64afb7.md",
        "droplet-rewrites-ring": "2026-06-26_the-droplet-that-rewrites-the-ring_69f8581e.md",
    },
    "b4": {
        "nucleus-tells-on-itself": "2026-07-26_the-nucleus-tells-on-itself_edc2587e.md",
        "confinement-stiffening-films": "2026-06-16_confinement-stiffening-in-nanoscale-ballistic-films_6b9b99ac.md",
        "metal-fall-apart-on-purpose": "2026-07-09_letting-a-metal-fall-apart-on-purpose_6609c393.md",
        "topo-chirality-structured-light": "2026-04-30_topological-control-of-chirality-and-spin-with-structured-li_c172b505.md",
        "color-space-geometry": "2026-06-09_color-space-has-potholes_0a5c3ef4.md",
    },
    "b5": {
        "qg-deep-dive-1-mergers-emission": "2026-06-25_quantum-gravity-deep-dive-1-from-black-hole-mergers-to-spont_0b25cbf8.md",
        "qg-deep-dive-2-info-holography": "2026-06-27_quantum-gravity-deep-dive-2-outside-project-from-information_5c0fdae0.md",
        "qg-deep-dive-3-holographic-codes": "2026-06-28_quantum-gravity-deep-dive-3-holographic-codes-and-bulk-recon_447ad3f1.md",
        "qg-deep-dive-4-de-sitter": "2026-06-29_quantum-gravity-deep-dive-4-de-sitter-holography-and-quantum_cea522d1.md",
        "mass-instantons-zero-modes": "2026-04-08_mass-and-instatons-zero-modes_7b9a60cf.md",
    },
    "b6": {
        "cryptochrome-ascorbate-compass": "2026-07-26_todd-intended-the-spin-quiet-partner-that-almost-never-shows_de8ad8dd.md",
        "ultrafast-chemical-shifts": "2026-03-12_ultrafast-chemical-shifts-analysis_653e2cb3.md",
        "two-lasers-one-reaction": "2026-07-03_two-lasers-one-reaction_942df2d8.md",
        "gpu-mass-spectrometry": "2026-06-06_the-gpu-moment-for-mass-spectrometry_d44aa7e3.md",
        "bond-breaking-discount": "2026-07-09_the-bond-breaking-discount_30ce2966.md",
    },
    "b7": {
        "millisecond-pharma-factory": "2026-06-03_millisecond-pharma-factory-drug-scaffold-rings-built-in-mida_20cc3e4b.md",
        "ruthenium-atom-catalysis": "2026-07-04_a-single-ruthenium-atom-that-both-lights-the-match-and-bends_9beb4c8d.md",
        "water-rna-polymerase": "2026-05-01_water-molecules-in-rna-polymerase-ii-catalysis_90d5cce7.md",
        "molecular-bias-point": "2026-07-22_finding-the-bias-point-where-a-molecule-stops-listening_1bb5fc5d.md",
        "interstellar-sulfur-ice": "2026-06-17_paper-analysis-on-sulfur-chemistry-in-interstellar-ice_d08f1727.md",
    },
    "b8": {
        "one-bond-inductive-effect": "2026-07-12_one-bond-and-done_b51aa206.md",
        "enzyme-resistance-tax": "2026-07-26_todd-actual-the-resistance-tax-how-breaking-the-one-enzyme-t_93719d40.md",
    },
}

which = sys.argv[1] if len(sys.argv) > 1 else "b3"
files = BATCHES[which]
for slug, fn in files.items():
    t = (src / fn).read_text(encoding="utf-8", errors="replace")
    body = re.sub(r"^---.*?---\s*", "", t, count=1, flags=re.S)
    # Prefer punchy sections
    (out / f"{slug}.txt").write_text(body[:12000], encoding="utf-8")
    print(which, slug, "ok", len(body))
print("DONE", which, len(files))
