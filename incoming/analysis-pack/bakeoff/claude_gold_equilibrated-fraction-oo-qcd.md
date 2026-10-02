Analyzing | Framework v3.10

**Access Status** — Full paper: retrieved from arXiv HTML (ar5iv, arXiv:2604.05307v1) · Abstract: cross-checked against arXiv and APS/DOI landing metadata (*Phys. Rev. C* 114, 024906, DOI 10.1103/r39m-l6gz, published 12 Aug 2026) · Supplementary material: EurekAlert press note consulted only to frame the ~30% central-corona figure already present in the paper itself · Analysis basis: full text (arXiv HTML rendering; APS HTML blocked by Cloudflare in this environment)

---

## 1. Punchy Title & Hook

**Oxygen's Split Personality: Even the Most Violent O+O Collisions Never Fully "Boil."**

A new hybrid hydrodynamics calculation shows that even in the densest, most crowded oxygen-on-oxygen smash-ups the LHC can produce, roughly three particles in ten are still just ordinary vacuum debris — never part of the genuine, thermalized quark-gluon-plasma droplet the collision was trying to make.

---

## 2. Big-Picture Context

For the last twenty-five years, "make a quark-gluon plasma (QGP)" has meant one thing: slam two heavy nuclei — gold on gold at RHIC, lead on lead at the LHC — together at nearly the speed of light. The logic was straightforward: you need a big, dense, long-lived fireball for the strongly-interacting soup of quarks and gluons inside to bounce off each other enough times to "forget" where they started and settle into a smooth, locally-equilibrated fluid — the condition under which relativistic hydrodynamics, the theory used to describe everything from ocean currents to supernova cores, becomes a valid description of nuclear matter.

That clean story got complicated about a decade ago, when LHC experiments found flow-like, collective-looking signatures (the famous "ridge" correlations) even in small systems — high-multiplicity proton-proton and proton-lead collisions — that shouldn't have been big enough to thermalize at all. The field has spent the years since trying to figure out where, exactly, the transition from "just ordinary particle debris" to "genuine thermalized plasma" actually happens, and whether it's a sharp switch or a gradual blend.

Oxygen-oxygen (O+O) collisions, first collected in a dedicated LHC run and analyzed by experiments like ALICE, CMS, and ATLAS starting in 2025, are the field's newest tool for pinning this down. Oxygen-16 sits deliberately in between: too big to dismiss as trivially "small," too small to guarantee the enormous, comfortably-thermalized fireball of a lead-lead collision. It's also of independent interest because $^{16}$O is theorized to have a clustered internal structure — four alpha particles arranged roughly like a tetrahedron rather than a smooth ball of nucleons — which could leave fingerprints on the collision's initial geometry that a heavier, smoother nucleus wouldn't show.

This paper, by Naoya Ito and Tetsufumi Hirano at Sophia University in Tokyo, doesn't measure anything directly — it's a theoretical/phenomenological calculation, timed to land alongside the freshly collected O+O data, that asks a very specific, quantitative version of the "how much of this is really plasma?" question: using a hybrid model that explicitly tracks two separate populations of particles event by event — a thermalized, hydrodynamically-evolving "core" and a non-thermalized, ordinary-fragmentation "corona" — what fraction of the final observed particles come from each, as a function of how violent the collision is and how fast each particle is moving?

**Paper Type & Stakes:** This is a theoretical/phenomenological modeling paper — a hybrid Monte Carlo-plus-hydrodynamics calculation — built to provide quantitative, falsifiable predictions for real, newly collected LHC oxygen-oxygen data; the stakes are turning a qualitative debate ("is this small system a plasma or not?") into a specific, numbers-on-the-table answer.

**Prior Belief Check:** This result is confirmatory, not field-upending. The expectation that an intermediate-size system like O+O would show an intermediate, incompletely-thermalized mix of core and corona behavior — rather than either "fully plasma like Pb+Pb" or "no plasma at all like p+p" — is exactly what most heavy-ion theorists already expected from the trend across system sizes. Nothing here is surprising to experts in the sense of overturning a consensus view. What's genuinely useful is that this paper turns that qualitative expectation into specific numbers (a multiplicity threshold near 20, a persistent ~30% corona floor at the highest achievable O+O multiplicities) that can be directly checked against data, rather than leaving the question as a vague "somewhere in between."

**Replication & Convergence Note:** This is a single theory group's calculation (Ito & Hirano, using their own previously-published DCCI2 framework) with no independent hybrid-model cross-check yet of these specific O+O numbers. The general core-corona concept itself is well-established and used across multiple independent frameworks in the literature (EPOS, PACIAE, and other hybrid approaches), which is a form of conceptual convergence — but that's convergence on the modeling *strategy*, not on this paper's specific quantitative predictions. Genuine independent confirmation would look like either (a) another group's differently-built hybrid model (say, an EPOS4 or AMPT-based calculation) reproducing similar core/corona fractions and thresholds for the same O+O system, or (b) the real ALICE/CMS/ATLAS O+O data — already collected as of this paper's writing — directly confirming the predicted multiplicity- and momentum-dependent trends once fully analyzed.

---

## 3. Necessary Background Crash-Course

**Concept 1 — What "thermalization" buys you, and why it's the dividing line.**

Think of a huge, sustained flood of nearly-identical requests hitting a distributed system — so many, so fast, and so densely packed that the system's internal state stops depending on any individual request's specific history and instead settles into smooth, predictable aggregate behavior: average latency, average queue depth, average throughput — quantities you can model with a handful of continuum equations instead of tracing every request by hand. That's the computational analogue of "local thermal equilibrium": enough repeated interaction among the constituents (quarks and gluons, in this case) that the system forgets its specific initial conditions and can be described by smooth, collective variables like temperature and pressure — which is exactly what makes hydrodynamics (a theory built for smooth, continuous fluids) applicable to it at all.

**Breaks when:** you push it to ask what's actually producing the smoothing. A heavily-loaded system reaches predictable aggregate statistics through queueing and averaging, not because individual requests are physically colliding with and altering each other the way QCD partons genuinely scatter off one another thousands of times per femtosecond. The analogy is about *statistical* behavior emerging from many interacting units, not literal thermal contact — real thermalization in QCD matter requires actual, repeated microscopic collisions, not just high volume.

**Concept 2 — Core vs. corona: two populations riding through the same collision.**

Here is the paper's actual central mechanism. In any given collision, some quarks and gluons happen to be produced in a dense enough region, surrounded by enough neighbors, to rescatter repeatedly and get pulled into the smooth, collectively-flowing thermalized medium — the **core**. Others are produced in sparser regions (near the edges, or simply where the local density happens to be lower on that particular event) and never get pulled in; they just fragment on their own into hadrons, exactly the way an ordinary, isolated proton-proton collision would produce particles — the **corona**. Crucially, this is not a fixed geographic split (a hot inner sphere versus a cooler outer shell you could point to in space); it's decided dynamically, collision by collision, by local density, so even the most central, highest-multiplicity events still have corona-classified partons scattered through them.

**Breaks when:** you try to picture "core" and "corona" as literally two separate physical zones, like the core and atmosphere of a star. There is no clean boundary — a given event's core and corona partons are interleaved throughout the collision region, and the split is a *classification*, applied after the fact based on local conditions, not a spatial partition you could draw a line around.

**Concept 3 — Strangeness enhancement: why "weirder" particles show up more in bigger collisions.**

Producing a strange quark–antiquark pair costs more energy than producing an up or down pair, because the strange quark is heavier. In an isolated, "one string pays its own way" fragmentation process — the corona's mechanism — that cost is a real tax, and strange particles come out relatively rarely. In a hot, deconfined medium full of freely available gluons — the core's environment — strange pairs can be produced efficiently through gluon-fusion-type processes that don't have to be paid for by a single string alone; strangeness production gets, in effect, subsidized by the shared medium. So as a collision produces more core (more thermalized medium) relative to corona, the ratio of strange particles to ordinary pions should climb — this is one of the oldest and most trusted signatures of QGP formation in the field, going back to the 1980s and 1990s.

**Breaks when:** you try to extend the "shared cost" framing into an actual mechanism. The real physics is specific QCD processes (thermal gluon-gluon fusion into strange quark pairs, efficient in a deconfined medium) — not a literal cost-sharing arrangement. The economic metaphor captures *why more strangeness appears with more core*, not *how* it's actually produced at the parton level.

**Central analogy for this paper:** Core is warm cache; corona is cold fallback.

---

## 4. Core Technical Explanation

The calculation runs through a specific pipeline called **DCCI2** (Dynamical Core–Corona Initialization, version 2) — a tool Hirano's group had already built and published before this paper, here applied for the first time specifically to O+O collisions at 5.36 TeV per colliding nucleon pair, matching the real 2025 LHC O+O run:

**Step 1 — Generate the initial partons.** PYTHIA8's Angantyr module (an extension of the standard proton-proton event generator to full nuclear collisions) combined with GLISSANDO 2 (a Monte Carlo model of nuclear geometry, using a smooth Woods-Saxon density profile) produces the initial quarks and gluons for a simulated O+O collision, event by event.

**Step 2 — Classify and split.** Based on local parton density, each patch of the event is dynamically tagged as core-like (dense enough to thermalize) or corona-like (too sparse). Core partons deposit their energy and momentum as source terms feeding a genuine (3+1)-dimensional relativistic hydrodynamic fluid; corona partons are set aside to fragment independently.

**Step 3 — Evolve and hadronize separately.** The hydrodynamic core evolves until it cools to a switching temperature of 165 MeV (a standard QCD-crossover-scale value used across the field), then converts to individual hadrons via the Cooper-Frye prescription, sampled with the iS3D Monte Carlo tool. The corona partons, meanwhile, fragment via the ordinary Lund string model — the same mechanism PYTHIA uses for plain proton-proton collisions, unmodified.

**Step 4 — Combine and finish.** Both hadron populations (from core and from corona) are passed through the JAM hadronic transport code, but with full hadronic rescattering deliberately switched off — only resonance decays are applied. This is a specific methodological choice: leaving rescattering on would let core and corona hadrons interact with each other after formation, blurring the clean bookkeeping ("this particle came from the core, that one from the corona") that the whole analysis depends on.

Once every event is run this way, the authors compute, as a function of collision centrality (how head-on/violent the collision was) and particle momentum, exactly what fraction of the final observed particles trace back to the core versus the corona.

**Worked equation — the core/corona fraction:**

$$R_{\text{core/corona}} = \frac{\left\langle \dfrac{dN_{ch}}{dY} \right\rangle_{\text{core (or corona)},\,|Y|<0.5}}{\left\langle \dfrac{dN_{ch}}{dY} \right\rangle_{\text{total},\,|Y|<0.5}}$$

**Symbol definitions:**
$R_{\text{core/corona}}$ : the fraction of the observed charged-particle yield attributable to the core (or, separately, the corona)
$dN_{ch}/dY$ : the number of charged particles produced per unit of rapidity (a coordinate roughly tracking how far along the beam direction a particle is heading)
$\langle \cdot \rangle$ : an average taken over many ($10^5$) simulated collision events
$|Y|<0.5$ : restricted to particles near mid-rapidity — roughly perpendicular to the beam — the region least contaminated by leftover beam-fragment effects

**What this actually means:** This is exactly like measuring, in a system handling a mixed workload, what fraction of served requests came from the "hot," cached, high-throughput code path versus the "cold," uncached fallback path — snapshotted in the steady middle of a session rather than during startup or shutdown transients (mid-rapidity, versus the beam-remnant-contaminated edges).

**Concrete numbers:** in the most central (0–10%) O+O collisions modeled, the total midrapidity charged-particle yield is about 136 particles. With the paper's reported ~30% corona floor persisting even here, that means roughly 41 of those 136 particles are still ordinary vacuum-fragmentation debris, and only about 95 come from the genuinely thermalized fluid — even in the single most violent class of collision this system can produce.

**Assumption Audit**

> **Watch:** The reader might assume "core-dominated" is synonymous with "fully thermalized, textbook QGP behavior." The paper is explicit that even in the highest-multiplicity O+O collisions accessible, roughly 30% of the yield is still corona — full equilibration is never reached for this system size. "Core exceeds corona" (the ≈20-multiplicity threshold) and "the system is fully thermalized" are two different claims, and this paper only supports the first.

> **Watch:** The reader might assume switching off hadronic rescattering in Step 4 is a minor numerical convenience. It's actually load-bearing for the entire analysis: it's the specific choice that makes clean core/corona bookkeeping possible at all. The paper describes the effect of leaving it off as "minor," but that claim isn't independently demonstrated within the material retrieved here — it's worth flagging as an assumption resting on the authors' own characterization rather than something this analysis could verify directly.

> **Watch:** The reader might assume the precise algorithm for classifying a given parton or fluid cell as "core" versus "corona" is spelled out in this paper. It isn't, in the material retrieved — DCCI2's exact density-based classification criterion is presumably detailed in Hirano's group's earlier DCCI2 publication, which this paper builds on rather than re-derives. This analysis infers the general density-threshold logic from the standard core-corona literature rather than from an explicit statement in this specific paper.

---

## 5. What's Genuinely New or Clever

The core-corona concept itself is not new — it's roughly fifteen years old, and DCCI2 is the authors' own previously-published tool, not introduced here. What's new in *this* paper is narrower and more concrete: it's the first application of a dynamical, event-by-event core-corona hybrid model specifically to the brand-new LHC O+O collision system, producing multiplicity- and momentum-differential quantitative predictions timed to match real, freshly collected experimental data. That's new to the field in the sense of being the first such number set for this specific system — not a new theoretical mechanism.

The more genuinely interesting physics insight is what falls out of applying an existing tool to a genuinely intermediate-size system: because O+O collisions are small enough that the core and corona never fully separate the way they effectively do in central Pb+Pb (where corona shrinks to a few percent, easily ignored), the mixing itself becomes directly visible and measurable — turning two historically separate observables (the mass-ordered momentum thresholds where core-dominance gives way to corona-dominance, and the multiplicity-dependent strangeness enhancement pattern) into two faces of the same underlying core/corona mixture. O+O collisions function as a kind of magnifying glass for a mixing effect that's usually too small to see clearly in either extreme (p+p or Pb+Pb).

**Predictive Content Check**

1. **Falsifiable handle (always):** Yes, and it's concrete. The paper commits to specific, checkable numbers: a multiplicity threshold near $\langle dN_{ch}/d\eta\rangle \approx 20$ where core exceeds corona; a persistent ~30% corona floor at the highest O+O centralities; transverse-momentum crossing points near 3.7 GeV (0–30% centrality) and 2.8 GeV (30–60%); and mass-ordered core-dominance thresholds (pions to about 3.3 GeV, kaons to about 3.8 GeV, protons to about 5 GeV). All of these are numbers that the real ALICE/CMS/ATLAS O+O data — already collected — can directly confirm or contradict once fully analyzed.
2. **Formalism load:** Not fired. This paper doesn't lean on novel mathematical structure to generate its claims — the equations here are bookkeeping definitions (the fraction ratios above) layered on top of established, previously-published simulation machinery (PYTHIA, hydrodynamics, JAM). There's no heavy formalism whose necessity needs interrogating; the paper is an application study, not a formalism-driven one, so this half of the check is skipped as not applicable.

---

## 6. Limitations & Open Questions

> The nuclear geometry model (GLISSANDO 2's Woods-Saxon density profile) is, by the paper's own description, "primarily optimized for heavier nuclei," yet applied here to light $^{16}$O — a nucleus with a theorized clustered (four-alpha, roughly tetrahedral) internal structure that a smooth Woods-Saxon profile doesn't capture. **(A) Consensus** — the tension between smooth-density nuclear models and oxygen's debated cluster structure is an actively discussed issue in the field (it's part of the motivation for the dedicated LHC O+O run in the first place). **(paper's own acknowledgment + broader literature)**

> Hadronic rescattering was switched off specifically to preserve clean core/corona bookkeeping, with the paper describing its omitted effect as "minor." **(B) Contested** — this is a reasonable simplification for the analysis's purposes, but "minor" is the authors' characterization rather than something independently quantified in the material available here; a specialist could reasonably ask for a direct with/without comparison. **(paper's own claim, not independently verified in this reading)**

> String fragmentation uses an older PYTHIA version (8.244) while parton production uses a newer one (8.315) — described by the paper as a "methodological compromise for consistency" with prior DCCI2 work. **(B) Contested** — mixing generator versions is a defensible continuity choice, but it introduces a version mismatch whose quantitative impact isn't independently assessed in this paper. **(paper's own acknowledgment)**

> This is a single theory group's calculation with no independent hybrid-model cross-check of these specific O+O numbers yet. **(A) Consensus** — this is a standard, uncontroversial epistemic point about early-stage phenomenological predictions made ahead of, or alongside, the data they're meant to describe. **(analyst inference)**

> The absolute size of the "core fraction" — including headline numbers like the ~30% corona floor — is somewhat framework-dependent: different core-corona implementations (EPOS, PACIAE, and others) can, in principle, classify the same collision differently and arrive at different exact splits for otherwise similar physics. **(C) Speculative** — this is a general critique known in the broader core-corona literature rather than something this specific paper addresses or that this analysis could confirm with a direct side-by-side comparison. **(analyst inference)**

---

## 7. Detailed Summary & Explanation

Ito and Hirano set out to answer a specific, quantitative version of a question the heavy-ion physics community has been circling for a decade: as collision systems get smaller than the traditional gold-gold or lead-lead heavyweights, how much of what comes out is genuine, thermalized quark-gluon plasma, and how much is just ordinary particle-physics debris along for the ride? Using their own previously-developed DCCI2 hybrid model — which explicitly, event by event, splits produced partons into a thermalized "core" that gets handed to relativistic hydrodynamics and a non-thermalized "corona" that fragments the same way an isolated proton-proton collision would — they simulate oxygen-oxygen collisions at the LHC's actual 2025 run energy and track exactly how the core and corona contributions shift with collision violence (centrality) and particle momentum.

The headline finding has two parts. First, there's a real, well-defined threshold: once a collision produces more than about 20 charged particles per unit of rapidity near mid-rapidity, the core outweighs the corona — genuine collective, thermalized behavior starts to dominate. Second, and more strikingly, that dominance is never complete: even in the single most violent class of O+O collisions the LHC can currently produce, roughly 30% of the final particles are still corona — still, in effect, ordinary fragmentation debris, not plasma. This is a genuinely quantitative statement, not just a qualitative "it's somewhere in between" — and it distinguishes O+O sharply from central lead-lead collisions, where the corona fraction shrinks to a few percent and is often simply neglected.

The paper backs this up with two further, internally consistent observations. Looking at particle momentum rather than just overall multiplicity, core-dominance persists to higher momenta for heavier particles (protons stay core-like out to roughly 5 GeV, versus about 3.3 GeV for pions) — the signature of collective, hydrodynamic radial flow, where heavier particles get pushed to higher momenta by the same underlying expansion velocity. And looking at strange-particle production, the ratio of strange baryons (Lambda, Xi, Omega) to pions climbs steadily with increasing multiplicity — the classic strangeness-enhancement signature long used as circumstantial evidence for QGP formation — but that climb never reaches the value predicted for a purely core (fully thermalized) system, exactly mirroring the persistent corona floor seen in the multiplicity analysis. The two observables (momentum-dependent core dominance and strangeness enhancement) turn out to be two views of the same underlying mixture, rather than two independent phenomena requiring separate explanations.

The key interpretive choice made in this summary is to treat the ~30% corona floor as the paper's real headline result, rather than the more expected-sounding "core exceeds corona above a threshold" finding — because the persistence of a substantial non-thermalized component, even at maximum achievable violence for this system size, is the specific, falsifiable, quantitative claim that real O+O data can most directly test.

**Where I'm least confident in this analysis:** the precise algorithm DCCI2 uses to classify a given parton or fluid cell as "core" versus "corona" — the actual density threshold or criterion driving the split shown in every headline number in this paper — was not present in the material retrieved for this analysis. I've inferred the general density-based logic from the standard core-corona literature rather than from an explicit statement in this specific paper's text, so if DCCI2's actual classification criterion differs from that inferred picture in some material way, that's the piece of this analysis most likely to be off. This reading also relies on an AI-mediated extraction of the arXiv HTML rather than a direct read of the raw source by me, which carries a small residual risk that some emphasis or wording was compressed or reworded in the fetch, though the specific numeric values reported were internally consistent.

---

## 8. Three Crystallized Takeaways

1. Even in the single most violent oxygen-oxygen collisions the LHC can currently produce, roughly three particles in ten are still ordinary "vacuum" debris, not part of a genuine thermalized quark-gluon-plasma droplet — full equilibration simply never happens at this system size.

2. Whether a given particle looks like it came from a plasma or from plain old fragmentation depends on how heavy and how fast it is: heavier particles (protons) keep looking plasma-like out to much higher speeds than light ones (pions), because collective flow in the plasma gives heavier riders a bigger momentum boost — a fingerprint of real collective behavior hiding inside a system that's still mostly not thermalized.

3. The well-known "stranger particles show up more often in bigger collisions" pattern isn't a separate mystery needing its own explanation — it falls straight out of the fact that bigger, denser collisions simply contain a larger (though still incomplete) fraction of genuinely thermalized matter mixed in with ordinary fragmentation.

---

## 9. Shorter Summary

Physicists make quark-gluon plasma — a hot, deconfined soup of quarks and gluons thought to have filled the universe microseconds after the Big Bang — by smashing heavy atomic nuclei together at nearly the speed of light. For twenty-five years, that meant colliding the biggest nuclei available, like gold or lead, because you need a big, dense, long-lived fireball for the plasma to actually reach thermal equilibrium — the condition needed for it to behave like a smooth, flowing fluid rather than a spray of independent particles. Then physicists found flow-like signatures even in surprisingly small collisions, like proton-proton, complicating the picture.

Oxygen-oxygen collisions, newly collected at the Large Hadron Collider starting in 2025, sit deliberately in between — small enough to study cleanly, potentially large enough to form real plasma. This paper, by two theorists in Tokyo, doesn't run an experiment; it runs a detailed computer simulation that explicitly splits each simulated collision's output into two populations: a genuinely thermalized, fluid-like "core," and an ordinary, non-thermalized "corona" that behaves just like debris from an isolated particle collision.

The result: once a collision is violent enough to produce more than about twenty particles in a certain measurement window, the thermalized core outweighs the corona. But even in the single most violent oxygen-oxygen collisions modeled, roughly thirty percent of the particles produced are still corona — ordinary debris, never fully absorbed into the plasma. That's a sharp contrast with collisions between much bigger nuclei like lead, where the corona shrinks to almost nothing.

The simulation also shows that heavier particles, like protons, keep looking plasma-like out to much higher speeds than lighter particles like pions — a signature of the plasma's collective flow physically pushing heavier riders faster. And the well-known tendency for "stranger," more exotic particles to appear more often in bigger collisions turns out to be the same story told a different way: bigger collisions simply have a larger, though still incomplete, thermalized-plasma fraction mixed into their debris.

Because this uses newly collected LHC data as its point of comparison, the predictions here — the twenty-particle threshold, the thirty-percent floor, and the specific momentum thresholds where each particle type stops looking plasma-like — are concrete, checkable claims that real experimental measurements can directly confirm or overturn in the near future.
