---
tags: [papers, nuclear-physics, heavy-ion, qcd-critical-point, rhic]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [color-superconductivity-qcd, star-jpsi-spin-interference, high-pt-physics-cern-isr, na61-isospin-kaon-asymmetry, emc-effect-marathon-a3]
source_analysis: "spacex_export/extracted-analyses/2025-10-01_precision-net-proton-fluctuations-at-rhic_284130d8.md"
cleanup_note: "2026-08-04: abstract claims verified against arXiv:2504.00817; extract chat noise discarded"
---

# Precision Net-Proton Fluctuations at RHIC (STAR BES-II)

**One-line summary:** STAR BES-II reports high-precision net-proton cumulants and proton factorial cumulants in Au+Au; central $C_4/C_2$ stays below the Poisson baseline at all energies and shows a **minimum in significance of deviation** (~2–5σ) from non-critical baselines near $\sqrt{s_{NN}}=19.6$ GeV (arXiv:2504.00817).

## Key claims and results

- **Paper:** STAR Collaboration, “Precision Measurement of (Net-)proton Number Fluctuations in Au+Au Collisions at RHIC,” arXiv:2504.00817 [nucl-ex] (2025).
- Program: RHIC Beam Energy Scan **phase II** (collider mode); $\sqrt{s_{NN}}=7.7$, 9.2, 11.5, 14.6, 17.3, 19.6, 27 GeV (9.2 and 17.3 new vs BES-I).
- Observables: cumulants $C_n$ and factorial cumulants $\kappa_n$ up to fourth order for (net-)protons.
- Acceptance (same as BES-I analysis window): midrapidity $|y|<0.5$, $0.4<p_T<2.0$ GeV/$c$; high purity (~99%) via TPC (+TOF at higher $p_T$).
- Statistics: ~7–18× BES-I event counts; iTPC upgrade improves centrality resolution (RefMult3X) and shrinks uncertainties (factor ~4.7 statistical / ~3.2 systematic on central $C_4/C_2$ vs BES-I, per paper).
- **Central result:** relative to non-critical models (UrQMD, HRG with canonical baryon charge, hydro + excluded volume) **and** peripheral 70–80% data, net-proton $C_4/C_2$ in 0–5% collisions shows a **minimum around 19.6 GeV** with significance of deviation ~**2–5σ** (5σ when peripheral data is the reference; ~2σ vs hydro EV).
- Related deviations near the same energy in proton factorial ratios, especially $\kappa_2/\kappa_1$ and $\kappa_3/\kappa_1$.
- **Important nuance vs BES-I narrative:** BES-II precision data **do not support** a non-monotonic $C_4/C_2$ trend *with respect to the Poisson baseline*; values remain **below** Poisson (unity) at all BES-II energies. The interesting structure is the deviation **from non-critical / peripheral baselines**, not a Poisson peak.
- Call for dynamical models **with** a critical point to interpret the suite of ratios.

## Physical intuition

Near a QCD critical point, baryon-number fluctuations should swing non-monotonically as the scan walks $\mu_B$ (roughly 400→150 MeV over 7.7→27 GeV). Net protons are the experimental proxy. BES-II is the high-statistics remake of that scan: the “boring” baselines (hadronic transport, thermal models with exact baryon conservation, peripheral events) no longer sit under the central $C_4/C_2$ near 20 GeV — a ~few-σ notch that critical-point dynamics are invited to explain.

## Limitations and assumptions

- **Source quality:** the SpaceX extract contains the STAR abstract (usable) plus off-topic “context rot” chat noise — **discarded**; quantitative claims on this page follow arXiv:2504.00817.
- 2–5σ is suggestive, not a discovery claim; significance depends on which baseline is chosen.
- Efficiency, volume fluctuations, centrality resolution, and conservation-law effects dominate systematics.
- Acceptance cuts limit direct infinite-volume theory comparison; FXT gap between 3 and 7.7 GeV still open.
- No published critical-point dynamical model yet fully matches the full cumulant suite.

## Connections

- Dense QCD / color SC context: [[color-superconductivity-qcd]]
- RHIC / spin nuclear neighbor: [[star-jpsi-spin-interference]]
- SPS isospin / strangeness neighbor: [[na61-isospin-kaon-asymmetry]]
- EMC medium PDFs: [[emc-effect-marathon-a3]]
- High-energy nuclear history: [[high-pt-physics-cern-isr]]
- Key terms: net-proton cumulants, Beam Energy Scan II, QCD critical point, $\mu_B$, $C_4/C_2$, factorial cumulants
- Synthesis: [[nuclear-dense-matter-precision]] (nuclear & dense-matter precision map)

## Source

- `spacex_export/extracted-analyses/2025-10-01_precision-net-proton-fluctuations-at-rhic_284130d8.md`
- Primary: arXiv:2504.00817
