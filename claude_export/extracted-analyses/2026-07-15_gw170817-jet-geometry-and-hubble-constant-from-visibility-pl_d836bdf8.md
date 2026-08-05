---
source: claude_export
conversation_uuid: d836bdf8-8690-4233-a09f-81202c805b37
title: "GW170817 jet geometry and Hubble constant from visibility-plane fitting"
created_at: 2026-07-15T19:47:55.377173Z
updated_at: 2026-07-15T21:27:26.481352Z
tier: A
score: 265
n_messages: 4
---

# GW170817 jet geometry and Hubble constant from visibility-plane fitting

## Human

Analyze this paper

## Assistant

**Access Status** — Full text provided directly (ApJ 1005:93, open access, CC BY 4.0). No retrieval needed. Analysis basis: full text including all appendices, tables, and figures.

---

## 1. Punchy Title & One-Sentence Hook

**The Universe's Only Good Ruler Just Got Recalibrated — And It Sided With Planck**

By fitting relativistic jet models directly to the raw interferometer samples instead of to a reconstructed radio image, this team squeezed the jet geometry of GW170817 to sub-degree precision — and found that the resulting Hubble constant, 65.5 ± 4.4 km s⁻¹ Mpc⁻¹, sits almost on top of the early-Universe Planck value, in the wrong place for a late-Universe measurement that was supposed to agree with SH0ES.

---

## 2. Big-Picture Context

**Paper Type & Stakes:** This is a methods-driven observational cosmology paper that re-analyzes an existing, irreplaceable dataset with a better statistical engine and better forward models. What's at stake is the only distance-ladder-independent, electromagnetically-identified standard siren humanity possesses — and whether it can say anything useful about the Hubble tension.

The Hubble tension is now the most durable crack in ΛCDM. Planck's CMB-based inference gives H₀ = 67.4 ± 0.5; SH0ES's Cepheid-calibrated supernova ladder gives 73.04 ± 1.04. These are two very different measurement stacks with different systematics, and they disagree at roughly 5σ. The field badly wants a third, structurally independent method — one that doesn't touch Cepheids, doesn't touch the CMB, and doesn't inherit either one's error model.

Gravitational-wave standard sirens are exactly that. General relativity encodes the luminosity distance *directly* into the waveform amplitude — no rungs, no calibration chain, no distance ladder. But GW170817, the one and only "bright" siren (with an identified host galaxy, NGC 4993, and therefore a redshift), suffers from a nasty degeneracy: the strain amplitude scales roughly as cos ι / D_L, so a face-on binary at 45 Mpc and a moderately inclined binary at 40 Mpc look nearly identical to LIGO. You break that degeneracy by measuring both GW polarizations — but Hanford and Livingston are nearly coaligned, and the event was near face-on, which is precisely the geometry where the two polarizations are hardest to separate. The loudest events are the least informative about inclination. That's the trap.

The escape route is electromagnetic. The merger launched a relativistic jet, and the jet axis should track the orbital angular momentum axis. VLBI can watch the jet's radio afterglow centroid crawl across the sky at apparently superluminal speed, and that apparent speed encodes the viewing angle. Mooley et al. (2018, "M18") did this first with two epochs; Hotokezaka et al. (2019) folded the result into H₀ and roughly doubled the precision; Ghirlanda et al. (2019, "G19") added a higher-resolution epoch; Mooley et al. (2022, "M22") added an HST kilonova position as a day-0 anchor and got θ_v ≈ 21.9°, H₀ = 71.5 ± 4.6. Meanwhile, analyses based on the *unresolved* light curve (Palmese et al. 2024) reported θ_v ≈ 30° and H₀ ≈ 75. Two families of methods, two answers, and the disagreement traces to how each treats the late-time afterglow.

What nobody had done: use all four astrometric epochs at once, fit a *continuum* of physically-simulated jet geometries rather than a handful of discrete models, fit in the visibility plane instead of the deconvolved image plane, and marginalize honestly over the peculiar-velocity systematic. This paper does all four.

**Prior Belief Check.** The *methodology* here is an unambiguous improvement and will be received as such — nothing in it is controversial. The *result* is more interesting. H₀ = 65.5 ± 4.4 is not a surprise to specialists who have been paying attention: Howlett & Davis (2020) already got 64.8 ⁺⁷·³₋₇·₂ by combining a similarly small viewing angle with Bayesian-model-averaged peculiar velocity corrections. So the low central value is largely a *rediscovery* under a much better geometry engine, not a new claim. What genuinely raises eyebrows is the internal tension: this analysis prefers D_L = 44.0 ± 1.6 Mpc, more than 1σ above the surface-brightness-fluctuation distance of 40.7 ± 2.4 Mpc to the same galaxy. Since SBF is Cepheid-calibrated, a distance-ladder-free method disagreeing with the ladder *on the same galaxy* is the more provocative sentence in this paper, and it's buried in §4.2. The headline "we're 0.5σ from Planck, 1.7σ from SH0ES" is honest but should be read as calibrated-and-consistent rather than as evidence: at 6% precision, this measurement cannot adjudicate a 9% argument. It is a vote, not a verdict, and the authors say so.

**Replication & Convergence Note.** This is a single-group analysis of a dataset that *every* competing analysis also uses — the same four sky positions from the same three VLBI epochs plus HST. That makes the literature's apparent convergence much weaker than it looks: these are not independent measurements, they're correlated re-analyses of one event. The partial exception is Govreen-Segal & Nakar (2023), who fit the *same* hydro model to image-plane centroids and got θ_v = 19.4° ± 2.1°, agreeing closely — but that tests the fitting method, not the model. Genuine independent confirmation would require (a) a second bright siren with a resolvable jet, or (b) an independent group re-reducing the raw correlated visibilities with a different hydro model family. The paper actually demonstrates why (b) matters: their independent re-reduction of the G19 global-VLBI data landed 0.46/0.48 mas away from M22's version of the same observation, and they note that M22's day-207 position could not be adequately fit at all.

---

## 3. Necessary Background Crash-Course

**Standard sirens and the distance–inclination degeneracy.**

A compact binary radiates gravitational waves whose amplitude at Earth depends on how far away it is and how it's tilted. For a near-face-on system:

$$h \;\propto\; \frac{\cos\iota}{D_L}$$

**Symbol definitions:**
- $h$ : strain — the fractional length change the detector measures (dimensionless, ~10⁻²¹ here)
- $\iota$ : inclination — angle between the orbital angular momentum vector and the line of sight (degrees)
- $D_L$ : luminosity distance to the merger (Mpc)

**What this actually means:** GR hands you a *product*, not two separate numbers. This is the classic differential-signaling problem. GW170817 delivers two polarization channels (plus and cross), and their *ratio* encodes ι while their *common* scale encodes 1/D_L. Hanford and Livingston are nearly coaligned — electrically, they're two receivers wired onto the same side of a differential pair. You recover the common-mode sum with terrific SNR (32.4σ) and almost none of the differential information that would separate the two.

**Breaks when:** you push the analogy toward "just add another receiver." A third detector helps only if it's *both* sensitive enough *and* rotated enough — Virgo's near-null detection contributed sky localization but little inclination leverage. Worse, the cos ι terms mean the polarizations become intrinsically similar as the system goes face-on, which is exactly when the event is loudest and most detectable. The wiring isn't the whole problem; the source geometry conspires against you. Adding all five second-generation detectors would help, but the network is throttled by its least sensitive member and its combined duty cycle.

**The uv-plane, and why "the image" is a lie.**

A radio interferometer does not take pictures. Each pair of antennas measures one complex number — a *visibility* — which is a single sample of the 2D spatial Fourier transform of the sky brightness, at a spatial frequency set by the baseline's projection onto the sky. Earth rotation drags those sample points along arcs, so you accumulate a sparse, irregularly-scattered set of Fourier samples. An "image" is what you get after inverse-transforming that sparse spectrum (producing a mess convolved with an ugly sidelobe-riddled point spread function) and then running CLEAN — a nonlinear, non-unique, heuristic sparse-recovery deconvolution — to guess what was there.

**Analogy:** it's like reconstructing a waveform from a handful of scattered, unevenly-spaced DFT bins, then measuring a feature on the reconstruction with calipers. Every prior analysis of GW170817's afterglow position did exactly this: CLEAN the data, fit a single circular Gaussian to the resulting blob, read off the centroid, and then fit *that number*. The right move — and what this paper does — is to push the model forward into the sampled Fourier domain and compare there, where the noise is nearly white, the sampling function is known exactly, and no deconvolution assumption has been injected.

**Breaks when:** you assume the visibility-domain noise is perfectly white and diagonal. It isn't. Per-antenna gain and phase errors, ionospheric delay residuals, and imperfect calibration all inject correlated, baseline-dependent errors — which is precisely why this paper carries per-epoch nuisance parameters for flux scale and astrometric offset rather than trusting the calibration. The Fourier domain is *cleaner*, not clean.

**Apparent superluminal motion, and the two geometry knobs.**

A jet with Lorentz factor Γ ≈ 5–10 pointed near your line of sight nearly keeps up with its own photons. The emitting material chases the light it emitted, so the observer's clock runs compressed by a factor of roughly (1 − β cos θ), and the transverse displacement per unit *observed* time is inflated well past c. GW170817's afterglow centroid moved ~2.5 mas in ~155 days, an apparent transverse speed of ~4c.

**Analogy:** a messenger sprinting a route while carrying the news of his own departure. He arrives barely after the announcement of his start, so from your seat he appears to have covered the ground impossibly fast. The "speed" you infer isn't anyone's speed — it's an artifact of the compressed arrival schedule.

**Breaks when:** you treat the moving thing as a point. It isn't. The observed centroid is the flux-weighted centroid of an extended, angularly structured, decelerating shock, whose brightness distribution changes shape between epochs. The apparent proper motion is not the velocity of any material element, and the centroid is not a landmark. That's the entire reason this paper models *images* rather than *points* — and why the paper explicitly warns that the image-plane crosses in Figure 2 "should not be taken as the 'true' or 'best' positions."

The geometry factorizes beautifully. Rather than fitting the viewing angle θ_v and the core opening angle θ_cp separately, the paper fits two derived combinations:

- **θ_v − θ_cp** (the difference) → controls how much proper motion you see. This is what the centroid displacement measures, and it's constrained *tightly* (to ~±1°).
- **θ_v / θ_cp** (the ratio) → controls the angular *size* of the afterglow. This is what only high-resolution baselines and the light-curve peak width can measure, and it's constrained *loosely*.

**Peculiar velocities.**

To get H₀ you need the host's recession velocity due purely to cosmic expansion. What you measure is total velocity: Hubble flow plus the galaxy's own motion through its group, plus the group's coherent drift toward nearby large-scale structure. At 40 Mpc, cz ≈ 3000 km/s and peculiar velocities are ~300 km/s — a 10% contaminant.

**Analogy:** clocking a conveyor belt by timing a passenger who is also walking around on it. The closer you stand, the more his walking dominates your estimate of the belt.

**Breaks when:** you assume you can average the walking away over many passengers. Peculiar velocities are *spatially correlated* — nearby galaxies share bulk flows — so the errors on multiple standard sirens don't beat down as 1/√N. Blake & Turner (2024) estimate this may double the number of sirens needed below 100 Mpc.

**Central analogy for this paper: fit the raw Fourier samples, never the developed picture.**

---

## 4. Core Technical Explanation

### 4.1 The measurement, stripped down

The entire cosmological result rests on four numbers on the sky, listed in the paper's Table 2:

| Day | Instrument | What it is |
|---|---|---|
| 8 | HST | Kilonova position = the merger location (day 0 anchor) |
| 75 | HSA VLBI | Afterglow centroid, 58 μJy |
| 207 | Global VLBI | Afterglow centroid, 47 μJy, **S/N 4.3** |
| 230 | HSA VLBI | Afterglow centroid, 48 μJy |

Total angular excursion: about 2.5 milliarcseconds. That's the width of a human hair at ~1500 km. Everything downstream — jet geometry, luminosity distance, the Hubble constant — is leveraged off those four dots and their error ellipses.

### 4.2 The forward model

For each proposed parameter vector, the pipeline does this, per epoch:

1. Generate a model afterglow image from the Govreen-Segal & Nakar (2023) 2D relativistic hydrodynamic library, scaled to the proposed geometry and epoch (details in §4.3).
2. Normalize the image, multiply by a global flux scale F₀ and a per-epoch fractional flux nuisance term (1 + δ_F,i).
3. Hand it to **GALARIO** — a GPU-accelerated tool borrowed from the protoplanetary-disk community — which rotates the image by the position angle, Fourier transforms it, and samples the result at the *exact* uv coordinates of that epoch's real observation.
4. Translate the model visibilities by (R.A._off + δ_ra,i, decl._off + δ_dec,i), where the δ terms absorb per-epoch astrometric systematics.
5. Compute χ² against the real visibilities.

Sum the χ² across epochs, multiply by −0.5, and that's the log-likelihood. Nested sampling (DYNESTY via BILBY) explores the space and returns both posteriors and Bayesian evidence.

The key architectural insight: **the comparison happens in the domain where the data actually live.** No CLEAN, no deconvolution settings, no circular-Gaussian approximation. And critically, this retains the *size* information — the visibility amplitudes on the longest baselines encode the afterglow's angular extent, which a centroid fit throws away entirely. That's what gives the ratio θ_v/θ_cp any traction at all.

### 4.3 The genuinely clever part: model scaling

You can't run a relativistic hydro simulation inside a likelihood function. You'd need a dense grid over (jet energy profile, core opening angle, viewing angle, time) and you'd still only sample the space finitely. The authors instead exploit a self-similarity in the physics.

Govreen-Segal & Nakar showed that afterglow images are *invariant* for jets sharing the same θ_v/θ_cp ratio, when observer time is measured in units of the light-curve peak time t_p. So one simulated family, indexed by primed parameters, can be rescaled to any desired (t_obs, θ_v, θ_cp, t_p):

$$\ell \;\longrightarrow\; \ell \times \frac{t_{\rm p}}{t_{\rm p}'} \times \frac{(\theta_{\rm v}' - \theta_{\rm cp}')}{(\theta_{\rm v} - \theta_{\rm cp})}$$

**Symbol definitions:**
- $\ell$ : model image pixel length scale (cm, later converted to angle via D_L)
- $t_{\rm p}$, $t_{\rm p}'$ : desired and simulated afterglow light-curve peak times (days post-merger)
- $\theta_{\rm v}$, $\theta_{\rm cp}$ : desired viewing angle and core opening angle at peak (degrees)
- primed quantities : the corresponding values in the stored simulation

**What this actually means:** it's a lookup table plus a similarity transform. Rather than caching every possible jet, you cache one normalized family and apply a coordinate rescaling — exactly the move you'd make with a normalized design curve, or with a cached basis you rotate into on demand rather than recomputing. The stored library gets picked by nearest ratio, linearly interpolated in time, and stretched. Cost per likelihood evaluation drops from "impossible" to "an interpolation and an FFT." The images are downsampled 400×400 → 80×80 (~100 μas per pixel) to keep the FFT cheap — comfortably finer than the ~3–7 mas beam.

The library covers one top-hat jet and three power-law energy profiles (E_iso ∝ θ⁻ᵇ, with b = 3, 4, 6), and is validated only for θ_v < 0.75 rad — a hard prior boundary in the fit.

### 4.4 The ladder of fits (Figure 1)

This is the most instructive figure in the paper. Four corner plots, each adding information:

| Panel | Data | Ratio prior | θ_v/θ_cp | θ_v (68%) |
|---|---|---|---|---|
| A | days 0, 75, 230 | flat | 15.6 ⁺⁶·²₋₇·₆ | 14.6–18.3° |
| B | days 0, 75, 230 | light curve | 8.0 ⁺²·⁶₋₂·₇ | 15.5–19.4° |
| C | days 0, 75, 207, 230 | flat | **5.6 ⁺⁵·⁷₋₂·₃** | 18.2–22.2° |
| D | all four | light curve | 6.2 ⁺²·²₋₂·₀ | **18.3–20.3°** |

Read the ratio column. Without day 207, the ratio is essentially unconstrained — a flat smear from 5 to 25. Adding day 207 collapses it, for two reasons the authors identify: (i) three VLBI epochs constrain the *deceleration* of the centroid, not just its displacement, and (ii) the global-VLBI beam is ~3× finer north–south, so it can discriminate against models whose afterglow has bloated. Panel D is the money result: θ_v = 18.3–20.3°, θ_cp = 2.3–4.7°.

Also note the difference parameter θ_v − θ_cp barely moves across all four panels (15.0–15.8°, ±1°). The centroid motion nails the difference immediately and the entire argument is about pinning the ratio.

### 4.5 Bolting on cosmology

The final tier adds three parameters (H₀, D_L, cz) and three likelihoods:
1. **GW likelihood** — a KDE over the LIGO/Virgo (θ_JN, D_L) posterior. Figure 7 shows what GW data alone says: D_L = 40.1 ⁺⁴·²₋₆·₈ Mpc, and a viewing angle sprawling from ~15° to ~45°. That banana is the degeneracy this whole paper exists to cut.
2. **Redshift likelihood** — the observed heliocentric group velocity against catalog values.
3. **Peculiar velocity likelihood** — the hard part. They run **28 combinations** of galaxy-group catalog × peculiar-velocity reconstruction (from PVHUB), and combine the 28 posteriors weighted by Bayes evidence — Bayesian model averaging.

Result: H₀ = 65.5 ± 4.4, D_L = 44.0 ± 1.6, θ_v = 16.8–19.2°.

Notice what the VLBI constraint does to the GW banana: forcing θ_v ≈ 18° instead of the GW-preferred ~30° slides you along the degeneracy from D_L ≈ 40 to D_L ≈ 44. That extra 3.3 Mpc is where the low H₀ comes from — H₀ = cz_cosmo/D_L, so a bigger distance at fixed velocity is a smaller Hubble constant.

### 4.6 The error budget — read this twice

The paper's own decomposition of the ~6% total uncertainty:

| Source | Fractional contribution |
|---|---|
| Peculiar velocity of NGC 4993 | **0.05** |
| GW amplitude SNR (32.4σ event) | 0.03 |
| Viewing angle (±1° around 18°) | **0.01** |

The jet geometry — the subject of this entire 20-page methodological effort — is now the *smallest* term. It has been optimized past the point of mattering for this event.

### Assumption Audit

**Watch:** Reader likely assumes that because the improved VLBI geometry is what's new here, the improved geometry is what drove H₀ down to 65.5. The paper actually says the *value* was largely already visible: Howlett & Davis (2020) reported 64.8 ⁺⁷·³₋₇·₂ using Hotokezaka's older, cruder viewing angle with the same Bayesian-model-averaging peculiar-velocity treatment. The gap to M22's 71.5 is dominated by the peculiar-velocity methodology plus the ~3° smaller viewing angle, and the paper's contribution is a **1.6× tightening** of the error bar (±7.2 → ±4.4), not a new central value. This is a precision paper masquerading, in the abstract, as a discovery paper.

**Watch:** Reader likely assumes the headline viewing angle θ_v = 18.3–20.3° is distance-ladder-independent, since that's the whole point of standard sirens. It isn't. That number assumes D_L = 40.7 Mpc, the SBF distance from Cantiello et al. (2018) — which is **Cepheid-calibrated**. The paper is scrupulous about this (§4.2) and provides the ladder-free version (16.8–19.2°), but the abstract leads with the ladder-dependent number "as used in most previous analyses." Worse, this creates a subtle circularity across the literature: M22's θ_v assumed the SBF distance, and when this paper imposes a SH0ES prior on H₀, it recovers larger viewing angles more consistent with M22 — exactly as you'd expect if both are inheriting the same Cepheid scale.

**Watch:** Reader likely assumes more VLBI epochs is uniformly better, and that a 4.3σ detection can't matter much. Neither holds. Removing day 230 entirely produces a *negligible* change in θ_v. Removing the HST day-0 anchor blows the difference parameter from 16° ± 1° to 19° ± 2° and opens θ_v to 18.4–23.9°. And the day-207 point — detected at **S/N 4.3**, source unresolved, deconvolved Gaussian size consistent with zero — is what constrains the ratio and pulls the viewing angle up by a full 1σ. The single most influential VLBI epoch in this analysis is a marginal detection.

**Watch:** Reader likely assumes the jet model family choice (top-hat vs. power-law b = 3, 4, 6) is a physically meaningful fitted result. The paper reports Bayes factors of 0.39–1.38 across all four — statistically indistinguishable, "insignificant evidence" on the Jeffreys scale they adopt. The reason is physical: after t_obs > 0.5 t_p the emission is dominated by jet-core material near the line of sight, so the angular structure washes out of the images. This is convenient (the geometry result is robust to the model family) *and* damning (the data cannot test the jet structure it depends on). The authors flag this and note the fix for future events: get a VLBI epoch before 0.5 t_p.

---

## 5. What's Genuinely New or Clever

**1. The model-scaling formalism is the real invention (new to the field).** Turning a finite hydro simulation library into a continuous, differentiable-enough parameter space by exploiting the (θ_v/θ_cp, t/t_p) invariance is the move that makes everything else possible. Previous work faced a brutal choice: use physically faithful hydro models but sample only a handful of discrete geometries by brute force (M18: five models), or sample a continuum but with semianalytic synthetic models of lower fidelity (Hotokezaka 2019). This gets both — full 2D relativistic hydrodynamics *and* nested sampling over a continuum. That's a genuine methodological unlock, and the authors correctly note it generalizes to any GRB, not just GW170817.

**2. Visibility-plane fitting of a GRB afterglow (new to this subfield, standard elsewhere).** GALARIO is a disk-imaging tool; forward-modeling into the uv-plane is routine at ALMA. Bringing it to milliarcsecond GRB astrometry is what's new, and the payoff is concrete: it retains the source-size information that centroid fitting discards, which is the only reason the θ_v/θ_cp ratio is measurable at all from these data. The comparison to Govreen-Segal & Nakar (2023) — same physical model, image-plane centroid fitting, θ_v = 19.4° ± 2.1° vs. this paper's 18.3–20.3° — is the clean control experiment. Consistent results, but this paper is 1.5× more precise than M22.

**3. Two quiet forensic findings.** The independent re-reduction of the G19 global-VLBI data revealed that M22's version of the day-207 position sits 0.46/0.48 mas away and *cannot be adequately fit* by any model in the family. And the DIFMAP rounding bug (fixed May 2019) meant M18 and M22 published beam sizes underestimated by 6.6%. Neither is headline material; both are the kind of thing that only surfaces when someone actually re-does the reduction from the correlator output. This is an argument for exactly the sort of independent replication the field is short on.

**4. Appendix D is unusually honest.** Voluntarily quantifying how your own prior parameterization biases your headline result is not standard practice. More on this below.

---

## 6. Limitations & Open Questions

**The peculiar velocity of NGC 4993 is a hard floor that this paper does not lower.** It contributes 5% of the 6% total. The 28 catalog × reconstruction combinations swing H₀ by up to ~1σ (~4 km s⁻¹ Mpc⁻¹), and the Bayes evidence cannot discriminate among them (max ln B = 1.8, "marginal"). Bayesian model averaging over models you can't distinguish is a defensible convention, not a derivation. *(A) Consensus — the paper states this explicitly and quantifies it, and every prior GW170817 H₀ paper hits the same wall; it is the field's agreed-upon bottleneck for nearby sirens.* **(paper §4.3)**

**The choice of 150 km s⁻¹ for the peculiar velocity uncertainty is conventional rather than derived.** The authors test 250 km s⁻¹ and find <1% change, which is reassuring but tests only the width, not the centroid, of the correction. *(B) Contested — reasonable cosmologists disagree about whether reconstruction-based corrections at 40 Mpc are trustworthy at all, versus whether the 150 km s⁻¹ convention adequately captures reconstruction bias.* **(broader literature)**

**The implied-prior correction is asserted, not demonstrated, for the fits that produce the headline number.** This one deserves care. The fit parameterizes in (θ_v − θ_cp, θ_v/θ_cp), but reports θ_v, recovered algebraically:

$$\theta_{\rm v} \;=\; (\theta_{\rm v} - \theta_{\rm cp}) \times \frac{r}{r-1}, \qquad r \equiv \theta_{\rm v}/\theta_{\rm cp}$$

**Symbol definitions:**
- $r$ : ratio of viewing angle to core opening angle at light-curve peak (dimensionless)
- $\theta_{\rm v} - \theta_{\rm cp}$ : the angle difference the centroid motion actually constrains (degrees)

**What this actually means:** this is a change of variables with a non-trivial Jacobian, and flat priors do not survive the transformation. As r → ∞, θ_v collapses onto the difference; as r → 1, θ_v blows up. A flat prior over r ∈ [1, 25] therefore piles almost all its mass at θ_v ≈ difference, silently pushing the posterior toward small viewing angles — a gauge choice masquerading as ignorance. Appendix D confirms it: correcting to the physically desired prior (uniform in cos θ_v, i.e. isotropic) *broadens* and *shifts* the four-epoch posterior from 18.0–22.4° to 18.2–25.3°, ~3° wider at the top. The direction matters enormously: larger θ_v → smaller D_L → **larger** H₀, toward SH0ES. The authors then state that "where informative, Gaussian priors on θ_v/θ_cp are used in our fits, no such corrections are required." That's plausible — a data-driven prior isn't an ignorance prior — but the Jacobian doesn't vanish just because the ratio prior got narrower, and no corrected posterior is shown for the light-curve-informed case. *(C) Speculative — the paper explicitly raises and analyzes this issue in Appendix D and its argument is defensible; I am extrapolating that a residual correction survives into the informative-prior fits, and a specialist in prior-volume effects may well know this is a second-order effect once r is pinned to 6.2 ± 2.*  **(paper Appendix D + analyst inference)**

**D_L = 44.0 ± 1.6 Mpc vs. the SBF distance 40.7 ± 2.4 Mpc to the same galaxy is unresolved.** ~1.2σ in quadrature — not alarming in isolation, but it is the *entire* source of the low H₀, and the SBF distance is Cepheid-calibrated. If SBF is right, H₀ climbs to ~71. The paper flags it in one paragraph and moves on. *(B) Contested — the paper notes the discrepancy and calls it "important to carefully consider," but whether it signals an SBF systematic, a jet-model systematic, or is simply a 1σ fluctuation is genuinely open.* **(paper §4.2)**

**Model misspecification: standard jet models fail on the late-time (≳350 day) light curve.** The origin of the excess flux — merger remnant? kilonova afterglow? missing jet physics? — is unknown. The authors' defense is solid: their data all sit at ≤230 days, where geometry dominates over model detail, and their results shift only ~1% under uninformed priors on the ratio and a range of t_p. But the light-curve-informed prior on θ_v/θ_cp comes from Makhathini et al. (2021)'s analysis of the panchromatic curve out to 940 days — which includes the regime where the models fail. *(A) Consensus that late-time excess is real and unexplained; (C) Speculative that it contaminates the imported prior.* **(paper §4.3, broader literature, + analyst inference)**

**Every analysis here assumes the jet launches along the orbital angular momentum axis.** Müller et al. (2024) show that misalignment biases H₀ nonlinearly downward. The authors estimate a ~−10° misalignment would push their posterior to the SH0ES value — i.e., a single unverified geometric assumption is worth the entire result. There is no observational handle on this for GW170817. *(A) Consensus — universally assumed and universally acknowledged as unverified.* **(paper §4.3, broader literature)**

**This is one event, and the literature's agreement is an illusion of independence.** All GW170817 H₀ measurements share the same four sky positions, the same GW posterior, and largely the same peculiar-velocity machinery. The scatter across the literature (64.8 to 75.5) reflects analysis choices, not measurement noise. *(A) Consensus — the paper implicitly acknowledges this by calling for more sirens.* **(broader literature)**

**What the next 12–24 months should tackle:** the O4/O5 bright-siren drought is the real problem and nobody can fix it by analysis. Actionable items are (i) an independent group re-reducing GG084a and the HSA data with a different hydro family, (ii) a proper treatment of *correlated* peculiar velocities for multi-siren combination (Blake & Turner 2024), which may double the ~12-siren requirement for 2% precision below 100 Mpc, and (iii) resolving the SBF vs. GW+VLBI distance discrepancy to NGC 4993, which is tractable *now* with existing data and is arguably the most interesting loose thread here.

---

## 7. Detailed Summary & Explanation

GW170817 remains the only gravitational-wave merger with an identified host galaxy, and therefore the only one that can deliver a Hubble constant without leaning on either the cosmic microwave background or the Cepheid distance ladder. Its weakness has always been geometric: the gravitational waveform's amplitude confounds distance with orbital tilt, and the LIGO network is oriented in the one way that cannot separate them for a face-on event. The fix has been to watch the merger's relativistic jet with very long baseline interferometry — the jet points along the orbital axis, and the apparent superluminal drift of its radio afterglow across the sky encodes how far off-axis we're looking.

This paper rebuilds that measurement from the correlator output up. Three things change. First, the fitting happens directly on the interferometer's raw complex measurements rather than on centroids extracted from deconvolved images. That preserves the afterglow's *angular size*, which turns out to be the only thing constraining one of the two geometric parameters. Second, instead of a handful of pre-computed jet simulations, the authors exploit a scaling symmetry in relativistic hydrodynamics to turn one simulation family into a smooth continuum of jet geometries that a sampler can explore. Third, they include every astrometric epoch that exists — including a marginal day-207 detection that they re-reduced themselves and that turns out to matter more than any other VLBI point — and they marginalize over 28 different plausible corrections for the host galaxy's motion through its neighborhood rather than picking one.

The result: a viewing angle of 18.3–20.3° at the conventionally-assumed distance, or 16.8–19.2° when the distance is fitted directly, and H₀ = 65.5 ± 4.4 km s⁻¹ Mpc⁻¹. That's within half a sigma of Planck's early-Universe value and 1.7σ below SH0ES's late-Universe value — which is the wrong side of the fence for a late-Universe measurement, and mildly awkward for any explanation of the Hubble tension that invokes new physics acting recently.

I've framed this as a precision paper rather than a discovery paper because the paper's own numbers demand it. The interpretive choice that matters most: I've weighted the error budget (§4.6) more heavily than the abstract does. The jet geometry — the entire subject of the work — contributes 1% of a 6% error, behind the gravitational-wave amplitude's 3% and the host galaxy's peculiar velocity at 5%. A comparable H₀ value with a comparable peculiar-velocity treatment already existed in Howlett & Davis (2020). What's new is the robustness and a 1.6× tighter error bar, arriving at exactly the moment it stops helping. That's not a criticism of the authors, who say all of this plainly in §4.3 and §5 — it's the honest shape of the result, and the reason their concluding message is aimed at *future* events. The methods here are a gift to the next bright siren, not to this one.

The loose thread I'd chase: the fitted luminosity distance of 44.0 ± 1.6 Mpc against the surface-brightness-fluctuation distance of 40.7 ± 2.4 Mpc to the same galaxy. That gap is where the low Hubble constant lives, and the SBF value is Cepheid-calibrated. A distance-ladder-free method disagreeing with the ladder on a single, nearby, extremely well-studied galaxy is a more testable claim than anything in the abstract.

**Where I'm least confident in this analysis:** the model-scaling formalism in §2.4 — specifically, how faithfully the (θ_v/θ_cp, t/t_p') invariance holds across the interpolation, and how much error the nearest-neighbor ratio selection plus linear time interpolation injects into the model images. The paper delegates validation entirely to Govreen-Segal & Nakar (2023), which I have not read, and I am taking the invariance claim on authority. Since this scaling is the load-bearing element that makes the entire continuous fit possible, an error there would propagate straight into θ_v and hence H₀ without appearing anywhere in the quoted uncertainties. My secondary soft spot is the Appendix D prior-volume argument: I'm confident the Jacobian effect is real and directionally toward larger θ_v (the paper demonstrates it), but I'm genuinely unsure whether it survives at a meaningful level once the informative light-curve prior pins the ratio to 6.2 ± 2 — the authors say no, they may well be right, and I'm pattern-matching from general Bayesian reparameterization arguments rather than having done the integral.

---

## 8. Three Crystallized Takeaways

**1.** The only gravitational-wave measurement of the Universe's expansion rate that comes with a known address now reads 65.5 ± 4.4 — closer to the early-Universe answer than the late-Universe one, which is the wrong result for anyone hoping new physics explains the Hubble tension. But at 6% precision it cannot settle a 9% argument. One vote, not a verdict.

**2.** The thing limiting our best standard siren isn't gravity, isn't jet physics, and isn't the telescope. It's that we don't know how fast one galaxy is drifting through its own neighborhood. At 40 Mpc, local traffic drowns out the Hubble flow — and because galaxies drift *together*, this error won't average away by collecting more sirens.

**3.** A radio interferometer doesn't take pictures; it samples the sky's Fourier transform. Everyone before fit models to the reconstructed image. This team fit them to the raw samples instead, bought a 1.5× tighter jet angle — and their own error budget shows that improvement is now the smallest term in the answer. The technique's real payoff is waiting for the next bright siren.

---

## 9. Shorter Summary

The merger of two neutron stars in 2017 remains the only gravitational-wave event whose home galaxy we can name. That makes it the only one that can measure how fast the Universe expands without relying on either the cosmic microwave background or the century-old chain of stellar distance calibrations — the two methods that currently disagree by about 9% and have refused to reconcile for a decade.

The catch is geometric. A merger's gravitational-wave loudness depends on both its distance and its orientation, and the detectors are arranged in the one configuration that can't separate the two for a face-on system. The workaround: the merger fired a jet nearly at the speed of light, and radio telescopes spanning the globe watched the jet's glowing debris drift across the sky by about two and a half thousandths of an arcsecond — a hair's width at fifteen hundred kilometres. How fast it appears to drift reveals how far off-axis we're looking, which unlocks the distance.

This team rebuilt that measurement from scratch. Radio telescope arrays don't actually take pictures; they collect scattered samples of the sky's spatial frequencies, and turning those into an image requires guesswork. Every previous analysis measured the jet's position on the guessed-at image. These authors compared their physics simulations directly to the raw samples, skipping the guess — which also preserved information about the glow's *size*, something everyone else had thrown away. They also found a mathematical shortcut that turned a small library of expensive simulations into a smooth continuum of possible jet shapes, and they folded in every observation that exists, including one marginal detection they re-processed themselves that proved unexpectedly decisive.

Their answer for the expansion rate, 65.5 with an uncertainty of 4.4, lands almost exactly on the early-Universe value and somewhat below the late-Universe one — an awkward result for anyone hoping recent new physics explains the disagreement.

Two honest caveats. The precision, roughly 6%, is too coarse to settle a 9% argument. And their own accounting shows the jet geometry they worked so hard to nail contributes just 1% of that error. The real bottleneck is that we can't tell how fast the host galaxy is drifting through its own neighborhood. This paper's methods are a gift to the next bright siren, whenever one arrives.

## Human

Every prior analysis of GW170817's afterglow position did exactly this: CLEAN the data, fit a single circular Gaussian to the resulting blob, read off the centroid, and then fit that number. The right move — and what this paper does — is to push the model forward into the sampled Fourier domain and compare there, where the noise is nearly white, the sampling function is known exactly, and no deconvolution assumption has been injected.

## Assistant

Correcting | Framework v3.7.1

That passage is wrong, and specifically wrong about M18 — which is the one prior analysis that matters most for the claim.

**What M18 actually did.** From Gourdji's own Appendix A.1: M18 represented the nonzero pixels of their five 2D hydro afterglow model images as a collection of delta-function components and fit *those to the observed visibilities* by brute force, using Levenberg–Marquardt via `modelfit` in DIFMAP, with R.A., decl., PA, and flux scale free. That is forward-modeling into the uv-plane. The circular Gaussian in M18 was a **yardstick**, not a measurement — they perturbed a best-fit circular Gaussian by 0/1/2/3σ and recomputed χ² purely to establish a goodness-of-fit reference scale for the model χ² values. I collapsed the yardstick into the measurement.

**Corrected taxonomy:**

| Analysis | Fitting domain | Actual limitation |
|---|---|---|
| M18 (2018) | **Visibility plane** (DIFMAP `modelfit`, delta components) | 5 discrete models; LM point estimates; no evidence; no per-epoch nuisance params; PA range too narrow |
| Hotokezaka (2019) | Image-plane centroids | Semianalytic synthetic models |
| M22 (2022) | Image-plane centroids | Single fixed peculiar velocity; centroid-only |
| Govreen-Segal & Nakar (2023) | Image-plane centroids | Point-source approximation of the same hydro models |
| **Gourdji (2026)** | Visibility plane, GALARIO | — |

Gourdji is precise about this in the intro and I wasn't: they describe prior work as *either* semianalytic-model fitting *or* limited parameter-space sampling, and then separately note that previous studies used centroid positions only. M18 falls in the second bucket, not the third.

**What this costs the analysis.** §5 item 2 — "visibility-plane fitting of a GRB afterglow (new to this subfield)" — is the casualty. It isn't new; M18 did it on this exact dataset eight years earlier. GALARIO's contribution is throughput, not domain: DIFMAP's direct DFT over delta components and GALARIO's FFT-plus-uv-interpolation compute the same quantity, but nested sampling needs ~10⁵–10⁶ likelihood evaluations and M18 needed five LM runs. The GPU is what makes the *continuum* tractable. So the visibility plane isn't the axis of novelty against M18 — it's a precondition that M18 already satisfied. The real novelty compresses to one thing: **the model-scaling formalism plus Bayesian sampling with nuisance parameters over a continuum of geometries.** §5 item 1 absorbs the whole weight.

**The tell I walked past.** Gourdji's Appendix A.1 forensic result — that M18's A25 χ² minimum was never actually located because the explored PA range was too small — only makes sense if M18 was fitting in the visibility plane. You can't under-explore PA in a centroid fit; PA isn't a parameter there. That finding is a direct indictment of M18's *parameter coverage and optimizer*, not its choice of domain. It was sitting in my own §5 item 3 while §3 said the opposite.

**Central analogy status:** keeping it locked, per the framework, but its domain narrows. "Fit the raw Fourier samples, never the developed picture" is the correct frame for the Hotokezaka → M22 → GS&N lineage — which is the lineage the *H₀ literature* actually ran on, so it still carries §4.5 and §4.6. It does not discriminate Gourdji from M18. The sharper frame for that comparison would be *sample the continuum, don't grid-search five points* — noted for next time, not swapped in now.

Good catch. My §3 sentence generalized "every prior analysis" from the three papers that were salient to me and never checked it against the appendix I'd already read.
