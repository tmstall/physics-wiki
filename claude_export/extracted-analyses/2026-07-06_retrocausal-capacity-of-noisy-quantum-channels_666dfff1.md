---
source: claude_export
conversation_uuid: 666dfff1-d66e-4f1c-93e0-10cfd5a95203
title: "Retrocausal capacity of noisy quantum channels"
created_at: 2026-07-06T02:18:00.198013Z
updated_at: 2026-07-07T03:23:56.181449Z
tier: A
score: 50
n_messages: 10
---

# Retrocausal capacity of noisy quantum channels

## Human

Analyze this paper

Retrocausal Capacity of a Quantum Channel: Communicating through Noisy Closed Timelike Curves
Kaiyuan Ji
1,2,*, Seth Lloyd
2,†, and Mark M. Wilde
1,‡

Phys. Rev. Lett. 136, 230801 – Published 11 June, 2026

DOI: https://doi.org/10.1103/znyd-npk5

Abstract
We study the capacity of a quantum channel for retrocausal communication, where messages are transmitted backward in time, from a sender in the future to a receiver in the past, through a noisy postselected closed timelike curve mathematically represented by the channel. We completely characterize the one-shot retrocausal quantum and classical capacities, and we show that the corresponding asymptotic capacities are equal to the average and sum, respectively, of the channel’s max-information and its regularized Doeblin information. This endows these information measures with a novel operational interpretation. Furthermore, our characterization can be generalized beyond quantum channels to all completely positive maps. This imposes information-theoretic limits on transmitting messages via postselected-teleportation-like mechanisms with arbitrary initial- and final-state boundary conditions, including those considered in various black-hole final-state models.

Physics Subject Headings (PhySH)
Quantum channels
Quantum communication
Quantum correlations, foundations & formalism
Quantum foundations
Quantum information theory
Quantum protocols
Quantum teleportation
Authorization Required
We need you to provide your credentials before accessing this content.
Log in via your institution
If your institution provides access using Shibboleth/OpenAthens log in.

Log in via APS Member Subscription
If you have a personal subscription through your APS membership please log in.
Starting August 1, 2019 APS member subscribers will need to log in using your member credentials instead of your APS Journal Account.
APS Member Log In
Other Options
Buy Article »
Log in with APS Journals Account
Log in with username/password provided by your institution
Get access through a U.S. public or high school
Supplemental Material (Subscription Required)
References (Subscription Required)
Outline
Information
Purpose Led Publishing - Science is our shareholder
APS Logo

Authors

Reviewers

Librarians

Students

Connect
ISSN 1079-7114 (online), 0031-9007 (print).
©2026 American Physical Society. All rights reserved.
Physical Review Letters™ is a trademark of the American Physical Society, registered in the United States, Canada, European Union, and Japan. The APS Physics logo and Physics logo are trademarks of the American Physical Society. Information about registration may be found here. Use of the American Physical Society websites and journals implies that the user has read and agrees to our Terms and Conditions and any applicable Subscription Agreement.

## Assistant

**Access Status**
Full paper: retrieved from arXiv (2509.08965, main text + full 31-page Supplemental Material)
Abstract: retrieved (APS page paste + arXiv)
Supplementary material: included in the arXiv version
Analysis basis: full text

---

## 1. Punchy Title & One-Sentence Hook

**"How Many Bits Can You Send Yesterday?"** — Ji, Lloyd, and Wilde prove an exact, closed-form Shannon-theoretic limit on sending messages backward in time through a noisy postselected time machine, and the answer turns out to be governed by two previously abstract information measures whose product sets how hard the universe's "retry button" can be pressed.

## 2. Big-Picture Context

**Paper Type & Stakes:** This is a rigorous theoretical quantum Shannon theory paper — a complete capacity theorem for an exotic (hypothetical) communication resource — with a claimed side payoff for black-hole final-state models.

General relativity permits closed timelike curves (CTCs) — worldlines that loop back into their own past — in solutions like Gödel's rotating universe and Gott's cosmic-string spacetimes. Whether nature actually permits them is a separate (and dubious) question, but quantum information theorists have long used CTCs as stress tests: if you *did* have one, what could you compute or communicate? Two rival quantum models exist. Deutsch's model imposes a self-consistency fixed-point condition; the postselected model (P-CTC), championed by Lloyd and collaborators, treats time travel as quantum teleportation where you *postselect* on the Bell measurement succeeding without correction. Noiseless CTCs of either flavor are famously overpowered — perfect discrimination of nonorthogonal states, cloning, collapsing complexity classes.

What nobody had done is the sober engineering question: what if the time machine is *noisy*? Real channels degrade; a noisy P-CTC is modeled as an ordinary quantum channel N whose output lands in the past of its input. The authors define "retrocausal communication" — a sender in the future (they use *Interstellar*'s father-behind-the-bookshelf as the framing device) transmitting to a receiver in the past — and completely characterize its one-shot and asymptotic capacities. The kicker is *which* quantities show up: the channel's **max-information** and its **Doeblin information**, the latter a recently revived quantity (2025, from Wilde's own group) that until now bounded contraction coefficients but lacked a communication-task meaning. The paper also has hidden charm: footnote 58 names the retrocausal capacity the "flux capacity," and reference 64 cites a forthcoming paper by "E. L. Brown, M. McFly, ... October 26, 1985."

For your ongoing quantum gravity thread, the relevant hook is the final section: P-CTCs are mathematically the Horowitz-Maldacena black-hole final-state proposal, and because the authors' theorems hold for *all completely positive maps* (not just trace-preserving channels), they bound information flow in final-state evaporation models with arbitrary boundary conditions.

**Prior Belief Check:** The result *aligns with* the mainstream view that CTCs confer exotic information power, but it *complicates* the folk intuition in a way experts find genuinely interesting: postselection does not make capacity unconditionally unbounded. Noise imposes a hard, exactly computable ceiling — and the ceiling is finite whenever the Doeblin information is finite. Conversely, the capacity diverges as noise vanishes, confirming that noiseless P-CTCs are singular objects. The exactness of the one-shot formula — not bounds, an *equality* with a floor function — is the part specialists would call surprising; closed-form one-shot capacities are nearly unheard of in quantum Shannon theory. Within its subfield this is a substantive advance; as physics, it is strictly conditional on a speculative resource.

**Replication & Convergence Note:** This is a single-group theoretical result (though spanning Cornell and MIT), peer-reviewed at PRL, with no independent verification of the proofs yet; for mathematics of this kind, "replication" means independent checking of the converse and achievability proofs by other quantum Shannon theorists, which matters because subtle errors in nonlinear-map renormalization arguments are easy to make and the field's confidence will rest on that scrutiny over the next year or two.

## 3. Necessary Background Crash-Course

**Postselected teleportation (P-CTC).** Standard teleportation: Alice and Bob share a maximally entangled pair; Alice Bell-measures her half against the message qubit; one of four outcomes occurs; Bob applies a corrective rotation keyed to the outcome. In *postselected* teleportation you keep only the runs where the outcome needing *no correction* occurred, and discard the rest. Conditioned on that outcome, the message appeared at Bob's side "before" Alice measured — the correlations behave as if information flowed backward.

*Analogy:* Branch prediction in a speculative-execution pipeline. The CPU guesses a branch outcome and executes ahead of confirmation; wrong guesses are squashed and retired as if they never happened. Architecturally, committed state only ever reflects the "lucky" timeline.
**Breaks when:** you ask about resource cost. A CPU pays for squashed work in wasted cycles but always makes forward progress; postselection *discards entire experimental runs*, and in standard quantum mechanics the discard probability can be exponentially small — you can't force nature to take the lucky branch. The P-CTC model is precisely the fiction that you can.

**Nonlinearity and renormalization.** Ordinary quantum evolution is linear: channels act on states independently of what the state is. Enclosing a process in a P-CTC divides by the postselection success probability (you renormalize over surviving runs), and that denominator *depends on the input state*. This nonlinearity is the engine of everything exotic here.

*Analogy:* Importance sampling. You reweight surviving samples by the inverse of their survival probability, so rare-but-desired events dominate the renormalized distribution far beyond their raw frequency.
**Breaks when:** you push on causality bookkeeping. In Monte Carlo you, the simulator, stand outside the sampled world doing the reweighting. In a P-CTC the reweighting is supposed to be *physically instantiated inside* the dynamics — that's exactly the step with no known physical mechanism.

**Max-information and Doeblin information.** Both are properties of a channel's Choi state (the state you get by feeding half of a maximally entangled pair through the channel). Max-information asks: what's the smallest factor λ by which a "useless" replacement channel (one that throws away input and outputs a fixed state) must be scaled to dominate this channel from *above*? Doeblin information asks the mirror question from *below*: how much useless channel is hiding *inside* this channel? A channel with high max-information is very far from useless at its best; a channel with high Doeblin information has almost no useless component at its worst. Crucially (Lemma 1 in the paper), they equal the log of the **maximum** and (negative log of the) **minimum** achievable *singlet fractions* — the best and worst overlap with a perfect entangled pair that any decoder can arrange after the channel acts.

*Analogy:* Eye-diagram margins on a serial link. Max-information is like the best-case eye opening a good equalizer can recover; Doeblin information measures how far the *worst* deliberately mistuned equalizer can slam the eye shut. One quantifies achievable signal integrity, the other quantifies achievable signal *destruction*.
**Breaks when:** you treat them as symmetric roles in ordinary communication — in conventional Shannon theory only the "best case" matters. Here the worst case matters equally, because (next section) the protocol needs to make a failure branch maximally *suppressible*.

**Central analogy for this paper:** *the causal loop rigs the teleportation lottery.*

## 4. Core Technical Explanation

**The setup.** The father (future) and daughter (past) are connected by a noisy P-CTC represented by channel N from system A (fed in by the father) to system B (received by the daughter, earlier). Their strategy is a pair of ordinary quantum channels: the daughter's decoder D, and the father's encoder E. The distinctive ingredient: the daughter, being in the past, can leave a **noiseless quantum memory L** for the father to pick up later. Memory forward in time plus P-CTC backward in time closes a loop. The authors show (Remark 2, Supplemental) this is mathematically identical to *forward* communication through N assisted by a *noiseless* P-CTC — a nice duality: it's the ordinary channel plus the loop, and you can slide which segment you call "the time machine" around the cycle.

They then define capacities the standard Shannon way: the one-shot retrocausal quantum capacity is the most qubits transmissible with worst-case infidelity at most ε; asymptotic capacity is the rate over many parallel uses. The main theorem gives an exact answer.

The sentence before the key equation: the one-shot quantum capacity is exactly

$$Q^{\varepsilon}_{\mathrm{retro}}(\mathcal{N}) = \log_2\!\left\lfloor \sqrt{\tfrac{\varepsilon}{1-\varepsilon}\, 2^{\,I_{\max}(\mathcal{N}) + I_{\mathrm{doe}}(\mathcal{N})}} + 1 \right\rfloor$$

Symbol definitions:
- $Q^{\varepsilon}_{\mathrm{retro}}$ : max qubits sendable backward in one channel use, tolerating infidelity $\varepsilon$
- $I_{\max}(\mathcal{N})$ : the channel's max-information (log of the best achievable singlet fraction, up to dimension factors)
- $I_{\mathrm{doe}}(\mathcal{N})$ : the channel's Doeblin information (negative log of the worst achievable singlet fraction)
- $\lfloor \cdot \rfloor$ : floor function — message dimensions are integers, and the formula is exact enough that the floor matters

What this actually means: the number of *messages* (not qubits — square the count for the classical version, which drops the square root) grows with the product of two things: your noise tolerance ratio, and $2^{I_{\max}+I_{\mathrm{doe}}}$ — the **ratio of best-case to worst-case singlet fraction**. That ratio is the total dynamic range of the channel: how well it can preserve entanglement when you help it, divided by how badly it can be made to mangle entanglement when you sabotage it. The classical asymptotic capacity is simply $I_{\max} + I^{\infty}_{\mathrm{doe}}$ (sum), and the quantum capacity is half that (average) — the familiar factor-of-2 between bits and qubits under dense-coding-like resources.

**The optimal strategy — amplified probabilistic teleportation — is the conceptual heart.** Here's what they actually do, and it's cleaner than you'd guess:

1. The daughter (past) doesn't try to decode anything from B directly. She prepares a fresh maximally entangled pair between her output register and memory L₁, stashes the raw channel output B untouched in memory L₂, and leaves both memories for the father.
2. The father (future) Bell-measures his message against L₁ — ordinary *probabilistic* teleportation. Success (no correction needed) has raw probability 1/d², where d is the message dimension. He gets a flag k: success or failure.
3. Conditioned on k, he applies one of two channels to L₂ and feeds the result into the P-CTC entrance. On success (k = 0), he applies the channel that **maximizes** the singlet fraction of the loop; on failure (k = 1), the channel that **minimizes** it.

The loop's postselection renormalizes probabilities in proportion to each branch's amplitude for surviving the final entangled-state projection. By making the success branch loop-friendly and the failure branch loop-hostile, the father reweights the lottery: the renormalized success probability gets multiplied by up to the best/worst singlet-fraction ratio, i.e., $2^{I_{\max}+I_{\mathrm{doe}}}$. The message never travels through the noisy channel at all — it teleports through the noiseless memory. The noisy channel serves purely as the *amplification medium* whose dynamic range powers the retry-rigging.

*Analogy:* it's retry-until-success where the retries are free and invisible. Like a link-layer protocol where NACKed packets are not retransmitted but *erased from history*, and the ACK probability gets renormalized over surviving history. The channel quality doesn't limit what a surviving packet carries — it limits how aggressively history can be pruned.

The converse proof is a clean sandwich argument: any channel is squeezed between λ·(replacement channel) from above and (1/μ)·(replacement pseudo-channel) from below, replacement channels are provably useless inside any loop (Lemma 3 — a time machine that outputs a fixed state teaches you nothing about the future), and chaining the two inequalities through the fidelity and error conditions forces d² ≤ ελμ/(1−ε) + 1. Optimizing λ and μ gives exactly the max- and Doeblin informations. Achievability and converse meet: an exact result.

**Assumption Audit**

**Watch:** Reader likely assumes the message is encoded into the system that traverses the time machine. The paper actually shows the optimal protocol *never* sends the message through the noisy channel — it teleports it through the noiseless memory, and the noisy P-CTC only powers the probability amplification loop.

**Watch:** Reader likely assumes the daughter's memory L is bookkeeping. The paper actually says it's load-bearing: without memory retrieval, the setting collapses mathematically to conventional forward communication, and the entire capacity advantage (including exceeding entanglement-assisted capacity, and divergence at low noise) evaporates.

**Watch:** Reader likely assumes "capacity" here has the usual coding-theoretic texture — long block codes, typicality, decoders. The paper actually achieves the one-shot optimum with a *fixed, structurally trivial* strategy plus two optimized channels found by semidefinite programming; there is no error-correcting code in the conventional sense anywhere.

**Watch:** Reader likely assumes a PRL titled "communicating through closed timelike curves" is making a claim about physics. The paper actually states explicitly that these capacities apply only *within* the P-CTC model and imply no backward signaling in standard quantum theory — the physical existence of the resource is assumed, not argued.

## 5. What's Genuinely New or Clever

**New to the field (1): an exact one-shot capacity formula.** Quantum Shannon theory almost never produces closed-form one-shot capacities — the norm is upper/lower bounds meeting only asymptotically with smoothing parameters. An equality, with a floor function, valid at every ε, achieved by an explicit strategy, is a rarity, and it hands the max- and Doeblin informations their first genuine communication-task operational meaning (the Doeblin coefficient literature is barely a year old as a quantum object; this gives it teeth).

**New to the field (2): the amplification mechanism itself.** The insight that a noisy P-CTC's communication value is the *dynamic range* between the best and worst singlet fractions — that you exploit a time loop not as a conduit but as a branch-reweighting engine, with the "bad" channel direction being just as much a resource as the "good" one — is a genuinely new way to think about postselected resources. The extension of all theorems to arbitrary completely positive maps (not just trace-preserving ones) is what buys the black-hole final-state applicability, since Gottesman-Preskill-type generalized boundary conditions produce exactly such non-trace-preserving maps.

## 6. Limitations & Open Questions

**P-CTCs may simply not exist, and "experimental simulation" is weaker than it sounds.** Simulations via postselection reproduce conditional statistics; they do not instantiate nonlinear dynamics. Whether the model describes anything physical is unresolved, and prominent critiques (Bennett–Leung–Smith–Smolin's "preparation problem" line) argue the exotic power is an artifact of conflating proper and improper mixtures. **(B) Contested** — the paper cites this debate ([20–22]) without resolving it, and reasonable physicists split on whether P-CTC capacities describe anything at all. (broader literature)

**The Doeblin information is nonadditive in general, so the asymptotic capacity needs regularization.** For measurement channels and highly symmetric (mictodiactic covariant) channels it single-letterizes and is SDP-computable; for general channels only sandwich bounds exist and efficient computability of the regularized quantity is unknown. **(A) Consensus** — the paper states this limitation explicitly and it mirrors the standard regularization plague of quantum Shannon theory. (paper, Remark 6)

**The noiseless-memory assumption is idealized.** The entire protocol leans on the daughter's memory surviving decades (in the framing story) with zero decoherence. The paper poses the noisy-memory tradeoff [their Eq. (13)] as an open problem, and I'd expect the capacity to degrade sharply, since the memory carries the actual message. **(A) Consensus** — flagged by the authors themselves as the natural next question. (paper, Discussion)

**Model dependence: none of this transfers to Deutschian CTCs.** D-CTCs decorrelate the time traveler from its environment, so partial entangled states can't traverse; the capacities here are P-CTC-specific. A reader wanting model-independent statements about "time machines" gets none. **(A) Consensus** — stated in the paper. (paper, Retrocausal capacity section)

**The black-hole payoff is promissory.** The final-state-model implications are asserted via the CP-map generalization but their physical interpretation (what does "retrocausal capacity of black hole evaporation" bound, observationally or even conceptually?) is deferred to future work — reference [64], which is currently a Back to the Future joke. Whether this yields real insight into the information paradox, or is a formal correspondence, is unestablished. **(C) Speculative** — I'm judging the depth of an application the authors have not yet written; specialists in final-state models may see more or less here than I do. (analyst inference)

## 7. Detailed Summary & Explanation

The paper asks how efficiently messages can be sent backward in time through a *noisy* postselected closed timelike curve, modeled as a quantum channel whose output lies in the past of its input. The scenario allows the receiver in the past to leave a noiseless quantum memory for the sender in the future, and this closes a causal loop: what the receiver decodes can influence how the sender encodes, which determines what the receiver decodes. Within the postselected model, such loops are consistent, and the authors show they are the entire source of the setting's power — forbid the memory and everything reduces to ordinary communication.

The main theorem gives exact one-shot capacities. In plain language: the number of distinct classical messages transmissible with error at most epsilon equals (up to rounding down) one plus the noise-tolerance ratio times a channel-dependent amplification factor. That amplification factor is the ratio between the best possible and worst possible entanglement-preservation of the channel — how well a cooperating decoder can preserve a maximally entangled pair through it, divided by how badly an adversarial decoder can wreck one. These two extremes are the operational content of the max-information and Doeblin information respectively. The quantum capacity is the square root of the same expression in message-count terms, giving asymptotic rates equal to the average (quantum) and sum (classical) of the two information measures.

The optimal protocol is elegantly perverse. The message is teleported to the past through the noiseless memory via ordinary probabilistic teleportation, which succeeds with tiny raw probability. The noisy time machine is then used *only* to rig the odds: on the success branch the sender drives the loop through the channel's most entanglement-friendly configuration; on the failure branch, through its most entanglement-hostile one. Postselection renormalizes probabilities in favor of loop-friendly branches, so failure histories are almost entirely pruned away. The channel's noise level sets how much pruning is possible — that is the physical meaning of the capacity formula, and why capacity diverges to infinity as noise vanishes (a noiseless P-CTC can amplify the success probability without bound, recovering the known pathologies of ideal CTCs).

Why frame the summary this way? The interpretive choice is to foreground the *mechanism* (lottery-rigging via branch reweighting) rather than the formula, because the formula's structure — a sum of two dual information quantities — is opaque until you see that one measures the ceiling and the other measures the floor of the same physical quantity, entanglement survival. The second interpretive choice is to keep the result firmly conditional: this is mathematics about a model, rigorously peer-reviewed as mathematics, and its physics content depends entirely on whether postselected time loops (or their black-hole final-state cousins) describe nature.

**Where I'm least confident in this analysis:** the converse proof's handling of the nonlinear renormalization — specifically why sandwiching by replacement maps survives the state-dependent denominator without loopholes — is the place where my plain-language rendering compresses a genuinely delicate argument (Supplemental Sec. V.A), and where I'd most recommend independent verification; I've verified the logical skeleton but not line-audited the operator inequalities, and I'm also least certain about how much physical content the final-state-model generalization ultimately carries.

## 8. Three Crystallized Takeaways

1. **A noisy time machine has an exactly computable bandwidth backward in time** — and it's set by the ratio of the best to worst entanglement survival through the channel, not by anything resembling ordinary channel capacity.

2. **The message never travels through the time machine.** The optimal protocol teleports it through an ordinary memory and uses the time loop purely as a probability amplifier that erases failure histories — postselection as retry-until-success with the retries deleted from reality.

3. **Even hypothetical time travel obeys Shannon-style limits:** noise tames the legendary pathologies of closed timelike curves, with infinite capacity recovered only in the strictly noiseless limit — and the same math bounds information escape in black-hole final-state models.

## 9. Shorter Summary

General relativity's equations permit closed timelike curves — paths that loop into their own past — and quantum theorists have long studied a "postselected" model of them, where time travel works like quantum teleportation conditioned on always getting the lucky measurement outcome. Ideal versions are absurdly powerful: they can clone quantum states and crack hard computations. This paper asks the sober follow-up: what if the time machine is noisy, degrading whatever passes through it like a static-ridden phone line?

Ji, Lloyd, and Wilde prove an exact formula for how many bits or qubits can be sent from the future to the past through such a noisy loop. The answer depends on the noise via two quantities: how well the channel can preserve quantum entanglement when everything cooperates, and how thoroughly it can destroy entanglement when deliberately sabotaged. The ratio of these two extremes — the channel's dynamic range — sets the backward-in-time bandwidth. Less noise means a bigger ratio; as noise vanishes, capacity blows up to infinity, recovering the old pathological results.

The optimal strategy is a beautiful trick. The sender doesn't push the message through the time machine at all. Instead, the receiver in the past leaves behind an ordinary quantum memory; the sender teleports the message through that memory, a process that normally succeeds only rarely. The time loop is then used solely to rig the lottery: histories where teleportation failed get almost entirely erased by the loop's postselection, while success histories survive. The noise level determines how aggressively failure can be pruned.

The authors are careful about what this does and doesn't mean: nothing here permits backward signaling in standard quantum mechanics. It is a rigorous limit theorem *within* a speculative model. Its most intriguing spillover is that the same mathematics governs "final-state" models of black-hole evaporation — proposals for rescuing information from black holes that secretly have the same structure as postselected time travel — so these results bound information flow there too, a connection the authors promise to develop in future work.

(348 words)

---

Two small delights worth noting: the authors name the retrocausal capacity the "flux capacity" in footnote 58, and reference 64 — the promised final-state follow-up — is attributed to "K. Ji, E. L. Brown, S. Lloyd, M. McFly, and M. M. Wilde, October 26, 1985." This also connects to your Thread A-adjacent territory: Horowitz-Maldacena is essentially postselected teleportation at the singularity, so if you want, a future session could unpack final-state models against the island-formula picture you've already built.

## Human

Explain Nonlinearity and renormalization. Ordinary quantum evolution is linear: channels act on states independently of what the state is. Enclosing a process in a P-CTC divides by the postselection success probability (you renormalize over surviving runs), and that denominator depends on the input state. This nonlinearity is the engine of everything exotic here.

## Assistant

Explaining

This is the right thing to zoom in on — it's the load-bearing wall of the whole subject. Let me build it up in layers.

**Why ordinary quantum mechanics is linear**

A quantum channel is a linear map: if you feed it a 50/50 mixture of state ρ and state σ, the output is exactly the 50/50 mixture of channel-of-ρ and channel-of-σ. The channel processes each "ingredient" independently and never asks what else is in the blend. This is not an aesthetic choice — it's what protects causality and no-cloning. A nonlinear evolution would let you distinguish a proper mixture ("I flipped a coin and prepared ρ or σ") from an improper one ("this is half of an entangled pair"), and that distinction is exactly the crack through which faster-than-light signaling leaks.

Computer-architecture version: linearity is like a stateless pipeline stage. The ALU computes f(x) for whatever x arrives; it doesn't behave differently depending on the statistical distribution of the workload. Every input transaction is processed on its own terms.

**Where the division comes from**

Now enclose a process in a P-CTC. Mechanically, a P-CTC is: (1) create a maximally entangled pair spanning "past" and "future" ends of the loop, (2) run your dynamics, (3) at the end, project onto that same entangled state and *keep only the runs where the projection succeeds*.

Step 3 is a measurement with a yes/no outcome. Conditioning on "yes" means your final state is (projected state) divided by Prob(yes) — that's just Bayes' rule in quantum dress. Every conditional state in quantum mechanics has this normalization denominator; nothing exotic yet. What makes the P-CTC different is that you declare the conditioning to be *part of the dynamics itself*. The time machine, by fiat, only ever produces the "yes" branch. So the effective evolution of the system is:

$$\rho \;\mapsto\; \frac{\Pi\, \mathcal{E}(\rho)\, \Pi}{\mathrm{Tr}[\Pi\, \mathcal{E}(\rho)]}$$

Symbol definitions:
- $\rho$ : the input state you feed in
- $\mathcal{E}$ : the ordinary (linear) dynamics inside the loop
- $\Pi$ : the projector onto the entangled boundary condition — the "did the loop close consistently?" test
- $\mathrm{Tr}[\Pi\,\mathcal{E}(\rho)]$ : the probability that the loop closes, **which depends on ρ**

What this actually means: the numerator is honest linear quantum mechanics. All the trouble lives in the denominator. Because Prob(yes) depends on the input, different inputs get rescaled by *different* amounts. Feed in the 50/50 blend of ρ and σ and the output is no longer the 50/50 blend of the individual outputs — it's a *reweighted* blend, tilted toward whichever ingredient was better at surviving the postselection. The map now cares about the whole ensemble, not each ingredient in isolation. That's the definition of nonlinearity.

**Why this is an engine for exotica**

Once the map can reweight, you can *design* the reweighting. Suppose branch A of your protocol closes the loop with probability 0.9 and branch B with probability 0.001. In standard QM, if branch B occurs 99% of the time, you're stuck with it 99% of the time. Inside a P-CTC, the surviving-history statistics renormalize to roughly (0.01 × 0.9) versus (0.99 × 0.001) — branch A now dominates about 9-to-1 despite being rare. You've amplified a 1% event into a ~90% event by making its competitor loop-hostile.

That's precisely the retrocausal protocol from the paper: teleportation success is the rare branch A; the father deliberately makes the failure branch B maximally loop-hostile (worst singlet fraction) and the success branch maximally loop-friendly (best singlet fraction). The amplification factor is the ratio — and the ratio is $2^{I_{\max}+I_{\mathrm{doe}}}$. Noise caps the ratio, and that's the entire capacity theorem in one sentence: **noise limits how unfairly the loop can reweight histories.** The same trick, uncapped, is what lets ideal P-CTCs distinguish nonorthogonal states and solve PP-complete problems: you amplify exponentially unlikely "lucky guess" branches to certainty.

Analogy: it's a load balancer that drops requests instead of queuing them, where you control each backend's drop rate. If server A drops 0.1% of traffic and server B drops 99.9%, then *among completed requests* nearly everything went through A — regardless of how the incoming traffic was actually distributed. The completed-request log tells a statistical story wildly different from the arrival log. The P-CTC declares that only the completed-request log physically exists.

**Breaks when:** you ask who pays for the dropped requests. The load balancer physically received and discarded them — real packets, real time, real energy. In experimental "simulations" of P-CTCs, the discarded runs likewise really happened and were thrown out in classical post-processing, which is why simulations only reproduce conditional statistics and don't instantiate nonlinear dynamics. The P-CTC model asserts the failed branches never occur at all, and no known physical mechanism performs that erasure. This is also exactly the Bennett-Leung-Smith-Smolin objection I tagged (B) Contested in the analysis: they argue the "power" is an artifact of doing statistics on a conditioned ensemble and then talking as if it were dynamics.

One last connection to your quantum gravity thread: this denominator is the same object that appears in Horowitz-Maldacena. Imposing a final-state boundary condition at the black hole singularity is imposing Π, and the state-dependence of the normalization is the source of the model's known tension with unitarity for infalling observers. When the paper says its theorems extend to all completely positive maps "with arbitrary boundary conditions," it's saying: however you rig Π and the interior dynamics, the reweighting power — and hence the information flow — obeys the same max-information/Doeblin-information budget.

## Human

Don't you mean that Branch a is a low probability such as like 1 instead of 0.9? Suppose branch A of your protocol closes the loop with probability 0.9 and branch B with probability 0.001. In standard QM, if branch B occurs 99% of the time, you're stuck with it 99% of the time. Inside a P-CTC, the surviving-history statistics renormalize to roughly (0.01 × 0.9) versus (0.99 × 0.001) — branch A now dominates about 9-to-1 despite being rare.

## Assistant

Clarifying

Good catch — you've spotted a real ambiguity in how I wrote it, though the arithmetic is actually intended. The trouble is that **each branch has two different probabilities**, and I used one for A in the setup sentence and the other for A in the renormalization, without ever labeling them. They're not in conflict; they describe different things.

The two probabilities per branch:

| Branch | Prior: how often it *occurs* | Loop-closing: how well it *survives* postselection |
|---|---|---|
| A (teleport succeeded) | 0.01 — **rare** | 0.9 — loop-friendly (rigged high) |
| B (teleport failed) | 0.99 — **common** | 0.001 — loop-hostile (rigged low) |

Your instinct is correct: **branch A is the low-probability branch — 1%, i.e. 0.01.** That's the *prior*, and it's exactly the "teleportation succeeds only rarely (1/d²)" fact from the protocol. So when I wrote "(0.01 × 0.9)" for A, the 0.01 is that rare prior. You were right to expect a small number there.

The **0.9** is a *different* quantity: given that you're in branch A, how likely the loop closes consistently (the postselection succeeds). The father *designs* this to be high by steering branch A through the channel's most entanglement-friendly configuration. Likewise he designs branch B's loop-closing probability to be tiny (0.001) by steering it through the most hostile configuration.

So the full story for each branch is: **(how often it happens) × (how well it survives the loop).**
- A: 0.01 × 0.9 = 0.009
- B: 0.99 × 0.001 = 0.00099
- Renormalized: A ≈ 90%, B ≈ 10% — about 9-to-1.

The whole point is that A is rare *and* A survives the loop, while B is common *but* dies in the loop. Postselection multiplies each branch's occurrence rate by its survival rate and then renormalizes, so a 1% event that survives well beats a 99% event that survives terribly.

Where my wording misled you: the sentence "branch A closes the loop with probability 0.9" was describing the *survival* number, but sitting right next to "branch B occurs 99% of the time" (an *occurrence* number), so it read as if 0.9 were A's occurrence rate — making A look common, contradicting the "despite being rare" tag. Two different columns of the table above, collapsed into one sentence. The amplification factor in the real theorem, $2^{I_{\max}+I_{\mathrm{doe}}}$, is precisely the maximum ratio between those loop-closing (survival) probabilities that the channel's noise allows.

## Human

Explain The father (future) and daughter (past) are connected by a noisy P-CTC represented by channel N from system A (fed in by the father) to system B (received by the daughter, earlier). Their strategy is a pair of ordinary quantum channels: the daughter's decoder D, and the father's encoder E. The distinctive ingredient: the daughter, being in the past, can leave a noiseless quantum memory L for the father to pick up later. Memory forward in time plus P-CTC backward in time closes a loop. The authors show (Remark 2, Supplemental) this is mathematically identical to forward communication through N assisted by a noiseless P-CTC — a nice duality: it's the ordinary channel plus the loop, and you can slide which segment you call "the time machine" around the cycle.

## Assistant

Explaining

The geometry here is a circle, and the paragraph is describing how it's stitched together before Remark 2 tells you the circle has no privileged starting point.

**The two arcs.** There are two links connecting father and daughter, running in opposite time directions. The noisy channel N is the *backward* arc: the father feeds system A in the future, and N deposits system B in the daughter's past. That's the time machine — information flowing future→past. The quantum memory L is the *forward* arc: the daughter, living earlier, writes something into a durable register and just... waits for the father to read it decades later. Ordinary storage, past→future, no exotic physics. One arc goes back, one arc goes forward, and together they close a ring.

**Why it's a genuine loop and not just two messages.** Trace the dependency around the ring. What the daughter decodes (via D) determines what she writes into memory L. The father reads L and lets it condition his encoding E. His encoding determines what he feeds into the P-CTC. The P-CTC carries that back to become the B the daughter receives — which is what she decodes in the first place. The output of the cycle feeds its own input. That's a causal loop, and it only makes sense if the whole thing is *self-consistent*: the state going around must be a fixed point. The P-CTC's job is to enforce exactly that consistency — the postselection projector Π from the previous discussion is precisely the "did the loop close on itself coherently?" condition. Runs where it didn't close are discarded; what survives is a consistent loop.

**Remark 2 — sliding the label.** Now the key observation. A closed ring has no objective "first" segment. You, the analyst, *chose* to call the backward arc (N) "the time machine" and the forward arc (memory L) "ordinary storage." But you could equally walk around the same ring and re-designate: call N an ordinary *forward* channel that the father uses in the normal time direction, and call the *memory arc* the time machine — a noiseless P-CTC. Nothing about the physical loop changed; you only moved the label for which segment counts as "the CTC." Under that relabeling, the problem reads: *forward communication through N, assisted by a noiseless P-CTC.* Same joint state, same consistency condition, same everything — just described from a different seat on the ring.

**Why this duality earns its keep.** It's what lets ordinary channel quantities do the work. In the retrocausal framing, N is a weird backward object and it's not obvious what "capacity" even means. In the dual framing, N is a bog-standard forward channel, and you're asking how much a *noiseless* time loop boosts your ability to communicate through it. That's a question you can attack with familiar tools — and the answer comes out in terms of N's max-information and Doeblin information, which are properties of N used the normal way. The duality is the bridge that turns "capacity of a time machine" into "ordinary channel, extraordinary side resource."

Analogy (feedback loop / ring interconnect): think of a retiming feedback loop or a ring oscillator. In a closed loop of logic-plus-registers, which element you call "the delay stage" and which you call "the combinational block" is a bookkeeping choice — the loop's steady state is whatever's a fixed point of going all the way around, and every valid labeling has to agree on that same fixed point. The loop doesn't know where you drew the boundary.

**Breaks when:** you push the symmetry too hard and forget the two arcs aren't physically interchangeable in *quality*. The memory arc is stipulated noiseless; N is noisy. So while you can freely relabel which arc is "the time machine," you can't swap their noise properties — the whole capacity theorem lives in the asymmetry that one arc is perfect and the other degrades. The relabeling is a change of description, not a claim that a noisy memory and a noisy channel would play identical roles.

One thing worth flagging since it connects to the earlier point: this equivalence is about the *setting*, and holds regardless of what protocol you run. It's separate from the later result that the *optimal* protocol teleports the message through the noiseless memory and uses N only for amplification. Remark 2 is the structural stage-setting; the optimal-protocol claim is a result proved on top of it.

## Human

Need help understanding The optimal strategy — amplified probabilistic teleportation — is the conceptual heart

## Assistant

Explaining

This is where the two threads you've been pulling — probabilistic teleportation and loop-reweighting — get braided into one move. The name says it: **amplified** (the reweighting engine) **probabilistic teleportation** (the message-transport primitive). Let me take them in that order and then show why bolting them together is not just clever but provably optimal.

**The primitive: probabilistic teleportation**

Ordinary teleportation is *deterministic*. Alice Bell-measures, gets one of d² outcomes, and Bob applies a correction keyed to the outcome. It always works because every outcome has a fix.

Probabilistic teleportation throws away the fixes. You keep only the single outcome that needs *no correction* — the identity outcome — and on every other outcome you declare failure and raise a flag. For a message of dimension d, that clean outcome has raw probability 1/d². When it fires, the message lands on the far side pristine, with nothing to undo. When it doesn't, you don't patch it — you just record "failed."

Why deliberately cripple teleportation this way? Because in this setting you don't *want* corrections. Corrections would smear the message across the measurement outcome, entangling "what was sent" with "which branch happened." What you want instead is a clean binary flag — *success* or *failure* — that you can then treat differentially. The whole strategy needs a crisp two-way fork it can route through two different loop configurations. Probabilistic teleportation manufactures exactly that fork.

*Analogy:* a transporter that only completes when the quantum handshake returns clean, and otherwise aborts with an error code rather than trying to reconstruct a garbled signal. You've traded reliability for a trustworthy success/fail signal.
**Breaks when:** you assume aborting is cheap. Raw success is 1/d² — for any decent-sized message alphabet, the transporter almost always aborts. On its own this primitive is nearly useless. That's the problem the amplifier exists to solve.

**The problem, stated sharply**

Left alone, probabilistic teleportation gives you a rare success drowning in common failures. If you want to send one of d messages, you need d to be large, but success scales as 1/d² — the bigger the alphabet, the rarer the clean handshake. Something has to rescue the rare branch.

**The amplifier: rig the loop so success dominates**

This is precisely the reweighting mechanism from three messages ago, now aimed at the teleportation flag. Conditioned on the flag k:

- **Success (k=0):** the father steers the loop through the channel's *most entanglement-friendly* configuration — the one achieving the **maximum** singlet fraction. This branch closes the P-CTC loop with high probability.
- **Failure (k=1):** he steers it through the *most entanglement-hostile* configuration — **minimum** singlet fraction. This branch is loop-poison; postselection prunes it.

The loop's postselection then multiplies each branch's occurrence rate by its survival rate and renormalizes. The rare-but-loop-friendly success branch gets boosted; the common-but-loop-hostile failure branch gets erased. The boost factor is capped by the channel's dynamic range — the ratio of best to worst singlet fraction, which is exactly $2^{I_{\max}+I_{\mathrm{doe}}}$.

Now you can see the whole capacity theorem as a tug-of-war. Sentence before the equation: the number of distinguishable messages is limited by whether the amplification can overcome the teleportation handicap, which the converse pins down as

$$d^{2} \;\le\; \frac{\varepsilon}{1-\varepsilon}\,\lambda\mu \;+\; 1$$

Symbol definitions:
- $d$ : number of message values you're trying to send
- $d^2$ : the teleportation handicap — inverse of the raw success probability $1/d^2$
- $\lambda\mu$ : the amplification budget, equal to $2^{I_{\max}+I_{\mathrm{doe}}}$ — best singlet fraction times inverse worst singlet fraction
- $\varepsilon$ : tolerated infidelity — your willingness to accept residual failure sets how hard you can push

What this actually means: on the left, the penalty for wanting a big alphabet (harder clean handshake). On the right, how much the loop can amplify to compensate, scaled by how much error you'll tolerate. Solve for d, take the floor, and you have the exact capacity formula from the analysis. The $1/d^2$ teleportation penalty and the $2^{I_{\max}+I_{\mathrm{doe}}}$ amplification are the two forces; noise sets the amplifier's ceiling.

*Analogy:* retry-until-success where the retries are deleted from history — applied to a transporter's abort flag. You can only "retry away" the aborts as fast as the channel's dynamic range permits; a noisier channel gives a weaker retry button, so you must shrink the alphabet to keep the clean-handshake rate manageable.

**The load-bearing subtlety: the message never touches N**

Here's the part that catches everyone. The message rides the *noiseless memory* teleportation (through L₁). The noisy channel N is not the message's conduit at all — it's purely the amplification medium. Its noise doesn't corrupt the message; it *limits how aggressively the failure branch can be pruned.* This is why the capacity depends on N only through its singlet-fraction extremes (max- and Doeblin information) and not through, say, its coherent information the way an ordinary channel's capacity would. N is being used as a probability pump, not a pipe.

This is also why, back in the Assumption Audit, I flagged that killing the memory collapses everything to conventional forward communication: without the noiseless memory arc, the message would have no choice but to travel through N itself, and you'd lose both the amplification structure and the clean success/fail fork it feeds.

**Why this is optimal, not just good**

The inequality above is a *converse* — it holds for every conceivable protocol, derived from the replacement-map sandwich argument (any channel is trapped between λ·useless from above and (1/μ)·useless from below, and useless channels teach a loop nothing). Amplified probabilistic teleportation *saturates* it: the construction hits the bound exactly. Achievability meets converse, so this isn't merely a clever scheme that works well — it's the scheme, and the floor function in the final formula is the only slack left (message counts must be integers). That coincidence of a structurally trivial protocol with the information-theoretic optimum is the paper's quiet flex: no block codes, no typicality, no decoder — just probabilistic teleportation plus two SDP-optimized channels, and you've already reached the ceiling.

Quick synthesis of the arc you've been building across these questions: **nonlinearity** gives the loop the power to reweight histories; the **memory-plus-CTC ring** gives you a place to stand where an ordinary channel's quantities apply; and **amplified probabilistic teleportation** is the specific move that cashes both in — teleport clean through the perfect arc, then spend the noisy arc's entire dynamic range rigging the lottery in the clean branch's favor.
