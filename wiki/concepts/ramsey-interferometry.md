---
tags: [concepts, quantum-sensing, metrology]
last_updated: 2026-07-31
status: draft
related_papers: [time-goes-quantum, quantum-proper-time-ion-clocks, massive-tunneling-schrodinger-cats]
---

# Ramsey Interferometry

**One-line summary:** Split a quantum system into a coherent superposition, let a relative phase accumulate, recombine, and read the phase out as a population imbalance — the quantum lock-in amplifier for precision sensing.

## Physical picture

Three acts:

1. **Split** (π/2 pulse or half-tunneling event): create a balanced superposition of two “arms.”
2. **Precess** (dark / free evolution time \(T\)): any energy difference between arms accumulates phase \(\phi \propto \Delta E \cdot T\).
3. **Recombine** (second π/2): convert phase into measurable populations; fringes vs. \(T\) or controlled detuning give the signal.

Fringe **contrast / visibility** measures how coherent the superposition remained. Anything that entangles the system with an unobserved degree of freedom (motion, environment, which-path information) reduces contrast.

## Appearances in this wiki

| Paper | What Ramsey measures |
| --- | --- |
| [[time-goes-quantum]] | Contrast vs. \(T\) fingerprints motional state / quantum proper time |
| [[quantum-proper-time-ion-clocks]] | Visibility loss as entanglement witness under squeezing |
| [[massive-tunneling-schrodinger-cats]] | NOON-state phase accumulation; sub-SQL energy-gradient sensing |

## Engineering analogy

Lock-in amplifier: encode a weak signal as a phase relative to a reference, integrate, demodulate. Ramsey is the same idea with quantum amplitudes instead of RF voltages.

## Related pages

- [[noon-states]]
- [[quantum-proper-time]]
- [[optical-ion-clocks]]
