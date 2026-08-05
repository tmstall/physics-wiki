---
source: claude_export
conversation_uuid: 9cdb1c0c-aae8-427d-b7f0-6daf62825571
title: "Second-order gravitational wave strain analysis"
created_at: 2026-06-19T07:30:41.263379Z
updated_at: 2026-06-19T07:55:18.334191Z
tier: A
score: 43
n_messages: 6
---

# Second-order gravitational wave strain analysis

## Human

Analyze this paperReference: “Observable Gravitational Wave Strain at Second Order” by Guillem Domènech, Shi Pi and Ao Wang, 3 June 2026, Physical Review Letters.
DOI: 10.1103/pwbs-xwrh

## Assistant

**v3.6.3**

---

## Section 1 — Punchy Title & One-Sentence Hook

### *The Gauge Has Been Settled: Newton Wins*
For decades, theorists argued over which mathematical "coordinate language" correctly predicts the gravitational waves produced by the early universe — and this paper finally proves, by tracking actual light pulses between actual observers, that Newton's gauge is the physically correct one.

---

## Section 2 — Big-Picture Context

Gravitational waves (GWs) are ripples in spacetime geometry, and since LIGO's first detection in 2016 they've become a precision observational tool. But the GWs LIGO measures come from black hole and neutron star mergers — compact, nearby, well-understood sources. The cosmological GW frontier is different: it involves a *stochastic background* of gravitational waves generated throughout the early universe, potentially from primordial black hole formation, phase transitions, and — most relevant here — the sheer act of density fluctuations growing under gravity. These are called **induced** (or secondary) gravitational waves.

Induced GWs arise because the same primordial density fluctuations that seeded the CMB and all large-scale structure also drive spacetime to wiggle at *second order* — meaning at a level quadratic in those fluctuations, rather than linear. This second-order signal is now scientifically urgent: all four major Pulsar Timing Array (PTA) collaborations (NANOGrav, EPTA, PPTA, CPTA) reported hints of a stochastic GW background in 2023, and induced GWs from primordial black hole scenarios are a leading candidate source.

The trouble is that general relativity is written in a language that is explicitly coordinate-free. You can slice the four-dimensional spacetime into time + space in infinitely many ways — each "slicing" is a gauge choice — and the mathematics looks different in each one. At *linear* order in perturbations, the physically meaningful GW component (the transverse-traceless, or TT, piece of the metric) is perfectly gauge-invariant: everyone agrees on it regardless of slicing. At *second order*, that gauge invariance breaks down. The same physical universe gives you different-looking TT components depending on your coordinate choice. Previous calculations found that the Newton gauge, the synchronous gauge, and the flat gauge all agreed on the induced GW power spectrum, while the comoving gauge gave discrepant results — but nobody could *prove* which (if any) was right, because nobody had connected the theoretical quantity to an actual measurement protocol.

This paper closes that gap: it computes what a real detector — two observers exchanging light signals — actually measures when a second-order GW passes, entirely without fixing a gauge, and identifies exactly which mathematical combination maps to that observable.

**Prior Belief Check:** This result is not surprising in its conclusion — the Newton gauge has been the community's working assumption for years, and the expectation that it would turn out to be the correct one was widely shared. What *is* surprising to experts is that it took until 2026 for anyone to produce a rigorous proof. The calculation is genuinely hard: second-order geodesics in a perturbed FLRW universe are involved, and keeping everything gauge-free throughout is technically demanding. The result is confirmatory rather than field-overturning, but it resolves a concrete, publicly acknowledged ambiguity that had been nagging the induced-GW community for nearly a decade.

**Replication & Convergence Note:** This is a single-group result with no independent replication yet. The companion paper (reference [62] in the arxiv version, by the same authors) contains the full derivation; an independent confirmation would look like a separate group tracking geodesic observers through second-order FLRW perturbation theory and arriving at the same gauge-invariant combination — or, eventually, a PTA data-analysis team showing that Newton-gauge templates fit observations better than comoving-gauge ones.

---

## Section 3 — Necessary Background Crash-Course

**Gravitational waves and the transverse-traceless gauge.** A gravitational wave is a propagating distortion of spatial geometry. In flat spacetime or linearized GR, you can always decompose any metric perturbation into scalar, vector, and tensor pieces. The tensor piece — the transverse-traceless (TT) part — is what GW detectors respond to. "Transverse" means the distortion is perpendicular to the wave's direction of travel; "traceless" means the volume doesn't change, only the shape. At linear order this decomposition is unambiguous: every observer, regardless of coordinate choice, extracts the same TT piece.

*Analogy:* Think of pulling on a rubber sheet that's stretched over a drum. You can grab and twist the edges however you like (that's your gauge choice), but the drumhead itself only supports a specific set of vibrational modes — the ones that are perpendicular to the rim and don't change the total area. Those modes are the "TT part," and at linear order everyone agrees on what they are.
*Breaks when:* you go to second order in the oscillation amplitude. Now the twisting of the edges you chose affects the apparent shape of the drumhead, so two people holding different parts of the rim disagree about what "transverse-traceless" even means.

**Gauge freedom in cosmological perturbation theory.** In an expanding universe, you must choose how to slice the four-dimensional spacetime into a sequence of three-dimensional spatial snapshots — what counts as "the same moment in time" across different locations. This choice is the gauge, and different choices can shuffle energy, momentum, and even gravitational wave content between different perturbation modes at second order. The Newton gauge (also called the Poisson or longitudinal gauge) sets two scalar perturbations to zero in a way that recovers Newtonian gravity on sub-Hubble scales. The comoving gauge ties the time slices to the matter flow. Neither is "wrong" — they're coordinate systems, not physics — but the physical observable (what a detector reads) must be the same in all of them.

*Analogy:* This is exactly like the choice of reference frame in special relativity. Length contraction and time dilation look different to observers in different frames. But the spacetime interval — the real, invariant thing — is always the same. The Newton gauge is like the rest frame of the atom you're measuring: maximally convenient for connecting theory to observation.
*Breaks when:* you try to compute energy density of GWs rather than strain. The energy in a gravitational wave field (the pseudo-energy-momentum tensor) has its own second-order gauge ambiguity, and this paper explicitly notes it does *not* resolve that separate problem.

**Induced (secondary) gravitational waves.** GWs can be produced not just by merging black holes but by large density fluctuations in the early universe. A strong primordial density perturbation creates a second-order "back-reaction" on the metric that propagates as a gravitational wave. These are particularly interesting as a probe of the epoch before Big Bang Nucleosynthesis (which is otherwise observationally inaccessible) and as a signature of primordial black hole formation.

*Analogy:* Imagine two boats (the density waves) crossing a lake. The linear waves they each create are independent. But at second order, the interference pattern between the two boats creates its own waves — smaller, but real. Those are the induced GWs.
*Breaks when:* you want to think about superposition. Unlike acoustic waves in a lake, gravitational waves curve the spacetime they propagate through, so second-order GWs don't simply add on top of first-order ones — they mix in a gauge-dependent way, which is exactly the problem this paper solves.

**Geodesic clocks and EM signal exchange.** This paper's approach to the problem is to compute what an actual detector measures: two freely-falling observers exchanging light pulses. A "geodesic clock" is the idealized version of every real GW detector — LIGO (bouncing laser light off mirrors), PTAs (timing radio pulses from millisecond pulsars), LISA (exchanging laser signals between spacecraft). The observable is the time delay or frequency shift of those light pulses. Because proper time is frame-independent, computations done in terms of proper time are automatically gauge-invariant.

*Analogy:* This is like checking whether your watch runs fast or slow by comparing it against GPS signals — the comparison is a physical process, not a coordinate artifact. Whatever your coordinate convention, the ticks of your watch and the arrival times of the GPS pulses are real events. Building GW detection theory from those events is the only way to get a truly gauge-invariant answer.
*Breaks when:* you ask about non-geodesic observers. LIGO's mirrors are not in free fall — they're suspended by seismic isolation systems and experience non-gravitational forces. The paper acknowledges this and notes that generalizing to non-geodesic observers would affect only the "observer motion subtraction" piece, not the GW propagation result itself.

**Central analogy for this paper:** *GPS arrival-time comparison*

---

## Section 4 — Core Technical Explanation

**Setup: the perturbed FLRW metric.** The authors work in a spatially flat Friedmann–Lemaître–Robertson–Walker universe — the standard cosmological background — perturbed to second order. The metric is written in conformal time using an exponential parameterization:

$$ds^2 = a^2\!\left(-e^{2\phi}d\eta^2 + e^{2\psi}(e^Y)_{ij}(dx^i + N^i d\eta)(dx^j + N^j d\eta)\right)$$

Symbol definitions:
- $a(\eta)$: scale factor (how much the universe has expanded)
- $\eta$: conformal time (ordinary time rescaled by $a$ to absorb the expansion)
- $\phi, \psi$: scalar metric perturbations (the "gravitational potential" and its spatial analogue)
- $N^i$: vector shift perturbation (set to a pure gradient, ignoring vector modes)
- $Y_{ij}$: spatial tensor perturbation, decomposed into a scalar trace-free piece $E$ and TT piece $h_{ij}$
- $h_{ij}$: the transverse-traceless metric perturbation — what we loosely call "the gravitational wave"

This is the exact same machinery used in CMB physics and large-scale structure perturbation theory. Nothing exotic yet.

**The geodesic clock.** They place two freely-falling observers separated by a comoving distance $L$ along direction $n^i$, and have them exchange electromagnetic signals. The emitter fires pulses; the receiver logs the arrival times. Perturbations in the metric perturb the null geodesic of the photon and the timelike geodesics of the observers, causing tiny shifts in the proper reception time $\tau_\mathrm{rf}$. The key move: proper time is *gauge invariant by construction* — it's what your clock actually reads — so any result expressed in terms of proper time is automatically physical.

**First-order result (the warm-up).** They solve everything to first order first, as a check. The first-order time delay comes out as:

$$\tau_{\rm rf}^{(1)} = a_{\rm rf}\!\left(\int_0^L d\lambda\,\tfrac{1}{2}n^i n^j h_{ij}^{(1)} - \Phi^{(1)} - \Psi^{(1)}\right) + \text{(boundary/observer-motion terms)}$$

- $\Phi^{(1)}, \Psi^{(1)}$: the gauge-invariant Bardeen potentials (gravitational potential + spatial curvature perturbation)
- The $n^i n^j h_{ij}$ term: the GW contribution — it picks out the component of the metric distortion along the line connecting the two observers, exactly the "quadrupole" geometry every GW detector has
- The boundary terms: encode the observers' initial positions and velocities

At first order, $h_{ij}^{(1)}$ is gauge invariant, so no ambiguity arises. They also compute the redshift (by looking at successive pulse pairs rather than a single pulse), which is cleaner because it cancels initial-condition ambiguities and gives the standard Sachs-Wolfe + GW formula. Reproducing the known Hellings-Downs formula for PTA geometry is the sanity check.

**Second-order result (the main result).** At second order, the quadrupole component of the time delay is:

$$\tau_{\rm rf}^{(2)} \supset a_{\rm rf}\,n^i n^j\!\left(\tfrac{1}{2}\int_0^L d\lambda\,h_{ij}^{N(2)} + \text{(observer-motion boundary terms)}\right)$$

The key quantity is:

$$h_{ij}^{N(2)} \equiv h_{ij}^{(2)} + P_{ij}^{\;lk}\!\left(\sigma_l^{(1)}\sigma_k^{(1)} + E_{,lm}^{(1)}E_{,mk}^{(1)}\right)$$

- $h_{ij}^{(2)}$: the raw second-order TT metric perturbation (gauge-dependent on its own)
- $\sigma^{(1)}$: the spacetime shear, built from the scalar perturbation $E$ and its time derivative
- $P_{ij}^{\;lk}$: the transverse-traceless projector (strips out non-TT pieces)
- The combination $h_{ij}^{N(2)}$: this is the gauge-invariant quantity that the authors identify as the *physical* GW strain at second order — and it *equals* the TT metric components in the Newton gauge (where $\sigma = E = 0$ by definition)

The observer-motion boundary terms — involving the observers' first-order velocities and displacements — are cleanly separable: they encode how the detectors themselves moved during the measurement, not the GW passing through. If you track observer motion by independent means (e.g., additional signal exchanges between detectors), you can subtract them and isolate $h_{ij}^{N(2)}$ cleanly.

**The redshift at second order.** The same logic applied to the redshift (the ratio of successive pulse arrival intervals) gives:

$$z_{\rm GW}^{(2)} = \frac{a_{\rm rf}}{a_{\rm ei}}\,\frac{1}{2}\,n^i n^j \int_0^L d\lambda\,h_{ij}^{N(2)\prime}$$

where the prime denotes a time derivative. This is the second-order version of the PTA timing residual formula, and it directly tells you: what PTAs measure is the time derivative of $h_{ij}^{N(2)}$ integrated along the line of sight. Newton gauge wins.

**The constant-strain bonus result.** A subtle side finding: in early matter-dominated phases, there are solutions where the induced GW strain becomes *time-independent* — a "frozen" mode. Looking at the redshift formula, a time-independent strain has $h' = 0$, so it contributes *nothing* to the redshift and nothing to PTA or LIGO measurements. But it does appear in the time-delay formula (not the redshift). The authors interpret this as a *gravitational wave memory* analog — it's not an oscillating wave, but it permanently shifts the geometry. If a detector was calibrated before this frozen mode was established, the mode would be observable as a step-function shift in detector arm length. If calibrated after, it's invisible. This is a physics bonus: the constant mode isn't a gauge artifact — it's real, but behaves like GW memory rather than a propagating wave.

---

### Assumption Audit

**Watch:** Reader likely assumes the result only applies to induced GWs from primordial fluctuations. The paper actually says the calculation makes no assumptions about the source — it applies to any second-order GW from any cosmic source (phase transitions, preheating, etc.).

**Watch:** Reader likely assumes that proving Newton gauge is correct for the *strain* also proves it's correct for the *energy density* of GWs. The paper explicitly says the opposite — the energy density (defined through the pseudo-energy-momentum tensor) has a *separate, unresolved* gauge ambiguity at second order. The paper settles strain; it explicitly defers energy density to future work.

**Watch:** Reader likely assumes the "observer-motion boundary terms" in the second-order time delay are small corrections that can safely be ignored. The paper treats them as potentially non-negligible and argues that they must be independently measured and subtracted — for instance, by having detectors exchange signals with *each other* in addition to receiving GWs. This is conceptually significant: it means the full second-order GW measurement is not just "point your detector at the sky" but requires a more complete network-level subtraction of internal detector kinematics.

---

## Section 5 — What's Genuinely New or Clever

**The novelty is the methodology, not just the conclusion.** Everyone suspected Newton gauge was right. What the field lacked was a proof that didn't rely on an ad-hoc physical argument (like "Newton gauge recovers Newtonian physics on small scales, therefore it's physical"). The authors' trick is to define the problem entirely in terms of proper time — a manifestly gauge-invariant observable — and *then* read off which mathematical combination of metric perturbations it corresponds to. They don't pick a gauge; gauge-independence is built into the starting point. The answer ($h_{ij}^{N(2)}$) then identifies itself as the Newton-gauge TT component, rather than being assumed from the outset.

**The constant-mode / GW memory connection** is the genuinely surprising physical insight. Several previous papers had noticed the time-independent mode and treated it as either a gauge artifact (to be discarded) or a theoretical nuisance. This paper gives it a physical home: it's GW memory. That reinterpretation is new to the field and has implications for how PTA collaborations should think about the low-frequency behavior of their signal. A constant-strain mode won't show up in timing residuals — but a detector calibrated at the right moment might see it as a sudden step in arm length. That's not a crazy new effect; it's the same GW memory that LIGO already sees (in principle) from black hole mergers.

---

## Section 6 — Limitations & Open Questions

**1. Geodesic observers only — no ground-based interferometers yet.** The entire calculation assumes freely-falling observers. LIGO and Virgo mirrors are not free-falling; they're isolated from seismic noise by complex suspensions subject to non-gravitational forces. The authors note the generalization is straightforward in principle but leave it undone. (A) Consensus — this is standard practice in the field: treat first the ideal case, then generalize. (paper §Conclusion)

**2. Scalar-scalar terms only; scalar-tensor cross-terms omitted.** The second-order TT components receive contributions from scalar×scalar, scalar×tensor, and tensor×tensor combinations of first-order perturbations. The paper focuses solely on scalar×scalar because those are what matter for induced GWs in the standard scenario. Scalar-tensor cross terms are known to produce divergences in some gauge choices, and it's unknown whether $h_{ij}^{N(2)}$ also fixes *that* problem. (B) Contested — some papers treat the scalar-tensor divergences as gauge artifacts and others as physical; the Newton-gauge proof here might or might not extend cleanly. (paper §Conclusion + broader literature)

**3. GW energy density remains gauge-ambiguous.** The paper explicitly flags that settling the strain does not settle the energy density. The GW energy density is computed from a pseudo-energy-momentum tensor (Isaacson's formula and its cosmological generalizations), which has additional second-order ambiguities not addressed here. This matters because PTA collaborations report results in terms of $\Omega_\mathrm{GW}$ (GW energy density per log frequency), not raw strain. (A) Consensus — acknowledged explicitly in the paper and in the broader field literature. (paper §Conclusion)

**4. No treatment of vector modes.** The paper sets vector perturbations to zero from the start for simplicity. In some early-universe scenarios (certain topological defects, turbulence from phase transitions) vector modes can be significant at second order. Whether $h_{ij}^{N(2)}$ remains the right physical strain in the presence of vector modes is not addressed. (C) Speculative — the paper does not discuss this; I'm inferring from the generality of cosmological perturbation theory. (analyst inference)

**5. The companion paper doing the heavy lifting hasn't been independently verified.** The detailed derivation is in reference [62], a companion paper by the same three authors. The PRL letter is the announcement; the proof lives in the companion. Independent confirmation would require someone else working through the second-order geodesic calculation in full. (B) Contested — companion papers are standard in the field, but until the companion is independently refereed and verified, the proof chain has only one check. (analyst inference)

---

## Section 7 — Detailed Summary & Explanation

The central problem the paper addresses is this: in cosmological perturbation theory, the metric perturbation that we call a "gravitational wave" is only unambiguously defined at first (linear) order. At second order — the level at which the universe's own density fluctuations generate gravitational waves — different coordinate choices (gauges) give you different answers for what the TT (transverse-traceless) component of the metric looks like. This matters enormously for the induced GW program, which is the theoretical backbone of the current PTA GW background results and future LISA science.

Previous work had found empirically that the Newton, synchronous, and flat gauges agree with each other, while the comoving gauge disagrees. But "agree with each other" is not the same as "are correct." The field needed to connect the theoretical quantity to an actual physical observable and show which combination of metric perturbations a detector truly measures.

The authors' strategy is elegant: define a "geodesic clock," the simplest possible gravitational wave detector — two freely-falling observers exchanging light pulses. Proper time elapsed is a frame-independent quantity. They then solve, at full second order in cosmological perturbation theory, the null geodesic of each photon and the timelike geodesics of each observer in a perturbed expanding universe, without fixing any gauge. The result is a second-order time delay and redshift that can be decomposed into pieces. The piece with the characteristic quadrupolar directional signature — $n^i n^j$ times something, where $n^i$ is the direction between the observers — is, by definition, the GW contribution.

That quadrupolar piece turns out to be proportional to a specific gauge-invariant combination of metric perturbations, which they call $h_{ij}^{N(2)}$. Computing what $h_{ij}^{N(2)}$ equals in different gauges reveals it matches the TT components in the Newton gauge exactly. The other gauges (comoving, synchronous) give the same answer after gauge transformation — of course they must, since $h_{ij}^{N(2)}$ is gauge-invariant — but the *simplest expression* for it is in Newton gauge. In practice, this tells theorists: run your induced-GW calculations in the Newton gauge, and your predicted strain directly equals what detectors measure.

A secondary result concerns the time-independent ("frozen") strain mode that appears in matter-dominated cosmological phases. These modes have troubled the field because they seemed to contribute a constant offset to the GW signal, with unclear observational status. The time-delay formula reveals: such modes don't appear in the redshift (which is what PTAs actually measure), because the redshift is sensitive to $h'$ (the *time derivative* of the strain). But they do appear in the raw time delay. The resolution is that the frozen mode is physically analogous to GW memory — a permanent displacement of spacetime geometry, visible if your detector was calibrated before the mode was established, invisible if calibrated after.

The paper is 10 pages and fairly compressed; the full derivation lives in a companion paper. The PRL version presents the key results and their physical interpretation clearly, with the formalism set up enough to follow the logic even without the companion.

**Where I'm least confident in this analysis:** The treatment of the observer-motion boundary terms in the second-order time delay — specifically whether the decomposition between "propagating GW" and "detector kinematic" contributions is fully clean at second order in a dynamical spacetime, or whether there are subtle cross-terms I may be glossing over in the plain-language translation. The companion paper [62] is where the detailed accounting lives, and I have not read it in full.

---

## Section 8 — Three Crystallized Takeaways

1. **Newton gauge is not just convenient — it's proven correct.** For the first time, someone computed what an actual detector (two freely-falling observers exchanging light pulses) measures at second order in cosmological perturbation theory, without assuming a gauge. The answer is the TT metric components in Newton gauge. Every future induced-GW calculation that uses Newton gauge is now on rigorous observational footing — not just community consensus.

2. **The "frozen mode" is gravitational wave memory, not a gauge artifact.** A long-standing source of confusion in the induced GW literature — a time-independent strain mode that appeared in some gauges and not others — is now physically interpreted. It behaves exactly like GW memory: invisible in timing residuals (which PTAs measure), but potentially observable as a permanent step-function shift in detector arm length if you calibrated before the mode appeared. It's real, just quiet.

3. **Settling the strain does not settle the energy density.** The GW spectrum reported by PTA collaborations is expressed as energy density, not raw strain — and the energy density of second-order GWs has a separate, still-open gauge ambiguity. This paper is a necessary step, not the final word. The result is that $h_{ij}^{N(2)}$ is the physical strain; what that implies for the precise normalization of $\Omega_\mathrm{GW}$ predictions remains to be shown.

---

## Section 9 — Shorter Summary

*(350-word ceiling)*

Gravitational wave detectors measure spacetime distortions by tracking how long it takes light to travel between two points. When a gravitational wave passes, it stretches and squeezes that travel time with a specific directional signature — the quadrupole pattern that gives LIGO its distinctive L-shape and pulsar timing arrays their Hellings-Downs angular correlation.

At first order in perturbation theory — the standard approximation for black-hole mergers and similar sources — this is well understood and unambiguous. The "transverse-traceless" piece of the metric perturbation is gauge-invariant: every coordinate system agrees on its value. At second order, where you square the perturbations, this invariance breaks down. Different choices of how to slice the expanding universe into time snapshots give different-looking gravitational wave amplitudes. For cosmologists trying to predict the background signal from the early universe — especially from the processes that may have formed primordial black holes — this ambiguity has been a persistent headache.

Previous calculations found that the Newton gauge, the synchronous gauge, and the flat gauge all gave the same induced GW spectrum, while the comoving gauge disagreed. But no one had connected any of these to an actual physical measurement. Was the comoving gauge wrong? Were the others merely agreeing by coincidence?

Domènech, Pi, and Wang resolved this by going back to first principles. They set up the simplest possible detector — two freely-falling observers exchanging light signals — and computed what it actually measures at second order in a perturbed expanding universe, without fixing any gauge at all. Proper time is inherently gauge-invariant, so building the observable from proper-time comparisons gives a result that's automatically coordinate-free. When they read off which combination of metric perturbations drives the detector response, they found it matches the transverse-traceless components in the Newton gauge exactly.

As a bonus, they clarified the status of "frozen" strain modes that had confused theorists: these don't show up in timing residuals (what pulsar timing arrays measure) because those measurements track the *rate of change* of strain, not strain itself. The frozen modes instead behave like gravitational wave memory — real, permanent shifts in geometry, but silent to oscillatory measurements.

One caveat: this result settles the *strain* gauge ambiguity. A separate ambiguity in the *energy density* of induced gravitational waves remains open and is left for future work.

## Human

ExplainGauge freedom in cosmological perturbation theory. In an expanding universe, you must choose how to slice the four-dimensional spacetime into a sequence of three-dimensional spatial snapshots — what counts as "the same moment in time" across different locations. This choice is the gauge, and different choices can shuffle energy, momentum, and even gravitational wave content between different perturbation modes at second order. The Newton gauge (also called the Poisson or longitudinal gauge) sets two scalar perturbations to zero in a way that recovers Newtonian gravity on sub-Hubble scales. The comoving gauge ties the time slices to the matter flow. Neither is "wrong" — they're coordinate systems, not physics — but the physical observable (what a detector reads) must be the same in all of them.

## Assistant

Responding

Let me unpack this carefully, because there are actually two distinct ideas compressed into that paragraph that are worth separating.

---

## Idea 1: What "gauge" means in this context

In flat spacetime, if you have a gravitational wave, you can ask: what is the metric perturbation? There's an ambiguity — you can redefine your coordinates slightly (a "gauge transformation"), and the numbers describing the perturbation change, even though the physics doesn't. This is the same kind of freedom you have in electromagnetism: the electric and magnetic fields are physical, but the vector potential $\mathbf{A}$ is not unique — you can add a gradient to it without changing $\mathbf{E}$ or $\mathbf{B}$.

In cosmology the same thing happens, but with a twist: the background itself is *dynamic*. The universe is expanding, and that expansion defines a natural "flow of time" — but only at zeroth order (the background). Once you add perturbations (density fluctuations, GWs), you have to decide how to match up points in the perturbed universe with points in the smooth background universe. That matching is the gauge choice.

The concrete thing you're choosing is: **what do you call "the same moment in time" at two different spatial locations?** 

Imagine you're trying to compare the density at point A to the density at point B "at the same time." In an unperturbed universe, that's trivial — just use the cosmic clock (the scale factor $a$). But in the real universe, point A might be in a dense region where time runs slightly slower (gravitational time dilation), and point B might be in a void. "The same moment" is not defined without a convention.

The gauge choice is that convention — a rule for drawing your time slices across the perturbed universe.

---

## Idea 2: Why this shuffles perturbation content

Here's the key physical intuition. Suppose you draw your time slices to follow the matter: you always call "simultaneous" the set of points where the matter density takes the same value. That's the **comoving gauge**. From this vantage point, there are no density fluctuations by definition (you've absorbed them into your time slices), but your time slices are now wavy — they're not flat surfaces in spacetime, they ripple with the matter distribution.

Alternatively, draw your time slices to make the metric look as "Newtonian" as possible: set the off-diagonal metric terms and one scalar piece to zero. That's the **Newton gauge** (Poisson gauge). Now your time slices are flatter, but the density fluctuations are plainly visible as variations in the gravitational potential $\Phi$.

Both descriptions contain the same physics. But the *numbers* you assign to each mode — how much is "scalar density perturbation," how much is "gravitational potential," how much is "GW" — depend on which slicing you chose.

At **first order**, this is manageable. You can construct explicit gauge-invariant quantities — the Bardeen potentials $\Phi$ and $\Psi$ — that have the same value in every gauge. The TT (gravitational wave) part is also separately gauge-invariant at first order. So even though individual components shift around, you can always identify and track the physical pieces.

At **second order**, the situation is harder in a specific way: the TT decomposition itself becomes gauge-dependent. Here's why. The TT projection is a *nonlocal* operation — it involves solving $\nabla^{-2}$ (an inverse Laplacian, essentially a spatial integral over the whole universe). When you change your time slices, the scalar perturbations ($\phi$, $\psi$, $E$) mix into the tensor sector at second order, because the coordinate transformation itself is now *first-order-times-first-order* — a product of two small things, which contributes at second order. That mixing is precisely what the $P_{ij}^{lk}(\sigma^{(1)}_l \sigma^{(1)}_k + ...)$ correction term in the paper is doing: it's subtracting out the scalar leakage into the TT sector that comes from the gauge transformation.

---

## Why "neither is wrong"

This is really the core point. A gauge choice is like a coordinate system in ordinary geometry. The distance between two cities doesn't change when you switch from kilometers to miles, or when you rotate your map. Similarly, the physical GW strain — what the detector reads — doesn't change when you switch from Newton to comoving gauge. 

What *does* change is what you call the "raw" $h_{ij}^{(2)}$ component of the metric. In Newton gauge, $h_{ij}^{(2)}$ equals the physical observable directly. In comoving gauge, $h_{ij}^{(2)}$ is a different-looking number — and to recover the physical observable, you have to add back the correction terms from the gauge transformation. The paper shows that after that correction, you always get the same $h_{ij}^{N(2)}$, regardless of starting gauge.

The comoving gauge isn't *wrong* — it gave wrong-looking predictions for the GW spectrum only because people were comparing $h_{ij}^{(2)}$ in comoving gauge directly to $h_{ij}^{(2)}$ in Newton gauge, without doing the gauge transformation that relates them. That's like comparing a temperature in Celsius to one in Fahrenheit and concluding they're different temperatures.

---

## The sub-Hubble / Newton-gauge connection

One more piece worth unpacking: why does the Newton gauge "recover Newtonian gravity on sub-Hubble scales"?

The Hubble radius is roughly the scale at which the expansion of the universe becomes important — beyond it, two points are receding from each other faster than light. On scales *smaller* than this, gravity behaves approximately as Newton described: instantaneous action at a distance, no relativistic effects. The Newton gauge is designed to make the metric look like this on small scales: the scalar potential $\Phi$ in Newton gauge obeys the ordinary Poisson equation ($\nabla^2 \Phi = 4\pi G \rho \delta$), exactly as in Newtonian physics. 

That's why it's the natural gauge for connecting theory to observation — real detectors (LIGO, PTAs) are always much smaller than the Hubble radius, so they live in the regime where Newton gauge is the cleanest description. The paper's result — that what detectors measure equals the TT components in Newton gauge — is, in retrospect, physically intuitive for exactly this reason. The proof just confirms that the intuition survives rigorously at second order.

## Human

ExplainAt second order, the situation is harder in a specific way: the TT decomposition itself becomes gauge-dependent. Here's why. The TT projection is a nonlocal operation — it involves solving del to the minus 2 (an inverse Laplacian, essentially a spatial integral over the whole universe). When you change your time slices, the scalar perturbations (phi, psi, E) mix into the tensor sector at second order, because the coordinate transformation itself is now first-order-times-first-order — a product of two small things, which contributes at second order. That mixing is precisely what the P ij to the lk ( sigma to the (1) l sigma to the (1) k + ...) correction term in the paper is doing: it's subtracting out the scalar leakage into the TT sector that comes from the gauge transformation.

## Assistant

Responding

Three separate claims are bundled here. Let me pull them apart one at a time.

---

## Claim 1: "The TT projection is nonlocal — it involves an inverse Laplacian"

Start with what TT projection actually *does*.

You have some symmetric tensor field $s_{ij}(\mathbf{x})$ — the spatial metric perturbation at every point in space. It contains scalar content (traces, divergences) and tensor content (the GW part). To extract the TT part, you apply a projector that removes everything with a divergence or a trace. In Fourier space, that projector is algebraic and clean. But in real space — in position space — extracting the divergence-free, traceless part requires knowing what the field is doing *everywhere*, because you need to invert the Laplacian $\nabla^2$.

Concretely: if you want to remove the scalar piece from $s_{ij}$, you subtract off terms like $\partial_i \partial_j \nabla^{-2} s$. The $\nabla^{-2}$ is the inverse Laplacian — and inverting a differential operator means solving a boundary value problem over all space. The value of the TT piece at your location depends on the field configuration at arbitrarily distant points.

This is not exotic. It's the same reason the electric field from a charge distribution depends on the *entire* charge distribution, not just what's at your location. The Coulomb potential is also built from $\nabla^{-2}\rho$.

**Why this matters for gauge dependence:** When you perform a gauge transformation — a relabeling of your coordinates — the transformation itself is a local operation. But because TT projection is nonlocal, a local change in coordinates produces a *nonlocal* change in what you call the TT part. The TT decomposition doesn't commute with the gauge transformation. At first order this is fine because the TT piece happens to be invariant anyway. At second order it isn't, and the nonlocality is part of why.

---

## Claim 2: "The coordinate transformation is first-order times first-order, which contributes at second order"

This is the heart of why second order is qualitatively harder than first order.

A gauge transformation in GR is a smooth map of the manifold to itself — a diffeomorphism. For small perturbations, you write the transformation as:

$$\tilde{x}^\mu = x^\mu + \xi^\mu$$

where $\xi^\mu$ is a small displacement vector field. Under this, a metric perturbation $h_{\mu\nu}$ transforms as:

$$\tilde{h}_{\mu\nu} = h_{\mu\nu} + \mathcal{L}_\xi g_{\mu\nu}$$

where $\mathcal{L}_\xi$ is the Lie derivative along $\xi$ — basically "how much $g$ changes if you drag it along $\xi$."

At **first order**: $\xi$ is first-order small. The Lie derivative produces first-order terms. The transformation of $h_{\mu\nu}^{(1)}$ is first-order. Everything stays in its own perturbation order. Crucially, scalars, vectors, and tensors transform *separately* — there's no mixing between sectors.

At **second order**: you need to expand to second order in perturbation theory. Now you have to include *second-order* gauge parameters $\xi^{(2)\mu}$, but you also have to account for terms that are **quadratic in the first-order gauge parameter** $\xi^{(1)\mu}$. Schematically:

$$\tilde{h}_{\mu\nu}^{(2)} = h_{\mu\nu}^{(2)} + \mathcal{L}_{\xi^{(2)}} g_{\mu\nu} + \underbrace{\mathcal{L}_{\xi^{(1)}} h_{\mu\nu}^{(1)} + \tfrac{1}{2}\mathcal{L}_{\xi^{(1)}}^2 g_{\mu\nu}}_{\text{these are first} \times \text{first}}$$

Those underbraced terms are the new thing. They are products of two first-order quantities, and they contribute at second order. They couple the *first-order scalar perturbations* ($\phi$, $\psi$, $E$, $\beta$) to the *second-order tensor perturbation* $h_{ij}^{(2)}$.

In plain language: when you change your time-slicing convention, the squeezing and stretching of your coordinate grid (which is a first-order effect) can *itself* look like a gravitational wave distortion when you square it. The universe's density fluctuations, through the coordinate transformation, fake a tensor signal. That fake signal is gauge-dependent and must be removed.

---

## Claim 3: What the correction term $P_{ij}^{\;lk}\left(\sigma_l^{(1)}\sigma_k^{(1)} + E_{,lm}^{(1)}E_{,mk}^{(1)}\right)$ is actually doing

Now the specific expression from the paper makes sense.

Recall:

$$h_{ij}^{N(2)} \equiv h_{ij}^{(2)} + P_{ij}^{\;lk}\!\left(\sigma_l^{(1)}\sigma_k^{(1)} + E_{,lm}^{(1)}E_{,mk}^{(1)}\right)$$

Each piece:

**$h_{ij}^{(2)}$** — the raw second-order TT metric perturbation in whatever gauge you're working in. This is gauge-dependent.

**$\sigma^{(1)}$** — the spacetime shear, defined as $\sigma = \beta - E'$ where $\beta$ is the vector shift and $E$ is the scalar spatial perturbation, and prime is a conformal time derivative. In Newton gauge, $\sigma = 0$ and $E = 0$ by definition. In any other gauge, they're nonzero.

**$E^{(1)}_{,lm}$** — the second spatial derivatives of the scalar metric perturbation $E$. This encodes how much spatial curvature is "hiding" in the scalar sector.

**$P_{ij}^{\;lk}$** — the TT projector. It takes whatever tensor is inside the brackets and strips out its scalar and vector parts, leaving only the TT piece.

**What the full correction term is doing:** It's computing the spurious TT signal generated by the coordinate transformation — the "fake GW" produced by squaring the first-order scalar perturbations — and subtracting it from the raw $h_{ij}^{(2)}$.

The $\sigma \sigma$ term handles the leakage from the *time-slicing* choice (the shear of your coordinate frame). The $E_{,lm} E_{,mk}$ term handles the leakage from the *spatial coordinate* choice (how you've labeled spatial points within each time slice). Together they are exactly the first-order-times-first-order quadratic terms from the gauge transformation — the underbraced terms in the schematic above — projected onto the TT sector.

The result, $h_{ij}^{N(2)}$, is what's left after that subtraction. And what's left happens to be exactly what you'd compute in Newton gauge (where $\sigma = E = 0$, so the correction vanishes trivially). The expression is not "Newton gauge" — it's a gauge-invariant quantity that *equals* the Newton-gauge value everywhere.

---

## The whole picture in one sentence

At second order, first-order scalar perturbations ($\sigma$, $E$) can masquerade as gravitational waves under a coordinate change; the correction term in the paper subtracts that masquerade by explicitly computing how much scalar content leaked into the TT sector via the $\xi^{(1)} \times \xi^{(1)}$ terms in the second-order gauge transformation, leaving a remainder that is truly coordinate-independent — and that remainder is what detectors measure.
