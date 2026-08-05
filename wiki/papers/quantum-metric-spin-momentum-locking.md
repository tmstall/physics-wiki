---
tags: [papers, condensed-matter, quantum-geometry, spintronics, oxide-interfaces]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [snte-light-topological-inversion, brown-zak-nonlinear-transport, ciss-homochirality, nickelate-nodeless-gap-arpes]
source_analysis: "spacex_export/extracted-analyses/2026-02-08_quantum-metric-from-spin-momentum-locking_7ba11668.md"
---

# Quantum Metric from Spin-Momentum Locking (LAO/STO)

**One-line summary:** Spin-momentum locking (Rashba-type) forces a finite **quantum metric** into ordinary inversion-broken SOC bands; Sala et al. (*Science* 2025) measure its fingerprint as gate-tunable, $B$-odd nonlinear magnetoresistance in 111-LaAlO₃/SrTiO₃.

## Key claims and results

- **Paper:** Giacomo Sala et al., *Science* **389**, 822 (2025), DOI 10.1126/science.adq3255 (analysis framing).
- Quantum geometric tensor = Berry curvature (imaginary) + quantum metric (real). Metric lagged experiments outside exotic magnets.
- Theory: minimal Rashba (+ warping) models yield diagonal metric $g_{xx}=g_{yy}$ finite and set by locking strength — no magnetism or nontrivial topology required.
- Nonlinear conductivity term odd in in-plane $B$ tracks the metric.
- Experiment: 111-LaAlO₃/SrTiO₃ 2DEG; second-harmonic nonlinear resistance after subtracting symmetric/extrinsic backgrounds.
- Gate voltage tunes density → Rashba strength → metric signal; angular dependence matches crystal symmetry.

## Physical intuition

Berry curvature is the “magnetic field” of band geometry; the quantum metric is the **distance** between nearby Bloch states. Spin-momentum locking ties spin to velocity like a rifled bullet — that helical twist bends the wavefunction so hard that the metric cannot stay zero. You then read geometry electrically: a current-squared correction to resistance that flips with in-plane field, without needing a net magnetization.

## Metric vs topology (keep the labels clean)

Finite quantum metric does **not** require a Chern number or a fractional filling. Ordinary inversion-broken Rashba bands already carry a real geometric tensor piece. That is why this experiment sits next to Brown–Zak nonlinear transport ([[brown-zak-nonlinear-transport]]) as a **geometry → nonlinear conductivity** tool, and why it should not be cited as “fractionalization evidence” on [[condensed-matter-topology-fractionalization]]. Geometry can *enable* correlated mini-band physics in moiré stacks; measuring $g_{ij}$ in LAO/STO is a controlled interface laboratory for that language, not a substitute for FCI optics or 1D anyon tails.

## Limitations and assumptions

- Isolation of the pure metric channel requires careful subtraction of extrinsic nonlinearities.
- (111) LAO/STO is a specific interface; quantitative transferability to other Rashba systems open.
- Higher-order warping and multi-band effects can reshape the metric tensor.
- Analysis-based ingest; verify formulas and gate maps against *Science* primary paper.

## Connections

- Light-driven topology / inversion-breaking: [[snte-light-topological-inversion]]
- Moiré quantum geometry transport: [[brown-zak-nonlinear-transport]]
- Spin-selective interfaces: [[ciss-homochirality]]
- Oxide / correlated films: [[nickelate-nodeless-gap-arpes]]
- Key terms: quantum metric, Rashba spin-orbit, nonlinear magnetoresistance, LAO/STO 2DEG

- Related (SpaceX set): [[magnetic-heliknoton-electric-write]] — Electric heliknoton write in FeGe
- Synthesis: [[condensed-matter-topology-fractionalization]] (fractionalization & topology map)

## Source

- `spacex_export/extracted-analyses/2026-02-08_quantum-metric-from-spin-momentum-locking_7ba11668.md`
