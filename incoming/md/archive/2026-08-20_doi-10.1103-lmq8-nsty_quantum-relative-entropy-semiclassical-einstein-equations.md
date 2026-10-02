# Gravity's Ledger: What a Horizon "Knows" About the Matter Crossing It

**Paper:** Philipp Dorau and Albert Much, "From Quantum Relative Entropy to the Semiclassical Einstein Equations," *Physical Review Letters* **136**, 091602 (2026). DOI: [10.1103/lmq8-nsty](https://link.aps.org/doi/10.1103/lmq8-nsty). arXiv:[2510.24491](https://arxiv.org/abs/2510.24491) (submitted 28 Oct 2025; v3, March 2026). Authors: Institut für Theoretische Physik, Universität Leipzig.

Framework v3.10 · Analyzed 2026-08-20 · Paper Analysis Pipeline - 11

**Access Status** — Full paper: retrieved from arXiv HTML, v3 (March 2026) — matches the published reference *Phys. Rev. Lett.* **136**, 091602 (2026), confirmed via the APS DOI landing page · Abstract: retrieved and cross-checked against both the arXiv abstract page and the APS journal page (consistent wording) · Supplementary material: one expository blog post (Tyler Walker, March 2026) and one paper-review aggregator (themoonlight.io) used only to cross-check framing and prior-work relationships, not as a primary source · Analysis basis: full text (arXiv v3, an open-access HTML extraction rather than the typeset PDF — see the uncertainty note in §7)

Citation verification: both arXiv:2510.24491 (v1–v3, Oct 2025–Mar 2026) and DOI 10.1103/lmq8-nsty resolve to the same paper (confirmed via journals.aps.org and link.aps.org) before analysis began.

**Hook:** Dorau and Much take a 30-year-old idea — that Einstein's equations aren't fundamental but are the thermodynamic "equation of state" of spacetime — and replace its shakiest ingredient, a classical entropy that's technically ill-defined in quantum field theory, with a quantum-information quantity that stays finite, then show the whole derivation still goes through.

## Big-Picture Context

In 1995, Ted Jacobson published one of the most influential thought experiments in gravitational physics: he showed that if you assume the Clausius relation (heat in = temperature × entropy change) holds for the local causal horizon of every accelerated observer at every point in spacetime, and combine that with the Unruh effect (accelerated observers see the vacuum as warm) and the Bekenstein-Hawking entropy-area law, Einstein's field equations pop out as an "equation of state" — not a fundamental law, but an emergent thermodynamic identity, the same way the ideal gas law emerges from statistical mechanics without being fundamental itself. It reframed gravity as thermodynamics, not geometry-for-its-own-sake, and spawned an entire research program (entropic gravity, entanglement-based derivations of GR) that continues today.

The soft spot in Jacobson's argument was always the "S" in that Clausius relation. The entropy he uses is the ordinary thermodynamic/von Neumann entropy of the horizon — but in genuine quantum field theory, that quantity is not well-defined. The algebras of observables associated with a region of spacetime are "type III" von Neumann algebras, and the vacuum's entanglement across any boundary is so densely packed at short distances that the naive entropy diverges. Jacobson's 1995 paper sidesteps this by working at the level of classical thermodynamics and invoking the Unruh/Hawking effects as physical justification, but a rigorous QFT-native version of the argument was left as an open problem. This paper is an attempt to close exactly that gap, for a controlled test case (a free scalar field on a local Killing horizon), using **quantum relative entropy** — a quantity that Casini and others have shown remains finite in QFT precisely because it measures the *difference* between two states relative to a shared reference, rather than an absolute entropy.

**Paper Type & Stakes:** this is a short theoretical/mathematical-physics Letter — not an experimental result and not a new numerical prediction — that re-derives a known equation (the semiclassical Einstein equation) via a more rigorous internal logic. What's at stake is not "does gravity work differently now" (it doesn't, observationally) but whether the "gravity is thermodynamics/emergent from quantum information" research program can be put on genuinely solid QFT footing rather than resting on classical heuristics — which matters for how seriously that whole program should be taken as a route toward quantum gravity.

**Prior Belief Check:** this does not contradict or surprise the field in the way a new observation might. It sits squarely inside an established and actively pursued lineage — Jacobson's 1995 derivation, Jacobson's own 2015 "Entanglement Equilibrium and the Einstein Equation" (which *also* uses relative-entropy-flavored reasoning, but on small causal diamonds via a first-law/linear-response argument rather than bifurcate Killing horizons), and Faulkner, Guica, Hartman, Myers & Van Raamsdonk's 2013 "Gravitation from Entanglement in Holographic CFTs" (linearized Einstein equations from the first law of entanglement entropy, in an AdS/CFT-specific setting). Specialists in this corner of the field have wanted exactly this kind of rigorous algebraic-QFT upgrade for a while; the result is not conceptually shocking to them, but the specific technical execution — using Tomita-Takesaki modular theory to get an *exact* closed-form identity rather than a linear-response approximation — is a genuine and non-trivial technical contribution.

**Replication & Convergence Note:** this is a single-group (two-author, University of Leipzig) theoretical result with no independent verification of the specific calculation. "Replication" for a derivation doesn't mean repeating an experiment, but it does mean: has another group checked or reproduced this exact modular-theoretic computation? Not yet — the paper posted its first version in October 2025 and reached PRL only in March 2026, too recent for independent technical scrutiny to have visibly accumulated. There *is* convergence at the conceptual level (multiple independent groups — Jacobson, Casini, Faulkner et al. — arriving at "relative entropy connects to area/curvature" via different technical routes), which is meaningful supporting context, but it is not the same as this specific derivation being independently checked.

## Necessary Background Crash-Course

**Local Rindler horizons and the Unruh effect.** Jacobson's trick — reused here — is to note that at any single point $p$ in any curved spacetime, the equivalence principle lets you approximate a small enough neighborhood as flat Minkowski space. In that local flat patch, pick a boost direction through $p$: this generates a local Rindler horizon, a pair of null sheets crossing at a spacelike 2-surface (the "bifurcation surface"), exactly like the horizon an accelerating observer in flat space would have. An accelerating observer, it turns out, perceives the ordinary vacuum as a thermal bath, at a temperature set by their acceleration (the Unruh effect) — and by the equivalence principle, this local horizon-at-a-point stands in for a real black-hole-like horizon everywhere in spacetime, all at once.

> **Analogy:** think of a Rindler horizon like the read boundary of a circular (ring) buffer for an accelerating process. Past that boundary, data (light rays, causal influence) is gone for good — it can never catch up to you again. What crosses that boundary and vanishes doesn't look, from inside, like a clean silent loss; it looks exactly like packets arriving from a thermal random source, at a "temperature" set by how fast you're accelerating (the Unruh temperature).
>
> **Breaks when:** you ask what's physically radiating. There's no actual particle emission happening at the horizon for an inertial observer watching the same region — the thermality is an artifact of one observer's coordinate/causal-structure choice, not a physical process occurring "at" the horizon in any frame-independent sense.

**Why relative entropy instead of von Neumann entropy.** Ordinary (von Neumann) entropy answers "how much entropy does this one state have." In QFT, that number is infinite for essentially every state, because the vacuum is entangled across any boundary all the way down to arbitrarily short distances (this divergence is the technical signature of the "type III" algebra structure of QFT). Quantum relative entropy asks a different question — "how distinguishable is state A from a fixed reference state B" — and Casini showed this quantity, unlike the individual entropies, stays finite.

> **Analogy:** von Neumann entropy in QFT is like trying to compute a checksum of an infinitely long file with no natural stopping resolution — the number diverges because there's always more detail to hash at every finer zoom level. Relative entropy is a *diff* between two versions of that same infinite file, both referenced against the identical baseline: the diff can be perfectly finite and well-defined even when neither file's own "size" is.
>
> **Breaks when:** you try to ask about a single state in isolation. Relative entropy only answers "how distinguishable is A from reference B" — it says nothing about A's own entropy content, and that's precisely the feature (not a bug) that lets it stay finite here.

**Modular theory and KMS states.** This is the technical engine of the paper. When you restrict the vacuum state to the algebra of observables living on one side of a horizon, deep operator-algebra theorems (Bisognano-Wichmann originally; Kay-Wald and Summers-Verch for horizons specifically) show that the state's own intrinsic "modular flow" — an abstract mathematical automorphism that exists for *any* quantum state on *any* algebra — coincides exactly with the physical boost symmetry that generates the horizon. In other words, the purely information-theoretic structure of the vacuum state and the purely geometric structure of the horizon turn out to be the same object.

> **Analogy:** every subsystem's reduced state has its own abstract "modular clock," derived purely from the state's own statistics, with no reference to physical time. For a horizon, this modular clock turns out to run in exact lockstep with the physical boost symmetry of spacetime — like discovering that a subsystem's own internally-derived cache-eviction ordering, computed purely from access statistics, happens to exactly match the real wall-clock of some unrelated physical process. It's a deep, non-obvious coincidence that holds only because the region in question is bounded by a genuine (Killing) horizon.
>
> **Breaks when:** you push it to a generic region of spacetime with no horizon. The modular flow still exists mathematically for any state on any algebra, but it no longer has this clean geometric (boost-like) meaning — it becomes some abstract, highly non-local flow with no simple physical picture at all. The clean geometric correspondence is a horizon-specific gift, not a generic feature.

> **Central analogy for this paper:** the bifurcate horizon as a tamper-evident audit log — the modular clock is its native timestamp, and relative entropy measures how "off" the log looks once extra traffic (matter) writes through it.

## Core Technical Explanation

The derivation is a five-step chain, and the payoff of the whole paper is that step 3 — the one place Jacobson's original argument had to appeal to classical thermodynamics — becomes a proven identity instead of an assumption.

**Step 1 — Set the stage.** At any spacetime point $p$, approximate a small neighborhood as flat and pick a local boost direction, generating a bifurcate Killing horizon (two null sheets $\mathcal{H}_A$, $\mathcal{H}_B$ meeting at a bifurcation surface $\mathcal{S}$). Put a free scalar field on it. The vacuum restricted to one side is a KMS (thermal) state at the Unruh temperature, and — this is the key structural fact from the background section — its modular flow acts geometrically as a boost along the horizon's null coordinate, which the paper writes as an affine dilation of the null coordinate $U$.

**Step 2 — Build the horizon's own quantum theory.** Rather than working with the bulk field theory, the authors construct the algebra of observables *living on the horizon itself*, generated by field data (test functions) on the null surface, with a natural symplectic (Poisson-bracket-like) pairing built from how that data varies along the horizon. The vacuum becomes a specific "quasifree" (Gaussian) state on this algebra, and a physically excited state — standing in for matter perturbing the horizon — is built as a **coherent state**: a displaced version of the vacuum, generated by exponentiating the field data.

**Step 3 — Compute the relative entropy exactly (the paper's central result).** For coherent states specifically, there's a known closed-form expression for the Araki-Uhlmann relative entropy in terms of the modular operator. Because step 1 established that the modular flow acts geometrically as a boost, this abstract expression collapses into a concrete geometric integral over the horizon:

$$S^{\text{rel}}(\omega_0 \,\|\, \omega_\phi) \;=\; -2\pi \int_{\mathcal{H}} U \,(\partial_U \phi)^2 \, dU \, d\mathrm{vol}_{\mathcal S}$$

**Symbol definitions:**
$S^{\text{rel}}(\omega_0\,\|\,\omega_\phi)$ : the relative entropy between the vacuum $\omega_0$ and the coherently excited state $\omega_\phi$ — a pure number, "how distinguishable is the excited horizon state from vacuum"
$U$ : the null (affine) coordinate along the horizon, negative on the relevant branch, that the boost dilates
$\phi$ : the classical field profile defining the coherent excitation (stand-in for matter crossing the horizon)
$\partial_U \phi$ : the rate of change of that field profile along the horizon
$d\mathrm{vol}_{\mathcal S}$ : the area element on horizon cross-sections

**What this actually means:** since $(\partial_U\phi)^2 \geq 0$ and $U<0$ on this branch, the integral is automatically non-negative — the formula bakes in relative entropy's required positivity (Araki's theorem) as a geometric fact rather than a separate check. More importantly, because $(\partial_U\phi)^2$ is directly proportional to the null-null component of the field's (normal-ordered) stress-energy tensor, this equation says: *relative entropy equals $2\pi$ times a boost-weighted flux of energy through the horizon.* That's a diff/checksum on the left, and a physical energy flow on the right — the paper is asserting these are the same number.

**Step 4 — Recognize this as the missing piece of Jacobson's argument.** Jacobson's 1995 Clausius relation, $\delta Q = T\,\delta S$, needed "$\delta Q$" (heat flux through the horizon) to equal "$T\,\delta S$" (temperature times entropy change) — a relation he had to import from classical thermodynamics. Step 3 above proves exactly this identity, but for genuine quantum relative entropy rather than classical thermodynamic entropy, and as a theorem rather than a postulate.

**Step 5 — Close the loop with geometry.** The Raychaudhuri equation governs how a horizon's cross-sectional area responds to energy flux through it (this is standard focusing-theorem physics, unchanged from Jacobson). Assuming — as an *imported* ingredient, not a derived one — that total horizon entropy obeys the Bekenstein-Hawking area law $S = A/4G$, the energy-flux-equals-relative-entropy identity from Step 3 becomes an area-change relation, which Raychaudhuri converts into a statement about the local Ricci curvature. Because this whole construction can be repeated at *every* spacetime point $p$ and *every* boost direction, the only way the resulting pointwise relation can hold universally is if the full tensorial semiclassical Einstein equation holds:

$$R_{ab} - \tfrac{1}{2}Rg_{ab} + \Lambda g_{ab} \;=\; 8\pi G\,\langle T_{ab}\rangle$$

**Symbol definitions:**
$R_{ab}, R$ : the Ricci tensor and Ricci scalar — measures of spacetime curvature
$g_{ab}, \Lambda$ : the metric and cosmological constant
$\langle T_{ab}\rangle$ : the *quantum expectation value* of the stress-energy tensor — not a classical field, a QFT expectation value

**What this actually means:** this is the "semiclassical" Einstein equation — spacetime curvature (fully classical, unquantized) sourced by the quantum-mechanically averaged energy-momentum of matter. It's the same equation used throughout black hole thermodynamics and Hawking radiation calculations; the paper's contribution is not a new equation, it's a new (more rigorous) route to the old one.

### Assumption Audit

> **Watch:** the reader likely assumes this derives Einstein's equations "from nothing" — proving gravity is pure quantum information with no other input. **The paper actually says:** the Bekenstein-Hawking area-entropy law ($S=A/4G$) is imported by hand, exactly as in Jacobson's original 1995 argument — it is not derived here. The real claim is narrower and still valuable: *if* you already accept $S=A/4G$, the rest of the argument — the part that used to require a classical thermodynamic postulate — now follows as a proven quantum-information-theoretic identity instead.

> **Watch:** the reader likely assumes "quantum relative entropy" here is being computed for genuinely entangled, highly non-classical excitations. **The paper actually says:** the explicit closed-form calculation is done only for **coherent states** — displaced-vacuum configurations that are quasi-classical in character (they're the QFT analogue of a classical wave riding on the vacuum, not a genuinely entangled superposition). The "quantum" in "quantum relative entropy" is doing real work — finiteness, and the modular-theoretic route to it — but the specific worked example is the mildest, most tractable case, not a demonstration for generic quantum states.

> **Watch:** the reader might assume this constructs a full alternative theory of gravity (global solutions, initial-value structure). **The paper actually says:** like Jacobson's 1995 argument, this is a strictly *local, pointwise* derivation — it shows the Einstein tensor is forced at each point individually, and never addresses whether patching these pointwise statements together yields a globally well-posed dynamical theory (a well-defined Cauchy problem for the metric).

## What's Genuinely New or Clever

The specific trick is combining two pre-existing but previously unconnected pieces of machinery: (1) the fact (Kay-Wald, Summers-Verch) that modular flow on a Killing horizon acts geometrically as a boost, and (2) the known closed-form expression for relative entropy of coherent excited states (from the Longo/Casini line of algebraic-QFT work). Individually, neither is new. What's new to the field is plugging them together into precisely the gap in Jacobson's argument that needed a rigorous QFT replacement — turning "assume $\delta Q = T\delta S$" into "here is the exact identity that plays that role, proven from modular theory, with the divergence problem of ordinary entropy sidestepped by using relative entropy instead." That's a genuine tightening of a 30-year-old argument's weakest joint, done with real technical machinery rather than another layer of physical intuition.

**Predictive Content Check:**

1. **Falsifiable handle:** none, in the ordinary empirical sense. This paper "relabels rather than predicts" — it re-derives an equation (the semiclassical Einstein equation) that is already extensively tested and already in everyday use in black hole physics and cosmology; it does not predict any new observable, number, or scale that could come out wrong in an experiment. Its only "check" is internal/mathematical: that the derivation is self-consistent and reproduces the correct proportionality constant ($8\pi G$) rather than some other coefficient. That's a legitimate and useful thing for a foundations paper to do, but it should be named plainly as structural rather than empirical content.

2. **Formalism load:** this half fires, because the paper leans entirely on mathematical structure with no empirical handle. The modular-theory machinery here is load-bearing, not decorative — it is the *entire* mechanism that converts an abstract information-theoretic quantity into a concrete geometric flux integral. Strip it out and you're left with Jacobson's original 1995 heuristic (an assumed Clausius relation); the machinery is doing the one specific job the paper claims for it.

## Limitations & Open Questions

> The Bekenstein-Hawking entropy-area relation is imported as an ingredient, not derived — the same feature that has drawn a standing circularity critique against the entire Jacobson-style "gravitational thermodynamics" program (see, e.g., the 2016 comments paper on Jacobson's 2015 "Entanglement Equilibrium," arXiv:1601.00528). **(B) Contested** — some physicists view this as a legitimate physical postulate grounded in independently-motivated black hole thermodynamics; others view importing the area law as smuggling in exactly the geometric content the derivation claims to produce. Reasonable experts land on both sides. **(broader literature; also the paper's own explicit framing, since it invokes $S=A/4G$ as an ingredient rather than a derived result)**

> The explicit calculation covers only coherent excitations of a free scalar field — not entangled states, interacting fields, or fermionic/gauge matter. **(A) Consensus** — restricting to coherent states is a standard, openly-used simplification throughout this line of work precisely because it's the analytically tractable case; extending beyond it is a recognized open technical challenge, not a controversial claim. **(analyst inference — the restriction is evident from what is and isn't computed; no explicit limitations section was retrievable from the extraction to confirm the authors state this themselves)**

> The result is local and pointwise, like Jacobson's original — it says nothing about whether stitching these single-point derivations together yields a globally well-posed dynamical theory of the metric (a proper initial-value formulation). **(A) Consensus** — this is a well-known, openly acknowledged limitation of the entire "gravity as equation of state" program going back to 1995, not something specific to this paper. **(broader literature)**

> No independent technical scrutiny has visibly had time to accumulate — the first arXiv version posted in October 2025 and PRL publication followed in March 2026. **(C) Speculative** — this is my inference from publication recency and the absence of visible follow-up critique in what I could retrieve, not a documented fact; a specialist actively working in this subfield might already be aware of seminar discussion, referee pushback, or early citations I have no visibility into. **(analyst inference)**

## Detailed Summary & Explanation

Jacobson's 1995 argument reframed Einstein's equations as a thermodynamic identity rather than a fundamental law: apply the Clausius relation ($\delta Q = T\delta S$) to the local causal horizon that exists, in principle, at every point of every spacetime, and general relativity falls out as an "equation of state." The argument was elegant and enormously influential, but it leaned on classical thermodynamic entropy — a quantity that simply isn't rigorously defined in quantum field theory, where the vacuum's own entanglement structure makes the ordinary (von Neumann) entropy of any finite region diverge.

Dorau and Much's contribution is to replace that classical entropy with quantum relative entropy — the Araki-Uhlmann distinguishability measure between two states — which Casini and others have shown stays finite in QFT precisely because it's a comparison between two states, not an absolute property of one. Using the deep fact that a horizon's modular flow (an abstract, state-defined mathematical structure) coincides geometrically with the physical boost symmetry that generates the horizon, they compute this relative entropy explicitly for coherent (quasi-classical) field excitations and get a clean closed-form answer: it equals $2\pi$ times a boost-weighted flux of energy through the horizon. That is exactly the relation Jacobson needed to assume in 1995 — here it's proven. Combined with the (still-imported) Bekenstein-Hawking area-entropy law and the standard Raychaudhuri focusing equation, the semiclassical Einstein equation falls out, holding at every point and in every direction.

The interpretive choice made in framing this analysis is to keep drawing a hard line between what's *proven* here (the relative-entropy-equals-flux identity, via modular theory) and what's still *imported* (the entropy-area law itself) — because the paper's actual, careful claim is the former, not "gravity fully derived from quantum information with nothing else assumed." Treating those as separable is what makes it possible to say the paper is a real technical advance without overselling it as a solved foundations problem. The framing also foregrounds that this is fundamentally a rigor upgrade to an existing 30-year-old argument, not a new physical claim about the world — which matters for calibrating how exciting this should feel relative to, say, a genuinely new experimental result.

**Where I'm least confident in this analysis:** the precise index-and-derivative manipulation that turns the abstract modular-operator expression for relative entropy (an inner product involving the derivative of the modular flow) into the concrete horizon integral over $U(\partial_U\phi)^2$ — and likewise the exact form of the Raychaudhuri-equation step that converts an area variation into a Ricci-tensor statement. This analysis worked from an AI-generated extraction of the arXiv HTML rather than the raw LaTeX/PDF, so the equation numbers and exact intermediate steps presented are a faithful paraphrase of that extraction's account, not a line-by-line verification against the paper's own typesetting — this is exactly the kind of calculation-heavy middle section where a translation step could quietly lose or misstate a technical subtlety. Also uncertain whether the closed-form relative-entropy formula for coherent states (the starting point of Step 3) is newly proven in this paper or quoted from prior literature (most likely Longo's or related algebraic-QFT work) — that distinction affects how much of the technical content here is genuinely new math versus a new assembly of known results, and this could not be resolved cleanly from the material retrieved.

## Three Crystallized Takeaways

1. **Einstein's equations might not be fundamental** — they could be the thermodynamic "equation of state" of quantum information flowing across horizons, an idea from 1995 that this paper makes mathematically rigorous rather than heuristic, at least for one clean test case.
2. **The fix is a quantity swap:** classical entropy (which literally doesn't converge in quantum field theory) gets replaced by quantum relative entropy (which does), and deep operator-algebra machinery shows this "how distinguishable are two states" number is secretly identical to a physical energy flow across a horizon.
3. **This isn't a testable prediction — it's a foundational tightening.** It still needs an outside ingredient (the Bekenstein-Hawking area-entropy law) to close the loop, so whether this counts as "gravity finally explained" or "an elegant restatement of an already-assumed package" remains a genuinely open and contested question, not one this paper settles.

## Shorter Summary

In 1995, physicist Ted Jacobson showed something remarkable: apply the basic thermodynamic relation "heat in equals temperature times entropy change" to the causal horizon that exists, in principle, at every point in space and time, and Einstein's equations of general relativity fall out — suggesting gravity isn't a fundamental force at all, but an emergent thermodynamic phenomenon, like how pressure emerges from the statistics of countless gas molecules.

The weak link in that 30-year-old argument was always "entropy." Jacobson used ordinary thermodynamic entropy, but in genuine quantum field theory that quantity is mathematically ill-behaved — it diverges to infinity because the quantum vacuum is entangled across any boundary all the way down to arbitrarily short distances.

Philipp Dorau and Albert Much's new paper fixes this by swapping in a different, better-behaved quantity from quantum information theory: relative entropy, which measures how distinguishable two quantum states are from each other rather than measuring one state's entropy in isolation. Crucially, this quantity stays finite even when ordinary entropy doesn't. Using sophisticated mathematical tools (modular theory, from the operator-algebra branch of physics) that reveal a hidden geometric structure inside the vacuum state itself, they compute this relative entropy exactly for a simple test case — a scalar field disturbing a local horizon — and show it equals precisely the quantity Jacobson needed to assume back in 1995, now proven rather than postulated. Combined with one more classic ingredient (that horizon entropy is proportional to horizon area, from black hole physics), the derivation closes and Einstein's equations emerge.

This is not a new experimental prediction — it doesn't tell you anything new to go measure. It's a foundational reformulation, tightening one specific weak joint in an influential 30-year-old argument using genuine quantum-information-theoretic rigor instead of classical hand-waving. It still leans on one imported assumption (the area-entropy law), so it doesn't fully "derive gravity from nothing" — whether that remaining gap matters is a real, unresolved disagreement among physicists working on this program. As a single-group, very recent result (first posted October 2025, published March 2026), it also hasn't yet had time for the community to stress-test the specific calculation.


---

## Appendix — Deep-Dive Discussion Log (2026-08-22)

**Q: I don't understand modular theory and KMS, no background in the algebras they were talking about.**

Let's build this from scratch, no operator-algebra background assumed.

*What "algebra of observables" means.* In QFT, physicists group together all the observables measurable using only equipment confined to some region of spacetime — the complete question-set for that region. A "state" (like the vacuum) is an assignment of an answer (expectation value) to every question in that set. QFT regional algebras are "type III," which is the technical reason ordinary entropy diverges — the reason a rigorous replacement (relative entropy) was needed at all.

*Modular theory: a "clock" that falls out of the state itself.* Take an algebra of observables and a specific state — like the vacuum restricted to one side of a horizon. Tomita-Takesaki theory says: from this pairing of algebra + state alone, you can manufacture a one-parameter family of transformations of the algebra, the **modular flow** ($\sigma_t$), relabeling observables as a fictitious parameter $t$ ticks forward — not physical time, but a "clock" manufactured purely from the state's own correlational structure. Change the state, get a different modular flow on the same algebra. Most of the time this abstract flow has no physical meaning at all.

*KMS states: the flow that makes a state "look thermal."* A thermal equilibrium state at temperature $T$ has correlation functions with a specific analytic-periodicity property (the KMS condition) when evolved in physical time. A state is *always* automatically KMS with respect to its own modular flow. So "modular flow" and "being thermal" are two descriptions of the same fact — any state, restricted to any algebra, is automatically in equilibrium with respect to the clock its own modular theory manufactures. Still pure math at this point, true for any state on any algebra.

*The physics-specific miracle.* When the state is specifically the vacuum, and the region is specifically one side of a horizon (Bisognano-Wichmann for flat space; Kay-Wald/Summers-Verch for horizons generally), the abstract modular flow isn't a featureless relabeling — it's literally the boost, the physical symmetry generating the horizon, sliding points along the horizon's null generators. Two completely different-sounding objects — an abstract, state-derived information-theoretic clock, and a concrete geometric spacetime symmetry — turn out to be the exact same transformation, but only in this special horizon setup. Push the same construction to a generic region with no horizon and the modular flow keeps existing mathematically but loses this clean geometric picture.

*Why the paper needs this.* Relative entropy's native definition is an abstract expression built from modular operators — no geometric meaning on its own. Substituting "modular flow" with "boost" is what turns it into the concrete integral in Step 3. Take away Bisognano-Wichmann/Kay-Wald/Summers-Verch, and relative entropy stays finite but has no route to a geometric flux integral.

---

**Q: Further explanation of *why* the vacuum-on-a-horizon modular flow is literally the boost.**

*The geometric picture.* The right Rindler wedge is $x>|t|$ in Minkowski space. A boost with rapidity $\theta$ slides points along hyperbolas of constant acceleration; at the horizon itself (where the hyperbolas degenerate to null lines), the boost becomes an affine dilation of the null coordinate $U \to e^{-\theta}U$.

*The trick: Euclidean rotation.* Continuing time to imaginary values ($t\to -i\tau$) turns Minkowski space into Euclidean space, and a Lorentzian boost becomes an ordinary Euclidean rotation — the same formula, rapidity playing the role of rotation angle. Rotations are periodic (period $2\pi$), so a boost continued to imaginary rapidity inherits that periodicity.

*How the vacuum is built.* The Minkowski vacuum can be constructed as a Euclidean path integral over the full Euclidean plane; in polar coordinates, the angle is the (imaginary-continued) boost parameter. The right wedge is one ray of that plane. Restricting to operators in the right wedge while integrating over the full $2\pi$ of Euclidean angle is mathematically identical to a thermal path integral on a periodic imaginary-time circle of circumference $2\pi$.

*Analogy:* picture the full Euclidean plane as a pie and the right wedge as one slice, hinged at the center (bifurcation surface). Rotating the whole pie by angle $\theta$ and watching only your slice is indistinguishable, correlator by correlator, from thermal time evolution for imaginary time $\theta$ around a clock face of circumference $2\pi$.

*Why the periodicity settles it.* The KMS condition requires correlation functions, continued to imaginary time, to be periodic with period $2\pi$ in modular units — exactly what the Euclidean-rotation argument hands us from pure geometry. Modular theory also guarantees the modular flow is the *unique* flow making a given state KMS. The boost, continued to imaginary rapidity, demonstrably has that periodicity; uniqueness forces modular flow and boost to be the identical transformation. (This is the same calculation behind the Unruh effect — modular theory and Unruh thermality are two names for the same $2\pi$-periodicity fact.)

*Tie-back to the paper.* This is why Step 1 can assert "modular flow acts geometrically as a boost" as established fact, and why the $2\pi$ in the Step 3 formula is the same $2\pi$ as the Euclidean rotation's periodicity, not an arbitrary constant.

---

**Q: What is meant by a boost?**

A boost is the conversion between the descriptions of two observers moving at constant relative velocity — the relativistic version of "your friend jogging alongside sees the ball moving slower than you do." Relativistically, space and time mix under this conversion in a way that keeps the speed of light invariant:

$$t' = t\cosh\theta + x\sinh\theta,\qquad x' = x\cosh\theta + t\sinh\theta$$

— structurally identical to an ordinary rotation with $\cos/\sin$ replaced by $\cosh/\sinh$ ("hyperbolic rotation mixing space and time"). Substituting imaginary rapidity ($\theta\to i\phi$) turns the hyperbolic formulas into the circular ones directly — the fact used above.

A continuous family of boosts, run as a flow, traces a hyperbola in $(t,x)$ — the worldline of a uniformly accelerating observer. So "the boost" as a generator is simultaneously the frame-conversion operation and the flow generating an accelerated observer's trajectory. That accelerating observer can never exchange signals with events across a pair of diagonal lines through the origin — the Rindler horizon — and the boost is exactly the symmetry sliding the observer along their hyperbola while sliding points along the horizon itself, degenerating from hyperbola to straight null line exactly at the horizon. This is the construction Jacobson (and this paper) reuse at every spacetime point: pick a boost direction, get a local Rindler horizon.

---

**Q: Explain the central analogy in the analysis** (the bifurcate horizon as a tamper-evident audit log).

Note: this framing is a teaching device from the analysis, not literal language from the paper.

- **The log = the horizon.** Each point along the null coordinate $U$ is a line-number.
- **"Tamper-evident" = the vacuum's thermality (KMS-ness).** An unaltered stretch of log has a predictable statistical fingerprint — the vacuum's automatic KMS thermality with respect to the modular flow.
- **"Native timestamp" = the modular flow = the boost.** No external clock is imported; the horizon's own causal structure supplies its own ordering.
- **"Extra traffic writes through it" = matter crossing the horizon** — the coherent state $\omega_\phi$, standing in for a classical field crossing.
- **"How off the log looks" = relative entropy** $S^{\text{rel}}(\omega_0\|\omega_\phi)$ — purely a tamper-detection question: how distinguishable does the log look from its clean baseline.

*The punchline:* because the log's native timestamp is already the boost — a genuine geometric coordinate, not an abstract label — "how off the log looks" can be computed using that same coordinate, collapsing the abstract relative-entropy formula into the concrete integral $-2\pi\int_{\mathcal H} U(\partial_U\phi)^2\,dU\,d\mathrm{vol}_{\mathcal S}$: a $U$-weighted sum of how much the "extra traffic" disturbed each point. Since that disturbance term is proportional to the crossing matter's energy, "how anomalous the log looks" and "how much energy crossed" are the same number, up to the $2\pi$ inherited from the boost's periodicity — exactly the missing piece Jacobson needed to assume in 1995.

---

**Q: Explain Step 2 of the Core Technical Explanation.**

Step 2 builds a self-contained "toy universe" living only on the horizon, rather than dragging the whole bulk field theory through the calculation.

*Field data (test functions) on the null surface.* Field values at exact points are often ill-defined in QFT, so the field is smeared against smooth test functions and integrated: $\int\phi(U)f(U)\,dU$. The horizon algebra is built from all these smeared observables.

*The symplectic pairing.* In classical mechanics, position and momentum are linked by the Poisson bracket $\{q,p\}=1$. On the horizon there's no separate momentum — the field's own rate of change along $U$ plays that role, giving a natural pairing like $\int(f\,\partial_U g - g\,\partial_U f)\,dU$ between two smeared observables, which becomes the commutation structure once quantized.

*The vacuum as a "quasifree" (Gaussian) state.* Like a Gaussian probability distribution needing only a mean and variance (unlike a general distribution, which needs infinitely many moments), a quasifree state is completely determined by its two-point correlation function, zero mean, with all higher correlators fixed automatically. The vacuum, restricted to the horizon algebra, is exactly this simplest kind of state — the technical reason the calculation stays tractable.

*Coherent states — displacing the vacuum.* To represent matter crossing the horizon while staying inside this tractable family, apply an exponential ("Weyl") operator $e^{i(\text{smeared field data})}$ to the vacuum — like sliding a bell curve's center over without changing its shape. The result is still Gaussian/quasifree, but now has a nonzero mean equal to the classical field profile $\phi$ — the standard representation of "a classical wave riding on vacuum fluctuations."

*Why this setup matters.* Relative entropy between two Gaussian/quasifree states differing only by such an exponential displacement has a known, exact closed-form expression in terms of the modular operator (the Longo/Casini-line result). A more general, non-Gaussian excitation would have no such clean formula — Step 2's entire job is engineering the setup so Step 3's formula is exact rather than approximate.

---

**Q: Details on Step 3 — the heart of the paper.**

*What's being computed.* $S^{\text{rel}}(\omega_0\|\omega_\phi)$, the "how distinguishable" score between vacuum and the matter-displaced state. In finite dimensions this would be $\mathrm{Tr}[\rho\ln\rho-\rho\ln\sigma]$; QFT has no density matrices, so Araki generalized it via modular operators — same question, different machinery.

*The special fact for coherent states.* Relating relative entropy to an energy difference is normally only exact to leading order for small perturbations (the "first law of entanglement entropy"). But because coherent states are built by a simple exponential displacement, a known theorem makes the relation *exact*:

$$S^{\text{rel}}(\omega_0\|\omega_\phi) = \langle K\rangle_\phi - \langle K\rangle_0$$

where $K$ is the modular Hamiltonian (generator of modular flow, the operator-theory analogue of an ordinary Hamiltonian).

*Why $K$ becomes concrete.* Because modular flow = boost, $K$ is literally the boost generator — a Noether charge with the standard form (same logic as angular momentum = position × momentum):

$$K = 2\pi\int_{\mathcal H} U\,T_{UU}\,dU\,d\mathrm{vol}_{\mathcal S}$$

weighting the local energy flux $T_{UU}$ by how far along the horizon ($U$) it crossed.

*Two standard substitutions.* The vacuum's own expected boost charge $\langle K\rangle_0=0$ after normal-ordering, so only $\langle K\rangle_\phi$ survives. For a free scalar, $T_{UU}\propto(\partial_U\phi)^2$ — textbook stress-tensor content.

*Result.*

$$S^{\text{rel}}(\omega_0\|\omega_\phi) = -2\pi\int_{\mathcal H} U\,(\partial_U\phi)^2\,dU\,d\mathrm{vol}_{\mathcal S}$$

Chain, compressed: coherent states saturate the first law exactly (imported theorem) → modular Hamiltonian = boost generator (Step 1's geometric fact) → boost generator has the standard $U$-weighted-flux Noether form → a free scalar's flux is just $(\partial_U\phi)^2$ (textbook). None of the individual pieces is new; the contribution is recognizing the stack produces exactly the identity Jacobson needed.

*Positivity check.* Relative entropy must be $\geq0$ (Araki's theorem). $(\partial_U\phi)^2\geq0$ always, and $U<0$ throughout the relevant branch, so $-U(\partial_U\phi)^2\geq0$ pointwise — positivity is wired into the geometry itself, not checked after the fact.

---

**Q: Step 4.**

Jacobson's Clausius relation $\delta Q = T\,\delta S$ needed heat flux $\delta Q$, temperature $T$, and entropy change $\delta S$, with the relation holding as physics.

*"Heat flux" is boost-weighted energy flux.* Heat is always defined relative to a system's own time-translation symmetry — near a horizon, that's the boost. So Jacobson's $\delta Q$ is exactly the same $U$-weighted integral ($\int U\,T_{UU}$) as the modular Hamiltonian/boost charge from Step 3 — not a coincidence, a direct identification.

*The temperature is the Unruh temperature*, $T=\kappa/2\pi$ — the same $2\pi$ from the Euclidean-rotation/KMS periodicity discussed above, and the same $2\pi$ out front of the Step 3 formula. A genuine consistency check: any other constant in Step 3 would have broken the match.

*Jacobson's gap.* He had to *assume* $\delta Q=T\delta S$ using an entropy that isn't actually well-defined in QFT — a postulate dressed as an established law.

*What Step 3 delivers.* $S^{\text{rel}} = \delta Q/T$ falls out as a proven theorem, no postulates, for a genuinely well-defined quantum quantity. Quantum relative entropy steps into the role classical entropy used to occupy — for coherent excitations specifically; it doesn't yet reach Einstein's equations by itself (still needs the area law and Raychaudhuri, Step 5).

---

**Q: Step 5.**

Untouched from Jacobson 1995 — the novelty was entirely Steps 1–4.

*Raychaudhuri equation.* Governs how a bundle of light rays generating the horizon focuses:
$$\frac{d\theta}{dU} = -\frac{\theta^2}{2}-\sigma^2-R_{ab}k^ak^b$$
Pure geometry — curvature (by definition) bends geodesic bundles together; no reference to matter, entropy, or Einstein's equations. For a small local patch, the $\theta^2,\sigma^2$ terms drop, leaving area-change proportional to $\int R_{ab}k^ak^b\,dU\,d\mathrm{vol}_{\mathcal S}$.

*Bringing in the still-imported ingredient.* $S=A/4G$ turns area-change into entropy-change, so the entropy side is now also expressed as an integral of Ricci curvature, weighted identically to the energy-side integral from Steps 3–4.

*Matching the two sides.* Since both integrals run over the same patch with the same weighting, for arbitrary field configuration $\phi$ at arbitrary point $p$, their integrands must be proportional: $R_{ab}k^ak^b\propto T_{ab}k^ak^b$ for every null $k^a$ at every point.

*From one null direction to the full tensor equation.* If two symmetric tensors agree contracted against every null vector, they're equal up to a metric-proportional term (undetectable by null vectors). That residual term — the trace/cosmological-constant piece — is pinned down by requiring local conservation of stress-energy ($\nabla^aT_{ab}=0$), which via the contracted Bianchi identity forces the Einstein-tensor combination specifically:

$$R_{ab}-\tfrac12 Rg_{ab}+\Lambda g_{ab} = 8\pi G\langle T_{ab}\rangle$$

*Why universality matters.* The construction never depended on which point or direction was chosen, so the relation holds everywhere and in every direction simultaneously — strong enough to force the full tensorial field equation, not a special-case coincidence.

---

**Synthesis — a third summary, tracing the whole chain in one arc:**

Jacobson noticed a thermodynamic relation, applied to horizons everywhere, spits out Einstein's equations — but needed an entropy that doesn't actually exist as a well-defined QFT quantity.

Every spacetime point, via a boost, has a local horizon attached to it, and that horizon carries its own intrinsic timestamping mechanism (modular flow) which — by Bisognano-Wichmann/Kay-Wald/Summers-Verch — is provably identical to the horizon's own boost symmetry. A coherent state (vacuum, displaced) is the mildest possible way to represent matter crossing the horizon, mild enough that "how different from baseline" (relative entropy) becomes exactly computable rather than approximate. Because the clock is the boost, and the boost has the standard Noether-charge form (energy weighted by position), that computation collapses into a geometric integral — automatically non-negative, as required.

That formula is precisely Jacobson's missing ingredient: boost-weighted heat flux over Unruh temperature equals entropy change, now proven for a rigorously finite quantum quantity rather than assumed for an ill-defined classical one.

Geometry then closes the loop unchanged from 1995: light-ray focusing (Raychaudhuri) plus the still-imported area-entropy law turn the energy-side identity into a curvature statement, and because the match must hold at every point and direction, it's forced into the full Einstein field equation.

Two things are now rigorously proven that weren't before (modular clock = horizon geometry; relative entropy of a coherent excitation = boost-weighted energy flux). One thing is still just assumed, exactly as in 1995: horizon entropy proportional to area. The paper's contribution is narrowing the argument's soft spot from an entire ill-defined entropy down to one specific, nameable, still-debated postulate.
