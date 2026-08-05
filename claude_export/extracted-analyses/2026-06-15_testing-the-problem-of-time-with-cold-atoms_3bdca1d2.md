---
source: claude_export
conversation_uuid: 3bdca1d2-3717-40aa-bc8f-05a009f3d18a
title: "Testing the problem of time with cold atoms"
created_at: 2026-06-15T21:03:58.162130Z
updated_at: 2026-06-15T21:06:06.452911Z
tier: A
score: 22
n_messages: 2
---

# Testing the problem of time with cold atoms

## Human

Analyze this paper Publication details
Giovanni Barontini, Testing the problem of time with cold atoms, Physical Review Research (2026). DOI: 10.1103/1h9j-df4k

Journal information: Physical Review Research

## Assistant

v3.6.2

---

# 1. Punchy Title & One-Sentence Hook

**The Clock That Grew Inside the Universe**

A tabletop cloud of rubidium atoms — chilled to a hair above absolute zero, partitioned into a "bright" and "dark" side, and watched through hundreds of Big Bang–to–Big Crunch cycles — demonstrates that a meaningful, directional flow of time can be constructed from *nothing but internal entropy*, bypassing the need for any external clock.

---

# 2. Big-Picture Context

Time is physics' most embarrassing variable. Every equation of motion treats it as a freely given, external parameter — a smooth backdrop against which things happen. General relativity complicates this by making time coordinate-dependent, but still treats it as a geometric ingredient. Quantum gravity, however, breaks the deal entirely. The Wheeler-DeWitt equation — the leading attempt to write a quantum wave function for the entire universe — contains no time parameter at all. The total Hamiltonian (the energy operator) acting on the universal wave function gives zero, which means the equation admits no external handle with which to sequence physical changes. This is the "problem of time": by the most fundamental rules we have, the universe as a whole is timeless. Yet here we are, clearly experiencing time flowing. Something is missing.

The leading theoretical escape route is *relational time*: instead of time being written in from outside, it emerges from relationships between subsystems within the universe. One part of the universe acts as a clock; everything else is described relative to what that clock is doing. This idea goes back to Leibniz philosophically and to Page, Wootters, and Barbour physically, but it has remained stubbornly abstract because the universe is not a system you can put in a box and probe. The key question Barontini's paper asks is whether the dynamics of an observed sector of a closed system can be ordered using only internal degrees of freedom — no external lab clock allowed.

A parallel problem is the *arrow of time*. Every fundamental equation of physics is time-symmetric — run the movie backward and it still obeys the rules. Yet we never see entropy decreasing. In a Wheeler-DeWitt description, the total state is pure and fine-grained entropy is conserved. This appears incompatible with the observed growth of coarse-grained entropy unless one partitions the universe into subsystems, allowing entropy to flow between them even while the global total is fixed. The standard resolution is the "past hypothesis" — the universe started in an extremely low-entropy state — but this only pushes the question to initial conditions, not mechanism.

**Prior Belief Check:** This paper is not overturning any established physics. Relational time and the problem of time are well-known, theoretically mature frameworks, and the idea that entropy could serve as an internal clock is not new. What *is* new is bringing it into the laboratory and making it quantitative. Specialists will find this confirmatory and useful — a proof-of-concept that the concepts survive contact with a real physical system — but they will not be surprised that relational time can be defined. The surprise value is methodological, not conceptual.

**Replication & Convergence Note:** This result comes from a single group at the University of Birmingham; no independent replication exists yet. Independent confirmation would require a different cold-atom platform (e.g., lithium or potassium BEC, or a different trap geometry) constructing entropic time by the same method and recovering the same ordering fidelity. Until that happens, the demonstration is compelling but not yet field-certified.

---

# 3. Necessary Background Crash-Course

**Bose-Einstein Condensate (BEC):** When you cool a cloud of bosonic atoms (atoms with integer total spin) below a critical temperature — in this case rubidium-87 atoms at roughly 100 nanokelvins — they all fall into the same quantum ground state and behave as a single coherent quantum object, described by one wave function. Think of it as every CPU core in a massively parallel machine suddenly executing the exact same instruction stream simultaneously, so you can describe the whole chip with one program counter instead of thousands.

Breaks when: you push this to imply the atoms are "the same atom." They retain individual identities and positions; they just share a collective quantum state. The analogy also breaks for fermions (electrons, protons), which can never all occupy the same state.

**Wheeler-DeWitt Equation:** This is what you get when you apply quantum mechanics to all of spacetime simultaneously, treating geometry itself as the quantum variable. The result is a wave equation with no time parameter — the total energy of the universe is identically zero (kinetic + potential + gravitational all cancel). Think of it like a perfectly balanced transmission line with equal and opposite signals propagating simultaneously: the net current is zero, even though there is real activity inside.

Breaks when: you ask what "zero energy" means physically. A balanced transmission line carries no net power, but the quantum vacuum does carry real zero-point energy with measurable consequences. The WDW "zero" is a constraint on the *total*, not a statement that nothing is happening internally.

**Relational Time / Page-Wootters Mechanism:** Instead of a universal clock, you pick one subsystem and use its state as the "time variable." All other dynamics are then described relative to that subsystem's state — you are reading time off the correlations between subsystems, not from an external dial. Think of it as GPS: your position is determined by comparing signals from four satellites relative to each other; there is no "absolute" position dial anywhere in the system.

Breaks when: you need the "clock" subsystem to be perfectly distinguishable at all times. If the clock's states become degenerate or ambiguous (if two different "times" look the same to the clock), the whole scheme fails. In practice, clocks can run backward or stall.

**Coarse-Grained Entropy:** Fine-grained (von Neumann) entropy of an isolated pure quantum system never changes. Coarse-grained entropy *does* increase, because it ignores microscopic correlations you can't measure — it counts only the macroscopically distinguishable states. Think of your hard drive's file-system used space vs. the actual bit patterns: from the file system's perspective, writing a file increased disorder (used space) even though the total number of bits on disk is unchanged.

Breaks when: you try to use it to derive irreversibility from first principles. Coarse-graining is a choice about what you measure, not a law of physics — a different coarse-graining could give different entropy behavior.

**Central analogy for this paper:** GPS without absolute position.

---

# 4. Core Technical Explanation

**The Setup**

Barontini cools roughly 24,000 rubidium-87 ($^{87}$Rb) atoms to near absolute zero, creating a BEC in an optical dipole trap — laser beams whose intensity gradients push the atoms into a potential well, like a bowl of light. A second laser (675 nm) creates a thin barrier ~8 micrometers wide at the center of this bowl, acting as a dividing wall. The wall splits the system into two sectors:

- The **dark sector** (bottom half, unobserved) — the "rest of the universe," hidden behind the wall.
- The **bright sector** (top half, observed) — the "observable universe," where measurements happen.

The full system runs for about 100 milliseconds and is effectively closed: no measurable dissipation, no atom loss. The total Hamiltonian splits as:

$$\hat{H}_\text{total} = \hat{H}_\text{bright} + \hat{H}_\text{dark} + \hat{H}_\text{coupling}$$

**Symbol definitions:**
- $\hat{H}_\text{bright}$: energy operator for the observed (bright) sector
- $\hat{H}_\text{dark}$: energy operator for the unobserved (dark) sector
- $\hat{H}_\text{coupling}$: energy operator governing atom exchange across the barrier

**What this actually means:** Think of this as a CPU package split into two cache domains — L1/L2 (bright, observed) and L3/DRAM (dark, unobserved) — connected by a bus (the coupling). You can measure everything in L1/L2, but the DRAM state is hidden. The question is: can you reconstruct the timeline of what happened in L1/L2 using only information available inside L1/L2?

**The Dynamics: Big Bang to Big Crunch**

With the barrier at low height, the BEC sloshes back and forth across it. When atoms first flood into the bright sector, Barontini calls this the "Big Bang." When they drain back out, it's the "Big Crunch." The bright sector thus undergoes repeated expansion-recollapse cycles — a mini-Friedmann universe.

Using lab time (the external clock on the wall), you can describe this perfectly. But that's cheating — a true quantum gravity description has no external clock. So the experiment asks: can you reconstruct this history using *only* what's happening inside the bright sector?

**Building Entropic Time**

Barontini's key move: he defines a coarse-grained entropy for the bright sector by looking at how the atoms are distributed spatially — essentially, how "spread out" the density profile is — and calls this the **entropic time**. The atom population flowing into and out of the bright sector produces a non-Hermitian effective Hamiltonian for that sector (the energy operator gains an imaginary term representing gain and loss of atoms). This gain/loss is the engine that drives entropy exchange with the dark sector.

He then shows that this entropic time:
1. **Increases monotonically** from Big Bang to maximum expansion (entropy grows as the BEC spreads out).
2. **Decreases monotonically** from maximum expansion back to Big Crunch (entropy shrinks as atoms return to the dark sector).
3. **Disambiguates** the two halves of the cycle — expansion gets a different entropic time value than the equivalent state on the contraction side.

Critically, he derives an **effective Schrödinger equation** written in terms of entropic time instead of lab time, and shows it reproduces the measured bright-sector dynamics quantitatively. So entropic time is not just a label — it acts as a genuine dynamical parameter.

**Assumption Audit**

Watch: Reader likely assumes the BEC is a purely quantum object throughout. The paper actually says the bright-sector dynamics are described in the **mean-field (Gross-Pitaevskii) limit** — a classical field approximation valid when interactions are weak and atom numbers are large. The quantum nature of the many-body state is largely averaged out in the primary analysis.

Watch: Reader likely assumes the dark sector plays an active "clock" role analogous to the Page-Wootters mechanism. The paper actually constructs the clock variable from the **entropy exchange between sectors**, not from the quantum state of the dark sector directly. The dark sector functions more like a heat reservoir than a quantum clock.

Watch: Reader likely assumes that because the whole system is closed (pure quantum state, constant total energy), the entropy analysis is automatically consistent with quantum mechanics. The paper actually uses a **non-Hermitian effective Hamiltonian** for the bright sector — a standard open-systems trick — which implicitly treats the dark sector as an environment. This is formally correct but means the "closed universe" interpretation rests on a Born-Oppenheimer-like factorization that breaks down when quantum correlations between sectors become strong. The analog is profound: the paper's WDW connection relies on the sectors being weakly entangled, which is a regime the real universe need not be in.

---

# 5. What's Genuinely New or Clever

**New to the field, not just to the reader:**

The first clever trick is **making the problem of time *touchable*.** The WDW equation is purely theoretical — you can't run an experiment on the whole universe. Barontini finds a physical system (a partitioned BEC) whose effective Hamiltonian has the same mathematical structure as a minisuperspace WDW model. This isn't metaphor; it's a structural mapping. The bright sector's Gross-Pitaevskii Hamiltonian maps onto the minisuperspace variables with one sector acting as the scale factor and another as a matter field. That mapping is the paper's intellectual core.

The second trick is **using entropy flow as a monotonic clock hand.** Most relational-time proposals use a degree of freedom (a field value, a volume) that can oscillate and thus fail to act as a reliable clock (the "Janus problem" — the clock can't tell which way time is flowing). Barontini's entropic time is directional *by construction* within each half-cycle and, crucially, the experiment verifies this empirically: the entropic time robustly orders events across many repeated expansion-recollapse cycles, even though the underlying BEC dynamics are fully reversible. That's a nontrivial result — a reversible system nonetheless produces a locally monotonic internal time variable, exactly as WDW models predict.

---

# 6. Limitations & Open Questions

**The mean-field approximation hides genuine quantum gravity content.** The analysis uses Gross-Pitaevskii mean-field theory, which is a classical nonlinear wave equation — it erases inter-particle quantum correlations. The WDW framework is fundamentally about quantum geometry. The mapping is structural, but the quantum side of the analogy is thin.
(B) Contested — some researchers view mean-field BEC cosmology analogs as sufficiently rigorous for the purpose of testing relational time concepts; others argue the quantum many-body structure is essential and mean-field misses it. (analyst inference, with grounding in broader literature on BEC analog gravity)

**Single expansion-recollapse cycle degeneracy.** Entropic time is monotonic *within* each half-cycle but resets between cycles. Barontini shows the scheme works "across repeated cycles," but the arrow of time only points one direction within a single expansion or contraction, not globally. Over many cycles the system returns to its starting state, which is the thermodynamic equivalent of a perpetual motion machine — not physically wrong for a closed system, but it limits the cosmological interpretation.
(A) Consensus — this is explicitly acknowledged in the paper as a feature of the mini-universe setup. (paper, main text)

**The dark sector is truly dark — it cannot be verified.** The whole relational scheme requires the dark sector to behave correctly as an entropy reservoir. But by construction, you don't measure it. The consistency of the construction is inferred from the bright-sector behavior matching the model. This is epistemically analogous to the real cosmological horizon: you assume the unobserved sector behaves thermodynamically, but you can't check.
(C) Speculative — this is an analyst-level concern; the paper acknowledges using the dark sector as a reservoir but does not explicitly discuss what happens if that sector has non-thermal correlations. (analyst inference)

**No quantum fluctuations in the entropic time itself.** The entropic time is constructed from a macroscopic, classical entropy measure. A fully quantum treatment would require the entropy — and hence the time variable — to have quantum uncertainty. Page-Wootters and related approaches do handle this, but it requires the clock to be in a superposition of "time states." That regime is not explored here.
(B) Contested — whether quantum clock uncertainty is necessary for the analogy to be useful is actively debated in the quantum gravity literature. (broader literature)

**Single group, single atomic species, single geometry.** Robustness across different BEC species, trap geometries, or coupling strengths has not been demonstrated. The structural Hamiltonian mapping might not survive changes in the trap anisotropy or in the interaction parameter.
(C) Speculative — extrapolated from standard robustness concerns in analog gravity experiments; no specific literature evidence against it. (analyst inference)

---

# 7. Detailed Summary & Explanation

**The paper, section by section:**

Barontini opens by laying out the problem of time in the Wheeler-DeWitt framework and noting that the only robust temporal asymmetry in fundamental physics is the second law of thermodynamics — entropy increases. He reviews the theoretical landscape: relational time (where one subsystem's state serves as the clock), minisuperspace models (where the universe is simplified to a few degrees of freedom), and the connection between decoherence and entropy growth. He then notes that cold-atom platforms have become powerful cosmological simulators — prior work already demonstrated Hawking radiation analogs, Friedmann-Robertson-Walker universe emulation, and false vacuum decay in ultracold gases. His contribution is to target the problem of time specifically.

The experimental setup is a BEC of ~24,000 rubidium-87 atoms in an optical dipole trap, bisected by a thin laser-generated barrier. The barrier creates a "bright" (observable) sector and a "dark" (hidden) sector. By controlling the barrier height, Barontini controls how many atoms can cross between sectors. With the barrier low, the BEC sloshes back and forth in a ~100 millisecond cycle — expanding into the bright sector ("Big Bang") and retracting into the dark sector ("Big Crunch").

He then proposes replacing the external lab clock with an **entropic time** variable, built from the coarse-grained spatial entropy of the bright sector — essentially, how spread out the atomic density is. This entropy increases as the BEC expands and decreases as it contracts. Critically, it is always monotonic within a half-cycle, which means it can act as a one-way clock hand.

He writes down an effective Schrödinger equation using entropic time instead of lab time, derives it from the known Hamiltonian structure, and then compares its predictions against the actual experimental data. The match is quantitatively good. The entropic time scheme correctly orders all observed events across many expansion-recollapse cycles.

**Why the summary is framed this way:** The paper's core contribution is not a new theoretical idea — relational time is old. It is the *operationalization* of that idea in a controlled experiment that can be repeated, varied, and compared to theory. That's why the framing emphasizes the mapping between the BEC Hamiltonian and minisuperspace models, and the quantitative success of the entropic time Schrödinger equation. Those are the results that matter for the field. The "mini-universe" language is evocative but should be understood as an analog model, not a cosmological simulation in any direct sense.

**Where I'm least confident in this analysis:** The derivation of the effective Schrödinger equation parameterized by entropic time is the part where the plain-language translation most likely lost something real. The connection between the non-Hermitian open-system formalism and the Wheeler-DeWitt relational time construction involves mathematical steps that I have described structurally but not in full detail. A reader who wants to evaluate whether the mapping is truly rigorous — or whether it is a suggestive analogy dressed in formal notation — should go directly to the paper's equations in that section.

---

# 8. Three Crystallized Takeaways

1. **Time can be a derived quantity, not a given one** — this experiment is the first to demonstrate in a real physical system that a directional, usable flow of time can be extracted from nothing but the internal entropy of a closed system, with no external clock anywhere in the description.

2. **A bathtub of ultracold atoms is a testable universe** — the structural mapping between the BEC's Hamiltonian and the minisuperspace Wheeler-DeWitt equation is not metaphor; it gives quantum gravity theorists a real knob-turning laboratory where they can vary parameters and see relational-time constructions succeed or fail.

3. **Entropy's arrow of time is not just philosophical** — the fact that entropic time is monotonic within each half-cycle, in a system whose underlying dynamics are fully time-reversible, confirms experimentally that the second law's asymmetry is sufficient to generate a locally consistent arrow of time without any additional ingredients.

---

# 9. Shorter Summary

Hard ceiling: 350 words.

Barontini built a miniature analog universe from ~24,000 rubidium atoms cooled near absolute zero. A laser-generated barrier splits the atom cloud into an "observed" (bright) side and a "hidden" (dark) side. The atoms oscillate back and forth across this barrier in cycles of expansion — a Big Bang as they flood into the bright side — followed by collapse, a Big Crunch, as they drain back to the dark side. Each cycle lasts about 100 milliseconds. The whole system is closed: no dissipation, no energy leaking out.

The deep question the paper asks is: could you describe what happens in the bright side without ever consulting an external clock? In standard quantum gravity, the universe has no external clock — the Wheeler-DeWitt equation, which is quantum mechanics applied to all of spacetime, contains no time variable at all. One proposed fix is relational time: use the state of one part of the system as a clock, and describe everything else relative to that.

Barontini constructs an "entropic time" variable from the spatial spread of the atom cloud in the bright sector. As the cloud expands, this entropy grows; as it contracts, entropy shrinks. Within each half-cycle the entropy moves in one direction only, giving a natural arrow of time. He then derives a modified version of the Schrödinger equation — quantum mechanics' equation of motion — written in terms of this entropic time instead of lab time, and shows it reproduces the experimental data quantitatively.

The result matters for three reasons. First, it is the first controlled experimental test of relational time constructions, moving the idea out of pure theory. Second, the BEC's governing equation maps formally onto the simplified (minisuperspace) version of the Wheeler-DeWitt equation, so the experiment is a genuine structural analog of a quantum gravity scenario, not just a loose metaphor. Third, it demonstrates empirically that a fully time-reversible quantum system can nonetheless generate a consistent, directional internal time from entropy alone — exactly what quantum gravity theorists need if time is to emerge rather than be assumed.
