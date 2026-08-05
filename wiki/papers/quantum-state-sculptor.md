---
tags: [papers, quantum-optics, trapped-ions, continuous-variable]
last_updated: 2026-08-02
status: analysis-ingest
related_papers: [massive-tunneling-schrodinger-cats, photon-number-optical-analogy-control, dissipative-cavity-entanglement, macroscopic-crystal-entanglement-neutrons]
source_analysis: "claude_export/extracted-analyses/2026-06-10_the-quantum-state-sculpto_35bae5fb.md"
---

# Quantum State Sculptor: Non-Gaussian Oscillator Superpositions

**One-line summary:** Oxford trapped-ion experiment creates the first superpositions of *nonclassical non-Gaussian* oscillator states — including trisqueezed and quadsqueezed constituents and mixed-order pairs — via spin-conditioned nonlinear bosonic drives and mid-circuit heralding on $^{88}$Sr$^+$.

## Key claims and results

- Platform: single $^{88}$Sr$^+$ ion; axial motion as QHO (~1.2 MHz); internal levels as spin qubit / qutrit; 674 nm spin-motion coupling.
- Engineered Hamiltonian family $H_k\propto\sigma_z(a^k e^{-i\phi}+{\rm h.c.})$ for order $k=2,3,4$ (squeeze / trisqueeze / quadsqueeze).
- Protocol: spin superposition → conditional nonlinear drive → second rotation → mid-circuit fluorescence herald that projects a pure oscillator superposition while leaving motion intact on the dark branch.
- Demonstrates superpositions of opposite generalized-squeezed states and, with qutrit shelving, **independent** control of order, amplitude, and phase on each branch (e.g. $k=2$ with $k=3$).
- Full tomography via characteristic-function sampling → reconstructed Wigner functions with clear negativity and interference fringes matching simulation.
- Positions continuous-variable state engineering above ordinary coherent-state cats and Gaussian-squeezed cats toward states useful for CV error correction and metrology.

## Physical intuition

A harmonic oscillator is an infinite ladder of rungs. Cats usually superpose two “classical” laser-like blobs. Squeezing flattens the blob into an ellipse. Higher-order drives sculpt multi-lobe, non-Gaussian shapes (three-fold, four-fold symmetry in phase space). The ion’s internal spin is a control bit that decides *which way* the sculptor’s tool turns. Put the spin in superposition and both tools cut at once; a careful mid-circuit measurement then *selects* the even or odd combination without scattering photons that would heat the motion. Shelving one branch on an auxiliary spin level lets you cut two *different* shapes and recombine them — a factory for arbitrary exotic cat cousins, not just mirror images of one mold.

## Limitations and assumptions

- Analysis-based ingest; verify fidelities, success probabilities, and $k=4$ performance against the PRX primary paper.
- Heralded success probability falls as branches become orthogonal (~50% asymptote for large opposite squeezings); mixed-order protocols add overhead.
- Residual thermal phonons, laser phase noise, and decoherence limit achievable non-Gaussianity and Wigner negativity depth.
- Single-mode demonstration; multi-mode CV codes need further wiring.

## Connections

- Macroscopic / cat-like states: [[massive-tunneling-schrodinger-cats]], [[macroscopic-crystal-entanglement-neutrons]]
- Optical state control neighbor: [[photon-number-optical-analogy-control]]
- Engineered open-system entanglement: [[dissipative-cavity-entanglement]]
- Key terms: continuous-variable QHO, trisqueezing, quadsqueezing, Wigner negativity, mid-circuit measurement, spin–motion coupling, GKP / cat codes (context)

- Synthesis: [[amo-quantum-state-control]] (AMO state control)

## Source

- `claude_export/extracted-analyses/2026-06-10_the-quantum-state-sculpto_35bae5fb.md`
