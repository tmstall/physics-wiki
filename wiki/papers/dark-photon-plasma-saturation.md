---
tags: [papers, cosmology, dark-matter, plasma, dark-photons]
last_updated: 2026-08-16
status: analysis-ingest
related_papers: [axion-detector-quantum-erasure, lab-blazar-pair-instability, dense-plasma-opacity-revision, gamma-glow-pbh-detector]
source_analysis: "raw/analyses/2026-08-16_doi-10.1103-98cx-7t43_dark-photon-dark-matter-nonlinear-plasma-saturation.md"
---

# Dark-Photon Resonant Heating: Nonlinear Plasma Saturation Weakens Cosmological Bounds

**One-line summary:** Hook, Huang & Shalaby (*PRL* 2026) show resonant dark-photon → Langmuir conversion self-limits via ponderomotive density detuning and wave breakup; heating saturates near thermal energy, weakening classic resonant-conversion $\varepsilon$ bounds by ~$10^3$–$10^7$ and leaving non-resonant / dark-ages / Lyα channels as leading constraints.

## Key claims and results

- **Paper:** *Phys. Rev. Lett.* **137**, 071004 (2026), DOI 10.1103/98cx-7t43; arXiv:2510.13956.
- Target: kinetic-mixing dark photon DM; cosmological resonant conversion when $\omega_p(t)=m_{A'}$ heats pre-/post-recombination plasma.
- Critique: linear Landau–Zener heating assumes a passive plasma; PIC (1+1D) shows nonlinear quiver + ponderomotive force redistributes density, detunes resonance, cascades to higher-$k$ Langmuir + ion-acoustic turbulence.
- Saturation: deposited energy ~$O(1)$–$O(100)\times$ electron thermal energy — far below linear prediction.
- Consequence: old resonant $\varepsilon$ bound too strong by factors ~3000–$10^7$ over ~$10^{-14}$–$10^{-4}$ eV; re-derive weaker non-resonant heating + dark-ages ($T\lesssim10$ eV, $z\sim20$–$500$) + Lyα forest ($T\lesssim0.8$ eV, $z\sim2$–$6$) limits.
- Does **not** rule DM in — replaces over-strong bound with weaker ones.

## Physical intuition

Resonance looks like a slow sweep through an LC tank that dumps dark-photon energy into plasma ringing. Once the ringing is as hard as thermal motion, the plasma’s own amplitude **changes the spring constant** (density), detunes the resonance, and breaks into turbulence — a self-limiting circuit, not a bottomless heater. Cosmology had budgeted as if the tank never detuned.

## Limitations and assumptions

- 1+1D unmagnetized PIC — 3D/magnetized cosmological plasma open (authors flag).
- Saturation “~thermal” is order-of-magnitude, hence wide weakening factors.
- Single-group simulation result; independent PIC codes needed.
- Analysis from full arXiv companion to PRL.

## Connections

- Synthesis: [[dark-matter-detection-channels]]

- Other DM detection theory: [[axion-detector-quantum-erasure]], [[gamma-glow-pbh-detector]]
- Lab plasma nonlinearities: [[lab-blazar-pair-instability]], [[dense-plasma-opacity-revision]]
- Concepts: [[warm-dense-matter]] (different regime; shared nonlinear plasma language)
- Soft x-ray TES instrumentation (not DM): [[bessy-tes-soft-xray-spectrometer]]

## Source

- `raw/analyses/2026-08-16_doi-10.1103-98cx-7t43_dark-photon-dark-matter-nonlinear-plasma-saturation.md`
