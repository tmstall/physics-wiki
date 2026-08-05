---
tags: [papers, biophysics, diagnostics, crispr]
last_updated: 2026-08-01
status: analysis-ingest
related_papers: []
source_analysis: "raw/analyses/Kinetic Barcoding Cracks One-Pot.md"
---

# Kinetic Barcoding for Multiplexed Cas13a RNA Detection

**One-line summary:** DNA-tailed crRNAs program Cas13a’s collateral-cleavage speed into kinetic barcodes, so multiple viral RNAs are identified in one pot of microdroplets from fluorescence ramp shape — no sample splitting, extra colors, amplification, or sequencing.

## Key claims and results

- **Paper:** Sungmin Son et al., *Nature Biomedical Engineering* (2026). DOI: 10.1038/s41551-026-01642-6.
- LbuCas13a in ~10 pL droplets: single-target occupancy; measured cleavage ~471 reporters/s; diffusion-limited \(k_\mathrm{cat}/K_M\).
- Natural crRNA-dependent kinetic variability turned into a channel; **igRNAs** (5′ poly-dT DNA tails, 6–12 nt via short RNA linker) act as programmable brakes (MD: tail occludes HEPN active site).
- Multiplex in one mix: respiratory viruses + SARS-CoV-2 variants; kinetic clusters separated by slope/endpoint; SVM classification.
- 15 clinical nasal swabs (high load, Ct < 20): 100% variant ID without sequencing (analysis claim).

## Physical intuition

Cas13a is a security gate that, once unlocked by the right RNA key, shreds every reporter “paper” in the room. Different keys (and DNA governors on those keys) change shredder RPM. Tiny oil-isolated water droplets are single-threaded cores so you measure one shredder’s power signature without cache contention. Multiplexing lives in the **shape of the glow curve**, not in extra dyes or wells.

## Limitations and assumptions

- ~4–6 reliable kinetic bins before distributions overlap.
- Clinical demo at high viral load; low-load / matrix robustness not fully established in the analysis.
- Still needs fluorescence imaging — not yet handheld POC.
- RNA secondary structure / degradation can shift barcodes.

## Connections

- Soft-matter island neighbor (different field): [[boronate-velcro-synthetic-cells]] — both one-pot programmable chemistry, no shared physics.

## Open questions

- 8–10 plex with better ML or orthogonal kinetic axes?
- Smartphone imagers for endpoint classification?
- Port kinetic brakes to Cas12 / other Cas13 orthologs?

## Source

- Analysis: `raw/analyses/Kinetic Barcoding Cracks One-Pot.md` (base64 images stripped).
