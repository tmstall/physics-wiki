---
tags: [papers, cold-atoms, quantum-sensing, macroscopic-superposition]
last_updated: 2026-07-31
status: analysis-ingest
related_papers: []
source_analysis: "raw/analyses/Quantum Tunneling Just Hauled a 608-Dalton Object Into Superposition .md"
---

# Massive Tunneling Schrödinger Cats

**One-line summary:** Ultracold Rb clusters of up to 7 atoms (~608 atomic mass units) tunnel as rigid composites through an optical superlattice barrier, forming spatial NOON / cat states used for sub-SQL quantum sensing.

## Key experimental numbers

| Quantity | Value (from analysis) |
| --- | --- |
| Species / cluster size | ⁸⁷Rb; \(n = 1\ldots7\) atoms per double well |
| Mass at \(n=7\) | ~608.4 u |
| Matter-wave (de Broglie) scale | ~320 nm |
| Well / barrier scale | ~532 nm lattice spacing (optical) |
| Tunneling dynamics | Coherent Rabi-like left–right oscillations; rate only weakly dependent on \(n\) (near-unity mass scaling in the \(J_0/U\sim 1\) regime) |
| Sensing | Sub-µm energy gradients at **hertz-level** precision; claimed sub-SQL (Heisenberg-scaling with \(n\)) |
| Parallelism | Hundreds of identical double-well units |
| Coherence limits | Superlattice phase noise, technical vibration, three-body recombination; cavity stabilization proposed for ~10³ longer coherence |

*Exact oscillation frequencies and coherence times are not pinned down in the ingested analysis — treat as qualitative until checked against arXiv:2502.06246.*

## Key claims and results

- Cold ⁸⁷Rb atoms loaded into an optical **superlattice** (array of double wells) in the Mott-insulator regime give exact integer filling \(n = 1\ldots7\) per well unit.
- Strong **on-site repulsion** does not scatter the cluster apart; it **forbids partial hopping**. The only resonant move is all \(n\) atoms left ↔ all \(n\) right — collective center-of-mass tunneling.
- In the regime where single-particle tunnel coupling and interaction energy are comparable (\(J_0/U \sim 1\)), tunneling rate barely falls with mass — **defeating the naive exponential mass curse**.
- Tunneling generates **NOON states** \((|n,0\rangle + e^{i\phi}|0,n\rangle)/\sqrt{2}\); Ramsey sequences with these cats beat the standard quantum limit on sub-micron energy gradients (hertz-level precision claimed).
- Matter-wave scale ~320 nm. Claimed record mass for coherent COM tunneling of an indivisible composite — provisional pending primary-paper check.

## Physical intuition

Seven people in a phone booth next to an empty booth: the “rule” of energy conservation only allows everyone to switch booths together. One person sneaking through alone is off-resonance by roughly the interaction energy \(U\). Repulsion is not glue in the chemical sense — it **locks out every escape route except the collective one**.

Cooling to nanokelvin stretches the de Broglie wavelength until it matches the laser-scale barrier (~half a micron). The object is still a few nanometers physically; its *quantum* presence spans optical wavelengths.

## Limitations and assumptions

- 608 u is a record-scale for this platform class, but still **many orders of magnitude** below masses proposed for gravitational entanglement tests (BMV-type).
- Coherence limited by superlattice phase noise, vibrations, and **three-body recombination** in dense clusters.
- Entanglement certified interferometrically, not by full tomography or loophole-free Bell tests at large separation.
- The \(J_0/U \approx 1\) sweet spot is fragile under drift.
- Primary reference cited in analysis: arXiv:2502.06246 (verify publication status and exact claims).

## Connections

  - Concepts: [[collective-tunneling]], [[noon-states]], [[optical-lattices]], [[ramsey-interferometry]]
- Sensing link: quantum-enhanced inertial / gradient measurements; long-term interest in macroscopic superpositions and quantum gravity tests.
- Contrast with ion-clock [[quantum-proper-time]] work ([[time-goes-quantum]]): here the “two places at once” is **spatial**; there it is **proper-time / motional**.
- Cold-atom platform cousin (dwell-time weak values, not spatial cats): [[negative-weak-valued-excitation-times]].
- Continuous-variable non-Gaussian “cat cousins” (ions, not lattice NOON): [[quantum-state-sculptor]]
- Synthesis: [[quantum-time-across-platforms]]

## Open questions

- How far can cavity-stabilized lattices push mass (analysis projects ~10⁴ u-scale with large coherence gains)?
- Fermionic species or different elements to suppress three-body loss?
- Clean path from this platform toward gravitationally relevant superpositions?

- Synthesis: [[amo-quantum-state-control]] (AMO state control)

- Synthesis: [[measurement-problem-threads]] (foundations: measurement problem threads)

## Source

- Analysis: `raw/analyses/Quantum Tunneling Just Hauled a 608-Dalton Object Into Superposition .md`
