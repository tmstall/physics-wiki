---
source: claude_export
conversation_uuid: 7a3d1b76-1c22-4165-aa83-8700029aa751
title: "The Oscilloscope That Outran the Electron"
created_at: 2026-07-05T05:58:22.903641Z
updated_at: 2026-07-05T06:07:54.910928Z
tier: A
score: 57
n_messages: 4
---

# The Oscilloscope That Outran the Electron

## Human

Analyze this paper

## Assistant

Full text uploaded — no retrieval needed, no Access Disclosure required. This is a full Nature Photonics Article with substantial experimental and theoretical content, not a lite candidate, so proceeding directly to full analysis.

---

## 1. Punchy Title & One-Sentence Hook

**The Oscilloscope That Outran the Electron**

For the first time, a microscope has pinned down a single tunnelling electron in *both* time (under a femtosecond) *and* space (a few angstroms) simultaneously — and discovered that at this "space-time limit," the electron lags behind the light field pushing it.

## 2. Big-Picture Context

**Paper Type & Stakes:** This is an experimental capability paper with strong theory support — it demonstrates a new instrument class (attosecond lightwave STM) and uses it to reveal new physics (retarded, photon-assisted tunnelling at the intermediate Keldysh regime). The stakes: whether we can watch electronic wavefunctions move inside atoms, molecules, and solids at their intrinsic scales.

Lightwave-driven STM has existed for about a decade. The idea: instead of a DC bias driving tunnelling continuously, you let the oscillating electric field of a focused light pulse transiently tilt the tunnelling barrier, so electrons tunnel only during a chosen half-cycle of the wave. With terahertz pulses (period ~1 ps), this gave ~100 fs snapshots of molecular orbitals — spectacular, but on those timescales electrons follow nuclei adiabatically. Nothing genuinely *electronic* happens that slowly. The intrinsic timescale of electron motion is attoseconds to femtoseconds, and the intrinsic length scale is angstroms. Reaching both at once — the "space-time limit" — is the holy grail this paper claims.

The obvious move is to crank the carrier frequency from 1 THz to ~190 THz (near-infrared), shrinking the tunnelling window ~200-fold. But this crossing changes the physics itself. At THz frequencies the Keldysh parameter κ is much less than 1: the field is quasi-static, and electrons tunnel adiabatically through the tilted barrier. At NIR frequencies in this junction, κ ≈ 1 — the crossover regime where field-driven tunnelling and multi-photon absorption compete on equal footing. The electron can no longer respond instantly. The paper turns this complication into the discovery: the temporal and spatial structure of the tunnelling wave packet become intertwined, and both can be measured and controlled.

There's also a quiet methodological subplot. Prior claims of attosecond control in STM (notably Garg & Kern, *Science* 2020, which this paper cites specifically regarding beam chopping) used intensity-modulation schemes. This paper shows that even 10⁻⁴ relative laser-power fluctuations create thermal current artifacts that *exceed* the genuine lightwave-driven signal by orders of magnitude — a pointed demonstration that motivates their entirely different, constant-power detection scheme.

**Prior Belief Check:** The core findings align with, rather than contradict, mainstream expectations: attosecond CEP-sensitive currents from nanotips were established (Krüger 2011, Dienstbier 2023), and κ ≈ 1 physics was theoretically anticipated (Ma et al., PRL 2024). What will surprise experts is (a) the demonstrated *simultaneity* of attosecond timing and atomic-scale imaging — the field expected this was coming, but nobody had done it — and (b) the cleanly resolved 0.5 fs retardation of the current behind the field maximum, direct evidence of non-instantaneous tunnelling response. The thermal-artifact analysis will also raise eyebrows, since it implicitly questions the robustness of earlier intensity-modulated attosecond-STM claims. Overall: a genuine capability milestone, with the underlying physics evolutionary rather than revolutionary.

**Replication & Convergence Note:** This is a single-group result (Regensburg experiment, MPSD Hamburg theory) with no independent replication of the combined attosecond + atomic-scale measurement; independent confirmation would look like another lightwave-STM group (Cocker's, or the Hommelhoff-adjacent nanotip community adapting to junctions) reproducing CEP-sensitive sub-femtosecond currents *with their own artifact controls* — which matters especially here because the history of this subfield includes contested claims traced to thermal artifacts.

## 3. Necessary Background Crash-Course

**Lightwave-driven STM.** A conventional STM applies a DC bias and reads a steady tunnelling current. A lightwave STM lets the electric field of a light pulse act as an ultrafast transient bias: for a fraction of one optical cycle, the field tilts the potential landscape and electrons tunnel across the tip–sample gap.

*Analogy:* Think of the light field as a clock edge on a single-electron transistor. The DC bias sets the operating point; the optical field is a sub-cycle gate pulse that opens the channel for a sliver of time far shorter than any electronic pulse generator could produce.

**Breaks when:** you push it to gate *fidelity* — a real clock edge is engineered to switch the channel deterministically, but here the "gate" is a smooth analog field and the tunnelling response is exponentially nonlinear and probabilistic; most cycles transfer far less than one electron.

**Carrier-envelope phase (CEP).** A few-cycle pulse has an envelope (the overall intensity hump) and a carrier (the oscillation inside it). The CEP is the offset between the carrier's crest and the envelope's peak. For a single-cycle pulse, CEP decides whether the field's strongest excursion points "up" or "down" — and by how much the strongest half-cycle beats the second-strongest.

*Analogy:* The envelope is a wave group rolling toward shore; the CEP determines whether the tallest individual wave sits exactly at the group's center or slightly off it. Surfers (electrons) only catch the single tallest wave, so this offset controls everything.

**Breaks when:** the pulse contains many cycles — then adjacent crests are nearly equal in height, the "tallest wave" advantage vanishes, and CEP effects wash out (exactly what the authors show in Extended Data Fig. 3).

**Keldysh parameter κ.** A dimensionless ratio comparing the field's oscillation speed to the time an electron needs to traverse the barrier. κ ≪ 1: the field looks quasi-static, and the electron tunnels adiabatically through a tilted barrier (strong-field regime). κ ≫ 1: the field oscillates too fast for tunnelling to follow, and the electron instead absorbs discrete photons (multi-photon regime). κ ≈ 1: both channels operate at once.

*Analogy:* It's the ratio of clock period to gate delay in a logic circuit. If the clock is slow relative to the gate delay (κ ≪ 1), the transistor tracks the input faithfully — quasi-static operation. If the clock outruns the gate delay (κ ≈ 1 and beyond), the device response lags and distorts; you've entered a regime where the switching dynamics themselves matter.

**Breaks when:** you take "clock too fast" to mean the signal simply doesn't get through. In the quantum case the fast field doesn't block transport — it opens a *different* channel (photon absorption into excited states) that actually *enhances* transmission through a reduced effective barrier.

**Kramers–Henneberger (KH) transformation.** A mathematical identity: an electron in an oscillating field near a static barrier is exactly equivalent to a field-free electron near a barrier that *shakes back and forth in space*. Temporal modulation and spatial displacement are two descriptions of the same physics.

*Analogy:* Filming a pole vaulter from a camera car moving with the athlete — you can put all the motion into the athlete (lab frame) or into the scenery (KH frame). The physics is identical; one frame just makes the space-time coupling obvious.

**Breaks when:** the shaking amplitude or frequency gets so extreme that the time-averaged potential itself deforms (KH atom stabilization regime) — then the "same physics, different frame" intuition needs the full dressed-potential treatment, not just a rigid displacement.

**Lock-in detection at the CEP-offset frequency.** The experiment's central trick. The CEP is swept linearly at f₍CEO₎ ≈ 917 Hz while total laser power stays rigorously constant. Only current components that *depend on the field's waveform shape* — genuine lightwave-driven tunnelling — oscillate at f₍CEO₎. A lock-in amplifier demodulates at exactly that frequency.

*Analogy:* This is differential signaling for photocurrents. Thermal effects respond to power (common mode); lightwave tunnelling responds to waveform shape (differential mode). By modulating only the shape and demodulating at the modulation frequency, everything common-mode — thermal drift, DC background, 1/f noise — is rejected, just as a differential receiver rejects ground bounce.

**Breaks when:** any spurious effect couples to CEP itself rather than power. The rejection is only as good as the orthogonality between "waveform shape" and every artifact channel; the authors verify power is CEP-independent to 10.2 nW, but the analogy hides that this orthogonality had to be *engineered and measured*, not assumed.

**Central analogy for this paper:** *A light-field clock edge strobing a one-electron transistor.*

## 4. Core Technical Explanation

**Waveform synthesis.** The authors build a CEP-stable Er:fibre laser producing two spectrally *disjoint* NIR pulses centred at 164 THz and 249 THz. Because their spectra don't overlap, the pulses cannot interfere — so sweeping their mutual delay τ changes the *shape* of the combined field without changing average power at all. At τ = 0 the superposition synthesizes a single-cycle waveform: 5.2 fs FWHM intensity envelope at a 190 THz effective carrier, peak far-field of 7.6 MV cm⁻¹ at the tip. An acousto-optic phase shifter sweeps the CEP linearly in time, and the CEP-dependent part of the tunnelling current, I₍CEO₎, is extracted by lock-in demodulation — along with its phase φ₍CEO₎ relative to the CEP sweep.

They do this because the enemy is thermal. Extended Data Fig. 1 shows that power modulations at the 10⁻⁴ level already produce thermal current modulations exceeding the lightwave signal. Chopping the beam — the standard approach — is therefore disqualified. Modulating CEP at constant power is the only channel that carries lightwave physics and nothing else.

**Fingerprints of subcycle tunnelling (Fig. 2).** Scanning τ over an atomically flat Ag(100) surface, I₍CEO₎(τ) appears only near τ = 0, where the two pulses overlap into the most asymmetric waveforms. It oscillates on subcycle scales with reproducible features down to 0.5–0.6 fs, and its peak scales threshold-like with pulse energy — a nonlinear signature. The phase φ₍CEO₎(τ) shows discrete steps precisely at the current minima. The mechanism (Fig. 2f) is elegant: as τ shifts, the position of the envelope maximum relative to the carrier crest evolves, and at specific delays the envelope develops *two* equally strong maxima — the "tallest wave" identity suddenly jumps from one crest to another, producing a phase step within a few hundred attoseconds of delay.

**Full quantum theory.** They simulate the junction with time-dependent density functional theory: a 55-atom sodium pyramid tip facing a 256-atom Na(100) slab, driven by the experimentally retrieved waveforms. TD-DFT treats strong-field and multi-photon physics on equal footing — essential at κ ≈ 1, where neither perturbation theory nor quasi-static tunnelling models suffice. The simulated I₍CEO₎(τ) and φ₍CEO₎(τ) reproduce the measurements (Fig. 2c–e), licensing them to read off quantities the experiment can't directly time-resolve.

The headline extraction: the current transient is confined to 988 attoseconds FWHM — but its maximum is *delayed by 0.5 fs after the field maximum*, persisting to ~1.5 fs. In THz-STM the current tracks the field instantaneously. Here the barrier modulation approaches the electrons' own response time (the Keldysh time), and the charge transfer lags. The charge-density movies (Fig. 3b) show why: the field first "shakes up" the density, transiently populating excited states near the vacuum level (confirmed in Fig. 3c). Tunnelling at κ ≈ 1 proceeds *through* these spatially extended excited states, which see a reduced barrier — photon-assisted tunnelling, sketched in Fig. 3d.

For the illustrative one-dimensional picture (Fig. 1a,b), the KH transformation converts the field's tilt of the barrier into a rigid spatial shift. Breaking the sentence for the one equation worth displaying:

$$\Delta x(t) = \frac{e\,E_x(t)}{m_e\,\omega^2}$$

Symbol definitions:
- $\Delta x(t)$ : instantaneous spatial displacement of the barrier in the KH frame (angstroms)
- $e$ : elementary charge
- $E_x(t)$ : instantaneous electric field along the tunnelling axis
- $m_e$ : electron mass
- $\omega$ : central angular frequency of the driving field

What this actually means: the oscillating field is exactly equivalent to physically shaking the barrier back and forth, with amplitude set by field strength divided by frequency squared. For their parameters the barrier excursion is 1.1 Å — comparable to atomic dimensions. Think of jitter injection in a timing circuit: modulating the threshold in time is indistinguishable from modulating the position of the sampling window, and because the excursion here rivals the feature size, timing structure imprints directly onto spatial structure.

**Measuring the wave packet's size (Fig. 4).** Vertical extent: retracting the tip, I₍CEO₎ at the highest pulse energy (171 pJ) decays over l_c = 8.7 Å — nearly an order of magnitude longer than the 1 Å decay of steady-state Fermi-level tunnelling. Excited electrons see a shallower barrier and reach farther. Dropping pulse energy to 36 pJ steepens the decay to 3.8 Å: less few-photon excitation, more compact packet. Pulse energy is thus a *spatial confinement knob*. Lateral extent: raster-scanning over a single Cu adatom on Ag(100) in constant-height mode, the attosecond current I₍CEO₎ resolves the atom with ~6 Å lateral confinement, matching the simultaneous DC image. Attosecond electron pulses sculpted to few-angstrom size in all three dimensions — the space-time limit, reached.

**Assumption Audit**

- **Watch:** Reader likely assumes the 988-as current transient was directly *measured* with attosecond timing. The paper actually measures CEP-locked lock-in currents versus delay; the sub-femtosecond temporal shape and the 0.5 fs retardation are extracted from TD-DFT simulations validated against those measurements. The experiment constrains; the theory time-resolves.
- **Watch:** Reader likely assumes this is strong-field tunnelling like THz-STM, just faster. The paper actually establishes κ ≈ 1 photon-assisted transport through transiently occupied excited states — qualitatively different physics, with delayed response and extended wavefunctions that strong-field models miss.
- **Watch:** Reader likely assumes lowering pulse energy merely reduces signal-to-noise. The paper actually shows it changes the transport channel mix — suppressing few-photon excitation spatially *compacts* the wave packet from 8.7 Å to 3.8 Å vertical extent, which is why the "sweet spot" for space-time confinement sits at moderate, not maximal, field.
- **Watch:** Reader likely assumes the two pulses form an interferometric pump–probe pair. The paper actually uses spectrally non-overlapping pulses that *cannot* interfere; τ acts purely through waveform synthesis of the combined field, which is what makes constant-power CEP detection possible in the first place.

## 5. What's Genuinely New or Clever

**New to the field, instrumentally:** the constant-power CEP-modulation lock-in scheme. Every prior route to lightwave signals in STM modulated intensity somewhere, leaving a thermal back door. Sweeping CEP at ~1 kHz with power stable to 10⁻⁴ and demodulating at f₍CEO₎ makes the detection channel orthogonal to thermal physics *by construction*. Combined with the spectrally disjoint two-color synthesis — attosecond-precision waveform control with zero interference — this is the enabling invention.

**New to the field, physically:** the first simultaneous demonstration of attosecond temporal and angstrom spatial resolution in real-space microscopy (the Cu adatom image taken with sub-femtosecond currents), plus the cleanly resolved non-instantaneous tunnelling response at κ ≈ 1 — the 0.5 fs current retardation tied to the Keldysh time, revealed by the theory–experiment combination. The recognition that pulse energy tunes the *spatial size* of the tunnelling wave packet (via the excitation channel mix) is the conceptual bridge that makes "space-time sculpting" more than a slogan.

## 6. Limitations & Open Questions

The adatom contrast mechanism is unresolved — I₍CEO₎ *decreases* over the Cu adatom, tentatively attributed to a local work-function change, and the paper flags it as under investigation. (A) Consensus — the authors state this explicitly and the tentative assignment is clearly labeled as such. (paper, "Measuring the size" section)

The temporal shape of the current — including the headline 988 as duration and 0.5 fs delay — rests on TD-DFT, not direct measurement; absolute attosecond clocking of the transfer has not been performed. (A) Consensus — the authors themselves close by calling for "absolute clocking experiments" to clarify attosecond delays. (paper, Conclusion)

The TD-DFT model replaces tungsten/silver/copper with sodium clusters under the LDA functional. The transferability argument leans on one prior benchmark (ref. 55), and how quantitatively Na/LDA captures d-electron screening, image-potential states, and work-function details of real transition-metal junctions is genuinely debatable. (B) Contested — TD-DFT practitioners disagree on how far jellium-like alkali models can be pushed for quantitative junction dynamics, even when qualitative agreement is excellent. (broader literature)

The entire signal chain depends on power stability better than 10⁻⁴ and on the demodulated power being τ-independent; any system where CEP control couples even weakly to pointing or power (different laser architectures, plasmonic tips) could reintroduce artifacts that mimic waveform-dependent currents. This bears directly on how easily other groups can replicate. (C) Speculative — the paper demonstrates its own orthogonality convincingly, but I am extrapolating about fragility in other implementations; instrument builders may know mitigations I don't. (analyst inference)

The measurements average over ~10⁸ pulses per data point (80 MHz, 100 ms lock-in); the "single electron" is statistical — far less than one electron transfers per pulse, and shot-to-shot correlations or rare multi-electron events are invisible. (B) Contested — whether ensemble-stroboscopic measurement meaningfully limits the "single-electron wavefunction" interpretation is a live foundational argument in ultrafast physics, with reasonable people on both sides. (analyst inference)

Follow-up work in 12–24 months should include: absolute clocking of the tunnelling delay (attosecond-streaking-style referencing), imaging of a molecular orbital rather than an adatom with attosecond currents, resolving the adatom contrast mechanism, and a second-group replication with an independent artifact budget.

## 7. Detailed Summary & Explanation

The Regensburg–Hamburg team set out to answer whether a scanning tunnelling microscope can operate at the intrinsic scales of electronic motion — attoseconds in time, angstroms in space — and what tunnelling even looks like there. Their instrument synthesizes single-cycle near-infrared waveforms from two spectrally separate pulses whose delay tunes the field shape with attosecond precision. Because the pulses cannot interfere, average power never changes; only the waveform does. Sweeping the carrier-envelope phase at about 917 hertz and lock-in detecting the current at that frequency isolates the genuinely lightwave-driven current from thermal backgrounds that would otherwise swamp it by orders of magnitude.

The detected current appears only where the pulses overlap into strongly asymmetric single-cycle fields, oscillates on subcycle timescales with reproducible half-femtosecond features, and carries phase steps that track sudden jumps in which field crest is tallest — all hallmarks of tunnelling controlled by the waveform itself rather than by the pulse's energy content. Time-dependent density functional simulations of a model junction reproduce these observables quantitatively, and from the validated theory the authors extract that the current flows in a burst lasting just under one femtosecond — but delayed by half a femtosecond after the field peak. That delay is the signature of the intermediate light–matter regime, where the Keldysh parameter is near one: the barrier oscillates almost as fast as the electrons can respond, and transport proceeds through briefly occupied excited states that see a thinner effective barrier.

Those excited states are spatially extended, and that is where time and space intertwine. At high pulse energy the wave packet's vertical decay length is 8.7 angstroms — nearly nine times longer than ordinary tunnelling. Reducing the pulse energy suppresses the excitation channel and compacts the packet to 3.8 angstroms. Choosing moderate energy, the team images a single copper adatom using only the attosecond current, confirming lateral confinement of about six angstroms. The electron pulse is confined to under a femtosecond in time and a few angstroms in all three spatial dimensions simultaneously.

Why frame the summary this way? The key interpretive choice is to treat the instrumentation and the physics as one story: the artifact-immune detection scheme is not plumbing, it is the reason the physical claims are credible in a subfield with a contested history. The second choice is to keep the division of labor explicit — experiment establishes waveform-controlled, CEP-sensitive, atomically localized currents; theory supplies the attosecond-resolved internal timing. The reader should take away that "space-time limit" here is not rhetoric: temporal structure and spatial extent of the tunnelling electron are coupled through the excitation pathway, and both are now measurable and tunable.

**Where I'm least confident in this analysis:** the mechanism I gave for the phase steps of the current (the envelope developing two equal maxima and the "tallest crest" identity jumping) compresses a subtle waveform-synthesis argument from Fig. 2f and Extended Data Fig. 2 into a picture I could not fully verify against the fitting pipeline that extracts the CEP-dependent charge from the simulations — the quantitative link between the fitted phase and the physical crest-swap is where my plain-language translation is most likely to have lost something real.

## 8. Three Crystallized Takeaways

1. A microscope can now watch a single electron tunnel with better-than-femtosecond timing *and* atom-scale position at the same time — the long-sought "space-time limit" of electron imaging has been reached.

2. At these speeds, tunnelling stops being instantaneous: the electron lags the light field by half a femtosecond because it hops through briefly excited states — and those states are physically bigger, so how *fast* you drive the electron changes how *large* it is.

3. The breakthrough was as much noise engineering as physics: by modulating only the light wave's shape at perfectly constant power, the team built a detection channel that thermal artifacts — the poison of every previous attempt — cannot enter.

## 9. Shorter Summary

Electrons move on attosecond timescales and live on angstrom length scales. Microscopy has long been forced to choose one or the other: electron microscopes see atoms but blur motion; ultrafast optics catches motion but blurs space. This paper reaches both at once, using a scanning tunnelling microscope driven not by a battery but by the electric field of a single cycle of infrared light.

The team synthesizes light waveforms from two color-separated pulses whose relative delay sculpts the combined field with attosecond precision. Because the colors never overlap, the total power stays perfectly constant while the wave's shape changes — and only a genuinely light-driven tunnelling current cares about shape. By wobbling the wave's internal phase a thousand times per second and listening for current changes at exactly that rhythm, they filter out the thermal effects that have plagued (and possibly contaminated) earlier attempts at this experiment.

The resulting current flows in bursts lasting under a femtosecond. Strikingly, quantum simulations that reproduce the data show the burst peaks half a femtosecond *after* the light field does. At these frequencies the barrier flickers almost as fast as electrons can react, so instead of sliding through a slowly tilting barrier, electrons hop via fleetingly occupied excited states. Those states are physically larger, which couples timing to size: at full laser power the electron cloud stretches nearly nine angstroms out of the surface, while at reduced power it compacts to under four. Driving strength becomes a dial for the electron's spatial extent.

Choosing the compact setting, the researchers imaged a single copper atom sitting on a silver surface using only the sub-femtosecond current — proving the electron pulse is confined to atomic size in all three dimensions while lasting less than a millionth of a billionth of a second.

The result opens a genuinely new observational window: watching electron wavefunctions reshape during chemical bond formation, inside next-generation petahertz electronics, or wherever quantum motion and atomic structure meet. One caveat: the finest timing details rest on simulation, and direct attosecond clocking — plus independent replication — comes next.

## Human

Analyze this paper

Published 24 July 2024 • © 2024 The Author(s)
Journal of Cosmology and Astroparticle Physics, Volume 2024, July 2024
Citation A.M. Lopez et al JCAP07(2024)055
DOI 10.1088/1475-7516/2024/07/055

PDFOpens in a new tab.
Article metrics
4141 Total downloads

2323 total citations on Dimensions.
Share this article
Abstract
We present the discovery of `A Big Ring on the Sky' (BR), the second ultra-large large-scale structure (uLSS) found in Mg II-absorber catalogues, following the previously reported Giant Arc (GA). In cosmological terms the BR is close to the GA — at the same redshift z ∼ 0.8 and with a separation on the sky of only ∼ 12°. Two extraordinary uLSSs in such close configuration raises the possibility that together they form an even more extraordinary cosmological system. The BR is a striking circular, annulus-like, structure of diameter ∼ 400 Mpc (proper size, present epoch). The method of discovery is as described in the GA paper, but here using the new Mg II-absorber catalogues restricted to DR16Q quasars. Using the Convex Hull of Member Spheres (CHMS) algorithm, we estimate that the annulus and inner absorbers of the BR have departures from random expectations, at the density of the control field, of up to 5.2σ. We present the discovery of the BR, assess its significance using the CHMS, Minimal Spanning Tree (MST), FilFinder and Cuzick & Edwards (CE) methods, discuss it in the context of the GA+BR system, and suggest some implications for the origins of uLSS and for our understanding of cosmology. For example, it may be that unusual geometric patterns, such as these uLSSs, have an origin in cosmic strings.

BibTeXRIS

Authors
Article information
Previous article in issue
Next article in issue

Published by IOP Publishing Ltd on behalf of Sissa Medialab. Original content from this work may be used under the terms of the Creative Commons Attribution 4.0 licence. Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI.

Show References
Journal articles
Hubble Space Telescope Faint Object Spectrograph Observations of a Unique Grouping of Five QSOs: The Sizes and Shapes of Low-z Lyα Forest Absorbers
Large-Scale Structure at z = 1.2 Outlined by Mg II Absorbers
ODIN: Identifying Protoclusters and Cosmic Filaments Traced by Lyα-emitting Galaxies
The Importance of Einstein Rings
The Sloan Lens ACS Survey. VI. Discovery and Analysis of a Double Einstein Ring
IOPscience
Books
IOP Conference Series
About IOPscience
Contact Us
Developing countries access
IOP Publishing open access policy
Accessibility
IOP Publishing
Copyright 2024 IOP Publishing
Terms and Conditions
Disclaimer
Privacy and Cookie Policy
Text and Data mining policy
Publishing Support
Authors
Reviewers
Conference Organisers
About IOP Publishing
IOP Publishing, the publishing arm of the Institute of Physics, is a purpose-led, not-for-profit, society-owned scientific publisher. We publish high-quality, trusted, peer-reviewed research in over 100 scientific journals on our IOPsicence platform, providing visibility, recognition, and impact for work across the physical sciences.
IOP Publishing
IOP Publishing Facebook page
IOP Publishing LinkedIn page
IOP Publishing Youtube page
IOP Publishing WeChat QR code
IOP Publishing Weibo page
IOP Publishing Bluesky page
IOP Publishing Threads page

## Assistant

| partial upload — retrieving full paper

This is a landing page + abstract only, so I'm executing the master retrieval protocol before analyzing.

Full text located on arXiv — fetching the body now.

I have sections 1–4.2; the fetch truncated before §4.3 and §5 (Discussion). Grabbing the remainder.

Analyzing | Framework v3.7.1 | partial upload — full text retrieved, tail sections truncated

**Access Status**
Full paper: retrieved from arXiv (2402.07591v2, HTML version) — complete through §4.2, but the fetch truncates mid-way through the ellipse analysis; §4.3 (Equivalent widths) and §5 (Discussion and conclusions) were not recovered despite a second targeted attempt.
Abstract: retrieved (JCAP landing page, user-supplied + arXiv).
Supplementary material: Sky & Telescope discovery feature (including expert reaction context); the same group's follow-up "A Giant Ring on the Sky" (arXiv 2604.17534, April 2026) surfaced in search and informs the replication picture.
Analysis basis: full text of §§1–4.2 + abstract + secondary sources for the missing discussion section.

---

## 1. Punchy Title & One-Sentence Hook

**The Ring That Shouldn't Fit in the Universe**

A near-circular arrangement of galaxies 1.3 billion light-years across — bigger than the scale at which the cosmos is supposed to look smooth — sits on the sky just 12 degrees from an equally impossible Giant Arc, at the same distance, found by the same three people.

## 2. Big-Picture Context

**Paper Type & Stakes:** This is an observational discovery-and-significance paper — a serendipitous structure detection followed by a battery of post-hoc statistical defenses. What's at stake is nothing less than the Cosmological Principle: if genuinely coherent structures exceed the ~370 Mpc homogeneity ceiling, the assumption underlying every FLRW-based calculation in cosmology is in trouble.

The standard model of cosmology rests on the assumption that, averaged over large enough volumes, the Universe is homogeneous and isotropic. Structure formation theory then predicts a rough ceiling on how large a coherent overdensity can grow by any given epoch — commonly quoted near 370 Mpc. Over three decades, a rogues' gallery of claimed violators has accumulated: the Sloan Great Wall, the Huge Large Quasar Group, the Hercules–Corona Borealis Great Wall, the giant GRB ring, the South Pole Wall. This paper adds the Big Ring (BR): ~400 Mpc in diameter, at redshift z ~ 0.8, traced by 51–62 magnesium-absorption systems, sitting a mere 12° from the Giant Arc the same team reported in 2022 in the *same redshift slice*. The authors raise the possibility that GA+BR form a single, even larger system, and float cosmic strings — relic one-dimensional topological defects from a symmetry-breaking phase transition — as a possible origin, alongside more exotic alternatives like Penrose's Conformal Cyclic Cosmology.

The detection method matters as much as the claim. Individual galaxies at z ~ 0.8 are too faint for SDSS to map wholesale, so the team uses Mg II absorbers: cold gas halos around galaxies and groups that imprint a distinctive absorption doublet (rest wavelengths 2796 and 2803 angstroms) on the spectra of background quasars. Each absorber gives an exquisitely precise redshift (velocity error tens of km/s) but only where a background quasar happens to pierce that patch of sky. The map of matter is therefore inherently sparse and shaped by where the survey pointed — the paper's core methodological battle is separating real structure from the fingerprint of the probe distribution.

The technical arc: discover the ring visually in the new Anand21 DR16Q absorber catalogue; verify all 59 doublets by eye in the raw spectra (100% real); show the pattern doesn't repeat in adjacent redshift slices using the same quasars (so it's not a probe artifact); assess significance with four semi-independent statistics (CHMS, MST, Alpha Hull, Cuzick–Edwards); corroborate with bright field quasars and DESI photometric clusters as independent tracers; and finally rotate the 3D absorber positions to reveal that the "ring" is really a coil aligned face-on with our line of sight.

**Prior Belief Check:** This paper contradicts, rather than complicates, the mainstream position — and the mainstream has pushed back on exactly this genre of claim. The prevailing counterargument, articulated forcefully after the Huge-LQG episode (Nadathur 2013), is that friends-of-friends-style linking applied to sparse point processes readily "finds" enormous connected patterns even in perfectly homogeneous random fields, so exceeding 370 Mpc in *linked extent* does not by itself falsify the Cosmological Principle. Senior figures including Jim Peebles publicly weighed in with measured skepticism when the BR was announced. So the result is surprising to experts not because a ring pattern exists in the data — the visual pattern is undeniable — but because the authors interpret it as a physical, CP-challenging structure. That interpretive step is where consensus breaks: the field broadly accepts the *detection*, contests the *significance framework*, and largely rejects the *cosmic-string interpretation* as premature. This is a contested, potentially field-shaking claim, not an incremental result — and equally, not yet an accepted one.

**Replication & Convergence Note:** This is a single-group result in the strongest sense — the Giant Arc, Big Ring, and the 2026 follow-up Giant Ring all come from the same Lopez–Clowes collaboration, the same sky field, and the same Mg II methodology, so the follow-ups corroborate the pattern but not independently; genuine confirmation would require a different team recovering the BR in a different tracer with full 3D coverage (DESI spectroscopic galaxies or Mg II from DESI spectra mapping this exact volume), which matters acutely here because the entire debate hinges on methodology rather than data quality.

## 3. Necessary Background Crash-Course

**Mg II absorbers as matter tracers.** A quasar's light crosses billions of light-years before reaching SDSS. Any galaxy halo it passes through steals a characteristic pair of wavelengths — the Mg II doublet — from the spectrum, stamped at the absorber's redshift, not the quasar's. Each detection localizes cool gas (hence a galaxy or group) in 3D with superb depth precision.

*Analogy:* It's traceroute for the cosmos. Each quasar sightline is a probe packet crossing the network; every absorber is a router that stamps its address on the packet in transit. You reconstruct network topology not by imaging the routers but by collecting hop records along whatever routes your packets happened to take.

**Breaks when:** you forget that traceroute coverage defines what you can see. A region with no sightlines isn't empty — it's unmeasured. The paper's flat-fielding against the probe distribution is the constant fight against confusing "no packets went there" with "nothing is there."

**The homogeneity scale and uLSS.** Averaging the galaxy distribution in ever-larger boxes, the density contrast shrinks; beyond roughly 370 Mpc it's expected to be statistically uniform. The authors coin "ultra-large LSS" (uLSS) for candidate structures exceeding that ceiling.

*Analogy:* Zoom out on a chip die photo. At transistor scale it's wildly heterogeneous; at full-wafer scale every reticle looks identical. The homogeneity scale is the zoom level where the wafer becomes boring. A uLSS claim is like finding one reticle-spanning defect pattern on a wafer that's supposed to be defect-uncorrelated at that scale.

**Breaks when:** you equate "a connected pattern larger than the scale" with "variance exceeding expectation at that scale." A scratch-shaped chain of ordinary, uncorrelated point defects can span the wafer without any single process excursion causing it — this is precisely the Nadathur-style critique of uLSS claims.

**SLHC linking and CHMS/MST significance.** Single-Linkage Hierarchical Clustering joins absorbers into candidate structures whenever neighbors sit closer than a linkage scale (~76–80 Mpc here, scaled to field density). CHMS then asks: distribute this many points randomly at the control-field density — how often is their convex-hull volume as small (as compact) as observed? MST significance instead asks how anomalously short the mean edge of the minimal spanning tree is. Both measure "these points are more crowded than chance," expressed in σ.

*Analogy:* CHMS is like judging a point cluster by its bounding box; MST by its average nearest-neighbor wiring length. For a blob, both agree. For a ring, the bounding box is mostly empty air — the bounding-box metric (CHMS) systematically understates how special the arrangement is, which is exactly the CHMS-vs-MST spread the paper reports.

**Breaks when:** you treat either number as "probability this ring shape is real." Both test compactness against randomness at an assumed control density — neither tests *ring-ness*, and neither knows about the visual pre-selection that defined the member list.

**Cosmic strings.** Hypothetical line-like defects frozen into spacetime during an early-universe phase transition, carrying enormous energy per unit length; they would seed matter along wakes and loops, potentially producing geometric — even ring-like — patterns unachievable by ordinary Gaussian gravitational collapse.

*Analogy:* Dislocation lines in a rapidly cooled crystal. Quench a melt fast enough and the ordered phase can't coordinate globally; mismatched domains leave one-dimensional defect lines threading the solid. The universe's symmetry-breaking transitions could have done the same to spacetime's vacuum structure.

**Breaks when:** you use it to predict specifics. Crystal dislocations are directly imaged and well-quantified; cosmic strings are unobserved, with CMB and gravitational-wave bounds pushing their allowed tension ever lower, and no worked-out string model in the paper produces a 400 Mpc coil quantitatively.

**Central analogy for this paper:** *Cosmic traceroute — topology inferred from borrowed sightlines.*

## 4. Core Technical Explanation

**Discovery and data hygiene.** While re-examining the Giant Arc field with the newer Anand21 Mg II catalogue (built from SDSS DR16Q — over three times the background quasars and twice the absorbers of the older Z&M catalogue used for the GA), the authors visually spot an annulus of absorbers, ~400 Mpc across, north of the GA in the z = 0.802 ± 0.060 slice. They do three things before any statistics. First, they eyeball all 59 doublet systems in the raw spectra: every one is real. Second, they compare the two absorber catalogues probe-by-probe and find only ~60% agreement on shared quasars — each pipeline misses real absorbers the other catches — which they flag as an inherent completeness limitation. Third, the artifact test: keeping the *same* background quasars, they map absorption in the adjacent non-overlapping redshift slice (z = 0.682). If the ring were an imprint of the probe pattern (survey geometry, plate boundaries, S/N structure), it would recur there. It doesn't — no SLHC structure, no FilFinder filament. The ring lives at one redshift; the probes span all of them. That's the single cleanest argument that the BR is in the gas, not the survey.

**The significance battery.** They run four member-identification routes (SLHC-linked, visually-selected with and without interior absorbers, FilFinder-selected) against two significance metrics. The pattern in the numbers is instructive: the visually-selected full set gives the headline CHMS 5.2σ; the SLHC set gives CHMS 3.6σ but MST 4.7σ; FilFinder members give CHMS 2.5σ but MST 3.6σ. The MST significance clusters tightly around 4σ across all member definitions, while CHMS swings wildly — because a convex hull wrapped around a ring is mostly empty volume, diluting the compactness signal. The mean over everything is 3.88 ± 0.83σ. An Alpha Hull estimate treating the ring as a tube gives a volume of about 22 million cubic megaparsecs, overdensity 0.75, and a Poisson significance of 4.0σ — concordant with MST. The Cuzick–Edwards case-control test (imported from epidemiology, treating absorbers as "cases" and quasars as "controls" to handle the inhomogeneous probe population) finds clustering at only p ≈ 0.024 (2.0σ) in the BR field but essentially none in four matched comparison fields — supportive in direction, weak in strength, and the authors say so.

**Independent-tracer corroboration.** Field quasars (the ones *in* the slice, not behind it) show no obvious ring by eye, but running FilFinder with increasing size thresholds eliminates every filament except one — a ring-shaped skeleton coinciding with the BR. DESI photometric clusters, particularly the richer ones, trace the lower half of the ring's filamentary path. Neither tracer suffers the Mg II probe-sparsity problem, so this is the paper's best evidence that something physical occupies that annulus — with the caveat that DESI photometric redshift errors smear structures far more than absorber redshifts do.

**The ring is a coil.** The most physically interesting move: exploiting the absorbers' precise redshifts to rotate the 3D distribution. They define a coordinate frame with the mean line of sight as the normal, then re-project along other axes. Side-on, the redshift structure separates into three bands forming a backwards-S; viewed from "below," the BR would have been discovered as an arc, not a ring; at 45°, it clearly resembles a coil (corkscrew) threaded by a thin, flat inner filament, aligned face-on with our sightline. A fitted ellipse gives semi-axes of 184 and 162 Mpc. This kills the most conventional explanation available — that the BR is a fortuitous detection of a single Baryon Acoustic Oscillation shell (characteristic radius ~150 Mpc): the size is somewhat off, and BAO physics produces spherical shells, not coils. It also means "Big Ring" is a projection-dependent name — which the authors candidly note cuts both ways, since other uLSS may hide in "boring" projections.

**Why no simulations?** The authors explicitly decline ΛCDM mock comparisons, arguing a faithful mock would need to simulate the universe, the quasar population, SDSS's spatially varying selection, and the Mg II detection software — too many unknowns. They instead "use the data to correct the data" (flat-fielding, control fields, adjacent-slice tests) and lean on independent tracers.

**Assumption Audit**

- **Watch:** Reader likely assumes 5.2σ means "the ring is real at 5.2σ." The paper actually reports 5.2σ as the CHMS compactness of the *visually-selected* absorber set — the analysis the authors themselves label the upper-limit estimate; the cross-method mean is 3.88 ± 0.83σ, the field-level CE test reaches only 2.0σ, and every one of these tests measures overdensity against a control field, not the probability that a ring-shaped structure exists.
- **Watch:** Reader likely assumes the "no look-elsewhere effect" claim settles the post-hoc problem. The paper actually argues only that they hadn't scanned many fields *before* this discovery — but the BR was found by visually selecting the most striking pattern in a field already famous for hosting the GA, and the significance tests are then applied to the pattern that vision pre-selected; the paper concedes the analysis is "necessarily post-hoc" and mitigated, not eliminated.
- **Watch:** Reader likely assumes exceeding 370 Mpc directly violates the Cosmological Principle. The paper actually establishes a *linked* structure exceeding that scale under a specific linkage definition (its own footnote flags the implicit uniform-survey assumption); whether linkage-connected patterns of this extent are incompatible with homogeneous ΛCDM is precisely the contested question, and this paper does not compute how often ΛCDM mock catalogues produce comparable false positives.
- **Watch:** Reader likely assumes the two absorber catalogues (Anand21, Z&M) are interchangeable measurements of the same sky. The paper actually finds only ~60% agreement on shared quasars, and the Giant Arc itself looks noticeably different in the new catalogue (16 of 51 GA absorbers missed by Anand21) — the tracer maps are pipeline-dependent at a level that matters for fine morphology, even if the gross structures persist.

## 5. What's Genuinely New or Clever

**New to the field, observationally:** a second, independent-in-location uLSS candidate in Mg II absorbers, and the first ring/coil-morphology candidate at these scales from this tracer — plus the striking GA+BR spatial coincidence (same slice, 12° apart), which converts two anomalies into a candidate *system* and sharpens the theoretical challenge beyond what either structure poses alone.

**New to the field, methodologically, and underappreciated:** the same-probes/adjacent-slice artifact test — an elegant control that isolates survey-geometry systematics by holding the sightline network fixed and sliding the redshift window — and the project-plane rotation analysis, which exploits absorber redshift precision to do genuine 3D morphology (ring → coil) on a structure discovered in 2D projection. The recruitment of the Cuzick–Edwards epidemiological case-control test into cosmology (begun in the GA paper, continued here) is a genuinely clever borrowing for exactly this probe-inhomogeneity problem, even though its verdict here is the weakest of the batch.

## 6. Limitations & Open Questions

The significance framework tests compactness against a control density, not the chance of finding *some* striking pattern somewhere in visually-scanned data; the post-hoc, vision-seeded selection is mitigated but not resolved, and the field's standing critique — that linkage algorithms find enormous "structures" in homogeneous random fields — is not confronted with mock catalogues. (B) Contested — the authors argue their look-elsewhere exposure is minimal and post-hoc guidelines from Lopez22 suffice, while critics of prior uLSS claims (the Nadathur line of argument) hold that exactly this analysis pattern generates false CP violations; reasonable experts genuinely disagree. (broader literature)

The refusal to use ΛCDM simulations, however pragmatically motivated, leaves the paper's central quantitative question — how rare is this in a standard universe? — unanswered; approximate mocks (lognormal fields sampled through the real quasar sightline network with the real S/N cuts) are feasible and standard. (B) Contested — the authors state simulations would be too complex and uncertain to be effective, which is a defensible engineering judgment but one many LSS statisticians would reject. (paper §3, analyst inference on feasibility)

Tracer completeness is pipeline-limited: ~60% inter-catalogue agreement on shared probes, SLHC structures that fragment or merge depending on modest S/N cuts, and the GA itself changing appearance between catalogues — fine morphology (the inner filament, the coil's detailed shape, the backwards-S) sits near the reliability floor of the data. (A) Consensus — the paper documents this candidly and repeatedly. (paper §§2.1, 3.1)

The Cuzick–Edwards result (2.0σ, "inconclusive at the >3σ level") is the only field-level, selection-agnostic test in the battery, and it is the weakest — an internal tension the paper reports but does not dwell on. (A) Consensus — explicitly acknowledged in the paper's own wording. (paper §3.4)

The cosmic-string suggestion is a gesture, not a model: no string network calculation is shown to produce a ~400 Mpc face-on coil plus a nearby giant arc at consistent probability, and current bounds on string tension leave limited room. (C) Speculative — I am assessing the theoretical gap; the paper itself offers strings only as a possibility with citations to related suggestive work, and a string theorist may know of loop-collapse morphologies I'm not crediting. (analyst inference)

Redshift-space distortion is dismissed as ~7 Mpc blurring from peculiar velocities, but coherent flows (not random dispersions) can *systematically* distort apparent 3D morphology — a coil aligned with the line of sight is exactly the geometry where coherent velocity structure along the sightline axis could masquerade as spatial structure. (C) Speculative — the paper addresses random blurring, not coherent flows; I'm extrapolating from standard RSD physics and haven't quantified whether plausible flows could produce the observed redshift banding. (analyst inference)

The 12–24 month follow-up agenda writes itself: DESI spectroscopic mapping of this exact volume with galaxies and finer Mg II detection; ΛCDM mock-catalogue false-positive rates for ring/arc-shaped linkages under the real sightline mask; and independent-team reanalysis. Notably, the same group's April 2026 "Giant Ring" paper claims a *third* uLSS in the same field, encircling the BR — which either strengthens the case for something genuinely anomalous in this volume or amplifies the concern that this field and method preferentially generate such findings.

## 7. Detailed Summary & Explanation

Lopez, Clowes, and Williger report a ring-shaped arrangement of matter roughly 400 megaparsecs — 1.3 billion light-years — in diameter, at a distance of 9.2 billion light-years, discovered in maps of cool galaxy-halo gas detected as magnesium absorption in the spectra of background quasars. The Big Ring sits in the same redshift slice as, and only twelve degrees from, the Giant Arc the same team reported in 2022, and exceeds the roughly 370 megaparsec scale beyond which the standard cosmological model expects the universe to look statistically smooth.

The discovery was visual and serendipitous, made while revisiting the Giant Arc field with a newer, denser absorber catalogue. The team then works to rule out mundane explanations. Every absorption system in the ring is verified by eye in the raw spectra. Critically, when the same background quasars are used to map absorption at a neighboring distance slice, the ring vanishes — demonstrating the pattern belongs to the intervening matter at one specific distance, not to the arrangement of the quasar probes or the survey's geometry. Bright galaxies-hosting-quasars within the slice and clusters from an independent DESI catalogue trace similar filamentary paths, providing corroboration from tracers with entirely different systematics.

The statistical case is deliberately multi-pronged and honestly uneven. Compactness tests give significances ranging from 2.5 to 5.2 sigma depending on how members are chosen and volumes defined, with the most stable method (minimal-spanning-tree edge lengths) consistently near 4 sigma; the headline 5.2 sigma applies to the visually-chosen member list and is labeled an upper limit by the authors themselves. A field-level clustering test borrowed from epidemiology finds the BR field special compared with four matched control fields, but only at 2 sigma. Rotating the three-dimensional absorber positions reveals the deepest surprise: the "ring" is actually a coil, aligned face-on with our sightline, threaded by a thin flat filament — a morphology the authors argue is inconsistent with the most conventional explanation, a baryon acoustic oscillation shell, and which leads them to float cosmic strings as one exotic possibility.

The key interpretive choice in this summary is separating three claims the paper bundles: that a striking absorber pattern exists at this location (secure), that it constitutes a statistically significant physical overdensity (probable but method-dependent, roughly 4 sigma by the most stable measure), and that it challenges the Cosmological Principle or requires new physics (contested, resting on a definition of "structure" the broader field disputes and on significance tests that don't fully price in visual pre-selection). The reader should carry away that the data quality and artifact controls are genuinely careful — this is not sloppy work — while the inferential leap from "linked pattern larger than 370 Mpc" to "cosmology is broken" is where nearly all the epistemic risk is concentrated.

**Where I'm least confident in this analysis:** the paper's §4.3 (equivalent-width analysis) and §5 (Discussion and conclusions) could not be retrieved — my characterization of the discussion's content, including the framing of the GA+BR system and the cosmic-string and CCC arguments, is reconstructed from the abstract, introduction, and secondary coverage rather than read directly, so any specific probability arguments or additional caveats the authors make there are invisible to me; secondarily, my Nadathur-style framing of the mainstream critique is drawn from the broader literature rather than from responses targeting the BR specifically, and the precise state of that exchange may have evolved.

## 8. Three Crystallized Takeaways

1. Astronomers found a ring of galaxies 1.3 billion light-years across — bigger than the universe's supposed "smoothness scale" — sitting right next to an equally enormous arc they found two years earlier, at the same distance, which is either a profound clue or a warning about the method.

2. In 3D it's not a ring at all: precise gas-absorption redshifts reveal a corkscrew coil that happens to face us head-on — a reminder that every "structure on the sky" is one projection of something we can only see from a single vantage point.

3. The statistics say "unusually crowded" at about 4 sigma, but no test in the paper measures the thing that matters most — how often a homogeneous universe, scanned by human eyes through a sparse web of quasar sightlines, coughs up a pattern this striking by accident.

## 9. Shorter Summary

Astronomers have mapped a ring-shaped collection of galaxies about 1.3 billion light-years across, located 9.2 billion light-years away — the second colossal structure found by the same team in the same patch of sky, close to their earlier Giant Arc. Both exceed the size at which the universe is expected to look uniform, and the pair together poses an even sharper puzzle than either alone.

The structures reveal themselves indirectly. Light from distant quasars passes through gas surrounding intervening galaxies, and that gas removes a telltale pair of wavelengths, stamping each galaxy's precise distance into the quasar's spectrum. The upside is superb depth precision; the downside is that matter is only visible where a quasar happens to shine from behind, making the map inherently patchy. Much of the paper is devoted to proving the ring is not a mirage of that patchiness: every absorption signal was verified by eye, and when the same quasars are used to map a neighboring distance slice, the ring disappears — so the pattern belongs to matter at one distance, not the survey layout. Bright galaxies and an independent cluster catalogue trace similar paths through the same region.

Statistical tests peg the crowding at roughly four sigma by the most stable measure, though estimates range from about two-and-a-half to five sigma depending on assumptions — a spread the authors report openly. The biggest twist comes from the third dimension: rotated in space, the ring is actually a coil, coincidentally facing Earth head-on. That shape argues against the tidiest conventional explanation, a fossil sound-wave shell from the early universe, and leads the authors to mention speculative origins such as cosmic strings.

The caution is equally important. All three giant structures claimed in this field come from one research group using one method, and critics have long argued that connect-the-dots algorithms applied to sparse data can assemble impressively large "structures" even in a perfectly ordinary universe. The pattern in the data looks real; whether it breaks cosmology is a genuinely open fight. Independent mapping of this volume — coming with DESI — should settle it.
