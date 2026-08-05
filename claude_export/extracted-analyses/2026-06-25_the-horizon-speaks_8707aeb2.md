---
source: claude_export
conversation_uuid: 8707aeb2-ca5e-47a9-8f39-cd1938fb30a3
title: "The Horizon Speaks"
created_at: 2026-06-25T02:25:19.142709Z
updated_at: 2026-06-25T04:02:31.329959Z
tier: A
score: 72
n_messages: 12
---

# The Horizon Speaks

## Human

Analyze this paper

## Assistant

The framework is confirmed via the in-context document (the PDF renders as binary via view, but the full text was provided inline in the conversation). The paper is paywalled at Nature — triggering the retrieval protocol.

I have the full paper. Now let me also fetch the theoretical predecessor (Oshita et al. 2025, arXiv:2509.09165) to properly characterize the theory side.

I now have everything needed for a thorough analysis. Let me also check the independent confirmation paper.

Good enough — the independent confirmation is already cited in the search results above (arxiv:2606.06592, "Measuring a Black Hole's Area Immediately after Merger"). I have everything needed.

---

**Access Status**
Full paper: retrieved from arXiv:2510.01001v1 (HTML)
Abstract: retrieved (also from arXiv abstract page)
Supplementary/Methods: retrieved — full Methods section included in arXiv HTML
Note: The Nature version (published 24 June 2026) adds the Kerr-consistency result in the abstract as "full agreement with theoretical predictions for a Kerr black hole," but the core analysis is the October 2025 arXiv preprint. The analysis below draws on both.
Analysis basis: full text (preprint) + Nature abstract update

---

## Section 1 — Punchy Title & One-Sentence Hook

**The Horizon Speaks: Gravitational Waves Carry the Fingerprint of a Newborn Black Hole's Surface of No Return**

For the first time, physicists have pulled a signal directly encoding a black hole horizon's rotation rate and surface gravity out of LIGO data — not from the ringdown's familiar quasinormal-mode spectrum, but from a brief burst of "direct waves" emitted as the infalling companion was swallowed alive.

---

## Section 2 — Big-Picture Context

**Paper Type & Stakes:** This is an observational discovery paper reporting the first detection of a predicted gravitational-wave component (the "direct wave") that directly encodes horizon properties, using GW250114 — the loudest binary black hole merger ever recorded. The stakes are high: if confirmed, this opens a qualitatively new window onto near-horizon physics and the ergosphere, distinct from and complementary to quasinormal-mode spectroscopy.

For the past decade, the gold standard of post-merger gravitational-wave physics has been quasinormal-mode (QNM) spectroscopy — essentially treating the ringing remnant black hole like a struck bell and reading off its mass and spin from the characteristic tone and decay of the ringing. The analogy is powerful but has a key limitation: QNMs are tied to the *light ring* (a region of unstable circular photon orbits at roughly 1.5 times the Schwarzschild radius), not to the horizon itself. They probe the exterior spacetime geometry, not the surface of no return. The Event Horizon Telescope gives us a shadow; X-ray reflection spectroscopy gives us disk truncation radii; LIGO ringdown gives us light-ring frequencies. None of these are direct reads on the horizon's intrinsic properties — its rotation frequency $\Omega_H$ and surface gravity $\kappa$.

The theoretical groundwork for a more direct probe was laid in pieces: Mino & Brink (2008) and Zimmerman & Chen (2011) showed that plunging objects drive radiation that asymptotes to a "horizon mode" near frequency $2\Omega_H$. Oshita, Ma, Chen & Yang (arXiv:2509.09165, September 2025 — one month before this paper) synthesized and extended this into a full prediction: during the brief merger window, as the companion falls through the ergosphere and crosses the horizon, a "direct wave" is emitted whose oscillation frequency clusters near $2\Omega_H$ and whose decay rate is controlled by $\kappa$, modified by additional screening from the gravitational potential barrier. This direct wave coexists with and overlaps QNMs near the strain peak. Oshita et al. also estimated SNRs for current detectors and found values around 10 — tantalizingly detectable.

GW250114, announced in 2025, changed what's possible. With a total SNR of ~80, it's dramatically louder than GW150914 (SNR ~24) — the previous benchmark event. This loudness isn't just a quantity bonus; it crosses a qualitative threshold for picking out sub-signals that would be swamped by noise in quieter events. The remnant spin $\chi_f = 0.68$ also matters: Oshita et al. showed that high-spin ergospheres effectively "freeze" the direct wave's instantaneous frequency near $2\Omega_H$, making it look more like a stable sinusoid and thus more tractable to match-filtering. This paper applies that theory to GW250114 and reports a detection with matched-filter SNR ~14 in each LIGO detector.

**Prior Belief Check:** This result aligns with — but significantly advances — what theorists expected. The existence of direct waves was predicted and their detectability was anticipated specifically for GW250114 by Oshita et al. In that sense, the result is not surprising to specialists who had read the theory paper. What is genuinely striking, even to experts, is the *clarity* of the signal: SNR ~14 for a sub-dominant waveform component whose theory was published just weeks earlier is remarkable. The result does not overturn any consensus; it adds a new observational layer consistent with GR and the Kerr metric.

**Replication & Convergence Note:** At time of arXiv submission this was single-group. However, an independent group (arXiv:2606.06592, using a completely different approach — full inspiral-merger-ringdown waveform subtraction rather than rational filters) has since confirmed direct-wave signatures in GW250114. This convergence substantially increases confidence. The two methods use different systematics and different data-processing pipelines, making correlated failures unlikely.

---

## Section 3 — Necessary Background Crash-Course

**The Kerr black hole's two fundamental surface properties.** A rotating (Kerr) black hole is characterized near its horizon by two quantities that appear together in the first law of black hole thermodynamics — the mechanical law analogous to the first law of ordinary thermodynamics ($dE = TdS - PdV$). The horizon rotation frequency $\Omega_H$ (units: rad/s, or inverse mass in geometrized units) is the angular velocity at which the horizon itself "rotates" — which, by the no-hair theorem, is entirely determined by the black hole's mass M and dimensionless spin $\chi$. The surface gravity $\kappa$ (units: inverse time/length) measures how sharply the gravitational pull intensifies as you approach the horizon from outside; it is the Kerr analog of gravitational acceleration at a surface, and it sets the Hawking temperature. Both appear in:

$$dM = \frac{\kappa}{8\pi} dA + \Omega_H \, dJ$$

Symbol definitions: $M$ : black hole mass; $\kappa$ : surface gravity (intensive, like temperature); $A$ : horizon area (extensive, like entropy); $\Omega_H$ : horizon rotation frequency (intensive, like pressure); $J$ : angular momentum (extensive, like volume).

What this actually means: this is the black hole's "thermodynamic equation of state" — add a bit of angular momentum $dJ$ and some area $dA$, and the mass changes by the sum of the conjugate intensive quantities times their extensive differentials. Exactly like $dE = TdS + \mu dN$ in statistical mechanics. $\kappa$ and $\Omega_H$ are the intensive variables that the direct wave actually measures.

*Breaks when:* you push the thermodynamic analogy to ask about *actual* thermal equilibrium — a classical Kerr black hole doesn't radiate (Hawking radiation is quantum-mechanical and negligibly small for astrophysical black holes), so the "temperature" $T_H = \kappa / 2\pi$ is a formal quantity, not a measurable heat bath in any practical observation.

**Frame dragging and the ergosphere.** Inside the ergosphere — a flattened region outside the event horizon, extending from the horizon to roughly twice the horizon radius at the equator — spacetime itself rotates so fast that *nothing* can remain stationary relative to distant observers. Any object in the ergosphere is forced to co-rotate with the black hole. The angular velocity of the ergosphere enforces a minimum angular velocity on everything inside it, and this minimum asymptotes to exactly $\Omega_H$ at the horizon itself. Think of it like a river current: once you're inside the ergosphere you can't paddle upstream — you're being dragged along at the river's speed whether you like it or not. For a particle plunging toward the horizon, this means its orbital angular velocity gets locked to $\Omega_H$ as it approaches, completely forgetting its prior inspiral history.

*Breaks when:* you think of the ergosphere as a hard boundary. Objects in the ergosphere can still escape (unlike inside the event horizon) — the Penrose process extracts energy by splitting objects inside the ergosphere, with one piece falling in and the other escaping faster than it arrived. The "river" analogy fails if you think the ergosphere traps things the way the horizon does.

**Quasinormal modes and why they're not the horizon.** When you pluck a guitar string, it rings at its natural resonant frequencies. The ringing-down black hole does the same thing: linear perturbations of the exterior Kerr spacetime have characteristic complex frequencies — the quasinormal modes — with a real part (oscillation frequency) and imaginary part (decay rate). These QNM frequencies depend only on mass and spin, making them tools for precision spectroscopy of the remnant. But crucially, QNMs are eigenmodes of the *potential barrier near the light ring*, not of the horizon. They're analogous to the acoustic resonances of a room (shaped by the walls = light ring) rather than to any property of the speaker at the center. Cardoso et al. (2016) showed explicitly that exotic compact objects with no horizon at all can mimic QNM spectra — you can have all the right room-acoustic resonances without any specific physics at the source.

*Breaks when:* you conclude that QNMs carry *no* horizon information. The QNM frequencies depend on mass and spin, which are defined for the whole spacetime including the horizon. The point is more subtle: QNMs are not *selectively* sensitive to horizon structure in the way that the direct wave is.

**The direct wave as "the final signal before silence."** As the companion spirals into the remnant, it emits radiation throughout its trajectory. Once it enters the ergosphere, this radiation oscillates near $2\Omega_H$ (the factor of 2 is from the quadrupole nature of gravitational radiation — the dominant $\ell=m=2$ mode emits at twice the orbital frequency). The companion's emitted radiation also gets exponentially suppressed as it approaches the horizon — gravitational redshift kills off the signal at a rate set by $\kappa$. On top of this, the potential barrier surrounding the light ring partially reflects outgoing waves, adding additional time-varying modulation. What survives to reach LIGO is the "direct wave": radiation that made it through the potential barrier, carrying the combined imprint of $\Omega_H$, $\kappa$, and barrier screening. Think of it like trying to hear someone speak while they fall into a well that is surrounded by an echo chamber: the fundamental pitch of their voice (fixed by $\Omega_H$) bleeds through, but it's muffled (suppressed by $\kappa$) and reverberant (modulated by barrier screening). The moment they hit bottom, all sound stops.

*Breaks when:* you treat the direct wave as a clean, isolated signal. In the data, it overlaps temporally with the QNMs and with nonlinear effects. Isolating it requires surgically removing the QNMs first — which is exactly what the rational filter accomplishes.

**Rational filters.** A rational filter is a signal-processing operation that targets and cancels specific complex-frequency components. If you know a QNM has complex frequency $\omega' = \omega_{re} - i/\tau$, you can construct a filter that multiplies the data by a rational function of $e^{i\omega' t}$ designed to zero out that exact exponentially oscillating component while leaving everything else relatively intact. Analogy: if noise-canceling headphones know exactly the frequency and phase of the engine hum, they can cancel precisely that frequency while leaving your music. Here, the "music" is the direct wave and the "engine hum" is the dominant QNMs ($\ell=m=2$ with overtones $n=0,1,2$ plus the $\ell=3, m=2, n=0$ mode).

*Breaks when:* the QNM you're canceling is not perfectly characterized or there are nonlinear QNMs you didn't model. A slightly wrong cancellation frequency leaves a residual that could masquerade as a signal — this is one of the key systematic concerns in the analysis.

**Central analogy for this paper:** Stripping the bell's ring to hear the final cry of the clapper.

---

## Section 4 — Core Technical Explanation

### The physical setup and why GW250114 is special

The authors model the binary merger using the Effective One-Body (EOB) framework — a well-established mapping of the two-body problem onto a test particle orbiting a deformed Kerr black hole. This isn't a new assumption; EOB underlies essentially all LIGO waveform models. The companion's trajectory spirals inward, crosses the potential barrier near the light ring (radius ~3M), enters the ergosphere, and asymptotically approaches the horizon. At each phase, it drives radiation.

GW250114 is special for two reasons: (1) its SNR ~80 is by far the highest ever, giving enough signal budget to look for a sub-dominant component; (2) the remnant spin $\chi_f = 0.68$ is high enough that the ergosphere locks the direct wave's instantaneous frequency to a nearly constant value near $2\Omega_H$, making it effectively behave like a damped sinusoid — far easier to detect than the more frequency-modulated direct waves expected from lower-spin remnants.

### The waveform model for the direct wave

The theoretical model for the direct-wave waveform (from Oshita et al. 2025) takes the form:

$$h_{\rm DW}(t) \sim [\omega_G(t) - \omega_H] \, e^{-i \int \omega_G(t) \, dt}$$

Symbol definitions: $h_{\rm DW}$ : direct-wave strain (the gravitational-wave signal from the direct wave); $\omega_G(t)$ : effective instantaneous complex frequency of the emitted wave, which varies with time as the companion falls and barrier screening evolves; $\omega_H = 2\Omega_H - i\kappa$ : the "horizon mode" — the complex frequency the direct wave asymptotes toward as $t \to \infty$ (i.e., as the companion reaches the horizon); the prefactor $[\omega_G(t) - \omega_H]$ causes the amplitude to vanish as the companion's frequency merges with the horizon mode.

What this actually means: the prefactor is what makes the direct wave "turn off" at the horizon — as the companion's motion synchronizes with the horizon's own rotation, there's nothing more to drive relative to the horizon's natural frequency, and the emission fades to zero. This is analogous to a loudspeaker whose output goes to zero as the speaker cone's vibration frequency locks exactly to the cabinet's resonant frequency — when driver and resonator are perfectly matched, net radiation goes to zero.

For the actual LIGO analysis, the authors use a simplified two-parameter version: a pure damped sinusoid with a constant frequency $f_{\rm DW}$ and damping time $\tau_{\rm DW}$. This is model-agnostic — it doesn't assume the exact theoretical template, just that the signal looks approximately sinusoidal over a short window. Then separately, they also run a matched-filter analysis using the full Oshita et al. template, with two free parameters (amplitude and time shift).

### The analysis pipeline: three steps

**Step 1 — QNM removal.** They apply rational filters tuned to cancel the dominant QNMs: the $(\ell=2, m=2, n=0,1,2)$ modes and the $(\ell=3, m=2, n=0)$ mode. The QNM frequencies used come from the independently determined remnant mass and spin from the full inspiral-merger-ringdown parameter estimation. The output is a "QNM-removed" strain — what's left after the dominant ringing has been subtracted.

**Step 2 — Model-agnostic detection.** In the QNM-removed data, they fit a damped sinusoid over sliding 0.2 s windows starting at $t_{\rm start} \in [-9, -3] M_f^{\rm det}$ (where $M_f^{\rm det} = 68.1 M_\odot$ detector-frame is roughly 1 ms, so the window spans roughly ±10 ms around the peak). The key result: the inferred frequency and damping rate *evolve* as $t_{\rm start}$ shifts later, and they cluster toward $\omega_H$ — they don't match any of the known QNM frequencies. A detection statistic $\mathcal{D} \approx 530$ at $t_{\rm start} = -7 M_f^{\rm det}$ corresponds to a false-alarm probability below 0.1% (the threshold for 0.1% FAP is $\mathcal{D}_{0.1\%} = 8.78$).

**Step 3 — Matched-filter confirmation.** Using the full Oshita et al. theoretical template $h_{\rm DW}(t)$, they perform a Bayesian matched-filter analysis over the 0.2 s segment starting at $-7 M_f^{\rm det}$. Result: matched-filter SNR of $14.0^{+0.2}_{-0.1}$ (Hanford) and $13.5^{+0.1}_{-0.2}$ (Livingston) — stated in the paper as "90% credible" in the Nature version. These numbers are consistent with the theoretical predictions for GW250114's parameters made by Oshita et al. before the analysis was done.

### What "consistent with Kerr" means

The measured direct-wave frequency clusters near $2\Omega_H$ computed from the independently measured remnant spin, and the measured damping rate approaches $\kappa$ computed from the same spin. The paper cannot measure $\Omega_H$ and $\kappa$ *independently* from the direct wave alone with high precision (the signal is too short and the waveform template too simple), but the consistency check is meaningful: the direct-wave parameters don't contradict the Kerr prediction, and they don't match the QNM predictions either.

### Assumption Audit

**Watch: The reader likely assumes the QNM subtraction is clean.** The paper actually acknowledges that the rational filter cancels QNMs at fixed frequencies determined from the remnant's independently measured mass and spin — but if those QNM frequencies are slightly wrong (due to parameter estimation uncertainty, or due to nonlinear QNM shifts, or due to QNM overtones not included in the filter), the residuals from incomplete subtraction could mimic or corrupt the direct-wave signal. The analysis tests robustness against window length variation but does not perform a full sensitivity analysis over the space of slightly-wrong QNM filters.

**Watch: The reader likely assumes the "direct wave" and "nonlinear QNMs" are distinguishable.** The paper actually notes that quadratic QNMs — nonlinear mode-mode coupling products that appear at frequencies $\omega_{\ell m n} + \omega_{\ell' m' n'}$ — also coexist with the direct wave near merger time. The paper argues that the direct wave dominates in the $t \gtrsim -7 M_f^{\rm det}$ window, but this claim rests on comparison with the NRSur7dq4 waveform, which itself models nonlinear effects only approximately. There is no independent proof that the detected signal contains zero contribution from nonlinear QNMs.

**Watch: The reader likely assumes the damped-sinusoid model is an adequate stand-in for the full theoretical template.** The paper actually shows that the direct-wave instantaneous frequency evolves with time — Figure 3 and the structure of $h_{\rm DW}(t)$ both make this clear. A single-frequency damped sinusoid is explicitly called "a practical first step, though ultimately insufficient for high-precision analyses." The reported SNRs and parameter constraints should be understood as conservative first measurements with simplified templates, not precision horizon characterization.

---

## Section 5 — What's Genuinely New or Clever

**New to the field, not just the reader:**

**1. The first horizon-targeted signal extraction from gravitational-wave data.** Previous GW observations have probed black holes through QNMs (light-ring physics), mass/spin inference, and Hawking area-law tests. The direct wave is something different: it is generated by near-horizon dynamics in the ergosphere, and encodes $\Omega_H$ and $\kappa$ specifically — the two intensive thermodynamic variables of the horizon's first law. This is not merely a refinement of existing spectroscopy; it's a new observational channel targeting a different region of the black hole spacetime. The Event Horizon Telescope images the shadow at tens-of-thousands of Schwarzschild radii for supermassive black holes; this measurement probes the near-horizon ergosphere during a dynamical event.

**2. The rational-filter strategy as a surgical extraction tool.** The ingenious move here is not the direct-wave detection itself but *how* the direct wave is isolated: by designing a filter whose transfer function is a rational function of the Laplace variable tuned to perfectly zero out the exponentially oscillating QNM components, you can subtract the QNM contribution from the data without subtracting the broad-band noise floor (which a simple frequency-domain notch would do), and without touching the direct wave that lives at a different, evolving complex frequency. The result is that you're looking at data already cleaned of its loudest contaminator, and the direct wave appears as the dominant remaining signal in a specific time window. This is a non-trivial application of the Ma, Sun & Chen (2022, 2023) rational-filter formalism specifically adapted to the problem of near-horizon physics extraction.

---

## Section 6 — Limitations & Open Questions

**The waveform template is rudimentary.** The matched-filter analysis uses the Oshita et al. linearized perturbation-theory template derived for a point particle plunging into a Kerr black hole — a framework that ignores mass ratio effects, precession, eccentricity, and nonlinear perturbations. GW250114 is a nearly equal-mass merger (33.6 vs. 32.2 solar masses), so the point-particle approximation is qualitatively motivated by EOB intuition but quantitatively uncertain. The paper explicitly calls this "ultimately insufficient for high-precision analyses." (A) Consensus — explicitly stated in the Conclusion as the first priority for future work. (paper §Conclusion)

**QNM subtraction systematics are the least-auditable uncertainty.** The rational filter cancels QNMs at frequencies determined from independent parameter estimation. If those frequencies are biased (by nonlinear QNM frequency shifts, by calibration errors, or by misidentification of which overtones are significant), the "cleaned" data contains residuals from the QNMs, not just the direct wave. The paper shows robustness to window-length variation but not to QNM frequency perturbation. This is the most subtle and least characterized systematic in the analysis — a small error in QNM removal could either create a spurious direct-wave detection or suppress a real one. (B) Contested — the paper's own team has previously developed the rational filter and has demonstrated its reliability in simulations, so they're better positioned than most to assess this risk; but independent groups may have different assessments of the residual systematic. (paper §Methods B + broader literature)

**The direct wave and nonlinear QNMs may not be separable at this SNR.** Quadratic quasinormal modes — the gravitational-wave nonlinear equivalent of second harmonics, excited when linear QNMs beat against each other — appear at combination frequencies that can overlap with the direct-wave frequency range near merger. The paper argues the direct wave dominates at $t \gtrsim -7 M_f^{\rm det}$ based on NRSur7dq4 comparison, but the numerical relativity surrogate model itself doesn't perfectly resolve nonlinear effects during the merger peak. The extent to which the detected ~SNR 14 signal contains nonlinear QNM contributions has not been rigorously bounded. (C) Speculative — this concern is raised in the literature on nonlinear ringdowns but is not directly quantified in this paper; I am extrapolating from the Mitman et al. / Cheung et al. 2023 nonlinear QNM results to ask whether they contaminate the merger window specifically. (analyst inference)

**The $t_{\rm start}$ ambiguity.** The direct wave "turns on" over a transition window, not at a sharp moment. The paper reports results for $t_{\rm start} \in [-7, -3] M_f^{\rm det}$ as the clean regime, but also includes earlier times $[-9, -7] M_f^{\rm det}$ with a caution that those may include inspiral-regime signals not matching the direct-wave interpretation. Any analysis that inadvertently includes inspiral contamination could either inflate or deflate the measured parameters. The sensitivity to precisely where the analysis window starts is flagged but not fully marginalized over. (A) Consensus — the paper itself acknowledges this ambiguity explicitly, and it is standard in merger-phase analyses. (paper §Measurement section footnote 1)

**Single-event detection; no systematic survey.** This detection is enabled by GW250114's exceptional SNR. The paper explicitly calls for a systematic search across all GWTC events. For the field to confirm the direct wave as a robust observational phenomenon rather than a lucky high-SNR artifact, it needs to appear (at lower significance) in multiple events with consistent parameters. (A) Consensus — the need for a population-level search is stated in the Conclusion. (paper §Conclusion)

---

## Section 7 — Detailed Summary & Explanation

Black holes have two surfaces: the event horizon and, for rotating black holes, the ergosphere boundary just outside it. For decades, gravitational wave astronomy has probed the post-merger black hole through quasinormal modes — the ringdown frequencies tied to the potential barrier near the light ring, not to the horizon itself. This paper takes a different approach: it looks for "direct waves," a component of the merger-phase gravitational wave signal that encodes the horizon's own fundamental properties — its rotation rate $\Omega_H$ and surface gravity $\kappa$ — because these waves are generated by the companion's orbital motion as it plunges through the ergosphere and approaches the horizon.

The physical picture, developed by Oshita et al. in September 2025, goes like this. During the final plunge of a binary merger, the infalling companion is dragged into corotation with the horizon by frame dragging — its orbital angular velocity locks to $\Omega_H$. The gravitational radiation it drives during this phase therefore oscillates near $2\Omega_H$ (twice the horizon frequency, because gravitational waves are quadrupolar). Simultaneously, the radiation is exponentially suppressed by gravitational redshift at a rate set by $\kappa$, and further modified as it propagates out through the gravitational potential barrier surrounding the remnant. This modified radiation is the "direct wave." It appears around and just after the strain peak, coexisting temporally with the quasinormal modes, and it fades to zero as the companion falls through the horizon and is silenced.

GW250114 is the ideal event to look for this: it's the loudest binary black hole merger ever detected (SNR ~80), and its remnant spin of $\chi_f = 0.68$ is high enough that the ergosphere's strong frame dragging keeps the direct-wave frequency quasi-stable near $2\Omega_H$, making it behave approximately like a steady damped sinusoid rather than a rapidly chirping signal.

The analysis proceeds in three stages. First, the authors apply "rational filters" — a signal processing technique that surgically cancels the dominant quasinormal modes from the data by zeroing out their exact complex frequencies in the transfer function. This is like removing the bell's ringing from a recording to hear what else was happening when it was struck. After QNM removal, a distinct oscillatory signal remains in the merger window starting around 7 remnant-mass time units before the peak. This residual aligns well with the theoretical NRSur7dq4 numerical-relativity surrogate waveform after its own QNM content is stripped — a strong cross-check that the analysis isn't simply finding a numerical artifact.

Second, they fit a simple damped sinusoid to the QNM-removed data in sliding windows. The inferred frequency and damping rate evolve over time and cluster toward the theoretically predicted horizon mode $\omega_H = 2\Omega_H - i\kappa$ as the analysis window moves later — exactly the behavior predicted for the direct wave. They don't match any of the known quasinormal modes, whose predicted parameter-space locations are clearly separated. The detection statistic ($\mathcal{D} \approx 530$, threshold for 0.1% false alarm: $8.78$) makes noise the essentially implausible explanation for the feature.

Third, using the full Oshita et al. theoretical template in a Bayesian matched-filter framework, they extract matched-filter SNRs of 14.0 (Hanford) and 13.5 (Livingston). Both are consistent with what Oshita et al. predicted for GW250114's parameters before the analysis — no post-hoc tuning. The Nature version of the paper adds that the measured properties are fully consistent with a Kerr black hole.

The result is interpreted as providing the first direct measurement of the horizon's thermodynamic intensive variables $\Omega_H$ and $\kappa$ from a gravitational-wave event — not mediated by the light-ring potential, but via the near-horizon dynamics of the ergosphere itself.

**Why the summary is framed this way:** I've led with the distinction between light-ring probes (QNMs) and horizon probes (direct waves) because that's the interpretive crux. Without it, the result looks like "yet another ringdown measurement" — which badly undersells it. The direct wave as "horizon first law" measurement is what makes this categorically new. The framing of GW250114's SNR as a "qualitative threshold" (not just a quantitative benefit) is deliberate: below some SNR, you can't distinguish direct wave from noise, no matter how clever the analysis.

**Genuine Uncertainty Disclosure:** Where I'm least confident in this analysis is the claim that the model-agnostic sinusoid fit and the matched-filter result together constitute a clean detection of the *direct wave specifically*, as opposed to some combination of direct wave, nonlinear QNMs, and inspiral-merger transition radiation — the paper makes a compelling case that the direct wave dominates in the chosen time window, but this rests on NRSur7dq4 waveform comparison, and the numerical relativity surrogate's treatment of nonlinear effects at the merger peak is not perfect; I cannot fully evaluate from the paper's content how much of the SNR 14 signal might be attributable to effects not cleanly described by the Oshita et al. perturbative template.

---

## Section 8 — Three Crystallized Takeaways

**1.** We've heard the final cry of a black hole companion as it crossed the horizon: GW250114's merger data contains a gravitational wave component oscillating near twice the horizon's own rotation frequency and fading at a rate set by the horizon's surface gravity — the first time either of these fundamental horizon properties has been directly read from a gravitational-wave signal.

**2.** Quasinormal modes and direct waves are probing physically different geography of the black hole: QNMs ring from the light ring (1.5 Schwarzschild radii out); direct waves are generated in the ergosphere, centimeters (in the sense of proper proximity) from the actual surface of no return — this is a categorically new observational channel, not just a better measurement of the same channel.

**3.** The enabling technology is as important as the result: the rational-filter framework that surgically removes QNMs from the data while leaving everything else intact is the methodological breakthrough that made this detection possible, and it will likely power searches for direct waves across the full LIGO event catalog as well as future precision horizon measurements with next-generation detectors.

---

## Section 9 — Shorter Summary

When two black holes merge, the final phase before the companion disappears forever behind the event horizon produces a brief gravitational wave signal called the "direct wave." Unlike the well-studied quasinormal-mode ringdown — which probes the exterior potential barrier near the light ring — the direct wave is generated inside the ergosphere, where frame dragging forces the infalling companion into corotation with the horizon. This locks the wave's oscillation frequency near twice the horizon's own rotation rate and causes the wave to fade exponentially at a rate set by the horizon's surface gravity. Both quantities — the rotation frequency and the surface gravity — are the fundamental thermodynamic variables of the black hole's first law, and they had never been directly measured from a gravitational wave before.

GW250114, the loudest binary black hole merger ever detected, provided the SNR headroom (~80 total) to look for this sub-dominant signal. The analysis strips out the dominant quasinormal modes using "rational filters" — a signal-processing technique that precisely cancels specific complex-frequency components without disturbing the rest of the data. What remains in the merger window is a clear oscillatory signal that clusters toward the theoretical horizon mode frequency as time progresses — not matching any quasinormal mode, but consistent with direct-wave predictions. A Bayesian matched-filter analysis using the theoretical direct-wave template gives SNRs of 14.0 and 13.5 in the two LIGO detectors, matching predictions made weeks earlier by the theoretical paper that predicted this signal.

The result establishes a new observational channel for black hole physics, complementing quasinormal-mode spectroscopy with the first measurements of the horizon's own characteristic properties. Independent confirmation from a different analysis group and a different methodology, published shortly after, substantially strengthens confidence in the result. Near-term priorities include developing precision waveform templates for the direct wave (the current analysis uses a simplified point-particle model), conducting a systematic survey of the full LIGO event catalog, and understanding how direct waves must be accounted for in conventional QNM spectroscopy where they may currently be treated as contamination.

## Human

explain The direct wave as "the final signal before silence."

## Assistant

Explaining

Let me build this up from scratch — geometry first, then dynamics, then the actual signal.

---

## The Setup: Two Regions, Two Physics Regimes

A rotating Kerr black hole has a layered structure outside the singularity. Working outward from the center, the first important surface is the **event horizon** — the true point of no return, radius:

$$r_+ = M\left(1 + \sqrt{1 - \chi^2}\right)$$

Symbol definitions: $r_+$ : outer horizon radius (in geometrized units where $G=c=1$); $M$ : black hole mass; $\chi$ : dimensionless spin parameter, $0 \leq \chi < 1$.

What this means: for a maximally spinning black hole ($\chi \to 1$), the horizon shrinks toward $r_+ = M$. For a non-spinning Schwarzschild black hole ($\chi = 0$), it sits at $r_+ = 2M$, the Schwarzschild radius.

Just outside the horizon lies the **ergosphere**, bounded by:

$$r_{\rm ergo} = M\left(1 + \sqrt{1 - \chi^2 \cos^2\theta}\right)$$

Symbol definitions: $\theta$ : polar angle from the spin axis; at the equator ($\theta = \pi/2$), the ergosphere extends farthest out to $r_{\rm ergo} = 2M$ regardless of spin.

The ergosphere isn't a surface of no return — things can escape from it. But it has a property that nothing inside the horizon has: **frame dragging so strong that all objects, including light, are forced to co-rotate with the black hole.** Stationary means rotating.

The **light ring** sits farther out still, at roughly $r \approx 3M$ for a Schwarzschild black hole (modified by spin for Kerr). This is where photons can orbit in unstable circular paths. The quasinormal modes — the GR analog of a ringing bell — are eigenmodes of the potential barrier that lives *near* the light ring. They are exterior geometry. The ergosphere and horizon are interior to the light ring.

So three distinct regions:
- Light ring (~3M): where QNMs live
- Ergosphere (from $r_+$ to $r_{\rm ergo}$): where frame dragging dominates
- Horizon ($r_+$): the surface itself

The direct wave is not a light-ring phenomenon. It comes from inside the ergosphere.

---

## Phase 1: The Inspiral (Everything Is Normal)

During the long inspiral, the two black holes orbit each other far from their individual horizons. The gravitational radiation they emit is well-described by post-Newtonian theory — the orbital frequency increases slowly as the system loses energy, producing the characteristic chirp. Crucially, the radiation carries the imprint of the *orbital dynamics*, not of either individual horizon. The signal depends on masses and orbital parameters, not on $\Omega_H$ or $\kappa$ of either component.

The companion can be thought of as carrying its own "clock frequency" — its instantaneous orbital angular velocity $\Omega_{\rm orb}(t)$, which increases slowly inward. The radiation emerges at twice this frequency (quadrupolar emission). That clock is set by Kepler's law modified for GR: it's an *orbital* clock, set by the mutual gravitational dynamics.

---

## Phase 2: The Ergosphere — Where the Clock Gets Hijacked

As the companion crosses the light ring and enters the ergosphere, something qualitative changes. Frame dragging is no longer a small perturbation on Newtonian dynamics — it *dominates*. The spacetime geometry itself is rotating, and it forces the companion's motion.

Here is the precise statement. Inside the ergosphere, the minimum allowed angular velocity for any object (including a photon) is nonzero. That minimum increases as you move inward. At the event horizon, it exactly equals the horizon's rotation frequency $\Omega_H$:

$$\Omega_H = \frac{\chi}{2r_+}$$

Physically: as the companion falls through the ergosphere, its orbital angular velocity $\Omega_{\rm orb}(t)$ — which was set by inspiral history — gets forcibly driven toward $\Omega_H$. The ergosphere's frame dragging acts like a very strong current that locks onto the companion and refuses to let it rotate at any other rate. The companion's "memory" of its prior orbital history is being erased and replaced with the horizon's own imprint.

This is not a gradual correction. By the time the companion is deep in the ergosphere and approaching the horizon, $\Omega_{\rm orb}(t)$ has essentially converged to $\Omega_H$. This convergence is the physical origin of the direct wave's oscillation frequency.

Because the dominant gravitational wave emission is quadrupolar, a source rotating at $\Omega_H$ drives radiation at $2\Omega_H$. So the direct wave oscillates near that frequency — not because someone tuned a filter to $2\Omega_H$, but because the ergosphere *physically forces the source to orbit at $\Omega_H$*.

---

## Phase 3: The Horizon — Where the Signal Dies

While the frequency is being pinned by the ergosphere, the amplitude is being killed by the horizon. Two mechanisms:

**Gravitational redshift.** Any photon or gravitational wave climbing out of a strong gravitational field loses energy to that field. Near the horizon, this redshift becomes catastrophic — the gravitational time dilation diverges. A wave packet emitted at radius $r$ just outside $r_+$ takes infinite coordinate time to reach infinity, and arrives exponentially dimmed by a factor:

$$e^{-\kappa \, \Delta t}$$

Symbol definitions: $\kappa$ : surface gravity — the rate at which the redshift factor grows as you approach the horizon; $\Delta t$ : coordinate time elapsed.

What this means: the surface gravity $\kappa$ is exactly the decay constant of this exponential suppression. A larger $\kappa$ (a "hotter" horizon, in the thermodynamic analogy) means the signal dies faster. As the companion falls inward and emits, each successive wave crest is emitted from deeper in the potential, more severely redshifted, arriving more dimly. The envelope of the signal decays exponentially at rate $\kappa$.

**The final silence.** When the companion crosses the horizon, the emission stops entirely. Photons and gravitational waves emitted from exactly at $r_+$ never escape — they sit at the horizon forever in coordinate time. There is a hard cutoff: the companion radiates continuously up to the moment of crossing, and then nothing. The gravitational-wave signal has a natural termination.

So the combined result of these two effects: the companion's orbital frequency converges to $\Omega_H$ (setting the oscillation frequency of the direct wave at $2\Omega_H$), while the gravitational redshift exponentially attenuates its amplitude at rate $\kappa$ (setting the decay envelope). The signal oscillates at $2\Omega_H$ and dies on a timescale $1/\kappa$.

---

## Phase 4: Barrier Screening — The Last Complication

The direct wave doesn't travel from the ergosphere to LIGO in free space. It has to propagate through the potential barrier near the light ring. This barrier — the same one responsible for the QNMs — partially reflects outgoing waves back toward the black hole and partially transmits them. The transmission is frequency-dependent and time-dependent (because the source is moving).

The effect on the direct wave is that its instantaneous frequency and damping rate get additional time-dependent corrections on top of the clean $\omega_H = 2\Omega_H - i\kappa$ value. The observed signal's frequency doesn't sit exactly at $2\Omega_H$ — it approaches it from above or below depending on the barrier geometry — and the decay rate doesn't equal $\kappa$ exactly but is modified by the barrier's additional absorption. This is why the paper reports that the direct-wave frequency "clusters near but not exactly at $\omega_H$" as the analysis window moves later.

The theoretical waveform captures this:

$$h_{\rm DW}(t) \sim \left[\omega_G(t) - \omega_H\right] e^{-i \int \omega_G(t) \, dt}$$

The prefactor $[\omega_G(t) - \omega_H]$ deserves close attention. This term goes to zero as $\omega_G(t) \to \omega_H$ — which happens as the companion approaches the horizon and its frequency converges to the horizon mode. So the amplitude is *maximum when the companion's frequency is farthest from $\omega_H$* (early in the ergosphere crossing) and goes to zero as the companion asymptotically converges to the horizon frequency (just before crossing). The signal is loudest during the transition and silent at the end — structurally, it's a burst of radiation that announces the companion's ergosphere entry and fades to silence as the companion merges with the horizon.

---

## Why "Final Signal Before Silence" is Exact, Not Metaphorical

Putting the full picture together:

The QNMs are *freely oscillating* modes of the remnant — they ring on after the merger, driven by the initial perturbation of the potential barrier, decaying only because the outgoing radiation carries energy away. They have nothing to do with the companion anymore once it's crossed the horizon. The ringdown QNMs are the bell ringing after you've struck it; the striker (the companion) is gone.

The direct wave is the *source-driven* emission of the companion itself during its final approach. It is the radiation you get because there is still a moving mass in the ergosphere radiating. When that mass crosses the horizon: no more moving mass, no more direct wave, silence. The QNMs continue; the direct wave stops.

This is why the direct wave lives in the merger window — the brief period *around and just after the strain peak* — while the QNMs dominate later. The strain peak marks, roughly, the moment when the companion's merger with the remnant is most violent. The direct wave is present *up to that point*; the QNMs take over *after*.

The term "final signal" is exact in a specific sense: the direct wave is the last emission that carries information about what the companion was *doing* just before it ceased to exist as a separate object. Everything after that is the remnant ringing on its own.

## Human

explain The direct wave as "the final signal before silence."

## Assistant

Explaining

You asked the same question twice — I just gave a full first-principles answer. Did you want me to go deeper on a specific part of that explanation, or was the duplicate message accidental?

## Human

ok, here's a new question. explain Rational filters.

## Assistant

Explaining

Let me build this from scratch — signal processing foundations first, then the specific QNM problem, then how rational filters solve it cleanly.

---

## The Problem Being Solved

After a binary black hole merger, the gravitational-wave data contains several overlapping components: the QNMs (dominant), the direct wave (sub-dominant, present around the strain peak), late-time tails, noise, and potentially nonlinear QNM contributions. To find the direct wave, you need to remove the QNMs without disturbing everything else.

The naive approaches all fail in instructive ways, and understanding *why* they fail is the best route to understanding what rational filters actually do.

---

## Why Naive Subtraction Fails

**Approach 1: Fit and subtract a damped sinusoid model for the QNMs.**

Fit the post-merger data to a sum of damped sinusoids $A e^{-t/\tau} \cos(2\pi f t + \phi)$, one per QNM, then subtract. The problem: this requires knowing the QNM amplitude and phase with high precision. These aren't predicted by theory — they depend on the details of the merger dynamics and require fitting from data. If your fit is slightly wrong (and it will be, because you're fitting noisy data), the residual from the subtraction contains a correlated, structured artifact that looks signal-like. You've traded one problem (QNMs obscuring the direct wave) for a worse problem (a subtraction artifact that mimics a signal).

**Approach 2: Bandpass filter around the direct-wave frequency.**

The direct wave is expected near $2\Omega_H$ — just bandpass filter out everything else. But the QNM frequencies are *close* to $2\Omega_H$, not far from it. The $(\ell=2, m=2, n=0)$ fundamental QNM and the direct-wave frequency differ by a small amount that a bandpass filter can't resolve cleanly, especially over the short time window (a few hundred milliseconds) involved. You'd cut out the direct wave along with the QNMs.

**Approach 3: Notch filter at the QNM frequencies.**

A notch filter zeros out a narrow frequency band in the Fourier domain. The problem here is that QNMs are *not* simple frequency components — they are exponentially decaying oscillations. In the Fourier domain, a damped sinusoid $e^{-t/\tau}\cos(2\pi f t)$ doesn't live at a single frequency $f$. It has a Lorentzian spectral shape with width $1/\pi\tau$. A notch at frequency $f$ removes only the zero-damping component; it leaves behind all the power in the Lorentzian tails. You'd need to zero out an entire frequency band, which destroys broadband structure — including the direct wave.

The root problem with all three approaches is the same: they treat QNMs as Fourier frequency components, but QNMs are actually poles in the complex frequency plane — they have *both* a real frequency and an imaginary damping rate. Any tool that only acts on the real frequency axis is the wrong tool.

---

## Complex Frequencies and the Laplace Domain

Here's the reframing that makes rational filters natural.

A single QNM in the time domain looks like:

$$h_{\rm QNM}(t) = A \, e^{i\omega_{\ell mn} t}, \quad t > t_0$$

Symbol definitions: $A$ : complex amplitude (encodes both magnitude and phase); $\omega_{\ell mn} = 2\pi f_{\ell mn} - i/\tau_{\ell mn}$ : complex QNM frequency; the real part $2\pi f_{\ell mn}$ gives oscillation frequency; the imaginary part $-1/\tau_{\ell mn}$ gives the exponential decay rate (negative imaginary part means decaying, not growing).

What this means: a QNM isn't a sinusoid — it's a *complex exponential with a complex exponent*. The real part of the exponent drives oscillation; the imaginary part drives decay. In the complex frequency plane (also called the s-plane or the Laplace domain), this QNM is a **pole** at $s = i\omega_{\ell mn}$. A Fourier transform only resolves the real-frequency axis — it can't see poles that are off the real axis.

The Laplace transform of the QNM signal is:

$$H(s) = \frac{A}{s - i\omega_{\ell mn}}$$

This has a pole at $s = i\omega_{\ell mn}$. The signal "blows up" at that complex frequency value. Everything about the QNM's behavior is encoded in this single pole location.

---

## What a Rational Filter Does

A rational filter is a linear filter whose transfer function $R(s)$ is a ratio of polynomials in $s$ (hence "rational"):

$$R(s) = \frac{N(s)}{D(s)} = \frac{(s - z_1)(s - z_2)\cdots}{(s - p_1)(s - p_2)\cdots}$$

Symbol definitions: $z_k$ : zeros of the transfer function — frequencies at which $R(s) = 0$, so the filter completely suppresses the input at those complex frequencies; $p_k$ : poles of the transfer function — frequencies at which $R(s) \to \infty$, which can be used to boost specific components.

When you pass a signal through a filter with transfer function $R(s)$, the output's Laplace transform is the input's Laplace transform multiplied by $R(s)$. If $R(s)$ has a **zero at exactly $s = i\omega_{\ell mn}$** — the pole location of the QNM — then the QNM component gets multiplied by zero. It's completely annihilated.

To cancel one QNM with complex frequency $\omega'$, construct:

$$R(s) = \frac{s - i\omega'}{s - i\omega_{\rm stable}}$$

Symbol definitions: $\omega'$ : complex frequency of the QNM to be canceled; $\omega_{\rm stable}$ : any stable complex frequency chosen to make the filter well-behaved (its imaginary part must be negative, ensuring the pole doesn't blow up).

The numerator places a zero exactly at the QNM's pole — canceling it perfectly. The denominator places a compensating pole somewhere stable — this is needed because a transfer function that goes to zero everywhere would kill the entire signal, and a rational function must have equal numbers of poles and zeros for physical realizability. The denominator pole is chosen far from any signal of interest.

To cancel multiple QNMs, multiply the filters:

$$R(s) = \prod_k \frac{s - i\omega_k'}{s - i\omega_{{\rm stable},k}}$$

Each factor kills one QNM. For the GW250114 analysis, the product cancels $(\ell=2, m=2, n=0,1,2)$ and $(\ell=3, m=2, n=0)$ — four QNMs total, one factor per QNM.

---

## What the Filter Leaves Untouched

This is the key property. The rational filter is a *targeted* operation: it places zeros at specific complex frequencies and leaves the transfer function essentially equal to 1 everywhere else in the complex plane. Any signal component whose complex frequency is not one of the zeros passes through with minimal distortion.

The direct wave's complex frequency evolves through a range of values near $\omega_H = 2\Omega_H - i\kappa$ — values that are distinct from the QNM poles. Because the rational filter's zeros are placed at the QNM poles, not near $\omega_H$, the direct wave passes through.

Broadband noise also passes through. This is actually fine — you want the noise to pass through, because your subsequent Bayesian analysis will model it and account for it. What you don't want is the structured, signal-like QNM contamination in your data — and the rational filter removes precisely that.

The analogy I find clearest: imagine a spectrograph analyzing starlight. A notch filter removes all light at a specific wavelength — it destroys information at that wavelength for everything, signal and contaminant alike. A rational filter is more like a holographic notch: it knows the exact spatial pattern of the contaminant (the QNM's complex-plane structure) and cancels only that pattern, leaving the rest of the light field undisturbed.

---

## Practical Implementation: From the s-Plane to the Time Domain

In practice, you don't implement filters in the continuous Laplace domain — you implement them on discretely sampled data. The continuous-time rational filter $R(s)$ gets discretized into a difference equation operating on successive samples of the strain data.

For a single zero at complex frequency $\omega'$, the time-domain operation is:

$$h_{\rm filtered}[t_j] = h[t_j] - e^{i\omega' \Delta t} \cdot h[t_{j-1}]$$

Symbol definitions: $h[t_j]$ : strain data at sample $j$; $\Delta t$ : sample spacing; $e^{i\omega' \Delta t}$ : the phase and amplitude advance of the QNM over one sample interval.

What this means: at each time step, you subtract from the current sample a prediction of what the QNM would contribute based on the previous sample, propagated forward by one step using the QNM's known complex frequency. If the data contains exactly a QNM at $\omega'$, this operation exactly cancels it — the prediction is perfect. If the data contains other components, those components aren't predicted correctly by $e^{i\omega' \Delta t}$, so they're not subtracted.

This is the discrete-time incarnation of placing a zero at $i\omega'$ in the z-plane (the discrete-time analog of the s-plane). The chain of QNM-canceling operations (one per QNM) is implemented as a cascade of these first-order difference equations, one per QNM.

---

## The Critical Assumption and Its Failure Mode

The rational filter works perfectly if the QNM frequency $\omega'$ is known exactly. In practice, $\omega'$ depends on the remnant mass and spin, which are measured with finite precision. If the QNM frequency used in the filter is slightly wrong — say, off by $\delta\omega$ — the filter places its zero at $i(\omega' + \delta\omega)$, not at $i\omega'$. The true QNM pole at $i\omega'$ is not exactly canceled. The residual passes through with amplitude proportional to $\delta\omega$ times the QNM amplitude.

For the dominant $(2,2,0)$ mode of GW250114 (SNR ~80 total), even a 1% error in $\omega'$ leaves a residual in the filtered data that could be larger than the direct wave itself. This is why the paper uses QNM frequencies derived from the best-available parameter estimation of the remnant — and why the systematic uncertainty in those QNM frequencies is the least-auditable uncertainty in the entire analysis.

There's also a subtler failure mode: nonlinear QNMs. The quadratic QNM at frequency $\omega_{211} + \omega_{220}$ (for example) has a complex frequency that the filter wasn't designed to cancel. If that mode's amplitude is significant in the merger window, its contribution passes through the rational filter and sits in the "QNM-removed" residual alongside the direct wave. The analysis relies on NRSur7dq4 comparisons to argue this contribution is subdominant in the chosen time window — but it's not analytically guaranteed.

---

## Connecting Back to the Detection

With the rational filter applied, the QNM-removed strain in the merger window contains the direct wave plus broadband noise plus any residuals from imperfect QNM cancellation. The subsequent Bayesian analysis fits a damped sinusoid to this residual — now the fit is modeling only the direct-wave structure, not trying to simultaneously model QNMs plus direct wave in a highly correlated parameter space. The rational filter has *decoupled* the detection problem: first cancel the dominant modes, then fit for the subdominant one.

The detection statistic $\mathcal{D} \approx 530$ versus a threshold of $8.78$ — four orders of magnitude above threshold — reflects how cleanly the direct wave appears in the filtered data. If the rational filter were leaving substantial QNM residuals, those residuals would be structured in a way that the damped-sinusoid fit would partially absorb, inflating $\mathcal{D}$ spuriously. The consistency between the model-agnostic sinusoid fit and the matched-filter result (both converging on the same parameters, which match the theoretical $\omega_H$) is the argument that the filter is working as intended and not polluting the result.

## Human

ok, here's a new question. explain Rational filters.

## Assistant

Explaining

Let me build this from the ground up — signal processing first, then the specific construction, then why it's the right tool for this problem.

---

## The Core Problem

After a binary black hole merger, the LIGO strain data in the ringdown window contains a superposition of signals:

- Dominant QNMs: large-amplitude, exponentially damped sinusoids at known complex frequencies
- Direct wave: smaller-amplitude, slowly evolving signal at a different complex frequency
- Noise: broadband detector noise

The direct wave's SNR is ~14 in GW250114. The dominant QNM ($\ell=m=2, n=0$) SNR is much larger — likely over 50. If you just look at the raw data, the QNMs completely bury the direct wave. You need to remove the QNMs first.

The naive approaches fail in instructive ways.

**Naive approach 1 — Subtract a fitted QNM model.** Fit a damped sinusoid to the ringdown, subtract it, look at the residual. Problem: the QNM parameters (amplitude, phase, start time) have to be estimated from the same data you're trying to clean. Small errors in the fit leave large residuals that mimic or corrupt the signal you're looking for. You're dividing by a poorly-known number.

**Naive approach 2 — Notch filter in the frequency domain.** Apply a bandstop filter around the QNM frequency. Problem: QNMs are not narrowband in the frequency domain. A damped sinusoid $e^{-t/\tau} \cos(2\pi f_0 t)$ has a Lorentzian frequency spectrum with half-width $1/(2\pi\tau)$ — for typical GW ringdown damping times of ~10–15 ms, this is ~10–15 Hz wide. A notch broad enough to catch the QNM also eats into the direct wave's spectrum, which lives nearby. You'd be removing the signal you want along with the contamination.

**Naive approach 3 — Time-domain windowing.** Just analyze data only after the QNMs have decayed sufficiently. Problem: the direct wave exists *before* the QNMs become dominant — it's a merger-phase signal, not a ringdown-phase signal. By the time the QNMs are small, the direct wave is already gone. There is no time window where the direct wave is present and the QNMs are absent.

The rational filter solves all three problems simultaneously.

---

## The Mathematical Structure

A damped sinusoid in the time domain is:

$$h_{\rm QNM}(t) = A \, e^{-t/\tau} \cos(2\pi f_0 t + \phi) \quad \text{for } t \geq t_0$$

This can be written in complex notation as the real part of $A e^{i\phi} e^{-i\omega^* t}$ where $\omega^* = 2\pi f_0 + i/\tau$ is the complex conjugate of the QNM frequency. More usefully, in the $z$-transform (the discrete-time version of the Laplace transform), a damped complex sinusoid $e^{-i\omega t}$ corresponds to a geometric sequence with ratio $z_0 = e^{-i\omega \Delta t}$ — a single pole in the $z$-plane.

Now here's the key idea. If a signal $h(t)$ contains a component $e^{-i\omega' t}$, and you apply the operator:

$$\mathcal{F}_{\omega'} = \frac{d}{dt} + i\omega'$$

to it, that component maps to:

$$\left(\frac{d}{dt} + i\omega'\right) e^{-i\omega' t} = -i\omega' e^{-i\omega' t} + i\omega' e^{-i\omega' t} = 0$$

Symbol definitions: $\omega'$ : complex frequency of the mode to be removed ($\omega' = 2\pi f_0 - i/\tau$, where $f_0$ is oscillation frequency and $\tau$ is damping time); $\mathcal{F}_{\omega'}$ : the first-order differential operator that annihilates $e^{-i\omega' t}$.

What this means: the operator $d/dt + i\omega'$ is an exact annihilator of the complex damped sinusoid at frequency $\omega'$. It zeros it out completely, regardless of amplitude or phase — those are free parameters that drop out. This is the fundamental reason the rational filter doesn't require fitting the QNM amplitude or phase first.

In discrete time (actual sampled data), the derivative $d/dt$ becomes a difference operator, and $\mathcal{F}_{\omega'}$ becomes a first-order IIR (infinite impulse response) filter with a zero at $z_0 = e^{-i\omega' \Delta t}$ in the $z$-plane.

---

## Building Up to Multiple Modes

To remove $N$ QNM components simultaneously, you cascade $N$ such first-order operators:

$$\mathcal{F} = \prod_{k=1}^{N} \left(\frac{d}{dt} + i\omega_k'\right)$$

Symbol definitions: $\omega_k'$ : complex frequency of the $k$-th QNM to be removed; the product means applying each operator in sequence.

This is a rational filter — the name comes from its transfer function in the frequency domain, which is a rational function (ratio of polynomials) in $s$ or $z$. The numerator polynomial has roots at the QNM frequencies $\omega_k'$; those are the zeros of the transfer function. At those exact complex frequencies, the filter has zero gain — it transmits nothing. Everywhere else, it transmits the signal with a gain that depends on how far you are from the zeros.

The resulting transfer function is:

$$H(s) = \prod_{k=1}^{N} (s + i\omega_k')$$

What this actually means: think of the transfer function as a terrain in the complex plane. At each QNM frequency $\omega_k'$, the terrain has a valley that goes all the way to zero — a "zero" in the signal-processing sense. The filter's output at that frequency is exactly zero, regardless of how large the input is. At other frequencies — including the direct wave frequency — the terrain is above zero, so the signal passes through, attenuated by a factor that depends on the distance from the zeros.

The analogy: this is like a noise-canceling headphone that doesn't just reduce the engine hum broadly — it *exactly* cancels the engine hum at its precise frequency and all its harmonics, while leaving your music completely untouched. The cancellation is exact because it exploits the known mathematical structure of the noise (damped sinusoid = pole in the $z$-plane = zero in the annihilating filter), not a statistical estimate of the noise level.

---

## Why the Filter Doesn't Need to Fit Amplitudes or Phases

This is the non-obvious payoff. The operator $d/dt + i\omega'$ annihilates $A e^{i\phi} e^{-i\omega' t}$ for *any* $A$ and *any* $\phi$:

$$\left(\frac{d}{dt} + i\omega'\right) A e^{i\phi} e^{-i\omega' t} = A e^{i\phi} \left(-i\omega' + i\omega'\right) e^{-i\omega' t} = 0$$

The amplitude $A$ and phase $\phi$ factor out and multiply zero. So the filter removes the QNM completely without needing to know its excitation amplitude or starting phase — the two quantities that are hardest to determine from data and that make naive subtraction unreliable.

What the filter *does* need to know: the complex frequency $\omega' = 2\pi f_0 - i/\tau$ — equivalently, both the oscillation frequency $f_0$ and the damping time $\tau$. For Kerr QNMs, these are determined solely by the remnant mass and spin, which are measured from the full inspiral-merger-ringdown parameter estimation independently of this analysis. So the filter inputs are known quantities, not free parameters.

This is the key asymmetry: QNM frequencies are pinned by the no-hair theorem to $(M_f, \chi_f)$; QNM amplitudes and phases depend on the specific merger geometry and excitation history and are not predicted from first principles. The rational filter exploits exactly what is known (frequency) and sidesteps exactly what isn't (amplitude, phase).

---

## What Happens to Everything Else

After the filter removes components at $\omega_1', \omega_2', \ldots, \omega_N'$, the output contains:

- Everything in the original signal that is *not* a damped sinusoid at those exact frequencies
- Detector noise, modified by the filter's transfer function (which is not unity everywhere)
- The direct wave, which lives at a different and evolving complex frequency

The direct wave survives because its instantaneous frequency is not equal to any $\omega_k'$. How much does it survive? The attenuation of the direct wave by the filter depends on how close the direct wave's frequency is to the QNM zeros. If the direct wave frequency is well-separated from all the QNMs, attenuation is small. In GW250114 this separation is sufficient — the paper shows in Figure 4 that the inferred direct-wave parameters lie clearly away from the QNM dashed contours.

The noise is also modified — the filter is not flat across frequency, so the noise floor is reshaped. This has to be accounted for in the subsequent statistical analysis, which is why the Bayesian inference that follows uses a noise model that reflects the filtered noise spectrum rather than the raw detector noise.

---

## Why This Specific Problem Needed This Specific Tool

Three properties of rational filters make them uniquely suited here:

**Exactness.** The annihilation of the target QNMs is mathematically exact, not approximate. This matters because the direct wave's SNR (~14) is small compared to the QNM SNR, so even a 1% residual from an imperfect QNM subtraction could be comparable in power to the direct wave you're trying to find.

**Amplitude-phase independence.** As argued above, the filter doesn't need to know the QNM excitation amplitudes or phases — the quantities that would require fitting and would introduce parameter estimation uncertainty into the cleaning step.

**Time-domain operation.** The rational filter operates causally in the time domain, which preserves the time-domain structure of the direct wave. A frequency-domain notch filter would smear temporal features; this filter doesn't.

The cost: the filter does modify the noise, and it attenuates signals near the QNM frequencies (not just at them). If the direct wave were very close in frequency to a QNM, the filter would suppress it too. In the GW250114 case, the separation is sufficient, but this is a genuine constraint on when the method works.

---

## The Specific Application in the Paper

For GW250114, the authors remove four QNM components: $(\ell=2, m=2, n=0)$, $(\ell=2, m=2, n=1)$, $(\ell=2, m=2, n=2)$, and $(\ell=3, m=2, n=0)$. The complex frequencies of all four are computed from the independently measured $(M_f, \chi_f)$ using tabulated Teukolsky equation solutions. Four first-order operators are cascaded into a single fourth-order rational filter. The output is the strain with those four modes exactly cancelled — and the direct wave, the noise floor (reshaped), and any nonlinear QNMs or other residual signals left behind.

That cleaned output is then what they hand to the Bayesian inference engine to fit the direct-wave damped sinusoid model — and, separately, to the matched-filter analysis with the full Oshita et al. template.

## Human

too much math in this response, give how they work without as much math

## Assistant

Explaining

Fair point. Here's the same explanation with the math stripped out.

---

## The Problem

After a binary black hole merger, the LIGO data in the merger window contains several overlapping signals at once. The dominant ones are the quasinormal modes — the loud, characteristic ringing of the remnant as it settles down. The direct wave is also present, but it's much quieter, buried underneath the QNM ringing.

The direct wave's SNR in GW250114 is around 14. The dominant QNM is far louder than that. If you look at the raw data you simply cannot see the direct wave — it's like trying to hear someone whisper in the front row while a brass band plays behind them.

So you need to remove the QNMs first. Three obvious approaches all fail:

**Fit a model and subtract it.** Estimate the QNM amplitude and phase, compute what they look like, subtract. Problem: fitting the QNM parameters introduces errors, and even a small fitting error leaves a large residual — because the QNMs are so much louder than the direct wave, a 1% subtraction error produces a residual comparable in size to the signal you're trying to find.

**Apply a frequency-domain notch filter.** A notch filter kills everything near a target frequency. Problem: the direct wave lives near the same frequency range as the QNMs. A notch wide enough to catch the QNM also removes the direct wave you're trying to preserve.

**Wait for the QNMs to die.** Analyze only the late ringdown, after the QNMs have decayed. Problem: the direct wave exists only during and just after the merger peak. By the time the QNMs have quieted down, the direct wave is already gone. There is no time window where one is present and the other isn't.

The rational filter solves all three problems at once.

---

## The Core Idea

A damped sinusoid — which is exactly what each QNM is — has a very precise mathematical structure. It oscillates at a specific frequency and decays at a specific rate. Together, those two numbers (oscillation frequency and decay rate) completely specify what kind of object it is, independent of how loud it is or what phase it starts at.

It turns out that you can construct a mathematical operation that, when applied to any signal, completely zeros out anything with that exact frequency-and-decay-rate combination — regardless of amplitude, regardless of phase, regardless of when it started. The operation exploits the known structure of the thing you want to remove. It doesn't need to know how loud the QNM is, or what phase it's in. It only needs to know those two numbers: oscillation frequency and decay rate.

For Kerr black holes, those two numbers are not free parameters — they are fixed entirely by the remnant's mass and spin, which are measured independently from the full inspiral-merger-ringdown signal. So the filter inputs are known going in. Nothing has to be fit from the data being cleaned.

---

## Why This Is Different From Subtraction

In ordinary subtraction you estimate the QNM's amplitude and phase from the data, construct a best-fit model, and remove it. The problem is that amplitude and phase are not predicted by theory — they depend on the specific geometry of the merger, and fitting them introduces uncertainty. Any mismatch between the fitted model and the actual QNM leaves a residual.

The rational filter sidesteps amplitude and phase entirely. The annihilation works for any amplitude and any phase — they just cancel out in the math. You only need the frequency and decay rate, which are theoretically predicted. This is the key asymmetry: what theory knows (frequency, decay rate) is exactly what the filter uses; what theory doesn't know (amplitude, phase) is exactly what the filter ignores.

---

## What Survives

After the filter runs, anything in the data that was oscillating at the exact QNM frequencies is gone. Everything else survives — attenuated somewhat if it's close in frequency to the zeros, but present. The direct wave, which oscillates at a different and slowly evolving frequency, is not cancelled. The detector noise survives (reshaped somewhat by the filter). Any nonlinear QNMs or other residual effects that weren't in the filter's target list also survive.

That cleaned output is what the authors then hand to their Bayesian inference — fitting a damped sinusoid model to look for the direct wave signal that's now visible without the dominant QNM ringing on top of it.

---

## The Analogy That Actually Holds

Noise-canceling headphones work by measuring the external noise with a microphone and generating an equal-and-opposite sound wave to cancel it. But that requires continuously estimating the noise in real time, and it works imperfectly when the noise changes faster than the system can track.

The rational filter is more like a physical resonance trap. If you know a pipe resonates at exactly 440 Hz and you want to remove that frequency from a recording, you can design a physical notch that has a node — a point of zero displacement — at exactly 440 Hz, without touching anything else. The rational filter is the signal-processing equivalent: it is engineered to have an exact zero at the complex frequency of each QNM. Not a minimum, not a suppression — a genuine zero. Anything at that exact complex frequency is annihilated completely.

The cost is that frequencies *near* the zeros are attenuated too, not just the zeros themselves. In GW250114 the direct wave's frequency is sufficiently separated from the QNM frequencies that this attenuation is acceptable. For a different event with different parameters that separation might be smaller, and the filter would be more damaging to the signal you want to preserve — that's the genuine limitation of the approach.
