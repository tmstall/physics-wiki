---
source: claude_export
conversation_uuid: af4e5b7a-3c82-4d0c-9b9d-0d61f09c3a1c
title: "\"Two Clocks, One Laser, Zero Excess Noise:"
created_at: 2026-07-10T03:36:34.196186Z
updated_at: 2026-07-10T04:13:38.786330Z
tier: A
score: 250
n_messages: 4
---

# "Two Clocks, One Laser, Zero Excess Noise:

## Human

Analyze paper

## Assistant

*(Full text — Article, Methods, and Extended Data — was provided directly in-context, so no retrieval was needed. Pre-read: this is a full Nature Article with substantial experimental and statistical content, not a lite candidate; proceeding to full analysis.)*

---

## 1. Punchy Title & One-Sentence Hook

**"Two Clocks, One Laser, Zero Excess Noise: Proving the Mid-Band Detector's Core Trick with the Hard Isotope"**

The AION team drowns each of two strontium atom interferometers in several *radians* of laser phase noise — enough to completely erase every individual fringe — and still pulls the differential signal out clean at the fundamental quantum floor, exactly as a kilometre-scale gravitational-wave detector will need to.

---

## 2. Big-Picture Context

Gravitational-wave astronomy has a hole in its hearing. Ground-based laser interferometers (LIGO, Virgo, KAGRA) hear roughly 10 Hz to 1000 Hz; the future space mission LISA will hear 10⁻⁴ Hz to 10⁻¹ Hz. Between them — the "mid-band," roughly 0.1 Hz to 10 Hz — nobody hears anything yet. That gap is where two prizes sit: mergers of *intermediate-mass* black holes (10²–10⁴ solar masses, the suspected building blocks of the supermassive black holes at galactic centres), and the slow multi-week inspiral of stellar-mass binaries *before* they sweep up into LIGO's band — which would let you predict where and when to point telescopes for multi-messenger astronomy.

Atom interferometers are the leading proposal to fill that gap. Instead of bouncing light between mirrors, they split and recombine the quantum matter-waves of freely-falling atoms, using laser pulses as beam-splitters and mirrors. A passing gravitational wave stretches the baseline, changing the light-travel time between two widely-separated atom clouds, which shows up as a phase shift. Proposed experiments — AION (UK), MAGIS (US), AICE (CERN), and the space concept AEDGE — all rely on this. The same setup is simultaneously a scalar ultralight-dark-matter detector: a dark-matter field around 10⁻¹⁵ eV would make atomic energy levels oscillate, shifting the clock tick rate.

There's one dragon guarding this treasure: **laser phase noise**. The single laser that interrogates both clouds jitters in phase by amounts orders of magnitude larger than the quantum measurement floor. The entire program rests on one bet — that if you run *two* interferometers off *one* laser (a "gradiometer") and measure only their *difference*, the shared laser noise cancels in common mode while the physics signal survives. The principle was demonstrated years ago with bosonic $^{88}$Sr and with $^{87}$Rb, but only "to within known limitations." Nobody had quantified *how completely* it cancels, and nobody had done it with the isotope that a real space/km detector actually requires.

**Paper Type & Stakes:** This is an experimental proof-of-principle / milestone paper — a 1-mm tabletop prototype that rigorously validates the noise-rejection *principle* (not the detector sensitivity) using the demanding species. The stakes: if common-mode rejection doesn't actually reach the quantum floor with fermionic $^{87}$Sr on its single-photon clock transition, the noise-cancellation foundation of the whole mid-band program is in question. This paper shows it does.

**Prior Belief Check:** This *confirms* mainstream expectation rather than overturning it — no expert believed common-mode rejection was impossible. What's genuinely non-trivial and would mildly surprise a specialist is the *degree*: injecting several radians of noise (Gaussian, σ = 4π rad, per shot) and measuring **zero** statistically significant excess above the standard quantum limit — 16(17) μrad of headroom, consistent with zero. That the demanding $^{87}$Sr clock transition, with its hyperfine mess and millihertz linewidth, behaves this cleanly is the reassuring part. This is a high-quality de-risking result, not a discovery. Calibrated honestly: it moves a technology-readiness needle, not a physics paradigm.

**Replication & Convergence Note:** This specific $^{87}$Sr single-photon demonstration is single-group (AION). But the *underlying principle* enjoys convergent support from independent groups using different species ($^{88}$Sr, ref. 24; $^{87}$Rb, refs. 25,26), which raises confidence in the mechanism itself. Independent confirmation of *this* result would look like MAGIS-100 or another $^{87}$Sr collaboration reproducing SQL-limited common-mode rejection under injected noise — which matters because the systematic error budget of clock-transition interferometry is species- and apparatus-specific.

---

## 3. Necessary Background Crash-Course

**Atom interferometer (matter-wave Mach–Zehnder).** An atom's wavefunction is put into a superposition of two paths by a laser "beam-splitter" pulse, redirected by a "mirror" pulse, and recombined by a final beam-splitter. The probability of finding the atom excited depends on the phase difference between the two paths — exactly like optical interference, but the interfering thing is the atom's de Broglie wave.

*Analogy:* it's a signal routed down two traces on a board and recombined; the output level encodes the phase skew between the traces.
**Breaks when:** you forget the atom carries rest mass and an internal clock. The path phase includes the atom's own internal transition frequency ticking during flight, so this interferometer is *also* a clock — an optical trace-pair isn't.

**Clock transition / single-photon interferometry.** These atoms are driven on the $^1S_0 \to {}^3P_0$ optical clock transition of $^{87}$Sr at 698 nm — the same ultra-narrow transition used in the world's best atomic clocks. A single photon does the splitting (unlike two-photon Raman schemes in $^{87}$Rb).

*Analogy:* a reference oscillator with an astronomically high Q — a crystal so stable it barely drifts over a 150-second lifetime.
**Breaks when:** you picture a classical vibrating crystal. The "tick" here is the quantum phase accumulating between two energy eigenstates in superposition — there is no physical oscillation, just a phase.

**Gradiometer / common-mode rejection.** Run two interferometers (top cloud, bottom cloud, 1 mm apart) off the *same* clock laser. Both pick up the identical laser phase noise. Subtract them, and the shared noise vanishes while a real gradient signal (a gravitational wave stretching the baseline, or dark matter shifting one clock relative to the other) survives.

*Analogy:* **differential signaling** — an LVDS pair, USB, or twisted-pair Ethernet. The receiver reads the *difference* between two conductors; interference coupled equally onto both lines is common-mode and gets rejected, while the intended differential signal passes.
**Breaks when:** the two receivers don't see *identical* interference. At km baselines the laser wavefront takes real time to propagate from one cloud to the other, so the "common" noise is no longer perfectly common — timing/wavefront effects break the cancellation. At 1 mm and 200 μs, that's negligible; at a kilometre it is the central unsolved engineering problem.

**Standard Quantum Limit (SQL) / atom shot noise.** With N unentangled atoms, the phase you can resolve is limited by the statistical spread of counting discrete two-level outcomes — noise scaling as one-over-root-N.

The relevant scaling is:

$$\sigma_{\delta\phi} \propto \frac{1}{\sqrt{N}}$$

**Symbol definitions:**
- $\sigma_{\delta\phi}$ : the smallest resolvable spread in the differential phase (radians)
- $N$ : number of atoms contributing to the measurement

**What this actually means:** it's the quantization/shot-noise floor of an ADC or a photodiode — the irreducible statistical hash you get from counting a finite number of discrete quanta. More atoms, lower floor.
**Breaks when:** you treat it as a hard wall like thermal noise. It's the *unentangled* floor; squeezed atomic states can push below it (a stated future goal). Also don't conflate it with the Heisenberg limit, which is the much steeper 1/N floor entanglement can eventually reach.

**Central analogy for this paper: a differential signaling pair rejecting common-mode noise.**

---

## 4. Core Technical Explanation

**What they built.** Two crossed optical dipole traps hold clouds of fermionic $^{87}$Sr (~2 μK) separated vertically by 1 mm. The clouds are released into free fall. An ultrastable 698-nm clock laser fires a three-pulse Mach–Zehnder sequence (π/2 – π – π/2), with a 44-μs π-pulse and a 200-μs dark time between pulses, creating two simultaneous interferometers interrogated by that one common laser. A velocity-selection pulse first skims off only the slowest atoms so the Rabi pulses are clean. A separate off-resonant "Stark-shifting" beam hits *only the top* interferometer, imprinting a controllable bias phase — this deliberately puts the two-interferometer data on a Lissajous *ellipse* rather than a line, which carries more information about the differential phase.

**The phase bookkeeping.** A single interferometer's phase decomposes as:

$$\phi = \int_{-\infty}^{\infty} \omega_0\, g(t)\, dt + \phi_{\text{laser}} + \phi_{\text{other}}$$

**Symbol definitions:**
- $\phi$ : total accumulated phase of one interferometer (radians)
- $\omega_0$ : angular frequency of the atomic clock transition (radians/second)
- $g(t)$ : a switching function that is −1 on the first arm segment, +1 on the second, 0 otherwise — it encodes which way the "clock ticks" count
- $\phi_{\text{laser}}$ : phase stamped onto the atoms by the laser's own phase during pulses (the enemy)
- $\phi_{\text{other}}$ : background gravitational/EM contributions, irrelevant to the signal

**What this actually means:** think of it as three accumulators summing into one register — a signal term (the clock ticking, gated by g(t)), a noise term (laser jitter), and a slowly-varying offset. The gradiometer's whole job is to make the noise register read identically in both interferometers so it cancels on subtraction.

**The signal it's sensitive to.** A gravitational wave changes the baseline, giving a differential phase:

$$\delta\phi_{\text{GW}} = \pm\,\frac{\delta L}{c}\,\omega_0$$

**Symbol definitions:**
- $\delta\phi_{\text{GW}}$ : differential phase induced between the two interferometers (radians)
- $\delta L$ : the tiny change in baseline length caused by the wave (metres)
- $c$ : speed of light (metres/second)
- $\omega_0$ : clock transition angular frequency (radians/second)

**What this actually means:** the wave subtly changes when the laser pulse arrives at the far cloud versus the near cloud — a timing skew of δL/c — and because each cloud is a high-frequency clock, that timing skew gets multiplied up by ω₀ into a measurable phase. It's a delay line whose length is being wobbled by spacetime, read out by two very fast clocks.

**The two-dataset test.** They interleaved, shot-by-shot over 61.9 hours (56,623 shots), a **low-laser-noise (LLN)** set (only the clock laser's intrinsic noise) and a **high-laser-noise (HLN)** set, where they deliberately injected large uncorrelated phase jumps (Gaussian, σ = 4π rad) between pulses to *emulate* what a km-baseline detector will suffer when multi-second laser drift piles up. In the HLN data, each individual interferometer's fringes are **completely obliterated** (Fig. 4a, bottom) — a single interferometer retains no recoverable phase. Yet the differential phase survives.

**How they actually extract δφ (this is the clever engine).** They do *not* fit each interferometer separately and subtract. They run a joint **unbinned maximum-likelihood** fit over both interferometers' excitation fractions, treating the shot-to-shot common phase as a *nuisance parameter* and mathematically integrating it out (marginalizing over a uniform prior). The signal lives in the *correlation* between the two clouds — the shape of the Lissajous ellipse — not in either phase alone. This is why washing out the individual fringes doesn't destroy the measurement.

**Headline numbers.** The quantum floor (Cramer–Rao SQL) is 43.5(16) mrad per shot, set by ~3,100 and ~2,040 atoms in the two traps; extrapolated over the full run, 258(10) μrad. The measured excess of HLN over the SQL is **16(17) μrad**, and HLN over LLN is **14(19) μrad** — both consistent with **zero** additional noise despite several radians of injected laser noise. A 5,100-run Monte Carlo, pushed through the identical analysis pipeline, agrees (p = 0.82 HLN, p = 0.65 LLN), and the Allan-deviation slopes (~ −0.465) match the white-noise −0.5 scaling expected of a shot-noise-limited instrument averaging down cleanly.

**Second result — oscillatory signal recovery (Fig. 5).** They injected sinusoidal signals via the Stark beam across 10⁻⁴ to 10⁻¹ Hz, parameterized as a coherent oscillation, and recovered them at SQL-limited resolution with Q > 5,000 — *in the fully phase-randomized HLN regime where a single interferometer is blind*. Amplitude recovery scaled linearly and correctly favoured the null hypothesis when nothing was injected. This is the "you literally cannot do this with one interferometer" demonstration.

### Assumption Audit

**Watch:** Reader likely assumes the injected laser noise faithfully emulates a real detector's noise. **The paper actually says** it neglects the noise's effect on *mirror-pulse fidelity* — the injection is applied as discrete phase steps *between* pulses, so it tests common-mode cancellation of accumulated phase but not the degradation of pulse quality that real continuous noise during finite pulses would cause.

**Watch:** Reader likely assumes reaching the SQL here means the device is near gravitational-wave sensitivity. **The paper actually says** the SQL here is set by only ~3,100/2,040 atoms and a 1-mm baseline; this validates the *noise-rejection principle*, and sensitivity to actual GWs depends on baseline, atom number, momentum transfer, and interrogation time — none at detector scale.

**Watch:** Reader likely assumes the demonstrated 10⁻⁴–10⁻¹ Hz band is the detector's target science band. **The paper actually says** that band is an artifact of the prototype's ~3-s shot cycle and hours-to-day run duration — it is *not* the 0.1–10 Hz mid-band target. A real detector engineers its band via interrogation time, repetition rate, and baseline; the frequencies here are coincidental to the slow cadence.

**Watch:** Reader likely assumes "differential" means subtract two independently-measured phases. **The paper actually says** δφ comes from a *joint* likelihood fit that marginalizes the common phase; independent subtraction would fail because each individual fringe is destroyed — the recoverable information is in the two-cloud correlation, not either phase.

---

## 5. What's Genuinely New or Clever

**1. The species leap, quantified.** Moving from bosonic $^{88}$Sr / $^{87}$Rb to fermionic $^{87}$Sr on the single-photon clock transition — the isotope a real space/km detector *needs* (near-ideal clock properties, 150-s excited-state lifetime) — and demonstrating that its hyperfine and millihertz-linewidth complications don't spoil common-mode rejection. This is *new to the field*, not just to the reader: it pins down the prior work's "to within known limitations" caveat with a hard number (zero excess noise within ~17 μrad).

**2. The marginalized-common-phase maximum-likelihood estimator.** Treating the scrambled common phase as a nuisance parameter and integrating it out lets the analysis extract the differential signal *even when every individual fringe is destroyed*. Older binned ellipse-fitting can't do this robustly in the fully phase-randomized regime; this ML approach has negligible bias and lower statistical error and remains functional at σ = 4π rad. The signal-injection recovery (Fig. 5) is the proof that this is a real, general capability, not a one-off.

---

## 6. Limitations & Open Questions

The 1-mm baseline and 200-μs dark time test no wavefront-propagation or laser-delay effects. **(A) Consensus** — the paper acknowledges this and everyone in the field knows km baselines introduce propagation delay and wavefront curvature that partly break common-mode cancellation. *(paper discussion; broader literature — Le Gouët, ref. 27)*

The injected noise neglects mirror-pulse fidelity degradation. **(A) Consensus** — stated explicitly in the paper; real continuous noise during finite pulses is a known separate effect. *(paper, Fig. 4 discussion)*

Atom numbers (~3,100/2,040) are modest, and the SQL only drops with more atoms — but higher atom number and density bring collisional shifts and readout systematics. **(A) Consensus** that more atoms are needed; the *ease* of getting there is less settled. **(B) Contested** on how cleanly density scales. *(paper, future work; broader literature)*

The demonstrated frequency band is not the mid-band target and is set by the slow prototype cadence; the claim that the band simply "shifts by design" into 0.1–10 Hz *while preserving* SQL-limited rejection is asserted, not demonstrated here. **(B) Contested / (C) Speculative** on the preservation-at-scale part — it's a reasonable engineering expectation but unproven. *(paper §; analyst inference)*

Full sensitivity targets large momentum transfer (~10⁴ photon recoils), which imprints laser noise n-fold and drives *deeper* into the phase-randomized regime; LMT on a narrow clock transition is hard and adds its own systematics. **(B) Contested** — an active R&D frontier with no guaranteed path. *(paper, future work; broader literature)*

This precise $^{87}$Sr single-photon result is single-group. **(A) Consensus** that independent replication would strengthen confidence, tempered by convergent evidence from other species. *(analyst inference / field norm)*

---

## 7. Detailed Summary & Explanation

The AION collaboration built a small tabletop version of a mid-band gravitational-wave and dark-matter detector and used it to prove the single most important thing such detectors must do: cancel laser noise. Two clouds of strontium-87 atoms sit 1 mm apart and are read out by one shared clock laser. Each cloud becomes a tiny atom interferometer — effectively an extraordinarily fast, stable clock. Because both clouds share the same laser, the laser's phase jitter lands on both identically. The detector reads only the *difference* between the two, so the shared jitter cancels the way common-mode interference cancels on a differential signaling pair, while a genuine signal (spacetime stretching the gap, or dark matter shifting one clock relative to the other) survives.

To prove the cancellation is real and not marginal, they deliberately poisoned the laser with several radians of random phase noise per shot — enough that each individual interferometer's signal turns to pure hash, with no recoverable information at all. They then measured the *difference* channel and found no measurable extra noise above the fundamental quantum floor set by counting atoms: the excess is consistent with zero to within about seventeen millionths of a radian. A separate 5,100-run simulation, processed through the exact same analysis, agrees, and the way the noise averages down over time matches the clean statistical behavior of a device limited only by atom-counting noise. In a second test, they injected fake oscillating "signals" across a range of very low frequencies and recovered every one of them at the quantum-limited resolution — something flatly impossible for a single interferometer in this regime.

The key interpretive choices worth flagging: first, "reaching the standard quantum limit" here is a statement about *noise rejection*, not detector sensitivity — the device is 1 mm long with a few thousand atoms, nowhere near sensing a real gravitational wave. Second, the frequency range shown is a quirk of the slow prototype, not the physics band a real detector would target. Third, and most technically important, the "differential" measurement is not a naive subtraction — the shared, scrambled phase is treated as a mathematical nuisance and integrated away, so the surviving information lives in how the two clouds' outputs *correlate*, not in either one alone. The takeaway: the noise-rejection principle underpinning the entire AION/MAGIS/AEDGE program now has rigorous experimental validation with the hard, detector-relevant isotope — a genuine milestone, with the hard scaling problems (baseline, atom number, momentum transfer, wavefront effects) still ahead.

**Where I'm least confident in this analysis:** the statistical machinery — specifically how the Cramer–Rao SQL is constructed from the marginalized likelihood, how the "zero excess noise" figures (16(17) and 14(19) μrad) propagate through the hybrid Bayesian–frequentist pipeline, and the precise logic of the Allan-slope consistency test. My plain-language rendering of the marginalization and the Monte Carlo closure test almost certainly smooths over real subtleties in how uncertainties are assigned; that's the part to dig into independently if the exact error budget matters to you.

---

## 8. Three Crystallized Takeaways

1. **They deliberately blinded each of two atom interferometers with several radians of laser noise, then recovered the shared signal at the fundamental quantum floor — proving common-mode rejection works about as perfectly as a differential signaling pair rejecting interference.**

2. **The real advance is doing it with fermionic strontium-87 on its single-photon clock transition — the demanding, detector-relevant isotope — and quantifying that "zero excess noise" means zero to within ~17 millionths of a radian.**

3. **This validates the *principle* behind mid-band gravitational-wave detectors, not the detectors themselves: it's a 1-mm prototype, and the km-baseline, atom-number, and wavefront-propagation problems are all still ahead.**

---

## 9. Shorter Summary

Gravitational-wave astronomy has a gap between ground-based detectors (LIGO/Virgo/KAGRA) and the future space mission LISA — the "mid-band" near 0.1–10 Hz, home to intermediate-mass black-hole mergers and early binary inspirals. Atom interferometers are the leading way to fill it, but they face one dominant obstacle: laser phase noise, which jitters far above the quantum measurement floor. The proposed fix is a gradiometer — two atom interferometers run off one laser, measuring only their difference, so the shared laser noise cancels like common-mode interference on a differential signaling pair.

This paper is the experimental proof that the fix works, using the hard, detector-relevant isotope strontium-87. Two clouds of atoms 1 mm apart, read out by a common clock laser, form the two interferometers. The team deliberately injected several radians of random laser noise — enough to completely erase each individual interferometer's signal — and still recovered the differential measurement at the fundamental atom-counting floor, with excess noise consistent with zero (about 17 millionths of a radian of headroom). Simulations processed identically confirm the device behaves as a purely quantum-noise-limited instrument. In a second test, they injected artificial oscillating signals across low frequencies and recovered every one at quantum-limited precision — impossible for a single interferometer in this regime.

The essential subtlety: the "difference" is not a naive subtraction. The scrambled shared phase is treated as a mathematical nuisance and integrated away, so the surviving information lives in how the two clouds' outputs correlate, which is why destroying the individual fringes doesn't destroy the measurement.

Read honestly, this confirms rather than overturns expectations — nobody thought common-mode rejection was impossible — but it pins down *how completely* it works with the demanding isotope, which is genuinely reassuring for the field. Crucial caveats: this validates the noise-rejection principle, not detector sensitivity; the device is 1 mm long with a few thousand atoms. The demonstrated frequency range reflects the slow prototype, not a real detector's target band. The hard scaling problems — kilometre baselines, many more atoms, large momentum transfer, and wavefront-propagation effects that partly break the cancellation — all remain ahead. A solid milestone on a long road.

## Human

Explain How they actually extract δφ (this is the clever engine). They do not fit each interferometer separately and subtract. They run a joint unbinned maximum-likelihood fit over both interferometers' excitation fractions, treating the shot-to-shot common phase as a nuisance parameter and mathematically integrating it out (marginalizing over a uniform prior). The signal lives in the correlation between the two clouds — the shape of the Lissajous ellipse — not in either phase alone. This is why washing out the individual fringes doesn't destroy the measurement.

## Assistant

Explaining

Here's the core move, and it's genuinely elegant once you see it: **they throw away the absolute phase entirely and keep only the relative phase, because the absolute phase is exactly the part the laser noise ruins.**

Let me build it up in the terms that'll click for you.

**The setup in two lines**

Each interferometer's excitation fraction (the fraction of atoms found in the excited state) is a cosine of its phase:

P₁ ≈ offset + contrast · cos(φ₁)
P₂ ≈ offset + contrast · cos(φ₂)

Now decompose each phase into a **common** part and a **differential** part:

φ₁ = φ_c + Φ/2
φ₂ = φ_c − Φ/2

φ_c is the shared phase — dominated by laser noise, and in the HLN regime it's scrambled to a *uniformly random* value every single shot. Φ is the differential phase, the signal you actually want, and it's stable shot to shot.

The problem is stark: measure φ₁ by itself and you get φ_c + Φ/2 with φ_c random, so φ₁ is just uniform noise. That's the "individual fringe washed out" — literally no information survives in either interferometer alone.

**Why the correlation survives — the oscilloscope XY analogy**

This is the part your instincts will lock onto immediately. Take the two excitation fractions and plot P₁ against P₂ — X-Y mode on a scope, one signal into each channel. Over many shots, φ_c wanders randomly, which sweeps the point (P₁, P₂) *around a closed curve*. Because the two cosines differ only by the fixed offset Φ, that curve is a **Lissajous ellipse whose shape — its tilt and openness — is set entirely by Φ**. The random φ_c only controls *where on the ellipse* each individual shot lands; it does nothing to the ellipse's shape.

So scrambling the common phase doesn't destroy anything you need. It just samples the ellipse at random points around its perimeter — arguably *better* than a coherent measurement, because you fill the whole figure out evenly. You've lost the ability to say where any single shot sits in absolute terms; you never needed that. You needed the ellipse's geometry, and random sampling reveals it cleanly.

**The comms analogy that nails the estimator**

This is differential phase-shift keying. DPSK works precisely because it encodes information in the phase *difference* between symbols, so the receiver never needs to know the absolute carrier phase — which is smart exactly when that carrier phase is drifting or unknown. The atom gradiometer is doing the same trick against a laser whose absolute phase is garbage: the signal is protected by living in the differential, and a non-coherent receiver "integrates over the unknown carrier phase" to read it out.

That integration-over-the-unknown-phase *is* the marginalization step.

**What "marginalize over a uniform prior" concretely does**

They write down the full likelihood — the actual binomial probability of getting the observed excited/not-excited counts for the discrete atoms in *both* clouds — as a function of Φ *and* the per-shot nuisance phase φ_c. Then, for each shot, they don't try to pin down φ_c; they integrate it out:

for each candidate Φ, sum the probability of this data over every possible value φ_c could have taken, weighted equally.

The uniform prior isn't a convenient approximation here — in the HLN regime φ_c genuinely *is* uniformly distributed, so integrating with a flat weight is the physically correct thing to do. The candidate Φ that makes the observed two-cloud correlations most probable, averaged over all possible common phases, wins. The common phase is treated as something you don't care about and refuse to estimate, rather than something you subtract.

**Why unbinned ML rather than just fitting an ellipse**

Two reasons. First, *unbinned*: each shot's exact excitation fraction feeds the likelihood directly — no arbitrary binning choice, no information smeared away, which matters when atom numbers are modest. Second, and this is the real reason they don't literally fit an ellipse: **geometric ellipse-fitting is statistically biased.** It's a known pathology — the fitted phase systematically drifts, especially at low contrast or small Φ. The marginalized ML estimator has negligible bias and lower variance, and critically it keeps working at σ = 4π rad where the fringes are fully randomized. Figure 5's signal recovery is the proof it's a general, robust estimator and not a regime-specific fluke.

**So the one-sentence version of why fringe destruction doesn't kill it:** the laser noise lives entirely in the common phase, which only sets *where on the ellipse* each shot lands; the signal lives in the *shape* of the ellipse, which random common-phase sampling reveals just fine — and the ML fit reads that shape off the raw correlated counts without ever needing to know, or subtract, the noise itself.

One caveat worth flagging so I'm not overselling the geometry: the ellipse picture has intrinsic symmetries (a sign/orientation degeneracy in Φ), and the Stark-imposed bias phase plus the full likelihood parameterization are what resolve those. The ellipse is the right *intuition*; the actual estimator is doing the careful version of that intuition with the degeneracies handled properly.
