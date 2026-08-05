---
tags: [papers, condensed-matter, spintronics, topology, chiral-magnets]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [spin-flip-flop-saf, photonic-supersolid, quantum-metric-spin-momentum-locking, nonabelian-photonic-braiding]
source_analysis: "spacex_export/extracted-analyses/2026-02-14_electric-nucleation-of-3d-magnetic-heliknotons_65da18c4.md"
---

# Electrically Written Magnetic Heliknotons in FeGe

**One-line summary:** Li et al. (*Nature Materials* 2026) nucleate and steer 3D magnetic heliknotons in FeGe with nanosecond current pulses at zero external field; holography + micromagnetic fits reveal a distorted skyrmion–antiskyrmion core that moves straight (Hall cancellation).

## Key claims and results

- **Paper:** Long Li et al., *Nature Materials* (2026), DOI 10.1038/s41563-025-02450-0.
- Material: chiral magnet FeGe (Dzyaloshinskii–Moriya helix ground state).
- FIB microdevices with electrodes; pulse densities ~$7\times10^{10}$ A m$^{-2}$, durations 1–40 ns, $B=0$.
- Spin-transfer torque nucleates a heliknoton (Hopf-class 3D knot) over an energy barrier (min-energy-path sims).
- Angle-dependent electron holography + MuMax3 fits: z-distorted skyrmion–antiskyrmion pair with knotted spin texture.
- Further pulses translate the soliton collinearly without skyrmion-Hall deflection (emergent-field cancellation of the pair).
- Sequencing pulses enables 3D position control; LLG dynamics track rigid translation/rotation/dilation.

## Physical intuition

2D skyrmions are spin whirlpools on a surface. Heliknotons are **volume knots** — linked preimages of spin directions with a Hopf index, like knotted magnetic field lines. Current pulses are the writing stylus: spin-transfer torque twists the helical ground state over a barrier into the knot. Once written, the skyrmion half and antiskyrmion half feel opposite Hall pushes, so the package slides straight — no sideways racetrack drift.

## Technical connections (why this is not “just another skyrmion”)

A Hopf index counts how spin directions on a sphere wrap and link through 3D space. That is a **topological charge of a texture**, not a fractional electric charge: the heliknoton is a classical soliton in an ordered magnet, fully describable by continuum micromagnetics once DMI sets the preferred helix. The write process is barrier crossing under spin-transfer torque — engineering of a metastable knot — while readout is holography plus MuMax3 matching of the projected phase map. Hall cancellation is geometry: skyrmion and antiskyrmion partners produce opposite emergent Lorentz deflections, so the center of mass tracks the current direction. That makes heliknotons interesting for racetrack-style memory without the sideways drift that plagues single-skyrmion tracks, but it does **not** put them in the same ontology as FCI anyons or photonic non-Abelian braids ([[condensed-matter-topology-fractionalization]] Thread C vs A/D).

## Limitations and assumptions

- Cryogenic (FeGe helimagnetism below ~280 K); room-temp materials open.
- Nucleation probability plateaus below ~50%; defects/heating matter.
- Nanoscale devices; array cross-talk untested.
- Classical micromagnetics; quantum/disorder effects under-modeled.
- Analysis-based ingest; verify thresholds and Hopf assignment against primary paper.

## Connections

- Magnon / SAF neighbors: [[spin-flip-flop-saf]], [[magnons]]
- Topological soft matter of light: [[photonic-supersolid]]
- Geometric spin transport: [[quantum-metric-spin-momentum-locking]]
- Other electrically / topologically steered spin textures: Hopf-class 3D knots sit above 2D skyrmion racetracks; contrast with non-Abelian photonic braiding of modes ([[nonabelian-photonic-braiding]]) as a different platform for “write and reconfigure topology.”
- Concepts: [[magnons]]
- Key terms: heliknoton, Hopf soliton, chiral magnet, spin-transfer torque, skyrmion Hall effect
- Synthesis: [[condensed-matter-topology-fractionalization]] (fractionalization & topology map)

## Source

- `spacex_export/extracted-analyses/2026-02-14_electric-nucleation-of-3d-magnetic-heliknotons_65da18c4.md`
