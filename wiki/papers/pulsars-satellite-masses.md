---
tags: [papers, astrophysics, pulsars, galactic-dynamics]
last_updated: 2026-08-01
status: analysis-ingest
related_papers: [loki-early-accreted-vmp]
source_analysis: "raw/analyses/List1_Combined_Clean.md"
---

# Pulsars as Accelerometers for Satellite Masses

**One-line summary:** Vertical acceleration asymmetry of solar-neighborhood millisecond pulsars yields kinematics-free mass estimates for the LMC and Sagittarius dSph — first such measurements independent of stellar velocity modeling.

## Key claims and results

- **Paper:** Donlon, Chakrabarti & Hunt, *Phys. Rev. D* (May 2026). DOI: 10.1103/zz5s-zwh8; arXiv:2512.10883.
- 54 MSPs from IPTA-class data; line-of-sight accelerations → vertical component vs height.
- Signal: up/down asymmetry driven by LMC/Sgr disk waves + halo–disk center-of-mass offset.
- N-body grid fit: LMC \(M(<16.6\,\mathrm{kpc}) = (4.1 \pm 1.0)\times 10^{10}\,M_\odot\); Sgr \(M(<5\,\mathrm{kpc}) = (3.5 \pm 2.4)\times 10^8\,M_\odot\).
- Acceleration is “short memory” — tracks live gravity, not integrated merger history.

## Physical intuition

Stellar kinematics are a hard-drive full of every past file. Accelerations are the live sensor reading — they go quiet when the disturbance ends. Pulsars are atomic clocks on free-fall trajectories; their Doppler residual is a nanometer-per-second-squared accelerometer. Asymmetry above vs below the plane is the trampoline surface telling you who is pushing from one side.

## Limitations and assumptions

- Only 54 nearby pulsars; solar-neighborhood pencil beam.
- Simulation fidelity (idealized N-body) load-bearing.
- Sgr mass uncertainty ~70%; SMC/LMC internal structure incomplete.

## Connections

- Concepts: [[galactic-accretion]]
- Assembly neighbors: [[loki-early-accreted-vmp]] (local fossils of early accretion), [[cosmos-web-cosmic-web]] (high-\(z\) environment).
- Dynamical-friction / pairing cousin (inclination filter for post-merger SMBH binaries — drag physics that also shapes how satellites and holes sink): [[smbh-inclination-angle]], [[dynamical-friction]], [[supermassive-black-hole-binaries]]
- PeVatron / pulsar-wind neighbor (different science, same compact-object zoo): [[aquila-booster-pevatron]], [[pulsar-wind-nebulae]]
- Young relativistic binary timing lab: [[psr-j1906-binary-timing]]

## Source

- Analysis section in `raw/analyses/List1_Combined_Clean.md` (Pulsars as Galactic Scales).
