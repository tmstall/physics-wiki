---
tags: [papers, strong-lensing, muse, desi, cosmography, spectroscopy]
last_updated: 2026-10-09
status: analysis-ingest
related_papers: [holismokes-sn-winny, fdm-wave-lensing-hs0810, desi-evolving-dark-energy, radio-galaxy-z4946]
source_analysis: "raw/analyses/2026-10-09_lin-2026-apjs-286-9_muse-confirmation-desi-lens-candidates.md"
---

# MUSE Confirmation of DESI Strong-Lens Candidates

**One-line summary:** MUSE on the VLT takes 76 of the best southern neural-net lens candidates and measures redshifts: 55 systems get a lens+source pair (47 robust for both), 15 remain lens-only, and 6 are impostors (spiral arms, tidal tails, foreground blobs). Lin et al., ApJS 286:9 (2026), DOI 10.3847/1538-4365/ae844d.

## Key claims and results

- **Paper:** Lin et al., *ApJS* **286**:9 (2026 September). DESI Strong Lens Foundry Part IV. 74-page catalog. Neural net on DESI Legacy Imaging → ~3,500 candidates; this paper is southern spectroscopic follow-up with MUSE integral-field cubes (five ESO filler programs, 2022–2024). 175 blocks requested, 100 executed, 92 useful, 76 distinct targets, 223 extracted spectra.
- Verdicts: 55 confirmed (lens and at least one source redshift), 15 lens redshift only, 6 not lenses. Typical lens $z\sim0.4$, typical source $z\sim1.4$. ~2/5 of source redshifts sit past where the [O II] doublet leaves the MUSE window, so those use weaker UV absorption (Fe, Mg, C, Lyα).
- Headline “55 with both redshifts” includes quality flags 2–3. **47** have a robust (flag 1) value for both. One “confirmed” lens redshift is photometric from neighboring red galaxies, not a spectrum. Three confirmed sources are flag “possible” only.
- Standouts: two double-source-plane systems (one with sources at $z\sim1.3$ and $z\sim3.0$, possible Lyman-break galaxy; one at $z\sim1.7$ and $z\sim3.5$ with textbook Lyα). A lens at $z\sim1.1$. Complete four-image redshifts for CSWA 20 (matches Pettini et al. X-shooter to ~200 km s$^{-1}$) and the team’s Einstein cross. Cluster-lensed quasar SDSS J2222+2745.
- Impostors (the instructive result): two spiral arms sharing the galaxy’s lines; one tidal tail between mergers; one star-forming knot at the galaxy redshift; two “arcs” in *front* of the supposed lens. Object X inside a confirmed field is also at the lens redshift.
- Quoted redshift errors are fit-covariance only. Smallest correspond to ~1 km s$^{-1}$; MUSE’s resolution element is ~75–150 km s$^{-1}$. In 6 of 14 image pairs of a claimed single source, images disagree by >3× combined quoted error. Worst: two images of one quasar differ by ~570 km s$^{-1}$ (~13σ on the quoted errors). Geometry still works (part in a thousand is enough); using those differences to split “one source” vs “neighbors” does not.

## Physical intuition

A strong lens is several CDN routes to one file. Spectroscopy is the barcode test: every line stretches by the same factor $1+z$. The foreground galaxy’s calcium H&K (old, red elliptical) must sit at a *smaller* stretch than the arc’s [O II] doublet or UV absorption. If the “arc” shares the galaxy’s barcode, it is a spiral arm or a tidal tail, not a background source.

MUSE’s value is the data cube: point once, then decide what to extract. A slit would need several pointings and prior knowledge to catch a second source plane, a group of lens galaxies, or a dwarf sitting in front of an arc. Filler time buys volume at the cost of weather: almost half the requested blocks never ran, which explains most of the 15 lens-only outcomes.

Double-source-plane systems are the cosmology prize. Two rings behind one lens give a distance-ratio lever that does not care how massive the lens is — a dark-energy handle independent of BAO/SN, once imaging and mass models catch up (Carousel Lens companion already tries; error bars still modeling-dominated).

## Limitations and assumptions

- Hand-picked high-ranked southern candidates under filler seeing. Confirmation rate does not carry to the full ~3,500. 15 lens-only systems are open cases, not rejections.
- Line ID, apertures, and quality flags are one-person visual judgments. No automated template, no second inspector. Companion DESI/Keck papers (Foundry II–III) are the independent spectrograph check.
- Table bugs for catalog users: two source rows copy another system’s coordinates (>10° off); one non-lens arc has another target’s coordinates; some photometry rows duplicate; Fig. 67 plots a $z\sim0.25$ “source” that Table 2 does not have. One lens magnitude 7.8 is impossible.
- Seven robust systems are single giant arcs. The field usually accepts those; a strict multiple-image cut drops the robust count to ~40.
- No lens model or mass measurement in this paper. “Confirmed” means the geometry is spectroscopically right.

## Connections

- Time-delay cosmography path (lensed SLSN, delays not yet measured): [[holismokes-sn-winny]], [[time-delay-cosmography]]
- Wave-halo lensing (different lensing science): [[fdm-wave-lensing-hs0810]]
- DESI as an expansion-history probe (different DESI product): [[desi-evolving-dark-energy]]
- Other VLT spectroscopic confirmation of rare high-$z$ objects: [[radio-galaxy-z4946]]
- Concepts: [[strong-gravitational-lensing]]
- Synthesis: [[cosmology-expansion-history-and-structure]] (Thread A, geometric $H_0$ / distance-ratio path)

## Open questions

- DESI/Keck (Papers II–III) reproduce flag 2–3 source redshifts to ~1 part in 1,000?
- High-resolution imaging of the 15 lens-only systems: predicted counter-images?
- Double-plane systems: space-based imaging + mass models tight enough for dark energy, or still systematics-limited like Carousel?

## Source

- `raw/analyses/2026-10-09_lin-2026-apjs-286-9_muse-confirmation-desi-lens-candidates.md`
