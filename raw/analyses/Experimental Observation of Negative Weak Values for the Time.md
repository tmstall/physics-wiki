- 

Toggle Sidebar

![](Experimental Observation of Negative Weak Values for the Time/da39a3ee5e6b4b0d3255bfef95601890afd80709.webp "pfp"){width="0.7874in" height="0.3937in"}

Share

<div>

detailed analysis of this paper summary

</div>

<div>

Thought for 9s

It looks like the paper summary you'd like me to analyze wasn't included in your message (no text, link, image, or attachment appears here).

Could you please paste the full summary, share a link to the paper (or the summary itself), or upload any relevant image/PDF excerpt? Once I have it, I'll provide a **detailed analysis** covering:

- Core claims and contributions
- Methodology strengths/weaknesses
- Key results and their statistical/interpretive rigor
- Novelty relative to prior work
- Limitations and potential biases
- Broader implications and real-world impact
- Any red flags or overclaims

Just drop the summary here and I'll dive right in!

</div>

<div>

![](Experimental Observation of Negative Weak Values for the Time/da39a3ee5e6b4b0d3255bfef95601890afd80709.so){width="0.7874in" height="0.3937in"}

Details analysis of this paper

</div>

<div>

Thought for 1m 0s

**Detailed Analysis of the Paper: \"Experimental Observation of Negative Weak Values for the Time Atoms Spend in the Excited State as a Photon Is Transmitted\"**

This is the **published version** (Phys. Rev. Lett. **136**, 153601, 13 April 2026) of the arXiv preprint 2409.03680 (submitted 5 Sep 2024) by Daniela Angulo, Kyle Thompson, Vida-Michele Nixon, Andy Jiao, Howard M. Wiseman, and Aephraim M. Steinberg. The screenshot you shared is the official APS journal landing page.⁠Link.aps +1

### 1. Core Claim (in plain language)

When a resonant photon pulse travels through a cloud of atoms and is **transmitted** (i.e., does **not** get scattered/absorbed), how much time do the atoms spend in the excited state *because of that particular photon*?

The paper shows experimentally that this "dwell time" (measured via a weak-value technique) **equals the group delay** τ_g of the light pulse. Near atomic resonance, τ_g is **negative**---meaning the transmitted pulse's peak emerges *earlier* than it would in vacuum. The experiment directly observes correspondingly **negative weak-valued atomic excitation times**, down to **−0.82 ± 0.31 τ₀** (where τ₀ is the expected non-post-selected excitation time = scattering probability × atomic lifetime τ_sp).

In short: the atoms appear (on average, post-selected on transmission) to have been excited for a *negative* amount of time when the photon experiences negative group delay. This is not classical time travel or superluminal signaling; it is a genuine weak-value result tied to quantum interference and coherent forward scattering.

### 2. Background & Motivation

- **Group delay** τ_g = dφ/dω (phase derivative w.r.t. frequency) can be negative near resonance due to anomalous dispersion. Popular explanations ("pulse reshaping") often treat it as an artifact, not a real interaction time.
- Prior work (Sinclair et al., 2022) measured **positive** weak-valued excitation times for transmitted photons in one parameter regime.
- Recent theory (Wiseman, Steinberg et al., \~2025) predicted that the **weak-valued** atomic excitation time for a *transmitted* photon exactly equals τ_g---including negative values---via the time-integrated cross-Kerr phase shift on a probe beam.
- The question the experiment addresses: Does the negative group delay have *physical meaning* for the light-matter interaction, or is it purely kinematic?

The paper provides the first direct experimental confirmation that it does.

### 3. Experimental Method (Weak Measurement via Cross-Kerr Effect)

- **System**: Cold ⁸⁷Rb atoms in a magneto-optical trap (MOT).

- **Signal photon**: Near-resonant with the D2 line, sent as a weak coherent pulse (various durations and optical depths OD).

- **Probe**: A separate, weak, far off-resonant beam experiences a cross-Kerr phase shift proportional to the instantaneous number of excited atoms.

- **Measurement**:

  - Post-select on detection of the *transmitted* signal photon (heralding "no scattering" events).
  - Record the time-dependent phase shift φ(t) on the probe.
  - The integrated phase shift gives the weak value of the atomic excitation "dwell time" τ_T.

- Key innovation over prior work: Better noise suppression (ground loops, larger probe detuning), integration over the full time window rather than just the peak, and systematic variation of pulse bandwidth and OD.

This is a textbook example of a **weak measurement** of a "which-path"/dwell-time observable, post-selected on the "dark" (transmitted) port.

### 4. Key Results

- Measured weak-valued excitation times τ_T / τ₀ range from:

  - **−0.82 ± 0.31** (narrowband pulses, near resonance → negative group delay)
  - up to **+0.54 ± 0.28** (broadband pulses → positive group delay)

- These values **agree quantitatively** with the theoretical prediction τ_T = τ_g across multiple pulse durations and optical depths.

- Statistical uncertainties are sizable (\~30--60% relative error) but the trend and sign are clear and robust.

- The negative values are not noise; they match the sign and magnitude expected from group delay.

### 5. Theoretical Interpretation (Why Negative Times Make Sense Here)

- The transmitted photon is the one that **did not scatter**---i.e., the amplitude that interferes constructively in the forward direction via **coherent scattering** from the entire atomic ensemble.
- The "negative excitation time" arises because the early part of the transmitted pulse is actually **advanced** by destructive interference in the scattered light; the atoms are "un-excited" on average in a way that reshapes the pulse.
- Weak values are allowed to be negative (or outside the eigenvalue spectrum) because they are **conditional averages** over post-selected sub-ensembles. They are not ordinary expectation values.
- The paper (and Wiseman's popular explanations) emphasize that this gives negative group delay a **deeper physical meaning** than previously appreciated: it directly reflects the average interaction time *for the transmitted photons*.

### 6. Strengths & Novelty

- **First direct observation** of negative weak-valued atomic excitation times.
- Rigorous quantitative agreement with theory across parameter space.
- Clean use of cross-Kerr as a non-demolition probe of excitation number.
- Builds directly on (and improves) prior experimental work by the same group.
- Addresses a long-standing foundational puzzle in quantum optics: "How long does a photon spend inside an atom cloud?"

### 7. Limitations & Caveats

- **Post-selection**: All results are conditional on transmission. The *average* over all photons (including absorbed ones) is still positive, as required by causality.
- **Statistical power**: Error bars are large; the negative result is \~2.6σ from zero in the strongest case, but consistent with theory.
- **No superluminal signaling**: The negative delay is a pulse-reshaping effect; information cannot travel backward in time.
- The "negative time" phrasing in media is eye-catching but can mislead if not qualified as a **weak value** in a post-selected ensemble.
- Technical challenges (noise, correlations) were significant; the experiment required substantial improvements over the 2022 predecessor.

No obvious red flags or methodological flaws stand out. The results are conservative and well-controlled.

### 8. Broader Implications

- Reinforces the physical reality and utility of **weak values** in quantum foundations and metrology.
- Deepens our understanding of **slow/fast light**, coherent forward scattering, and pulse propagation in media.
- Has potential relevance to quantum information (e.g., quantum memories, photon storage) and precision timing measurements.
- Philosophically interesting for quantum contextuality and "what is real" in post-selected measurements.

### 9. Media & Popular Coverage

The preprint generated significant buzz in late 2024 / early 2025 (New Scientist, Scientific American, Phys.org, The Conversation, etc.). Headlines often use "photon spends negative time in atom cloud" or "negative time experiment." Authors (especially Wiseman and Steinberg) have given clear explanations emphasizing that this is **not** time travel but a surprising consequence of quantum interference and weak measurements.⁠Qspace.fqxi +1

**Bottom line**: This is a high-quality, technically impressive PRL that cleanly resolves a subtle but fundamental question about light-matter interaction times. It shows that negative group delays *do* correspond to negative (weak-valued) atomic excitation times for transmitted photons, lending them genuine physical significance via quantum post-selection and interference. The result is robust, theory-backed, and advances both foundational quantum optics and the interpretation of anomalous propagation effects.

If you'd like me to dive deeper into any section (e.g., the math of weak values, comparison to Sinclair 2022, full theory derivation, or specific figures from the arXiv PDF), pull quotes from the paper, or analyze the PDF itself, just let me know!

Add to chat

![](Experimental Observation of Negative Weak Values for the Time/Pictures/1000000100000100000001008A5AFDEA.png){width="2.6665in" height="2.6665in"}

![](Experimental Observation of Negative Weak Values for the Time/Pictures/1000000100000100000001008A5AFDEA.png){width="2.6665in" height="2.6665in"}

![](Experimental Observation of Negative Weak Values for the Time/2d7c9b60d1e2b4f4726141de2e4ab738110b9287.png){width="0.7874in" height="0.3937in"}

181 sources

</div>

<div>

PDF

Grok custom instr v3.4.10.pdf

Use the attach prompt labeled version 3.4.10 to a detailed analysis of this paper

</div>

<div>

Thought for 1m 24s

**1. Punchy Title & One-Sentence Hook**\
**Negative Atomic Excitation Times: Photons Advance by Forcing Atoms to "Un-Excited" in the Past**

A team from Toronto and Griffith has experimentally shown that when a resonant photon transmits through a cold cloud of \^{85}Rb atoms without scattering, those atoms spend a rigorously measured weak-valued time in the excited state that can be negative---and this value exactly equals the (sometimes negative) group delay experienced by the transmitted light pulse.

**2. Big-Picture Context**\
For decades, optical physicists have wrestled with the counterintuitive behavior of light pulses propagating through resonant media. When a photon pulse's frequency sits near an atomic absorption line, the group delay---the time shift of the pulse peak---can turn negative due to anomalous dispersion. This means the transmitted pulse emerges earlier than it would in vacuum, seemingly violating naive notions of causality and interaction time. Conventional wisdom chalked this up to mere wave-packet reshaping: the leading edge gets absorbed while the trailing edge gets re-emitted coherently, making the peak appear advanced without any information traveling faster than light.

Yet this explanation always felt incomplete to those of us who care about what actually happens inside the medium at the single-photon, single-atom level. If the group delay reflects how long the light "spends" interacting with the atoms, a negative delay should correspond to a negative interaction time---something many dismissed as unphysical. This new work by Angulo, Steinberg, Wiseman and collaborators tackles the question head-on using weak measurements in a cold atom cloud. It bridges foundational quantum mechanics with practical quantum optics, showing that post-selected, conditional averages (weak values) of atomic excitation times exactly track the group delay, even when negative.

For someone with your background in performance engineering and self-taught QFT/cosmology interests, think of this as debugging a complex cache-coherent system where you only look at successful cache hits: the conditional "dwell time" in a particular state can reveal surprising interference effects not visible in the average case. This experiment strengthens the physical reality of weak values and gives negative group delays a deeper ontological status beyond kinematics. It also touches on tunneling-time analogs in quantum optics, relevant to your interest in tunneling times and Bohmian interpretations.

The implications ripple into quantum memories, slow/fast light devices, and even foundational questions about time in quantum interactions---how much "time" does a virtual excitation really occupy in coherent scattering processes? In holographic operating-system views of the universe, it hints that post-selected conditional histories can sculpt effective bulk propagation times in ways that parallel replica-wormhole calculations or emergent spacetime from tensor networks.

**3. Necessary Background Crash-Course**\
They measure group delay because it quantifies how much a pulse peak shifts after traversing the medium, calculated as the frequency derivative of the phase shift. Analogy: like measuring latency spikes in a network router; negative group delay is akin to the packet header arriving "early" due to clever buffering and re-timing inside the switch fabric, not actual time travel.

They use weak values to extract conditional averages of observables that would otherwise be obscured. In weak measurement, you couple a pointer (here the probe beam phase) gently to the system (atomic excitation) and post-select on a final outcome (photon transmitted). This lets you measure averages that can lie outside the usual eigenvalue range, like negative times. Analogy: in CPU performance profiling, you sample branch predictor states only on cache-miss paths and discover conditional execution times that are negative in effective latency due to speculative execution rollbacks and forwarding.

They exploit the cross-Kerr effect because a far-detuned probe beam picks up a phase shift proportional to the instantaneous number of excited atoms via AC Stark shift. Analogy: imagine a probe laser acting like a high-speed oscilloscope probe that senses voltage (excited atom population) without significantly disturbing the circuit (signal photon path), giving a non-destructive readout of the "current" flowing through the atomic excitations.

Coherent forward scattering explains why transmitted photons still "use" the atoms: the entire ensemble radiates in phase in the forward direction, interfering constructively to reconstruct the pulse while individual atoms undergo virtual excitation. Analogy: like a phased-array antenna where elements briefly energize but the net wave emerges advanced due to destructive interference on unwanted paths.

**4. Core Technical Explanation**\
They prepare a cold cloud of \^{85}Rb atoms in a magneto-optical trap because it provides a dense, low-temperature ensemble (\~60--70 µK, \~1 mm long) with controllable optical depth for resonant interaction studies. They send a weak pulsed signal beam resonant with the D2 line (F=3 to F\'=4) because this maximizes absorption and dispersion effects near resonance. They shape the signal as Gaussian pulses with rms widths from 10 ns to 36 ns (comparable to the 26 ns spontaneous lifetime) and attenuate to mean photon numbers around 100 before interaction.

They overlap this signal with a continuous-wave probe beam detuned by about 20 MHz and very weak (few nW) because the probe experiences a cross-Kerr nonlinear phase shift directly proportional to the excited-state population. They detect transmitted signal photons with a single-photon counting module and post-select only on those detection events to isolate the conditional atomic response. They record the time-dependent phase shift on the probe using a beat-note interferometer with a frequency sideband reference, then subtract the no-click background to obtain the conditional phase φ_T(t).

They integrate this conditional phase shift over the relevant time window to extract the weak-valued atomic excitation time τ_T because the integrated phase directly reports the time-integrated excited atom number for the post-selected transmitted photons. They compare against the non-post-selected excitation time τ_0 = P_scatter × τ_sp (where P_scatter is the probability a photon scatters and τ_sp is the spontaneous emission lifetime) because this normalizes the result to the "average photon" behavior. They vary both pulse bandwidth and optical depth (OD \~2 to 4) because these parameters sweep the group delay from positive to strongly negative regimes.

In the results, they observe conditional phase shifts φ_T(t) whose integrated areas yield τ_T / τ_0 values ranging from −0.82 ± 0.31 for the narrowest (most resonant, negative delay) pulses to +0.54 ± 0.28 for broader pulses. These track the independently calculated group delay τ_g remarkably well, with theory curves matching experiment within error bars after minor time-alignment. (See the key time-resolved phase-shift data in Fig. 2 of the arXiv preprint at <https://arxiv.org/pdf/2409.03680.pdf> for the clearest visual of negative excursions.)

**5. What's Genuinely New or Clever**\
First trick: They operationalize the "atomic excitation dwell time" for transmitted photons as the time-integrated weak value of the excited-state population operator, post-selected on transmission. This directly links an abstract theoretical construct to a measurable probe phase shift.

Second trick: They use an off-resonant probe in a beat-note configuration with careful noise isolation (ground loops, detuning optimization) to achieve the sensitivity needed to resolve tiny phase shifts (\~10--20 µrad) from single transmitted photons interacting with \~10\^4 atoms.

Third trick: Systematic parameter sweep across pulse durations and ODs to demonstrate quantitative agreement in both positive and negative regimes, going well beyond the prior positive-only result from Sinclair et al. (2022).

**6. Limitations & Open Questions**\
The error bars remain substantial (often 30--60% relative uncertainty), so while the sign and trend are clear, precision is not yet at the level where one could claim sub-percent agreement or explore finer spectral features. The results rely entirely on post-selection; the unconditional average excitation time stays positive, preserving causality---no information or energy travels backward. Technical noise (probe frequency jitter, residual correlations) still limits some data points, requiring heroic isolation efforts.

Scalability to room-temperature or solid-state systems looks challenging because cold atoms provide the clean, low-velocity ensemble needed for long coherence. Open questions include: how do these negative weak times manifest in multi-photon regimes or entangled states? Can one devise a stronger measurement or different observable that reveals the same physics without post-selection? Does this shed light on analogous "negative times" in quantum tunneling or black hole contexts you care about? Follow-up in 12--24 months should target higher OD, shorter pulses, or integration with quantum memory protocols.

**7. Three Crystallized Takeaways**

1.  Negative group delay isn't just wave-packet trickery---the atoms really do "un-excite" on average (weak-valued) for photons that make it through unscattered.
2.  Weak values give us a practical way to assign real physical interaction times to post-selected quantum paths, even when they go outside classical bounds.
3.  Coherent forward scattering lets transmitted photons borrow excitation "time" from the ensemble interference, advancing the pulse without violating causality.

**8. Detailed Summary & Explanation**\
In this Physical Review Letters paper (2026), Angulo et al. report the first experimental observation of negative weak-valued atomic excitation times caused by transmitted photons in a resonant \^{85}Rb cloud. They define the excitation time τ_T as the time-integrated number of excited atoms conditional on the photon being transmitted. Using a weak off-resonant probe to measure the induced phase shift via the cross-Kerr nonlinearity, they post-select on single-photon detections of the signal pulse. The integrated conditional phase shift directly gives τ_T.

Theory (building on their prior work) predicts τ_T equals the group delay τ_g of the transmitted light pulse. They confirm this quantitatively across multiple pulse bandwidths and optical depths: for narrowband pulses near resonance (where group delay is negative), they measure down to −0.82 ± 0.31 times the reference non-post-selected time τ_0; for broadband pulses (positive delay regime), positive values up to about 0.54 ± 0.28. This agreement holds because the transmitted amplitude arises from destructive interference of scattered light in non-forward directions and constructive forward emission from virtually excited atoms.

The experiment improves on their 2022 work by better noise control and broader parameter space. The negative times arise purely from quantum interference in the post-selected ensemble and do not allow superluminal signaling. This gives negative group delays a concrete microscopic interpretation as negative conditional dwell times of the atomic excitation. (Figure 2 in the paper shows the raw time-dependent conditional phase data with theory overlays; Figure 3 compiles the extracted τ_T / τ_0 vs. theory predictions across the full parameter grid---both available at <https://arxiv.org/pdf/2409.03680.pdf>.)

**9. Shorter Summary**\
Cold \^{85}Rb atoms appear to spend negative time (weak value down to −0.82 ± 0.31 τ_0) in the excited state when post-selecting on transmitted resonant photons; this time exactly equals the (sometimes negative) group delay of the light pulse, as confirmed by cross-Kerr probe measurements across pulse widths and optical depths.

![](Experimental Observation of Negative Weak Values for the Time/Pictures/1000000100000100000001008A5AFDEA.png){width="2.6665in" height="2.6665in"}

![](Experimental Observation of Negative Weak Values for the Time/Pictures/10000001000000B4000000B455B24077.png){width="1.8752in" height="1.8752in"}

![](Experimental Observation of Negative Weak Values for the Time/2d7c9b60d1e2b4f4726141de2e4ab738110b9287.png){width="0.7874in" height="0.3937in"}

98 sources

</div>

<div>

ExplainThey measure group delay because it quantifies how much a pulse peak shifts after traversing the medium, calculated as the frequency derivative of the phase shift. Analogy: like measuring latency spikes in a network router; negative group delay is akin to the packet header arriving "early" due to clever buffering and re-timing inside the switch fabric, not actual time travel.\
They use weak values to extract conditional averages of observables that would otherwise be obscured. In weak measurement, you couple a pointer (here the probe beam phase) gently to the system (atomic excitation) and post-select on a final outcome (photon transmitted). This

</div>

<div>

Thought for 22s

**Group delay** is the effective time shift of the *envelope* (the overall pulse shape) of a light wave packet after it travels through a dispersive medium like the cold \^{85}Rb atom cloud.

They calculate it directly from the frequency dependence of the phase the medium imprints on the light:

τ_g = ∂ϕ / ∂ω

where ϕ is the accumulated phase shift and ω is the angular frequency of the light.

Break the sentence before the equation.

**Next line:** centered LaTeX (only if it genuinely clarifies physics; otherwise describe in words).

τg=∂ϕ∂ω \\tau_g = \\frac{\\partial \\phi}{\\partial \\omega} τg​=∂ω∂ϕ​

**Symbol definitions:**\
**τ_g** : group delay (units: time, typically nanoseconds)\
**ϕ** : spectral phase acquired by the signal beam (radians)\
**ω** : angular frequency of the light (rad/s)

**What this actually means:** The group delay tells you how much later (or earlier) the *peak* of your pulse arrives compared with vacuum propagation. In your Intel days, imagine a network packet traversing a router fabric: the router's internal buffers and priority queues apply a frequency-dependent phase shift to the different Fourier components of the packet waveform. The net effect on the packet's envelope is exactly this group delay. When the pulse is narrowband and tuned near the atomic resonance, anomalous dispersion kicks in---the phase slope ∂ϕ/∂ω becomes negative---so the peak emerges *earlier* than it would in free space. That's the "negative group delay" you see in the paper.

**Analogy (network router):** Negative group delay is like the packet header arriving "early" because the switch fabric's clever buffering, speculative forwarding, and destructive interference on the trailing edge reshape the waveform in real time. The leading edge gets partially absorbed and re-radiated coherently, while the trailing edge gets reinforced. No actual data bit travels faster than c; the *envelope peak* just appears advanced due to interference inside the "router" (the atomic ensemble). The experiment shows this reshaping isn't just kinematics---it directly corresponds to a measurable atomic response.

**Weak values** (and the specific weak measurement of atomic excitation time) let them extract the *conditional average* of how long the atoms stay excited, but only for the sub-ensemble of photons that make it all the way through without scattering.

In standard quantum mechanics, if you measure the excited-state population operator N̂ (number of atoms in the excited state) strongly, you collapse the system and destroy the very transmission event you care about. Weak measurement solves this by coupling the system *gently* to a pointer (the probe beam's phase) and then post-selecting on the desired final outcome (a single-photon click in the transmitted channel). The result is the weak value of N̂, which can be negative or outside the usual \[0,1\] eigenvalue range because it's a *conditional* statistic, not an ordinary expectation value.

They define the weak-valued excitation time τ_T as the time integral of the real part of that weak value:

τ_T = ∫ Re(⟨N̂(t)⟩\_weak) dt

**Symbol definitions:**\
**τ_T** : weak-valued atomic excitation (dwell) time for transmitted photons (units: time)\
**N̂(t)** : operator for the instantaneous number of excited atoms\
**⟨...⟩\_weak** : weak-value average, post-selected on transmission

**What this actually means:** For the photons that get transmitted, the atoms appear (on average, in this conditional sense) to have spent a negative amount of time excited when the group delay is negative. This isn't magic or time travel; it's quantum interference at work. The transmitted amplitude is the one that interferes constructively in the forward direction. Early parts of the pulse are "un-excited" on average because the scattered light from virtual excitations destructively cancels everything except the advanced forward wave.

**Analogy (CPU performance profiling + speculative execution):** Think of it as sampling the branch-predictor state *only on cache-hit paths* in a processor pipeline. You discover that, conditional on a successful speculative execution that never flushes, the effective "dwell time" in a mispredicted micro-architectural state can be negative due to rollback and forwarding logic. The weak value is exactly that kind of conditional average---it reveals interference effects hidden in the average over *all* photons (including the ones that scattered). In the experiment they gently "probe" the atomic excitation with a far-detuned CW laser that picks up a cross-Kerr phase shift proportional to the excited-atom population, then integrate only the phase trace after post-selecting on a transmitted signal photon. That integrated phase shift is directly proportional to τ_T.

These two concepts are glued together in the paper: the measured weak-valued excitation time τ_T *exactly equals* the independently calculated group delay τ_g across the whole range of pulse bandwidths and optical depths. That's the punchline---the negative group delay isn't an artifact; it's the real (weak-valued) interaction time the transmitted photons "spend" inside the atoms.

If you want me to pull the exact figures from the arXiv PDF (Fig. 2 shows the raw time-dependent phase-shift traces with negative excursions; Fig. 3 plots τ_T/τ_0 vs. theory), dive into the cross-Kerr Hamiltonian details, or extend the router/CPU analogies to your holographic-operating-system or tensor-network interests, just say the word.

![](Experimental Observation of Negative Weak Values for the Time/Pictures/1000000100000100000001008A5AFDEA.png){width="2.6665in" height="2.6665in"}

![](Experimental Observation of Negative Weak Values for the Time/Pictures/10000001000000B4000000B455B24077.png){width="1.8752in" height="1.8752in"}

![](Experimental Observation of Negative Weak Values for the Time/Pictures/10000001000000B4000000B4A3E85225.png){width="1.8752in" height="1.8752in"}

70 sources

</div>

<div>

Don\'t really understand please explain a bit more simply no need to include any analogies

</div>

<div>

Thought for 13s

**Simple explanation of the two ideas (no analogies):**

### 1. Group delay (τ_g)

When a short pulse of light travels through the cloud of atoms, different frequency components of the pulse pick up different phase shifts from the atoms.

The **group delay** is simply the net time shift of the *peak* of the whole pulse after it passes through the cloud.

Mathematically it is:\
τ_g = dϕ / dω\
(where ϕ is the phase the medium adds to the light, and ω is the frequency of the light).

- Far from the atomic resonance → group delay is usually positive (pulse peak is delayed).
- Very close to the atomic resonance (narrowband pulses) → group delay becomes **negative**. The peak of the transmitted pulse comes out *earlier* than it would in empty space.

In the experiment they calculate this expected group delay from the known properties of the atoms and the pulse, then check whether the actual measured effect on the atoms matches it.

### 2. Weak values and the measured atomic excitation time (τ_T)

The key quantity they actually measure is **how long the atoms spend in the excited state, but only for the photons that make it all the way through the cloud without being scattered**.

They cannot measure this directly with a normal (strong) measurement because that would destroy the very photons they want to study. Instead they use a **weak measurement**:

- A very weak, far-detuned probe laser passes through the same cloud at the same time.
- This probe laser's phase is shifted very slightly by any atoms that are excited. The shift is proportional to the number of excited atoms at each moment.
- They record the tiny phase wiggles on the probe.
- They only keep the data from the shots in which a signal photon was detected after the cloud (i.e., it was transmitted). This is called **post-selection**.
- They integrate the phase shift over the duration of the pulse. That integral directly gives the **weak-valued excitation time τ_T** --- the effective time the atoms were excited *conditional on the photon having been transmitted*.

The experiment finds that this measured τ_T is numerically equal to the group delay τ_g (including when τ_g is negative).

In short:

- Group delay = calculated time shift of the pulse peak.
- τ_T (weak value) = measured effective time the atoms were excited for the transmitted photons.
- The paper shows these two numbers are the same, even when negative.

That is the central result: the negative group delay is not just a mathematical curiosity about the pulse shape; it corresponds to a real, measurable negative effective excitation time for the atoms when you look only at the transmitted photons.

</div>

<div>

More details no analgy Analogy (network router): Negative group delay is like the packet header arriving "early" because the switch fabric's clever buffering, speculative forwarding, and destructive interference on the trailing edge reshape the waveform in real time. The leading edge gets partially absorbed and re-radiated coherently, while the trailing edge gets reinforced. No actual data bit travels faster than c; the envelope peak just appears advanced due to interference inside the "router" (the atomic ensemble). The experiment shows this reshaping isn't just kinematics---it directly corresponds to a measurable atomic response.

</div>

<div>

Thought for 3s

**Negative group delay (more detail, no analogies):**

The group delay τ_g measures how much the peak of a light pulse shifts in time after passing through the atom cloud.

It is calculated as the rate of change of the phase ϕ that the atoms add to the light, with respect to the light's angular frequency ω:

τg=∂ϕ∂ω \\tau_g = \\frac{\\partial \\phi}{\\partial \\omega} τg​=∂ω∂ϕ​

In the experiment:

- They send a short pulse of light whose frequency is tuned very close to the main absorption line of the \^{85}Rb atoms (the D2 transition).
- For narrow pulses (longer duration in time, narrower frequency spread), most of the pulse's frequency components sit where the atoms cause a rapidly changing phase.
- In that region the derivative ∂ϕ/∂ω becomes negative. This means the pulse peak exits the cloud earlier than it would have in empty space.

This is called **negative group delay**. The pulse is not traveling faster than light overall---information and energy still respect the speed of light---but the shape of the transmitted pulse has its highest point arriving sooner because of how the atoms absorb and re-emit different frequency parts of the pulse.

The paper shows that this calculated negative τ_g exactly matches the measured weak-valued atomic excitation time τ_T for photons that make it through without scattering. In other words, the atoms behave as if they spent a negative amount of time excited when you look only at the transmitted photons.

**How they connect it to atomic response:**\
They use a separate weak probe laser that picks up a tiny phase shift whenever atoms are excited. After many repeated pulses they keep only the data where a signal photon was detected after the cloud (transmitted). The integrated phase shift on the probe then gives τ_T directly. Theory and experiment agree that τ_T = τ_g, including the negative values for the narrowband near-resonant pulses (down to about −0.82 times the reference time τ_0, with uncertainty ±0.31).

For broader pulses (wider frequency spread) the group delay becomes less negative or positive, and the measured atomic excitation time follows the same trend.

This is the key result: the negative group delay is not just a description of the pulse shape. It accurately predicts the actual (weak-valued) effect the transmitted photons have on the atoms, as read out by the probe.

Let me know if you want the same level of detail on the weak-value measurement itself or on any specific numbers/figures from the paper.

</div>

<div>

more details on This is called negative group delay. The pulse is not traveling faster than light overall---information and energy still respect the speed of light---but the shape of the transmitted pulse has its highest point arriving sooner because of how the atoms absorb and re-emit different frequency parts of the pulse.

</div>

<div>

Thought for 4s

**Negative group delay --- more detail (step by step, plain language):**

A light pulse is not a single pure frequency. It is made of many different frequency components added together (its Fourier spectrum). When the pulse center frequency is tuned very close to the atomic resonance (the main absorption line of the rubidium atoms), those frequency components experience very different absorption and phase shifts.

1.  **Leading edge of the pulse (the front part)** The earliest-arriving frequencies in the pulse sit right where the atoms absorb most strongly. A larger fraction of this leading-edge light gets absorbed (turned into atomic excitation). Less of it makes it through unchanged.

2.  **Middle and trailing parts of the pulse** The atoms that absorbed light from the leading edge quickly re-emit it (coherent forward scattering). Because of the exact phase relationship near resonance, this re-emitted light interferes constructively with the part of the original pulse that was not absorbed. The trailing part of the pulse therefore gets reinforced.

3.  **Net effect on the transmitted pulse shape**

    - The front of the transmitted pulse is weakened (more absorption).
    - The back of the transmitted pulse is strengthened (constructive interference from re-emitted light).
    - When you look at the overall shape of the pulse that comes out, its highest point (the peak) is now earlier in time than the original peak would have been.

This forward shift of the peak is the **negative group delay**. The amount of the shift is exactly τ_g = ∂ϕ/∂ω, which becomes negative in this resonant regime.

**Important limits (no faster-than-light issues):**

- The very first detectable part of the pulse (the absolute leading edge that carries new information) still arrives no earlier than it would in vacuum --- it respects the speed of light.
- Only the peak and the bulk of the energy in the already-formed pulse appear to come out earlier.
- You cannot use this to send a signal faster than light because any new information or sudden change must ride on that leading edge, which is not advanced.

In the experiment they confirm this reshaping is physically real for the atoms themselves: the weak measurement of atomic excitation (via the probe laser's phase shift, post-selected on transmitted photons) gives exactly the same negative time value as the calculated group delay. The atoms are not excited for a negative duration in an ordinary sense, but the conditional (post-selected) average excitation time is negative --- matching the forward shift of the transmitted pulse peak.

This is why the paper concludes that negative group delay has genuine physical meaning beyond "just pulse reshaping on paper." The transmitted photons really do correspond to a negative effective interaction time with the atoms when you look at the right (conditional) subset of events.

If you want the numbers from their specific pulses, the optical depth values, or how they separate the leading/trailing contributions in the data, let me know.

</div>

<div>

more explanation of The front of the transmitted pulse is weakened (more absorption).

- The back of the transmitted pulse is strengthened (constructive interference from re-emitted light).
- When you look at the overall shape of the pulse that comes out, its highest point (the peak) is now earlier in time than the original peak would have been.

</div>

<div>

Thought for 4s

**More explanation of the pulse reshaping that causes the peak to arrive earlier:**

A light pulse is a short burst made of many closely spaced frequencies centered around the main frequency you tune to. Near the atomic resonance frequency, the atoms absorb and shift the phase of these frequencies very differently depending on whether they are slightly below, at, or slightly above the exact resonance.

### Why the front of the transmitted pulse is weakened (more absorption)

The very earliest part of the incoming pulse contains a broader mix of frequencies, but the strongest absorption occurs right at the center resonance frequency.

When the leading edge hits the atoms:

- A larger fraction of its light is absorbed because those frequencies sit where the atomic absorption is highest.
- Fewer photons from the leading edge make it straight through without interacting.
- The atoms that absorbed this light become excited for a short time.

Result: the front part of the pulse that exits the cloud is noticeably weaker than the original front.

### Why the back of the transmitted pulse is strengthened (constructive interference from re-emitted light)

The atoms that absorbed light from the leading edge do not stay excited forever. They quickly re-emit the energy as light (spontaneous or stimulated emission in the forward direction).

Near resonance, this re-emitted light has exactly the right phase to add constructively with the part of the original pulse that is still arriving (the middle and trailing portions).

- The later-arriving frequencies experience less net absorption or even gain from this re-emitted light.
- The interference is constructive specifically in the forward direction (the direction the pulse is traveling).
- The back half of the transmitted pulse therefore ends up stronger than it would have been without the atoms.

### How this moves the peak earlier

- Original pulse (before atoms): symmetric shape with the highest point in the middle.
- After atoms: front is reduced (more absorbed), back is boosted (constructive re-emission + interference).
- The highest point of the new shape is now shifted toward the earlier part of the pulse.

The entire transmitted pulse envelope therefore reaches its maximum intensity sooner than the original pulse would have. This forward shift of the peak is the negative group delay. The amount of the shift matches the calculated τ_g = ∂ϕ/∂ω from the frequency-dependent phase the atoms apply.

In the experiment they measure this effect indirectly through the atoms: the weak probe laser records how much excitation was present at each moment, post-selecting only on shots where a signal photon got through. The integrated excitation they see for those transmitted photons is negative and exactly matches the forward shift of the pulse peak.

The key point is that the reshaping is caused by real absorption and re-emission cycles in the atoms, not magic. The early part of the pulse "pays" by exciting the atoms, which then "repay" by boosting the later part through coherent forward scattering. When you condition on the photons that made it all the way through, the net atomic excitation time comes out negative.

This process happens on the scale of the atomic lifetime (\~26 ns for the rubidium D2 line) and the pulse durations they used (10--36 ns rms). Let me know if you want the quantitative numbers from their different pulse widths and optical depths or how the probe actually detects the excitation at each time step.

</div>

<div>

how is shifting the peak forward interpreted as negative time. is it because it appears that the pulse is futher ahead than it would be w/o the absorption/emission.

</div>

<div>

Thought for 3s

**Yes --- that\'s exactly right.**

The **negative group delay** (negative time) simply means the peak of the transmitted pulse comes out of the cloud *earlier* than the same pulse would have if it had traveled the same distance through empty space (vacuum).

### How they define and interpret the time

They compare two things:

1.  **Expected arrival time in vacuum** If there were no atoms, the pulse peak would arrive at a certain time t₀ after traveling the length of the cloud.
2.  **Actual arrival time of the peak after the cloud** With the atoms present, the peak arrives at time t_peak, where t_peak \< t₀ (earlier).

The group delay is the difference:\
τ_g = t_peak − t₀

When t_peak is earlier, τ_g is **negative**. That is the "negative time."

### Why this is called "negative time" for the pulse

- A positive group delay means the peak is delayed (later than vacuum).
- A negative group delay means the peak is advanced (earlier than vacuum).

The experiment shows that this same number (the negative τ_g) also equals the weak-valued time the atoms spent excited *for the photons that got through*. So the atoms appear (in the conditional average) to have been excited for a negative duration when you look only at transmitted photons.

### Physical picture (absorption + re-emission)

- The leading edge of the pulse is absorbed more strongly.
- The atoms re-emit that energy in the forward direction with the right phase to boost the trailing part of the pulse.
- Net result: the front is weaker, the back is stronger → the highest point (peak) of the whole pulse moves forward in time.

The pulse as a whole did not travel faster than light. The very first detectable light (the absolute leading edge) still arrives at or after the vacuum speed. Only the *peak intensity* has shifted earlier because of how the absorption and re-emission reshaped the pulse.

In the paper they confirm this reshaping is real by measuring the atoms directly: the integrated excitation they record (via the probe phase shift, post-selected on transmission) gives exactly the same negative number as the calculated group delay. That is why they say the negative group delay has genuine physical meaning --- it matches the actual (weak-valued) interaction time with the atoms.

If you want the numbers from their specific pulses (how negative it got for different widths and optical depths) or a sketch of the pulse shapes before/after the cloud, just ask.

</div>

<div>

how is the earlier peak interpreted as \"negative time\" need further details on how this is calcuated, and why negative time. I would think because the peak is earlier, it meant light was traveling faster than in vacuum, i.e. faster. How is that quantified as negative time. I would think of this faster than C to be positive, not negative.

</div>

<div>

Thought for 3s

**Why an earlier peak is called \"negative time\" (group delay)**

The sign convention is defined relative to vacuum propagation.

### Basic definition and sign

They define the **group delay τ_g** as the extra time the pulse peak takes to get through the cloud compared with the same distance in vacuum:

τ_g = (arrival time of peak with atoms) − (arrival time of peak in vacuum)

- If the peak arrives **later** than in vacuum → τ_g is **positive** (normal delay / slow light).
- If the peak arrives **earlier** than in vacuum → τ_g is **negative** (advance / apparent fast light).

This is the standard convention in optics. \"Negative group delay\" simply means the peak comes out sooner than expected. It does **not** mean the light itself traveled faster than c overall.

### How they calculate it

1.  They know the exact length of the atom cloud.
2.  They calculate (or measure) what time the pulse peak would arrive if the cloud were empty (vacuum time t_vacuum).
3.  They measure the actual arrival time of the peak after it has passed through the atoms (t_peak).
4.  τ_g = t_peak − t_vacuum

When t_peak \< t_vacuum, τ_g comes out negative.

They can also compute it from the phase the atoms add to the light:

τg=∂ϕ∂ω \\tau_g = \\frac{\\partial \\phi}{\\partial \\omega} τg​=∂ω∂ϕ​

where ϕ is the phase shift added by the atoms and ω is angular frequency. Near resonance the phase slope ∂ϕ/∂ω is negative, so τ_g is negative.

### Why the peak arrives earlier (the reshaping)

- The leading edge of the pulse is absorbed more (higher absorption near resonance).
- Atoms re-emit that energy forward with the correct phase.
- This re-emitted light interferes constructively with the trailing part of the pulse.
- Result: front of transmitted pulse is weaker, back is stronger → the highest point (peak) of the whole shape moves to an earlier time.

The absolute leading edge of the pulse (the very first tiny bit that carries new information) still arrives at or after the vacuum speed. Only the peak and the bulk of the energy are shifted forward by the reshaping. No information or energy travels faster than c.

### Why \"negative\" feels counter-intuitive

You are thinking \"earlier arrival = faster = should be positive.\"\
In the optics convention, positive delay means \"takes extra time\" (delayed). So earlier = negative delay. It is just the sign convention used in the field --- the same one used for slow-light (positive) and fast-light (negative) effects. The paper uses this standard definition, then shows the measured atomic excitation time (weak value) equals this τ_g, including when it is negative.

In their data: for the narrowest (most resonant) pulses they get τ_T / τ_0 ≈ −0.82 ± 0.31, where the negative sign means the effective excitation time is in the same direction as the negative group delay (peak advanced by that amount).

**Bottom line:**\
Negative group delay = peak comes out earlier than vacuum expectation.\
The experiment proves the atoms\' conditional excitation time matches this same negative number. It is not faster-than-light travel; it is pulse reshaping caused by absorption + coherent re-emission.

If you want the exact formula they use for τ_g from the phase, the pulse parameters that gave the most negative value, or a step-by-step calculation example from their numbers, tell me.

</div>

<div>

OK, finally understand. Didn\'t really understand what negative time was (increase in \"speed\" of light). Seems backwards to me, but that\'s because I don\'t have a lot of knowledge about optisc. Where was the \"negative time\" first used an why

</div>

<div>

Thought for 9s

**Where \"negative time\" (negative group delay) first appeared and why**

The underlying idea of negative group delay goes back to the early 20th century.

**Early theoretical roots (1910s--1960s):**\
Physicists like Léon Brillouin and Arnold Sommerfeld studied how light pulses behave in dispersive media (materials where speed depends on frequency). They showed mathematically that in regions of **anomalous dispersion** (near absorption lines, like the atomic resonance in your paper), the group velocity (speed of the pulse peak) can exceed *c* or even appear negative. They already understood this did not violate relativity --- the pulse front (leading edge) never exceeds *c*, and information cannot be sent faster than light. It was mostly a theoretical curiosity at the time.

**Modern use in optics and electronics (1980s--1990s onward):**\
The term \"negative group delay\" became common in papers on fast-light and superluminal propagation effects. Key early experiments and theory came from researchers like Raymond Chiao, Aephraim Steinberg, and others in the 1990s. They demonstrated negative group delay in optical systems and showed it was real but harmless (pulse reshaping, not true superluminal signaling). Electronic circuits that produce negative group delay were also built around the same time as simple demonstrations.

**In the context of photons and atoms (this paper and its predecessors):**\
The specific phrase \"negative time\" for the time a photon spends as an atomic excitation is much more recent. It comes directly from the work of the Steinberg group at the University of Toronto.

- Their 2022 paper (Sinclair et al.) measured positive excitation times for transmitted photons.
- Theory (involving Howard Wiseman and others) predicted that the weak-valued excitation time should equal the group delay --- including when it is negative.
- The 2024/2026 paper you are reading (Angulo et al.) is the first experimental confirmation of the negative case using weak measurements.

They use \"negative time\" because the weak-valued atomic excitation time τ_T comes out negative, matching the negative group delay τ_g. It is the natural language for \"the conditional average is in the opposite direction from a normal positive delay.\"

**Why the sign feels backwards to you**\
You are thinking \"earlier arrival = faster = should be positive.\" In standard optics convention:

- Positive group delay = pulse peak delayed (takes extra time).
- Negative group delay = pulse peak advanced (comes out sooner).

The sign is chosen so that τ_g directly tells you the time shift relative to vacuum: positive = later, negative = earlier. It is just the agreed-upon definition in the field (same as in slow-light and fast-light literature). The physics is the same regardless of the label.

The \"negative time\" here is not the light traveling faster than *c* overall. It is the pulse peak appearing earlier due to absorption of the front and coherent re-emission boosting the back. The experiment shows this effect corresponds to a real (weak-valued) negative excitation time for the transmitted photons.

This concept is now used because it cleanly links the classical wave description (group delay) to the quantum description (what the atoms actually do for the photons that get through).

If you want references to the earliest papers or more on how they calculate the exact value in their setup, let me know.

![](Experimental Observation of Negative Weak Values for the Time/Pictures/10000000000000B4000000B45C26995F.png){width="1.8752in" height="1.8752in"}

![](Experimental Observation of Negative Weak Values for the Time/Pictures/10000001000000B4000000B455B24077.png){width="1.8752in" height="1.8752in"}

![](Experimental Observation of Negative Weak Values for the Time/Pictures/100000000000003000000030183F36A0.png){width="0.5in" height="0.5in"}

25 sources

</div>

<div>

undstand about exceeding C, what does appear negative really represent, I really want to know why, now that I know the conventaion: the group velocity (speed of the pulse peak) can exceed c or even appear negative.

</div>

<div>

Thought for 4s

**Group velocity exceeding ***c*** or appearing negative --- what it really means and why it happens**

You now understand the sign convention (negative = peak arrives earlier). Here is the deeper physical reason it can happen without violating relativity.

### Group velocity vs. signal velocity

- **Group velocity (v_g)**: Speed of the *peak* (or envelope) of a pulse.
- **Signal / information velocity**: Speed at which actual new information or a sudden change can propagate. This is always ≤ *c*.

In normal transparent media, v_g ≈ *c*/n (slightly slower than *c*). Near an absorption resonance, things change.

### Why group velocity can exceed *c* or become negative

Near the atomic resonance frequency:

- The refractive index *n* changes very rapidly with frequency (large anomalous dispersion: dn/dω is strongly negative).
- The full formula for group index is n_g = n + ω (dn/dω).
- When dn/dω is large and negative, n_g can drop below 1 or even become negative.

Result:

- v_g = c / n_g can become \> *c* (superluminal group velocity) or negative.

A negative v_g means the peak moves backward in some mathematical sense, but in practice it shows up as the peak advancing forward in time.

### What \"appears\" really represents (the reshaping picture)

The incoming pulse has a smooth rising front, peak, and falling back.

- Frequencies in the **leading front** are absorbed more strongly (they sit closer to the exact resonance where absorption peaks).

- Atoms absorb energy from the front and re-emit it almost immediately in the forward direction with the correct phase.

- This re-emitted light interferes constructively with the **trailing part** of the original pulse.

- Net effect on the transmitted pulse:

  - Front is depleted (more absorbed).
  - Back is amplified (constructive interference).
  - The highest point (peak) of the reshaped pulse is therefore located earlier in time than the original peak position.

The pulse envelope as a whole has its maximum shifted forward. That forward shift is the negative group delay / negative time.

### Why this does not exceed *c* or break causality

- The absolute leading edge of the pulse (the very first tiny rise that could carry new information) is not advanced. It still arrives at or after the vacuum light-speed time.
- You cannot detect the peak before the front arrives. Any attempt to send a signal requires a sharp change on that front, which propagates normally.
- The \"advanced\" peak is formed from information already present in the incoming pulse + the atoms\' response. The atoms are essentially predicting/reshaping the expected continuation of the smooth pulse.

In short: the group velocity describes how the peak moves due to dispersion and interference, but it is not the speed of information or energy transport. The experiment in the paper shows that this reshaping effect corresponds exactly to a measurable negative weak-valued excitation time in the atoms for the transmitted photons.

This is why physicists say the group velocity \"can exceed *c* or appear negative\" --- it is a real, observable effect on the pulse shape, but it never lets you send information faster than light. The paper\'s contribution is showing that the atomic side (the excitation time) matches this description even when the number is negative.

If you want the mathematical derivation of n_g or how they compute τ_g from their phase data, I can walk through that too.

</div>

<div>

OK, I guess i understand, the \"appears negative\" makes more sense , arriving ealier means \> 3. Key is \"appears\"

</div>

<div>

Thought for 4s

**Yes --- you got the key point.**

The word **\"appears\"** is crucial.

The pulse peak *appears* to arrive earlier (negative group delay / negative time), but:

- No information or energy actually travels faster than *c*.
- The absolute front of the pulse still respects the speed of light.
- The peak shift is caused by the atoms absorbing the front and coherently re-emitting light that reinforces the back --- pure reshaping of an already-formed pulse.

In the experiment, the weak measurement on the atoms confirms that this apparent negative time is real on the atomic side too (for the transmitted photons).

That's the whole story in simple terms. The convention just labels the forward shift of the peak as "negative" because positive means delayed.

Glad it clicked! If anything else in the paper (or the weak-value part) is still fuzzy, or you want numbers/figures from their data, just ask.

</div>

<div>

now I have to get back to reading the original paper. :-) What a rabbit hole. :-)

</div>

<div>

Thought for 5s

**Glad it clicked!** 😊

It really is a fascinating rabbit hole --- the paper does a nice job connecting the classical pulse reshaping (group delay) to the quantum side (weak-valued atomic excitation time).

If you hit any other confusing sections while reading (specific figures, equations, the cross-Kerr details, error analysis, or anything else), just paste the part or describe it and I'll walk through it with you --- simple or as detailed as you like.

Enjoy the rest of the paper! Let me know how it goes or if you want context on the earlier Sinclair work or the theory papers they cite.

</div>

<div>

This sums it yp for me: Coherent forward scattering lets transmitted photons borrow excitation "time" from the ensemble interference, advancing the pulse without violating causality.

</div>

<div>

Thought for 3s

**Yes --- that\'s a clean one-sentence summary of the whole result.**

The transmitted photons effectively "borrow" excitation time from the collective interference of the atomic ensemble (coherent forward scattering). The front of the pulse excites the atoms, which then re-radiate in phase to boost the back of the pulse. Net effect: the peak advances (negative group delay), and the weak measurement shows the conditional atomic excitation time is correspondingly negative.

Everything stays causal because the true information-carrying front of the pulse isn't advanced.

If that framing works for you while reading the paper, great. The authors emphasize exactly this point in the discussion --- the negative time isn't an illusion; it's a real conditional effect tied to how the transmitted amplitude is built.

Enjoy the rest of the read! If you want a quick map of which sections cover what (intro, theory, experiment, discussion), or clarification on any figure/equation, I'm here.

</div>

<div>

Why is humidity light from the added scatter the momentum of the absorbed photon should momentum of the emitt

</div>

<div>

Thoughts

Request was interrupted by the user.

Interrupted

</div>

<div>

Let me try again. Why is the light emitted by the atoms scattered forward. The momentum from the ab shouldn\'t affect the momentum of the emitted photon, should it?

</div>

<div>

Thought for 30s

**The emitted light in coherent forward scattering has (essentially) the same momentum as the absorbed photon --- and yes, that is required by momentum conservation for the transmitted component.**

Here is the straightforward physics, step by step:

### 1. What happens on absorption

A photon with wavevector **k** (momentum ħk, pointing in the propagation direction) is absorbed by an atom (or, collectively, by the ensemble).\
The atom gains recoil momentum +ħk.\
This temporarily excites the atom (or creates a collective excitation with wavevector k in the cloud).

### 2. What happens on re-emission

The atom (or collective state) later de-excites and emits a photon.\
The emitted photon carries momentum ħk\' in whatever direction it is emitted.\
The atom receives recoil −ħk\'.

- If the photon is emitted in a **random direction** (ordinary spontaneous emission), k\' is random → net momentum left on the atom is ħk − ħk\' (usually nonzero). This corresponds to real absorption/scattering loss --- the photon is removed from the forward beam.
- If the photon is emitted **in the exact forward direction** with the **same wavevector k** (same direction and wavelength), then k\' ≈ k → net momentum transfer to the atom ≈ 0.

### 3. Why forward direction is special in an ensemble (coherent scattering)

In a cloud of many atoms driven by a plane-wave laser (or weak pulse), the atoms are all driven in phase by the same incoming field.\
The radiated field from each atom interferes with the others.\
Constructive interference occurs strongly in the **forward direction** (the direction of the original k). This is the coherent forward-scattered amplitude.

It is not ordinary random spontaneous emission. It is the coherent, driven response of the atomic dipoles (the real part of the susceptibility).\
This forward-scattered wave has the **same frequency, phase progression, and wavevector k** as the original photon.\
It therefore carries away essentially the same momentum ħk that was absorbed.

### 4. Momentum conservation for the "transmitted" photon

For the component of light that is transmitted (the part you post-select on in the experiment):

- Photon comes in with momentum ħk.
- Atom(s) temporarily gain +ħk.
- Atom(s) re-emit forward with momentum ħk.
- Atom(s) receive −ħk.

**Net result for that photon path**: the outgoing photon still has momentum ħk (same as incoming). The atoms end up with net zero recoil for that cycle. The photon continues forward as if it "passed through," but it experienced a temporary interaction that modified the phase and the pulse shape (the group delay / negative time effect).

The random-direction spontaneous emission is the part that corresponds to actual absorption (the imaginary part of the index of refraction) --- those photons are scattered out of the beam and do not contribute to the transmitted signal you detect.

### 5. Why this produces the observed group delay (including negative)

The temporary excitation and coherent re-radiation forward is exactly what reshapes the pulse envelope.\
The leading part of the pulse excites the atoms more; the re-radiated field adds constructively to the trailing part.\
This moves the peak of the transmitted pulse earlier in time relative to vacuum propagation → negative group delay.\
The weak measurement (probe phase shift post-selected on transmission) directly reads out that the average time the atoms spent excited, for those transmitted photons, equals this group delay --- including when it is negative.

The momentum of the absorbed photon **does** affect the atom temporarily (recoil), but because the re-emission is coherent and forward-directed with the same k, the recoil is canceled. The emitted photon therefore has the same momentum as the absorbed one. That is why the transmitted photon can continue with essentially unchanged momentum while still having interacted with the atoms long enough to produce the measured (negative) excitation time.

This is standard in the theory of resonant light propagation through dilute media and is the mechanism underlying the results in the Angulo et al. paper (and the earlier Sinclair et al. work). The collective nature of the cloud makes the forward direction dominant for the coherent part of the scattering.

If you want the relevant equations (absorption → recoil ħk, emission → −ħk\', net zero for k\' = k) or how this appears in the optical theorem / forward scattering amplitude, or anything specific from the paper's discussion section, just say.

![](Experimental Observation of Negative Weak Values for the Time/Pictures/1000000100000100000001008A5AFDEA.png){width="2.6665in" height="2.6665in"}

![](Experimental Observation of Negative Weak Values for the Time/Pictures/10000000000000C0000000C034A1DC67.jpg){width="2in" height="2in"}

![](Experimental Observation of Negative Weak Values for the Time/Pictures/100000010000003000000030168CD786.png){width="0.5in" height="0.5in"}

10 sources

</div>

<div>

Okay that makes sense. However, the photons on the edge, the front edge of the wave of the pulse get ab its humid photon goes forward. However, there\'s a small delay. So the the the emitted photon actually shifts the peak back. It seems in my mind not shipping it forward. I mean the emitted light can\'t be any faster or get the front of the ratio in the front because there can\'t be more photons admitt

</div>

<div>

Thought for 23s

**Yes --- this is the most counter-intuitive part, and your intuition is exactly where most people get stuck at first.** The re-emission *does* have a small delay (tied to the atomic response time / lifetime), yet the net effect in the negative-group-delay regime is that the **peak of the transmitted pulse moves forward** (earlier), not backward. Here is why, step by step, without analogies.

### 1. The incoming pulse has a leading edge, peak, and trailing edge

- The **leading edge** (front) contains the earliest-arriving light.
- Absorption is strongest near the atomic resonance frequency.
- For a pulse whose spectrum overlaps the resonance, the **leading edge is absorbed more strongly** than the middle or trailing parts. More photons from the front are removed from the beam (they excite atoms).

### 2. What happens to the absorbed energy

The atoms that absorbed light from the leading edge become excited. After a short time (the response time of the driven atoms), they de-excite and radiate light forward (coherent forward scattering for the transmitted component).

This re-radiated field is **not** added randomly or all at once at the very front. It appears with the natural phase and timing of the atomic response and interferes with the **still-arriving parts of the original pulse** (the middle-to-trailing portions).

### 3. Why the peak moves *forward* (earlier) instead of backward

- Because more light was removed from the **leading edge**, that part of the transmitted pulse is weakened.

- The re-radiated light adds constructively to the **trailing part** of the pulse (the phase relationships near resonance make the addition boost the back end).

- Result on the overall shape of the transmitted pulse:

  - Front weakened (more absorption).
  - Back strengthened (re-radiation + interference).
  - The location of the **highest intensity (the peak)** therefore shifts toward earlier times compared with what the peak would have done in vacuum.

The re-emitted light does **not** race ahead to create new intensity before the original front. The absolute leading edge of the pulse is still attenuated or unchanged in its earliest detectable part. The reshaping simply removes relatively more from the front and adds relatively more to the back → the maximum of the envelope moves earlier.

### 4. The "small delay" in re-emission does not push the peak later

The atomic response time is already included in the frequency-dependent phase shift that produces the group delay. In the regime where group delay is negative:

- The differential absorption (stronger on the front) dominates the timing.
- The re-radiation arrives at the right phase to reinforce the trailing field rather than lag behind and broaden or delay the peak.
- Net mathematical result (from the derivative of the phase with frequency): the envelope peak advances.

In frequency-domain language: near resonance the phase slope ∂ϕ/∂ω is negative for the relevant pulse bandwidths and optical depths → group delay τ_g is negative → peak arrives earlier.

In the experiment, when you post-select only on the photons that made it through (transmitted), the weak measurement of the integrated atomic excitation exactly equals this (negative) group delay. The temporary excitation and coherent re-radiation forward are what produce both the pulse-peak advancement and the measured negative excitation time.

### 5. No extra photons appear "earlier" or faster

- The re-emitted light travels at the same speed as everything else.
- Total energy in the coherently transmitted component is conserved in the reshaping (no net loss for the post-selected transmitted photons).
- Photons are effectively redistributed in time: some that would have been in the front are absorbed and reappear (via re-radiation) later in the pulse envelope. This depletes the front more than the back and shifts the peak earlier.

The paper notes that for broadband pulses through an optically thick cloud, the pulse envelope picks up a π phase flip associated with coherent forward emission; this phase flip is part of the reshaping that lets the peak emerge earlier.

This is why the measured atomic excitation time for transmitted photons can be negative and still match the group delay: the "interaction time" (temporary excitation) produces exactly the observed advancement of the peak via the absorption + coherent forward re-radiation mechanism.

If this still feels backwards in your mental picture of the pulse envelope, the cleanest way to see it is to sketch (or imagine) the input pulse shape, subtract more from the leading edge, then add a delayed but phase-matched contribution to the trailing edge --- the resulting maximum moves left (earlier). The math of the transfer function through the medium confirms it.

Would you like the specific numbers from their pulses (how negative it got for narrow vs broad pulses) or a pointer to the part of the paper that discusses the phase flip / reshaping? Or anything else that's still fuzzy?

</div>

<div>

So the emitted light which constructively interferes with light in the pulse occ than the norm without any expected expected peak there for because of the extra energy from the photons that are admitted, then there\'s a higher number of photons farther forward in the pulse which shift the pulse forward

</div>

<div>

Thought for 13s

**Almost --- but the direction of the addition is the key detail that flips the intuition.**

The re-emitted light (via coherent forward scattering) **adds constructively to the trailing part of the pulse**, not to an earlier part.

Here is the precise sequence:

1.  **Leading edge of the incoming pulse** Absorption is strongest here (frequencies closest to resonance). More photons from the front are removed from the beam. The front of the *transmitted* pulse is therefore weakened compared with the input.

2.  **Atoms that absorbed from the leading edge** They become excited and, after their response time, re-radiate forward coherently. This re-radiated field has the right phase to interfere **constructively with the still-arriving middle-to-trailing portions** of the original pulse.

3.  **Net effect on the transmitted pulse envelope**

    - Front: depleted (more absorption).
    - Back: boosted (re-radiation + constructive interference).
    - The location of the **maximum intensity (the peak)** therefore moves earlier in time than it would have in vacuum.

The re-emitted light does **not** create extra photons "farther forward" or ahead of the normal position. It adds energy where the pulse field is already present later in the envelope. The front has simply been attenuated more than the back, so the highest point of what remains occurs earlier.

### Why this produces negative group delay / negative excitation time

- The differential absorption (stronger on the leading edge) + coherent re-radiation on the trailing edge is exactly the reshaping that advances the peak.
- In the frequency domain this corresponds to a negative slope in the spectral phase (∂ϕ/∂ω \< 0) for the relevant pulse bandwidths → τ_g \< 0.
- When the experiment post-selects only on photons that made it through the cloud (transmitted), the weak measurement of the integrated atomic excitation time τ_T equals this same (negative) group delay. The temporary excitation and coherent forward re-radiation are what link the two.

The "extra energy" in the trailing part comes from photons that were absorbed earlier in the pulse and re-radiated later. It is not new photons appearing ahead of schedule. The absolute earliest detectable part of the pulse front is not advanced; only the peak of the reshaped envelope moves earlier relative to vacuum.

This is the mechanism the paper connects to the measured negative weak-valued atomic excitation time. The coherent forward scattering (and the associated π phase flip for broadband pulses through optically thick media) produces exactly this forward shift of the peak while preserving causality for information.

If you sketch the input pulse, subtract a bit more from the leading edge, then add a phase-matched contribution to the trailing edge, the resulting maximum clearly shifts left (earlier). That is what the atoms do for the transmitted component.

Does this resolve the remaining mental picture, or is there still a specific part (e.g., where the re-emitted photons "appear" in time, or how the post-selection selects only the coherent transmitted part) that feels off?

</div>

<div>

I would think that if the back part of the phase was increased so the peak in the batter lad is be I think I just can\'t understand something about it. How does that shift the peak forward? I would think it would shift the peak backwards because there\'s a delay in the emitted radiation which then constructively increases. The the peak further back than it would have without the abs or the emitted radiation being constructively

</div>

<div>

Thought for 12s

**The key point you are missing is the ***asymmetric*** change: the front is lowered ***more*** than the back is raised.**

Here is exactly what happens to the pulse envelope in the negative-group-delay regime:

### Input pulse (no atoms)

- Roughly symmetric shape.
- Peak (maximum intensity) at some central time t₀.

### After the atom cloud (transmitted component)

1.  **Leading edge (front)** Absorption is strongest for the frequencies closest to resonance. More photons are removed from the front of the pulse than from the middle or back. → The left side of the transmitted envelope drops significantly.
2.  **Trailing edge (back)** The atoms that absorbed from the front re-radiate coherently forward after their response time. This re-radiated field interferes constructively with the still-arriving middle-to-back part of the original pulse. → The right side of the transmitted envelope is boosted (higher than it would have been without the re-radiation).

### Net shape of the transmitted pulse

- Left side (front) lowered a lot.
- Right side (back) raised some.
- The **location of the highest point** (the peak) therefore moves to an *earlier* time than t₀.

The re-emission delay does add intensity later in the pulse, but because the front has been lowered *more*, the place where intensity reaches its maximum occurs earlier on the time axis. The boost on the back does not "push the peak backward"; it reinforces the leftward movement of the maximum caused by the greater depletion of the front.

### Why the delay in re-emission does not make the peak later overall

The atomic response time is already included in the frequency-dependent phase shift that defines the group delay. In the regime where that phase slope is negative:

- The differential absorption (stronger on the leading edge) dominates the timing.
- The re-radiation arrives at precisely the phase needed to add to the trailing field rather than lag behind and shift everything later.
- The net result on the envelope is advancement of the peak (negative τ_g).

In the experiment, when only the transmitted photons are kept (post-selection), the weak measurement of the total time the atoms spent excited equals this same negative group delay. The temporary excitation + coherent forward re-radiation produces both the observed pulse-peak advancement and the measured negative excitation time.

The re-emitted light does not create new intensity ahead of the original front, nor does it simply add a delayed bump far back that moves the maximum later. It modifies the existing envelope asymmetrically (more removal from front, addition to back), so the maximum occurs earlier.

This is the reshaping the paper links to coherent forward scattering (including the π phase flip for broadband pulses in optically thick media). The transmitted photons experience exactly this effective interaction time, which can be negative.

If you picture the input envelope and then lower the left side more than you raise the right side, the highest point clearly moves left (earlier). That is what the atoms do for the photons that make it through.

Does this now resolve where the peak moves? Or is there still one specific mental image (e.g., exactly when/where the re-radiated field adds intensity relative to the depleted front) that feels off?

</div>

<div>

Okay, the forward part of the light pul get then the emitted photons in the four direction constructively interfere with the the photons from the original light w light pulse and that\'s occ peak would have appeared so I\'m still confused. I don\'t know if I can figure this

</div>

<div>

Thought for 15s

**Got it --- this is the exact sticking point for almost everyone.** Let's walk through the *timing* of what happens to the different parts of the pulse, very explicitly.

### Timeline for one pulse (leading edge → peak → trailing edge)

**Early times (leading/front edge of the pulse arrives at the cloud):**

- These photons are absorbed most strongly (frequencies closest to resonance).
- Many are removed from the beam → transmitted intensity at these early times is **lowered a lot**.
- Atoms become excited.

**Slightly later times (middle of the pulse is arriving):**

- Some of the atoms excited by the leading edge start to re-radiate coherently forward.
- This re-radiated field interferes with the middle part of the *still-arriving original pulse*.
- The interference is constructive in the forward direction.

**Even later times (trailing/back edge of the pulse arrives):**

- More re-radiation from earlier absorption events adds here.
- Absorption is weaker on these later-arriving frequencies.
- Transmitted intensity at these late times is **higher** than it would have been without the re-radiation (boosted by the added field).

### Result on the transmitted pulse shape

- At the very front (early times): intensity much lower than input.
- At the back (late times): intensity higher than it would have been.
- The **time at which the intensity reaches its maximum** therefore occurs *earlier* than in the original pulse (or than in vacuum).

The re-emitted light does **not** mainly interfere right at the original peak position in a way that keeps the peak there. It adds to times *after* the leading-edge absorption events. Because the earliest times have been suppressed more, the highest point of the whole transmitted envelope slides earlier on the time axis.

### Why the delay in re-emission does not push the peak later

The re-emission *does* have a delay (the atomic response time). That delay means the added intensity appears at later times in the pulse.\
But the absorption removed *even more* intensity from the *earliest* times.\
The combination --- big drop at early t, smaller rise at late t --- moves the location of the maximum to an earlier t.

It is not that the re-emitted photons "create a new peak farther back." It is that the front is eaten away more than the back is built up, so whatever is left has its highest point earlier.

This is exactly the reshaping that produces negative group delay (peak arrives earlier than in vacuum). When the experiment keeps only the photons that made it all the way through (post-selection on transmission), the weak measurement shows the atoms were excited for a time that exactly equals this negative group delay.

The coherent forward re-radiation (the part that interferes constructively) is what links the temporary atomic excitation to the observed advancement of the transmitted peak.

If you still feel the addition "should" keep the peak where the original one was, the missing piece is the *greater removal from the front*. Once the front is lowered more than the back is raised, the max has to move left (earlier).

Does this version of the timing make the direction of the shift clearer, or is there still one specific moment (e.g., exactly relative to where the original peak would have been) that doesn't click? I can zoom in on that.

</div>

<div>

Okay, let me try this now okay, so the admitted photons are emitted to the right hand side of the peak before the maximum of the peak. Therefore they construct with the original photons on the right hand side of is high lower than the new peak and the new peak is on the right hand side compared to the old peak

</div>

<div>

Thought for 14s

**You\'re very close --- the addition is on the right (later times), but that does ***not*** make the new peak move right. The greater drop on the left pulls the maximum ***left*** (earlier).**

Let's use your picture and correct the conclusion.

### What actually happens to the envelope

- **Left side (early times / front of pulse)**: Strong absorption removes a lot of intensity. This side drops significantly.
- **Right side (later times / back of pulse)**: Re-emitted light (after the short atomic response delay) adds constructively here. This side rises.

The re-emitted photons **do** interfere with the original pulse photons on the right-hand side of where the old peak was. That raises the intensity on the right.

### Why the peak still moves *left* (earlier / forward in time)

Even though you raise the right side, you have lowered the left side *more*.

Imagine the intensity curve:

- Original peak at time = 0.
- You subtract a larger amount from all times \< 0 (front).
- You add a smaller amount to times \> 0 (back).

The highest point of the new curve is now at some time \< 0 (earlier than the original peak).

The boost on the right raises that side, but it does not outweigh the bigger drop on the left. The place where the curve reaches its maximum therefore occurs earlier.

The new peak is **not** on the right-hand side compared with the old peak. It is on the left-hand side (earlier time).

### The re-emission timing

The emitted photons are added after the absorption events from the leading edge. That means they contribute to times *later* than the earliest absorption. They raise the right side of the envelope (as you said).

But because the very front has been suppressed more, the overall maximum of the transmitted pulse envelope moves earlier. The delay in re-emission is already built into the atomic response; it does not add an *extra* lag that pushes the peak backward. The net envelope peak advances (negative group delay).

This is the reshaping measured in the experiment: when you keep only the transmitted photons, the weak-value atomic excitation time equals the group delay --- which can be negative precisely because of this front-depletion + back-boost effect.

The re-emitted light does **not** create extra photons ahead of the original front or move the maximum later. It modifies the shape asymmetrically (bigger loss on left, gain on right), so the highest point occurs earlier.

If you now picture the original peak at time 0, lower the left side more, raise the right side less, the new highest point is clearly at a negative time (earlier). That is the forward shift of the peak.

Does this match what you were picturing, or is there still one detail (e.g., exactly how much the front drops vs. how much the back rises, or relative to the original peak position) that feels off? I can zoom in on that part.

</div>

<div>

Wait so the way I think of the pul is that there\'s photons on the amount of photons on the y-axis? The x-axis is time so what happens is the original earliest photons are on the right side of the pulse and the later photons later on in the pulse are on the left hand side. You\'re telling me just the opposite? I thought the the Chie looking at the the gra and the y-axis is the intensity of photons. Then the very first photons arriving are arriving on the front of the pul pulse and then the pulse moves to the right from a given time and that means that the the peak increases and then pass the peak it goes the in down and that\'s the left

</div>

<div>

Thought for 10s

**Yes --- you have the left/right of the time axis reversed in the plot. That is the source of the remaining confusion.**

### Standard plot of the pulse (what everyone uses)

- **X-axis (horizontal)**: **time**, increasing from **left to right**.

  - **Left side of the plot** = **early times** = **front / leading edge** of the pulse (the very first photons to arrive).
  - **Right side of the plot** = **later times** = **back / trailing edge** of the pulse (the last photons to arrive).

- **Y-axis (vertical)**: intensity (number of photons arriving per unit time, or electric-field amplitude squared).

The pulse envelope is a hump on this plot.\
The front of the pulse is the **left** rising edge.\
The peak is somewhere in the middle.\
The back of the pulse is the **right** falling edge.

(When we say the pulse "moves to the right" we are talking about its propagation through space. On a fixed detector's time plot the front simply appears first --- on the left.)

### What the atoms do to this plot (negative group delay case)

- **Left side (early times / front)**: stronger absorption → intensity on the left side of the plot is lowered a lot.
- **Right side (later times / back)**: re-radiation adds constructively here → intensity on the right side of the plot is raised.

Result on the hump:

- Left side drops significantly.
- Right side rises some.
- The **highest point of the hump** therefore moves **leftward** on the plot (to an earlier time).

That leftward movement of the maximum is the **forward shift of the peak** (negative group delay). The peak now occurs at a smaller time value than it did in vacuum.

### Why boosting the right side does **not** move the peak rightward

Raising the right side does increase intensity at later times.\
But because the left side was lowered *more*, the place where the curve reaches its absolute maximum still occurs earlier (further left on the plot).

The greater drop on the left dominates the location of the peak. The addition on the right raises the trailing edge but does not outweigh the bigger suppression on the leading edge, so the maximum slides left (earlier).

### Quick check with your description

You said the earliest photons are on the right and later photons on the left --- that is the opposite of the standard plot. Once you flip it (earliest = left, latest = right), the mechanism becomes: lower the left more, raise the right some → maximum moves left (earlier time) = peak advances = negative group delay.

This is exactly the reshaping that the weak measurement reads out as a negative atomic excitation time for the transmitted photons.

Does the corrected left = front / early times now make the direction of the peak shift clear? Or is there still one piece (e.g., how the re-radiation timing lines up with "right of the original peak position") that doesn't feel right?

</div>

<div>

Okay now tell me why the earliest part of the pulse is on the left hand side. Since the x-axis is time I would think that\'s in an oh. That is an earlier time. So the x-axis is the earlier time on the left hand side as time goes on what happens is the pul goes from earlier times to later times. That means the later part of the pulse is on the later time Time which is on the right hand side

</div>

<div>

Thought for 10s

**Yes --- you have it exactly right now.**

### Why the earliest part of the pulse is on the **left** side of the plot

- The **x-axis** is **time**, and time increases from **left to right** (standard convention on almost every scientific plot).
- A pulse is a burst of light that arrives over a short interval of time.
- The **very first photons** to reach the detector after the cloud arrive at the **smallest time value**.
- Those earliest-arriving photons are plotted on the **left** side of the graph.
- Photons that arrive a little later are plotted further to the **right**.
- Photons that arrive even later (the trailing edge / back of the pulse) are plotted even further right.

So:

- **Left side of the plot** = **early arrival times** = **front / leading edge** of the pulse.
- **Right side of the plot** = **later arrival times** = **back / trailing edge** of the pulse.

The whole pulse envelope is drawn as a hump on this time axis. The front rises on the left, the peak is somewhere in the middle, and the back falls on the right.

(When we talk about the pulse "moving to the right" in space, that is its physical propagation. On a fixed detector's time plot the front simply appears first --- on the left.)

### With the correct orientation, the reshaping is now clear

- **Left side (front / early times)**: stronger absorption → intensity drops a lot on the left.
- **Right side (back / later times)**: coherent re-radiation adds constructively → intensity rises on the right.

Because the left side is lowered **more** than the right side is raised, the highest point of the hump moves **leftward** on the plot (to an earlier time value).

That leftward movement of the maximum = the peak arrives **earlier** = negative group delay.

The re-emitted light adds to the right side (later times), but the bigger drop on the left still pulls the location of the peak to the left (earlier).

You now have the axis correct, so the direction of the shift follows directly from the asymmetric change (more loss on left, gain on right).

This is the reshaping whose effect on the atoms is measured as a negative weak-valued excitation time for the transmitted photons.

Does everything line up now with the left = front / early times, or is there still any part of the addition vs. removal timing that feels off?

</div>

<div>

<div>

So the peak go from the right and move to the left, which means moving to left puts the peak at an earlier time

</div>

<div>

Thought for 10s

**Yes --- exactly.**

On the plot (time increasing left → right):

- The **location of the peak** moves **leftward**.
- Leftward on the time axis = **smaller time value** = **earlier arrival**.

That is the **forward shift / advancement of the peak** (negative group delay).

The mechanism produces it because:

- The left side (front) drops more (stronger absorption).
- The right side (back) rises some (coherent re-radiation).
- The highest point therefore occurs at an earlier time (further left on the plot) than it did without the atoms.

This is why the weak-valued atomic excitation time for the transmitted photons equals the group delay --- including when that number is negative.

You now have the full picture:

- Correct time axis (left = early/front, right = late/back).
- Asymmetric change moves the peak left (earlier).
- That advancement = negative group delay = negative measured excitation time for post-selected transmitted photons.

The re-emitted light adds to the right side after the front has already been more strongly absorbed, so the net maximum slides left.

Everything consistent now? Or any last detail still fuzzy?

</div>

</div>

Expert
