---
tags: [papers, antimatter, quantum-optics, matter-waves]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [3d-electron-diffraction-osc, sunlight-spdc-ghost-imaging, truncated-photon-dynamical-casimir]
source_analysis: "spacex_export/extracted-analyses/2026-01-19_positronium-diffraction-breakthrough-in-antimatter-physics_1d9d4313.md"
---

# Positronium Diffraction from Graphene

**One-line summary:** Nagata et al. (*Nature Communications* 2025) observe first-order diffraction of a coherent keV positronium beam from few-layer graphene — matter-wave interference of a bound electron–positron atom as a single quantum object.

## Key claims and results

- **Paper:** Yugo Nagata et al., *Nature Communications* (2025), DOI 10.1038/s41467-025-67920-0.
- Beam path: $^{22}$Na → moderated $e^+$ → Ps$^-$ on W → accelerate → UV photodetachment → neutral Ps up to ~3.3 keV.
- Photodetachment keeps energy spread narrow enough for coherent diffraction (key improvement over hot-surface Ps beams).
- Transmission through 2–3 layer graphene on TEM grid; TOF velocity gating; MCP position-sensitive detection.
- Spatial map shows first-order diffraction shoulder at the angle expected from $\lambda=h/p$ with $m_{\rm Ps}=2m_e$ and graphene lattice $d\approx0.246$ nm.
- Energy dependence matches quantum diffraction, not classical scattering; treats Ps as one wave, not separate $e^+$ and $e^-$ waves.

## Physical intuition

Electrons, neutrons, and even fullerenes have waved through gratings. Positronium is a fleeting hydrogen-like atom made of matter and antimatter — hard to make into a clean beam. Build a tunable Ps “laser” by accelerating a charged ion then laser-peeling the extra electron, fire it through atomic chicken wire (graphene), and the interference lobes prove the whole pair travels as one de Broglie wave.

## Why photodetachment matters

Hot-surface Ps sources spit out a messy velocity spray; the coherence length collapses and diffraction washes out. The ion-then-peel path freezes energy spread to what the accelerator and laser bandwidth allow, so the de Broglie phase front stays flat enough to resolve a first-order Bragg shoulder. Graphene is a fixed atomic grating ($d\approx0.246$ nm): the diffraction angle is a pure $\lambda=h/p$ check with $m=2m_e$. If $e^+$ and $e^-$ diffracted independently, the pattern would not match a single composite wavelength. That is the antimatter engineering lesson — composite matter waves need beam quality as carefully as cold atoms need laser cooling, even when the particle is not trapped.

## Limitations and assumptions

- Only first-order peak resolved; higher orders washed by divergence.
- Graphene ripples/defects can broaden spots.
- Ps lifetime limits flight path / interferometer size.
- Higher-energy beams enter relativistic corrections to reduced mass.
- Analysis-based ingest; verify energies and angular matches against primary paper.

## Connections

- Electron diffraction of organics: [[3d-electron-diffraction-osc]]
- Quantum optics / imaging neighbors: [[sunlight-spdc-ghost-imaging]], [[truncated-photon-dynamical-casimir]]
- Structured-light / OAM cousin: [[twisted-light-chiral-ms]]
- Near-field / interface wave structure (different physics, same “hidden momentum in constrained waves” flavor): [[evanescent-wave-transverse-spin]]
- Antimatter / composite-matter wave note: Ps diffracts as one de Broglie object of mass $2m_e$, not as independent $e^+$ and $e^-$ gratings.
- Matter-wave / AMO control cousins: [[amo-quantum-state-control]] (state engineering culture, different platform)
- Key terms: positronium, matter-wave diffraction, photodetachment beam, graphene grating

## Source

- `spacex_export/extracted-analyses/2026-01-19_positronium-diffraction-breakthrough-in-antimatter-physics_1d9d4313.md`
