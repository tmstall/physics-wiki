---
tags: [papers, astrophysics, dark-matter, galaxies, stellar-streams]
last_updated: 2026-08-14
status: analysis-ingest
related_papers: [not-a-globular-cluster, pulsars-satellite-masses, cosmos-web-cosmic-web, loki-early-accreted-vmp]
source_analysis: "raw/analyses/2026-08-13_doi-10.1038-s41586-026-10878-w_globular-cluster-stellar-stream.md"
---

# Oyashio: First Globular-Cluster Stellar Stream Beyond the Milky Way

**One-line summary:** Holm et al. (*Nature* 2026) detect a ~2 kpc, ~72 pc-wide tidal stream (Oyashio) from a globular cluster in ultra-diffuse galaxy UGC 9050-Dw1 (~35 Mly) and fit a generative stream model for host halo mass and inner slope — first confirmed extragalactic GC stream and first stream-based DM probe outside the MW.

## Key claims and results

- **Paper:** Holm, Pearson, Nibauer et al., *Nature*, DOI 10.1038/s41586-026-10878-w; arXiv:2608.12254.
- Host: ultra-diffuse galaxy UGC 9050-Dw1; stream independently recovered in HST ACS/WFC and CFHT MegaCam.
- Photometric feature: ~2 kpc long, width $72.3\pm8.9$ pc, ~2.5 kpc offset from galaxy center; detection significance **7.34σ** for the light excess (not for DM parameters).
- Color match stream ↔ compact clump at stream end → candidate surviving progenitor (old, metal-poor GC-like).
- Alternatives argued against: tidal shell, lensing, dust, stripped dwarf (too broad/massive in mocks); chance alignment not fully excluded.
- Generative Bayesian stream fit (“X-Stream” lineage): progenitor mass upper limit ~$2.5\times10^6\,M_\odot$ (95%; below Ω Cen scale); host $\log_{10}(M_{200}/M_\odot)$ roughly LMC-class (~11.3–11.6 range in analysis — **verify exact table values**); inner slope $\gamma\approx0.92\pm0.57$ (cuspier than many UDG cores).
- Analysis flags internal mass-numeral inconsistency in secondary extraction — treat digits as approximate pending primary tables.

## Physical intuition

Milky Way streams are system traces of the halo potential. Until now, GC streams were a local trick (resolved stars). Oyashio is the same idea as an unresolved light smear 35 Mly away: the trail’s thin shape still encodes the dark well. One stream, one orbit — sharp along a path, not a full 3D halo map.

## Limitations and assumptions

- GC identity inferred (mass + color + width), not spectroscopic velocities/chemistry.
- Single stream / single galaxy / single modeling family.
- Halo mass and $\gamma$ are model-conditional posteriors, much weaker significance than 7.34σ photometry.
- Analysis notes retrieval/numeral caveats — check arXiv tables for precise $M_{200}$.

## Connections

- Synthesis: [[dark-matter-detection-channels]]

- GC / cluster classification neighbors: [[not-a-globular-cluster]]
- Satellite / dynamical mass context: [[pulsars-satellite-masses]]
- Large-scale structure / environment: [[cosmos-web-cosmic-web]], [[cosmic-web]]
- Galactic archaeology cousins: [[loki-early-accreted-vmp]]
- Concepts: [[cosmic-web]]

## Source

- `raw/analyses/2026-08-13_doi-10.1038-s41586-026-10878-w_globular-cluster-stellar-stream.md`
