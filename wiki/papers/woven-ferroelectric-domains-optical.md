---
tags: [papers, ferroelectric, topology, domains, optical-control]
last_updated: 2026-09-05
status: analysis-ingest
related_papers: [magnetic-heliknoton-electric-write, snte-light-topological-inversion]
source_analysis: "raw/analyses/2026-09-04_nodoi_woven-ferroelectric-domains-optical.md"
---

# Woven Ferroelectric Domains with Optical Control

**One-line summary:** KTN:Li near $T_C$ forms 3D woven polarization domains that trap charged walls; a 514 nm laser unravels them via photo-carrier screening — optical write / thermal erase toward topological memory (Xin et al.; DelRe / Agranat collaboration).

## Key claims and results

- Material: KTN:Li ($\mathrm{K}_{0.997}\mathrm{Ta}_{0.62}\mathrm{Nb}_{0.38}\mathrm{O}_3$:+Li) with growth-axis compositional striations (~5 μm); $T_C\approx292$ K.
- Slow cool (<0.4 K/min): regular diagonal stripe lattice at $T-T_C\approx-1.95$ K → woven fabric at ≈−2.0 K; persists ~$T_C-2$ to $T_C-8$ K.
- Two superdomain thread families (45° / 135°) interlace in 3D with random over/under crossings (linking numbers); multifocus imaging (0 to −24 μm) shows genuine depth stacking, not a 2D projection artifact.
- Weaving forces charged domain walls (head-to-head / tail-to-tail) at crossings — high-energy features locked by interlacing geometry.
- 514 nm focused laser ($D\approx0.8$ μm, $I\sim6\times10^6$ W cm$^{-2}$) selectively eliminates one thread family (wefts), leaving parallel warps; 1040 nm does not; $E\gtrsim200$ V/mm also disentangles.
- Proposed mechanism: photorefractive screening of CDW bound charge by sub-bandgap photo-carriers; thermal cycle through $T_C$ regenerates a new random weave.
- Multi-probe support: white-light multifocus, PFM, SHG, confocal Raman, dielectric hysteresis / dispersion.

## Physical intuition

Skyrmions and vortices are local tiles — lift one, the neighbors barely notice. Here domains *weave* like cloth: each thread runs through many crossings, so the network is globally connected. Over/under geometry breaks flux closure and pins charged walls that would normally relax away. A green laser injects the carriers the insulator cannot supply in the dark; screening unlocks relaxation — write by light, erase by reheating through the Curie point.

## Limitations and assumptions

- No quantitative model for *why* lattice → weave onsets at ~2 K below $T_C$ or for the 0.4 K/min cooling threshold (Kibble–Zurek invoked qualitatively only).
- Photorefractive disentanglement is a candidate, not a closed proof; thermal / polarizability alternatives not fully excluded.
- Single material, single-group observation; bulk depth beyond ~24 μm inferred, not volumetrically imaged.
- “Topological protection” here is energy-barrier / linking geometry, not a conserved homotopy charge; LK patterns rewrite under laser / thermal erase.
- Memory framing is prospective: binary write/erase shown; no LK readout protocol or bit-error metrics.
- Analysis-based ingest; verify temperatures, intensities, and model claims against the primary paper.

## Connections

- Synthesis (texture / topology map): [[condensed-matter-topology-fractionalization]]
- Optical write of 3D topological texture (magnetic cousin): [[magnetic-heliknoton-electric-write]]
- Light-driven band / order control neighbor: [[snte-light-topological-inversion]]
- Probe / control hardware shelf: [[ultrafast-optics-and-solid-state-emitters]]

## Source

- `raw/analyses/2026-09-04_nodoi_woven-ferroelectric-domains-optical.md`
