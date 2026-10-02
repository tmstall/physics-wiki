Analyzing | Framework v3.10 | rewrite — explanatory-flow pass

**Access Status** — Full paper: arXiv HTML (ar5iv / arXiv:2604.05307v1) · Journal: *Phys. Rev. C* **114**, 024906 (published 12 Aug 2026), DOI [10.1103/r39m-l6gz](https://doi.org/10.1103/r39m-l6gz) · Abstract: cross-checked against APS/DOI landing metadata · Press note (EurekAlert) used only to confirm the ~30% central-corona figure already in the paper · Analysis basis: full text

v3.10

# 1. Punchy Title & One-Sentence Hook

**Even the Hardest Oxygen Collisions Never Fully “Boil”**

A hybrid simulation of LHC oxygen–oxygen smash-ups finds that once you make enough particles the thermalized fluid finally outproduces ordinary debris — but even in the densest events, about three particles in ten still never joined the fluid at all.

# 2. Big-Picture Context

For about twenty-five years, “make a quark–gluon plasma” meant slam the biggest nuclei you can find — gold on gold at RHIC, lead on lead at the LHC — hard enough that the overlapping soup of quarks and gluons scatters so many times it forgets how it started. Once that happens, you no longer need to track every parton by hand. You can describe the fireball with a handful of smooth fields (temperature, pressure, flow velocity) and evolve them with relativistic hydrodynamics, the same continuum language used for ordinary fluids. That story worked brilliantly for large systems.

Then small systems spoiled the plot. High-multiplicity proton–proton and proton–lead collisions started showing collective-looking “ridge” correlations that look suspiciously fluid-like, even though nobody expected a big, long-lived plasma droplet there. The field has spent a decade arguing where the transition from “spray of independent debris” to “genuine thermalized medium” actually sits — and whether it is a sharp switch or a gradual blend.

Oxygen–oxygen collisions are the newest probe of that middle ground. Oxygen-16 is deliberately awkward: big enough that you cannot dismiss it as trivial, small enough that full equilibration is not guaranteed. The LHC ran dedicated O+O (and Ne+Ne) data at $\sqrt{s_{NN}}=5.36$ TeV; experiments are already publishing geometry and flow results. There is a second motive too: $^{16}$O may be α-clustered (four helium-like clumps in a tetrahedral arrangement rather than a smooth ball), so final-state flow might image nuclear structure — but only if enough of the fireball actually behaved like a fluid that can remember the initial shape.

This paper does not measure that. Naoya Ito and Tetsufumi Hirano (Sophia University) run a phenomenological calculation timed to the new data. They ask a quantitative version of “how much of this is really plasma?”: in a model that tracks two populations event by event — a thermalized, hydrodynamically evolving **core** and a non-thermalized **corona** that fragments like ordinary vacuum debris — what fraction of the final hadrons comes from each, as a function of multiplicity and momentum?

**Paper Type & Stakes:** Theoretical / phenomenological modeling paper (hybrid Monte Carlo + hydrodynamics), not a new measurement. Stakes: turn “O+O is somewhere in between” into numbers you can falsify — and argue that pure hydro is the wrong default toolkit for this system size.

**Prior Belief Check:** Confirmatory for experts, useful for everyone else. Specialists already expected incomplete thermalization in intermediate systems and already know core–corona ideas. What is new is the concrete package for LHC O+O: crossover near midrapidity multiplicity ≈20, ~30% corona surviving even in 0–10% central events, and strange-baryon/pion ratios that rise with multiplicity but never reach a pure-core (near chemical-equilibrium) ceiling. That is incremental for the DCCI program, load-bearing for anyone about to analyze O+O with pure hydro alone.

**Replication & Convergence Note:** Single theory group applying their own previously published **DCCI2** framework (Dynamical Core–Corona Initialization, version 2 — built by Hirano’s line, Kanakubo–Tachibana–Hirano) to O+O. No independent hybrid code reproduces these exact O+O fractions in this paper. The *strategy* (core + corona) has conceptual cousins elsewhere (EPOS-style hybrids, PACIAE, and older core–corona implementations), which is convergence on approach, not on these numbers. Real confirmation looks like (a) another group’s differently built hybrid hitting similar thresholds, or (b) final ALICE/CMS/ATLAS O+O data confirming the multiplicity- and $p_T$-dependent trends.

# 3. Necessary Background Crash-Course

**Concept 1 — What “thermalization” buys you, and why it is the dividing line.**

Imagine a huge flood of nearly identical requests hitting a distributed service — so many, so fast, and so densely packed that the system’s internal state stops depending on any one request’s history. Instead you get smooth, predictable aggregates: average latency, average queue depth, average throughput. Those are quantities you can model with continuum equations instead of tracing every request by hand.

That is the computational analogue of **local thermal equilibrium** in a nuclear collision. Quarks and gluons scatter enough times that the system forgets its microscopic initial conditions and can be described by smooth collective variables — temperature, pressure, flow — which is exactly what makes hydrodynamics applicable at all. Without that forgetting, you are stuck following individual partons and string fragments. The whole “is this a plasma droplet or just debris?” debate is really a debate about whether that continuum description has earned the right to be used.

> **Breaks when:** you treat “high volume” as if it were the same thing as microscopic scattering. A loaded web service reaches predictable averages through queueing and statistics; real QCD thermalization requires actual, repeated parton–parton interactions, not merely a large particle count.

**Concept 2 — Core vs corona: two populations in the same collision.**

This paper’s central modeling idea is simple once you have Concept 1. In any given smash-up, some quarks and gluons are born in a dense enough neighborhood, with enough neighbors, that they rescatter into the smooth collective medium — the **core**. Others are born in sparse regions (edges, or just unlucky low-density patches) and never get pulled in; they fragment into ordinary hadrons the way an isolated proton–proton collision would — the **corona**.

Important: this is **not** a fixed geographic onion (hot inner sphere, cool outer shell you could draw with a compass). The split is dynamical and local. Dense patches thermalize; sparse patches do not. Even the most central, highest-multiplicity events still contain corona-classified partons mixed through the overlap region. “Core” here is a model compartment defined by deposition into a fluid, not an experimental sticker glued onto each detected hadron.

> **Breaks when:** you picture core and corona as two clean spatial zones like a star’s core and atmosphere. There is no sharp boundary you could circle on an event display; the labels are a classification from local conditions.

**Concept 3 — What DCCI2 actually is.**

**DCCI2** means Dynamical Core–Corona Initialization, version 2. It is not a universal law of nature and not an experiment. It is Hirano’s group’s previously published simulation framework: generate initial partons, let them deposit energy–momentum into a fluid when the local density warrants it, evolve that fluid with hydrodynamics, hadronize the fluid and the leftover partons separately, then (optionally) let hadrons rescatter. This paper’s contribution is applying that existing tool to LHC O+O at 5.36 TeV and reading out the core/corona budget — not inventing the two-component idea from scratch.

> **Breaks when:** you hear “DCCI2 finds 30% corona” as if every hybrid model on Earth must agree. Another framework can draw the core/corona line differently and move the number.

**Concept 4 — Strangeness as a soft thermometer of equilibration.**

Making a strange quark costs more energy than making an up or down quark. In corona-style string fragmentation, that cost is paid locally by one string — strange hadrons are relatively rare. In a hot, deconfined core full of gluons, strange pairs can be produced more efficiently through medium-assisted processes; strangeness production is, in effect, subsidized by the shared medium. So as the core fraction grows, the ratio of strange baryons (Λ, Ξ, Ω) to ordinary pions should climb. That “strangeness enhancement” pattern is one of the oldest circumstantial QGP signatures in the field. If the ratios rise but stay below a pure-core benchmark, you are watching partial equilibration — exactly the story this paper wants to tell.

> **Breaks when:** you treat the “shared subsidy” metaphor as the literal Feynman diagram. The real microphysics is specific QCD channels (e.g. gluon fusion into strange pairs in a deconfined medium); the metaphor only captures *why more core → more strangeness*.

> **Central analogy for this paper:** core as warm shared cache; corona as cold uncached fallback path.

# 4. Core Technical Explanation

Ito and Hirano run each simulated O+O event through DCCI2 as a staged pipeline. Here is what each stage is *for*, not just which package name appears.

**Step 1 — Make the initial partons.**  
They use **PYTHIA8 Angantyr**, an extension of the standard proton–proton event generator that builds a nucleus–nucleus collision as a superposition of nucleon–nucleon sub-collisions. Nuclear geometry comes from **GLISSANDO 2**, which places nucleons according to a smooth Woods–Saxon density. The authors are explicit that this is a *baseline*, not an α-clustered $^{16}$O — they want a controlled starting point for later geometry scans, not a claim about oxygen’s true shape. Soft multiparton cutoffs (`pT0Ref = 1.0` GeV) are carried over from their earlier Pb+Pb DCCI2 tune so the same framework can talk across system sizes. They bumped the parton-production PYTHIA version to 8.315 (better nuclear-profile hooks for future work) and checked that yields barely moved.

**Step 2 — Decide who joins the fluid.**  
Nonequilibrium partons continuously dump four-momentum into a medium at a density-dependent rate. Dense neighborhoods thermalize faster and grow the core; sparse neighborhoods keep streaming as corona. Those deposits source **(3+1)D ideal hydrodynamic equations** — continuum fluid evolution in three space dimensions plus time, here without viscosity. So “becoming core” in this paper means “your energy–momentum was accepted as a fluid source under DCCI2’s deposition rule,” not “a detector tagged you as QGP.”

**Step 3 — Turn fluid and leftovers into hadrons separately.**  
When a fluid cell cools below the switching temperature $T_{\mathrm{sw}}=165$ MeV (a standard QCD-crossover-scale choice), the core converts to hadrons with the **Cooper–Frye** prescription, Monte Carlo–sampled by **iS3D**. Leftover corona partons hadronize by **Lund string fragmentation** inside PYTHIA — the same mechanism ordinary pp collisions use. (Fragmentation stays on PYTHIA 8.244 for continuity with prior DCCI2 hadronization, even though initial production used 8.315.)

**Step 4 — Bookkeeping, not afterburner physics.**  
Both hadron populations go into the hadronic transport code **JAM**, but with **rescattering switched off** and only resonance decays on. That is a methodological choice: late hadron–hadron scattering would remix the labels, and the whole point of this paper is a clean core/corona yield split. The authors say rescattering barely moves integrated yields and rapidity distributions here; flow-sensitive fine structure might care more.

They generate $10^5$ minimum-bias weighted Angantyr events and report fractions versus multiplicity and transverse momentum $p_T$ (how hard a particle is kicked sideways relative to the beam).

**Worked bookkeeping — the core/corona fraction:**

$$
R_{\mathrm{core/corona}}=\frac{\langle dN_{\mathrm{ch}}/dY\rangle_{\mathrm{core/corona},\,|Y|<0.5}}{\langle dN_{\mathrm{ch}}/dY\rangle_{\mathrm{total},\,|Y|<0.5}}.
$$

**Symbol definitions:** $R$ is the fraction of midrapidity charged hadrons from that component · $dN_{\mathrm{ch}}/dY$ is charged particles per unit rapidity · $\langle\cdot\rangle$ is a PYTHIA-weighted average over events · $|Y|<0.5$ keeps you near midrapidity (sideways to the beam), away from beam-remnant junk.

**What this actually means:** it is the fraction of served requests that took the warm cached path versus the cold fallback path, measured in the quiet middle of the collision rather than in the beam-direction mess. In the most central (0–10%) class, midrapidity multiplicity reaches about **136** charged particles. With a ~30% corona floor, that is roughly **forty particles still ordinary fragmentation debris** and only about ninety-five from the thermalized fluid — even in the most violent O+O class this setup can make.

**What the plots say in prose.**  
At low multiplicity (peripheral), corona wins. The curves cross near $\langle dN_{\mathrm{ch}}/d\eta\rangle_{|\eta|<0.5}\approx 20$ — core overtakes, but never knockout-wins. Soft and intermediate $p_T$ are core-heavy (fluid-like spectra); high $p_T$ is corona-heavy (fragmentation power law). The handoff $p_T$ drops from ~3.7 GeV (0–30%) to ~2.8 GeV (30–60%); in 60–90% the core never dominates any $p_T$. Heavier species keep core dominance farther out (protons to ~5 GeV vs pions to ~3.3 GeV at 0–30%) — the fingerprint of **radial flow**, where the expanding fluid boosts heavy particles to higher momentum. Crucially, a **soft corona** survives even at $p_T\lesssim 1$ GeV, so bulk-integrated flow is not pure fluid either (prior DCCI2 work tied that soft corona to diluting $c_2\{4\}$).

Strange baryon to pion ratios rise with multiplicity (Ω most), matching the qualitative ALICE strangeness-enhancement pattern across systems — yet full DCCI2 stays **below** core-only benchmarks. Pure Angantyr (no core) is almost flat (“jet universality”). So the rise *is* the growing core fraction, and the deficit versus core-only *is* the stubborn corona.

**Assumption Audit**

> **Watch:** Reader hears “30% corona in central O+O” as a model-independent fact. **Actually:** it is the DCCI2 decomposition with a specific deposition law, ideal hydro, $T_{\mathrm{sw}}$, and Angantyr tune — a controlled estimate, not a direct observable.

> **Watch:** Reader equates “core exceeds corona above multiplicity 20” with “the system is fully thermalized QGP.” **Actually:** those are different claims; this paper supports the first and explicitly denies the second for this system size.

> **Watch:** Reader assumes Woods–Saxon oxygen geometry is the physics target. **Actually:** authors call it a consistency baseline for future profile/α-cluster scans; geometry is deliberately *not* the claim here.

> **Watch:** Reader thinks switching off hadronic rescattering is a physics prediction. **Actually:** it is an accounting choice to keep labels clean; yields may barely care, but some correlation observables might.

# 5. What’s Genuinely New or Clever

The core–corona idea is old; DCCI2 is the authors’ own prior tool. What is new *here* is narrower and more useful: the first published DCCI2 core/corona budget specifically for LHC O+O at 5.36 TeV, with multiplicity- and $p_T$-differential numbers timed to real, freshly collected data. That is new to the field as a system-specific prediction set, not as a new mechanism.

The sharper physics insight is what intermediate size buys you. In central Pb+Pb the corona shrinks to a few percent and is easy to ignore; in plain pp there is essentially no core. O+O sits where the mixture is large enough to see — turning mass-ordered $p_T$ handoffs and multiplicity-dependent strangeness into two faces of the same incomplete thermalization, rather than two unrelated mysteries.

**Predictive Content Check**

1. **Falsifiable handle:** Yes. Concrete targets once final LHC O+O analyses mature: (a) midrapidity multiplicity vs centrality near their Fig. 2 (already comparable to preliminary CMS PAS HIN-25-010); (b) strange-baryon/pion ratios that rise but undershoot pure-core expectations; (c) species-dependent $p_T$ handoffs (pion/kaon/proton scales as quoted). A pure-hydro + afterburner that matches spectra *and* drives multi-strange ratios to equilibrium without corona-like dilution would tension this picture.

2. **Formalism load:** Not really fired. The equations are bookkeeping on top of established simulation machinery. The load-bearing *physics input* is the deposition-rate definition of equilibration, not decorative math.

# 6. Limitations & Open Questions

> Core/corona fractions are framework-defined (deposition rate, ideal hydro, $T_{\mathrm{sw}}$, Angantyr `pT0Ref`). Another generator or viscous hydro-only approach can disagree on the 30% number. **(A) Consensus** — standard for dynamical models; authors frame results inside DCCI2. **(paper §§II–III)**

> Nuclear geometry is Woods–Saxon GLISSANDO, not α-clustered $^{16}$O — fine for a baseline, incomplete for the geometry program that motivates O+O. **(A) Consensus** — stated by the authors as future work. **(paper §II, §IV)**

> Ideal (not viscous) hydro for the core; shear/bulk could change how much “looks equilibrated” in soft spectra and flow. **(B) Contested** — ideal core + corona may mimic some viscous effects; specialists will ask for a viscous DCCI variant. **(analyst inference; paper uses ideal hydro explicitly)**

> Multiplicity comparison uses preliminary CMS public-analysis figures; final published data could shift absolute normalization. **(A) Consensus** — labeled preliminary. **(paper §III.1; CMS PAS HIN-25-010)**

> Single-group DCCI2 application; no second independent core–corona code on the same O+O setup in this paper. **(C) Speculative** on how much the 20 / 30% numbers move under reimplementation. **(analyst inference)**

> Exact microscopic deposition-rate kernel that decides core membership is detailed in prior DCCI2 papers more than re-derived here. **(A) Consensus** for a follow-on application paper; still the thinnest link if you need the criterion line-by-line. **(paper §II + prior DCCI2 refs)**

# 7. Detailed Summary & Explanation

Ito and Hirano ask a blunt question about the LHC’s oxygen run: how much of the produced QCD matter behaves like a locally equilibrated fluid, and how much is still ordinary fragmentation debris? They answer inside their group’s DCCI2 hybrid — a framework that, event by event, lets partons feed a hydrodynamic core or remain a stringy corona — then count final hadrons by origin with late rescattering disabled so the labels stay honest.

The story that emerges is a **partially equilibrated intermediate system**. Below midrapidity multiplicity ~20, corona production wins; above it, core wins — but never by a knockout. Central collisions still look ~30% corona. Soft $p_T$ is not pure fluid; high $p_T$ is not pure corona in a trivial way either — the handoff scale depends on centrality and hadron mass, with protons riding core radial flow farther out. Strange-baryon to pion ratios climb with multiplicity (Ω most), matching the qualitative ALICE enhancement pattern, yet remain below core-only benchmarks — chemical equilibrium is approached, not finished.

The interpretive choice that matters for reading this next to geometry-from-flow papers: treat the **persistent ~30% corona floor** as the real headline, not only the more expected “core overtakes above a threshold.” If three-tenths of the soft yield bypasses the fluid, anisotropic-flow → nuclear-shape inferences need two-component caution, not only better $^{16}$O initial conditions.

**Where I’m least confident in this analysis:** the precise density / deposition criterion DCCI2 uses to classify a parton as core versus corona — the switch behind every headline fraction — lives mostly in the group’s earlier DCCI2 papers. I followed this paper’s qualitative description and did not re-derive the four-momentum loss kernel from those references; a specialist reading the code might refine how sharp the ≈20 crossover is under parameter variation.

# 8. Three Crystallized Takeaways

1. Even in the most violent O+O class this setup can produce, roughly three final particles in ten are still ordinary vacuum-like debris — full equilibration never happens at this system size.

2. Heavier particles keep looking “plasma-like” out to higher sideways momentum than light ones, because collective radial flow in the core boosts heavy riders farther — a fluid fingerprint sitting inside a system that is still only partly thermalized.

3. The rise of strange baryons relative to pions with multiplicity is not a separate mystery; it is the growing (but still incomplete) core fraction telling the same story in a chemical language.

# 9. Shorter Summary

Physicists make quark–gluon plasma by smashing nuclei together hard enough that quarks and gluons scatter into a smooth, locally equilibrated fluid. That used to mean the biggest nuclei available — gold or lead — because you seemed to need a big fireball. Then small systems started looking collective too, and the field needed a middle-sized laboratory. Oxygen–oxygen collisions at the LHC are that laboratory: large enough to matter, small enough that full equilibration is not guaranteed.

This paper is not an experiment. Two theorists in Tokyo run their group’s DCCI2 simulation — a hybrid that splits each collision into a thermalized fluid “core” and an ordinary fragmentation “corona” — for oxygen collisions at the real LHC energy. Once a collision makes more than about twenty charged particles in a midrapidity window, the core outproduces the corona. But even in the densest events, about thirty percent of the particles are still corona. Heavier particles keep looking fluid-like out to higher momenta than light ones, a sign of collective push from the expanding core. Strange particles become more common as multiplicity rises, yet never as common as a fully equilibrated core-only world would predict.

Those numbers — the twenty-particle crossover, the thirty-percent floor, the species-dependent momentum handoffs — are concrete claims that real LHC oxygen data can confirm or overturn.

---

*Analyzer: Grok (Physics Wiki analysis pack) · 2026-08-28 · explanatory posture (peer-reviewed PRC) · rewrite after pedagogy gap vs Claude gold*

### Rubric self-score
D1 2 · D2 2 · D3 2 · D4 2 · D5 2 · D6 2 · D7 2 · D8 2 · D9 2 · D10 2 · D11 2 · D12 2  
Total: 24/24  
Production gate: PASS — full spine, frameworks explained on first use, §§3–4 teach in paragraphs, no overclaim

## Deep Dive candidates

- [ ] How DCCI2’s density-dependent deposition rate actually decides core vs corona (kernel from prior papers)
- [ ] Soft corona at $p_T\lesssim 1$ GeV and why it dilutes $c_2\{4\}$
- [ ] What changes if the core uses viscous hydro instead of ideal
- [ ] How α-clustered $^{16}$O geometry would reshape the same core/corona budget
