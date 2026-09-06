---
tags: [papers, quantum-simulation, cft, rydberg, criticality]
last_updated: 2026-08-22
status: analysis-ingest
related_papers: [quantum-state-sculptor, fractional-fermi-sea-1d-bosons, problem-of-time-cold-atoms, nonabelian-photonic-braiding, qg-deep-dive-2-info-holography]
source_analysis: "raw/analyses/2026-08-20_doi-10.1038-s41586-026-10904-x_cft-spectra-quantum-simulator.md"
---

# CFT Excitation Spectra in a Rydberg Quantum Simulator

**One-line summary:** Modulation spectroscopy on a ⁸⁸Sr Rydberg array (up to L=35) resolves discrete Ising and tricritical-Ising CFT level towers with universal ratios (e.g. even-sector 2:4:6:8) — first direct many-body CFT spectrum measurement in any physical system (*Nature* 2026).

## Key claims and results

- **Paper:** *Nature* (2026), DOI 10.1038/s41586-026-10904-x (Caltech + theory collaborators).
- Platform: 1D tweezer array realizing FSS / Rydberg blockade Hamiltonian; disordered ↔ ℤ₂ CDW phases with Ising critical line ending at tricritical Ising (TCI) point.
- Technique: adiabatic prepare near criticality → weak coherent modulation (global or odd-parity local detuning) → ramp + readout $\delta n$; peaks map gaps and matrix elements.
- Ising (L=19): even ratios **2:4:6:8**; odd **3:5:7**; $L$-collapse for $L\ge19$; linear $E=\hbar v k$ light-cone from finite-$k$ drive.
- TCI: interacting CFT (no free-fermion rewrite); boundary-condition-dependent universal ratios (e.g. 4/3 free, 2 fixed) accessed experimentally.
- Payoff: path toward dynamical structure factor / unknown-class identification when classical simulation fails.

## Physical intuition

CFT in a finite box predicts a discrete “chord” of excitation energies whose **ratios** are universal — machine-independent once you normalize out the non-universal velocity. Modulation spectroscopy is a chirp: shake at frequency $f$ until the many-body chain rings, then read which notes sound.

## Limitations and assumptions

- Single lab / single atomic species; no ion or superconducting-qubit replication yet.
- Small $L$ shows large non-universal corrections; clean CFT ratios need $L\gtrsim19$.
- Theory confirmation of expected ratios — not a surprise about which CFT governs the FSS line.

## Connections

- Cold-atom / QI neighbors: [[quantum-state-sculptor]], [[fractional-fermi-sea-1d-bosons]], [[problem-of-time-cold-atoms]]
- Topology / braids (different angle): [[nonabelian-photonic-braiding]]
- CFT language cousin (holography): [[qg-deep-dive-2-info-holography]]
- Synthesis: [[amo-quantum-state-control]]; light [[condensed-matter-topology-fractionalization]] (criticality / CDW order context)

## Open questions

- Reproduce universal ratios on a microscopically different platform?
- Full dynamical structure factor mapping of unknown transitions?
- How far into the TCI multicritical window do corrections stay under control?

## Source

- `raw/analyses/2026-08-20_doi-10.1038-s41586-026-10904-x_cft-spectra-quantum-simulator.md`
