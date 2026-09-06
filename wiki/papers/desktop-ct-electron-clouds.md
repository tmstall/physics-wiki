---
tags: [papers, photoelectron, tomography, orbitals, ultrafast]
last_updated: 2026-09-05
status: analysis-ingest
related_papers: [chemistry-biotech-methods, ultrafast-optics-and-solid-state-emitters, 3d-electron-diffraction-osc]
source_analysis: "raw/analyses/2026-09-04_nodoi_desktop-ct-electron-clouds-3d-pot.md"
---

# Desktop CT for 3D Electron Clouds (Photoelectron Tomography)

**One-line summary:** Lab-table 3D orbital imaging in ~8 h via sparse recon + phase/sign recovery from intensity; HHG path to fs movies sketched but undemonstrated. Nodoi analysis.

## Key claims and results

- First table-top 3D photoemission orbital tomography (3D-POT): HHG EUV source (13–71 eV, fs pulses) + time-of-flight momentum microscope replaces synchrotron dense sampling.
- Cyclic-projections phase retrieval reconstructs full 3D orbitals (amplitude and sign/phase) from intensity on a few hemispherical shells in $k$-space, using support, sparsity, and symmetry constraints.
- PTCDA/Ag(110) HOMO and charge-transfer-filled LUMO imaged at ~0.75 Å resolution; 7 photon energies give high-quality reconstructions matching gas-phase DFT; 4 energies (~8 h total) are usable but more ambiguous.
- Algorithm recovers orbital phase structure (positive/negative lobes) without interpolating through Fourier nodes — first experimental test of the group's prior simulated CP method.
- Fs time-resolved 3D orbital movies are the explicit next step (sketch: ~80 h for 10 delays × 4 energies) but not demonstrated here.

## Physical intuition

Under the plane-wave final-state picture, ARPES momentum maps are the squared Fourier transform of a real-space molecular orbital. One photon energy samples one hemispherical shell in 3D $k$-space; changing energy changes the shell radius. Synchrotron 3D-POT stacked many closely spaced shells and interpolated. Sparse constraint satisfaction fills the gaps: measured magnitudes on a few shells plus "the orbital fits in this box, is sparse, and has this symmetry" recover both amplitude and sign — like reconstructing a sparse 3D array from a handful of curved-surface reads.

## Limitations and assumptions

- Plane-wave final-state approximation; final-state scattering can distort reconstructions for strongly interacting or non-planar adsorbates without an internal red flag.
- Phase ambiguity remains with sparse data (multiple similar-gap solutions); DFT or static support often breaks ties — risky for unknown excited-state orbitals.
- Demonstrated only on the well-behaved PTCDA/Ag(110) benchmark; gas-phase symmetry (including $z$-mirror) enforced for algorithmic stability even though the adsorbate bends slightly.
- Resolution ceiling (~0.75 Å) set by max photon energy (~71 eV); fs movies remain a projection, not a result.

## Connections

- Chemistry / orbital methods: [[chemistry-biotech-methods]]
- Ultrafast HHG / AMO sources: [[ultrafast-optics-and-solid-state-emitters]]
- Related 3D electron structural imaging: [[3d-electron-diffraction-osc]]

## Source

- `raw/analyses/2026-09-04_nodoi_desktop-ct-electron-clouds-3d-pot.md`
