---
source: claude_export
conversation_uuid: e23e36e1-74fb-4613-b836-82a4bd918ec8
title: "The Universe's Gas Pedal Is a Leaky Engine"
created_at: 2026-06-25T16:58:11.941129Z
updated_at: 2026-06-25T17:01:02.831363Z
tier: A
score: 251
n_messages: 2
---

# The Universe's Gas Pedal Is a Leaky Engine

## Assistant

**Access Status**
Full paper: retrieved from inline document paste (PRL, published 8 June 2026)
Abstract: included
Supplementary material: appendices A–D included in paste
Analysis basis: full text

---

## §1 — Punchy Title & One-Sentence Hook

**The Universe's Gas Pedal Is a Leaky Engine: Gravity as a Heat Cycle with an Escape Valve**

If spacetime geometry is just thermodynamics in disguise, then the near-perfection of that disguise — local Lorentz invariance, energy conservation — is itself a physics result, not an axiom, and the small imperfection produces exactly the late-time cosmic acceleration we observe.

---

## §2 — Big-Picture Context

**Paper Type & Stakes:** This is a theoretical framework paper in the thermogravity tradition — it doesn't do new observations, doesn't fit new data, but proposes a mechanistic origin for dark energy and Lorentz violation simultaneously from a single thermodynamic extension of emergent gravity. The stakes are high if correct: it would dissolve two of the hardest problems in modern cosmology (the cosmological constant problem and the origin of dark energy) by deriving them from the same microstructural assumption.

The emergent-gravity program starts from a remarkable coincidence first identified by Jacobson in 1995: if you treat local horizons as thermodynamic objects — assigning them entropy proportional to area and temperature proportional to surface gravity — then the demand that entropy and energy balance correctly across those horizons *is* the Einstein equations. Gravity, on this view, isn't a fundamental force written into an action principle; it's an equation of state, the macroscopic residue of microscopic spacetime degrees of freedom, much as fluid dynamics emerges from molecular collisions without needing a "fluid force."

The persistent question haunting this program is whether it's merely a rewriting — a tautology that tells you Einstein is thermodynamically consistent but nothing new — or whether it can be a *generative* framework producing theories GR cannot reach. This paper argues for the latter by noticing something structurally odd: the standard thermogravity derivation of GR uses only heat (energy flowing across horizons at temperature T with entropy S), with no work terms. Real thermodynamic systems generically do work. What happens if you allow it?

The answer the authors find is that adding work terms — specifically, chemical-potential-type contributions from a conserved "number" of microscopic spacetime constituents — forces controlled violations of local Lorentz invariance and breaks energy-momentum conservation in a precise, controlled way. The violation is suppressed by the extreme inefficiency of the resulting thermodynamic cycle, which is why GR works so well locally; but at cosmological scales and late times, the small leak accumulates into the observed accelerated expansion. This reframes the cosmological constant problem: the question isn't "why is Lambda so small?" but "why is the Otto cycle so inefficient?" — and the answer is structural rather than fine-tuned.

**Prior Belief Check:** This result runs against the grain in two directions simultaneously. In the emergent-gravity community, most practitioners accept that the framework reproduces GR (and some extensions) but are skeptical it can generate genuinely *new* physics beyond what can be expressed in an action principle — the "tautology" worry. This paper directly challenges that skepticism and will be contested. In the dark energy / cosmological constant community, the mainstream view is that any viable model needs to fit the full CMB + BAO + supernova dataset self-consistently; the authors explicitly defer this to future work, which will draw criticism. The result is *not* surprising in the sense of contradicting known observations — it's designed to produce acceleration compatible with them — but it is genuinely surprising to experts in proposing that Lorentz violation and dark energy are the *same* phenomenon, stemming from the same thermodynamic generalization.

**Replication & Convergence Note:** This is a single-group theoretical result with no independent derivation or phenomenological confirmation yet. Independent confirmation would require either (a) a different group deriving the same equations of state from a different microscopic model of spacetime constituents, or (b) observational discrimination of the predicted acceleration profile from ΛCDM using supernova or BAO data. Neither exists at time of publication.

---

## §3 — Necessary Background Crash-Course

**Emergent gravity and the Jacobson derivation**

The central idea is that Einstein's equations aren't fundamental laws but thermodynamic identities. Jacobson's argument: take a small patch of any null surface (a surface light travels along), assign it entropy proportional to its area (following Bekenstein-Hawking), assign it temperature proportional to the acceleration needed to hover near it (the Unruh temperature), and demand that energy flowing across the surface satisfies the first law of thermodynamics. This uniquely forces the Einstein equations. Gravity is the thermodynamic *pressure* of spacetime, not a force.

*Analogy:* Think of the Einstein equations the way you think of the ideal gas law PV = nRT. The gas law isn't a force law — it's a statement about macroscopic equilibrium between pressure, volume, and temperature that emerges statistically from molecular collisions. Jacobson's gravity is the same: the curvature-energy relation is an equation of state, not a dynamical equation in the usual sense.

*Breaks when:* you push this analogy to ask about fluctuations or dissipation. The ideal gas law breaks at low N (small-number fluctuations dominate). Analogously, thermogravity likely breaks at the Planck scale where the "number of molecules" of spacetime is small — but what replaces it there is precisely the unknown quantum gravity the framework is trying to probe.

---

**The causal diamond**

To apply thermodynamics locally — without choosing a preferred global frame — the authors work inside a *causal diamond*: the region of spacetime accessible to an observer who sends a light pulse out, waits for it to reflect off a mirror at fixed proper distance, and receives it back. The diamond is bounded by ingoing and outgoing null surfaces (the light cone) meeting at an "equator" (the mirror).

*Analogy:* Think of a causal diamond as a radar ping: you send a signal, it bounces, it returns. The spacetime volume enclosed by the outgoing and incoming pulses is your "local laboratory." All the entropy — and therefore all the thermodynamics — lives on the walls of this radar envelope, not in the interior.

*Breaks when:* you try to make the diamond arbitrarily large. The construction is infinitesimal by design; the thermodynamic relations hold in the limit where the diamond shrinks to a point. Finite diamonds introduce corrections that depend on the global causal structure — precisely the complications this approach tries to avoid.

---

**The Otto cycle**

A standard Otto cycle (the thermodynamic abstraction of a gasoline engine) has four strokes: two *isochoric* (constant volume, heat flows in or out) and two *adiabatic* (no heat flow, work is done). A *degenerate* Otto cycle with only the heat strokes and no work strokes is just a heat exchanger with zero efficiency — it moves heat but does nothing useful.

*Analogy:* Standard thermogravity (GR) is like an engine that only has intake and exhaust valves, with no pistons. Heat flows in, heat flows out, nothing is compressed or expanded, and no work is extracted. The authors' extension adds pistons — the "chemical work" strokes — and the engine starts doing something, at the cost of not conserving what went in perfectly.

*Breaks when:* you take "efficiency" too literally. Engine efficiency is a ratio of work output to heat input. Here the "efficiency" parametrizes how much the new violation terms deviate from zero — an efficient cycle means *more* Lorentz violation, not a better cosmology. The cosmologically favorable regime is an *inefficient* cycle.

---

**Unimodular gravity and the trace-free Einstein equations**

Standard GR has ten independent Einstein equations (in four dimensions). Unimodular gravity is a slight restriction that removes one of them — the trace — leaving nine trace-free equations. The cosmological constant then appears as an integration constant rather than a vacuum energy, which sidesteps one form of the cosmological constant problem (why quantum field theory's enormous vacuum energy doesn't curve spacetime catastrophically). The authors' framework naturally produces trace-free Einstein equations from the thermodynamic construction, and then adds a *new* equation from the work stroke.

*Analogy:* Think of the ten Einstein equations as ten components of a stress tensor for spacetime. Unimodular gravity says "I'm going to constrain the determinant of the metric to be fixed — I've chosen a unit cell for my spacetime lattice and I won't let it breathe." This removes one degree of freedom. The trace-free part is what survives.

*Breaks when:* you interpret this as gauge fixing. Unimodular gravity is sometimes called "just a gauge choice" for GR, and in that case it's physically identical. The authors' theory is *not* gauge-equivalent to GR — it genuinely breaks diffeomorphism invariance from the outset, so the unimodular structure here is physically meaningful, not cosmetic.

---

**Local Lorentz invariance and its violation**

Local Lorentz invariance (LLI) is the requirement that, in a small enough region of spacetime, the laws of physics look the same to all observers regardless of their velocity. It's the local version of special relativity. Most tests of GR are really tests of LLI. Violations are stringently constrained — but they become cosmologically relevant if they're suppressed by a ratio of Planck-scale physics to cosmological-scale physics, which is roughly 10⁻⁶⁰.

*Analogy:* LLI is like saying every local patch of the internet obeys the same TCP/IP protocol regardless of which router you're sitting behind. Lorentz violation would be like discovering that routers near cosmological-scale density gradients run a slightly different packet protocol — undetectable in any single hop but accumulating over billions of hops into a detectable delay.

*Breaks when:* you try to use this to design a local Lorentz-violation experiment. The suppression here comes from the extreme inefficiency of the Otto cycle — the new physics scale ℓ' must be enormous (cosmological) for the theory to be consistent with solar-system tests, not Planck-small.

---

**Central analogy for this paper:** *A near-perfectly efficient heat exchanger with a tiny piston leak*

---

## §4 — Core Technical Explanation

**The starting point: thermogravity as a degenerate cycle**

Standard thermogravity derives the Einstein equations by demanding the first law of thermodynamics across each surface element of the null boundary of a causal diamond. The internal energy variation is δU = T δS, where T is the Unruh temperature and S is the Bekenstein-Hawking entropy proportional to area. You apply this to the ingoing null surface (energy flows in), and the outgoing one (energy flows out), impose conservation (total δU = 0 around the cycle), and the Einstein equations pop out.

What the authors notice is that this cycle has only two legs — heat in, heat out — with no work strokes. In the language of thermodynamics, it's a *degenerate* Otto cycle: the work-producing legs (the isentropic, adiabatic strokes) have been collapsed to zero. This is not a derivation choice; it reflects the fact that standard thermogravity assumes no conserved "number" of microscopic spacetime constituents. There's nothing to do chemical work against.

**Adding the chemical potential**

The authors introduce a conserved quantity N — the number of microscopic spacetime "atoms," which could be causal-set sprinklings, loop-quantum-gravity spin-network nodes, or similar discrete structures depending on your preferred quantum gravity framework. This introduces a chemical potential μ and a new work term μ dN in the first law:

$$\delta U = T\,\delta S + \mu\,\delta N$$

Symbol definitions:
- $\delta U$: variation in internal energy of the causal diamond
- $T$: local Unruh temperature (temperature experienced by an accelerating observer crossing the null surface)
- $\delta S$: variation in Bekenstein-Hawking entropy (proportional to variation in horizon area)
- $\mu$: chemical potential conjugate to the microscopic constituent number
- $\delta N$: variation in the number of microscopic spacetime constituents

What this actually means: adding μ dN is exactly analogous to adding a gas-phase chemical reaction to your engine cycle. The pistons don't just compress an inert gas — they're doing work against a chemical degree of freedom that can absorb or release energy. For gravity, this new degree of freedom is the discrete microstructure of spacetime itself.

**The four-stroke Otto cycle in the causal diamond**

The authors now run a full Otto cycle on the causal diamond:

- **Legs 1 and 3** (isochoric = constant N): These are the standard thermogravity heat strokes. Energy flows as heat across the null surfaces, N is held fixed, and these legs reproduce the trace-free Einstein equations exactly as before.

- **Legs 2 and 4** (adiabatic = constant S): These are new. No heat flows, but N changes — the spacetime microstructure shifts. These legs contribute chemical work W to the total energy balance.

The full cycle then satisfies:

$$0 = \Delta Q + W$$

where ΔQ is the net heat entering the diamond (nonzero when the cycle isn't degenerate) and W is the chemical work done in the adiabatic strokes.

**Deriving the new field equation**

The heat-stroke legs (1 and 3) give the trace-free Einstein equations:

$$G_{\mu\nu} - \frac{1}{4}g_{\mu\nu}G = 8\pi G\left(T_{\mu\nu} - \frac{1}{4}g_{\mu\nu}T\right)$$

Symbol definitions:
- $G_{\mu\nu}$: Einstein tensor (encodes spacetime curvature)
- $g_{\mu\nu}$: metric tensor (encodes distances)
- $G$: the trace of the Einstein tensor
- $T_{\mu\nu}$: stress-energy tensor (encodes matter and energy content)
- $T$: its trace

What this actually means: this is GR with the "breathing mode" of spacetime removed — the universe can shear and twist and warp, but it can't uniformly expand or contract at the level of this equation alone. The vacuum energy term doesn't appear here, which is the unimodular gravity result that sidesteps the cosmological constant problem.

The work-stroke legs then add a second equation. To make the emergent theory *decouple* from the underlying thermodynamics (so you get clean field equations, not equations entangled with temperature and entropy), the authors impose a scaling requirement: μ must be linear in N, with a proportionality set by a new length scale ℓ'. After carrying through the integrals over the diamond's null boundary (detailed in Appendix B), the work stroke contributes:

$$\nabla_\mu T^{\mu\nu} = \frac{\ell'^2}{\ell_P^2}\, u^\mu u^\nu \nabla_\mu \rho$$

where I'm schematizing the key structure: the right-hand side is a preferred-frame term (the four-velocity $u^\mu$ of the mirror picks out a rest frame) proportional to the ratio $(\ell'/\ell_P)^2$ and to gradients of the energy density $\rho$. The actual expression in the paper is:

$$\nabla_\mu T^{\mu\nu} \neq 0$$

with the violation sourced by the Otto cycle efficiency, parametrized by ℓ'.

Symbol definitions:
- $\nabla_\mu$: covariant derivative (the curved-spacetime generalization of a partial derivative)
- $T^{\mu\nu}$: stress-energy tensor (same as above but with raised indices)
- $\ell'$: the new length scale governing the work stroke — must be *cosmologically large* for solar-system tests to pass
- $\ell_P$: the Planck length (~10⁻³⁵ m), which sets the gravitational coupling

What this actually means: this equation says energy-momentum is *not* conserved in the usual sense. Matter can be created or destroyed at a rate set by the ratio of the two length scales. Because $\ell' \gg \ell_P$, the ratio is huge — but the violation is cosmologically suppressed, appearing only on Hubble timescales. This is the engine's exhaust: the leak in the piston that converts some of the cycle's imperfection into matter production.

**Cosmological application**

Applying the complete theory (trace-free Einstein equations + the new energy-nonconservation equation) to a homogeneous isotropic universe (FRW cosmology) with scale factor a(t), the Friedmann equations are modified. For a matter-dominated universe with the cycle running in the appropriate direction (matter-creating rather than matter-destroying), the solution is:

$$a(t) \propto t^{2/3}$$ at early times (standard matter domination), transitioning to accelerated expansion at late times when the ℓ' term becomes comparable to the matter density.

The solution requires ℓ' to be positive and large for the acceleration to appear — a microphysical condition the theory doesn't fix. The authors are honest that the sign of ℓ' is not predicted and remains a free parameter ("a microphysical mystery").

**Assumption Audit**

*Watch: the reader likely assumes the two length scales ℓ and ℓ' are both Planck-scale, and the whole point is to derive macroscopic effects from Planck-scale inputs.*
The paper actually requires ℓ' to be *cosmologically large* — roughly Hubble-scale or larger — for the theory to pass solar-system constraints. The Planck length sets the gravitational coupling (as usual), but the new physics scale ℓ' must be enormous. This is not a prediction; it's a requirement imposed by observations, and the theory provides no mechanism for explaining why ℓ' should be so large. The authors reframe this as the "new cosmological constant problem" (why is Lorentz violation so small?), but that's a restatement, not a solution.

*Watch: the reader likely assumes "violation of local Lorentz invariance" means detectable anisotropy in the speed of light or CPT violation in particle physics.*
The paper actually produces a different kind of LLI violation — a preferred cosmological frame defined by where matter (not momentum) is created. The observable signature at solar-system scales is an anomalous drag on planetary orbits and a secular increase in the solar mass, not a photon dispersion relation or birefringence. These are constrained by entirely different experiments (Eötvös tests, lunar laser ranging, planetary ephemerides) than the standard LLI tests (UHECR anisotropy, Michelson-Morley variants).

*Watch: the reader likely assumes the trace-free (unimodular) Einstein equations are equivalent to standard GR up to a redefinition of the cosmological constant.*
The paper actually argues — correctly — that the usual objection (unimodular gravity is just GR gauge-fixed) doesn't apply here because their theory has *no gauge invariance from the outset*. The unimodular structure is a genuine physical restriction, not a coordinate choice. This distinction is essential: if the theory *were* gauge-equivalent to GR, the new energy-nonconservation equation would be a contradiction, not an extension.

---

## §5 — What's Genuinely New or Clever

**The degenerate-cycle reframing.** The genuinely clever move here is identifying that standard thermogravity is a *degenerate* Otto cycle — a heat exchanger with no pistons — and that asking "what happens when we add the pistons?" is a well-defined, answerable question within the framework. This isn't a new addition bolted onto thermogravity; it's a discovery that the original framework was implicitly assuming zero work, and that relaxing this assumption has controlled consequences. The framing is elegant because it makes the question feel natural rather than arbitrary.

**Linking Lorentz violation to dark energy through thermodynamic inefficiency.** The connection between the smallness of the cosmological constant (or late-time acceleration) and the smallness of Lorentz violation is not a coincidence in this framework — they're the same parameter, ℓ'/ℓ_P. The Otto cycle efficiency parametrizes both simultaneously. This is a genuine unification of two empirical puzzles (why is Lambda small? why is LLI so good?) into a single structural statement (the Otto cycle is nearly degenerate). Whether this is correct is another matter, but the structural elegance is real and distinguishes this from models that simply add a Lorentz-violating term to the action by hand.

---

## §6 — Limitations & Open Questions

**The sign of ℓ' is a free parameter.** The theory requires ℓ' > 0 (matter creation rather than destruction) for late-time acceleration, but provides no microscopic mechanism fixing this sign. The authors explicitly call this a "microphysical mystery." (A) Consensus — the paper acknowledges this directly and it's a standard gap in any theory that introduces a new dimensionful parameter without a symmetry argument fixing its sign. (paper §main text, discussion of acceleration requirement)

**Solar-system constraints are severe and not fully resolved.** The minimal diagonal model is acknowledged to be ruled out by solar-system observations unless the preferred frame coincides precisely with all visible matter. The DM model faces the same issue unless the preferred-frame velocity is large enough for the DM produced by the Sun to escape the solar system. The authors say the constraints "appear to require" ℓ'/ℓ_P ~ 10⁻⁶⁰ on solar-system scales, which is compatible with cosmological constraints, but the matching requires either a running ℓ' (scale-dependent) or a running preferred frame. (A) Consensus — any theory with a preferred frame needs to pass Eötvös-type bounds; the requirement here is standard. (paper §local observations discussion)

**The cosmological perturbation theory is entirely deferred.** The paper presents only the background (homogeneous, isotropic) cosmological solution. Perturbations — the CMB power spectrum, matter power spectrum, structure formation — are explicitly deferred to future work, with the caveat that results will depend on gauge choice (synchronous, comoving, longitudinal) in a theory that breaks diffeomorphism invariance. This is a significant gap: a model can produce the right background expansion while badly misfitting the CMB, and there's no way to know yet. (A) Consensus — the field demands perturbation theory before any cosmological model is taken seriously as a ΛCDM replacement. (paper §discussion of deferred cosmological phenomenology)

**The scaling requirement μ ∝ N is imposed, not derived.** The assumption that the chemical potential scales linearly with the constituent number (Eq. 12 in the paper) is imposed specifically to achieve decoupling of the emergent theory from the underlying thermodynamics. This is a consistency requirement, but its microscopic justification is not given. Different scaling laws would produce different theories. (B) Contested — the authors frame this as a naturalness condition, but a specialist in causal set theory or LQG might argue the relevant scaling is nontrivial. (analyst inference)

**No mechanism for the preferred frame.** The theory requires a cosmological preferred frame — physically identified as the frame where matter (not momentum) is created. But the theory gives no dynamical mechanism for *why* this frame exists, what selects it cosmologically, or how it relates to the CMB rest frame. This is not the same as the CMB dipole question; it's a question about the physical origin of the frame itself. (C) Speculative — the paper gestures at this but doesn't address it; my read is that this is a genuine structural gap, not just a feature to be fixed in a follow-up. (analyst inference)

---

## §7 — Detailed Summary & Explanation

The paper asks a structural question about thermogravity: if gravity emerges from thermodynamics, why does the thermodynamic cycle appear to be degenerate — producing only heat exchange and no work? Real thermodynamic systems do work. What happens when spacetime's thermodynamic cycle is made non-degenerate?

The answer is constructed around a causal diamond — a small region of spacetime bounded by null (light-speed) surfaces — treated as the working fluid of an Otto cycle. In the standard thermogravity derivation, the cycle has only two heat-exchange legs; the work legs are collapsed to zero because there's no conserved "number" of spacetime constituents to do work against. The authors introduce such a number N, with its conjugate chemical potential μ, and run the full four-stroke cycle. The isochoric (constant-N) legs reproduce the trace-free Einstein equations (GR with the cosmological-constant term removed, equivalent to unimodular gravity). The isentropic (constant-entropy) work legs produce a new field equation: a controlled violation of energy-momentum conservation, sourced by gradients of energy density and pointing along the preferred frame of the mirror bounding the causal diamond.

The preferred frame is physically crucial. Standard thermogravity's null surfaces are Lorentz-covariant — they don't pick a preferred direction. But the mirror at the equator of the causal diamond breaks this: it's attached to a specific frame. Local Lorentz invariance emerges only if the mirror has no physical effect (i.e., only if the work legs are degenerate). When the work legs are active, the mirror's preferred frame becomes a physical structure of the theory, and local Lorentz invariance is broken — gently, because the cycle is nearly (but not exactly) degenerate.

Applied to a homogeneous isotropic universe, the combined equations (trace-free Einstein + energy non-conservation) produce a cosmology that matches standard matter domination early on and accelerates at late times, provided the new length scale ℓ' is positive and large. The effective "dark energy" is not vacuum energy — it's the accumulated effect of matter creation from the Otto cycle's work strokes. This sidesteps the cosmological constant problem in the sense that vacuum energy never gravitates (unimodular structure), and the observed acceleration is reattributed to a microphysical-but-currently-free parameter ℓ'.

The cosmological constant problem is reframed but not dissolved: "why is Lambda small?" becomes "why is ℓ'/ℓ_P large enough to suppress Lorentz violation at solar-system scales?" The authors argue this is a genuine reframing — the two problems have different structures, and the Lorentz-violation framing may be more tractable — but they don't provide the microscopic answer.

Local constraints are challenging. Solar-system observations require the ratio ℓ'/ℓ_P to be extremely small on planetary scales, while cosmological observations require it to be significant on Hubble scales. This is either a genuine scale-dependence of ℓ' (running with the local curvature or density) or requires the preferred frame to be moving fast enough relative to solar-system matter that the DM trail escapes the solar system. Neither mechanism is worked out.

**Why the summary is framed this way:** The paper is primarily a theoretical existence proof — demonstrating that a non-degenerate Otto cycle in thermogravity produces something interesting, not that it uniquely predicts a specific cosmological history. The framing emphasizes the structural moves (degenerate → non-degenerate, heat-only → heat + work) because those are the genuinely novel contributions; the specific equations are secondary. The local-constraint discussion is given significant weight because this is where the theory faces its most immediate empirical risk, and the paper's treatment is more qualitative than quantitative.

**Genuine Uncertainty Disclosure:** Where I'm least confident in this analysis is the derivation of the new field equation from the work legs of the Otto cycle — specifically, the step where the scaling condition μ ∝ N (Eq. 12) is combined with the Stokes' theorem application to the diamond boundary to yield the explicit energy-nonconservation equation (Eq. 14). The paper's Appendix B handles the integral identities, but the plain-language translation of how the chemical work term becomes a preferred-frame source for ∇_μ T^μν involves geometric steps (conformal Killing vector corrections, light-cone averaging of the mirror's normal) where my reconstruction is necessarily schematic and may have lost quantitative detail.

---

## §8 — Three Crystallized Takeaways

1. **GR is a thermodynamic engine running on empty.** Standard emergent gravity produces Einstein's equations from a heat cycle with no work strokes — a degenerate engine. Adding work strokes (chemical potential for spacetime microstructure) yields a natural generalization that breaks energy conservation and Lorentz invariance in a controlled, cosmologically testable way.

2. **Dark energy and Lorentz violation are the same knob.** In this framework, the smallness of the cosmological constant and the near-perfection of local Lorentz invariance both reflect the extreme inefficiency of the spacetime Otto cycle, parametrized by a single ratio of length scales. Making the cycle slightly less degenerate simultaneously produces late-time acceleration and a preferred cosmological frame.

3. **The cosmological constant problem is reframed, not solved.** Vacuum energy still doesn't gravitate (unimodular structure), but the question "why is Lambda small?" is replaced by "why is Lorentz violation suppressed at solar-system scales?" — which the theory doesn't yet answer, though the authors argue this version of the problem has better prospects for a microscopic resolution.

---

## §9 — Shorter Summary

This paper extends the emergent-gravity program by asking what happens when the thermodynamic cycle underlying Einstein's equations is allowed to do work, not just exchange heat. In the standard picture, due to Jacobson and others, GR emerges from demanding that energy balance correctly across the boundary of a small spacetime region (a causal diamond), with entropy proportional to area and temperature set by local acceleration. This derivation uses only heat — entropy and temperature — with no work terms. The authors point out that this makes the cycle thermodynamically degenerate: a heat exchanger with zero efficiency, producing no work.

They fix this by introducing a conserved "number" of microscopic spacetime constituents — atoms of space in loop quantum gravity, sprinklings of events in causal set theory, or similar — and their conjugate chemical potential. Running the full Otto cycle on the causal diamond, the heat legs reproduce the trace-free Einstein equations (GR minus the cosmological-constant contribution, equivalent to unimodular gravity). The work legs produce a new equation stating that energy-momentum is not exactly conserved: matter can be created or destroyed at a rate set by a new length scale.

The preferred frame of the mirror bounding the causal diamond becomes physical when the work legs are active, breaking local Lorentz invariance. The breaking is suppressed by the ratio of the Planck length to the new length scale, which must be cosmologically large for the theory to pass solar-system tests. The smallness of this suppression is the same thing as the smallness of the cosmological constant — both reflect how nearly degenerate the spacetime Otto cycle is.

Applied to the universe as a whole, the theory produces standard matter domination early on and accelerated expansion at late times, with the acceleration driven by matter creation from the work strokes rather than by vacuum energy. The vacuum energy does not gravitate (unimodular structure), sidestepping one form of the cosmological constant problem. The full perturbation theory — needed to test the model against CMB and large-scale structure data — is deferred, and the sign of the new length scale (which determines whether the cycle creates or destroys matter) is a free parameter the theory does not yet predict.
