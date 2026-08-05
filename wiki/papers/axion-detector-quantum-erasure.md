---
tags: [papers, dark-matter, axions, quantum-optics, detectors]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [synchrotron-dm-detector, gw-induced-fermion-freeze-in, gamma-glow-pbh-detector, noise-driven-qubit-entanglement]
source_analysis: "spacex_export/extracted-analyses/2026-05-25_axion-quantum-signatures-erased-in-detectors_6487c8e0.md"
---

# Axion Quantum Signatures Erased in Haloscope Detectors

**One-line summary:** A fully quantum model of axion–photon conversion shows that mode averaging plus the tiny $g_{a\gamma\gamma}$ coupling erase all intrinsically nonclassical $P$-function signatures before readout — so the classical oscillating-field treatment used by ADMX-class experiments is the exact prediction of the quantum theory under realistic detector physics.

## Key claims and results

- **Problem:** Axion DM is routinely treated as a classical field $\phi(t)\approx\phi_0\cos(m_a t+\cdots)$ because occupation numbers are huge ($\gtrsim10^{28}$). Huge occupation alone does **not** guarantee classicality (squeezed/cat states can still be nonclassical).
- **Method:** Keep the dark-matter state fully general via Glauber–Sudarshan $P_{\rm DM}$; couple cavity photons only to one **effective** axion mode $a_{\rm eff}$ that is a weighted sum of many momentum modes inside the cavity acceptance.
- Interaction is a weak beam-splitter Hamiltonian with $g\propto g_{a\gamma\gamma}B_0\sqrt{\Omega}$ absurdly small.
- **Result 1 (mode averaging):** Quantum central-limit theorem drives the effective $P$ toward a positive Gaussian even if every constituent mode is violently nonclassical.
- **Result 2 (weak coupling):** Residual negativity / non-Gaussianity is diluted by powers of conversion efficiency $\eta\ll1$ and swamped by vacuum (or technical) noise; integration times to resolve it exceed cosmic timescales.
- Entanglement witnesses between DM modes or DM–cavity sector suffer the same suppression.
- Practical upshot: classical-field forecasts for haloscopes are not an approximation of convenience — they are what full quantum optics predicts once detector coarse-graining is included.

## Physical intuition

A cavity does not listen to one pure axion tone. It averages thousands of independent momentum modes, then multiplies the result by a coupling so feeble it looks like a beam splitter that barely opens. Averaging is a quantum central-limit blender; the tiny transmission is a further diluter. Even if the galactic axion field were a Schrödinger cat, the detector would still report a classical noisy sine wave.

## Limitations and assumptions

- Detailed for resonant cavity haloscopes; ABRACADABRA, CASPEr, dish antennas share qualitative weak-coupling suppression with different form factors.
- Assumes statistically independent modes in the effective sum; engineered galactic-scale long-range entanglement could in principle evade the CLT (no known production channel).
- Does **not** kill classical spectral anomalies or nonstandard energy distributions — only intrinsically quantum signatures (negativity, certain witnesses).
- Analysis-based ingest; verify $\eta$ scalings and mode-count estimates against primary paper.

## Connections

- DM detection hardware: [[synchrotron-dm-detector]], [[gamma-glow-pbh-detector]]
- Cosmological DM production context: [[gw-induced-fermion-freeze-in]], [[primordial-black-holes]]
- Quantum optics / nonclassical states: [[noise-driven-qubit-entanglement]], [[massive-tunneling-schrodinger-cats]]
- Detector classicalization note: even if the galactic field were a cat or squeezed state, the cavity still reports a classical noisy tone — same practical lesson as treating macroscopic occupation carefully in [[massive-tunneling-schrodinger-cats]].
- Key terms: axion haloscope, Glauber–Sudarshan $P$-function, mode averaging, $g_{a\gamma\gamma}$, quantum central-limit theorem

## Source

- `spacex_export/extracted-analyses/2026-05-25_axion-quantum-signatures-erased-in-detectors_6487c8e0.md`
