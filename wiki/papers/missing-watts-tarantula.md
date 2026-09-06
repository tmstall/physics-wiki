---
tags: [papers, stellar-feedback, xray, lmc, 30dor]
last_updated: 2026-09-05
status: analysis-ingest
related_papers: [high-energy-astrophysics-multimessenger, plasma-hed-lab, pulsar-wind-nebulae]
source_analysis: "raw/analyses/2026-09-04_apj-998-318_missing-watts-tarantula.md"
---

# Missing Watts of the Tarantula (30 Dor / R136 Wind Bubble)

**One-line summary:** 2 Ms Chandra + JWST/HST/Spitzer show the 30 Dor wind bubble is leaky (46–73% of X-ray gas inside the warm shells); dust and hot-gas temperatures decorrelate once the shared radial trend is removed; modern feedback sims get the shell right but dark soft interiors versus the observed flat harder glow — conduction / mass-loading is the leading suspect (*ApJ* **998**:318).

## Key claims and results

- Deep T-ReX Chandra stare (~2 Ms, 54 ObsIDs) of 30 Doradus / R136, cross-matched region-by-region with JWST NIRCam (PAH/dust), Spitzer dust SEDs, and HST Hα shells.
- Hot shocked wind: $kT \approx 0.24$–$0.88$ keV (~3–10 MK), $n_e \sim 0.04$–$0.21\,{\rm cm}^{-3}$ (lower limits at filling factor 1); hottest near R136.
- Dust vs hot gas: both cool gently with radius (shallower than $r^{-2}$ / adiabatic $r^{-4/3}$ textbook scalings). After binning by distance and subtracting the median radial trend, **residuals are uncorrelated** — dust is not collisionally heated by the X-ray plasma.
- Sputtering lifetimes ~0.85–1 Myr for $0.1\,\mu{\rm m}$ grains at typical measured $T,n$; comparable to R136’s age — dust overlapping X-rays sits in front of (shell), not inside, the hot gas; higher absorbing columns where dust is bright corroborate.
- Confinement proxy from segmented radial profiles: X-rays peak a few pc *interior* to Hα and stay relatively flat; apparent enclosed X-ray fractions **46% (R136), 55% (north), 73% (east)** — half to three-quarters bottled; fragmented arc-like Hα morphology implies venting.
- Forward-modeled Lancaster-class radiation+wind sim reproduces gross onion (X-rays in, Hα shell out) but fails two linked symptoms: **limb-brightened soft interface with dark interior** in the mock, versus **flat interior + substantial medium-band** in the data. Proposed fix: thermal conduction → evaporative mass-loading brightens and hardens the volume. Inverse-Compton from CR electrons flagged as an unexplored alternative.

## Physical intuition

Classic Weaver bubbles are sealed pressure cookers: wind heat stays bottled and should blaze in soft X-rays. Real 30 Dor behaves like a leaky pressure vessel with aggressive cooling at turbulent hot–cold interfaces (the ~$10^5\,{\rm K}$ cooling peak). Dust is a bystander in the walls, warmed by starlight — not a partner of the ten-million-degree gas. Sims that get the mixing-layer *rim* right still leave the cavity dark and soft; conduction that pages cold shell mass into the hot volume is the candidate that fills and hardens the middle in one stroke.

## Limitations and assumptions

- “Confinement fractions” are projected surface-brightness proxies under assumed spherical sections — not direct energy budgets; segment choice and projection matter.
- Densities assume filling factor 1 → lower limits; smaller filling factors raise $n$ and shorten sputtering times.
- Simulation confrontation uses a generic ~$5\times10^3\,M_\odot$, solar-metallicity cluster — not an R136 twin; only normalized profile *shapes* are compared.
- Conduction-as-missing-ingredient is contested in 2026 literature (M82 winds endorse it; other theory work favors geometry/mixing).
- Soft-band, single-$T$ spectral model; residual nonthermal / unresolved-source contamination in harder bands remains a soft spot (N157B PWN excised from the bandpass).

## Connections

- Synthesis: [[high-energy-astrophysics-multimessenger]] (stellar feedback / multiwavelength engines)
- Lab / multiphase plasma analogy (optional): [[plasma-hed-lab]]
- Nearby PWN / hard X-ray contaminant context: [[pulsar-wind-nebulae]]
- Concept: wind-blown bubbles, turbulent mixing layers, thermal conduction, mass-loading

## Source

- `raw/analyses/2026-09-04_apj-998-318_missing-watts-tarantula.md`
