---
tags: [papers, fuzzy-dark-matter, lensing, galaxies]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [dark-matter-detection-channels, strong-gravitational-lensing, mond-external-field-sparc]
source_analysis: "raw/analyses/2026-09-25_doi-10.3847-2041-8213-ae9a9e_fdm-wave-simulation-lensing-hs0810.md"
---

# Fuzzy-DM Wave Halos Lensing HS 0810+2554

**One-line summary:** ApJL DOI 10.3847/2041-8213/ae9a9e. Real Schrödinger-Poisson wave halos fit the 8-image radio lens slightly better than the statistical granule shortcut, mostly from overall shape not ripples. Projected ripples nearly Gaussian (CLT). Favored mass already disfavored by Lyman-α/dwarfs; CDM+multipoles also fit ~1.6 mas. Does not decide FDM vs CDM.

## Key claims and results

- Zhou, Li, Amruth, Gao, Lim & Zhu (*ApJL* 1008:L58, 2026; arXiv:2607.20614) evolve 1,000 Schrödinger–Poisson halos and forward-lens HS 0810+2554 (two radio components, eight VLBI images).
- At $m_\psi = 10^{-22}$ eV, median position anomalies are ~12 mas and ~6 mas; some realizations reach < 3 mas. A Gaussian-random-field (GRF) shortcut on NFW and a smooth NFW do worse. At $10^{-23}$ eV the anomalies jump to ~50 mas.
- Projected ripples are ~10% and nearly Gaussian (skewness ~0, kurtosis ~3). A GRF built on the wave halo’s own smooth shape closes most of the gap. The win is the soliton-plus-envelope layout, not non-Gaussian granules.
- Each halo’s score is the best of ~$10^{7}$ orientation × source trials, aligned with pairwise distances and Procrustes so sky position and rotation do not count.

## Physical intuition

Fuzzy dark matter is one coherent wave. In a galaxy it makes a dense core and interference granules a few hundred parsecs across. Lensing sees only the column. About 150 granules along a sightline average order-unity 3D swings down to ~10% ripples, and the central limit theorem makes those ripples look Gaussian. That is why the cheap statistical shortcut mostly works. The real wave halo still fits this quad a bit better because its overall mass shape is not an NFW with noise glued on. Milliarcsecond residuals do not name the missing piece: multipoles, subhalos, and granules can all nudge images.

## Limitations and assumptions

- The favored mass, $10^{-22}$ eV, sits where Lyman-α and dwarf-galaxy bounds disfavor FDM as all of the dark matter.
- No head-to-head with CDM plus angular multipoles (~1.6 mas rms on this system) or with CDM subhalos. The paper does not decide FDM vs CDM.
- Pure dark matter, five merging wave packets in a 40 kpc box, no baryons, one lens, positions only.
- Search freedom may not match the GRF comparison, so part of the gap could be a larger search, not new physics.
- The grid is marginal (~1.5–2.6 cells per de Broglie wavelength) and has no convergence test.

## Connections

- Synthesis: [[dark-matter-detection-channels]]
- Lensing geometry: [[strong-gravitational-lensing]]
- Force-law alternative (contrast only): [[mond-external-field-sparc]]

## Source

- `raw/analyses/2026-09-25_doi-10.3847-2041-8213-ae9a9e_fdm-wave-simulation-lensing-hs0810.md`
