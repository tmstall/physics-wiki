---
tags: [papers, materials, soft-matter, electron-microscopy]
last_updated: 2026-08-01
status: analysis-ingest
related_papers: []
source_analysis: "raw/analyses/List2_Combined_Clean.md (The Electron Microscope Finally Gets a Full Map)"
---

# 3D Electron Diffraction Completes TEM Mapping of Organic Solar Cells

**One-line summary:** Elastically filtered 3D electron diffraction in a TEM recovers GIWAXS-class crystal statistics (spacings, grain size, texture) from organic solar-cell films *and* the same-session real-space morphology—revealing “leaf” domains as internal mosaics with charge-trapping grain boundaries.

## Key claims and results

- **Paper:** Irene Kraus et al., *3D electron diffraction—the missing slice completing nanoscale analysis of organic solar cells in TEM*, *Nature Communications* (2026). DOI: 10.1038/s41467-026-70690-y; arXiv:2502.11254.
- FAU Erlangen-Nürnberg + Jülich + DESY: all-electron workflow closes the gap between ensemble X-ray structure and local TEM imaging.
- 3D ED (tilt series of diffraction patterns + elastic filtering) matches lab/synchrotron GIWAXS on lattice parameters, crystallite size, and orientation statistics.
- Same TEM session: imaging + local chemistry + spatially resolved orientation maps on identical sample area.
- Physics payoff: visually distinct leaf-shaped domains in model OSC film are **mosaic**—multiple misaligned sub-crystallites; internal boundaries act as carrier traps.
- “Missing slice” = reciprocal-space coverage gap closed relative to pure 2D ED (complementary missing wedge to GIWAXS remains).

## Physical intuition

GIWAXS is a stadium aerial photo of tile statistics; TEM imaging is a close-up of the pattern. Until now those lived in different buildings (synchrotron vs lab). 3D ED puts both tools on one microscope: tilt the sample like a CT scan in reciprocal space, filter out inelastic fog, and read crystal quality *where* the leaves are. The leaves turn out to be patchwork quilts, not single crystals—and the seams leak charge.

## Limitations and assumptions

- Beam damage on organics remains critical; safe dose protocols not universal across NFA systems (Y6-class not demonstrated here).
- Energy filter required—not every TEM lab has one.
- Local sampling vs mm² GIWAXS powder average; stitching statistics still weaker for highly heterogeneous films.
- Validation system P3HT:PC₇₁BM is a mature model, not a >20% NFA champion stack.
- Complementary missing wedges: full coverage still wants X-ray + ED overlay.

## Connections

- Soft-matter / materials island (new cluster entry).
- Key terms (stubs folded here): **3D electron diffraction** = tilt-series ED that fills reciprocal space for crystal stats; **organic solar cells** hinge on nanoscale domain packing (exciton split vs charge collection trade-off).
- Ultrafast nanophotonics neighbor (solution-processable nanocrystal optics, different probe): [[ito-nanocrystal-fieldoscopy]].
- Antimatter matter-wave diffraction: [[positronium-diffraction-graphene]]

## Source

- Analysis: `raw/analyses/List2_Combined_Clean.md` — *The Electron Microscope Finally Gets a Full Map.md*
