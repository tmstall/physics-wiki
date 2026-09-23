---
tags: [papers, black-holes, holography, islands, page-curve, kerr-ads]
last_updated: 2026-09-20
status: analysis-ingest
related_papers: [black-hole-evaporation-energy-conditions, entropic-information-gravity, qg-deep-dive-2-info-holography, hawking-radiation, bh-thermo-far-from-equilibrium]
source_analysis: "raw/analyses/2026-09-13_doi-10.1140-epjc-s10052-026-15820-y_entanglement-islands-page-curves-kerr-ads.md"
---

# Entanglement Islands and Page Curves for Kerr-AdS

**One-line summary:** Island rule still caps radiation entropy for rotating AdS BHs; Kerr-AdS swallow-tail phase structure can imprint a jump on the Page curve in fixed-spin ensemble (ensemble-dependent). EPJC DOI 10.1140/epjc/s10052-026-15820-y.

## Key claims and results

- Near-horizon reduction of Kerr-AdS + island rule: without an island, radiation entropy grows linearly forever; with one island, late-time entropy saturates at $2S_{BH}$ — Page curve restored for spinning AdS.
- Page time and scrambling time ~$(1/\kappa)\log S_{BH}$ match expected “fastest scrambler” scaling.
- Canonical-ensemble free energy reproduces the known Kerr-AdS swallow-tail below critical spin $a_c\approx0.12455$ (AdS radius = 1): small / unstable-intermediate / large branches.
- Linear horizon-shrinkage ansatz swept through that branch structure → sharp discontinuity on the dynamical Page curve when a first-order transition is present; smooth when absent (small BH or above $a_c$).
- Alternative $\zeta$-ensemble (Legendre transform conjugate to spin) has no swallow-tail → Page curves stay continuous. Discontinuity is ensemble-dependent.

## Physical intuition

Hawking’s bookkeeping lets radiation entropy grow without bound; unitarity demands a turnover (the Page curve). The island rule lets the entanglement calculation “reach into” the interior at late times and pick the cheaper description — entropy caps. Kerr-AdS already has a liquid-gas-style first-order transition in spin. If you let an evaporating hole’s radius sweep through that equilibrium branch structure, the information-recovery curve can develop a kink or jump — but only in the ensemble that actually supports the transition.

## Limitations and assumptions

- Slow-rotation limit $a\ll M$; superradiance neglected throughout.
- s-wave / near-horizon 2D reduction; higher partial waves and greybodies dropped without a quantified error bar.
- Discontinuity claim stitches an imported linear $dr_+/dt$ ansatz through *equilibrium* branches, including the thermodynamically unstable intermediate branch — not jointly derived from the island calculation.
- New $\zeta$-ensemble is a formal Legendre device; no boundary-CFT meaning and no engagement with restricted-phase-space Kerr-AdS literature.
- Single-group EPJC article; phase-transition-imprint claim unreplicated.

## Connections

- Synthesis (evaporation / NEC): [[black-hole-evaporation-energy-conditions]]
- Synthesis (entropic / QI gravity): [[entropic-information-gravity]]
- QG info / holography deep dive: [[qg-deep-dive-2-info-holography]]
- Concept: [[hawking-radiation]]
- Dynamical first-law / far-from-equilibrium thermo: [[bh-thermo-far-from-equilibrium]]

## Source

- `raw/analyses/2026-09-13_doi-10.1140-epjc-s10052-026-15820-y_entanglement-islands-page-curves-kerr-ads.md`
