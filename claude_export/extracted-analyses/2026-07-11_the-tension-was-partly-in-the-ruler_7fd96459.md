---
source: claude_export
conversation_uuid: 7fd96459-e335-49bd-be52-d7906b5236fc
title: "The Tension Was Partly in the Ruler"
created_at: 2026-07-11T05:25:47.674396Z
updated_at: 2026-07-11T17:09:38.633604Z
tier: A
score: 21
n_messages: 2
---

# The Tension Was Partly in the Ruler

## Human

Analyze this paper

## Assistant

Found the primary source. Let me retrieve the full paper from arXiv.

Analyzing | Framework v3.7.1

**Access Status**
Full paper: retrieved from arXiv (2603.09270v1, HTML). Matches the published version, *Phys. Rev. D* **113**, 123538 (22 June 2026), DOI 10.1103/sbdm-9vxz.
Abstract: retrieved (arXiv + APS landing page).
Supplementary material: the uploaded Phys.org / Science X Dialog piece is an author-written popular summary; used only for framing, superseded by the full text.
Analysis basis: full text.

This is a full-length methodological cosmology paper, not a lite candidate — a six-diagnostic statistical audit with substantial interpretation — so I'm going straight to the full nine-section treatment.

---

## 1. Punchy Title & Hook

**"The Tension Was Partly in the Ruler": Auditing Whether Sign-Flipping Dark Energy Really Fixes Hubble**

A model that lets dark energy flip from *attractive* to *repulsive* mid-history does nudge predictions toward the locally measured expansion rate — but when you stop using bell-curve shortcuts and ask the model to actually *predict the data*, the Hubble tension is still standing.

---

## 2. Big-Picture Context

The Hubble tension is the field's most stubborn crack. The early universe (CMB + the physics of recombination) predicts a present-day expansion rate near 67.4 km/s/Mpc; the local distance ladder (Cepheid-calibrated Type Ia supernovae, SH0ES) measures 73.04 ± 1.04. The two disagree at 5–7σ — far past anything you can wave away as noise. A decade of proposed fixes has followed: early dark energy, modified gravity, new relativistic species, and evolving dark energy.

ΛsCDM ("Lambda-sign-CDM") is one of the cleaner proposals in that zoo. It keeps every ingredient of standard ΛCDM and adds exactly *one* parameter: a transition redshift z† (near z ≈ 2) at which the cosmological constant abruptly flips sign — negative (attractive, AdS-like) before, positive (repulsive, dS-like) after. A negative Λ in the pre-transition era shrinks the sound-horizon "measuring stick," which lets a higher H₀ fit the same CMB angular scale. Prior papers — several co-authored by Suresh Kumar, an author *here* — reported that this single knob eases both H₀ and S₈ tensions.

The stakes of *this* paper are different from "does the physics work." Its target is the **measurement of tension itself**. Most tension claims in the literature use a Gaussian shortcut: take the difference in two parameter estimates, divide by the combined error bar, read off σ. That's fine when both posteriors are tidy ellipses. It's badly misleading when one dataset (here, the supernova set PPS) has a broad, skewed, lopsided posterior and the other (CMB+BAO) is razor-tight. So the authors run *six* diagnostics — the rule of thumb, difference-in-means (DM), updated difference-in-means (UDM), a goodness-of-fit statistic (DMAP), an **exact non-Gaussian parameter shift**, and **posterior predictive consistency (PPC)** — on both ΛCDM and ΛsCDM, using Planck+ACT+SPT (CMB), DESI DR2 (BAO), and Pantheon Plus + SH0ES (supernovae).

**Paper Type & Stakes.** This is a statistical-methodology / model-diagnostics paper, not a new-physics paper. What's at stake is epistemic hygiene: whether reported "tension alleviations" for ΛsCDM (and, by extension, for the whole family of late-time dark-energy fixes) are genuine predictive improvements or artifacts of oversimplified statistics.

**Prior Belief Check.** The headline conclusion — ΛsCDM softens but does not resolve the tension — is *incremental and confirmatory*, and won't surprise tension-metric specialists. That Gaussian metrics overstate disagreement when posteriors are non-Gaussian was established by Raveri & Hu (2019) and is by now consensus machinery. What carries weight is the *direction of the self-critique*: this comes partly from inside the ΛsCDM camp, and it explicitly walks back the strength of earlier "eases both tensions" claims by showing that parameter-level tension reduction and predictive adequacy are not the same thing. The genuinely notable expert-level result is the demonstration that the CMB–DESI "tension" some worried about is largely a Gaussian-metric artifact.

**Replication & Convergence Note.** This is a single-group analysis (Plaksha + UFPR/UNILA), but it leans entirely on community-standard, independently developed tools — the Tensiometer package, the exact-shift estimator (Raveri & Hu), CLASS/MontePython, and PPC methodology validated by the DES collaboration. Independent confirmation would mean another group re-deriving the same PPC p-values and exact-shift bounds on the same public datasets with an independent pipeline; because the constraints overlap heavily with existing ΛsCDM literature, the specific *numbers* are plausible but not yet independently reproduced.

---

## 3. Necessary Background Crash-Course

**The distance ladder vs. the CMB predictor.** Think of two ways to spec a CPU's clock: read it off the design/process parameters (early-universe CMB → predicted H₀) versus put the finished part on a bench and measure it (local supernovae → measured H₀). Both are precise; they disagree by more than their combined error bars allow.
*Breaks when:* you treat these as one "true clock" plus measurement error. The disagreement may be a missing term in the *design model* (new physics between recombination and today), not a bad measurement on either end — that's the whole open question.

**The cosmological constant and the sign switch.** In standard ΛCDM, dark energy is a constant repulsive term — a fixed bias that pushes space apart. ΛsCDM makes that bias flip polarity at a threshold:

$$\frac{H^2(z)}{H_0^2} = \Omega_{\rm r0}(1+z)^4 + \Omega_{\rm m0}(1+z)^3 + \Omega_{\Lambda_{\rm s}0}\,\mathrm{sgn}(z_\dagger - z)$$

Symbol definitions:
- $H(z)$ : expansion rate at redshift z (units km/s/Mpc); $H_0$ its value today.
- $\Omega_{\rm r0},\ \Omega_{\rm m0},\ \Omega_{\Lambda_{\rm s}0}$ : today's fractional densities of radiation, matter, and the sign-switching vacuum term (dimensionless).
- $z_\dagger$ : the redshift where the sign flips (here prior-bounded to 1–3).
- $\mathrm{sgn}(z_\dagger - z)$ : +1 after the transition (z < z†), −1 before it.

What this actually means: it's a comparator with hysteresis-free threshold switching — a bias rail that reads −V for z above the trip point and +V below it. Before z†, vacuum energy *pulls* (like extra gravity); after, it *pushes* (ordinary acceleration).
*Breaks when:* you take the hard step literally. A true `sgn()` discontinuity isn't a physical field configuration; it's a stand-in for a fast-but-continuous transition, and the abrupt limit isn't even well-defined across all redshifts without embedding it in something like the VCDM framework. Perturbation behavior right at the switch is where the toy model is thinnest.

**Posterior and its shape.** A Bayesian fit doesn't return a number; it returns a probability cloud over parameter space — an error ellipsoid if you're lucky, a banana or a lopsided blob if you're not. CMB+DESI gives a tight, near-elliptical cloud; the supernova set gives a wide, skewed one.
*Breaks when:* you summarize the cloud by its center and a symmetric width. For a skewed blob, mean-and-covariance throws away exactly the information that determines whether two clouds really overlap.

**Gaussian vs. exact tension metrics.** The Gaussian metric is a matched filter that assumes white, symmetric noise: difference-in-means over combined error. The exact non-Gaussian parameter shift instead computes the *full* distribution of the parameter difference and asks how much probability sits beyond the no-shift point — no bell-curve assumption.
*Breaks when:* the matched-filter analogy tempts you to think "more rigorous = always shows less tension." Not so: the exact method can *confirm* a large disagreement (as it does for supernovae here) when the displacement is real, not just a shape artifact.

**Posterior predictive check (PPC).** This is a property-based regression test for a physical model. Treat the fitted model as a spec, generate many *replicated* datasets from it, and ask: does the actually-observed value sit in the bulk of what the model would produce, or out in the tail?
*Breaks when:* you read a tail-value p ≈ 5×10⁻⁵ as "the model is falsified." It flags that *this observable, given these calibrating datasets*, is very atypical — informative, but conditional on the priors, the datasets combined, and the discrepancy statistic chosen.

**Central analogy for this paper:** *a skewed workload fooling a naive profiler.*

---

## 4. Core Technical Explanation

The authors fit both models to three data blocks separately and jointly, then interrogate consistency two different ways: *do the datasets prefer the same parameters* (parameter-space diagnostics) and *does the fitted model predict what we actually saw* (PPC).

**Parameter-space diagnostics.** They compute the rule-of-thumb, DM, UDM (directional — it matters which dataset updates which), DMAP (goodness-of-fit at the best-fit point), and the exact non-Gaussian shift. Two comparisons dominate:

*CMB vs. DESI DR2.* In ΛCDM the Gaussian DM reads ~2.25σ — a mild but non-zero "tension." The exact non-Gaussian shift gives ~2.2σ and, in ΛsCDM, the DM collapses to ~0.06σ with the exact shift at ~0.95σ. Translation: **early and intermediate-redshift probes actually agree well**, and ΛsCDM makes them agree even better by opening a degeneracy direction the CMB already tolerates. The modest Gaussian "tension" between CMB and BAO was partly the metric's fault.

*CMB+DESI vs. supernovae (PPS).* Here the Gaussian metrics scream: DM = 5.5σ in ΛCDM, and — counterintuitively — **7.7σ in ΛsCDM**. Taken at face value, ΛsCDM looks *worse*. But the exact non-Gaussian shift returns ≥5.1σ (p < 2×10⁻⁷) in *both* models, cross-checked by a Mahalanobis distance ≈ 5.12. The supernova posterior is so broad and non-Gaussian that the Gaussian DM inflates and destabilizes; the *real*, shape-robust displacement is large but comparable across models. The disagreement is genuine (disjoint high-probability support), not a shape mirage — and it does *not* get worse under ΛsCDM the way the 7.7σ number implies.

**The predictive test (the payoff).** They run PPC on two late-time observables: H₀ and a low-redshift distance-modulus proxy μ(z=0.01).

For ΛCDM, replicated H₀ clusters near the Planck value; the observed 73.04 sits far out in the tail, giving p_ppc(H₀) ≈ 5×10⁻⁵, echoed by the joint and worst-case statistics. Crucially, μ is reproduced fine, p_ppc(μ) ≈ 0.81. So the failure is **localized to the expansion rate, not to supernova distance calibration**.

For ΛsCDM, the predictive distribution slides modestly toward higher H₀; the joint p-value improves by roughly an order of magnitude to ≈ 4×10⁻⁴ — real movement, still tiny. μ stays well reproduced. The decisive diagnosis is the **marginal-vs-joint gap**: ΛsCDM shifts the 1-D H₀ prediction upward but doesn't reorganize the *joint* (H₀, μ) structure enough to make the pair jointly typical. Marginal improvement fails to become joint consistency — which is precisely why the model *softens but never closes* the tension.

**Assumption Audit**

- **Watch:** From the popular framing, a reader assumes "ΛsCDM eases the tension" means the datasets now broadly agree. **The paper says** parameter-level tension reduction and predictive adequacy are different things: the locally observed H₀ still lands in the far tail of the model's own predictive distribution (p ≈ 4×10⁻⁴). Easing ≠ agreeing.
- **Watch:** A reader sees DM = 7.7σ for ΛsCDM vs 5.5σ for ΛCDM and concludes the sign-switch makes things *worse*. **The paper says** that flip is a Gaussian-metric artifact driven by the broad, covariance-compressed supernova posterior; the shape-robust exact shift (≥5.1σ both models) and the PPC (ΛsCDM better) show a modest *improvement*, not a regression.
- **Watch:** A reader assumes the tension being probed is "CMB vs. supernovae distances." **The paper says** the supernova distance modulus μ is reproduced fine (p ≈ 0.81); the mismatch is specifically the *expansion rate* H₀ carried by the SH0ES calibration — so blaming SN luminosity systematics misses where the failure actually lives.
- **Watch:** Given recent DESI headlines about evolving dark energy, a reader assumes CMB and DESI are themselves in tension. **The paper says** the exact non-Gaussian shift finds them excellently consistent in both models; the small Gaussian "tension" there was overstated by the metric.

---

## 5. What's Genuinely New or Clever

1. **The marginal-vs-joint predictive distinction as the diagnosis of *why* ΛsCDM stalls.** Rather than just reporting "still tense," they pinpoint the mechanism: the single late-time knob moves the 1-D H₀ prediction but can't restructure the joint (H₀, μ) geometry the calibrated distance ladder demands. That's a genuinely sharper explanation than a σ-number.
2. **Showing a tension metric can flip the *sign* of the conclusion.** The 7.7σ-vs-5.5σ inversion is a clean, concrete demonstration that a Gaussian diagnostic doesn't just mis-scale tension — it can make a helpful model look actively harmful. Pairing that with the exact shift + PPC as the corrective is the paper's most transferable contribution (new to the field's *practice*, even if each tool is individually known).

---

## 6. Limitations & Open Questions

- **The abrupt `sgn()` transition is a toy.** A physical sign switch would be fast-but-continuous, and behavior at the step (especially perturbations) is undefined in the strict limit. **(A) Consensus** — acknowledged in-paper and standard caution in this literature. (paper §II, §IV)
- **Dark energy is assumed non-clustering; only the background is modified.** Growth of structure is left to the standard equation, so any DE-perturbation signatures (relevant to S₈) are excluded by construction. **(B) Contested** — whether late-time DE perturbations matter for these tensions is genuinely debated. (paper §IV)
- **PPC is restricted to H₀ and μ(z=0.01).** A defensible focus on the Hubble tension, but a two-observable predictive test can miss failures (or successes) elsewhere in the distance–growth structure. **(B) Contested** — reasonable analysts differ on whether this is too narrow. (paper §IV)
- **DESI DR2 alone doesn't fully converge in ΛsCDM;** the authors lean on effective-sample-size arguments (R−1 up to ~1.014) rather than clean Gelman–Rubin convergence. **(B) Contested** — the ESS defense is plausible but not airtight for the weakly constrained z† direction. (paper §V)
- **z† is prior-boxed to [1,3] and lands near ~2;** whether the data *prefer* a switch or merely tolerate one there isn't cleanly separated. **(C) Speculative** — my read; a dedicated model-selection (evidence-ratio) analysis would settle it and isn't done here. (analyst inference)
- **No head-to-head against rival late-time fixes** (w₀wₐCDM, early dark energy). "ΛsCDM doesn't fully resolve it" leaves open what, if anything, does. **(C) Speculative** — the authors flag a follow-up on dynamical dark energy, so this is a scope choice, not an error. (analyst inference; paper §VII)

**12–24 month follow-ups:** smooth-transition realizations run through the identical PPC pipeline; the promised extension to dynamical-dark-energy parameterizations; and an independent group reproducing the exact-shift and PPC numbers on the same public data.

---

## 7. Detailed Summary & Explanation

*Structural note:* I reorganized around the two diagnostic *modes* (parameter-space consistency vs. predictive adequacy) rather than the paper's metric-by-metric order, because the physics lives in that split, not in the sequence of estimators.

The paper asks whether ΛsCDM's reported success at easing the Hubble tension is real or partly a statistical illusion. It constrains standard ΛCDM and its one-extra-parameter sign-switching cousin against the same modern data — the combined Planck/ACT/SPT microwave-background set, DESI's second-release baryon-acoustic-oscillation distances, and the Cepheid-calibrated Pantheon Plus supernovae that carry the high local expansion rate. It then measures "tension" six ways.

Two findings emerge, pointing opposite directions. The reassuring one: once you drop the bell-curve shortcut and use an exact, shape-aware comparison, the early- and intermediate-universe data (microwave background and baryon oscillations) agree beautifully in both models, and ΛsCDM makes them agree even better — the modest disagreement people saw there was largely the crude metric's doing. The stubborn one: the moment you fold in the local supernovae, both models genuinely fail. The sign-switch model does push its predicted expansion rate upward, and by a proper predictive test it improves on standard ΛCDM by roughly a factor of ten — but the observed local rate still sits deep in the unlikely tail of what the model predicts. Meanwhile the supernova *distances* are reproduced fine, which pins the failure specifically on the expansion rate rather than on supernova calibration.

The interpretive spine is the gap between two kinds of "success." A model can reduce the number-of-sigmas between fitted parameters (ΛsCDM does) while still failing to *predict* the observed data as a typical outcome (ΛsCDM also does). The authors show the first kind of success can even be reported *backwards* by a Gaussian metric — the sign-switch model scored a scarier 7.7σ than plain ΛCDM's 5.5σ purely because the supernova posterior is broad and skewed enough to break the approximation. The takeaway they want the reader to carry is procedural: claims that a model "resolves" a cosmological tension should be backed by exact, non-Gaussian, *predictive* diagnostics, or they risk mistaking a statistical artifact for physical insight.

Where I'm least confident in this analysis: the precise interpretation of the UDM directional numbers (e.g., the 7.6σ "PPS updated by CMB+DESI" entry) — the paper's covariance-compression explanation is plausible and I've conveyed its logic, but the exact bookkeeping of why the *updated* covariance shrinks the way it does is where the plain-language translation is doing the most compression, and a specialist should check that against Tables I–IV directly.

---

## 8. Three Crystallized Takeaways

1. **Sign-flipping dark energy nudges the universe's predicted expansion rate the right way — about a tenfold predictive improvement — but the locally measured rate is still an outlier. It softens the Hubble tension; it doesn't solve it.**
2. **How you measure a disagreement can invert your conclusion: a standard bell-curve metric rated the better model as *worse* (7.7σ vs 5.5σ), purely because the supernova data have a lopsided error cloud.**
3. **The real culprit is narrow: the microwave background and galaxy-clustering data agree fine, and supernova *distances* are reproduced fine — the mismatch is specifically the *expansion rate* carried by the local calibration.**

---

## 9. Shorter Summary

For 25 years the ΛCDM model has fit the universe well, with one glaring exception: the Hubble tension, a 5–7σ disagreement between the expansion rate predicted from the early universe (~67) and the rate measured directly from nearby supernovae (~73). One popular fix, ΛsCDM, adds a single knob — the cosmological constant flips from attractive to repulsive around when the universe was a third its present age — and earlier work reported it eases the tension.

This paper asks a sharper question: is that "easing" real, or an artifact of how cosmologists measure disagreement? Most tension claims use a bell-curve shortcut that assumes tidy, symmetric uncertainty clouds. Real data — especially the supernova set — have broad, lopsided clouds that break the shortcut. So the authors run six diagnostics on both models against the latest microwave-background (Planck/ACT/SPT), galaxy-clustering (DESI), and supernova data.

Two stories emerge. Reassuringly, once you use exact methods that don't assume bell curves, the early- and intermediate-universe data agree excellently — the modest tension seen there was largely the crude metric's fault, and ΛsCDM improves that agreement further. But add the local supernovae and both models genuinely fail. Tellingly, a standard metric even rated ΛsCDM *worse* than plain ΛCDM (7.7 vs 5.5 sigma) — a pure artifact of the skewed supernova cloud.

The decisive test asks the fitted model to *predict* the data. ΛsCDM does shift its predicted expansion rate upward and beats standard ΛCDM by roughly tenfold — yet the observed local rate still sits deep in the tail of unlikely outcomes. Supernova *distances*, by contrast, are reproduced fine, so the failure is specifically about the expansion rate, not calibration.

The broader lesson is about method: reducing the sigma-count between fitted parameters is not the same as predicting reality. Claimed breakthroughs in resolving cosmological tensions should be checked with exact, non-Gaussian, predictive diagnostics — otherwise a statistical mirage can masquerade as new physics. The Hubble tension, on this rigorous accounting, remains unsolved.

*Note on the source you uploaded: it was the authors' own Phys.org write-up. I pulled and analyzed the primary PRD paper (via arXiv) — the popular piece's framing holds up, though it soft-pedals the marginal-vs-joint predictive distinction that does the real explanatory work.*
