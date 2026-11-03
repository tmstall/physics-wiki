---
tags: [papers, molecular-magnetism, superconductivity, sts]
last_updated: 2026-10-31
status: analysis-ingest
related_papers: [condensed-matter-topology-fractionalization, magnons]
source_analysis: "raw/analyses/2026-10-11_doi-10.1103-mwl6-8nzl_coexisting-spin-vibrational-orbital-excitations.md"
---

# Sorting Spin, Vibration, and Orbital Excitations on a Superconductor

**One-line summary:** PRL DOI 10.1103/mwl6-8nzl. A magnetic molecule's in-gap state on a superconductor copies its asymmetry onto vibrations, so anything that breaks the pattern is a different excitation. Entrance/exit counting predicts peak-height ratios (2:1 for cobaltocene's lowest orbital move) without trusting bad energy predictions. The spin flip barely notices 8 T because neighbors lock it.

## Key claims and results

- PRL 137, 116403 (2026), Editors' Suggestion. Banerjee, Robles, Lorente, Berndt, and Weismann. Cobaltocene (a cobalt atom between two carbon rings, one unpaired electron) on superconducting lead, read with a superconducting lead tip.
- Molecules form ordered islands. Interior molecules show an in-gap Yu–Shiba–Rusinov state plus about fourteen sharp features spread over about a hundred millivolts on each side. Isolated molecules do not show the spin-flip or orbital features.
- The in-gap state is slightly lopsided (peak-height ratio near four fifths). Five vibrations copy that ratio, and the ratios move toward one when a field kills superconductivity.
- A strong low-energy peak with a ratio near one is the spin flip. It shifts in a field, but only about a tenth as much as a free spin would. The authors blame antiferromagnetic locking by neighbours. The decisive spin-model fit lives in an unread supplement.
- Two features keep ratios near two and near five in both the superconducting and the normal state. Counting routes gives the two: the lowest orbital move (about 9 meV) has two ways for an electron to enter and one way to leave. The high feature (about 90 meV) pulls an electron out of a filled orbital the tip barely reaches, so exit is nearly blocked.
- Conductance maps at the in-gap state and at the lowest orbital excitation show lobes at right angles, matching the two orbital shapes. The high-ratio feature has no such map.
- Gas-phase calculations name the orbitals and miss the energies by large factors (several times to tens of times). The energy labels are experimental. Theory is not the clock.

## Physical intuition

A tunneling spectrum is a list of doors the electrons can open. On a superconductor the in-gap state is the main door, and it is already a bit wider one way than the other. A vibration that only rides that door inherits the same lopsidedness. A peak that refuses to copy the pattern is using a different door. For the lowest orbital move the bookkeeping is concrete: two entrance routes, one exit, so the incoming peak should stand about twice as tall. That test does not need a calculated energy, which is the number this class of theory gets wrong. The spin flip's indifference to 8 T is the other tell. A lone spin would swing hard. A spin whose neighbours hold it antiparallel barely nods. The "single molecule" is a site in a small magnet.

## Limitations and assumptions

- The route count is a heuristic, not a transport calculation. Equal, independent channels are an assumption. Interference could make the factor of two partly lucky. The paper calls the picture heuristic.
- The ratio cleanly flags only the strongly lopsided peaks. Vibrational ratios scatter from about 0.6 to 1 and overlap the spin flip's ratio near 1. Strength and the field response still do that separation.
- Calculated orbital energies miss the measured ones badly, and they swing with geometry. The ~90 meV assignment rests on the ratio and orbital character alone.
- The weak field response leans on a supplement model. A zero-field versus 1 T discrepancy is about as large as the claimed shift from 1 T to 8 T. Anisotropic g-factor, substrate response, and tip field are not ruled out in the main text.
- Spectra are from selected molecules. The lowest orbital energy already shifts between neighbours. No error bars on energies or ratios.
- The closing "two qubits in one molecule" line measures neither coherence, lifetime, nor entanglement, and the features exist only inside coupled islands.
- Single group. Data on request. Supplement (Figs. S1–S10) was not in the analysis.

## Connections

- Synthesis: [[condensed-matter-topology-fractionalization]]
- Spin-wave / neighbour-locking cousin (this page is molecular spins in an island, not a magnon spectrum): [[magnons]]

## Source

- `raw/analyses/2026-10-11_doi-10.1103-mwl6-8nzl_coexisting-spin-vibrational-orbital-excitations.md`
