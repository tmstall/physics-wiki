---
source: spacex_export
conversation_id: 0966092c-1c1f-45be-987f-8016e1b777f3
title: "Cold Atoms Measure Time via Entropy"
created_at: 2026-06-13T03:51:33.413879Z
updated_at: 2026-06-13T03:52:36.033756Z
n_responses: 2
platform: grok/xAI
pilot: false
---

# Cold Atoms Measure Time via Entropy

## Human

analyze this paper: Physical Review Research

* Recent

* Subjects

* Accepted

* Collections

* Authors

* Referees

* Editorial Policies

* About

* Scope

* Editorial Team

* RSS

- Letter

- Open Access

Testing the problem of time with cold atoms
Giovanni Barontini*
 

*  

 

*  

PDFShare

*  

*  

*  

*  

*  

*  

Phys. Rev. Research 8, L022047 – Published 11 June, 2026
DOI: [url]

## Assistant

**Analyzing v3.6.1**

**1. Punchy Title & One-Sentence Hook**  
Cold Atoms Forge an Internal Clock from Entropy Leakage in a Tabletop Wheeler-DeWitt Universe  

In a time-independent Bose-Einstein condensate deliberately split by a tunable optical barrier, researchers extract a monotonic entropic time from entropy flow between visible and hidden sectors; that single internal variable both orders multiple expansion-recollapse cycles and lets them write an effective Schrödinger equation whose predictions match the measured bright-sector dynamics.

**2. Big-Picture Context**  

The problem of time in canonical quantum gravity is stark: the Wheeler-DeWitt equation \(\hat{H}\Psi=0\) annihilates the wave function of the universe because the total Hamiltonian constraint contains no external time parameter. Classical general relativity and ordinary quantum mechanics both rely on an external clock; quantum gravity removes it. At the same time, the second law supplies the only robust arrow we actually observe. Relational-time proposals try to solve both issues by letting internal degrees of freedom act as clocks and by letting entropy flow between subsystems generate an arrow even when the global state remains pure.

Before this experiment those ideas lived in minisuperspace models, numerical simulations, and thought experiments. No laboratory system had quantitatively tested whether an entropy-derived internal time could actually order real quantum dynamics and recover a Schrödinger description across repeated cycles. Cold-atom platforms had already emulated analogue black holes, expanding universes, and false-vacuum decay; this work adds a controlled test of the foundational time problem itself.

The authors turn a well-isolated \(^{87}\)Rb BEC into a self-contained mini-universe analogue whose global Hamiltonian is strictly time-independent, yet whose visible sector exhibits emergent time and an arrow once entropy exchange with the hidden sector is allowed.

**Prior Belief Check**  
The results align with relational-time and entropic-arrow constructions discussed in the Wheeler-DeWitt literature; they do not contradict mainstream expectations in that subfield. The outcome is genuinely surprising to experts because a thermodynamic variable built from coarse-grained entropy is shown to function as a sufficiently accurate clock to reproduce unitary many-body evolution in a real quantum simulator across multiple “cosmic” cycles—an experimental closure of a loop that had remained conjectural.

**3. Necessary Background Crash-Course**  

**The Problem of Time in the Wheeler-DeWitt Equation**  
Analogy: Picture a perfectly sealed, frictionless mechanical clock whose every gear is locked to every other gear so that the total energy of the entire mechanism is exactly zero; from outside, the hands never move, yet relative motions still occur inside. The Wheeler-DeWitt constraint plays the same role for the universe: the total Hamiltonian annihilates the wave function, removing any external time parameter while internal degrees of freedom can still change relative to one another.  

Breaks when: you treat the global state as the only reality; real observers are always entangled with some subsystem, so relational time emerges once a clock variable is designated.

**Relational Time via Internal Degrees of Freedom**  
Analogy: In a closed economy with fixed total money, one firm’s cash balance can serve as the market’s clock if you watch how every other transaction correlates with that single ledger; “time” is whichever account you choose to read the books against. In minisuperspace cosmology one promotes a scalar field or scale factor to play this role.  

Breaks when: the chosen variable reverses (as center-of-mass position does in a recollapsing system); a non-monotonic clock cannot order the entire history, which is why the authors integrate entropy production instead.

**Entropic Arrow from Subsystem Partitioning**  
Analogy: Two rooms connected by a small door inside an otherwise sealed building; total molecules are fixed and the global state is pure, but an observer who sees only one room records a local entropy that grows whenever molecules cross the threshold in either direction. The arrow appears locally without violating global reversibility.  

Breaks when: coupling becomes so strong that the rooms fully thermalize; local entropy stops changing and the clock freezes—the exact “heat death” regime the experiment also observes when the barrier is fully open.

**4. Core Technical Explanation**  

The team prepares a BEC of roughly \(2.4 \times 10^4\) \(^{87}\)Rb atoms in a harmonic trap (\(\omega_x \approx 2\pi \times 25\) Hz) and inserts a thin optical barrier at \(x=0\) whose height \(V\) they can dial from zero to full coupling. The global Hamiltonian remains time-independent and conservative; the only “leak” is controlled atom exchange across the barrier. Absorption images every 2 ms give the bright-sector atom number \(N(\phi)\), center-of-mass coordinate \(\phi = X\), and RMS width \(\Sigma\).

They define a coarse-grained entropy \(S\) of the bright sector (essentially proportional to \(N\) because phase-space density per atom stays roughly constant). The entropic time is then constructed as
\[
\tau(\lambda) = \frac{\sigma}{k_B} \int_{\lambda} \left| \frac{dS}{d\phi} \right| d\phi
\]
along the observed trajectory. Because the integrand is an absolute value, \(\tau\) advances monotonically whenever entropy flows across the barrier, automatically supplying both a clock and an arrow.

When bright-sector observables are replotted versus this \(\tau\) rather than lab time, the expansion-recollapse trajectories collapse onto smooth, repeatable curves even though the cloud spends long intervals hidden in the dark sector. For low barrier height the motion remains cyclic; for high barrier height the system drifts toward a stationary state and \(\tau\) eventually stalls.

They start from the effective bright-sector dynamics (Gross-Pitaevskii with a small non-Hermitian term from atom exchange) and reparameterize the evolution operator by \(d\tau\) instead of lab time, obtaining an effective Schrödinger equation whose numerical solutions reproduce the measured density evolution \(N(\tau)|\psi(\tau,a)|^2\) across multiple cycles.

**Assumption Audit**  
Watch: Reader may assume the internal time \(\tau\) simply replaces lab time inside the ordinary Schrödinger equation \(i\hbar\partial_t\psi = H\psi\). The paper actually performs a non-local, state-dependent reparameterization that folds the entropy-flow rate into the generator; ordinary Schrödinger evolution is recovered only in the weak-coupling, monotonic-clock limit.  

Watch: Reader may assume the mini-universe is fully closed like a cosmological model. The paper deliberately keeps a tunable external barrier that allows controlled entropy exchange while conserving global atom number and energy; isolation is excellent on experimental timescales but engineered rather than fundamental.

**5. What's Genuinely New or Clever**  

The decisive trick is converting a sign-indefinite relational clock (\(\phi\) oscillates and reverses) into a strictly monotonic entropic time by integrating absolute entropy production. That single construction simultaneously solves the ordering problem and supplies the thermodynamic arrow without any external drive.  

They close the loop quantitatively: the same internal time not only orders events but, when inserted into a derived effective Schrödinger equation, reproduces the actual measured many-body dynamics. That direct experimental validation of a relational/entropic time construction inside a controllable quantum simulator is new to the field.

**6. Limitations & Open Questions**  

The mean-field Gross-Pitaevskii treatment plus one-dimensional effective description can miss genuine many-body entanglement and number fluctuations near the barrier. (A) Consensus — this is a standard limitation acknowledged for GPE dynamics involving strong depletion or fragmentation.  

The partitioning barrier is imposed by laser light rather than emerging dynamically from the degrees of freedom themselves; a fully self-contained cosmological analogue would require the split to arise internally. (B) Contested — analogue-gravity practitioners disagree on how much external scaffolding is acceptable before the analogy breaks.  

Whether the entropic-time construction survives coupling to genuine quantum fields or in regimes where relativistic or Planck-scale effects matter is unexplored; the present non-relativistic BEC is many orders of magnitude removed from quantum-gravity phenomenology. (C) Speculative — the paper makes no such claim; any extrapolation is an assessment that requires independent verification.

**7. Three Crystallized Takeaways**  

1. A carefully partitioned, strictly time-independent quantum many-body system can generate its own monotonic internal clock purely from entropy exchange between observed and hidden sectors.  

2. That entropic clock is accurate enough to let researchers derive and experimentally verify an effective Schrödinger equation for the visible sector across repeated expansion-recollapse cycles.  

3. Cold-atom BECs now serve as quantitative tabletop laboratories for testing relational-time and entropic-arrow ideas that previously existed only in quantum-gravity theory papers and numerical minisuperspace simulations.

**8. Detailed Summary & Explanation**  

The experiment realizes a miniature analogue of a closed universe inside a harmonic trap containing a \(^{87}\)Rb BEC. A thin optical barrier splits the cloud into a visible bright sector and a hidden dark sector. Atoms slowly cross the barrier, carrying entropy with them. By recording only the bright sector’s atom number, center-of-mass position, and width, the team constructs a cumulative entropic time \(\tau\) that advances solely when entropy flows across the barrier. Replotting the bright-sector breathing motion against this internal \(\tau\) yields smooth, repeatable trajectories through multiple “big bang / big crunch” cycles even though the cloud is invisible for long intervals in lab time. Finally they show that an effective Schrödinger equation written in the variable \(\tau\) reproduces the measured density evolution of the bright sector. The construction deliberately mirrors Wheeler-DeWitt relational-time proposals: the global Hamiltonian constraint is satisfied (total \(H\) is time-independent), yet an internal observer experiences emergent time and an arrow set by thermodynamic irreversibility.

Where I'm least confident in this analysis: the precise mapping between the experimental Gross-Pitaevskii effective Hamiltonian and a rigorously quantized Wheeler-DeWitt constraint; the paper uses a physically motivated analogy rather than a formal derivation from a constrained Hamiltonian system, so some interpretive steps rest on heuristic correspondence.

**9. Shorter Summary**  

Physicists split a Bose-Einstein condensate with an optical barrier and watched only one side. By tracking how entropy leaked across the barrier they built an internal clock that ordered the visible cloud’s expansion and recollapse through many cycles. That same clock let them write an effective Schrödinger equation whose predictions matched the actual quantum evolution seen in the lab. The work supplies the first direct experimental evidence that relational time constructed from entropy exchange can function quantitatively in a real, controllable many-body system, giving a concrete platform for testing foundational ideas about time in quantum cosmology.
