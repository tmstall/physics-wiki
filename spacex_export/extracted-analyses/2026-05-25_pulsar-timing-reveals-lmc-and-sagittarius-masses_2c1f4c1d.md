---
source: spacex_export
conversation_id: 9aa96624-c6ca-4543-ac62-84c41597bbcf
title: "Pulsar Timing Reveals LMC and Sagittarius Masses"
created_at: 2026-05-25T04:28:24.644882Z
updated_at: 2026-05-25T04:30:21.995285Z
n_responses: 2
platform: grok/xAI
pilot: false
---

# Pulsar Timing Reveals LMC and Sagittarius Masses

## Human

Analyze this paper

## Assistant

**v3.5.4**

**Analysis**

**1. Punchy Title & One-Sentence Hook**  
**Pulsar Accelerometers Weigh the LMC and Sagittarius: Reading the Milky Way’s Instantaneous Gravitational Tilt**  
Millisecond pulsars act as embedded gravitational sensors that reveal the present-day bound masses of the Large Magellanic Cloud and Sagittarius dwarf through the north-south asymmetry they imprint on the vertical acceleration field near the Sun—completely independent of any stellar kinematic data.

**2. Big-Picture Context**  
The Milky Way is dynamically young and unsettled. The LMC is on its first or second close passage, while Sagittarius has already been torn into a long tidal stream after multiple disk crossings. Both events drive warps, vertical waves, and large-scale phase-space spirals that violate the equilibrium and symmetry assumptions built into classical Jeans modeling and orbit-fitting mass estimates. Those traditional methods integrate forces over stellar lifetimes, mixing every past perturbation into a single blurred snapshot.

This paper instead measures the gravitational field right now. Millisecond pulsars function as ultra-stable clocks whose tiny period derivatives directly encode line-of-sight accelerations after known contaminants are removed. The LMC and Sagittarius offset the dark-matter halo center of mass relative to the baryonic disk and launch vertical waves; the resulting north-south imbalance in vertical acceleration near the Sun grows with height and scales with satellite mass. By running a controlled grid of N-body simulations and matching the predicted asymmetry profile to 53 clean pulsars, the authors extract masses that stand apart from every stellar-kinematic determination.

The payoff is both practical and conceptual. Accurate present-day satellite masses test how efficiently tides strip dwarfs, how the Milky Way halo responds to external perturbers, and how much “noise” these satellites inject into local dark-matter density or total-mass estimates.

**3. Necessary Background Crash-Course**  
Pulsar timing measures acceleration because a millisecond pulsar’s spin is so regular that any line-of-sight Doppler shift appears cleanly in the observed period derivative. After subtracting intrinsic spindown, the Shklovskii effect, and binary contributions, the residual directly gives a_los/c. Analogy: a perfectly regulated quartz oscillator bolted inside an accelerating elevator; the change in its tick rate reveals the elevator’s motion without any external reference.

Satellite-driven disequilibrium occurs because the LMC tugs the entire dark halo, shifting its center relative to the stellar disk, while Sagittarius punches through the disk and launches vertical waves. In perfect equilibrium the vertical restoring force would be symmetric above and below the midplane. The offset centers plus the waves break that symmetry, producing stronger net acceleration toward the midplane on one side. Analogy: a cargo ship whose heavy deck containers have slid to one side—the hull lists and sensors at symmetric heights above and below the waterline read systematically different “down” directions until the load is recentered.

Vertical acceleration asymmetry is the simple difference between the vertical acceleration measured at equal distances above and below the midplane. In equilibrium this difference is zero everywhere. Satellite-induced center-of-mass offsets and waves make the difference nonzero and increasing with height; its amplitude and shape encode the perturber masses. Analogy: two identical cars on a slope; secretly adding weight to one car’s trunk makes the suspension sensors on that side read a systematically different load—the difference directly reports how much extra mass was added.

**4. Core Technical Explanation**  
The authors start with a cleaned sample of 53 millisecond pulsars that have measured parallaxes. They derive line-of-sight accelerations from the period derivatives after removing all known contaminants. They define the observable  

\[ \Delta a(z) = a_{\rm los,z}(+z) - a_{\rm los,z}(-z) \]  

**Symbol definitions:**  
Δa(z): vertical acceleration asymmetry at signed height z from the midplane (units of acceleration).  
a_los,z: vertical component of the line-of-sight acceleration at that location.  

**What this actually means:** In equilibrium the Milky Way’s vertical gravity pulls equally from above and below; the difference vanishes. The LMC and Sagittarius displace the dark-halo center relative to the baryonic disk and launch waves, so the net restoring force becomes stronger on one side of the midplane. This is directly analogous to reading vibration sensors at symmetric locations above and below a hard-drive platter whose spinning disk has developed a warp—the imbalance reveals exactly how much off-center mass is perturbing the system.

They initialize a Milky Way-like galaxy (bulge + exponential disk + double-power-law halo) plus live LMC and Sagittarius satellites with Agama, then evolve the system for 3 Gyr with Gadget-4 at medium resolution. They create a 5 × 5 grid by varying LMC total mass from 1.0 to 2.25 × 10^{11} M_⊙ and Sagittarius stellar-plus-dark mass across five steps. For each snapshot they extract the acceleration field near the solar position, compute the asymmetry profile Δa(z) up to |z| = 1 kpc, and compare it to the pulsar data with the integrated goodness-of-fit statistic  

\[ \mathcal{L} = \frac{1}{\int_0^z dz'} \left( \frac12 \int_0^z \frac{[\Delta a_{\rm sim}(z') - \Delta a_{\rm obs}(z')]^2}{\sigma^2_{\Delta a_{\rm obs}}(z')} dz' \right) \]  

**Symbol definitions:**  
L: goodness-of-fit statistic (smaller is better; equivalent to averaged χ²).  
Δa_sim, Δa_obs: simulated and observed asymmetry profiles.  
σ_Δa_obs: uncertainty on the observed asymmetry from the pulsar sample.  

**What this actually means:** They ask how well each simulated “lopsidedness fingerprint” matches the real fingerprint carved into the pulsar accelerations. The best match occurs for a heavy LMC combined with medium-mass Sagittarius. They then read the bound mass inside each satellite’s tidal radius directly from the particle distribution in that best-fit snapshot.

They also demonstrate that LMC and Sagittarius effects do not add linearly—changing one satellite’s mass alters the spatial pattern of asymmetry, not just its overall strength—because the halo and disk respond collectively. Static triaxial halo models alone produce an asymmetry of the wrong sign and much smaller amplitude, confirming that the observed signal is dominated by time-dependent satellite perturbations.

**5. What’s Genuinely New or Clever**  
The decisive move is using instantaneous acceleration from pulsar timing instead of time-integrated stellar kinematics. Pulsar timing gives the gravitational field “right now,” so the asymmetry directly encodes the present-day mass distribution of the perturbers without the long orbital history that confuses traditional methods. The controlled N-body grid plus the simple integrated asymmetry metric turns a messy, non-linear dynamical problem into a tractable fitting exercise whose uncertainties can be read from the Hessian of the goodness-of-fit surface. The authors explicitly map the non-linear coupling between LMC and Sagittarius, showing that joint modeling is required rather than treating the satellites independently.

**6. Limitations & Open Questions (brutally honest)**  
The grid is coarse and the Milky Way host potential is fixed to one Agama realization; a different halo concentration or disk mass could shift the best-fit satellite masses by an amount comparable to the quoted errors. Hessian uncertainties assume the model is correct and do not fully capture systematic mismatches (resolution, missing baryonic physics, or additional perturbers). The pulsar sample is still modest; a few outliers or imperfect contaminant removal could bias the asymmetry profile. Satellite orbits are pinned to present-day observed positions; allowing modest variations in impact geometry would broaden the error bars. The present-day enclosed masses depend on how the code defines the tidal radius, which is somewhat arbitrary in a live, stripping host.

Open questions that should be attacked in the next 12–24 months include repeating the grid at higher resolution with varied Milky Way initial conditions, folding in upcoming SKA pulsar discoveries, jointly fitting with stellar-stream and disk-wave data, and testing whether the same asymmetry signature appears in other tracers such as Cepheids or red-clump stars. If the method survives these tests it becomes a powerful new tool; if the masses move significantly under reasonable model variations, the community will know the dominant systematic.

**7. Three Crystallized Takeaways**  
1. Millisecond pulsars function as embedded gravitational accelerometers that read the Milky Way’s instantaneous vertical tilt near the Sun—a tilt created by the offset centers of mass between the dark halo and the stellar disk.  
2. The LMC and Sagittarius do not simply add their gravitational effects; their combined influence on the acceleration asymmetry is non-linear, so both must be modeled together to extract reliable masses.  
3. This kinematics-free approach yields a present-day LMC bound mass of roughly 41 billion solar masses inside 16.6 kpc and a Sagittarius bound mass of about 350 million solar masses inside 5 kpc—numbers that sit comfortably among previous estimates yet rest on an entirely independent observable.

**8. Detailed Summary & Explanation**  
The paper introduces a novel dynamical probe of satellite galaxy masses that bypasses the usual reliance on stellar positions and velocities. The core observable is the vertical acceleration asymmetry Delta a measured by millisecond pulsars in the solar neighborhood. This asymmetry arises because the LMC’s massive halo and the repeated disk crossings of Sagittarius displace the dark matter halo center relative to the baryonic disk and launch vertical waves. The resulting north-south imbalance in the restoring gravitational force grows with height above the midplane and its amplitude scales with the masses of the perturbers.

The authors run a grid of self-consistent N-body simulations, vary the satellite masses across plausible ranges, and identify the combination that best reproduces the observed asymmetry profile extracted from 53 clean pulsars. The best-fit model corresponds to a relatively heavy LMC and medium-mass Sagittarius. From the particle data in that snapshot they measure the total mass still bound within each satellite’s tidal radius today: 4.1 ± 1.0 × 10^{10} solar masses for the LMC (inside 16.6 kpc) and 3.5 ± 2.4 × 10^8 solar masses for Sagittarius (inside 5 kpc). These values are consistent with literature determinations that used stellar kinematics, yet they are derived without any stellar kinematic information whatsoever.

The work also demonstrates that the observed asymmetry cannot be explained by a static triaxial dark halo alone and that the LMC plus Sagittarius effects interact non-linearly. Roughly 25 % of the asymmetry signal comes from the disk warp; the dominant contribution is the relative center-of-mass offset between the inner halo and the baryonic disk. The method therefore directly constrains the present-day mass distribution that is actively shaping the Milky Way’s disequilibrium.

What the summary means in broader terms is that we now possess a clean, time-localized gravitational snapshot of how much mass the two largest satellites still retain after billions of years of tidal stripping. Because the measurement is instantaneous, it is less contaminated by the long-term orbital history that confuses traditional methods. This opens a path to tighter tests of galaxy formation physics, better calibration of the Milky Way’s response to external perturbers, and ultimately more robust inferences about the local dark matter density and the Galaxy’s total mass profile. The approach is extensible: future pulsar discoveries will shrink the error bars, while higher-resolution simulations will reduce model systematics.

**9. Shorter Summary**  
By treating 53 millisecond pulsars as precise accelerometers, the authors measure a north-south asymmetry in the Milky Way’s vertical gravitational field near the Sun. This asymmetry is produced by the Large Magellanic Cloud and Sagittarius dwarf pulling the dark halo and stellar disk centers of mass out of alignment and launching vertical waves. A grid of N-body simulations shows that only a heavy LMC combined with a medium-mass Sgr reproduces the observed asymmetry strength and shape. The resulting present-day bound masses—4.1 ± 1.0 × 10^{10} M_⊙ for the LMC within 16.6 kpc and 3.5 ± 2.4 × 10^8 M_⊙ for Sgr within 5 kpc—are the first obtained completely independently of stellar kinematics and agree with previous estimates. The work highlights the non-linear coupling between the two satellites and shows that static triaxial halos cannot explain the signal.

v3.5.4
