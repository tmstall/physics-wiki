---
tags: [papers, cosmology, galaxies, large-scale-structure, tidal-torque]
last_updated: 2026-08-14
status: analysis-ingest
related_papers: [cosmos-web-cosmic-web, mond-external-field-sparc, newton-ksz-force-law, gigaparsec-anisotropic-structures]
source_analysis: "raw/analyses/2026-08-14_doi-10.1038-s41550-026-02948-w_primordial-tidal-torque-galaxy-spin.md"
---

# Primordial Tidal Torque Imprints on Galaxy Spins (~7σ)

**One-line summary:** Sheng et al. (*Nature Astronomy* 2026) compare MaNGA observed spins to ELUCID-reconstructed primordial tidal predictions and find a high-significance alignment for **gas in central ellipticals** ($\mu\approx0.116$ at $r_{\rm opt}\approx3.4\,h^{-1}{\rm Mpc}$, ~7σ vs shuffle null), with $r_{\rm opt}$ scaling with halo mass as tidal-torque theory expects.

## Key claims and results

- **Paper:** Sheng, Yu, Bao et al., *Nature Astronomy*, DOI 10.1038/s41550-026-02948-w; arXiv:2512.11383.
- Theory tested: tidal-torque theory (TTT) — protohalo spin from misalignment of inertia and primordial tidal tensors.
- Observed spin $j_G$: MaNGA IFU gas (Hα) and stellar maps; centrals only; quality cuts → hundreds of ellipticals/spirals with usable gas spins.
- Predicted spin $j_R$: TTT applied to ELUCID reconstructed initial density field, tidal tensor smoothed at scale $r$.
- Correlation $\mu=\langle\cos\theta_{GR}\rangle$; gas in central ellipticals peaks at $\mu=0.116$, $r_{\rm opt}=3.4\,h^{-1}{\rm Mpc}$; mass-bin RMS significance ~**7σ** vs 40k spin-shuffle nulls.
- Spirals and stellar spins generally weaker; signal concentrates where recently accreted gas tracks large-scale environment.
- Internal check: for $M\gtrsim10^{12.5}\,M_\odot$, $r_{\rm opt}$ rises with mass ≈ $0.8\,r_q$ (Lagrangian radius) as TTT predicts; lower masses in “decorrelation” (reconstruction limits).

## Physical intuition

Galaxy spin should remember the birth tidal field if you can rewind today’s map (ELUCID) and measure real rotation axes (MaNGA). The correlation is **modest per galaxy** but highly significant as a population excess over random. Gas in ellipticals wins not because it’s the oldest fossil — often the opposite: recently accreted gas still couples to the environment whose geometry still partially traces the primordial field.

## Limitations and assumptions

- Same research program lineage as Motloch et al. 2021 — refinement, not fully independent discovery.
- Reconstruction degrades at low halo mass; ELUCID is inference, not a direct early-universe image.
- 7σ depends on aggregation choice (RMS over mass bins).
- Analysis mixes Nature abstract/ED captions with arXiv structured extraction.

## Connections

- Synthesis: [[cosmology-expansion-history-and-structure]]

- Cosmic web / LSS: [[cosmos-web-cosmic-web]], [[cosmic-web]], [[gigaparsec-anisotropic-structures]]
- Large-scale gravity tests: [[newton-ksz-force-law]], [[mond-external-field-sparc]]
- Concepts: [[cosmic-web]], [[cosmological-principle]]

## Source

- `raw/analyses/2026-08-14_doi-10.1038-s41550-026-02948-w_primordial-tidal-torque-galaxy-spin.md`
