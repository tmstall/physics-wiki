---
tags: [papers, optomechanics, entanglement, levitated-nanoparticles, quantum-optics]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [quantum-jumps-of-sound, dissipative-cavity-entanglement, macroscopic-crystal-entanglement-neutrons, ultraheavy-dm-levitated-magnet-polonaise, imaging-vacuum-fluctuations-qft]
source_analysis: "raw/analyses/2026-10-01_arxiv-2602.03456_stationary-entanglement-levitated-oscillator-optical-field.md"
---

# Stationary Entanglement of a Levitated Oscillator with Propagating Light

**One-line summary:** A room-temperature optical tweezer entangles the motion of a ~100 nm glass bead with light that has already left the cavity; the Gaussian entanglement witness sits only ~8% below the classical bound, and the state is not EPR-steerable. arXiv:2602.03456 (Deplano et al. 2026).

## Key claims and results

- **Paper:** Q. Deplano, A. Pontin, F. Marino & F. Marin (Firenze / INFN / CNR-INO / LENS), arXiv:2602.03456v2 [quant-ph], 20 March 2026. Preprint; no journal version found at analysis time.
- Platform: ~100 nm silica sphere (~1 fg, ~3.5×10⁷ atoms) in a 1064 nm tweezer at 3.5×10⁻⁸ mbar, coupled to a cavity by coherent scattering. Bright-mode frequency ~106 kHz. Resolved-sideband regime (cavity width κ/2π = 58 kHz).
- Two lasers, two jobs, on cavity modes two free spectral ranges apart. Red-detuned laser A cools the bright mode to ~1.45 phonons (~7 µK equivalent motion). Blue-detuned laser B creates photon–phonon pairs. The B photons leave as a travelling beam.
- Heterodyne records both outputs. A model fit only to the two power spectra predicts the full 16-element correlation table. Beam A, rescaled by calibrated efficiency η = 0.283 ± 0.006, cavity width, and coupling, reconstructs the bead’s position and momentum.
- Best Gaussian witness: $\nu_{-} = 0.918 \pm 0.029$ (stat) $\pm 0.02$ (sys) at a ~35 kHz filter, so logarithmic negativity $E_N = 0.12 \pm 0.04$. Entanglement turns on once the filter is ~20 kHz wide and survives >40 kHz of detuning. The steady-state model predicts a deeper $\nu_{-} \approx 0.884$; the authors blame slow phase drift and treat the data as a lower bound.
- Analyst recomputation of the printed Fig. 2b matrix gives $\nu_{-} \approx 0.932$, not 0.918. A simpler Duan test on the same matrix also sits just below the separable floor (~3%). A Gaussian steering test does **not** pass: entangled, not steerable, and nowhere near a Bell test.
- Intracavity entanglement is model-only. It appears for a motion angle chosen after the fact (~2°) and vanishes at the natural cavity-axis angle (~4.7°).

## Physical intuition

A trapped bead is a mass on a spring whose position and momentum cannot both be sharp. Red detuning is an eviction: each scattered photon takes one quantum of motion out into the light. Blue detuning is a paired write: each scattered photon leaves a matching quantum behind. Run blue alone and the motion runs away. Run both and the bead stays cold while the outgoing beam carries a faint twin of that motion.

“Room temperature” is the chamber, the gas, and the glass. The centre-of-mass motion is laser-cooled by ~40 million from the ~6×10⁷ phonons a 106 kHz oscillator would hold at 295 K. The quantum link is not heat-proof motion. It is a cryostat-free cooler plus a pair-creation laser.

The travelling light mode is not a mirror mode. You define it by the frequency window you integrate. Too narrow and you miss the mechanical response (two peaks, because the sideways modes couple). Too wide and you add vacuum noise. The paper scans that window instead of picking one in silence.

## Limitations and assumptions

- Single group, no independent levitation lab yet. The margin is thin: ~2–4σ if ±0.029 is a run-to-run standard deviation plus the systematic, higher if the figure bars are a standard error. The text and a caption disagree on which.
- Trusted-device readout. Noise comes from data, but the bead’s scale uses η, κ, and the coupling, and ~10% of each mechanical variance is filled in by the model outside a 40 kHz band. A 10% upward error in that variance nearly erases $\nu_{-} < 1$; 20% pushes the printed matrix back above 1.
- Detection efficiency 0.28 means ~72% of the light is lost before the detector. That caps the visible entanglement and rules out near-term network use.
- “Nonlocal” in the introduction is an application goal. What was shown is non-separability of a Gaussian state, not steering and not gravity-mediated entanglement. The bead is far lighter than picogram drums or the 16 µg cat crystal already entangled elsewhere. Gravity-test proposals want ~10⁻¹⁴ kg and superpositions much larger than the ~8 pm zero-point motion.
- Headline $\nu_{-}$ is not reproducible from any matrix printed in the analysis. Likely bookkeeping (axial-motion correction, or averaging blocks rather than matrices), not a sign the dip is fake. Worth one sentence from the authors.

## Connections

- Mechanical quantum readout, different platform: [[quantum-jumps-of-sound]] (phonon-number jumps in a chip resonator)
- Cavity entanglement as a designed steady state: [[dissipative-cavity-entanglement]]
- Heavier mechanical entanglement: [[macroscopic-crystal-entanglement-neutrons]]
- Same word “levitated,” different experiment: [[ultraheavy-dm-levitated-magnet-polonaise]] is a magnetomechanical dark-matter search, not motion–light entanglement
- Vacuum-fluctuation imaging cousin: [[imaging-vacuum-fluctuations-qft]]
- Synthesis: [[amo-quantum-state-control]]

## Open questions

- Will another levitation group (Vienna, ETH, Barcelona, Tokyo) reproduce $\nu_{-} < 1$ with its own calibration chain and a margin several times the error bar?
- Does better phase stability move the data from 0.92 toward the model’s 0.88, and can higher η reach steering?
- Do rotational modes or several beads in one cavity produce multipartite entanglement, as the authors propose?

## Source

- Wiki source (non-`sonnet_` twin): `raw/analyses/2026-10-01_arxiv-2602.03456_stationary-entanglement-levitated-oscillator-optical-field.md`
- Twin kept in raw, not a second page: `raw/analyses/sonnet_2026-10-01_arxiv-2602.03456_levitated-nanosphere-stationary-entanglement-optical-field.md`
