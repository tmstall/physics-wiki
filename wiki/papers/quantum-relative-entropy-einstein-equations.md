---
tags: [papers, quantum-gravity, qft, black-hole-thermodynamics, foundations]
last_updated: 2026-08-22
status: analysis-ingest
related_papers: [gravity-from-entropy, hawking-radiation-charge-shell, evaporating-charged-black-holes, frozen-in-gravitational-fields, black-hole-third-law-violation]
source_analysis: "raw/analyses/2026-08-20_doi-10.1103-lmq8-nsty_quantum-relative-entropy-semiclassical-einstein-equations.md"
---

# From Quantum Relative Entropy to Semiclassical Einstein Equations

**One-line summary:** Dorau & Much replace Jacobson’s ill-defined classical horizon entropy with finite QFT relative entropy on a local Killing horizon (free scalar, coherent states) and re-derive the semiclassical Einstein equation as a thermodynamic identity (*PRL* **136**, 091602, 2026).

## Key claims and results

- **Paper:** Philipp Dorau & Albert Much, *Phys. Rev. Lett.* **136**, 091602 (2026). DOI 10.1103/lmq8-nsty; arXiv:2510.24491.
- Problem: Jacobson 1995 needs $\delta Q=T\delta S$ on local Rindler horizons, but von Neumann entropy diverges in type-III QFT algebras.
- Fix: Araki–Uhlmann relative entropy of vacuum vs coherent excitation on the horizon algebra — finite; modular flow = geometric boost (Bisognano–Wichmann / Kay–Wald lineage).
- Exact identity: $S^{\rm rel}(\omega_0\|\omega_\phi)=-2\pi\int_{\mathcal H} U(\partial_U\phi)^2\,dU\,d{\rm vol}_{\mathcal S}$ ↔ boost-weighted null energy flux.
- With imported Bekenstein–Hawking $S=A/4G$ + Raychaudhuri → pointwise semiclassical Einstein equation $R_{ab}-\tfrac12 Rg_{ab}+\Lambda g_{ab}=8\pi G\langle T_{ab}\rangle$.
- Scope: free scalar; closed form for **coherent** states; local/pointwise — not a new global Cauchy theory.

## Physical intuition

Absolute horizon entropy is an infinite checksum. Relative entropy is a **diff** against the vacuum reference — finite even when each file is endless. On a bifurcate horizon the modular “diff clock” *is* the boost, so the info-theoretic distinguishability equals a geometric energy flux — Clausius without classical hand-waving at that step.

## Limitations and assumptions

- $S=A/4G$ still imported, not derived.
- Worked example = coherent (quasi-classical) excitations, not generic entangled states.
- Free scalar on local Killing horizon — not interacting QFT / dynamical horizons.
- Two-author theory Letter; independent modular recalculation not yet visible.

## Connections

- Entropic / emergent gravity: [[gravity-from-entropy]], [[modified-speculative-gravity]]
- Horizon thermo: [[hawking-radiation-charge-shell]], [[evaporating-charged-black-holes]], [[black-hole-thermodynamics]]
- Geometry constraints: [[frozen-in-gravitational-fields]], [[black-hole-third-law-violation]]
- Synthesis: [[entropic-information-gravity]] (primary — thermo/QI → Einstein)
- Synthesis: [[black-hole-evaporation-energy-conditions]], [[modified-speculative-gravity]]

## Open questions

- Extend relative-entropy Clausius beyond coherent states / free fields?
- Dynamical (non-Killing) horizons?
- Independent group verification of the modular identity?

## Source

- `raw/analyses/2026-08-20_doi-10.1103-lmq8-nsty_quantum-relative-entropy-semiclassical-einstein-equations.md`
