---
source: spacex_export
conversation_id: ca8a9759-26c6-474a-82a1-1eb4278bdc40
title: "MUSE Captures Glowing Quasar Filament at z=3"
created_at: 2026-05-18T01:39:22.230093Z
updated_at: 2026-05-18T01:41:25.286264Z
n_responses: 2
platform: grok/xAI
pilot: false
---

# MUSE Captures Glowing Quasar Filament at z=3

## Human

Detailed analysis of this paper Journal Reference:

Davide Tornotti, Michele Fumagalli, Matteo Fossati, Alejandro Benitez-Llambay, David Izquierdo-Villalba, Andrea Travascio, Fabrizio Arrigoni Battaia, Sebastiano Cantalupo, Alexander Beckett, Silvia Bonoli, Pratika Dayal, Valentina D’Odorico, Rajeshwari Dutta, Elisabeta Lusso, Celine Peroux, Marc Rafelski, Mitchell Revalski, Daniele Spinoso, Mark Swinbank. High-definition imaging of a filamentary connection between a close quasar pair at z = 3. Nature Astronomy, 2025; 9 (4): 577 DOI: 10.1038/s41550-024-02463-w

## Assistant

**v3.4.9**

**1. Punchy Title & One-Sentence Hook**  
Lighting Up the Cosmic Highways: High-Def MUSE Image Captures a Glowing Filament Between Quasar Twins at z ≈ 3.22.  
Astronomers have delivered the sharpest map yet of intergalactic gas flowing between two active galaxies when the Universe was only about 2 billion years old, directly confirming that cold-dark-matter simulations get the filament densities right.

**2. Big-Picture Context**  
The cosmic web is the large-scale skeleton of the Universe: a network of dense filaments, sheets, and voids that emerges naturally in cold dark matter (CDM) cosmologies. Galaxies and their supermassive black holes form at the nodes where filaments intersect. Most of the baryons at high redshift live in this diffuse web, but they are faint and hard to see until something lights them up. Quasars act as natural beacons—their intense ultraviolet output ionizes surrounding hydrogen, and the subsequent recombination (plus some collisional excitation) produces Lyman-alpha (Lyα) photons that trace the gas in emission.

Previous detections of Lyα nebulae and filaments around quasars and galaxies existed, but they were usually fuzzy or limited to brighter, more compact structures. The MUSE Ultra Deep Field (MUDF) changes the game with extreme depth. By staring for 142 hours on a region already known to host a close quasar pair, the team turned one spectacular system into a quantitative laboratory for the cosmic web at cosmic noon (z ≈ 3.22). This matters because filaments are the delivery channels for fresh gas into halos and the sites where much of the “missing” baryon budget may still hide. Mapping them in emission lets us test whether the gas densities, thicknesses, and transition zones match what CDM + hydro simulations predict.

The work also bridges scales: it measures where a galaxy’s own circumgalactic medium (CGM) hands off to the true intergalactic medium (IGM) filament and shows that this boundary sits right where theory expects the virial radius. In short, it moves the cosmic web from a theoretical prediction and blurry detections to a system we can now characterize with profiles and simulation benchmarks.

**3. Necessary Background Crash-Course**  
**Cosmic web filaments**: CDM simulations predict that dark matter collapses into a network of filaments that funnel gas and galaxies. Think of it as the Universe’s fiber-optic backbone or interstate highway system—galaxies are the cities that grow where multiple routes meet, and the filaments are the long-distance supply lines carrying raw material.  

**Quasars as illuminators**: A quasar is a supermassive black hole accreting at high rate, blasting out UV radiation that escapes the host galaxy and lights up nearby gas like a stadium floodlight in fog. The hydrogen recombines and glows in Lyα (rest-frame 121.6 nm), redshifted into the optical at z ≈ 3. Analogy: the quasar is the lamp; the filament is the glowing mist it reveals.  

**MUSE integral-field spectroscopy**: MUSE on the VLT is a hyperspectral camera—it slices the sky into thousands of tiny spatial pixels (spaxels) and records a full spectrum for each. This gives a 3D data cube of position × position × wavelength, letting you tomographically map emission at a specific redshift. Analogy: it is like taking an MRI or hyperspectral scan of the Universe’s gas instead of a single 2D photo.  

**CGM–IGM transition radius**: Every halo has a virial radius inside which gas is bound and orbits with the dark matter. Beyond that, gas belongs to the larger filament. The transition radius marks this hand-off—roughly where the steep density drop of the halo meets the shallower filament plateau. Analogy: it is the city-limits sign where dense urban sprawl gives way to the thinner rural highway.

**4. Core Technical Explanation**  
The team took 142 hours of MUSE wide-field data on the MUDF, reaching a surface-brightness sensitivity of ~4.5 × 10^{-20} erg s^{-1} cm^{-2} arcsec^{-2} in a 30 Å narrowband around the redshifted Lyα line. After standard pipeline reduction they used CubEx for aggressive sky subtraction and continuum removal, then built an optimally extracted Lyα image by summing signal-to-noise-weighted voxels.

They identified connected structures above 2σ significance spanning multiple spectral layers. This revealed two bright nebulae around the quasars (QSO1 brighter, QSO2 fainter) plus a fainter filamentary bridge between them. The filament spans ~250 proper kpc between the quasars and the whole structure extends ~700 pkpc in projection.

To quantify morphology they extracted surface-brightness profiles two ways. Along the quasar–quasar axis they used circular annuli around each quasar and rectangular apertures along the filament. Both nebulae show steep power-law declines (roughly R^{-3} to R^{-2.7}); the profiles then flatten into the filament. They fitted a broken power-law model and located the transition radius R_t where the steep nebula profile meets the shallower filament regime—at 117 ± 8 pkpc for QSO1 and 107 ± 10 pkpc for QSO2, right around the expected virial radius for 2–3 × 10^{12} M_⊙ halos at this redshift. Transversely they sliced rectangular boxes perpendicular to the filament spine and measured a clean power-law fall-off with index –0.74 ± 0.15; the detectable width is ≲ 140 pkpc (roughly 70 pkpc per side) before hitting the noise floor. Mean filament surface brightness is ~8 × 10^{-20} erg s^{-1} cm^{-2} arcsec^{-2}.

They then compared directly to simulations. In IllustrisTNG they selected close quasar-pair analogs at z ≈ 3.28 and extracted gas density along the connecting filaments. Converting density to expected Lyα surface brightness (recombination + collisional excitation) produces transverse profiles that match the observed shape and normalization within a factor of ~2–3 once modest adjustments for denser gas pockets or scattering are allowed. Semi-analytic models on the Millennium simulation confirm that such close pairs are rare but expected, and most are filament-connected. The observed densities sit comfortably inside the range CDM predicts for filaments linking halos separated by < 1 pMpc.

They do all this because a single high-fidelity system with both radial and transverse profiles plus simulation twins turns a detection into a quantitative test of the cosmic web’s physical state.

**5. What’s Genuinely New or Clever**  
The extreme depth (142 h) plus the lucky geometry of a close quasar pair inside an already ultra-deep field let them resolve filament morphology and cleanly separate the CGM and IGM regimes for the first time in emission. The broken-power-law fit and explicit measurement of R_t at the virial radius is a clean, observationally defined boundary rather than a theoretical guess. The systematic, apples-to-apples comparison with TNG pairs (same selection, same projected quantities) is what makes the density validation robust instead of hand-wavy. Using the quasars simultaneously as signposts, illuminators, and halo mass anchors is elegant.

**6. Limitations & Open Questions**  
The filament sits near the 2σ noise floor, so small-scale wiggles and sub-structure are still uncertain. Lyα radiative transfer (resonant scattering) is treated approximately; full Monte-Carlo transfer on the simulated cubes would tighten the comparison. Only one system is analyzed—cosmic variance and the full population statistics are unknown. The exact powering mix (quasar fluorescence vs. collisional excitation vs. shocks) is not uniquely pinned down. The work traces baryonic gas, not dark matter directly, though the gas is expected to follow the dark-matter skeleton. Simulations themselves have resolution and sub-grid physics limits at these densities. Brutally: this is a spectacular proof-of-concept on one object; turning it into a precision cosmological probe will require many more fields and deeper or wider surveys with ELT-class instruments.

**7. Three Crystallized Takeaways**  
1. 142 hours of MUSE data has delivered the highest-definition image yet of a cosmic filament glowing in Lyα between two quasars at z ≈ 3.22.  
2. The handover from dense halo gas to the intergalactic filament occurs right at the expected virial radius (~110 pkpc), giving an observational definition of the CGM–IGM boundary.  
3. Cold-dark-matter simulations pass this test—the gas densities inferred from the observed glow sit where the models put them, with only modest room for refinement in the emission physics.

**8. Detailed Summary & Explanation**  
Tornotti et al. present the detection and quantitative characterization of a Lyα-emitting filament connecting two quasar-host galaxies at z ≈ 3.22 inside the MUSE Ultra Deep Field. With 142 hours of VLT/MUSE integration they reach surface-brightness limits that reveal both the bright nebulae around each quasar and the fainter bridge between them. The filament is ~250 pkpc long between the quasars (total structure ~700 pkpc), has a mean surface brightness of order 8 × 10^{-20} erg s^{-1} cm^{-2} arcsec^{-2}, and shows a transverse thickness of ≲ 140 pkpc with a power-law decline index of –0.74.  

By fitting broken power-laws to the surface-brightness profiles they measure a transition radius of ~110 pkpc, coincident with the virial radius expected for the host halos. This marks the point where gas bound to individual halos gives way to the larger-scale filament.  

Comparison with IllustrisTNG and semi-analytic models shows that the observed surface-brightness levels and profile shapes are consistent with the gas overdensities (typically >10× cosmic mean for close pairs) predicted by cold dark matter. The MUDF therefore functions as a precision laboratory: the same deep datacube that reveals the filament also supplies the quasar redshifts, halo-mass anchors, and control fields needed for clean simulation matching.  

The result validates the basic picture that filaments are the visible manifestation of the cosmic web’s gaseous component at cosmic noon and demonstrates that deep integral-field spectroscopy can now move from discovery to quantitative tests of cosmology and galaxy formation physics. It opens a practical route to using statistically larger samples of such filaments to constrain the physical state of the intergalactic medium and, indirectly, the underlying dark-matter distribution on megaparsec scales.

**9. Shorter Summary**  
Using 142 hours of MUSE data in the MUDF, Tornotti et al. obtained the highest-definition Lyα image of a filament connecting two quasar-host galaxies at z ≈ 3.22. They mapped its morphology, measured a clean CGM-to-IGM transition at the virial radius (~110 pkpc), extracted radial and transverse surface-brightness profiles, and showed through direct comparison with IllustrisTNG that the filament gas densities match cold-dark-matter expectations. This turns the cosmic web from a theoretical scaffold into a quantifiable, observable structure and demonstrates a new avenue for constraining intergalactic gas properties and tracing dark matter on large scales.
