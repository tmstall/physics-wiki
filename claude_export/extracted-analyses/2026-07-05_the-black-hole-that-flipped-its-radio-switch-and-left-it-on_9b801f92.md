---
source: claude_export
conversation_uuid: 9b801f92-baf1-45a0-8b0b-d0cf4ede1682
title: "The Black Hole That Flipped Its Radio Switch — and Left It On"
created_at: 2026-07-05T21:38:33.305946Z
updated_at: 2026-07-05T22:16:38.492046Z
tier: A
score: 259
n_messages: 2
---

# The Black Hole That Flipped Its Radio Switch — and Left It On

## Human

Analyze this paper

## Assistant

# 1. Punchy Title & One-Sentence Hook

**The Black Hole That Flipped Its Radio Switch — and Left It On**

A small, unremarkable nearby galaxy's central black hole quietly boosted its radio output more than 23-fold sometime between 2000 and 2017, has held that new level rock-steady for over eight years, and left essentially no fingerprint anywhere else in the electromagnetic spectrum — making it the first known long-duration "radio changing-look" AGN and a genuine puzzle for jet-launching physics.

---

# 2. Big-Picture Context

**Paper Type & Stakes:** This is an observational discovery-characterization paper — a multiwavelength case study of a single object that coins a new class term ("radio changing-look AGN") and works through a systematic elimination of outburst scenarios. What's at stake is our understanding of how radio jets switch on around supermassive black holes, particularly the low-mass, fast-growing kind that dominated the early Universe.

Active galactic nuclei have historically been filed into tidy bins: radio-loud or radio-quiet, type 1 or type 2, blazar or Seyfert. Over the last decade, the "changing-look" phenomenon has been dismantling that filing system. Optical changing-look AGN swap their spectroscopic type as broad emission lines appear or vanish; X-ray changing-look AGN swing between absorbed and unabsorbed states. What had *not* been seen is an AGN switching between radio-quiet and radio-loud and *staying* there — the classification everyone assumed was the most stable of all, because it's tied to whether the black hole launches a relativistic jet.

The object here, SDSS J1105+1452, is a narrow-line Seyfert 1 (NLS1) at redshift 0.12 — a class hosting small black holes (here roughly 3–4 million solar masses) accreting near their Eddington limit. NLS1s matter beyond their own zip code: they're the local, observable analogs of the rapidly growing black holes JWST is now finding in the early Universe. In 1999 this galaxy was a barely-detectable 1.4 mJy radio source. By December 2017 it was at ~39 mJy and radio-loud, and every observation since — this paper adds Effelsberg, ATCA, LOFAR, and ASKAP data through January 2026 — shows it parked at that high state with ~10% constancy. NLS1s as a class vary in the radio by less than a factor of 2, up to ~5 in rare jetted cases at high frequency. A factor of >23, at *low* frequency, sustained for >8 years, is simply outside the known catalog of AGN behavior.

The team (led by the discoverers of the outburst, GKK25) brings the first X-ray spectrum, first UV/optical SEDs, first simultaneous radio SEDs, and deep archival mining back to the 1950s, then runs the gauntlet of explanations: lensing, absorption variability, binary black hole effects, tidal disruption, first-time AGN ignition, blazar beaming, and accretion-rate changes. Their verdict: an accretion-rate change that nonlinearly amplified the jet, plausibly via magnetic flux accumulation near the horizon.

**Prior Belief Check:** The *observation* genuinely surprises experts — not because radio variability is new, but because this specific combination (high amplitude, low-frequency, near-constant, near-decade duration, in a low-mass NLS1) contradicts the expectation that radio-loudness is a quasi-permanent property and that big radio flares decay on months-to-years timescales. The *interpretation*, however, sits comfortably inside mainstream disk–jet coupling theory (Blandford–Znajek jets, magnetically arrested disks). So: a surprising phenomenon explained with consensus physics. The paper is a first-of-its-kind case study, not a statistical result — important to hold in mind when weighing the proposed "new class."

**Replication & Convergence Note:** This is a single-collaboration result with no independent analysis yet, though it's partially self-verifying: the flux history is stitched from public survey archives (FIRST, VLASS, RACS, LOFAR) that anyone can re-measure, which protects the core claim (the outburst happened and persists) far better than the interpretation (accretion-driven jet ignition). Independent confirmation would look like VLBI imaging resolving a compact young jet at parsec scales, and independent radio monitoring reproducing the flux constancy — both would materially raise confidence that this is jet physics rather than something stranger.

---

# 3. Necessary Background Crash-Course

**NLS1 galaxies.** These host the smallest supermassive black holes among active galaxies (10⁶–10⁷ solar masses) accreting close to the Eddington limit — the luminosity at which radiation pressure pushing out balances gravity pulling in.

*Analogy:* An NLS1 is a small chip overclocked to its thermal design power — a modest processor running as hard as physics allows, while big quasars are server-grade silicon loafing at 30% utilization. Studying it tells you what "maximum sustained throughput" looks like, which is exactly the regime early-Universe black holes grew in.

**Breaks when:** you treat Eddington as a hard shutdown. It's not a TDP throttle — super-Eddington accretion is possible (photon trapping, non-spherical geometry), and the limit only strictly applies to spherical, steady accretion.

**Radio-loudness and the "changing-look" idea.** Radio-loudness measures jet-powered synchrotron emission relative to disk emission; only ~7% of narrow-line objects are radio-loud. It was long treated as an intrinsic, stable property — you either have a jet or you don't.

*Analogy:* Classifying AGN by radio-loudness was like classifying devices by their spec sheet. Changing-look events reveal the spec sheet was actually a runtime state: the RF transmitter has a power switch nobody knew about, and this paper catches one being flipped on and left on.

**Breaks when:** you take the binary seriously — radio-loudness is a continuum with a messy, absorption-sensitive definition, and this source sits at log R_X = −1.6, radio-loud but nowhere near blazar territory.

**Peaked radio spectra (GPS sources) and spectral turnover.** This object's radio spectrum rises up to ~2.1 GHz and falls steeply above it — the shape of "gigahertz-peaked spectrum" sources, interpreted as *young*, compact jets. The low-frequency cutoff arises from synchrotron self-absorption (SSA: the plasma is opaque to its own low-frequency emission), free-free absorption (FFA: external ionized gas blocks it), or an intrinsic lack of low-energy electrons.

*Analogy:* The turnover is a high-pass filter on the jet's broadcast. SSA is the transmitter jamming itself — its own electron plasma reabsorbs low frequencies before they escape, like a signal that can't get out of its own crowded near field. FFA is attenuation in the transmission medium instead — lossy cable between transmitter and receiver. Diagnostically it matters which, because SSA's cutoff frequency encodes source *size* (smaller = higher turnover), while FFA's encodes the *environment's* density.

**Breaks when:** you assume there must be a filter at all — the paper explicitly notes the low-frequency decline could be intrinsic to the injected electron energy distribution, i.e., the transmitter simply never generated the low frequencies.

**Blandford–Znajek jets and the magnetically arrested disk (MAD).** Jets are powered by rotational energy extracted from a spinning black hole threaded by ordered poloidal magnetic field. Jet power scales as the *square* of both the accumulated magnetic flux and the spin. When inflowing gas drags in enough coherent field, the magnetic pressure begins to choke the inflow — the MAD state — and jet efficiency jumps dramatically at nearly fixed radiated luminosity.

*Analogy:* The jet is a transistor. The spinning black hole is the power rail; the accretion disk is the current source; the net poloidal magnetic flux is the *gate voltage*. Small changes at the gate produce disproportionate changes in output because the device response is nonlinear — and crossing into MAD is like driving the gate past threshold: the channel opens and output surges even though the supply barely changed.

**Breaks when:** you push terminal independence. In a transistor the gate is electrically isolated from the channel; here the "gate" flux is delivered *by the same accretion flow* that supplies the power, so gate and source are coupled — you can't dial them independently, which is exactly why MAD transitions are rare and episodic.

**Central analogy for this paper: the jet as a flux-gated transistor.**

---

# 4. Core Technical Explanation

I've pulled the two figures that carry the paper's core evidence:

**Figure 6 (first image)** is the high-state radio SED: flux density versus frequency from 0.1 to ~20 GHz, fit with a log-space parabola peaking at 2.1 GHz — the GPS-like shape that anchors the "young/compact jet" reading. **Figure 3 (second image)** is the radio light curve: the lone red diamond at lower left is the 1999.96 FIRST low state (1.4 mJy); everything after December 2017 sits on a flat plateau near 30–45 mJy. The flatness of that plateau, across nine years and half a dozen instruments, is the single most constraining fact in the paper.

The authors' work divides into four moves, which I'll walk through thematically rather than in the paper's section order.

**Move 1 — Nail down what the source is.** They confirm the NLS1 classification three independent ways, because everything downstream depends on the black hole being small. Single-epoch scaling relations using the H-beta line width and luminosity give a black hole mass of 4.4 million solar masses; the host galaxy's stellar velocity dispersion gives 2.8 million — consistent within the standard half-decade uncertainty of these methods. Both imply the black hole is accreting at 20–30% of its Eddington limit. The new Swift X-ray spectrum is soft (photon index 2.5), exactly the steep spectrum NLS1s are known for. Three fingerprints, one verdict: this is a genuine small-black-hole, high-throughput system, so the radio behavior can't be blamed on misclassification.

**Move 2 — Characterize the outburst.** New Effelsberg and ATCA observations give the first simultaneous radio SEDs beyond a few GHz. The spectrum rises steeply below the peak (spectral index +1.6 in the optically thick part), turns over at 2.1 GHz, and falls steeply above (−1.3), with non-detections above 18 GHz. The 4.85 GHz luminosity is 7 × 10⁴⁰ erg per second. Applying the empirical anticorrelation between GPS source size and turnover frequency, a 2 GHz peak implies a jet of order 100–200 parsecs — but a jet launched only years ago should be ~10 parsecs and peak *above* 10 GHz, a tension they flag and partially defuse (a wider-angle outflow or weaker magnetic field shifts the peak down).

**Move 3 — Establish what *didn't* change, which is the paper's real forensic muscle.** They mine every archive available: ASAS-SN, ZTF, Catalina, SDSS photometry, WISE/NEOWISE infrared, and photographic plates back to 1949. Result: no systematic optical or IR change since 2003 at all. The X-rays show only a factor-2 difference between ROSAT (1990) and Swift (2025). Absorption is ruled out as a hider of the trigger — the Balmer decrement of 3.3 is nearly the dust-free recombination value, and the X-ray fit needs no column beyond the Milky Way foreground. They also kill the "it's star formation" escape route: the measured star formation rate of 2 solar masses per year predicts radio emission 15 times *below* even the 1999 low state. Whatever happened, it happened to the AGN, and it either happened before 2003 or produced no disk signature at all. One caveat they own honestly: the photographic plates show the galaxy varied by at least a factor 6.8 in blue light sometime between the 1950s and 1990s, and the ROSAT state was brighter — so an early disk event followed by a *delayed* radio turn-on remains open.

**Move 4 — The elimination tournament.** Lensing: no foreground galaxy in deep imaging, no second redshift system in the spectrum — out. Neutral-hydrogen absorption variability (the low state was the anomaly): 21 cm absorption at this redshift lands at 1.25 GHz and can't reach the observed bands without absurd velocity dispersions, and the 4.85 GHz band was *also* faint in the 1980s — out. Free-free absorption clearing: requires an implausibly sharp-edged absorber clearing across a light-years-wide jet within decades, predicting spectral evolution that isn't seen — strained to breaking. A new self-absorbed blob: demands the spectral peak migrate from ~10 GHz to 2 GHz in years when known GPS sources take centuries — strained. Binary black hole coalescence with spin flip: attractive on paper (fast for low-mass black holes, naturally redirects the jet) but the host shows zero merger signatures — shelved for lack of evidence. Tidal disruption event: known radio TDEs peak 1–3 years post-disruption and *decline*; this source has been flat for 8+ — disfavored, though a rare giant-star disruption with slow debris circularization can't be fully excluded. First-ever AGN ignition: dead on arrival, because the 2005 SDSS spectrum shows a mature narrow-line region requiring thousands of years of prior illumination, and the 1999 radio detection means a jet already existed. Blazar flaring: wrong variability pattern (blazars flicker on days-to-months, they don't plateau) and wrong spectrum.

**The survivor: an accretion-rate change amplified by magnetic flux.** The elegant problem is a mismatch of amplitudes — X-rays changed by maybe a factor of 2, radio by a factor of 20+. Their reconciliation stacks two nonlinearities. First, jet power in Blandford–Znajek-type models:

$$P_{\rm jet} \propto \Phi_{\rm BH}^{2}\,\Omega_{\rm H}^{2}$$

Symbol definitions:
- $P_{\rm jet}$ : total kinetic power carried by the jet (erg/s)
- $\Phi_{\rm BH}$ : net poloidal magnetic flux threading the black hole horizon
- $\Omega_{\rm H}$ : angular rotation rate of the horizon (set by black hole spin)

What this actually means: jet output responds to the *square* of the gate variable — double the ordered magnetic flux through the horizon and you quadruple the jet power, with spin held fixed. This is the transistor's transconductance curve, not a linear resistor.

Second, the mapping from jet power to observed centimeter-band radio luminosity is itself sublinear (empirically, jet power scales as radio luminosity to the ~0.7–0.8 power, from X-ray cavity calibrations). Run the chain backwards: a 20-fold radio brightening needs only a 6–9-fold jet power increase, which needs only a factor 2.4–3 increase in magnetic flux. That's the punchline — a modest, plausibly invisible rearrangement of the disk's magnetic field can produce an order-of-magnitude radio transition with *no* order-of-magnitude change in accretion rate. Physically, such flux growth happens if the inner disk crosses from a regime where turbulent diffusion shreds incoming field to one where advection wins and field piles up toward the MAD threshold. The rarity of these events then has a natural reading: most accretion episodes deliver mixed-polarity field that self-cancels (differential signaling, net zero at the receiver); only occasionally does a sustained polarity imbalance survive the trip inward and drive the gate past threshold.

**Assumption Audit**

**Watch:** Reader likely assumes the triggering accretion-rate change was *observed*. The paper actually never detects it — optical, IR, and X-ray archives show no high-amplitude event since 2003. The accretion-change scenario wins by elimination plus theoretical plausibility, with the trigger pushed before 2003 or into the "radio lags disk" loophole (footnote 28 concedes it's a priori unknown whether an accretion *increase* or *decrease* even triggers the jet).

**Watch:** Reader likely assumes a factor->23 radio brightening means the black hole's energy output jumped 23-fold. The paper's scaling chain says the *kinetic* power rose only 6–9× and the underlying magnetic flux only ~2.4–3× — most of the drama is nonlinear amplification in the readout, not in the engine.

**Watch:** Reader likely assumes "turned radio-loud" implies a beamed, blazar-like jet pointed at us. The paper actually shows the opposite signature set: steep optically-thin spectrum, no rapid variability, log R_X of only −1.6 — consistent with an unbeamed, compact, GPS-like young jet.

**Watch:** Reader likely assumes the >8-year flux constancy comes from one instrument's monitoring. It's actually stitched from heterogeneous surveys and telescopes (VLASS, RACS, Effelsberg, ATCA, ASKAP) with beam sizes spanning 2.5 arcseconds to 2.4 arcminutes; constancy holds at the ~10% level only after excluding one archive-flagged outlier (FLASH) with a known ~13% field-wide calibration error.

---

# 5. What's Genuinely New or Clever

**New to the field, item 1: the phenomenon and its class name.** No AGN — let alone a low-mass NLS1 — has been seen executing a >23-fold, low-frequency, radio-quiet-to-radio-loud transition and then holding a constant high state for 8+ years. The paper defines "radio changing-look" as a category deliberately parallel to optical and X-ray changing-look, and positions this object as its prototype. The duration is the discriminating observable: it single-handedly kills TDE, blazar-flare, and supernova interpretations, which all predict decay.

**New to the field, item 2: the amplitude-mismatch argument.** The cleverest analytical move is quantitative, not observational: chaining the quadratic flux dependence of Blandford–Znajek jet power with the sublinear jet-power-to-radio-luminosity calibration to show a factor ~2.5–3 in magnetic flux suffices for a factor ~20 in radio. This dissolves what looks like a paradox (huge radio change, no disk change) into an expected feature of flux-gated jet launching — and it makes the episodic-MAD picture *testable*, since it predicts these transitions should be rare, long-lived, and largely decoupled from optical variability.

Also quietly clever: using the *absence* of narrow-line region arguments in reverse — the mature NLR proves millennia of prior AGN activity, elegantly executing the "first ignition" scenario with light-travel-time logic alone.

---

# 6. Limitations & Open Questions

**The favored scenario rests on elimination, not positive detection.** No disk-change signature was ever observed; "accretion-rate change" is the last scenario standing rather than one confirmed by data. **(A) Consensus** — the paper itself frames the conclusion as a suggestion and concedes the trigger is unobserved and its sign unknown. (paper §7.5, footnote 28, §8)

**No VLBI constraint yet on jet location and size.** The tightest current size limit is <5.4 kpc from VLASS resolution — three to four orders of magnitude looser than the parsec scales where the young-jet interpretation lives or dies. **(A) Consensus** — the authors explicitly list high-resolution VLBI imaging as the decisive next observation. (paper §8)

**The cavity-power scaling is borrowed from a different regime.** The jet-power-to-radio-luminosity relation was calibrated on X-ray cavities in massive cluster galaxies; applying it to a compact jet in a small spiral is an extrapolation the authors themselves label as illustrative only. **(B) Contested** — reasonable physicists would disagree on whether the 0.7–0.8 exponent transfers at all to this mass and environment regime, and the factor 2.4–3 flux estimate inherits that uncertainty wholesale. (paper §7.6.7)

**Pre-outburst X-ray coverage is two points in 33 years.** ROSAT 1990 and Swift 2023 bracket the entire turn-on window, so an early disk event (hinted by the brighter ROSAT state and the ≥6.8× photographic-plate variability) can be neither confirmed nor excluded, leaving the trigger chronology genuinely open. **(A) Consensus** — acknowledged plainly in the paper as a coverage gap. (paper §7.5)

**The turnover mechanism is undetermined, which undercuts the "young jet" size estimate.** SSA, FFA, and an intrinsic low-energy electron cutoff all remain viable, and they imply different source sizes and ages; the GPS analogy is suggestive, not demonstrated. **(B) Contested** — the paper presents the alternatives without adjudicating, and the size-turnover relation already sits in tension with the outburst's youth. (paper §7.4)

**"Prototype of a new class" from N=1 is premature as sociology, even if apt as physics.** History is littered with single-object classes that dissolved or merged on the second detection; whether SKA-era surveys find a population with shared physics, or a grab-bag of unrelated long transients, is entirely open. **(C) Speculative** — this is my extrapolation from how transient taxonomy has historically evolved, not a critique made in the paper or, to my knowledge, the literature yet. (analyst inference)

Follow-up work for the next 12–24 months writes itself and the authors list most of it: VLBI to resolve the jet, dense radio monitoring to catch a turn-off (turn-off physics would be as diagnostic as turn-on), 21 cm absorption spectroscopy to directly measure cold gas on the line of sight, XMM-Newton spectroscopy to separate soft excess from power law, and new optical spectroscopy to watch for delayed broad-line response.

---

# 7. Detailed Summary & Explanation

SDSS J1105+1452 is a barred spiral galaxy 1.6 billion light-years away hosting a black hole of roughly three to four million solar masses — small by AGN standards — accreting at twenty to thirty percent of its maximum sustainable rate. Its optical spectrum ticks every box of the narrow-line Seyfert 1 class, and the new Swift X-ray data reinforce that classification with a soft, steep spectrum and no sign of obscuring material along the line of sight.

In radio surveys of the 1980s and 1990s, this galaxy was nearly invisible: about one milli-jansky, at the edge of detectability. When the VLA Sky Survey imaged it in December 2017, it had brightened more than twentyfold and crossed into radio-loud territory. This paper's new observations with the Effelsberg 100-meter telescope and the Australia Telescope Compact Array, combined with archival survey data, establish three facts. First, the high state has now lasted at least eight years at essentially constant brightness — behavior no known transient (supernova, tidal disruption, blazar flare) can produce, since all of those rise and then decay. Second, the radio spectrum peaks near 2 gigahertz and falls off steeply on both sides, resembling the spectra of very young, compact jets. Third, nothing else changed: two decades of optical and infrared monitoring show a flat light curve, and the X-ray flux differs from its 1990 level by only a factor of two.

The authors systematically dismantle alternative explanations — gravitational lensing, absorbing clouds moving out of the way, a black hole merger, a star being shredded, the AGN igniting for the first time, a jet pointed at Earth — each failing on specific observational grounds. Their favored picture is that the accretion flow underwent a change that switched the jet into a high-efficiency mode. The key insight is that jet output responds nonlinearly to the magnetic flux delivered to the black hole: because jet power scales as the square of that flux, and observed radio luminosity rises faster than linearly with jet power, a modest increase in accumulated magnetic field — merely a factor of two-and-a-half to three — suffices to explain the entire twentyfold radio brightening without any dramatic, observable change in the disk's light output. Such flux accumulation events should be rare and episodic, which matches how seldom this phenomenon is seen.

Why frame the summary this way? The paper's rhetorical structure is an elimination argument, and I've preserved that because the strength of the conclusion depends entirely on the completeness of the elimination — the accretion-change scenario is never positively detected, only left standing. The key interpretive choice was to foreground the amplitude-mismatch resolution (small flux change, big radio change) as the paper's intellectual center of gravity, because that is what converts an unexplained anomaly into a testable physical narrative, and it is the piece most likely to generalize when more of these objects are found. The takeaway to carry: classifications of black hole systems are runtime states, not spec sheets, and the radio band — long assumed the most stable — just demonstrated it can be rewritten within a human career.

**Where I'm least confident in this analysis:** the magnetic flux-transport mechanism in Section 4 — the claim that the inner disk crossing from a diffusion-dominated to an advection-dominated regime drives flux accumulation rests on GRMHD and analytic literature (Lubow et al. 1994 through recent MAD simulations) that the paper cites but does not develop, and my plain-language rendering of "advection beats turbulent diffusion" may smooth over genuine open disputes about whether thin, high-Eddington NLS1 disks can advect large-scale field inward at all; that specific sub-question is where I'd verify independently before leaning on it.

---

# 8. Three Crystallized Takeaways

1. **A nearby galaxy's black hole switched its radio jet from "off" to "on" — a more than 23-fold brightening — and has held it perfectly steady for over eight years, something never before seen in any active galaxy.**

2. **The trigger left no trace in visible light, infrared, or X-rays, and the resolution is a nonlinear amplifier: because jet power scales as the square of the magnetic flux threading the black hole, a mere ~3-fold field change can produce a ~20-fold radio surge.**

3. **Small, fast-feeding black holes like this one are the local stand-ins for the growing black holes of the early Universe — so watching this jet ignite in real time is the closest we get to watching how the first radio jets turned on.**

---

# 9. Shorter Summary

Astronomers have identified the first active galaxy caught making a long-lasting switch from radio-quiet to radio-loud — a transition long assumed essentially permanent over human timescales. The galaxy, SDSS J1105+1452, sits 1.6 billion light-years away and hosts a comparatively small central black hole, a few million times the Sun's mass, feeding near its maximum sustainable rate. In radio surveys through the 1990s it was barely detectable. By December 2017 it had brightened more than twentyfold, and new observations reported here show it has remained at that elevated level, almost unchanging, for over eight years.

The research team gathered the first X-ray spectra, ultraviolet and optical measurements, and multi-frequency radio data for this object, alongside archival records stretching back to photographic plates from the 1950s. The results sharpen the puzzle: while the radio output soared, everything else stayed quiet. Optical and infrared brightness has been flat for two decades, X-rays changed only modestly, and there is no obscuring gas or dust that could have hidden a dramatic event.

The team examined explanations ranging from gravitational lensing and absorbing clouds to a black hole merger, a shredded star, and a jet aimed at Earth. Each fails: most predict fading or flickering, while this source simply turned on and stayed on. The surviving explanation is a change in the accretion flow that ignited a powerful jet. The elegant part is the arithmetic of amplification: jet power depends on the square of the magnetic field funneled onto the black hole, and radio brightness rises steeply with jet power. A roughly threefold increase in accumulated magnetic field can therefore produce the entire twentyfold radio surge — no dramatic, visible disk upheaval required.

Because small, rapidly feeding black holes like this one resemble the young, growing black holes of the early Universe, this galaxy offers a rare front-row seat to jet ignition physics. Upcoming radio surveys should reveal whether it is the prototype of a new class of "radio changing-look" galaxies — and continued monitoring may catch the equally informative moment it switches back off.
