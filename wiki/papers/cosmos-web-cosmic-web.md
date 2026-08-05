---
tags: [papers, cosmology, galaxies, jwst]
last_updated: 2026-07-31
status: analysis-ingest
related_papers: [cigars-i-supernova-cosmology]
source_analysis: "raw/analyses/Cosmic_web.md"
---

# COSMOS-Web: Galaxy Evolution in the Cosmic Web to \(z \sim 7\)

**One-line summary:** The largest contiguous JWST survey maps large-scale overdensity to \(z \sim 7\) and shows dense environments flip from fueling early star formation to quenching low-mass galaxies after \(z \approx 1.8\).

## Key claims and results

- **Paper:** Hatamnia et al., *ApJ* 2026; 1002 (2): 192; DOI: 10.3847/1538-4357/ae5bac. Survey: COSMOS-Web, 0.54 deg² NIRCam, ~164k galaxies with robust photo-\(z\).
- Density field via weighted adaptive kernel density estimation using full \(P(z)\) weights across ~157 comoving slices.
- Stellar mass correlates positively with overdensity \(\delta\) at all redshifts studied.
- **SFR–density reversal** near \(z \approx 1.8\): dense regions mildly elevate SFR at high \(z\); suppress it (especially for quiescent systems) at low \(z\).
- Quenching handover: mass quenching dominates \(z \gtrsim 2.5\); mass and environment comparable \(0.8 \lesssim z \lesssim 2.5\); environmental quenching stronger for low-mass (\(M_\star \lesssim 10^{10}\,M_\odot\)) systems below \(z \sim 0.8\).

## Physical intuition

The cosmic web is not scenery — it is traffic infrastructure. Early on, filaments and protoclusters are gas pumps: mergers and cold streams feed star formation in dense nodes. Later, the same downtowns become hostile — hot halos, strangulation, ram pressure — and engines stall first in smaller galaxies. JWST finally gives enough deep, wide near-IR galaxies to watch that role reversal in one continuous dataset from the first billion years to now.

## Limitations and assumptions

- Highest-\(z\) bin has modest counts (~1 100 galaxies in 5.5–7); treat correlations cautiously.
- Masses/SFRs from SED fitting — dust–age–metallicity degeneracies remain.
- Single field → cosmic variance for rare overdensities.
- No direct cold-gas or kinematic measurements of the fueling/quenching mechanisms.

## Connections

- Concepts: [[cosmic-web]], [[photometric-redshifts]]
- Photometric large-sample theme shared with [[cigars-i-supernova-cosmology]] (SNe as distance tools vs. galaxies as web tracers).
- High-\(z\) transient / lensing cosmography neighbor: [[holismokes-sn-winny]] (lensed SLSN path to \(H_0\), not density-field mapping).
- Local galactic-assembly fossil neighbor: [[loki-early-accreted-vmp]] (early-accreted VMP stars vs high-\(z\) web mapping).
- Large-scale gravity *dynamics* (pairwise kSZ force-law test, not photo-\(z\) density maps): [[newton-ksz-force-law]].
- Nearby group baryon cycle (metals moved by sloshing, shocks, and jets in the hot IGrM — local counterpart to environmental processing in the web): [[ic1262-metal-mixing]], [[intragroup-medium]], [[gas-sloshing]].

## Open questions

- Spectroscopic confirmation of \(z > 4\) overdensities?
- ALMA / MIRI gas comparisons dense vs. field?
- Matched hydro simulations for the \(z \sim 1.8\) flip?

- Related (SpaceX set): [[muse-quasar-filament-z3]] — MUSE filament emission map

## Source

- Analysis: `raw/analyses/Cosmic_web.md`
