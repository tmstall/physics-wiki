---
source: claude_export
conversation_uuid: c4c4cae5-20f5-4e86-b124-227909281a02
title: "Thorium-229 nuclear clock analysis"
created_at: 2026-06-14T07:33:38.778396Z
updated_at: 2026-06-14T07:36:48.188195Z
tier: A
score: 239
n_messages: 2
---

# Thorium-229 nuclear clock analysis

## Human

2 simiIlar papers and combine them together and give a detailed  analyze them together. Publication details
L. Toscani De Col et al, A thorium-229 optical nuclear clock with feedback loop, arXiv (2026). DOI: 10.48550/arxiv.2606.04997

Beichen Huang et al, A nuclear clock based on 229Th, arXiv (2026). DOI: 10.48550/arxiv.2606.08870

## Assistant

Let me fetch both papers before diving in.

Now I have enough to do a thorough comparative analysis. Let me build the full v3.6.1 response.

---

v3.6.1

---

# 1. Punchy Title & One-Sentence Hook

**The Nucleus Keeps Time: Two Independent Teams Build the World's First Working Nuclear Clocks — Simultaneously**

Two labs on opposite sides of the planet, one in Vienna and one in Beijing, independently crossed the same historic threshold in the same week: they locked a laser to the nucleus itself, not to electrons, producing the first self-sustaining nuclear clocks — and immediately used them to hunt for dark matter.

---

# 2. Big-Picture Context

Every clock in human history has counted something that oscillates. Pendulums swing. Quartz crystals vibrate. Atomic clocks count the electromagnetic frequency at which electrons hop between orbital energy levels. The best of these — optical lattice clocks based on strontium or ytterbium — are so stable that they wouldn't gain or lose a second in 30 billion years. We've been riding this technology curve for seventy years, and the returns are getting harder and harder to squeeze out.

A nuclear clock takes a fundamentally different approach: instead of an electron transition in the atom's outer shell, it uses a transition *inside the nucleus itself*. The nucleus is roughly 100,000 times smaller than the atom and couples far more weakly to external electric and magnetic fields that corrupt clock accuracy. Think of the difference between tuning a guitar string stretched across a room full of people (lots of acoustic interference) versus tuning one sealed inside a vacuum vault (almost none). The nuclear "string" is almost completely isolated from environmental noise.

The catch is that almost every nucleus transitions between energy levels via gamma rays or X-rays — megaelectronvolt-scale photons that no laser on Earth can conveniently produce. There is exactly one known exception in all of nuclear physics: the isomeric state of ^{229}Th (thorium-229). The exceptionally low isomeric excitation energy of about 8.4 eV in this nucleus results from an accidental near-cancellation between two enormous energy scales — the Coulomb (electromagnetic) force and the strong nuclear force. That near-cancellation pushes the transition energy down to the vacuum-ultraviolet (VUV) optical range, right where laser technology can just barely reach it. This energy corresponds to a wavelength of about 148.4 nanometers.

The proposal to build a nuclear clock using ^{229}Th was first formalized by Peik and Tamm in 2003. The subsequent two decades involved painstaking narrowing of the transition energy (originally uncertain by nearly 100 eV) and engineering the VUV lasers needed to probe it. By 2024–2025, several groups had successfully *excited* the nucleus with a laser but hadn't yet built a clock — a clock requires that the laser be *steered by the nucleus*, closing a feedback loop. Previous studies demonstrated that it was possible to excite the ^{229}Th nucleus using VUV lasers stabilized to external frequency standards, but no system existed in which the laser interrogating the nuclei was steered by the nuclear transition itself. These two June 2026 papers are the first to close that loop.

**Prior Belief Check:** This result is genuinely major — not in the "every paper is revolutionary" sense but in the "this is the culmination of a 20-year experimental program" sense. The field has been building to this moment since 2003, and experts have been expecting it *soon* but not necessarily *this* week from *two independent groups simultaneously*. The coincidence of publication days is striking and confirms the field reached technical readiness around the same time globally. Neither paper overturns theory — they validate a long-anticipated concept. What's surprising even to insiders is the dark matter sensitivity already achieved at this early, non-optimized stage.

---

# 3. Necessary Background Crash-Course

**Nuclear isomers.** A nucleus can exist in excited configurations — protons and neutrons rearranged into higher-energy collective patterns — that then decay back to the ground state. Most do this in nanoseconds. ^{229}Th's excited state (called ^{229m}Th) is extraordinarily long-lived: roughly 10 minutes for a bare nucleus in vacuum. That long lifetime means the transition is extremely narrow in frequency (energy-time uncertainty), which is what makes it useful for precision timekeeping. A narrow transition is like a very sharp notch filter — you can lock a laser to it with extraordinary precision.

*Analogy:* Think of the nuclear isomeric lifetime like a very high-Q resonator in a crystal oscillator. A high-Q crystal rings at its natural frequency for a long time before damping out, and that persistence is precisely what makes it a good frequency reference. The longer the ringdown, the sharper the frequency peak, the more precisely you can lock to it. ^{229}Th has a nuclear Q-factor on the order of ten quintillion (10^{19}).

*Breaks when:* You push this to ask why the nuclear clock isn't already far more stable than an atomic clock. In a crystal oscillator analogy, Q equals precision — but in a real clock, you also need *lots of oscillators* (atoms) contributing signal simultaneously to beat down shot noise. The Vienna team uses billions of nuclei in a crystal, not a single nucleus, so solid-state dephasing from the crystal environment currently limits performance far below the bare-nucleus limit.

**Calcium fluoride host crystal (Th:CaF₂).** Neither team probes bare ^{229}Th nuclei in vacuum. Instead, they dope ^{229}Th atoms (at concentrations of parts per million to parts per thousand) into transparent calcium fluoride crystals. Both teams embedded thorium-229 nuclei in crystals of calcium fluoride and probed them with a finely tuned continuous-wave laser operating at around 148 nanometers. The crystal acts as a rigid lattice host that keeps the nuclei spatially confined (the "Lamb-Dicke regime" — recoil-free absorption), allowing room-temperature operation without laser cooling. You get signal from billions of nuclei at once, trading some intrinsic linewidth broadening (from crystal field inhomogeneity) for massive signal-to-noise improvement.

*Analogy:* It's like the difference between timing individual cars on a highway versus measuring the average speed of a dense traffic flow with a radar gun. You lose the ability to track individual cars precisely, but your statistical measurement of the bulk is far more robust.

*Breaks when:* Pushed to accuracy, not just stability. The crystal environment shifts the nuclear transition frequency relative to a bare nucleus in vacuum — the amount of shift depends on crystal composition, temperature, strain, and defect density. This means the solid-state nuclear clock can be *stable* (reproducible) without necessarily being *accurate* (tied to an absolute fundamental frequency) at the sub-10⁻¹⁵ level until these environmental systematics are carefully characterized.

**Vacuum ultraviolet (VUV) lasers at 148 nm.** Air absorbs photons below about 190 nm, so the entire optical path must live in vacuum. Generating coherent light at 148 nm requires multiple stages of nonlinear frequency conversion. The required laser radiation at 148 nm wavelength has been produced using pulsed laser systems, but the nuclear resonance can also be excited with a continuous-wave (CW) laser source with less than 1 nanowatt of power, detected in absorption rather than fluorescence — eliminating the slow nuclear fluorescence decay from the detection process and offering considerable advantages for clock operation.

*Analogy:* Building a VUV laser is like trying to make AM radio signals by doubling shortwave, then doubling again, then doubling again — each stage losing efficiency but gaining access to a range of the electromagnetic spectrum that nature makes inconvenient to reach.

*Breaks when:* You ask about power scaling. The nonlinear conversions are intrinsically inefficient — the Vienna team uses sub-nanowatt VUV power, meaning the nuclear signal is extracted from a trickle of photons. More power would improve signal-to-noise dramatically, but scaling VUV power is a hard materials problem (most optics degrade rapidly under intense VUV irradiation).

**Feedback loop / closed-loop clock operation.** An atomic clock stabilizes a local oscillator (laser or microwave source) by repeatedly interrogating the atomic transition and feeding back an error signal. An optical clock is based on an atomic transition of narrow linewidth, probed by a clock laser with long coherence time. By stabilizing this laser to the atomic resonance, the laser can inherit the desired stability and reproducibility from the atom. In these two papers, the "atom" is replaced by the nucleus. Closing this loop — making the nucleus *steer* the laser rather than just being *probed* by it — is the definitional step from "nuclear spectroscopy" to "nuclear clock."

*Breaks when:* You assume feedback is instantaneous. Because nuclear absorption must be averaged over many photon counts to get a statistically clean error signal, the feedback bandwidth is limited to roughly once per several seconds or tens of seconds. This means short-term laser noise isn't suppressed by the nuclear signal — you still need a high-quality optical cavity to stabilize the laser at timescales shorter than the feedback update rate.

---

# 4. Core Technical Explanation

## Vienna team (Toscani De Col et al., TU Wien + PTB)

The Vienna group builds a two-tier servo architecture that any Intel performance engineer would recognize immediately: a fast inner loop for short-term noise, a slower outer loop for long-term drift correction, and a reference comparison to an external "gold standard."

**Inner loop — cavity stabilization:** They stabilize a 1187 nm external-cavity diode laser (ECDL) to a high-finesse Fabry-Pérot optical cavity using Pound-Drever-Hall locking. This is the workhorse of optical clock engineering — it suppresses laser phase noise at kHz-to-MHz timescales down to millihertz linewidths. Think of it as the L1 cache of the clock: fast, local, and very high bandwidth.

**Frequency upconversion:** The 1187 nm seed laser gets frequency-quadrupled (two sequential second-harmonic generation steps plus a final strontium tetraborate crystal doubling stage) to produce the 148 nm VUV interrogation beam with sub-nanowatt power in continuous-wave mode. This is the key technical enabler — prior work used pulsed VUV lasers, which can't be used for CW absorption spectroscopy (you can't generate a continuous error signal from a pulsed probe).

**Outer loop — nuclear feedback:** The VUV beam passes through the Th:CaF₂ crystal (a millimeter-scale slab at room temperature, 294.7 K). They modulate the interrogation frequency between two frequencies on either side of the nuclear resonance and measure how much absorption changes between them via a photomultiplier tube (PMT) in photon-counting mode. This differential absorption signal is their error signal. They feed it back via an electro-optic modulator (EOM) to offset the cavity-locked laser frequency, correcting for long-term cavity drift. The nuclear transition now *steers* the laser. The clock is closed. This constitutes the first implementation of a nuclear clock that operates as a stand-alone device.

**Comparison to external standard:** A frequency comb (an infrared frequency synthesizer) referenced via a Doppler-compensated fiber link to a Yb⁺ single-ion clock at the Austrian Bureau of Metrology (BEV) in Vienna lets them continuously compare the nuclear clock's output to one of the world's best atomic clocks. This is the performance benchmark.

**Performance:** The nuclear clock shows shot-noise limited scaling of the fractional frequency instability, approaching 10⁻¹⁵ instabilities over one day of continuous operation. Shot-noise limited means the dominant noise source is the fundamental quantum randomness of photon detection, not technical noise — the clock is operating at the statistical floor for its current signal rate. They also use the clock immediately to constrain ultralight dark matter, searching for periodic fluctuations and slow drifts in the nuclear transition energy on timescales between 20 seconds and one day, finding constraints that compete with the best atomic clocks on dark matter coupling to photons and go beyond previous measurements regarding coupling to the strong force and quarks.

## Beijing team (Huang et al., Tsinghua + NIM + SIOM + PKU)

The Chinese team used a more powerful laser than the Vienna group, while the Vienna team worked with a crystal containing a higher concentration of thorium nuclei. Both teams converge on Th:CaF₂ as the crystal host and CW VUV at 148 nm as the probe.

The Tsinghua group's VUV laser system originates from a separate major contribution: a continuous-wave narrow-linewidth VUV source published in Nature in 2026, which the same group (Xiao et al.) developed — essentially, the laser infrastructure paper preceded the clock paper by weeks. Higher VUV power gives more photon flux through the crystal, potentially better short-term signal-to-noise at the cost of slightly lower thorium concentration in the crystal host.

Their clock architecture is conceptually parallel to Vienna's: lock a narrow-linewidth VUV laser to the nuclear transition in Th:CaF₂, read out absorption, close the feedback loop, compare to a traceable frequency standard. They demonstrate the operation of a ^{229}Th nuclear clock by stabilizing a continuous-wave narrow-linewidth 148.4 nm VUV laser to a resolved nuclear transition in a solid-state host. The Beijing team demonstrated that its device could stabilize the frequency of its VUV laser, locking it to the nuclear transition with a fractional frequency instability approaching one part in 10 trillion after a day of operation — roughly consistent with the Vienna result.

## Assumption Audit

**Watch:** You might assume the nuclear clock is already more accurate than the best atomic clocks. It isn't — yet. The current results demonstrate *stability* (repeatability, low random noise over time) at the 10⁻¹⁵ level after a day of averaging, but *accuracy* (absolute agreement with the true transition frequency, free of systematic shifts from the crystal environment, temperature, magnetic fields, etc.) has not yet been characterized at this level. The best optical atomic clocks have verified accuracy at the 10⁻¹⁸ level. Nuclear clocks will need extensive systematic error budgeting before claiming superior accuracy.

**Watch:** You might assume that because both teams are doing essentially the same experiment, one is simply replicating the other. The papers were submitted four days apart (Vienna on June 3, Tsinghua on June 7) with no evidence of coordination. This is a genuine simultaneous convergence — both groups independently reached the required technical threshold (CW VUV source + CaF₂ crystal + feedback loop) in the same month. The slightly different engineering choices (crystal concentration vs. laser power) represent independent design decisions under the same physical constraints.

---

# 5. What's Genuinely New or Clever

**1. The closed feedback loop itself** — this is the definitional breakthrough. Dozens of groups have excited ^{229}Th with lasers since 2024. Neither those experiments nor previous Vienna/PTB spectroscopy work closed the loop where the *nucleus controls the laser*. The feedback architecture is conceptually simple but required solving a hard engineering problem: generating a continuous error signal from absorption of sub-nanowatt VUV light through a millimeter crystal at room temperature, and doing it fast enough to usefully correct laser drift. The modulation-based absorption error signal is the key trick — it bypasses the 10-minute nuclear fluorescence lifetime entirely, using the nuclear transition as an absorber (like a notch filter in feedback) rather than a fluorescence emitter.

**2. Dark matter sensitivity on day one** — the Vienna team immediately turns the nuclear clock into a dark matter detector. This isn't an afterthought. The large values of the Coulomb and strong-force energies and their near-cancellation make the ^{229}Th nucleus an excellent testing ground to look for time variation of the fine-structure constant or interactions with dark matter that might affect the strong-force energy. Because the Th transition energy arises from a near-cancellation of two huge quantities, any new physics that nudges either the electromagnetic or strong-force coupling constants will produce an outsized fractional change in the nuclear clock frequency relative to an atomic clock frequency. Even with the current modest performance, the Vienna team's dark matter constraints on strong-force coupling already exceed prior limits from electron-shell atomic clock comparisons — a remarkable first-generation result.

---

# 6. Limitations & Open Questions

**Systematic frequency shifts from the crystal environment are essentially uncharacterized at the 10⁻¹⁵ level.** The CaF₂ crystal applies electric field gradients (from crystal imperfections and lattice phonons) that shift the nuclear quadrupole energy levels and thus the clock frequency. Temperature variations of ±0.5 K around room temperature produce frequency drifts. The clock currently tracks these drifts at the 10⁻¹² level but cannot correct them below that without a full systematic error budget. **(A) Consensus — acknowledged explicitly in both papers and the broader field.**

**The transition frequency measured in the crystal differs from the bare-nucleus frequency in vacuum.** For a nuclear clock to serve as a proposed redefinition of the SI second or for cross-laboratory comparisons, this crystal shift must be measured and corrected. Different crystal hosts (CaF₂ vs. LiSrAlF₆) give slightly different frequencies due to different crystal field environments. This is an unsolved problem. **(A) Consensus.**

**Single-polarization, single-quadrupole-transition probing.** Both papers probe a specific spin projection of the quadrupole-split ground state transition. The full quadrupole structure has multiple lines, and different crystals have different strain-induced inhomogeneous broadening. Whether one can find a "magic" crystal environment where systematic shifts cancel — analogous to "magic wavelength" optical lattice clocks for atoms — is unknown. **(B) Contested — some theorists believe magic conditions exist; others doubt it for this crystal system.**

**VUV power is the limiting noise floor.** Both teams operate with sub-nanowatt VUV, giving photon detection rates that limit shot-noise performance to ~10⁻¹² at 1 second. Orders-of-magnitude improvement in power would push this floor down dramatically, but VUV power scaling is constrained by optical component damage and nonlinear conversion efficiency. The Tsinghua VUV source (published in Nature, 2026) represents the state of the art; further scaling routes exist but aren't demonstrated. **(A) Consensus.**

**Dark matter constraints assume a scalar ultralight dark matter field with specific coupling models.** The dark matter bounds from the Vienna paper are genuinely new for strong-force coupling but apply to a narrow class of models (nucleophilic scalar bosons oscillating at specific frequencies). They don't constrain vector dark matter, topological defects, or dark matter with masses above the inverse-day frequency. **(C) Speculative — my read of the dark matter model assumptions; a specialist should verify the exact coupling parameter space covered.**

**No ion-trap nuclear clock yet.** The solid-state approach accepts inhomogeneous broadening from the crystal as a trade-off for large signal. The ultimate precision route — a single ^{229}Th³⁺ ion in a laser-cooled trap, with no crystal perturbations — has not yet produced a working clock. That device would offer far better systematic control but requires trapping a radioactive ion and generating sufficient VUV signal from a single nucleus. **(A) Consensus — widely acknowledged as the next generation.**

---

# 7. Three Crystallized Takeaways

1. **The nuclear clock has arrived.** Two independent groups, working in Vienna and Beijing, simultaneously demonstrated the first nuclear clocks that operate as self-sustaining devices — the laser is now steered by the nucleus, not the other way around. This is the culmination of a 23-year experimental program and a genuine step-change in timekeeping technology.

2. **The nucleus is a better clock because it doesn't care about the outside world.** Atomic clocks are perturbed by electric and magnetic fields that push and pull on electron orbits; nuclear clocks are almost immune, because the nucleus is tiny and deep inside the atom. The solid-state crystal environment partially negates this immunity today, but the fundamental physics advantage remains and will drive future clock performance well beyond current atomic clock limits.

3. **The nuclear clock is already a dark matter detector.** Because ^{229}Th's transition energy arises from a freakish near-cancellation of electromagnetic and strong-force energies, any dark matter particle that nudges the strong force will produce a gigantic fractional shift in the nuclear clock frequency — far larger than in any atomic clock. Even in its first week of operation, the Vienna clock's dark matter constraints on strong-force coupling exceeded what decades of atomic clock comparisons could achieve.

---

# 8. Detailed Summary & Explanation

Both papers report the construction and first operation of working nuclear optical clocks — devices that use a transition *within the atomic nucleus* rather than in the electron shell to define a stable oscillation frequency.

The physical heart of both experiments is the isomeric state of ^{229}Th (thorium-229), a radioactive nucleus with a unique property: its first excited state sits only about 8.4 electron-volts above the ground state. For context, this is about the same energy as a UV photon from a germicidal lamp — absurdly low for a nuclear transition, where the norm is millions of electron-volts for gamma rays. The reason is a remarkable coincidence of nuclear structure: two enormous energy contributions from electromagnetic and strong-force interactions very nearly cancel each other, leaving a residual gap small enough for laser light to bridge. This near-cancellation is not just a timekeeping convenience — it means the transition is exquisitely sensitive to any new physics that would shift either contribution, making ^{229}Th a natural dark matter antenna.

To probe the nucleus, both teams generate continuous-wave (CW) laser light at 148 nanometers — deep in the vacuum ultraviolet, a wavelength at which ordinary air is completely opaque. The laser systems require multiple stages of nonlinear optical frequency doubling, starting from infrared diode lasers and cascading to shorter and shorter wavelengths. The resulting VUV beam carries less than a nanowatt of power — far less than a dim night-light — but that's enough to produce measurable absorption when passed through a crystal of calcium fluoride doped with trace amounts of ^{229}Th. The crystal acts as a room-temperature solid-state container holding billions of nuclei in fixed positions, eliminating the need for cryogenics or complex ion-trapping setups.

The clock operation works as follows. A cavity-stabilized laser handles short-term frequency stability (milliseconds to seconds). The VUV beam, derived from this laser, probes the nuclear transition continuously in absorption. An error signal derived from how much absorption changes as the laser frequency is dithered slightly around the nuclear resonance gets fed back to correct the laser frequency for long-term drift. Now the nuclear transition is *steering* the laser — the clock is closed. Both teams compare their nuclear clock output to a Yb⁺ single-ion atomic clock via frequency comb and fiber link, characterizing the nuclear clock's instability as a function of averaging time.

The results from both teams are consistent: fractional frequency instability at roughly three to ten parts in ten trillion (around 10⁻¹²) at short averaging times, improving as expected for random noise (going down as the square root of averaging time) and approaching 10⁻¹⁵ after one day of continuous operation. The Vienna team additionally performs a first search for ultralight dark matter by looking for oscillations or slow drifts in the nuclear clock frequency that would be absent in the atomic clock, setting new constraints on dark matter coupling to the strong force.

The framing of the summary reflects the genuine significance of closing the feedback loop — that single engineering step is what distinguishes these papers from the extensive spectroscopy work that preceded them. The dark matter application is highlighted because it's the most immediate scientific payoff beyond the clock itself, and because it illustrates why the nuclear transition's near-cancellation physics is scientifically valuable, not just metrologically convenient.

**Where I'm least confident in this analysis:** The specific details of the Tsinghua (Huang et al.) paper's clock architecture, systematic error discussion, and dark matter constraints — I have the abstract and secondary coverage but could not retrieve the full HTML of the Tsinghua paper. My characterization of the Tsinghua paper as "conceptually parallel" to Vienna's is well-supported by available sources, but the specific technical differences in feedback scheme, error signal generation, and performance at short averaging times may be more significant than I've conveyed. Treat the Tsinghua section as accurate in broad strokes but potentially missing important detail-level distinctions.

---

# 9. Shorter Summary

Two teams — one in Vienna (TU Wien and Germany's PTB national metrology institute) and one in Beijing (Tsinghua University, NIM, SIOM, and Peking University) — simultaneously built and operated the world's first nuclear clocks in early June 2026. These clocks use the same physical principle: a laser locked not to electron transitions in an atom's outer shell, but to a transition deep inside the nucleus of thorium-229.

Thorium-229 is unique in all of nuclear physics. Its nucleus has an excited state — a rearrangement of its protons and neutrons — that sits only about 8.4 electron-volts above the ground state, a freakishly small energy gap produced by an accidental near-cancellation between the electromagnetic force and the strong nuclear force. This means visible-to-ultraviolet light can drive the transition, unlike every other nucleus where the equivalent energies correspond to hard X-rays or gamma rays. Because the nucleus is tiny and sits deep inside the atom, it couples far more weakly to environmental electric and magnetic fields than electrons do, making it a potentially superior clock reference.

Both teams solved the same core engineering challenge: generating stable continuous-wave laser light at 148 nanometers (deep vacuum ultraviolet, where air is opaque) and using it to probe thorium nuclei embedded in transparent calcium fluoride crystals at room temperature. By continuously monitoring how much the laser is absorbed by the crystals and feeding that signal back to correct the laser frequency, they built closed-loop clocks — devices where the nucleus itself keeps the laser on frequency. This is the definitional step from "nuclear spectroscopy experiment" to "nuclear clock."

The performance of both clocks at this early stage already approaches a fractional frequency instability of about one part in one quadrillion (10⁻¹⁵) after one day of averaging — competitive with mature optical atomic clocks that took decades to optimize. The Vienna team immediately used their nuclear clock as a dark matter detector, searching for the tiny oscillations in nuclear transition frequency that a hypothetical ultralight dark matter particle would produce. Even in this first-generation form, the nuclear clock's dark matter constraints on coupling to the strong force surpassed what previous atomic clock comparisons had achieved, because the near-cancellation that makes thorium-229 usable as a clock also makes its frequency extraordinarily sensitive to any new physics that disturbs the strong nuclear force.

Future improvements — higher VUV laser power, better crystal engineering, improved systematic error characterization, and eventually trapping single thorium ions in vacuum instead of crystals — are expected to push nuclear clock performance well beyond current atomic clocks, potentially enabling new precision tests of the Standard Model and direct searches for dark matter, dark energy, and variations in fundamental constants.
