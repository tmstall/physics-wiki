---
tags: [synthesis, quantum-metrology, quantum-optics, foundations]
last_updated: 2026-08-01
status: synthesis
related_papers: [time-goes-quantum, quantum-proper-time-ion-clocks, negative-weak-valued-excitation-times, massive-tunneling-schrodinger-cats, collapse-models-clock-precision]
---

# Quantum Time Across Platforms

**One-line summary:** Three laboratory stories in this wiki treat “how long something took” as a quantum object — proper time as an operator on an ion, dwell time as a weak value on cold atoms, and interferometric phase time on massive spatial cats — plus a theoretical floor from spontaneous-collapse spacetime jitter — without needing the same Hamiltonian or even the same meaning of “time.”

## Why pull these together

Everyday physics uses one classical clock. Quantum experiments force a choice: *which* degree of freedom carries duration, and *how* you read it out. The wiki already holds three clean, non-overlapping answers. They do not reduce to one master theory. They do share a design pattern:

1. Split a quantum system into arms or branches that can accumulate different phases.
2. Let something that looks like “elapsed time” (proper time, group delay, free-evolution phase) act differently on those branches.
3. Recombine and read **contrast, weak value, or fringe** — not a classical stopwatch needle.

That pattern is the synthesis. The physics underneath stays platform-specific.

---

## Thread A — Proper time as an operator (ion clocks)

**Papers:** [[time-goes-quantum]], [[quantum-proper-time-ion-clocks]]  
**Concepts:** [[quantum-proper-time]], [[second-order-doppler-shift]], [[optical-ion-clocks]], [[motional-squeezing]], [[ramsey-interferometry]]

A trapped ion is a clock *and* a quantum harmonic oscillator. Special relativity says moving clocks run slow: the fractional frequency shift tracks kinetic energy over rest energy ([[second-order-doppler-shift]]). Classically you average \(\langle v^2\rangle\) and call it a systematic. Quantum mechanically the kinetic energy is an **operator** on the phonon ladder.

When the motion is a superposition of phonon numbers, the internal clock accumulates a **superposition of phases**. “How much proper time has ticked” becomes entangled with “which motional branch the ion is on.” That is [[quantum-proper-time]] in the lab.

**How you see it:**

| Motional state | Ramsey contrast signature |
| --- | --- |
| Thermal | Smooth, classical-looking dephasing |
| Coherent / engineered | Collapse–**revival** pattern ([[time-goes-quantum]]) |
| Squeezed | Dialable SODS shifts + visibility loss as entanglement witness ([[quantum-proper-time-ion-clocks]]) |

**Intuition:** GPS on a satellite that is simultaneously in two velocity states. Each branch has its own tick rate. Only a discrete, coherent spectrum lets the arms realign later — classical velocity noise never revives.

**Limits:** Flat-spacetime, special-relativistic. Full revivals may need hours of motional coherence. This is *not* yet gravitational proper-time superpositions (height twins, lattice-clock altitude experiments).

---

## Thread B — Duration as a weak value (transmitted photons)

**Paper:** [[negative-weak-valued-excitation-times]]  
**Concepts:** [[weak-values]], [[group-delay]], [[coherent-forward-scattering]]

Ask a different question: when a resonant photon pulse goes through a cold atomic cloud and is **transmitted**, how long did the atoms spend excited *because of that photon*?

Ordinary averages stay positive and causal. **Post-select** on transmission and measure excitation weakly via a cross-Kerr probe, and the conditional average — a [[weak-values|weak value]] — equals the optical [[group-delay]] \(\tau_g\). Near resonance, anomalous dispersion makes \(\tau_g\) **negative**. The experiment sees correspondingly negative weak-valued excitation times (down to roughly \(-0.8\,\tau_0\) in the reported case).

**Intuition:** The early peak of the transmitted pulse is sculpted by [[coherent-forward-scattering]] and interference. “Negative time” is not reverse causation; it is a conditional average over a rare outcome. Unconditional physics still respects causality.

**Limits:** Large error bars; media “time travel” framing is misleading; all results conditional on transmission.

---

## Thread C — Interferometric phase time on massive spatial cats

**Paper:** [[massive-tunneling-schrodinger-cats]]  
**Concepts:** [[collective-tunneling]], [[noon-states]], [[ramsey-interferometry]], [[optical-lattices]]

Here “time” is not an operator on a worldline. It is the **dark evolution** in a Ramsey sequence after a 7-atom Rb cluster tunnels into a spatial [[noon-states|NOON]] state: all left *and* all right (~608 u, ~320 nm scale). Phase \(\phi \propto n\cdot\Delta E\cdot T/\hbar\) winds \(n\) times faster than a single atom — Heisenberg-limited sensing of energy gradients.

**Intuition:** Duration enters as how long the cat is left to accumulate a which-path energy difference before recombination. The quantum object is the **spatial** superposition; time is the classical lab parameter that multiplies the enhanced phase. That still belongs in a “quantum duration” synthesis because the *useful* clock is the entangled cluster, not a classical timer alone.

**Limits:** Far below masses for gravitational entanglement tests; coherence limited by lattice noise and three-body loss.

---

## What is common (and what is not)

| | Ion proper time | Weak-valued dwell time | NOON Ramsey phase |
| --- | --- | --- | --- |
| **What “time” means** | Relativistic proper time along motional branches | Conditional atomic excitation duration | Lab free-evolution interval \(T\) |
| **Quantum object** | Clock–motion entanglement | Post-selected weak value | Path-entangled cluster |
| **Readout** | Ramsey contrast / visibility | Cross-Kerr phase integral | Population imbalance fringes |
| **Platform** | [[optical-ion-clocks]] | Cold ⁸⁷Rb MOT | Optical superlattice |
| **Needs gravity?** | No (SR only, so far) | No | No |

**Shared design pattern:** quantum interference + something that *acts like* duration differently on different amplitudes.

**Not shared:**

- Ion work promotes a **relativistic** quantity to an operator.
- Weak-value work promotes a **conditional average** outside the eigenvalue spectrum.
- NOON work keeps \(T\) classical but multiplies its effect with **entanglement**.

Do not collapse these into “time is quantized.” Prefer: **three operational definitions of duration in quantum experiments**, each tied to a measurable.

---

## Side thread — Collapse models as a theoretical time floor

**Paper:** [[collapse-models-clock-precision]]  
**Concepts:** [[spontaneous-collapse-models]], [[quantum-proper-time]]

If objective collapse (CSL / Diósi–Penrose) couples mass density to classical noise that one reads as Newtonian-potential jitter, general relativity turns that noise into a \(\sqrt{t}\) uncertainty on proper time. Standard parameters put the floor ~10⁻²⁸ s (CSL) after a year — many orders below optical clocks. This is **not** a fourth lab platform; it is a foundations bound that sits next to Thread A’s operational proper-time operator. Collapse models remain compatible with rock-solid timekeeping while linking the measurement problem to gravity and time.

---

## Cross-links and open synthesis questions

- [[ramsey-interferometry]] is the shared measurement language for Threads A and C (and metrology culture elsewhere: [[collective-superradiant-lasing]]).
- Cold-atom kinship: [[massive-tunneling-schrodinger-cats]] and [[negative-weak-valued-excitation-times]] share platform DNA, different questions.
- Path from Thread A toward gravitational proper-time superpositions remains open (altitude / lattice twins) — still far from the mass scales of Thread C’s quantum-gravity wish list.
- Foundations bound: [[spontaneous-collapse-models]] / [[collapse-models-clock-precision]] give a theoretical proper-time floor, not a near-term experimental program.

**Questions this synthesis raises:**

1. Is there a single information-theoretic account of “interaction time” that covers weak values *and* operator proper time?
2. Can ion-clock proper-time entanglement and spatial NOON cats ever sit in one experiment (motion + path)?
3. How should pedagogy talk about negative weak-valued times without feeding time-travel myths?
4. If collapse parameters were ever tightened by other experiments, would the clock-floor bound ever enter the same conversation as Thread A’s SODS systematics?

---

## Map of pages

| Role | Pages |
| --- | --- |
| Papers | [[time-goes-quantum]], [[quantum-proper-time-ion-clocks]], [[negative-weak-valued-excitation-times]], [[massive-tunneling-schrodinger-cats]], [[collapse-models-clock-precision]] |
| Core concepts | [[quantum-proper-time]], [[second-order-doppler-shift]], [[weak-values]], [[group-delay]], [[noon-states]], [[collective-tunneling]], [[ramsey-interferometry]], [[spontaneous-collapse-models]] |
| Platforms | [[optical-ion-clocks]], [[optical-lattices]] |

## Related synthesis

- Synthesis: [[measurement-problem-threads]] (foundations: measurement problem threads)


- [[amo-quantum-state-control]]
