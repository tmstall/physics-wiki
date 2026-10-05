---
tags: [papers, photonics, topology, non-hermitian, silicon-photonics]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [nonabelian-photonic-braiding, photonic-supersolid, twisted-light-chiral-ms, condensed-matter-topology-fractionalization]
source_analysis: "raw/analyses/2026-10-03_arxiv-2609.38352_interferometric-readout-momentum-space-topology-photonic-circuit.md"
---

# Interferometric Readout of Momentum-Space Topology

**One-line summary:** A reprogrammable silicon chip simulates a lossy two-band lattice one wavevector at a time and reads a Zak phase (0 versus π) and a Chern number (0 versus 1) from four interference measurements. The invariants are the ones that were programmed in. PRL (2026), DOI 10.1103/xkht-64kc, arXiv:2609.38352.

## Key claims and results

- **Paper:** Stockholm–Singapore–Wuhan collaboration, arXiv:2609.38352v1 (29 Sept 2026), Physical Review Letters 2026, DOI 10.1103/xkht-64kc. Six-page main text. The supplemental material (dilation details, the phase-relation proof, calibration, how the exceptional-point contour is drawn) was not in the arXiv bundle and was not read. Hardware continues the group’s Klein-bottle chip (arXiv:2512.20273).
- There is no lattice on the chip. A mesh of tunable interferometers is reconfigured for each wavevector, time, and readout phase. The lossy 2×2 step is rescaled and embedded in a 4×4 unitary (Sz.-Nagy dilation). Two ancilla waveguides take the amplitude that “loss” removes. Four phase settings recover the complex coherence between the two sites. One SSH Zak phase is 100 configurations. One pump cycle is 2,500.
- Lossy Su–Schrieffer–Heeger chain, with loss twice the largest coupling, so the zone is overdamped and an exceptional point sits at zero momentum. Summing the measured phase across half the zone gives 1.02π (non-trivial) and −0.0015π (trivial). Across a coupling scan the plateaus average about 1.04π and −0.025π, and they jump at j₂/j₁ = 1. Near that point the coherence vanishes and the phase cannot be read. Neighbouring points overshoot by ~0.1–0.15π. For injection into the lossy site, the phase of the coherence copies the phase of the programmed coupling and does not depend on the loss. The Zak phase is therefore the Hermitian parent’s winding, which the paper states in the text.
- A closed loop around the coherence’s zero gives a winding q = +1 or −1 with the direction of travel. The paper distinguishes this from the half-integer vorticity of an exceptional point’s eigenvalues. On the main-text description, a circle around a zero winds by construction. The supplement may define the contour differently.
- Lossy Rice–Mele pump on a 25×25 grid in momentum and pump phase. A loop that encloses the gap closing is assigned Chern number 1. A loop that misses it is assigned 0. Those integers come from a **fitted** pump loop, not from integrating measured phases the way the Zak phase is summed. Fig. 4(f) is drawn as smooth lines. Fitted centres sit 0.805 and 0.175 from the gap-closing point, close to the nominal 0.8 and 0.2. Phase error on the maps is ~0.021π. An ideal-pipeline check recovers Chern numbers +1 and 0 with or without the loss. The line gap stays open.
- Readout time is a model-informed choice. In an ideal replay, an intermediate window (about t = 0.50 to 0.76 for the quoted SSH loss) **inverts** the Zak phase. The paper’s displayed window (t from 1 to 2) is safe. The paper calls it a “representative well-conditioned interval.”

## Physical intuition

Edge-state experiments see topology by its consequences, and they need a new chip for each point in a phase diagram. This experiment never builds the crystal. It evaluates one Fourier bin at a time, the way a spectrum analyzer steps a tone instead of lighting the whole band.

Loss is the usual enemy of a phase measurement: the amplitude dies and the phase becomes noise. Two moves dodge that, and neither is available in a physical lossy material. Rescaling boosts a tiny singular value before the mesh runs. And for light sent into the lossy site, the loss drops out of the phase entirely, so the reading copies the coupling’s winding. The integer you recover is the ordinary one. Loss shapes how hard the shot is. It does not create a new invariant here.

## Limitations and assumptions

- Methods demonstration. The Zak phase, Chern number, and winding are textbook targets that were programmed in. A wrong integer would have indicted the instrument, not discovered a phase.
- The Chern number assumes the Rice–Mele family. A chip error that the fit absorbs into a deformed loop could still produce the right integer. No fit uncertainty is given in the main text.
- The exceptional-point winding, as the main text describes it, does not isolate an exceptional-point property. Supplement unread.
- Rescaling hides absolute loss. The amplitude-suppression problem is solved for a simulator, not for a material that actually dissipates.
- Only two-band models (four modes). Larger meshes lose fidelity per unitary. The paper points at calibration models as the mitigation. A three-band point-gap winding, which would have no Hermitian parent, is the real next test and is not done.
- Single group. Phase error ~0.02–0.06π is comfortable against a separation of π, and tight near the gap closing where the signal vanishes.

## Connections

- A different photonic emulator (non-Abelian braids of modes, real lattices, edge-style consequences): [[nonabelian-photonic-braiding]]
- Other structured-light / polariton neighbors: [[photonic-supersolid]], [[twisted-light-chiral-ms]]
- Synthesis: [[condensed-matter-topology-fractionalization]] (Thread D, emulators)

## Open questions

- Can the same per-wavevector method read a point-gap winding or an exceptional-point charge that does not exist in the Hermitian parent?
- Can a Chern number be summed from measured phases without fitting the loop family?
- Can the safe readout time be chosen without already knowing the model?

## Source

- `raw/analyses/2026-10-03_arxiv-2609.38352_interferometric-readout-momentum-space-topology-photonic-circuit.md`
