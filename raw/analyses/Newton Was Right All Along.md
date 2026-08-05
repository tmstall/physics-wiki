<div>

<div>

## You said: Analyze this paper Anonymous, Test of the gravitational force law on cosmological scales using the kinematic Sunyaev-Zeldovich effect, Physical Review Letters ...

Analyze this paper Anonymous, Test of the gravitational force law on cosmological scales using the kinematic Sunyaev-Zeldovich effect, Physical Review Letters (2026). DOI: 10.1103/rk8v-rcm3

Journal information: Physical Review Letters

Apr 17

## Claude responded: Analyzing v3.

Thought for 1s

Thought for 1s

****Analyzing**** v3.4.9

Synthesized gravitational physics findings and compiled comprehensive analysis

Synthesized gravitational physics findings and compiled comprehensive analysis

## ****Newton Was Right All Along---Across 230 Megaparsecs****

Galaxy cluster pairwise velocities, read off the microwave background, directly weigh the gravitational force law at the largest scales ever tested---and it\'s still inverse-square.

### 1. Big-Picture Context

Every test of gravity until recently has been local by cosmic standards. Solar system measurements, pulsar timing, even gravitational wave ringdowns probe scales of AU to kiloparsecs---rounding errors on the universe\'s ledger. The persistent embarrassment is that once you zoom out to tens of megaparsecs, you can only infer gravity\'s behavior from how matter clumps, and that inference requires assuming the expansion history, the dark-matter content, and a dozen other things simultaneously. It\'s like trying to measure the tension in a guitar string by watching a concert hall vibrate---too many modes entangled.

Modified Newtonian Dynamics (MOND) has survived precisely because that inference chain has gaps. MOND posits that below a critical acceleration threshold---roughly 10⁻¹⁰ m/s², far weaker than anything in the solar system---gravity\'s force law bends from 1/r² toward 1/r. That would explain galaxy rotation curves without dark matter. But testing MOND cosmologically has required either simulations with strong assumptions or statistical gymnastics. Nobody had cleanly asked: what exponent does the force law actually have between galaxy halos separated by 30--230 megaparsecs?

Gallardo et al. (ACT collaboration, PRL 2026) answer that directly. They use the kinematic Sunyaev-Zel\'dovich (kSZ) effect---tiny Doppler imprints on the CMB photons from moving hot gas---to measure how fast pairs of galaxy halos are falling toward each other across those scales. The pairwise infall velocity is a direct readout of the gravitational acceleration field. No assumptions about dark energy dynamics. No assuming the expansion rate. Just: how hard are these halos pulling on each other?

The answer is n = 2.1 ± 0.3, indistinguishable from Newton/Einstein\'s n = 2, and 3.3σ away from MOND\'s n = 1. This is the largest-scale direct test of the gravitational force law ever performed.

### 2. Necessary Background Crash Course

****The kinematic Sunyaev-Zel\'dovich (kSZ) effect.**** CMB photons---the afterglow of the Big Bang, filling all of space at microwave frequencies---occasionally scatter off free electrons in hot gas around galaxy clusters. If a cluster is moving toward you, the scattered photons get Doppler-blueshifted; moving away, redshifted. The shift is tiny (\~1 μK on a 2.7 K background), but measurable with ACT. Analogy: it\'s like reading the speedometer of a freight train by the pitch change of its horn, except the horn is the Big Bang itself.

****Mean pairwise velocity.**** Take every pair of galaxy halos in your catalog. For each pair, ask: what is the average line-of-sight velocity component that carries one halo toward the other? Average this over all pairs at a given separation r. This \"mean pairwise momentum\" is exquisitely sensitive to the gravitational acceleration at that scale because gravity is what drives halos to fall together. Analogy: if you track how fast two cars on a frictionless hill roll toward each other, you directly measure the slope---which is gravity.

****The force-law exponent n.**** Standard gravity: the acceleration between two masses drops as 1/r². MOND (in its large-scale linearized limit, called AQUAL/BIMOND): approaches 1/r at low accelerations. The paper parameterizes the acceleration as a power law with free exponent n, then fits n to the data. Lambda-CDM predicts n = 2; MOND\'s large-scale limit predicts n ≈ 1. Analogy: this is like fitting the rolloff slope of a filter response---does it fall at 12 dB/octave (Newtonian) or 6 dB/octave (MOND)?

****ACT DR6 + SDSS BOSS.**** The Atacama Cosmology Telescope Data Release 6 provides the highest-resolution ground-based CMB temperature maps to date, at 150 GHz. SDSS\'s Baryon Oscillation Spectroscopic Survey (BOSS) provides \~686,000 spectroscopic galaxy positions with accurate redshifts in the range z = 0.44--0.66. Cross-correlating CMB temperature with galaxy positions extracts the pairwise kSZ signal.

### 3. Core Technical Explanation

****Step 1: Building the theoretical prediction.**** The team derives what the mean pairwise momentum p̄(r) should be for a general gravitational force law g ∝ 1/rⁿ in an expanding universe. They start from the cosmic virial theorem / BBGKY hierarchy---essentially conservation equations for velocities in an ensemble of gravitating objects. The key insight: the pairwise velocity at separation r encodes an integral over the galaxy correlation function ξ(r\') weighted by the assumed force law. They work this out for general n analytically in the Supplemental Material. The result is a prediction template that depends on n and on the average electron optical depth τ̄ (how much CMB light each cluster scatters), which is also a free parameter.

****Step 2: Measuring the signal.**** They apply the standard pairwise kSZ estimator to the ACT DR6 150 GHz map. For each galaxy pair, they project the temperature difference toward each galaxy along the line of sight, weight by the pair separation vector, and average over 343,647 galaxies (227,837 in the primary redshift slice). The result is the observed pairwise momentum p̄\_obs(r) in bins from \~30 to \~230 Mpc.

****Step 3: Fitting the force law.**** Two fits: (a) fix n = 2 (Lambda-CDM) and float only τ̄---how much does the amplitude scale? (b) float both n and τ̄ simultaneously. The galaxy correlation function ξ(r) is measured separately from the BOSS catalog and fed into the theoretical template.

****Step 4: Results.****

The force-law exponent measurement:

n=2.1±0.3n=2.1±0.3

****Symbol definitions:****

- n : exponent of gravitational force-law power law; n = 2 is standard Newtonian; n = 1 is the MOND large-scale limit
- ±0.3 : 68% (1σ) confidence interval on n

****What this actually means:**** Newton\'s 1/r² law wins. The central value is 2.1---barely a ripple from 2.0---and the error bar doesn\'t reach 1. Standard gravity sits 0.4σ from the measurement. MOND\'s preferred n = 1 sits 3.3σ away. The data constrain n \> 1.4 at 95% confidence.

The goodness-of-fit numbers:

For Lambda-CDM: chi-squared = 20.1 over 15 degrees of freedom (probability to exceed = 0.17---a perfectly fine fit). For MOND: chi-squared = 33.8 over 15 degrees of freedom (probability to exceed = 0.004---a bad fit at the \~3σ level). The shape of the pairwise velocity curve as a function of separation is simply wrong for MOND, not just its amplitude.

### 4. What\'s Genuinely New or Clever

****The dynamics trick.**** Almost every large-scale gravity test before this one used the positions of galaxies---power spectra, correlation functions, weak lensing maps. Those measure where structure is, not how fast it\'s moving. Velocity-based tests are sensitive to the current gravitational force, not an integrated history of where matter ended up. This team is the first to use pairwise kSZ velocities over this scale range to directly read off the force-law exponent as a free parameter---not just compare to a specific model, but measure n empirically.

****Model independence.**** They don\'t commit to Lambda-CDM\'s expansion history or dark energy equation of state as priors. The derivation only assumes a Friedmann-expanding, isotropic universe plus the observed galaxy correlation function. Any theory that wants to survive must predict the same galaxy clustering and explain the pairwise velocity---a much tighter constraint than either alone.

### 5. Limitations & Open Questions

****MOND\'s escape hatch: the external field effect (EFE).**** MOND\'s behavior changes when a system sits inside a larger external gravitational field---called the external field effect. The team explicitly did not model this. They argue the relevant scales (tens to hundreds of megaparsecs) are much larger than any virialized structure, so the EFE is probably negligible. But \"probably\" is doing real work there. A proper MOND theorist would demand dedicated simulations of the EFE at these scales before conceding. The team acknowledges this.

****The redshift approximation.**** They assume the galaxy correlation function doesn\'t evolve much across z = 0.44--0.66. The growth function changes \~15% across that range; they argue ξ(r) changes only \~2%. That\'s reasonable but not zero, and future analyses need to model this redshift evolution explicitly.

****Integration lower bound.**** The pairwise velocity integral technically extends to small separations where non-linear physics dominates. They cut at 1--10 Mpc and show the answer shifts by \< 10%. But below 10 Mpc you\'re in the halo interior where screening mechanisms (like Vainshtein screening in many modified gravity models) can hide deviations. This test says nothing about modified gravity that is screened at small scales.

****Single frequency, single redshift.**** ACT DR6 at 150 GHz, one redshift slice. Thermal SZ contamination is a real foreground concern at 150 GHz. Future analyses at 90 GHz (where kSZ/tSZ spectral behavior differs) would be a cross-check.

****The τ̄ degeneracy.**** The optical depth τ̄ is marginalized over. Since τ̄ rescales the signal amplitude and n changes the shape, these are partially separable---but independent τ̄ constraints from stacked cluster profiles would tighten the n measurement significantly.

### 6. Three Crystallized Takeaways

1.  ****Newton\'s 1/r² law holds across 230 megaparsecs---the largest direct test in history---with n = 2.1 ± 0.3, consistent with standard gravity and 3.3σ away from MOND.****
2.  ****Using galaxy cluster velocities (kSZ pairwise momentum) rather than positions to probe gravity is a genuinely new and model-independent tool---and it works.****
3.  ****Future surveys with \~4 million galaxies will push this to 10σ sensitivity against n = 1, potentially closing the book on large-scale MOND for good.****

### 7. Detailed Summary & Explanation

The paper asks the most basic possible question about gravity at cosmic scales: does gravitational acceleration fall off with distance as 1/r-squared, or something else? This sounds almost too simple, but it had never been directly answered at separations of tens to hundreds of megaparsecs.

The team\'s approach is built around a physical insight: the average speed at which pairs of galaxy clusters are falling toward each other directly encodes how hard gravity is pulling them together. If you can measure those speeds, you can read off the force law without assuming much about the rest of cosmology.

They measure the speeds using the kinematic Sunyaev-Zel\'dovich effect. When the microwave background---the faint afterglow of the Big Bang---passes through the hot gas surrounding a galaxy cluster that\'s moving toward us, the photons get slightly blueshifted. Moving away, slightly redshifted. The Atacama Cosmology Telescope, a high-precision microwave telescope in the Chilean desert, is sensitive enough to detect these shifts, which are on the order of one millionth of a kelvin. By cross-correlating the temperature map with a catalog of about 343,000 galaxy positions from the Sloan Digital Sky Survey, the team extracts the pairwise momentum signal---how much the cluster gas is Doppler-shifted as a function of cluster separation.

To turn that signal into a constraint on the force law, they derive what the pairwise velocity should look like for a general power-law gravity where acceleration scales as one over r-to-the-n. The derivation uses conservation equations from statistical mechanics applied to a sea of gravitating objects, and the prediction depends on two free parameters: the force-law exponent n, and the average amount of CMB light each cluster scatters (the optical depth, tau-bar). They then fit these two parameters to the observed signal across separation bins ranging from 30 to 230 megaparsecs.

The measurement comes back at n equals 2.1 plus or minus 0.3. Standard Newtonian gravity, adapted to an expanding spacetime, predicts exactly n equals 2. The result sits 0.4 standard deviations from that prediction---essentially perfect agreement. Modified Newtonian Dynamics, in the large-scale limit relevant to these separations, predicts n equals 1. The data put that value 3.3 standard deviations away. The goodness-of-fit also tells the same story: Lambda-CDM fits the shape of the observed pairwise velocity curve well, with a reasonable chi-squared. MOND fits the shape badly.

Crucially, this is a test of the dynamics---of how fast things are moving---rather than the kinematics of where things ended up. Most large-scale gravity tests measure the distribution of matter: galaxy power spectra, weak gravitational lensing, baryon acoustic oscillation positions. Those are sensitive to the integrated history of structure formation, which is tangled up with dark energy, the expansion history, and other assumptions. The pairwise velocity approach cuts through all of that and asks directly: right now, over this separation, how hard is gravity pulling?

The analysis is also deliberately model-light. Beyond assuming the universe expands according to the Friedmann equations (the standard result from general relativity applied to a homogeneous, isotropic spacetime) and that the galaxy correlation function is measurable from the catalog, they commit to very little. Any theory---Lambda-CDM, MOND, or anything else---that wants to match these data must simultaneously reproduce the observed clustering of galaxies and their pairwise infall velocities.

Looking forward, the team estimates that surveys like the Simons Observatory, which is now operating and collecting deeper data, combined with galaxy catalogs approaching four million objects, could tighten this test enough to rule out n equals 1 at 10 standard deviations. That would not just disfavor MOND statistically---it would essentially close the kinematic window on large-scale modifications of the gravitational force law at these separations.

The primary caveats are the external field effect in MOND (not modeled, but argued to be negligible at these scales), the assumption that the galaxy correlation function doesn\'t evolve much across the redshift range studied, and the fact that screening mechanisms operating below 10 megaparsecs are not constrained by this analysis.

### 8. Shorter Summary

Gallardo et al. combine CMB temperature maps from the Atacama Cosmology Telescope with a galaxy catalog from the Sloan Digital Sky Survey to measure the mean pairwise velocity of galaxy halos using the kinematic Sunyaev-Zel\'dovich effect. They parameterize the gravitational force law as acceleration proportional to one over r-to-the-n and fit n to the observed cluster-pair infall speeds over separations from 30 to 230 megaparsecs. The standard cosmological model, with the inverse-square force law, fits the data well, while Modified Newtonian Dynamics does not match the shape of the signal. The measured exponent, n equals 2.1 plus or minus 0.3, sits 0.4 standard deviations from the Newtonian prediction and 3.3 standard deviations from the MOND prediction. The approach does not depend on committing to a detailed cosmological model beyond assuming an isotropic, homogeneous universe expanding according to the Friedmann equations, and the result is dominated by scales larger than 10 megaparsecs. Future surveys with much larger galaxy catalogs may be able to rule out n equals 1 at 10 standard deviations, potentially settling the large-scale MOND question decisively. [APS Journals + 3](https://journals.aps.org/prl/abstract/10.1103/rk8v-rcm3)

## You said: Explain about cnm

Explain about cnm

Apr 17

## Claude responded: \"CNM\" is ambiguous --- a few possibilities depending on context:

Weighed multiple interpretations and sought clarification

Weighed multiple interpretations and sought clarification

\"CNM\" is ambiguous --- a few possibilities depending on context:

- ****Cold Neutral Medium**** --- a phase of the interstellar medium (ISM), relevant to astrophysics
- ****Certified Nurse Midwife**** --- a medical credential
- ****College of New Mexico**** --- a community college system
- Something specific to the paper we were just discussing?

Which did you have in mind?

## You said: Cosmic background microwave

Cosmic background microwave

Apr 17

## Claude responded: You mean the CMB --- Cosmic Microwave Background.

Deciphered acronym and prepared clarification

Deciphered acronym and prepared clarification

You mean the ****CMB --- Cosmic Microwave Background****. Here\'s a solid explainer:

#### What It Is

The CMB is the oldest light in the universe --- thermal radiation left over from roughly 380,000 years after the Big Bang, when the universe cooled enough for protons and electrons to combine into neutral hydrogen. Before that moment, the universe was an opaque plasma; photons couldn\'t travel freely. When neutral atoms formed, the universe became transparent and that trapped radiation streamed out in all directions. We still see it today, redshifted down to microwave frequencies by 13.8 billion years of cosmic expansion.

It\'s not coming from a specific place --- it fills all of space uniformly. You\'re bathed in it right now at about 2.725 Kelvin, roughly 3 degrees above absolute zero.

#### Why It\'s So Useful

It\'s essentially a snapshot of the universe at age 380,000 years. The tiny temperature fluctuations --- variations of about 1 part in 100,000 --- encode the seeds of all large-scale structure: every galaxy, cluster, and cosmic filament you see today grew from those primordial ripples. Mapping those fluctuations (as WMAP, Planck, and ACT have done) constrains the geometry of the universe, dark matter density, dark energy, the Hubble constant, and more.

#### The Two Sunyaev-Zel\'dovich Effects

This connects directly to the paper we just analyzed. CMB photons don\'t just travel unimpeded --- they can scatter off electrons in hot gas around galaxy clusters:

- ****Thermal SZ (tSZ):**** Hot electrons in a cluster boost photon energies, distorting the CMB spectrum in a frequency-dependent way. Tells you the cluster\'s gas temperature and mass.
- ****Kinematic SZ (kSZ):**** A moving cluster Doppler-shifts the scattered photons. If the cluster is moving toward you, photons get slightly blueshifted. This is the \~1 microkelvin signal Gallardo et al. exploited to measure pairwise velocities.

The kSZ effect is far weaker than tSZ, which is why it took ACT\'s sensitivity to extract it cleanly from 300,000+ galaxies statistically.

#### The Big Picture Irony

The CMB is a relic of when the universe was impossibly hot and dense --- yet we use it as a precision ruler and speedometer for the current large-scale universe. It\'s like using the echo of a primordial explosion to measure traffic speeds on today\'s cosmic highway.

## You said: More details on what happened with the universe became transparent to to electromagnetic.

![](Newton Was Right All Along/4d7cdd19c178864e2a0fcd2c82d9860024776216.shtml "png"){width="0.7874in" height="0.3937in"}

More details on what happened with the universe became transparent to to electromagnetic. Genetic energy explained about what happened with the expanding universe and the fact that we can see incoming photons all the time from the cmb

Apr 17

## Claude responded: Great questions --- there are actually two separate puzzles here worth unpacking carefully.

Synthesized recombination epoch and CMB photon mechanics clarification

Synthesized recombination epoch and CMB photon mechanics clarification

Great questions --- there are actually two separate puzzles here worth unpacking carefully.

#### Why the Universe Became Transparent

For the first 380,000 years, the universe was a plasma --- protons and electrons existed separately, and photons couldn\'t travel more than a tiny distance before hitting a free electron and scattering. It was like trying to see through a dense fog. The universe was opaque in every direction, perpetually.

As the universe expanded, it cooled. At around 3,000 Kelvin, a threshold was crossed: electrons and protons could finally bind into stable neutral hydrogen atoms without immediately being blasted apart again by ambient radiation. This event is called ****recombination**** (a slightly misleading name since they were combining for the first time).

Neutral hydrogen is essentially invisible to photons --- it doesn\'t scatter them the way free electrons do. The fog lifted almost instantly on cosmic timescales. Every photon that had been trapped in the plasma was suddenly free to travel in a straight line --- and they\'ve been traveling ever since.

#### Why We Keep Receiving CMB Photons Today

This is the subtle part. You might ask: those photons were released 13.8 billion years ago --- shouldn\'t they have passed us long ago?

The answer is that we were inside the plasma too. The surface from which those photons were released --- called the ****Last Scattering Surface**** --- surrounds us in every direction like a shell. Photons released from points on that shell 13.8 billion years ago are just now arriving at us because those points were so far away. Meanwhile, photons released from points closer to us arrived earlier, and photons from points farther away haven\'t reached us yet.

It\'s like being at the center of an explosion --- the wavefront from progressively more distant parts is still rolling in.

#### What Expansion Does to Those Photons

As space itself stretches during cosmic expansion, photons traveling through it get their wavelengths stretched proportionally --- this is ****cosmological redshift****. The CMB photons were originally released as infrared/optical radiation at \~3,000 K. By the time they reach us after 13.8 billion years of expansion, they\'ve been stretched by a factor of about 1,100 --- pushing them down into the microwave range, which is why we call it the microwave background. The universe effectively cooled the light by stretching it.

The CMB temperature we measure today (2.725 K) is simply that original 3,000 K plasma temperature divided by that redshift factor of \~1,100.

#### The Ongoing Drizzle

So right now, photons from the Last Scattering Surface that originated slightly farther away than yesterday\'s photons are arriving. Tomorrow, slightly farther ones arrive. It\'s a continuous incoming drizzle from a shell that sits about 46 billion light-years away today (the universe expanded while the light was traveling, so the source is now much farther than 13.8 billion light-years). That shell will keep delivering photons essentially forever --- it doesn\'t run out, it just gets geometrically dimmer as the universe expands and the photon flux thins out.

Eventually, in the far future, the accelerating expansion driven by dark energy will redshift these photons to arbitrarily long wavelengths and undetectably low energies --- the CMB will effectively fade to nothing from the perspective of any future observer.

## You said: For about the last gathering surface

For about the last gathering surface

Apr 17

## Claude responded: The Last Scattering Surface --- Deep Dive

Marshaled comprehensive explanation for cosmological surface inquiry

Marshaled comprehensive explanation for cosmological surface inquiry

## The Last Scattering Surface --- Deep Dive

#### It\'s Not a Surface, It\'s a Shell Around Us

The name is slightly misleading. It\'s not a physical boundary sitting out in space like a wall. It\'s a ****spherical shell defined by distance and time**** --- specifically, the set of all points in space that are just far enough away that light released from them at the moment of recombination (380,000 years after the Big Bang) is arriving at Earth right now.

Every observer in the universe has their own Last Scattering Surface centered on themselves. It\'s observer-dependent, like your own horizon.

#### The Geometry Is Counterintuitive

The shell sits about ****42 million light-years away at the time the light was emitted**** --- but due to expansion, those same points in space are now about ****46 billion light-years away**** from us today. The light took 13.8 billion years to cross a distance that has since grown dramatically because space itself was expanding underneath the photons the entire time.

This is why the ****observable universe is 46 billion light-years in radius**** even though it\'s only 13.8 billion years old. The photons were running on an expanding treadmill the whole way.

#### It Has Finite Thickness

The transition from opaque plasma to transparent neutral gas wasn\'t instantaneous. Recombination took roughly ****100,000 years**** to complete --- so the Last Scattering Surface has a physical thickness corresponding to that duration of cosmic time. From our perspective, this smears the shell slightly, washing out the very finest angular structure in the CMB temperature map. This thickness sets a fundamental resolution limit on what the CMB can tell us --- features smaller than the shell\'s thickness are blurred out.

#### What We Actually See Looking At It

When ACT, Planck, or WMAP maps the CMB, they\'re taking a ****photograph of the Last Scattering Surface**** --- a 2D projection of that shell onto our sky. The temperature fluctuations they measure (\~1 part in 100,000) are direct snapshots of density ripples in the plasma at that moment --- regions slightly denser than average appear slightly warmer (matter was compressed and hot), slightly underdense regions appear cooler.

Those ripples are ****acoustic oscillations**** --- sound waves in the plasma, driven by the competition between gravity (pulling matter together) and radiation pressure (pushing it apart). They had been ringing for 380,000 years by the time recombination froze them in place. The pattern of those frozen ripples --- the CMB power spectrum --- is the Rosetta Stone of cosmology.

#### The Sound Horizon Connection

Those acoustic waves had a maximum distance they could travel in 380,000 years --- called the ****sound horizon****, about 450,000 light-years at that time. That scale shows up as a characteristic angular separation in the CMB temperature map (about 1 degree on the sky), and as the ****Baryon Acoustic Oscillation (BAO)**** feature in today\'s galaxy clustering --- the same ruler, now stretched by expansion to \~500 megaparsecs. This is the same SDSS BOSS feature used in the paper we analyzed to measure the galaxy correlation function.

#### Why It\'s Also a Wall --- In One Direction

Looking toward the Last Scattering Surface is literally looking at the ****edge of the observable universe in time****. You cannot see anything before recombination in electromagnetic radiation --- the plasma was opaque. It\'s a hard wall. The only way to probe before 380,000 years is with gravitational waves (which weren\'t scattered by the plasma) or neutrinos --- both of which have their own \"last scattering surfaces\" at even earlier times, which future detectors may eventually map.

#### The Analogy That Works Best

Imagine standing in the middle of a vast foggy lake at sunrise. The fog extends uniformly in every direction. Light from the water surface 1 km away just reaches you --- beyond that, you can\'t see through the fog. That 1 km circle is your \"last scattering surface.\" Now imagine the lake itself is expanding --- the fog bank that emitted the light you\'re seeing is now 3 km away, even though the light took only the equivalent of crossing 1 km. And new light from slightly farther water --- light that was just behind the fog --- keeps arriving continuously. That\'s the CMB geometry.

## You said: Explain That scale shows up as a characteristic angular separation in the CMB temperature map (about 1 degree on the sky),

Explain That scale shows up as a characteristic angular separation in the CMB temperature map (about 1 degree on the sky),

Apr 17

## Claude responded: The 1-Degree Spot --- Why Sound Waves Imprint a Specific Angular Scale

Synthesized sound horizon physics with angular scale interpretation

Synthesized sound horizon physics with angular scale interpretation

## The 1-Degree Spot --- Why Sound Waves Imprint a Specific Angular Scale

#### Start With the Sound Wave Itself

For 380,000 years after the Big Bang, the universe was a hot plasma --- a tightly coupled fluid of photons, protons, and electrons. Gravity constantly tried to pull slightly overdense regions together. Radiation pressure constantly pushed back. The result was ****acoustic oscillations**** --- literal sound waves propagating through the primordial plasma, like ringing a bell that fills the entire universe.

These waves had a maximum travel distance --- the ****sound horizon****: how far a sound wave could travel in 380,000 years given the speed of sound in that plasma. That speed was extraordinarily high --- roughly ****c/√3**** (about 58% the speed of light) because the plasma was radiation-dominated and incredibly stiff. Over 380,000 years, this gives a physical scale of about ****450,000 light-years**** at the time of recombination.

When recombination happened, the plasma froze. Those waves stopped dead in their tracks --- like a photograph of water waves at the exact moment the ocean freezes solid. Every wave that had completed exactly half a cycle, one full cycle, one and a half cycles, etc., got locked in at that moment.

#### From Physical Size to Angle on the Sky

Here\'s where the geometry comes in. That frozen 450,000 light-year scale is sitting on the Last Scattering Surface, which was about ****42 million light-years away**** when the light was emitted.

The angle something subtends is approximately its physical size divided by its distance.

θ≈dDθ≈Dd​

****Symbol definitions:****

- θ : angular size on the sky (radians)
- d : physical size of the feature at emission (the sound horizon, \~450,000 light-years)
- D : distance to the Last Scattering Surface at time of emission (\~42 million light-years)

****What this actually means:**** You\'re doing the same geometry as estimating how big the Moon looks --- angular size equals physical diameter divided by distance. The sound horizon is a ruler of known physical length sitting at a known distance. Dividing gives roughly 0.01 radians, which is about 0.6 degrees --- close to the observed \~1 degree peak.

Analogy: imagine you know a stop sign is 30 inches wide. If you can measure how many degrees of arc it spans from where you\'re standing, you can calculate your distance to it. Cosmologists run this in reverse --- they know the physical size of the sound horizon from theory, measure the angle on the sky, and infer the geometry of the universe.

#### Why It Shows Up as the First Peak in the Power Spectrum

The CMB temperature map gets decomposed by angular scale --- essentially a Fourier analysis on a sphere --- into a ****power spectrum****. The horizontal axis is multipole moment ℓ (higher ℓ = smaller angular scale), and the vertical axis is how much temperature variance exists at that scale.

The sound horizon scale --- about 1 degree, corresponding to ℓ ≈ 220 --- shows up as the ****first and tallest peak**** in that power spectrum. Why? Because waves that completed exactly ****half an oscillation**** by recombination were maximally compressed or maximally rarefied at that moment. They contribute the most temperature contrast. Waves that completed a full cycle were back at equilibrium --- they contribute nothing. This produces a series of peaks and troughs at harmonics of the fundamental scale --- the first peak at ℓ ≈ 220, second peak at ℓ ≈ 540, third at ℓ ≈ 800, and so on --- like harmonics on a guitar string.

#### Why the Angle Encodes the Geometry of the Universe

This is the beautiful part. The ****physical size**** of the sound horizon is known precisely from theory --- it depends only on the plasma physics (photon-to-baryon ratio, temperature), which are well constrained. So measuring the ****observed angle**** gives you the distance to the Last Scattering Surface. That distance depends on the ****curvature of space**** --- whether the universe is flat, positively curved (like a sphere), or negatively curved (like a saddle).

- A flat universe: photons travel straight lines → sound horizon looks \~1 degree → this is what we observe.
- A positively curved universe: photons converge, making distant objects look bigger → the peak shifts to angles larger than 1 degree.
- A negatively curved universe: photons diverge → the peak shifts to smaller angles.

The fact that the first CMB peak sits right at \~1 degree is one of the strongest pieces of evidence that ****the universe is spatially flat**** to within about 0.4% --- a genuinely extraordinary measurement from a single angular scale.

#### The BAO Connection Back to the Paper

Those same frozen sound waves --- now stretched by a factor of \~1,100 by cosmic expansion --- show up in today\'s galaxy distribution as the Baryon Acoustic Oscillation feature at \~500 megaparsecs. It\'s the exact same physical ruler, observed at two completely different epochs. The SDSS BOSS galaxy correlation function in Gallardo et al.\'s paper contains this BAO feature as a landmark in ξ(r) --- the same frozen sound wave, now 13.8 billion years older and vastly larger.

One primordial sound wave. Two completely different measurements. Same physical answer. That consistency is what makes modern cosmology so robust.

[Claude is AI and can make mistakes. Please double-check responses.](https://support.anthropic.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on)

</div>

</div>

<div>

</div>

\
