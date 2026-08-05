---
source: spacex_export
conversation_id: 3e3ce98e-aaf6-4aa8-a552-71967400444e
title: "Early Universe Ionization by Supermassive Stars"
created_at: 2025-08-20T05:21:46.495277Z
updated_at: 2025-08-20T05:23:08.207774Z
n_responses: 2
platform: grok/xAI
pilot: false
---

# Early Universe Ionization by Supermassive Stars

## Human

Please analyze this stock. Include i background information, simple math is okay. Use examples for appropriate

## Assistant

### Background Information

The paper titled "Flash Ionization of the Early Universe by Pop III.1 Supermassive Stars" is a scientific article authored by Jonathan C. Tan, affiliated with Chalmers University of Technology and the University of Virginia. It was originally posted on arXiv (a preprint server for physics and astronomy papers) on June 2025, with a revision in August 2025. The paper discusses a theoretical model for how the universe was partially ionized (meaning atoms lost electrons, creating plasma) very early in its history, around redshifts z ≈ 20–30 (roughly 100–200 million years after the Big Bang). This ionization is attributed to "Pop III.1" supermassive stars, which are hypothetical metal-free stars (Population III, or Pop III, refers to the first generation of stars with no heavy elements) that could grow to masses of about 100,000 solar masses (M⊙) and eventually form supermassive black holes (SMBHs) like those at the centers of galaxies.

To provide context:
- **Cosmic Reionization**: After the Big Bang, the universe was hot and ionized, but it cooled and became neutral (atoms formed) around z ≈ 1100. Later, sources like stars and galaxies reionized the intergalactic medium (IGM) by emitting ultraviolet light that stripped electrons from hydrogen atoms. Standard models attribute most reionization to galaxies at z < 10 (about 500 million years after the Big Bang), but this paper proposes an earlier "flash" phase from Pop III.1 stars.
- **Pop III.1 Theory**: This is a specific model for SMBH formation. Unlike "light seed" models (where black holes start small, ~10–100 M⊙, from normal star remnants) or "direct collapse" in larger halos, Pop III.1 suggests SMBHs form as "heavy seeds" (~100,000 M⊙) in small, pristine dark matter minihalos (~1 million M⊙). These stars are powered partly by dark matter annihilation (from weakly interacting massive particles, or WIMPs), allowing them to grow massive without fragmenting or evaporating. The theory predicts these stars ionize large bubbles in the IGM, suppressing further similar star formation and setting the cosmic density of SMBHs at about 0.1 per cubic megaparsec (cMpc⁻³).
- **CMB Optical Depth (τ)**: The cosmic microwave background (CMB) is radiation from the early universe. As it travels to us, it can scatter off free electrons in ionized regions, measured by τ (optical depth). Planck satellite data suggests τ ≈ 0.054–0.063 from standard reionization, but recent tensions in cosmology (e.g., "Hubble tension" where CMB-based expansion rates don't match local measurements, or hints of negative neutrino masses from DESI surveys) could be eased if τ is higher (~0.09). This paper argues Pop III.1 ionization adds ~0.04 to τ, pushing the total to ~0.10.
- **Other Implications**: The "Flash" could boost the cosmic radio background via free-free emission (electrons scattering in plasma), potentially explaining a deep 21-cm absorption signal reported by the EDGES experiment (though controversial).

This model contrasts with alternatives like Pop III.2 (ionized minihalos forming smaller stars) or direct collapse in larger halos, which struggle to produce enough SMBHs or explain the lack of intermediate-mass black holes (IMBHs, 100–10,000 M⊙).

### Key Analysis of the Paper's Model

The paper presents a simple, idealized calculation of the "Flash" ionization's impact, focusing on its contribution to τ. It assumes Pop III.1 stars form at high redshifts, create expanding HII regions (ionized bubbles), and ionize a large fraction of the universe briefly before recombination (electrons reattach to protons).

#### Main Assumptions and Parameters
- **Flash Epoch**: Peak ionization at z_flash = 20 or 25 (fiducial cases).
- **Ionization Fractions**: Peak ionization in HII regions (f_i,peak) = 0.5; volume fraction of universe ionized (f_i,vol) = 0.5. These are conservative; the model requires f_i,vol near 1 to explain SMBH abundance, but averages lower due to post-star expansion.
- **Timescales**:
  - Rise time (t_rise) to peak ionization: 30 million years (Myr), blending star lifetimes (~10 Myr) and Strömgren sphere establishment (ionized bubble in equilibrium).
  - Decline: Exponential decay on recombination timescale (~29–55 Myr, depending on z and overdensity ~3x mean IGM).
- **Ionizing Output**: Stars emit ~10^53 ionizing photons per second (S_53 = 1), creating bubbles ~1 cMpc in radius, independent of z.

The model ignores helium reionization and secondary sources like Pop III.2 stars or early AGN, assuming they're minor.

#### Simple Math and Calculations
The core calculation is the Thomson optical depth τ, which measures electron scattering of CMB photons. It's integrated along the line of sight:

τ = ∫ σ_T n_e ds

Where:
- σ_T = 6.65 × 10^{-25} cm² (Thomson cross-section).
- n_e = electron density (≈ hydrogen density n_H in fully ionized gas).
- ds = path length.

For a fully ionized mean-density IGM, each comoving Mpc contributes dτ ≈ 3.79 × 10^{-4}.

The paper integrates over the reionization history:
- Standard galaxies (from Robertson et al. 2015) contribute τ_gal ≈ 0.06 (reionization from z ≈ 10 to 5).
- Pop III.1 adds τ_PopIII.1 ≈ 0.04, for total τ ≈ 0.10.

Key equations:
1. **Ionization Timescale (t_ion)**: Time to establish a Strömgren sphere.
   t_ion = 1 / (α^{(2)} n_H) ≈ 51.3 [(1 + z_form)/31]^{-3} Myr
   - α^{(2)} ≈ 1.08 × 10^{-13} cm³ s^{-1} (recombination rate at 30,000 K).
   - Normalized to z=30 density n_H = 5.72 × 10^{-3} cm^{-3}.
   - Example: At z=25 (higher density), t_ion is shorter (~29 Myr), so recombination is faster.

2. **Bubble Radius (R_R)**: For R-type (rapidly expanding) HII regions.
   R_R ≈ 1.10 (t_*/10 Myr)^{1/3} (S/10^{53} s^{-1})^{1/3} cMpc
   - Determines SMBH density: n_SMBH = 3/(4π R_R^3) ≈ 0.18 / (t_* S_53) cMpc^{-3}.
   - Example: If t_* = 10 Myr and S=10^{53} s^{-1}, R_R ≈ 1.1 cMpc, leading to ~0.1 SMBHs per cMpc³, matching observations.

3. **Free-Free Brightness Temperature (T_B,ff)**: Radio emission from Flash plasma.
   T_B,ff ≈ 12.8 ν^{-0.118} T^{-0.323} f_clump^2 (s/10 pMpc) [(1+z)/26]^6 K
   - ν=1.4 GHz (radio frequency), T=30,000 K, clumping factor f_clump=10 (overdensity), path s=10 physical Mpc.
   - Integrated over history: ~1–3 K for z_flash=20–25.
   - Example: Doubling f_i,peak to 1 (full ionization) but halving f_i,vol to 0.25 keeps τ same but boosts T_B,ff, helping explain EDGES' ~67 K excess (vs. CMB's 50 K at z=17).

The paper notes linear degeneracy: τ scales with f_i,peak × f_i,vol. Maximal case (both=1) gives τ_PopIII.1 ≈ 0.15–0.16.

Figure 1 (described) shows τ vs. z: Galaxy curve plateaus at 0.06; Pop III.1 adds a high-z bump, totaling ~0.10, overlapping "high τ" band (0.09 ± 0.01) but above Planck's 0.06 ± 0.005.

#### Strengths and Examples
- **Resolves Cosmological Tensions**: Example – Hubble tension: CMB assumes low τ, giving H_0 ≈ 67 km/s/Mpc; higher τ allows H_0 ≈ 73 km/s/Mpc, matching supernova measurements. DESI BAO data implies negative neutrino masses under low τ; Pop III.1's extra ionization fixes this without exotic physics.
- **Testable Predictions**: 
  - 21-cm surveys (e.g., HERA, SKA) could detect ~1 cMpc HII bubbles at z>15.
  - CMB polarization (LiteBIRD) or patchy kSZ effect (Simons Observatory) could probe early ionization, though high-z reduces signal.
  - EDGES example: Flash adds ~1–3 K radio background; if confirmed, favors z_flash=25 (denser, brighter emission).
- **Uncertainties**: Idealized (uniform Flash); simulations needed for clumping, Pop III.2/AGN contributions. If added, τ increases, blurring phases.

### Overall Assessment
This paper strengthens the Pop III.1 model by linking SMBH origins to observable cosmology, predicting a distinct early reionization phase absent in standard models. It's motivated by astrophysics (SMBH abundance, no IMBHs) and eases ΛCDM issues without ad-hoc changes. However, it relies on unproven WIMP heating and faces challenges from current CMB data (τ too low) and 21-cm limits (no strong signals yet). Future observations could confirm or refute it—e.g., if SKA images early bubbles, it's supportive; if not, the model needs refinement. Simple math like the timescales shows the Flash is brief (~50 Myr), fitting a "flash" description without over-ionizing the universe prematurely.
