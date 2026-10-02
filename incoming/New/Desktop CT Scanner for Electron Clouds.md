I'll read the framework and the full paper, then run a quick search to ground the novelty claim before starting the analysis.Good — I have the full paper text from the inline document. Let me verify the novelty claim before starting the analysis.Now I have the full paper and sufficient context. Let me produce the analysis.

Analyzing | Framework v3.10

**Access Status** — Full paper: uploaded directly as PDF, complete text (10 pages including Methods, all figures, references). Abstract: included. Supplementary material: not provided, referenced but not needed for main analysis. Analysis basis: full text.

## § 1 — Punchy Title & One-Sentence Hook

**Desktop CT Scanner for Electron Clouds — First Lab-Scale 3D Orbital Imaging in 8 Hours**

A Göttingen team replaces the synchrotron with a table-top laser and the brute-force data torrent with a clever sparse-recovery algorithm, achieving the first laboratory-scale three-dimensional photograph of a molecule's quantum-mechanical electron cloud — the HOMO and LUMO of PTCDA — from just seven photon-energy snapshots, each sampled on a hemispherical shell in momentum space and stitched into a full 3D orbital by constraint-satisfaction math borrowed from the playbook of compressed sensing.

## § 2 — Big-Picture Context

**Paper Type & Stakes:** This is an experimental-methods paper demonstrating the first table-top realization of three-dimensional photoemission orbital tomography (3D-POT), combining a new light source architecture with a tailored reconstruction algorithm and benchmarking the result against DFT. What's at stake is whether 3D orbital imaging — previously locked behind synchrotron beamtime — can become a routine lab capability with femtosecond time resolution.

The goal is deceptively simple to state: take a photograph of a molecule's electron cloud in full three dimensions, at sub-ångström resolution, using only the electrons the molecule itself kicks out when you hit it with ultraviolet light. The technique that does this — photoemission orbital tomography (POT) — was invented in 2009 by Puschnig et al., who showed that angle-resolved photoelectron spectroscopy (ARPES) momentum maps are effectively the squared Fourier transform of the real-space molecular orbital. Measure enough momentum maps, and you can invert the Fourier transform to get the orbital back in real space. In 2D this works beautifully and has become a workhorse for studying organic semiconductors, exciton dynamics, and molecular adsorption geometry.

The 3D extension — sweeping photon energy to sample different hemispherical shells in momentum space — was demonstrated by Weiß et al. (2015) and Graus et al. (2019), but both experiments required synchrotron facilities and dense photon-energy sampling (many closely spaced energies to avoid interpolation artifacts). That combination made 3D-POT slow, expensive, and inaccessible to most ultrafast labs. Worse, it ruled out femtosecond time resolution, because synchrotrons provide quasi-continuous, not pulsed, light. The present paper attacks both bottlenecks simultaneously: it replaces the synchrotron with a high-harmonic generation (HHG) source that fits on an optical table and delivers femtosecond EUV pulses, and it replaces the dense-sampling requirement with a cyclic-projections phase-retrieval algorithm (developed by the same group in Dinh et al. 2024, tested on simulated data) that reconstructs the full 3D orbital from as few as four hemispherical shells.

**Prior Belief Check:** This result aligns with what the field expected to be possible in principle but considered practically difficult. Nobody doubted that HHG sources could generate the right photon energies (13–71 eV) — HHG-based ARPES is well established. The genuine surprise is quantitative: the sparse-reconstruction algorithm works on real experimental data with just four to seven photon energies where the synchrotron-based approach used dense sampling across dozens. That the algorithm, previously validated only on simulated data (Dinh et al. 2024), survives real noise, real background, and real calibration imperfections is a non-trivial validation. The result is best characterized as confirmatory-but-enabling: it confirms a predicted capability and makes it practically accessible.

**Replication & Convergence Note:** This is a single-group result (University of Göttingen, in collaboration with CNR-IFN Padova for the monochromator design). No independent replication of table-top 3D-POT exists. The benchmark comparison against gas-phase DFT-calculated Kohn-Sham orbitals serves as a quasi-independent check, and the earlier synchrotron work on the same PTCDA/Ag(110) system provides a cross-method validation of the orbital shapes. Full independent confirmation would require another group building a comparable HHG + momentum-microscopy setup and reproducing the sparse reconstruction on a different molecular system.

## § 3 — Necessary Background Crash-Course

### Photoemission orbital tomography (POT) — why kicking out electrons reveals orbital shape

When a photon with enough energy hits a molecule adsorbed on a surface, it ejects an electron via the photoelectric effect. That ejected electron carries away momentum — both its direction of travel and its speed encode information about the orbital it came from. Under the plane-wave approximation (treat the outgoing electron as a free particle, ignoring scattering off the substrate), the angular and energy distribution of photoelectrons is proportional to the squared Fourier transform of the real-space molecular orbital.

**Analogy:** Imagine you have a complex 3D data structure stored in memory — say, a sparse voxel grid representing a molecule's electron density. You can't read the memory directly, but you can probe it by firing test packets at it and measuring the diffraction pattern that comes back. Each diffraction pattern gives you the *power spectrum* (squared Fourier amplitudes) of the data along a particular slice. POT does exactly this: photons go in, electrons come out, and their angular distribution is the power spectrum of the orbital in momentum space.

**Breaks when:** real photoelectrons are not free particles. They scatter off the substrate, feel the crystal's inner potential, and have energy-dependent cross-sections. The plane-wave approximation ignores all of this. For the flat, weakly interacting PTCDA/Ag system it works remarkably well; for strongly interacting or non-planar adsorbates, final-state effects become significant.

### The hemisphere sampling trick — why you need multiple photon energies for 3D

Energy conservation links the photon energy, the orbital's binding energy, and the electron's kinetic energy. An electron ejected with kinetic energy $E_{\text{kin}}$ has a momentum magnitude $\|\mathbf{k}\|$ set by:

$$\|\mathbf{k}\| \approx 0.514 \sqrt{E_{\text{kin}}(\text{eV})} \quad \[\text{in } \text{Å}^{-1}\]$$

**Symbol definitions:**

- $\|\mathbf{k}\|$ : magnitude of the photoelectron momentum (in inverse ångströms)
- $E_{\text{kin}}$ : kinetic energy of the photoelectron (in eV)
- 0.514 : conversion factor from the relation $E_{\text{kin}} = \hbar^2 k^2 / 2m_e$

**What this actually means:** at a fixed photon energy, you can only sample the orbital's Fourier transform on a single hemispherical shell in 3D momentum space — the hemisphere's radius is set by the photon energy. Change the photon energy, and you get a different hemisphere with a different radius. Stack enough hemispheres and you've sampled the full 3D momentum space, which you can then invert to get the real-space orbital.

**Analogy:** Think of it like a 3D lookup table where each read operation returns the values along a curved 2D surface at a specific "radius." A single read gives you a 2D slice; sweeping the radius parameter gives you full 3D coverage. The synchrotron approach was like doing sequential reads at every possible radius with fine spacing. This paper's approach is like doing reads at only 4–7 radii and using constraint-based reconstruction to fill in the gaps — the same way a compressed-sensing algorithm recovers a sparse signal from undersampled measurements.

**Breaks when:** the hemispheres are too sparse relative to the spatial frequency content of the orbital. If the orbital has fine structure in the $k_z$ direction that falls between your sampled hemispheres, the reconstruction will miss it. The algorithm's success depends on the orbital being sparse enough (few significant lobes) that the constraints can fill the gaps correctly.

### High-harmonic generation (HHG) — table-top EUV in 35-femtosecond pulses

HHG is a nonlinear optical process: you focus an intense infrared laser pulse into a gas (here, argon), and the gas atoms' electrons tunnel out, accelerate in the laser field, and slam back into the parent ion, emitting a burst of extreme ultraviolet (EUV) photons at odd multiples (harmonics) of the driving laser frequency. With a 1030 nm driver, the harmonics are spaced by 2.4 eV and extend up past 71 eV. A grating-based monochromator then selects one harmonic at a time.

**Analogy:** HHG is like overclocking a processor until it emits harmonics — the electrons in the gas atoms are driven so hard by the laser field that their response becomes wildly nonlinear, and the output contains frequency components at 13th, 15th, 17th... multiples of the input. The monochromator is the bandpass filter that selects one harmonic.

**Breaks when:** you push the metaphor to imply the harmonics are independent oscillators. They're not — they're all phase-locked to the driving pulse, which is why HHG naturally produces femtosecond (and even attosecond) pulses. The coherence is a feature, not an artifact.

### Phase retrieval — reconstructing from magnitudes only

ARPES gives you the *intensity* of the Fourier transform — the squared magnitude $\|\mathcal{F}(\psi)(\mathbf{k})\|^2$ — not the phase. This is a classic phase-retrieval problem: recover a complex-valued function from its power spectrum. The paper's cyclic projections (CP) algorithm solves this by iteratively enforcing constraints — the measured magnitudes on the hemispheres, the real-space support (the orbital must fit inside a box roughly the size of the molecule), voxel sparsity (only ~800 of ~3000 voxels are nonzero), and symmetry (the orbital's known point-group symmetry).

**Analogy:** This is directly analogous to constraint-satisfaction in optimization: you have a feasibility problem with multiple constraints (measured data, bounding box, sparsity, symmetry), and you search for a solution that satisfies all of them simultaneously. The algorithm is a fixed-point iteration — it cycles through the constraints, projecting onto each constraint set in turn, converging to a point that (approximately) satisfies all of them. Multiple random initializations are needed because the landscape has many local minima, exactly like a non-convex optimization with many saddle points.

**Breaks when:** the constraints are inconsistent or too loose. With too few measured hemispheres, the feasibility space has many valid-looking solutions (local minima) that are physically different orbitals. The paper shows this explicitly: with 4 photon energies, several distinct solutions have similar "gap" values; with 10, the correct solution separates cleanly.

> **Central analogy for this paper:** reconstructing a sparse 3D array from a few curved-surface reads

## § 4 — Core Technical Explanation

### The light source: HHG + monochromator

The team starts with a Yb-fiber laser amplifier — a workhorse of ultrafast science — delivering 35 fs pulses at 500 kHz repetition rate, 130 μJ per pulse, centered at 1030 nm. They focus 65 W of this into an argon gas jet, generating high harmonics spanning 13–71 eV. A custom EUV monochromator (three gold-coated toroidal mirrors plus one of four selectable plane gratings at 100, 300, 400, or 600 lines/mm) isolates individual harmonics. The monochromator is designed for grazing-incidence off-plane diffraction geometry, which preserves the femtosecond pulse duration (minimizes temporal broadening from the grating) while maintaining high throughput for p-polarized light.

The key engineering constraint: you need enough photon energies spanning a wide enough range to sample momentum space from ~2 Å⁻¹ (where the orbital's main features live) out to ~4 Å⁻¹ (the resolution limit). The HHG source delivers 25 selectable harmonics across this range, though the paper demonstrates that only 4–10 are needed.

### Data collection: time-of-flight momentum microscopy

The sample is PTCDA adsorbed on Ag(110) in a brick-wall monolayer structure. The PTCDA LUMO is occupied (pushed below the Fermi level by charge transfer from the silver — a standard surface-chemistry effect you'd recognize immediately). This gives two targets: the HOMO and the LUMO, both accessible in the same measurement.

The momentum microscope is a parallel-detection instrument — it simultaneously records the full 2D momentum distribution ($k_x$, $k_y$) and the kinetic energy of every photoelectron, with no scanning needed. Each photon energy produces a 3D dataset ($k_x$, $k_y$, $E_{\text{kin}}$) in a single 2-hour exposure at ~2 × 10⁵ electrons/second. Ten such datasets were collected spanning 20.5–63.8 eV.

Background subtraction proceeds by fitting the momentum-integrated photoelectron spectrum at each photon energy to a sum of two Gaussians (HOMO and LUMO peaks) riding on a linearly varying background modulated by a Fermi-Dirac cutoff — then applying that decomposition momentum-pixel by momentum-pixel to extract the clean orbital fingerprint. After background removal, the data are symmetrized, divided by the polarization factor \|**A**·**k**\|², and normalized to photon flux.

### The reconstruction algorithm

The cyclic projections (CP) algorithm takes as input the background-corrected momentum maps on their hemispherical shells and attempts to find a 3D orbital that simultaneously satisfies:

1.  **Data consistency** — the orbital's Fourier-transform magnitudes on the measured hemispheres match the data.
2.  **Support constraint** — the real-space orbital fits inside a 12 × 18 × 6 Å³ box (roughly the van der Waals envelope of PTCDA).
3.  **Sparsity** — only 800 voxels (26% of the support) are nonzero.
4.  **Symmetry** — the known point-group symmetry of the gas-phase orbital (antisymmetric in $x$, $y$, $z$ for the HOMO; antisymmetric in $x$, $z$ but symmetric in $y$ for the LUMO).

Starting from a random initialization, the algorithm cycles through these constraints, projecting onto each constraint set in sequence. The "reconstruction gap" measures how far the current guess is from satisfying all constraints simultaneously — a gap of zero means perfect consistency.

In practice, the algorithm finds local minima, not the global minimum. The team runs 100 independent reconstructions from random starts and uses DBSCAN clustering (after PCA dimensionality reduction) to identify the most common solutions. The key finding: with 7 photon energies, two dominant cluster types emerge, differing mainly by a phase flip in the outer lobes. The lower-gap cluster matches the measured data better and also agrees with DFT calculations.

### Validation: comparing to DFT

The reconstructed HOMO is compared to a Kohn-Sham orbital calculated by DFT for the isolated gas-phase PTCDA molecule (from Puschnig's molecular orbital database), with a low-pass filter applied to match the experiment's momentum cutoff. Agreement is excellent in both the in-plane ($x$, $y$) lobe structure and the out-of-plane ($z$) profile, with the $z$-maximum correctly placed at ~0.8 Å above the molecular plane. The LUMO reconstruction shows equally good agreement.

A known subtlety: the adsorbed PTCDA molecule bends slightly (~0.3 Å), with oxygen atoms pulled toward the substrate. This distortion falls below the current 0.75 Å resolution limit and is invisible in the reconstruction — the algorithm returns a planar orbital consistent with the gas-phase geometry.

### Assumption Audit

**Watch:** Reader likely assumes the "Fourier transform" relationship between real-space orbital and momentum distribution is exact. The paper actually relies on the *plane-wave final-state approximation*, which treats the outgoing photoelectron as a free particle. This is an approximation — not an identity — and breaks for strongly interacting adsorbates or photon energies where final-state scattering becomes significant. The paper acknowledges this (citing Kern et al. 2023) but does not quantify the error for PTCDA/Ag.

**Watch:** Reader likely assumes the symmetry constraints reflect the actual adsorbed-molecule symmetry. The paper actually enforces the *gas-phase* orbital symmetry, including $z$-mirror symmetry, even though the adsorbed molecule is known to bend slightly (breaking $z$-symmetry). The authors note that releasing $z$-symmetry creates many spurious local minima, preventing reliable reconstruction — so the constraint is enforced for algorithmic stability, not because the physics demands it. This means any genuine asymmetry in the $z$-direction is suppressed by construction.

**Watch:** Reader likely assumes "4 photon energies suffice" means the reconstruction is equally reliable at 4 as at 10. The paper actually shows that with 4 energies, multiple distinct solutions have similarly small gaps and cannot be reliably distinguished without external information (like DFT comparison or tighter support constraints). The "4 suffice" claim is conditional on having prior knowledge of the orbital's support from a fuller initial characterization.

## § 5 — What's Genuinely New or Clever

Two innovations make this paper stand out, and they're synergistic — neither alone would close the gap:

**1. The experimental side: momentum microscopy + HHG eliminates two bottlenecks at once.** Previous 3D-POT required a synchrotron (big facility, no femtosecond pulses, limited beamtime) and scanned either the electron analyzer angle or energy (slow). The time-of-flight momentum microscope collects the full ($k_x$, $k_y$, $E_{\text{kin}}$) datacube in parallel — no scanning — and the HHG source provides 25 selectable photon energies in femtosecond pulses on an optical table. The combination converts 3D-POT from a months-long synchrotron campaign to an 8-hour (4 energies × 2 h) lab measurement, with intrinsic femtosecond time resolution available for pump-probe extensions. This is genuinely new to the field: no prior group had combined all three elements (HHG + momentum microscope + 3D reconstruction).

**2. The algorithmic side: cyclic projections turn sparse into sufficient.** The conceptual insight is that the traditional approach — interpolating between densely sampled hemispheres — is both data-hungry and error-prone near zero crossings of the Fourier transform (where the sign flips but the magnitude goes through zero, making interpolation unreliable). The CP algorithm sidesteps both problems by recovering amplitude *and phase* simultaneously through constraint satisfaction. The algorithm was validated on simulated data in Dinh et al. (2024); this paper is its first experimental test, and the demonstration that 7 hemispheres (out of a possible 25) produce excellent reconstructions — and 4 produce usable ones — is a non-trivial experimental validation.

**Predictive Content Check:**

**Falsifiable handle:** The paper makes an implicit prediction: the sparse-reconstruction approach should work on *unknown* orbitals (excited states, hybridized interfaces) where no DFT comparison is available to select among competing reconstructions. The acid test is a pump-probe 3D-POT experiment on a system where the excited-state orbital is not predicted by theory — the reconstruction must stand on its own without a DFT tiebreaker. The authors sketch this scenario explicitly (4 photon energies × 10 pump-probe delays ≈ 80 hours total), and the predicted outcome is that the static characterization provides enough constraint (support, sparsity) to bootstrap the dynamic reconstruction. If the algorithm produces ambiguous or inconsistent reconstructions for excited-state orbitals, the method's generalizability is falsified. The spatial resolution limit of 0.75 Å and the molecular-bending detection threshold of ~0.75 Å are also concrete, falsifiable numbers.

## § 6 — Limitations & Open Questions

**The plane-wave approximation sets an invisible floor.** The entire reconstruction assumes the photoelectron is a free particle once ejected. For PTCDA on Ag(110), this works well empirically, but the approximation ignores final-state scattering off the substrate and energy-dependent cross-section variations beyond the $\|\mathbf{A} \cdot \mathbf{k}\|^2$ polarization factor. For more strongly interacting systems (chemisorbed molecules, non-planar adsorbates), these effects could systematically distort the reconstruction without any internal diagnostic to flag the problem. **(A) Consensus** — this is the oldest and most widely acknowledged limitation of POT; the paper itself points to Kern et al. (2023) for extensions. **(paper acknowledgment + broader literature)**

**Phase ambiguity with sparse data is real and unresolved.** Even with 7 photon energies, two distinct solutions survive with similar gap values, distinguishable only by comparison to DFT or by detailed analysis of the momentum-space fit quality. With 4 energies, the ambiguity is worse. For truly unknown orbitals — the regime where the method is most needed (excited states, time-resolved) — there is no DFT oracle to break ties. The paper proposes using the gap metric plus clustering, but acknowledges this is not a guaranteed discriminator. **(B) Contested** — some groups working on phase retrieval would argue that tighter constraints (e.g., the relaxed Douglas-Rachford algorithm the authors themselves are developing) could eliminate spurious minima, while others would say the non-convexity of the feasibility landscape is fundamental. **(paper §4–5 + analyst inference)**

**Only demonstrated on a well-characterized benchmark.** PTCDA/Ag(110) is the fruit fly of orbital tomography — highly ordered, flat, weakly interacting, with well-known DFT-computed orbitals. The method's robustness on disordered films, non-planar molecules, strongly interacting interfaces, or multi-orientation domains remains untested. **(A) Consensus** — the community routinely expects benchmark demonstrations to precede general application, and the limitations of the PTCDA test system are widely understood. **(paper + broader literature)**

**No time-resolved demonstration yet.** The paper's strongest selling point — that the HHG source enables femtosecond 3D orbital movies — remains a projection, not a result. The 80-hour estimate (4 energies × 10 delays × 2 h) is plausible but unverified, and the signal-to-noise challenge for excited-state orbitals (which are weaker and shorter-lived than ground-state ones) could push measurement times significantly higher. **(C) Speculative** — I am extrapolating from the known difficulty of time-resolved ARPES on excited states; the paper's Outlook section is explicitly forward-looking but does not quantify the expected signal levels. **(analyst inference)**

**The 0.75 Å resolution ceiling is hard-limited by the maximum photon energy.** Doubling the resolution to ~0.375 Å would require quadrupling the maximum photon energy to ~250 eV, well beyond the current HHG cutoff of 71 eV. This is not a solvable problem within the current experimental architecture. **(A) Consensus** — this is a straightforward consequence of the Fourier-space sampling geometry and is explicitly stated in the paper. **(paper §2)**

## § 7 — Detailed Summary & Explanation

Bennecke et al. demonstrate the first laboratory-scale (table-top) three-dimensional photoemission orbital tomography experiment, achieving what previously required synchrotron beamtime. They image the two frontier molecular orbitals — the HOMO and the charge-transfer-filled LUMO — of the organic semiconductor PTCDA adsorbed on a silver surface, in full 3D, with sub-ångström (0.75 Å) spatial resolution.

The experiment rests on two pillars. The first is an instrumental one: a high-harmonic generation extreme ultraviolet light source (13–71 eV, femtosecond pulses, table-top format) coupled to a time-of-flight momentum microscope that records the complete momentum and energy distribution of photoelectrons in parallel, without scanning. This combination delivers the photon-energy-dependent momentum maps needed for 3D reconstruction at a pace the synchrotron approach could not match — each photon energy requires only a 2-hour exposure.

The second pillar is algorithmic. Traditional 3D orbital tomography required dense photon-energy sampling (many closely spaced energies) to interpolate the orbital's momentum-space distribution between measured hemispherical shells. That interpolation scheme is both data-hungry and vulnerable to systematic errors near zero crossings of the Fourier-transformed orbital. The authors' cyclic-projections algorithm replaces interpolation with constraint satisfaction: given the measured magnitudes on a few hemispheres, plus knowledge of the orbital's real-space bounding box, sparsity, and symmetry, the algorithm recovers both the amplitude and the phase of the full 3D momentum-space distribution, then inverts it to real space. The algorithm was previously validated on simulated data; this paper is its first experimental test.

The central result is that 7 photon energies — sampled from the 25 available harmonics — produce a high-quality 3D orbital that matches density functional theory predictions in both the in-plane lobe structure and the out-of-plane profile. Even 4 photon energies produce recognizable orbitals, though with greater ambiguity (multiple solutions of similar quality that require additional information to distinguish). The total measurement time for a 4-energy dataset is 8 hours, versus weeks at a synchrotron.

The paper also examines reconstruction reliability in detail: 100 random-start reconstructions are clustered, and the gap metric (measuring constraint violation) is shown to correlate with reconstruction quality. More data (more photon energies) improves the landscape, making the correct solution more clearly distinguishable. The authors propose a two-stage strategy for future time-resolved experiments: first characterize the static orbital with 7 energies to establish the support, then use only 4 energies per pump-probe delay step for the dynamic measurement, leveraging the static characterization as a constraint.

The summary is framed this way because the paper's contribution is dual — half experimental engineering (the light source and detector combination) and half applied mathematics (the reconstruction algorithm). Neither alone would constitute a major advance: HHG-based ARPES exists, and the algorithm was already published. The synergy is the story. The interpretive choice to emphasize the conditional nature of the "4 energies suffice" claim reflects the paper's own data (Fig. 4), which shows significantly more ambiguity at 4 versus 7 or 10 energies.

**Where I'm least confident in this analysis:** The reconstruction algorithm's behavior in the non-convex feasibility landscape — specifically, whether the gap metric is a reliable discriminator for unknown orbitals without DFT benchmarking — is something I've characterized based on the paper's own analysis and general knowledge of phase-retrieval algorithms, but the subtleties of the cyclic-projections convergence properties (versus alternatives like relaxed Douglas-Rachford) are at the edge of my depth. The paper cites three references (43–45) on improved algorithms, one of which is a 2025 preprint by the same group, and I have not evaluated those in detail. If the feasibility landscape's local-minimum structure is worse for more complex molecules than PTCDA, the reliability analysis presented here could be substantially more optimistic than reality.

## § 8 — Three Crystallized Takeaways

1.  **You can now image a molecule's 3D electron cloud on an optical table in 8 hours**, replacing a synchrotron and weeks of beamtime — the key being that a smart reconstruction algorithm makes sparse data sufficient where brute-force sampling was previously considered necessary.
2.  **The algorithm recovers not just the orbital's shape but its phase (sign structure)** — the positive and negative lobes that define bonding character — from intensity-only measurements, using constraint satisfaction rather than interpolation, which is both more data-efficient and more robust near the orbital's nodes.
3.  **The femtosecond time resolution is built in but not yet demonstrated**: the HHG source inherently delivers ultrashort pulses, so the path to 3D orbital movies of chemical dynamics at the ångström-femtosecond frontier is open in principle and sketched quantitatively (80 hours for a 10-frame movie), but the excited-state signal-to-noise challenge remains untested.

## § 9 — Shorter Summary

Photoemission orbital tomography reconstructs a molecule's electron orbital in real space from the angular distribution of photoelectrons, exploiting the fact that the momentum-space pattern is the Fourier transform of the real-space orbital. By varying the photon energy, each measurement samples a hemispherical shell at a different radius in momentum space, and enough shells give full 3D coverage.

Until now, 3D orbital tomography required synchrotron radiation and dense photon-energy sampling — dozens of energies, weeks of beamtime. Bennecke et al. replace the synchrotron with a table-top high-harmonic generation light source delivering femtosecond extreme ultraviolet pulses tunable from 13 to 71 eV, paired with a time-of-flight momentum microscope that records the full momentum-energy distribution of photoelectrons without scanning. This hardware combination collects each photon-energy dataset in two hours.

The algorithmic innovation is equally important: a cyclic-projections phase-retrieval algorithm recovers both the amplitude and the sign of the orbital's Fourier transform from intensity-only data on just a few hemispherical shells, using constraints on the orbital's real-space size, sparsity, and symmetry. Where previous methods needed dense sampling to interpolate reliably, this approach needs only seven (or even four) photon energies.

The team demonstrates full 3D imaging of the HOMO and LUMO of the organic semiconductor PTCDA adsorbed on silver, achieving 0.75-ångström resolution in eight hours of total measurement time. The reconstructed orbitals agree excellently with density functional theory predictions. Because the light source delivers femtosecond pulses, the setup is inherently ready for pump-probe extensions — time-resolved 3D orbital movies are the explicit next target, with an estimated 80-hour measurement for a 10-frame sequence.

The main open question is whether the reconstruction remains reliable for unknown orbitals where no theoretical benchmark exists to break ties between competing solutions. The phase ambiguity is real — multiple solutions can have similar quality metrics — and managing it for excited-state or hybridized orbitals will be the decisive test of the method's generalizability.
