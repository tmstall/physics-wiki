---
tags: [papers, phonons, quantum-acoustics, circuit-qed]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [amo-quantum-state-control, time-goes-quantum, collective-superradiant-lasing]
source_analysis: "raw/analyses/2026-09-21_doi-10.1126-science.aeh7535_quantum-jumps-of-sound.md"
---

# Quantum Jumps of Sound

**One-line summary:** Science DOI 10.1126/science.aeh7535. First real-time hops of a chip-scale mechanical resonator between phonon number states (atom-jump analog). Long-coherence mechanics + integrated superconducting qubit; nondestructive readout heralds single phonons ~85% fidelity. Engineering breakthrough enabling the observation.

## Key claims and results

- Safavi-Naeini group (Stanford): a lithium-niobate mechanical resonator dispersively coupled to a superconducting qubit (circuit quantum acoustodynamics).
- Quantum-nondemolition readout of phonon number — the mechanical analog of number-resolved photon counting in circuit QED — tracks a real-time jump from $n=1$ to $n=0$.
- Historical ancestor is the 1986 single-atom quantum-jump experiments (shelving / bright–dark fluorescence). The result does not change the quantum-mechanics picture; it shows the predicted jumps directly.
- Load-bearing trick: aligned transfer-print integration keeps the mechanical mode coherent for on the order of 2 ms (Stanford press; the abstract’s exact lifetime was blank in the available text) while still coupling it tightly enough to a qubit.
- Single-phonon Fock states heralded at ~85% fidelity.
- Practical stake: a mechanical mode as a quantum memory or bus next to microwave photons and superconducting qubits.

## Physical intuition

An accelerometer measures position. Position and energy do not commute, so that readout averages over a spread of phonon numbers and looks smooth. A nondemolition measurement asks only “how many phonons?” and can ask again without erasing the answer — the SRAM-style read, not a destructive DRAM sense. Chip-scale mechanics parked next to lossy superconducting circuitry usually decoheres before a jump is visible. Millisecond coherence plus a usable qubit coupling is what made the hop watchable.

## Limitations and assumptions

- Lite analysis: the Science PDF, methods, and supplement were unreachable. Claims rest on the abstract plus press (Stanford, EurekAlert). The exact lifetime and the dispersive shift were missing from the pasted abstract.
- Single group, no independent replication. The fabrication is specialized enough that a slow follow-up is expected, not suspicious.
- The accessible description covers only $n=1 \leftrightarrow n=0$. Higher-$n$ resolution is open.
- ~85% heralding leaves about a 1-in-7 misassignment rate. The error budget (qubit decoherence, thermal phonons, crosstalk, transfer-print loss) is not in the source text.
- Whether jump waiting times match a Markovian exponential is unknown from this basis.

## Connections

- Synthesis: [[amo-quantum-state-control]]
- Other quantum-platform pages: [[time-goes-quantum]], [[collective-superradiant-lasing]]

## Source

- `raw/analyses/2026-09-21_doi-10.1126-science.aeh7535_quantum-jumps-of-sound.md`
