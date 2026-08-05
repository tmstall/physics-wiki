---
source: claude_export
conversation_uuid: 557975a4-8bca-47a5-ab0c-34893bd3f9d7
title: "Two Ways to Read a Black-Hole Census"
created_at: 2026-07-12T20:43:52.711542Z
updated_at: 2026-07-12T21:56:22.969751Z
tier: A
score: 288
n_messages: 2
---

# Two Ways to Read a Black-Hole Census

## Human

Here are two related papers. Please analyze them togetherPublication details
Cailin Plunkett et al, Signatures of a Subpopulation of Hierarchical Mergers in the GWTC-4 Gravitational-Wave Dataset, Physical Review Letters (2026). DOI: 10.1103/n6p4-ftgq

Sharan Banagiri et al, Evidence for Three Subpopulations of Merging Binary Black Holes at Different Primary Masses, Physical Review Letters (2026). DOI: 10.1103/blyb-lqv6

## Assistant

I have the Plunkett paper's arXiv ID. Let me fetch the full text and locate the Banagiri paper.

Both papers located. Let me pull the full text of each, starting with Banagiri.

Banagiri paper retrieved in full. Now the Plunkett paper.

Let me pull the astrobites explainer as a supplement while the arXiv rate limit clears.

Analyzing | Framework v3.7.1

**Access Status**
Full papers: both retrieved — Plunkett et al. from arXiv:2601.07908v2 (published *Phys. Rev. Lett.* 137, 021404); Banagiri et al. from arXiv:2509.15646v1 (published *Phys. Rev. Lett.* 137, 021403). Includes both papers' supplemental material.
Abstract: retrieved (both).
Supplementary: *APS Physics* Viewpoint (v19/96) used only as framing for the convergence context; no analytic content drawn from secondary coverage.
Analysis basis: full text of both Letters.

These were published back-to-back (021403, 021404) and cite each other — analyzing them jointly is the right call, so I've merged them into one nine-section pass and flag the structural adaptation in §7.

---

## 1. Punchy Title & Hook

**Two Ways to Read a Black-Hole Census — and They Agree on the Punchline**

Two independent teams, one agnostic and one opinionated, comb the same GWTC-4 catalog and both find that above ~40–46 M<sub>☉</sub> the black holes stop looking like collapsed stars and start looking like the *offspring* of earlier mergers — with the opinionated team catching a second, unexpected litter of them hiding down at 15 M<sub>☉</sub>.

## 2. Big-Picture Context

For a decade the field has chased a single question: how do the ~150+ merging binary black holes (BBHs) LIGO–Virgo–KAGRA has seen actually form? Two broad channels compete — *isolated binary evolution* (two stars born together, evolving into two black holes) and *dynamical assembly* (black holes meeting and pairing in dense clusters or AGN disks). The problem is degeneracy: any single event's masses and spins are usually consistent with several channels. So the field moved to *population* inference — model the whole catalog's distributions of mass, mass ratio, spin magnitude, spin tilt, and redshift, and look for structure that fingerprints a channel.

Two features have become the field's obsession. First, a **pair-instability supernova (PISN) gap**: stellar theory predicts stars can't leave black holes in roughly 45–120 M<sub>☉</sub> because the pair-instability process blows the core apart. Yet we clearly see black holes there (GW190521, GW231123). Something must fill the gap — the leading candidate being **hierarchical mergers**, where a cluster's earlier merger remnants merge *again*, stacking mass past the forbidden zone. Second, hierarchical remnants carry a spin fingerprint: because a merger dumps orbital angular momentum into the remnant, second-generation black holes spin at a characteristic **χ ≈ 0.7**, with randomized (isotropic) orientations — unlike the small, often aligned spins expected from stellar collapse.

**Paper Type & Stakes.** Both are population-inference Letters on GWTC-4 — no new detector physics, no new events; the contribution is *statistical modeling* that extracts channel structure from the existing catalog. Banagiri et al. is deliberately **phenomenological** (agnostic pattern-finding); Plunkett et al. is **astrophysically-motivated** (it builds the expected hierarchical spin signature directly into the model). What's at stake: whether the BBH population cleanly separates into formation-channel subpopulations, and whether the spin–mass structure pins down the PISN gap edge — which in turn constrains nuclear astrophysics inaccessible in any lab (see §7).

**Prior Belief Check.** Neither result overturns consensus — both *sharpen and partly reframe* an already-emerging picture. That a high-mass, high-spin hierarchical subpopulation exists near the PISN edge was already claimed by several 2024–2025 analyses (Antonini, Li, Tong, Pierra). The genuinely notable, expert-surprising pieces are narrower: (a) Banagiri's claim that the famous **~35 M<sub>☉</sub> peak** in the primary-mass spectrum may be a *model-misspecification artifact* of forcing one shared pairing function — that would unsettle a feature many treated as physical; and (b) Plunkett's **low-mass hierarchical peak at ~15.7 M<sub>☉</sub>** coexisting with a *dearth* at 20–40 M<sub>☉</sub>, which is not what a naïve "hierarchical = heavy" intuition predicts. Both are incremental-to-moderate in significance, not revolutionary.

**Replication & Convergence Note.** Each paper is a single-group analysis (Monash/OzGrav; MIT/Williams/Adler "SPINS"), so neither is independently replicated *as a whole*. But — crucially — their key transition masses have been independently recovered by multiple other groups on the same catalog, and the two papers corroborate *each other's* high-mass transition from opposite methodological directions. Independent confirmation that would raise confidence further: reproducing these transitions with (i) genuinely nonparametric mass–spin models, and (ii) the newer GWTC-5.0 events, without shared LVK selection-function inputs. The shared dependence on the same catalog, the same injection-based selection estimates, and overlapping author communities means "convergence" here is real but not fully independent.

## 3. Necessary Background Crash-Course

**Effective inspiral spin (χ_eff).** The best-measured spin combination from a GW signal.

$$\chi_{\mathrm{eff}} = \frac{\chi_1 \cos\tau_1 + q\,\chi_2 \cos\tau_2}{1+q}$$

Symbol definitions:
- $\chi_{1},\chi_2$ : dimensionless spin magnitudes (0–1) of primary/secondary (dimensionless)
- $\tau_{1,2}$ : tilt angles between each spin and the orbital angular momentum (radians)
- $q = m_2/m_1$ : mass ratio, $0 < q \le 1$ (dimensionless)

What this actually means: it's the mass-weighted projection of the spins onto the orbital axis — the *component of spin that survives averaging over an orbit*. In DSP terms, χ_eff is a **lossy scalar compression of a 6-D spin state down to one number** — like reporting only the DC/in-phase component of a signal and throwing away the quadrature. Aligned spins push it positive, anti-aligned negative, isotropic spins center it at zero.
*Breaks when:* you treat χ_eff ≈ 0 as "no spin." Isotropic *large* spins also average to zero χ_eff — the compression discards exactly the information that distinguishes "spinless" from "randomly oriented and fast."

**Effective precessing spin (χ_p).** The in-plane companion to χ_eff — the quadrature channel.

$$\chi_{\mathrm{p}} = \max\!\left[\chi_1 \sin\tau_1,\ \tfrac{3+4q}{4+3q}\,q\,\chi_2 \sin\tau_2\right]$$

Symbol definitions:
- $\sin\tau$ terms : the spin components *perpendicular* to the orbital axis, which drive precession (dimensionless)

What this actually means: χ_p captures how much the orbital plane wobbles (precesses). Together, (χ_eff, χ_p) form a **2-D signal-space diagram** — think an I/Q plane. First-generation binaries (small, roughly aligned spins) sit near the origin. Hierarchical (1G+2G) binaries, with χ ≈ 0.7 and random tilts, scatter around the **boundary of an ellipse** — major axis χ_p ≈ 0.7, minor axis χ_eff ≈ 0.47.
*Breaks when:* you read the ellipse as a hard geometric locus. It's a *probability density concentrated near* a curve, smeared by measurement error and by the spread in mass ratios and secondary spins — a fuzzy ring, not a wire.

**Hierarchical Bayesian population inference.** Every event's parameters are themselves uncertain (posterior samples, not points). You fit a *population* model whose hyperparameters describe the distributions, marginalizing over each event's uncertainty and dividing out selection effects (the detector sees heavy, nearby, aligned-spin systems more easily).
*Analogy:* it's **deconvolution with a known instrument response** — you're recovering the true source distribution after the detector's transfer function has reshaped and truncated it. The selection term is the transfer function.
*Breaks when:* your parametric model can't represent the true shape — then you get confident, precise, and *wrong* (model misspecification, which both papers explicitly worry about).

**Bayes factor (ln 𝓑).** The evidence ratio between two models, automatically penalizing complexity. ln 𝓑 ≈ 5 is "strong," ≈ 10+ is "decisive."
*Analogy:* a **likelihood-ratio test with a built-in Occam penalty** — extra parameters must pay for themselves in fit quality.
*Breaks when:* both models are misspecified; the Bayes factor tells you which of two possibly-wrong stories the data prefers, not whether either is true.

**Central analogy for this pair: the χeff–χp plane as an I/Q constellation diagram.** First-generation mergers cluster at the noisy origin; hierarchical mergers land on a constellation *ring*. Plunkett does **matched-template constellation detection** (it knows the ring shape and asks how much of the signal lands on it, as a function of mass); Banagiri does **blind change-point detection** (it scans the mass axis for where the *statistics* of q, χ, tilt, redshift suddenly shift). Carry this forward.

## 4. Core Technical Explanation

I'll organize thematically around the shared question — *where along primary mass does the population change character, and what changes* — rather than paper-by-paper.

**Banagiri's machine: blind change-point detection on the mass axis.** They take the LVK fiducial primary-mass model (a broken power law + two Gaussian bumps) and then do the clever thing: they let the *other* distributions — mass ratio p(q), spin magnitude p(χ), tilt p(cosθ), redshift p(z) — each be allowed to abruptly change shape at up to three inferred **transition masses**, carving the population into up to four subpopulations. The functional form can stay the same across a boundary; only the hyperparameters jump. This directly tests **separability** — whether p(m,q,χ,θ,z) factorizes, or whether the parameters are conditionally coupled through mass.

The data pick out **three** subpopulations with two transitions:

| | Banagiri (phenomenological) | Plunkett (hierarchical-model) |
|---|---|---|
| Low mass | **A**: m₁ ≤ 27.7 M<sub>☉</sub>, flat-ish q (β₀≈−0.8), small spin χ≤0.5; likely a *mix* of channels | Low-mass **hierarchical peak** at m_peak = 15.7₋₁.₁⁺³·² M<sub>☉</sub>; ξ≳5% (99%) in 13–20 M<sub>☉</sub> |
| Middle | **B**: 27.7–40.2 M<sub>☉</sub>, sharp q≈1 pairing (β₁≈3.6), *same* spins as A → CHE or Pop III? | **Dearth** of hierarchical mergers 20–40 M<sub>☉</sub>; inferred mostly 1G+1G |
| High mass | **C**: m₁ ≥ 40.2 M<sub>☉</sub>, broad spins with χ>0.5 support, tentative q≈0.5 → hierarchical-like | Transition at m* = 46.2₋₇.₂⁺¹²·⁶ M<sub>☉</sub>; above it ξ→1, χ_c=0.66₋₀.₂₈⁺⁰·¹⁸ |

MULTIPOP beats the no-transition fiducial at ln 𝓑 = 12.3 (decisive). The single strongest feature is that Subpopulation C has a distinct, broader spin-magnitude distribution. A striking side-result: the celebrated **~35 M<sub>☉</sub> peak in p(m₁) evaporates** once Subpopulation B is allowed its own equal-mass pairing — it reappears only if you force a shared q distribution. Banagiri argues the "peak" was partly a **pairing-model artifact**, and finds instead a tentative bump in the *secondary* mass p(m₂) near 30 M<sub>☉</sub>.

**Plunkett's machine: matched constellation detection in χeff–χp.** Rather than scan agnostically, they *encode the answer they're testing for*. They model the spin population as a two-component mixture: an uncorrelated Gaussian blob at the origin (1G+1G) plus a **density riding the ellipse boundary** (1G+2G), parameterized by characteristic spin χ_c, characteristic mass ratio q_c, and a perpendicular width. Then they let the **mixing fraction ξ(m₁)** — the hierarchical branching ratio — vary freely with primary mass via a cubic spline, *without* forcing any transition to exist.

The payoffs:
- χ_c = 0.66₋₀.₂₈⁺⁰·¹⁸, sitting right on the theoretical 0.7 — the ring is where hierarchical physics says it should be.
- ξ(m₁) climbs through 0.5 at m* = 46.2 M<sub>☉</sub> and stays consistent with unity up to ~100 M<sub>☉</sub> — above the PISN edge the population goes essentially all-hierarchical.
- A *second*, low-mass bump in ξ at 15.7 M<sub>☉</sub>, robust to dropping the two hierarchical-flagged O4b events (GW241011/241110).
- Total hierarchical fraction ξ = 0.14₋₀.₀₇⁺⁰·¹², comfortably matching the ~10–17% from cluster (CMC) simulations.
- ln 𝓑 = 14.5 vs a pure Gaussian; ln 𝓑 = 6.8 vs a *mass-independent* branching ratio — so the mass dependence of ξ is itself strongly favored.

The subtle, important result: including the hierarchical component **halves the inferred 1G+1G spin width** (σ_χeff from 0.13 to 0.07). Ignoring the hierarchical tail forces the single Gaussian to *balloon* to swallow those high-spin events — biasing your estimate of how fast first-generation black holes spin.

**Assumption Audit.**

*Watch:* A reader assumes the two papers' "three subpopulations" and "hierarchical fraction" are measuring the same thing. They aren't. Banagiri's subpopulations are defined by **abrupt statistical transitions in bulk distributions** and are *channel-agnostic* — "C" is *hierarchical-like* but Banagiri flags "curious differences" (a spin-*magnitude* jump with no spin-*tilt* jump, plus residual small-χ support). Plunkett's ξ(m₁) is a **model-imposed hierarchical-vs-not branching ratio** — it can only find what the ellipse template is shaped to find.

*Watch:* A reader assumes the low-mass ~15 M<sub>☉</sub> peak means "lots of hierarchical mergers are light." What Plunkett actually says is subtler and self-limiting: cluster simulations *predict* the 2G mass spectrum peaks near 15 M<sub>☉</sub> because low-mass first-gen black holes are abundant, so a low-mass 2G peak is *expected*. The genuinely odd part is the **20–40 M<sub>☉</sub> dearth** in between, which the paper cannot yet explain (a dip in the 1G spectrum? a 1G pileup at 35?).

*Watch:* A reader assumes Banagiri finds *no* low-mass structure, contradicting Plunkett's 15.7 M<sub>☉</sub> peak. Banagiri actually reports *broad, unlocalized* posteriors near the 10 M<sub>☉</sub> peak — hints of substructure their phenomenological transition model can't cleanly fit — and explicitly defers it. The two are *not* in direct contradiction; they're probing different observables, and Plunkett additionally folds in the two O4b events Banagiri omits.

*Watch:* A reader treats χ_p as the load-bearing novelty in Plunkett. The paper is honest that adding χ_p **does not significantly tighten** the mass-dependent hierarchical fraction over χ_eff-only. Its value is *corroborative* (the ring shows up in the precession dimension too) and *bias-reducing*, not resolution-boosting.

## 5. What's Genuinely New or Clever

**Plunkett — the ellipse-boundary template (new to the field).** Prior work compressed spins to the scalar χ_eff and hunted for a distribution that broadens with mass. Plunkett's move is to stop compressing: model the *joint* χeff–χp density as a physically-derived **arc** — the exact locus a 1G+2G population traces given χ_c≈0.7 and isotropic tilts. This is the constellation-detection upgrade: instead of asking "did the variance of the projected signal increase?", it asks "did signal power appear *on the ring I predicted*?" That's a higher-fidelity, lower-bias question, and it's why neglecting the ring biases the 1G spin width.

**Banagiri — transition masses as the primary observable, and the 35 M<sub>☉</sub> deflation (reframing).** Rather than fit features and interpret them, Banagiri makes the *locations where separability breaks* the thing to be inferred, then shows those locations independently match spin-transition and pairing-transition masses others found piecemeal. The provocative corollary — that the 35 M<sub>☉</sub> "peak" is substantially a pairing-model artifact, with the real structure sitting in secondary mass — is the paper's sharpest and most falsifiable claim.

**The joint punchline (new to the reader, emergent across both).** An agnostic scan and an opinionated template, on the same data, land the same high-mass transition (~40 vs ~46 M<sub>☉</sub>, consistent within errors) and the same high-mass spin character (χ~0.7, q~0.5). Convergence from orthogonal methods is worth more than either result alone.

## 6. Limitations & Open Questions

The parametric mass model is shared and strong, so both inherit its shape assumptions. **(A) Consensus** — both papers explicitly name model misspecification as the central caveat, and Banagiri's own 35 M<sub>☉</sub> result *is* a demonstration of how a pairing choice manufactures a feature. *(paper §Conclusion, both)*

Plunkett's hierarchical fraction rests on *identifying the ellipse component with 1G+2G mergers*. **(B) Contested** — the ellipse shape is astrophysically motivated but the paper cautions the population fraction match to cluster simulations relies on that identification plus uncertain escape-velocity/merger-rate prescriptions; AGN or CHE channels could partly occupy the same region. *(paper Discussion; broader literature)*

Banagiri's Subpopulation C shows a spin-*magnitude* transition but **no** spin-*tilt* transition, and retains small-χ support — awkward for a pure dense-cluster hierarchical origin (which predicts isotropic tilts). **(B) Contested** — Banagiri flags this and notes another group inferred a *different* tilt distribution for the same regime, suggesting the high-mass spin inference is genuinely sensitive to model choice. *(paper §Subpop C; broader literature)*

The 20–40 M<sub>☉</sub> hierarchical dearth (Plunkett) has no settled explanation. **(C) Speculative** — the paper offers a 1G-spectrum dip *or* a 35 M<sub>☉</sub> 1G pileup as alternatives but resolves neither; I'd add that it may partly reflect the ellipse template's limited leverage where 1G and 2G densities overlap most, but that's my inference. *(analyst inference)*

Both lean on the same GWTC-4 selection-function injections and exclude/include different edge events (Banagiri drops GW190814 and GW231123; Plunkett adds GW241011/241110 without the rest of O4b, a selection bias the authors acknowledge). **(A) Consensus** — differing event cuts limit how strictly the two can be cross-validated, and small-sample sensitivity at the high-mass end is universally acknowledged. *(paper §Methods, both)*

The 15.7 M<sub>☉</sub> low-mass hierarchical peak is the least independently corroborated claim. **(C) Speculative** — it survives removing the two O4b events in Plunkett's own check, but no *separate* group has confirmed a low-mass 1G+2G excess with a precessing-spin model; verify against GWTC-5.0. *(analyst inference; partial paper support)*

## 7. Detailed Summary & Explanation

Both Letters ask where, along the axis of primary black-hole mass, the merging-binary population stops behaving like a single family. Banagiri, Thrane & Lasky answer *agnostically*: they let the mass-ratio, spin-magnitude, tilt, and redshift distributions each snap to new shapes at inferred mass boundaries, and the data decisively prefer three families split at 27.7 and 40.2 M<sub>☉</sub> (decisive over a no-transition baseline). The lightest family is a probable mixture of channels; the middle family is marked by strong equal-mass pairing (hinting at chemically homogeneous evolution or Population III stars, though its ordinary spins fit those stories only loosely); the heaviest shows broad, large spins and unequal pairing — the hierarchical-merger signature, but with quirks (a spin-magnitude shift unaccompanied by a tilt shift). A memorable byproduct: the well-known 35-solar-mass bump in the mass spectrum largely dissolves once each family is allowed its own pairing rule, implying that bump was partly an artifact of over-simple modeling, with the genuine structure hiding in the *secondary* masses.

Plunkett, Callister, Zevin & Vitale answer *with a hypothesis baked in*: they model the two spin observables jointly, placing first-generation binaries as a blob near zero spin and hierarchical binaries on a predicted elliptical ring at spin ≈ 0.7, then let the hierarchical *fraction* rise and fall freely with mass. The ring lands exactly where theory expects, the hierarchical fraction crosses one-half at 46 M<sub>☉</sub> — matching the predicted onset of the pair-instability gap — and, more surprisingly, spikes again near 16 M<sub>☉</sub>, implying that both metal-rich (low-mass) and metal-poor (high-mass) star clusters feed the hierarchical population. Their sharpest methodological lesson: leaving hierarchical mergers unmodeled inflates and biases your estimate of how fast *ordinary* black holes spin.

I framed the two around the shared mass-axis question rather than paper-by-paper because that's where they illuminate each other: Banagiri finds *that* something changes near 40 M<sub>☉</sub>; Plunkett supplies a physical *why* (hierarchical takeover) and a fidelity upgrade (keep both spin dimensions). The key interpretive choice a reader must hold onto is that "subpopulation," "hierarchical fraction," and "transition mass" mean subtly different, method-dependent things in each paper — convergence on numbers doesn't guarantee convergence on mechanism. The takeaway: the high-mass hierarchical picture is now robust across orthogonal methods; the low-mass and middle-mass stories remain live and model-sensitive.

**Structural adaptation note:** I merged the two papers into a single nine-section pass and added a side-by-side subpopulation table in §4 — a deviation from single-paper structure justified by the request to analyze them jointly and by their genuine methodological complementarity. All honesty checkpoints were retained.

**Genuine Uncertainty Disclosure.** *Where I'm least confident:* the precise statistical relationship between Banagiri's Subpopulation A/B/C boundaries and Plunkett's ξ(m₁) features. I'm confident the *high-mass* transitions correspond (≈40 vs ≈46 M<sub>☉</sub>, consistent within stated intervals), but whether Banagiri's *absence* of a clean low-mass transition genuinely conflicts with, or merely fails to detect, Plunkett's 15.7 M<sub>☉</sub> hierarchical peak is something I reasoned about from the papers' differing observables and event cuts rather than from a head-to-head test either paper performs — a specialist comparing the actual posteriors could sharpen or overturn my "not contradictory" read.

## 8. Three Crystallized Takeaways

1. **Above ~45 solar masses, black holes are probably grandchildren, not children** — remnants of earlier mergers, not collapsed stars — and two teams using opposite methods on the same data now agree on it.

2. **A famous "peak" in the black-hole mass chart may be a modeling mirage.** When you stop forcing every mass to pair up by the same rule, the celebrated 35-solar-mass bump largely vanishes — a caution that some cosmic "features" live in our models, not the sky.

3. **Ignoring the exotic biases the ordinary.** Failing to account for a small hierarchical-merger tail makes garden-variety black holes look like they spin twice as fast as they do — a clean lesson in how an unmodeled subpopulation contaminates everything else.

## 9. Shorter Summary

Gravitational-wave detectors have now cataloged over 150 black-hole mergers, but a basic question lingers: how do these black holes form? Two 2026 *Physical Review Letters*, published side by side, attack it by modeling the whole population rather than individual events — and reach compatible conclusions from opposite directions.

Banagiri, Thrane, and Lasky take an agnostic approach: they let the statistical properties of the black holes (how their masses pair up, how fast they spin) abruptly change at mass boundaries the data choose. GWTC-4 decisively prefers three distinct groups, split near 28 and 40 solar masses. The lightest is a mix; the middle prefers near-equal-mass pairs (possibly from a special stellar-evolution channel); the heaviest spins fast and unequally — the hallmark of "hierarchical" mergers, where black holes that already merged merge again in crowded star clusters. A bonus finding: a well-known bump in the mass distribution around 35 solar masses may be an artifact of oversimplified modeling rather than a real physical feature.

Plunkett, Callister, Zevin, and Vitale bake the hierarchical hypothesis in. Repeated mergers leave a spin fingerprint — a characteristic spin near 0.7 with random orientations — which traces a specific curved pattern when you plot two spin measurements together. They ask what fraction of mergers sits on that pattern as a function of mass. The fraction crosses one-half at 46 solar masses, right where theory predicts a forbidden "gap" from exploding massive stars should begin — strong support for hierarchical mergers filling that gap. Unexpectedly, they find a second cluster of these repeat-mergers near 16 solar masses, suggesting both ordinary and pristine (metal-poor) star clusters contribute. Their sharpest lesson: ignoring these repeat-mergers makes ordinary black holes appear to spin far faster than they really do.

Neither result overturns the field; both sharpen an emerging consensus. The high-mass hierarchical picture is now robust across independent methods. The low-mass and middle-mass stories remain sensitive to modeling choices — the next catalog, GWTC-5.0, will test them.

---

Want me to deep-dive any mechanism — the ellipse geometry and why isotropic 1G+2G mergers trace it, the χ_eff-broadening bias, or Banagiri's Bayes-factor bookkeeping (the relative vs differential 𝓑 distinction)?
