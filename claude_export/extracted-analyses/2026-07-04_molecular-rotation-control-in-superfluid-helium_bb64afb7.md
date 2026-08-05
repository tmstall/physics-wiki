---
source: claude_export
conversation_uuid: bb64afb7-aa7c-4364-9cd9-540e67378675
title: "Molecular rotation control in superfluid helium"
created_at: 2026-07-04T16:13:23.225667Z
updated_at: 2026-07-04T16:16:11.278704Z
tier: A
score: 27
n_messages: 2
---

# Molecular rotation control in superfluid helium

## Human

Analysis paper

Control of Molecular Rotation in Helium Nanodroplets with an Optical Centrifuge
Ian MacPhail-Bartley
1, Alexander A. Milner
1, Frank Stienkemeier
2, and Valery Milner
1,*

Phys. Rev. Lett. 136, 033002 – Published 22 January, 2026

DOI: https://doi.org/10.1103/5jnj-97vs

22 total citations on Dimensions.

Abstract
We experimentally demonstrate that the rotation of molecules embedded in helium nanodroplets can be controlled with an optical centrifuge, allowing for the study of molecular dynamics inside the strongly interacting many-body environment of superfluid helium at variable levels of rotational excitation. By doping the droplets with dimers of nitric oxide, (NO)2, and measuring the degree of their centrifuge-induced alignment as a function of time, we show both the forced in-field rotation of molecules in a continuous range of frequencies, as well as the field-free resonant rotation with a long nanosecond-scale decay. The ability to control and monitor the rotational dynamics of molecular rotors inside the superfluid medium may shed new light on superfluidity and the interaction of superfluids with defects at the atomic level.

Physics Subject Headings (PhySH)
Coherent control
Rotational states
Superfluidity
Ultrafast phenomena
Helium-4 superfluids
Physics logo purple small
synopsis

Spinning Molecules Suspended in Superfluid
Published 22 January, 2026
A technique for spinning up molecules in a gas has now been adapted to work with superfluid helium as the host medium.

See more in Physics

Authorization Required
We need you to provide your credentials before accessing this content.
Log in via your institution
If your institution provides access using Shibboleth/OpenAthens log in.

Log in via APS Member Subscription
If you have a personal subscription through your APS membership please log in.
Starting August 1, 2019 APS member subscribers will need to log in using your member credentials instead of your APS Journal Account.
APS Member Log In
Other Options
Buy Article »
Log in with APS Journals Account
Log in with username/password provided by your institution
Get access through a U.S. public or high school
References (Subscription Required)
Outline
Information
Purpose Led Publishing - Science is our shareholder
APS Logo

Authors

Reviewers

Librarians

Students

Connect
ISSN 1079-7114 (online), 0031-9007 (print).
©2026 American Physical Society. All rights reserved.
Physical Review Letters™ is a trademark of the American Physical Society, registered in the United States, Canada, European Union, and Japan. The APS Physics logo and Physics logo are trademarks of the American Physical Society. Information about registration may be found here. Use of the American Physical Society websites and journals implies that the user has read and agrees to our Terms and Conditions and any applicable Subscription Agreement.

## Assistant

| retrieving full text

Analyzing | Framework v3.7.1 | full text retrieved

**Access Status**
Full paper: retrieved from arXiv (2509.02913, HTML full text — identical to the PRL 136, 033002 version)
Abstract: retrieved (APS page + arXiv)
Supplementary material: APS Physics Synopsis noted; companion paper arXiv:2507.12689 (the centrifuge design paper) consulted for context
Analysis basis: full text

Pre-read note: this is a short PRL Letter, but it's a substantive experimental demonstration with real many-body physics stakes, not a narrow methods note — proceeding directly to full analysis.

---

## 1. Punchy Title & One-Sentence Hook

**A Synchronous Motor Inside a Superfluid: Spinning Single Molecules at Dial-a-Frequency Inside Helium Nanodroplets**

For the first time, an optical centrifuge has successfully grabbed and spun molecules embedded in superfluid helium — turning a single molecule into a tunable-frequency stirring rod for probing superfluidity at the atomic scale.

## 2. Big-Picture Context

Superfluid helium is the textbook macroscopic quantum fluid, but its microscopic behavior — how it responds to a single moving defect at the atomic scale — is still not fully understood. Helium nanodroplets (here, ~3000 atoms of $^{4}$He at 0.4 K) offer a beautiful laboratory: drop a single molecule inside, and the molecule becomes a nanoprobe of the surrounding quantum liquid. Decades of infrared spectroscopy established that embedded molecules often rotate surprisingly freely, but with renormalized rotational constants — the helium partially "dresses" the rotor, increasing its effective moment of inertia. Crucially, how strongly a molecule couples to the bath depends on whether its rotational energy overlaps the superfluid's collective excitation spectrum, especially the roton region around 180 GHz where the density of states piles up.

The problem: IR spectroscopy only sees the lowest rotational states, because at 0.4 K almost everything sits in the ground state. To map the frequency dependence of molecule–superfluid coupling, researchers had to swap in different molecules with different rotational constants — which changes everything else about the probe at the same time. Time-resolved wave-packet methods (femtosecond kick pulses) added dynamics, but suffer a fundamental confound: they can't separate rotational *decoherence* from rotational *energy relaxation*, because both kill the coherent signal.

The optical centrifuge — a laser pulse whose linear polarization rotates, dragging the molecule's most polarizable axis along with it — was the obvious tool to fix this, since it lets you dial in a single rotation frequency. But previous attempts in droplets failed: conventional centrifuges accelerate at ~100 GHz/ps toward terahertz terminal frequencies, and a helium-dressed molecule, with its enormously enhanced effective centrifugal distortion, simply gets flung off the merry-go-round. This paper deploys a newly developed constant-frequency centrifuge (cfCFG) — zero acceleration, tunable below 100 GHz — and shows it works.

**Paper Type & Stakes:** This is an experimental technique-demonstration Letter — the first successful application of an optical centrifuge to molecules inside helium nanodroplets — whose stakes are a new, general-purpose method for probing superfluidity with a single tunable molecular rotor.

**Prior Belief Check:** The findings align cleanly with mainstream consensus. The measured rotational-constant renormalization (factor of 1.9) and the long nanosecond-scale decay for rotational energies well below the roton are exactly what the field expects from twenty years of droplet spectroscopy. Experts would not be surprised by the numbers; what's notable to them is that the technique works at all, given documented prior failures. This is an enabling, incremental-but-important result — a new door opened, not a consensus overturned.

**Replication & Convergence Note:** This is a single-group result (UBC, with Freiburg collaboration on droplet expertise) with no independent replication of centrifuge spinning inside droplets; independent confirmation would look like another droplet-alignment group (e.g., the Aarhus/Stapelfeldt community) reproducing controlled in-field rotation and the resonant decay with a different molecule and apparatus — important here because the interpretation of the alignment signal relies on this group's specific centrifuge calibration.

## 3. Necessary Background Crash-Course

**Helium nanodroplets.** Expand high-pressure helium through a cold 5-micron nozzle and it condenses into droplets of a few thousand atoms, self-cooled by evaporation to 0.4 K — below the superfluid transition. Fly the droplet beam through a pickup cell with a trace of dopant gas, and droplets swallow single molecules, cooling them instantly to the droplet temperature.

*Analogy:* A droplet is like a flying cleanroom-plus-cryostat — a self-refrigerating container that isolates one molecule in the gentlest, coldest matrix known.
*Breaks when:* you assume the matrix is passive. Unlike an inert cage, the superfluid actively dresses the molecule — dragging effective mass, renormalizing its rotational constants, and opening dissipation channels when frequencies match its collective modes.

**Optical centrifuge.** Two counter-chirped, oppositely circularly polarized laser pulses interfere to make a linearly polarized field whose polarization axis rotates. The field induces a dipole in the molecule; the induced dipole torques the most polarizable molecular axis into alignment, and the axis follows the rotating polarization.

*Analogy:* It's a synchronous motor — the laser field is the rotating stator field, and the molecule is a rotor that phase-locks to it, provided the field doesn't accelerate faster than the rotor can follow.
*Breaks when:* you push to slip dynamics. In a real induction motor, a rotor that falls behind still gets torque from slip; a molecule that falls behind the centrifuge simply detaches — capture is adiabatic-or-nothing, and the dressed pendular states have no classical slip mechanism.

**Constant-frequency centrifuge (cfCFG).** The conventional centrifuge chirps the rotation rate upward violently. The cfCFG instead splits one chirped pulse in a Michelson interferometer; the delay between arms fixes a constant instantaneous frequency difference between the two recombined pulses, so the polarization rotates at one steady, tunable frequency (here 8–17 GHz).

*Analogy:* Conventional centrifuge = flooring the accelerator from 0 to redline; cfCFG = cruise control locked at a chosen RPM.
*Breaks when:* you assume perfect cruise control — third-order dispersion leaves a residual ~4 GHz frequency drift over the pulse, which sets the effective linewidth of the technique.

**Rotational decoherence vs. energy relaxation.** A rotational wave packet has both a phase relationship among its components and an energy content. Losing phase coherence (dephasing) and losing energy to the bath are physically distinct processes.

*Analogy:* This is exactly the T2 versus T1 distinction from quantum information — phase noise versus amplitude decay in a qubit or an oscillator.
*Breaks when:* you map it one-to-one onto two-level-system language — a rotor in a many-body bath has a ladder of states, anisotropic coupling, and the "T1" measured here is the decay of planar rotational alignment, not a single-state population lifetime.

**Roton spectrum.** Superfluid helium's elementary excitations follow a dispersion curve with a minimum — the roton — around 180 GHz, where the density of states is very high. A rotor whose frequency sits near that region couples strongly and dissipates fast; well below it, the superfluid has almost nothing to absorb the energy into.

*Analogy:* Driving a transmission line below its cutoff frequency — signals in the stopband barely couple into the medium and propagate losslessly; hit the band and energy pours in.
*Breaks when:* you take "stopband" as literally zero coupling — even far below the roton, phonon emission and droplet-surface modes give finite, if slow, relaxation.

**Central analogy for this paper:** a synchronous motor phase-locked inside a quantum fluid.

## 4. Core Technical Explanation

The team generates droplets of ~3000 $^{4}$He atoms (30 bar through a 5 μm nozzle at 18 K), dopes them with nitric oxide dimers, (NO)₂, and crosses the droplet beam with two collinear laser pulses: the cfCFG (peak intensity ~2×10¹² W/cm²) and, at a controllable delay, a 120-fs probe pulse (~5×10¹⁴ W/cm²) that Coulomb-explodes the dimer. A velocity-map-imaging spectrometer records where the NO⁺ fragments fly; the angular distribution of fragments reveals where the molecular axes pointed at the instant of explosion. The standard alignment metric is the average of cos-squared of the fragment angle relative to the centrifuge's rotation plane — call it the alignment score. Isotropic tumbling gives 0.5; axes confined to the rotation plane push it above 0.5.

They chose (NO)₂ cleverly, for two engineering reasons: the dimer doesn't survive at room temperature, so there's zero gas-phase background contaminating the signal — only dimers assembled cold inside droplets exist; and NO⁺ fragments are heavy enough not to be badly scattered by helium atoms during the explosion, which would smear the angular information (a known failure mode for light fragments).

**Result 1 — in-field forced rotation at arbitrary frequency.** With the centrifuge tuned to 8.5, 13, and 17 GHz, the alignment score oscillates in time at twice the centrifuge frequency — 18.1, 27.2, and 36.2 GHz respectively. The factor of two is geometric: the alignment metric can't tell "pointing left" from "pointing right," so it peaks twice per revolution. These oscillations are direct, time-resolved proof that the dimers are phase-locked to the rotating field, at frequencies that need not match any molecular resonance — the field-dressed "pendular states" follow the drive like a driven pendulum. The oscillation amplitude shrinks as frequency rises: fewer molecules get captured when the field's rotation frequency sits further from the molecules' initial standstill. And critically, when the centrifuge frequency is off-resonance, the alignment relaxes back to isotropic as the pulse ramps off — the molecule is adiabatically returned to its ground state, like a synchronous motor spun down gently to rest.

**Result 2 — resonance mapping.** When twice the centrifuge frequency matches a rotational transition, a two-photon Raman process deposits real population in the excited state, and the rotation *outlives the pulse*. Scanning the centrifuge frequency and measuring the alignment score 550 ps after the pulse reveals a single resonance at 8.4 GHz — the J=0 to J=2 transition (the only one accessible from the ground state at 0.4 K). From this they extract the in-droplet rotational constant: 0.092 inverse centimeters, a factor of 1.9 smaller than the gas-phase value. The helium drags along with the rotor, nearly doubling its effective moment of inertia — squarely in line with renormalizations seen across many molecules. Note what just happened methodologically: they measured a rotational constant *without any IR transition* — the centrifuge scan itself is the spectrometer.

**Result 3 — direct energy-relaxation lifetime.** Parking the centrifuge on the 8.4 GHz resonance and following the alignment score out to 3.3 ns shows it rising to ~0.6 during the pulse, then settling to ~0.52 and decaying exponentially. Fitting

$$S(t) = 0.5 + A\, e^{-t/\tau}$$

Symbol definitions:
- $S(t)$ : the alignment score (average of cos² of fragment angle) at probe delay $t$
- $A$ : amplitude of the persistent planar alignment just after the pulse
- $\tau$ : decay time constant of rotational energy
- 0.5 : the isotropic asymptote (no preferred plane)

What this actually means: after the drive shuts off, the molecule keeps spinning in the plane the centrifuge defined, and the "signal" is simply how long that plane persists — like watching how long a gyroscope's spin plane survives in a viscous-but-nearly-frictionless bath. The fitted lifetime is $\tau$ = 3200 ± 300 ps.

The conceptual keystone: unidirectional rotation makes the measurement immune to dephasing. Even after the wave packet's components lose mutual phase (decoherence), a unidirectionally spinning rotor keeps its axis confined to the rotation plane — the "donut" distribution — so the alignment score stays above 0.5 for as long as the rotational *energy* survives. The score decays only when energy actually drains into the helium. That's what previous kick-pulse experiments fundamentally couldn't do: their signal died at the decoherence rate, whichever process was faster. This experiment reads T1 through a channel that T2 can't touch.

The 3.2 ns lifetime is long, and consistent with the transmission-line picture: at ~17 GHz rotational energy, the rotor sits far below the roton stopband edge, so the superfluid has very little to absorb into.

**Assumption Audit**

- **Watch:** Reader likely assumes "optical centrifuge" means the trademark superrotor regime — spinning molecules up a ladder to extreme J. The paper actually drives at most a single J=0→2 transition; the achievement is *frequency control at low excitation*, not extreme spinning. The ladder-climbing version in droplets is explicitly future work.
- **Watch:** Reader likely assumes the 3.2 ns decay is the coherence lifetime, comparable to earlier droplet wave-packet studies. The paper actually measures energy relaxation, deliberately constructed to survive decoherence — the two timescales are different observables, and conflating them undoes the paper's central point.
- **Watch:** Reader likely assumes the factor-of-1.9 rotational-constant renormalization was cross-checked spectroscopically. It actually rests entirely on assigning the single 8.4 GHz peak to J=0→2 using the near-prolate energy formula with K conserved — a well-motivated but single-line assignment with no second transition to corroborate it in this dataset.
- **Watch:** Reader may assume the alignment score directly reports 3D alignment. It's a 2D projection from Coulomb-explosion fragment imaging, with known distortions from fragment–helium scattering; the NO⁺ mass mitigates but does not eliminate this, so absolute values (0.6, 0.52) carry more systematic uncertainty than the timescales do.

## 5. What's Genuinely New or Clever

**New to the field (1): a centrifuge that works inside superfluid helium.** Prior attempts (Aarhus, and this group's earlier work) failed because conventional centrifuges accelerate too hard and terminate too high for a helium-dressed rotor with enormous effective centrifugal distortion. The enabling trick is the constant-frequency centrifuge — zero acceleration, tunable in the 8–17 GHz window — built by splitting a chirped pulse in a Michelson interferometer rather than a pulse shaper. This converts a twenty-five-year-old gas-phase tool into a superfluid probe.

**New to the field (2): reading energy relaxation through a dephasing-proof channel.** Using the planar confinement of unidirectional rotation as the observable cleanly separates rotational energy decay from decoherence — the first time-domain measurement in droplets where the two are not entangled. As a bonus, scanning the centrifuge frequency doubles as a spectrometer for molecules with no usable IR transitions, demonstrated by extracting the in-droplet rotational constant of (NO)₂.

## 6. Limitations & Open Questions

- Only one molecule, one transition (J=0→2 at 8.4 GHz) was measured — the frequency-dependence program that motivates the whole approach (mapping coupling up toward the roton at 180 GHz) remains undone. (A) Consensus — the paper itself frames the ultra-slow ladder-climbing centrifuge as work in progress, and one data point cannot map a dispersion curve. (paper, concluding paragraphs)

- The resonance linewidth in the frequency scan is attributed primarily to the centrifuge's residual ~4 GHz frequency drift from third-order dispersion, not to the molecule–helium system itself; intrinsic linewidth information is therefore instrument-limited. (A) Consensus — the paper states this attribution explicitly, and an instrument-limited linewidth is a standard, uncontroversial limitation. (paper, Fig. 3 caption)

- Contributions from droplet-size inhomogeneity and possible isomer or cluster impurities to the lineshape and to the fitted decay are not disentangled; pickup statistics are tuned to suppress larger clusters but not characterized in this Letter. (C) Speculative — the paper does not address these systematics beyond citing standard doping practice, and I am extrapolating from general droplet-beam experience; a specialist may know these are negligible here. (analyst inference)

- The exponential fit fixes the asymptote at exactly 0.5 (full isotropy); any long-lived residual anisotropy or slow secondary decay channel would bias τ. (C) Speculative — the fit choice is stated but not stress-tested in the text, and I am flagging it as a fitting-model sensitivity rather than a known problem. (analyst inference)

- Quantitative alignment values from Coulomb-explosion imaging in helium are degraded by fragment scattering off helium atoms — a known systematic for this detection scheme, mitigated but not removed by using heavy NO⁺ fragments. (A) Consensus — this is an established critique with dedicated literature (nonaxial recoil deconvolution), and the paper acknowledges the effect as its reason for choosing (NO)₂. (broader literature)

Open questions for the next 12–24 months: extend the frequency range toward the roton with the ultra-slow ladder-climbing centrifuge (already in development, arXiv:2507.12689); measure state-by-state lifetimes with one molecule across the excitation spectrum; and test whether sustained unidirectional stirring from within nucleates quantized vortices detectable by diffraction imaging.

## 7. Detailed Summary & Explanation

The experiment answers a deceptively simple question: can you make a molecule inside superfluid helium spin at a frequency of your choosing, and then watch how the superfluid takes that rotational energy back? Both halves had resisted twenty years of effort. Frequency-domain IR spectroscopy could only interrogate the couple of rotational states thermally accessible at 0.4 K, forcing researchers to compare different molecules to sample different frequencies — changing the probe and the question simultaneously. Time-domain kick-pulse experiments created rotational wave packets but could not tell whether the signal died because the packet dephased or because the energy actually drained into the helium.

The authors solve the first half with hardware: a constant-frequency optical centrifuge that rotates its linear polarization at a steady, tunable rate below 100 GHz, gentle enough that the helium-dressed nitric oxide dimer — whose effective moment of inertia is nearly doubled by the co-rotating helium — can stay phase-locked. Timed snapshots via Coulomb explosion show the alignment signal oscillating at exactly twice the drive frequency at three different settings, the smoking gun of forced synchronous rotation. Off resonance, the molecule is returned adiabatically to rest when the field ramps off; on resonance — at 8.4 GHz, matching the transition from the ground rotational state to the second excited one — real population transfers, and the molecule keeps spinning after the light is gone.

They solve the second half with geometry: a unidirectionally spinning molecule keeps its axis in the rotation plane even after quantum phase coherence is lost, so the persistence of that planar confinement reads out energy content, not phase. The measured lifetime is 3.2 nanoseconds — long, because at these frequencies the superfluid's excitation spectrum offers almost nothing to decay into, far below the roton region near 180 GHz where dissipation should turn on sharply.

Why frame the summary this way? The interpretive choice is to present this as a *separation-of-observables* achievement rather than a spectroscopy result. The numbers (the renormalization factor, the lifetime) confirm expectations; the framing that matters is that frequency control and dephasing-immune energy readout now exist in the same apparatus, which is what converts droplet-embedded molecules from passive spectroscopic subjects into active, steerable probes of superfluidity. The reader should take away the method and its reach, with the specific (NO)₂ numbers as the proof of function.

**Where I'm least confident in this analysis:** the pendular-state physics underlying in-field capture and adiabatic return — how the dressed-state ladder behaves at these intensities and why capture efficiency falls off with drive frequency in the way Fig. 2 shows — is compressed in the Letter to citations, and my plain-language "synchronous motor" account of the capture-versus-detachment boundary may be smoothing over genuinely quantum features of the dressed-state dynamics that the cited alignment literature treats carefully.

## 8. Three Crystallized Takeaways

1. Physicists spun a single molecule inside a droplet of superfluid helium at a dial-in frequency for the first time — earlier attempts failed because the laser "motor" accelerated too hard for a molecule wearing a coat of helium.

2. The clever readout: a molecule spinning in one direction keeps its axis in one plane even after its quantum phases scramble, so watching that plane fade measures pure energy loss to the superfluid — 3.2 nanoseconds here, long because the superfluid has almost no excitations at that frequency to absorb it.

3. The helium coat nearly doubles the molecule's effective rotational inertia — and the centrifuge itself measured this, acting as a spectrometer for molecules that ordinary infrared spectroscopy can't see.

## 9. Shorter Summary

Superfluid helium — the frictionless quantum liquid — is still mysterious at the atomic scale. One of the best ways to study it is to embed a single molecule in a nanodroplet of a few thousand helium atoms, cooled to 0.4 kelvin, and watch how the molecule's rotation is affected by, and affects, the quantum fluid around it. But the standard tools had hard limits: infrared spectroscopy could only see the very lowest rotational states, and laser kick-pulse experiments couldn't distinguish two fundamentally different processes — the scrambling of quantum phase (decoherence) and the actual loss of rotational energy to the helium.

This experiment introduces a fix for both. The team used a newly designed "constant-frequency optical centrifuge" — a laser pulse whose polarization rotates at a steady, tunable rate — to grab nitric oxide dimers inside helium droplets and spin them at chosen frequencies. Earlier centrifuges failed at this because they accelerated too violently; a molecule dressed by co-rotating helium simply flew off the ride. The gentle, zero-acceleration version keeps the molecule locked to the field, and the data show it cleanly: the alignment signal oscillates at exactly twice the drive frequency, at every frequency they chose.

When the drive frequency matched the molecule's lowest rotational transition, the rotation outlasted the laser pulse. Because a molecule spinning in one direction keeps its axis in one plane even after quantum phases scramble, the persistence of that plane measures pure energy loss. The rotation survived 3.2 nanoseconds — a long time, because at these low frequencies the superfluid has almost no excitations available to absorb the energy. As a bonus, the resonance frequency itself revealed that the helium nearly doubles the molecule's effective rotational inertia, providing a new way to measure rotational properties of molecules invisible to infrared spectroscopy.

The result opens a program: spin one molecule at many frequencies, map exactly where the superfluid starts absorbing energy, and perhaps even stir up quantized vortices from inside a droplet — probing superfluidity one controlled rotation at a time.
