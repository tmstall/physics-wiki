---
tags: [papers, electron-microscopy, condensed-matter, interferometry, phonons]
last_updated: 2026-08-29
status: analysis-ingest
related_papers: [3d-electron-diffraction-osc, positronium-diffraction-graphene, hot-electron-coherent-phonons-ptcu, attosecond-stm-lightwave]
source_analysis: "raw/analyses/2026-08-27_doi-10.1038-s41586-026-10914-9_atomic-scale-double-slit-interferometry-si.md"
---

# Atomic-Scale Double-Slit Interferometry in Silicon

**One-line summary:** A focused STEM probe aimed between two Si columns 1.36 Å apart turns the crystal itself into a double slit; correlated (not independent) thermal motion keeps high-order fringes alive to 900 K and converts fringe visibility into a local, anisotropic bond-stiffness meter (*Nature* 2026; DOI 10.1038/s41586-026-10914-9).

## Key claims and results

- **Paper:** Tabata, K., Seki, T., Susi, T., Ishikawa, R. & Shibata, N., “Atomic-scale double-slit interferometry with a focused electron probe,” *Nature* (2026). DOI 10.1038/s41586-026-10914-9.
- Setup: [110] Si dumbbell (column separation 1.36 Å); ~1.1 Å FWHM probe parked at the midpoint; 4D-STEM CBED on a JEOL ARM300CF + DELTA corrector + DECTRIS ARINA pixelated detector; ~360 crystallographically equivalent pairs averaged.
- Electron channelling delocalizes the probe over both columns → two coherent sources without engineered slits. Midpoint geometry produces fringes; on-column control does not. Idealized two-aperture Fraunhofer model matches fringe spacing.
- **Einstein (independent) vs correlated frozen-phonon models:** independent motion washes out all but the lowest fringe; phonon-correlated displacements reproduce the observed higher-order fringes from 300 K to 900 K.
- QEP separation of elastic vs inelastic scattering: coherent double-slit structure survives **inside thermal diffuse scattering** when motions are correlated — TDS is not automatically featureless noise.
- Extracted in-plane correlation coefficients (300 K): $\rho_x = 0.362 \pm 0.005$, $\rho_y = 0.184 \pm 0.005$ (95% CI); ab initio (ML-potential) phonon prediction $\rho_x \approx 0.39$, $\rho_y \approx 0.24$. Both rise modestly by 900 K ($\rho_x = 0.419 \pm 0.009$, $\rho_y = 0.288 \pm 0.010$) while keeping bond-parallel stronger than transverse.
- Minimal 1D harmonic-chain map: $\kappa_\alpha = \rho_\alpha/(1-\rho_\alpha)^2$ with $\kappa_\alpha = k_\alpha/K_\alpha$. At 300 K (using ab initio $\rho$), $\kappa_x/\kappa_y \approx 2.5$ — stretch vs shear anisotropy of the Si–Si bond, read from fringe visibility rather than bulk averages.
- Mode decomposition of mean-squared *relative* displacement: long-wavelength acoustic modes move neighbors in phase (little fringe loss); zone-boundary TA modes (e.g. L-point ~3.02 THz, X-point ~3.88 THz) dominate visibility loss.

## Physical intuition

Young’s slits usually live in a lab you build. Here the lab is the lattice: aim a sub-Å electron beam between two bonded columns and the crystal’s own electrostatic “waveguides” split the probe into two coherent sources. Independent jiggling would jitter the slit spacing shot-to-shot and erase fine fringes — the Debye–Waller story every crystallographer already knows. Bonded neighbors reject that common-mode noise: when one atom moves, its partner tends to move with it, so the *relative* separation stays nearly fixed. High-order fringes therefore survive inside what electron microscopists usually treat as unstructured thermal-diffuse fog — and the leftover visibility encodes how stiff that specific bond is along vs across its axis.

## Limitations and assumptions

- High-end hardware stack (aberration-corrected cold-FEG STEM + fast pixelated detector) — outside-lab replication is a real barrier, not a routine re-run.
- Stiffness extraction uses a simplified nearest-neighbour harmonic chain validated against full phonons for elemental Si; chemically asymmetric bonds, defects, and interfaces (named next targets, e.g. GaAs) are not demonstrated here.
- Correlations are in-plane ($x$, $y$ transverse to the beam); beam-parallel motion is excluded as negligible to first order on the projected pattern.
- Bulk defect-free Si is a validation target with known force constants — capability claim first, unknown-local-environment payoff later.
- Single-lab result with strong *internal* theory–data convergence (chain model, ab initio phonons, experiment), not yet a second-lab experimental repeat.

## Connections

- Synthesis: [[ultrafast-optics-and-solid-state-emitters]] (atomic-scale electron probe / solid-state measurement neighbor)
- Electron-diffraction / TEM neighbors: [[3d-electron-diffraction-osc]]
- Matter-wave diffraction cousin (different probe, same “wave through a lattice” language): [[positronium-diffraction-graphene]]
- Phonon / lattice-dynamics cousin (coherent phonons driven optically, not fringe-visibility stiffness): [[hot-electron-coherent-phonons-ptcu]]
- Atomic-scale electron probe neighbor (STM lightwave, different observable): [[attosecond-stm-lightwave]]

## Open questions

- Does the same $\rho \to \kappa$ dictionary survive at defects, interfaces, or chemically inequivalent pairs without a new on-site spring model?
- Can absolute local force constants (not only $\kappa = k/K$) be recovered by combining $\rho$ with measured vibrational amplitude, as the Supplementary Material sketches?
- Will an independent instrument stack reproduce fringe persistence inside TDS at 900 K?

## Source

- `raw/analyses/2026-08-27_doi-10.1038-s41586-026-10914-9_atomic-scale-double-slit-interferometry-si.md`
