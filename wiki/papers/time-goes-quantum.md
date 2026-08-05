---
tags: [papers, quantum-metrology, relativity, ion-clocks]
last_updated: 2026-07-31
status: analysis-ingest
related_papers: [quantum-proper-time-ion-clocks]
source_analysis: "raw/analyses/Time Goes Quantum.md; List2_Combined_Clean.md (Time Goes Quantum.md)"
---


# Time Goes Quantum: Proper Time Superpositions in Ion Clocks

**One-line summary:** A trapped ion’s internal clock can entangle with its own quantized motion via special-relativistic time dilation, producing Ramsey contrast collapse-and-revival patterns that fingerprint quantum proper time.

## Key claims and results

- Optical ion clocks couple two degrees of freedom: the narrow electronic “clock” transition and the quantized vibration in the trap (phonon / Fock states).
- Special relativity links them: different motional energies mean different kinetic energies, hence different second-order Doppler (time-dilation) rates.
- When motion is a **superposition** of phonon numbers, the clock accumulates a **superposition of phases** — entanglement between “how much time has ticked” and “which motional branch the ion is on.”
- Ramsey fringe **contrast** is the characteristic function of the phonon-number distribution. Thermal motion gives featureless decay; coherent or engineered motional states produce **collapse and revival** at a computable revival time.

## Physical intuition

Think of a GPS satellite clock running slightly slow because it is moving — except the satellite is *simultaneously* in two velocity states. Each branch of the superposition has its own proper-time rate. Over a dark evolution time, the two clock phases drift apart and later re-align if the energy spectrum is discrete and coherent. Classical velocity noise never revives; only a quantum motional spectrum with fixed energy spacings does.

Engineering analogy: cache lines that accumulate different cycle counts on different cores. When you try to merge, coherence is lost until the cycle counters wrap into alignment again.

## Limitations and assumptions

- The effect is **special-relativistic** (flat spacetime, kinetic time dilation), not a full quantum-gravity test. Gravity / curved spacetime is not required.
- Revival times for flagship ions (e.g. Al⁺) can be **hours to days** with typical trap frequencies — far beyond current motional coherence (heating and decoherence dominate on much shorter scales).
- Full revival is therefore a near-term stretch; partial, non-thermal contrast structure is the realistic near-term target.
- The ingested analyses were reconstructed / multi-source without full PDF verification; treat numerical estimates as provisional until checked against the paper.
- **Ingest note (List2 batch 8):** List2 re-analyzes the same Sorci / Foo / Leibfried / Sanner / Pikovski proper-time program already filed from the standalone analysis—no second paper page.

## Connections

- Tightly related to [[quantum-proper-time-ion-clocks]], which pushes the same physics toward **squeezed motion** and named SODS corrections (vSODS, sqSODS, qSODS).
- Builds on [[quantum-proper-time]], [[second-order-doppler-shift]], and [[ramsey-interferometry]].
- Collapse-model *theoretical* time floor (far below lab): [[collapse-models-clock-precision]], [[spontaneous-collapse-models]].
- Experimental platform: [[optical-ion-clocks]] / Paul-trap metrology (NIST lineage in the analysis).
- Contrast with spatial cat superpositions in [[massive-tunneling-schrodinger-cats]] (position, not proper time).
- Metrology cousin (active clocks, vibration tolerance): [[collective-superradiant-lasing]].
- Synthesis: [[quantum-time-across-platforms]]

## Open questions

- Can cryogenic traps and ground-state cooling make partial revival structure visible before full revival time?
- How do multi-ion logic clocks and shared motional modes change the proper-time entanglement story?
- What is the cleanest path from this special-relativistic effect to gravitational proper-time superpositions (altitude / lattice-clock twin experiments)?

- Synthesis: [[measurement-problem-threads]] (foundations: measurement problem threads)

## Source

- Analysis: `raw/analyses/Time Goes Quantum.md` (authors discussed: Sorci, Foo, Leibfried, Sanner, Pikovski; connected to Pikovski et al. Nature Physics 2015 gravitational decoherence program).
