---
tags: [papers, cosmology, 21cm, meerkat, intensity-mapping]
last_updated: 2026-09-05
status: analysis-ingest
related_papers: [cosmology-expansion-history-and-structure, baryon-acoustic-oscillations]
source_analysis: "raw/analyses/2026-09-04_doi-10.3847-2041-8213-ae808f_hi-intensity-mapping-meerkat-autopower-detection.md"
---

# MeerKAT HI Intensity Mapping Autopower Detection

**One-line summary:** First SKA-precursor solo detection of unresolved 21 cm autopower (no galaxy survey); split-half cross + high-k modes dodge ~1e5 foregrounds; significance tempered in review (~3.2σ conservative). ApJL DOI 10.3847/2041-8213/ae808f.

## Key claims and results

- Auto-power (HI × HI, no optical catalog) of the unresolved 21 cm intensity field with MeerKAT interferometer on the DEEP2 field (~96 hr) at z ≈ 0.32 and 0.44, down to ~Mpc scales.
- Pipeline stays in the visibility / delay-spectrum domain: calibrate to ~10⁻⁵ gain error, split into independent halves, cross-correlate so shared sky squares and noise bias cancels, keep only modes above a conservative wedge cut ($k_\parallel > 0.3\,k_\perp$), flag residual systematics with Stokes-V noise sims.
- Published ApJL reports two systematics frameworks: conservative baseline-flagging at **3.2σ / 3.5σ** and a less conservative power-spectrum-flagging path at **5.9σ / 9.18σ**; arXiv v1 had quoted 8.0σ / 11.5σ and a "first" claim later dropped from the title.
- Sub-mK rms HI fluctuations at 1 Mpc reported (v1 numbers; treat published values as the authoritative ones when they diverge). Halo-model / HIMF fits largely unconstrained and prior-dominated.
- Null test (disjoint frequency bands) consistent with zero leftover correlated power.

## Physical intuition

Every hydrogen cloud rings a fixed 21 cm tuning fork; redshift turns frequency into a distance ruler, so a radio cube is a 3-D matter map. Intensity mapping sums unresolved beacons instead of cataloging galaxies. Foregrounds (synchrotron, radio galaxies) outshine HI by ~10⁵; they are spectrally smooth and pile up at low $k_\parallel$, while HI ripples across frequency. Cross-checking independent data halves kills noise bias; refusing to look inside the foreground wedge (and flagging residual stripes) is how the autopower stands without a galaxy-survey crutch.

## Limitations and assumptions

- One field, one instrument, ~2 deg²; no independent replication at these scales/redshifts.
- Significance fell under review; residual short-baseline MeerKAT artifact still under investigation.
- "Auto-power" means same tracer (HI × HI), not autocorrelating one cube with itself — the measurement always cross-correlates independent splits.
- 1-D binning leaves velocity-dispersion / shot-noise degeneracy unbroken; small scales mix shot noise and Fingers-of-God.
- Primacy landscape contested (CHIME z ~ 1 auto-power; MeerKLASS single-dish; GMRT limits) — narrow "first" (interferometric Mpc-scale autopower at z ≈ 0.3–0.44) is the defensible claim.

## Connections

- Cosmology structure / expansion: [[cosmology-expansion-history-and-structure]]
- Large-scale clustering rulers: [[baryon-acoustic-oscillations]]

## Source

- `raw/analyses/2026-09-04_doi-10.3847-2041-8213-ae808f_hi-intensity-mapping-meerkat-autopower-detection.md`
