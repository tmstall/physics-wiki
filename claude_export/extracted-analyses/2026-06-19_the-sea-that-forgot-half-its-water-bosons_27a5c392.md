---
source: claude_export
conversation_uuid: 27a5c392-9f87-44f7-9c5e-b13973725796
title: "The Sea That Forgot Half Its Water: Bosons"
created_at: 2026-06-19T02:16:50.592379Z
updated_at: 2026-06-19T07:32:41.354939Z
tier: A
score: 269
n_messages: 2
---

# The Sea That Forgot Half Its Water: Bosons

## Human

analyze this paper

## Assistant

Let me fetch the full paper before beginning the analysis.

Now I have enough to give a thorough analysis. Let me write the full v3.6.3 framework response.

---

**v3.6.3**

---

## Section 1 — Punchy Title & One-Sentence Hook

**The Sea That Forgot Half Its Water: Bosons Driven Into a New Kind of Critical State**

By cycling the interactions of a 1D Bose gas from strongly repulsive through strongly attractive and back, physicists have conjured a quantum state so exotic it has correlations that no existing theory of one-dimensional matter can describe — not just quantitatively, but structurally.

---

## Section 2 — Big-Picture Context

One-dimensional quantum physics occupies a special place in condensed matter because dimensionality profoundly changes what matter can do. In one dimension you can't go around another particle — every exchange involves a collision — and that unavoidable scattering fuses statistics and interactions in a way that has no higher-dimensional equivalent. The textbook result is the Tomonaga-Luttinger liquid (TLL): a universal theory that says virtually any 1D quantum system at low temperature, regardless of the microscopic details, flows toward the same long-distance behavior — power-law decaying correlations and characteristic spatial oscillations called Friedel oscillations. The TLL is the "Fermi liquid" of 1D, and it has dominated the field for decades.

The TLL's power comes from the emergence of an effective Fermi surface even in systems made of bosons. Strongly repulsive 1D bosons "fermionize" via the Tonks-Girardeau (TG) effect: they can't overlap, so they behave identically to free spinless fermions. That fermionized state has a sharp Fermi surface in momentum space, and the TLL framework extrapolates from there — the Fermi surface shape encodes all the long-distance physics. What nobody had previously managed to do was modify the nature of that underlying Fermi sea itself, which would crack open an entirely new family of critical behavior lying beyond the TLL.

This paper asks: what if, instead of the usual Fermi sea with occupancy 1 per state up to some momentum and 0 beyond, you could engineer a state with occupancy 1/ℓ per state spread over ℓ times the usual momentum range — same number of particles, same total "weight," but a fundamentally different Fermi surface structure? The authors show theoretically that cyclic sweeps of the interaction strength, shuttling the gas between strongly repulsive and strongly attractive regimes, do exactly that. Each complete cycle "clicks" the Fermi sea into the next fractional occupancy level. The resulting states have correlation functions that are genuinely incompatible with any conventional TLL — they don't just have different Luttinger parameters, they have different functional forms.

**Prior Belief Check:** This result is genuinely surprising to experts, and the surprise is two-layered. First, that these specific excited states survive at all — integrable systems have enormous numbers of conserved quantities that could have scrambled the state into something thermal. Second, and more importantly, that the correlation functions break TLL universality in a structural way. Most workers in 1D quantum physics would have bet that any low-energy behavior would eventually flow to some TLL fixed point with renormalized parameters. The claim here is that these states sit at a different class of fixed point entirely — not just a TLL with unusual Luttinger parameter, but something categorically distinct. That's a significant claim, and the community will scrutinize it carefully.

**Replication & Convergence Note:** This result comes from a single group (the Innsbruck Nägerl lab for experiment, Bastianello for theory), with the experimental companion paper (arXiv:2602.17657) still under review as of the PRL publication date. Independent confirmation from other cold-atom platforms would substantially strengthen the claim; what that would look like concretely is another group preparing an α = 2 fractional Fermi sea in, say, a $^{87}$Rb or $^{39}$K system using the same holonomy protocol and observing matching Friedel oscillations.

---

## Section 3 — Necessary Background Crash-Course

**The Lieb-Liniger (LL) Model**
The LL model is the exact quantum description of bosons confined to one dimension interacting via contact (delta-function) forces. The interaction strength is a single number, the coupling constant g₁D, which can be positive (repulsive) or negative (attractive). The model is exactly solvable via Bethe Ansatz — one of the very few interacting quantum field theories where you can write down exact eigenvalues.

Analogy: Think of the LL model as a pinball machine with exactly one lane. The balls (atoms) can only hit each other head-on, and you can adjust a spring constant that determines how hard the collisions are. Positive spring → they bounce apart hard; negative spring → they briefly stick.

Breaks when: you push this to ask about what happens at g₁D = ±∞. In the pinball analogy, infinite repulsion would just block passage, but in the quantum model it maps to the exactly-solvable Tonks-Girardeau fermionized state, a non-trivial mapping that has no pinball equivalent.

**Tonks-Girardeau (TG) and Super-Tonks-Girardeau (sTG) States**
At g₁D → +∞ (infinite repulsion), 1D bosons behave exactly like free spinless fermions — they can't pass through each other, so they fill energy levels just as fermions do. This is the TG gas. The mapping to free fermions is exact. The sTG state is the metastable excited state you land in when you suddenly switch from g₁D = +∞ to g₁D = −∞: the system "remembers" its fermionic node structure but is now in an attractive regime where binding would otherwise win, and integrability saves it.

Analogy: The TG gas is like a corridor so narrow that people (bosons) can't pass each other — they end up queuing in single file and behaving statistically like workers who each insist on personal space (fermions). The sTG state is like those same people suddenly discovering the hallway is magnetic and people attract each other, but they're moving so fast they haven't had time to clump.

Breaks when: you extend this to dynamics. The "personal space" fermion analogy makes you think the TG state is static, but the actual TG gas is a dynamic quantum system with specific phonon-like excitations; the corridor analogy has no equivalent of those.

**Tomonaga-Luttinger Liquid (TLL)**
For any interacting 1D quantum system at low temperature, regardless of microscopic details, the long-distance correlations are governed by two numbers: the sound velocity v and the Luttinger parameter K. All correlation functions decay as power laws with exponents set by K, and all exhibit Friedel oscillations at twice the Fermi momentum. This universality is the TLL's power — and its limitation.

Analogy: The TLL is like an RG-flow cache hierarchy for 1D physics. No matter what program (microscopic model) you start with, the long-distance (low-frequency) behavior gets folded into just two cache lines: v and K. Once those are filled, all observables read from those two values. You can't distinguish cache sources; you only see the output.

Breaks when: you encounter states whose "program" is so unusual that it doesn't flow to any single two-parameter fixed point — which is exactly what this paper claims the fractional Fermi seas do. The RG flow goes somewhere else entirely.

**Haldane's Generalized Exclusion Statistics (GES)**
Haldane generalized Pauli exclusion: instead of each added fermion blocking exactly 1 state (α = 1), you can define particles with a parameter α that blocks α states per added particle. Bosons have α = 0 (adding a boson doesn't block any state). Anyons have 0 < α < 1. Fermions have α = 1. The fractional Fermi seas in this paper correspond to α = ℓ > 1, which the authors call "super-fermionic" — each particle claims ℓ slots.

Analogy: Imagine energy states as parking spaces in a garage. Normal fermions are aggressive parkers who occupy one space and block the adjacent space (α = 1). Super-fermionic particles park in one space but their car is ℓ spaces wide, blocking ℓ − 1 neighbors too.

Breaks when: you ask what the physical mechanism of "blocking" is. In the parking analogy it's a physical car; in GES it's an emergent statistical effect of many-body correlations, not a real physical exclusion between individual particles. The particles themselves are bosons — the "super-fermionic" behavior is a collective property.

**Quantum Holonomy**
When you move a quantum system around a closed loop in parameter space (here: g₁D sweeping from 0 → +∞ → −∞ → 0), the system can return to the same Hamiltonian but in a different quantum state. This is a holonomy — the parameter-space loop accumulated a non-trivial geometric effect on the quantum state, analogous to how parallel-transporting a vector around a curved surface rotates it.

Analogy: Walk once around a Möbius strip holding a compass pointing "forward." When you return to your starting position, your compass points backward. You're back where you started geographically, but something has flipped. Each interaction cycle flips the quantum state up by one rung on the ladder of fractional Fermi seas.

Breaks when: you push the rotation/flip analogy to imply the state is periodic. After enough cycles the fractional sea occupancy 1/ℓ gets smaller and smaller — the state doesn't return to its starting point; it climbs a ladder.

**Friedel Oscillations**
In any system with a sharp Fermi surface (a hard edge in momentum-space occupancy), the one-body correlation function — which measures how correlated two particles are as a function of their separation — develops spatial oscillations at a wavelength set by the Fermi momentum. These are Friedel oscillations (FO). They're the spatial echo of the sharp Fermi edge, a quantum "ringing" that persists at arbitrarily long distances (though decaying in amplitude).

Analogy: Drop a stone into still water precisely at the edge of a dock. The dock reflects waves at a specific frequency, and you see ripples radiating outward at that frequency superimposed on the usual circular spreading. The dock edge is the Fermi surface; the ripples at the characteristic frequency are Friedel oscillations.

Breaks when: the analogy suggests the ripples are classical. Quantum Friedel oscillations are encoded in the off-diagonal density matrix — they're about quantum coherence between spatially separated points, not a density modulation you can see with your eyes (though in atomic systems you can image it indirectly).

**Central analogy for this paper:** Holonomy as a quantum gear-shift.

---

## Section 4 — Core Technical Explanation

**The Setup: The Lieb-Liniger model and its interaction cycle**

The authors start from the LL model — the exactly-solvable 1D Bose gas. The key lever is the coupling constant g₁D, which in the Innsbruck Cs experiment is tunable via magnetic-field-controlled Feshbach resonances combined with a confinement-induced resonance (CIR). This gives access to g₁D anywhere from 0 to +∞ to −∞ and back to 0, tracing a topological loop in the space of coupling constants.

A single interaction cycle consists of: starting at g₁D = 0 (non-interacting), ramping slowly to g₁D = +∞ (Tonks-Girardeau), jumping rapidly across the resonance to g₁D = −∞ (super-Tonks-Girardeau), ramping slowly back through g₁D = 0 from the attractive side, then jumping back to the starting point. Each complete cycle increments the charge parameter ℓ by 2. After ℓ/2 cycles, the gas sits at a fractional Fermi sea with occupancy 1/ℓ per momentum state.

**Why does the state change?**

This is the geometric heart of the paper. The LL model is exactly solvable, meaning the many-body quantum state can be labeled by a set of quasi-momenta (rapidities) via the Bethe Ansatz. When you adiabatically ramp g₁D from 0 to +∞, the rapidly evolve continuously into the TG fermionized state. When you then jump from g₁D = +∞ to g₁D = −∞, the jump is too fast for the state to follow, so you land in the sTG metastable state (the same fermionic node structure, but now in the attractive regime). When you ramp back from −∞ to 0, the state evolves again, but via the attractive branch — and here's the key: the two paths (repulsive branch and attractive branch) are not the same in Hilbert space. The roundtrip around the resonance is a geometric loop that applies a non-trivial transformation to the quasi-momentum distribution. Specifically, it stretches the Fermi surface by a factor of 2 and halves the occupancy per state, producing α = 2. Each subsequent cycle does it again: α = 4, then 6, and so on.

This is the "quantum holonomy" of the Lieb-Liniger model — a fact established in earlier theoretical work that this paper builds directly upon and extends.

**What state do you end up in?**

After ℓ cycles, the gas is in a highly excited, non-thermal many-body state. Its quasi-momentum distribution is a flat box of occupancy 1/ℓ stretching from −ℓ·k_F to +ℓ·k_F, where k_F is the Fermi momentum of the underlying TG state. In momentum space: same total area (same number of particles), but ℓ times wider and ℓ times shorter. This state is stabilized entirely by integrability — the enormous number of conserved quantities in the LL model prevent thermalization (the state can't collapse into a thermal cloud), so the system is frozen into a Generalized Gibbs Ensemble (GGE) rather than a thermal Gibbs state.

**What are the correlation functions doing?**

This is the theoretically new core. For a conventional TLL built on a normal Fermi sea (sharp step from 1 to 0 at k_F), the one-body correlation function decays as a power law times oscillating terms at the single Fermi momentum. The critical exponents are universally set by the Luttinger parameter K.

For the fractional Fermi sea (occupancy 1/ℓ up to ℓ·k_F), the paper shows that the correlation functions still decay as power laws and still oscillate (Friedel oscillations, now at the stretched Fermi momentum ℓ·k_F), but the exponents are different — and crucially, they can't be reproduced by any TLL with any choice of K. The oscillation structure is richer: there are multiple Fermi-surface harmonic contributions, each with its own exponent, and they don't fit into the two-parameter TLL framework. The paper computes these using GHD, which extends Euler-level hydrodynamics to integrable systems by treating the full distribution of quasi-particles as a continuous fluid. GHD correctly accounts for the spatially inhomogeneous trap, the finite-temperature effects, and the dynamics of the interaction ramps.

The smoking gun is the first-order correlation function G^(1)(x) going negative — it crosses zero and shows clear minima at the ℓ-stretched Friedel wavelength. A normal Bose gas ground state never has a negative G^(1)(x).

**Assumption Audit**

Watch: Reader likely assumes "out of equilibrium" means the state is hot, disordered, and decaying. The paper actually says the state is highly excited but highly ordered and indefinitely stable (in an ideal integrable system), protected from thermalization by conserved quantities. The energy is high; the entropy production rate is zero.

Watch: Reader likely assumes the TLL description fails here because the system is out of equilibrium, i.e., the TLL simply doesn't apply to non-equilibrium situations. The paper actually says the TLL fails not because of non-equilibrium dynamics but because the underlying Fermi sea itself has a different shape — the fractional Fermi sea is a fixed point of the long-distance behavior, just not a TLL fixed point. At long distances the system looks critical, but with exponents no TLL can produce.

Watch: Reader likely assumes the Friedel oscillations in these states look qualitatively similar to TLL Friedel oscillations, just at a different wavelength. The paper actually shows they have quantitatively different power-law envelopes — the decay exponent changes with ℓ — and that multiple harmonics contribute with different exponents, producing a multi-component oscillation structure that is qualitatively richer than anything TLL predicts. The stretched wavelength is the easy part to understand; the multi-exponent structure is the deeper novelty.

---

## Section 5 — What's Genuinely New or Clever

**1. Non-equilibrium criticality beyond TLL via quantum holonomy**

The genuinely field-moving insight is that a topological loop in coupling-constant space acts as a gear-shift for the universality class of a quantum critical system. The interaction cycle doesn't just heat the gas or create a transient excited state — it clicks the system into a new fixed point of the long-distance physics that lies outside the TLL universality class. That's new to the field. The Lieb-Liniger holonomy was known; the identification that the resulting states realize a categorically new critical phase with GES-α correlation exponents is what this paper establishes.

**2. Using GHD to compute non-equilibrium critical correlators**

Generalized hydrodynamics has been a rapidly developing toolbox for integrable systems, mainly applied to transport and density evolution. This paper pushes GHD into the territory of correlation functions — specifically, computing the one-body correlator for highly excited non-equilibrium states with non-standard Fermi surfaces — and compares directly to experiment. The match to the Innsbruck Cs data (including the negative-going G^(1)(x) and its Bessel-function envelope) is the strongest direct experimental test of GHD as a predictor of correlation structure, not just density profiles. New to the field.

---

## Section 6 — Limitations & Open Questions

**1. Stability is integrability-protected, but all real systems break integrability.**
Three-body losses, transverse mode mixing, and longitudinal trapping all weakly break the LL model's exact integrability. In the experiment the sTG lifetime is ~5 seconds, which is long enough to observe the state but short compared to any proposed device application. (A) Consensus — explicitly acknowledged in the experimental companion paper and standard in the field; the lifetime question is the known bottleneck for all near-integrable physics. (paper §sTG lifetime measurement; broader literature)

**2. Only α = 2 and α = 4 are experimentally confirmed; the hierarchy to higher ℓ is extrapolated.**
Each cycle introduces accumulated imperfections and atom loss; achieving ℓ = 6 or 8 with fidelity is not demonstrated. The claim that the pattern continues indefinitely is theoretically clear from the Bethe Ansatz structure, but experimental verification at higher ℓ is missing. (B) Contested — the theoretical argument is solid, so some researchers would not call this a true limitation; others would note that the interesting physics (multi-exponent criticality becoming richer) is precisely where experimental confirmation is most needed. (analyst inference)

**3. The "new critical phase" claim requires a proper RG analysis.**
The paper shows correlation functions with non-TLL exponents and argues this constitutes a novel critical phase beyond TLL. But a complete renormalization group analysis showing that this is a stable fixed point (not a transient or a crossover) is not presented in the Letter format. (C) Speculative — the authors are confident based on the GHD computation and the GES mapping, but without a full RG treatment a careful theorist could argue the system is flowing through a complicated crossover rather than sitting at a genuine new fixed point. Independently verifying this would require a conformal field theory analysis or numerical renormalization of the fractional Fermi sea correlators. (analyst inference)

**4. The connection to Haldane's GES is an analogy, not a derivation.**
The paper frames the fractional Fermi seas as implementing GES with α = ℓ. But GES was defined for equilibrium systems; these states are non-equilibrium GGEs. The paper argues the momentum distribution matches the GES prediction and the correlation functions carry GES-like signatures, but a rigorous derivation of GES from the Lieb-Liniger GGE is not provided. (B) Contested — this is a point of genuine debate in the integrable systems community. Some researchers would say the mapping is well-established at the level of the Bethe Ansatz TBA equations; others want a cleaner derivation. (broader literature)

**5. The experiment is conducted on ~7,000 non-uniform 1D tubes in parallel, not a single tube.**
The measured correlations are averages over tubes with different atom numbers. The comparison to theory requires a Thomas-Fermi approximation for the tube distribution, introducing model-dependence. (A) Consensus — this is a universal limitation of all current cold-atom 1D experiments and is explicitly handled in the GHD simulations; it softens sharp features but does not invalidate the main findings. (paper §experimental methods; broader literature)

---

## Section 7 — Detailed Summary & Explanation

This paper establishes the theoretical framework for a new phase of quantum matter — fractional Fermi seas — in a 1D Bose gas, and provides the theoretical backbone for their experimental realization with ultracold Cs atoms.

The starting point is the Lieb-Liniger model: a textbook-exact description of 1D bosons with contact interactions, tunable from repulsive to attractive. The authors exploit a topological trick embedded in the model's structure. When you trace a closed loop in coupling-constant space — ramping g₁D from 0 through +∞ to −∞ and back to 0 — the many-body quantum state doesn't return to where it started. The loop applies a non-trivial transformation to the quasi-momentum distribution, stretching the Fermi surface by a factor of 2 and halving its occupancy. Repeat ℓ/2 times, and you have an occupancy of 1/ℓ over a momentum range of ℓ times the original Fermi momentum. Same total particle count, completely different Fermi sea.

These states are stabilized by integrability. The Lieb-Liniger model has infinitely many conserved quantities (quasiparticle occupation numbers in each momentum mode), and these act as a complete set of "guardrails" that prevent the highly excited state from thermalizing. Instead the system settles into a Generalized Gibbs Ensemble — a maximum-entropy state subject to all those conservation laws — and stays there indefinitely (in the ideal model; in practice, ~5 seconds in the experiment before three-body losses degrade it).

The theoretically exciting part is what these states do to correlation functions. A normal TLL — the established framework for all 1D quantum criticality — has correlation functions built on a single sharp Fermi surface: power-law decay with exponents set by one parameter K, and Friedel oscillations at a single characteristic wavelength 2k_F. The fractional Fermi sea at α = ℓ has its Fermi surface spread over ℓ times the momentum range with 1/ℓ occupancy. The paper shows that this produces multi-component Friedel oscillations at harmonics of ℓ·k_F, with decay exponents that can't be fit by any TLL regardless of what K you choose. The long-distance behavior is still critical (power-law correlations) — it's not thermal noise — but it belongs to a different universality class. This is the claim that makes the paper significant: not just a new state, but a new fixed point of the long-distance RG flow.

The computation uses Generalized Hydrodynamics (GHD), which treats the full quasi-particle distribution as a fluid and can handle spatial inhomogeneity (the harmonic trap) and time-dependent interactions (the ramp protocol). The GHD results match the Innsbruck experiment — including the striking signature that the first-order correlation function G^(1)(x) goes negative (indicating phase oscillations that a ground-state Bose gas never shows) and has a Bessel-function-modulated envelope rather than a simple sinc.

The interpretation layer connects to Haldane's Generalized Exclusion Statistics: in a GES system with parameter α, each particle blocks α states from subsequent occupation. The fractional Fermi seas effectively implement α = ℓ > 1, which the authors provocatively call "super-fermionic." Whether this constitutes a precise derivation of GES from the Lieb-Liniger model or a suggestive analogy is the paper's most theoretically contentious point.

**Why is the summary framed this way?** The PRL Letter is primarily the theory paper; the experiment lives mostly in the companion arXiv preprint. I've emphasized the theoretical structure because that's the PRL content, while using the experimental details (Cs atoms, ℓ = 2 and 4, Friedel oscillation measurements) to anchor the claims. The most consequential interpretive choice is taking seriously the claim that these states represent a genuinely new universality class rather than just unusual excited states of a known system — that claim, if confirmed by RG analysis, elevates this well above a clever lab trick.

**Where I'm least confident in this analysis:** The specific form of the correlation function exponents and how they deviate from TLL predictions. The paper computes these via GHD and matches to experiment, but my plain-language translation of exactly how the multi-exponent structure arises from the fractional Fermi surface shape — and why those exponents can't be reproduced by any TLL — glosses over mathematical content (Bethe Ansatz form factors, large-distance asymptotic expansions) where the precision of the derivation matters enormously for the "new universality class" claim.

---

## Section 8 — Three Crystallized Takeaways

**1. A new phase of matter was engineered, not just observed.** By cycling the interaction of a 1D Bose gas between extreme repulsion and extreme attraction, the team used quantum geometry to "gear-shift" atoms into a state where each particle effectively claims multiple energy slots — a fractional Fermi sea. This state doesn't exist in equilibrium; you have to drive the system there on purpose.

**2. The Tomonaga-Luttinger liquid — the universal theory of 1D quantum matter — doesn't describe it.** That's not a shortcoming; it's the discovery. The correlations of a fractional Fermi sea decay with power laws and oscillate at stretched Friedel wavelengths that no choice of TLL parameters can reproduce. A new critical fixed point appears to exist beyond the established theory's reach.

**3. Integrability is what keeps the whole thing from collapsing.** The state is highly excited — the quantum equivalent of a car balanced on its roof — but conserved quantities in the exactly-solvable model act as structural braces, preventing thermalization. Without exact integrability, the gas would simply heat up. The experiment works because cesium in 1D is close enough to integrable for long enough (~5 seconds) to see the effect clearly.

---

## Section 9 — Shorter Summary

*(≤ 350 words)*

In quantum physics, particles in one dimension play by unusual rules. Bosons normally pile into the same state, while fermions stack one-per-level into a "Fermi sea." But in 1D, interactions and statistics are so intertwined that even bosons can behave like fermions when pushed hard enough — a phenomenon called fermionization. The theory governing all such systems at low temperature, the Tomonaga-Luttinger liquid (TLL), has been the established framework for decades.

This paper breaks out of that framework. The authors use a mathematical trick embedded in the exactly-solvable 1D Bose gas: when you trace a closed loop in interaction strength — slowly ramping from zero repulsion to infinite repulsion, jumping to infinite attraction, ramping back to zero attraction, then jumping back — the quantum state doesn't return to where it started. The roundtrip is a geometric detour in Hilbert space. Each complete cycle "stretches" the effective Fermi surface in momentum space by a factor of two and halves the occupancy per momentum state, producing what the authors call a fractional Fermi sea.

After two cycles you get a state with one-quarter the normal occupancy spread over four times the normal momentum range. Same number of particles, completely different internal structure. These states survive because the 1D Bose gas is exactly integrable — it has infinitely many conserved quantities that act as guardrails preventing the highly excited state from melting into thermal disorder.

The key result is what these states do to correlations. The oscillations and power-law decays that characterize quantum criticality are still present — this is not a thermal state — but their form is incompatible with any Tomonaga-Luttinger liquid, regardless of parameters. The Friedel oscillations appear at stretched wavelengths, the decay exponents take values no TLL can produce, and the first-order correlation function actually goes negative — something a ground-state Bose gas never does.

The Innsbruck experiment with ultracold cesium atoms confirmed these signatures at the first two rung-levels of the fractional sea. The theoretical description, built using Generalized Hydrodynamics, matches the data well. The result opens a new territory in the landscape of one-dimensional quantum phases, beyond the TLL's long reign.

---

*Turn count: 1 of 10 before next recommended* `check`*.*
