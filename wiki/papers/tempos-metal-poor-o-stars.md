---
tags: [papers, massive-stars, metallicity, stellar-winds, reionization]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [high-energy-astrophysics-multimessenger, lbt-yp-primordial-helium, early-universe-popiii-flash-ionization, ultra-metal-poor-stars]
source_analysis: "raw/analyses/2026-09-23_doi-10.3847-1538-4365-ae95f6_tempos-treasury-extremely-metal-poor-o-stars.md"
---

# TEMPOS Treasury of Extremely Metal-Poor O Stars

**One-line summary:** ApJS DOI 10.3847/1538-4365/ae95f6. Uniform FUV sample: 29 O stars, 6 galaxies, $Z<0.2\,Z_\odot$. Winds weaken with $Z$ as expected, but the lowest-$Z$ third fades faster than the smooth trend (preliminary). Bonus kinematic finds.

## Key claims and results

- Telford et al., ApJS 286:50 (2026); arXiv:2609.20928. HST-GO-17491 (Cycle 31 Large Treasury): 110 orbits, 12 new stars plus 17 archival, all brought to one COS standard (at least two gratings, common signal-to-noise floor, ~1150–1750 Å).
- Hosts within 1.6 Mpc: Leo P, Leo A, Sextans A, WLM, NGC 3109, IC 1613. Oxygen roughly 3–14% solar. Working bins: extremely metal-poor ($\lesssim 10\%\,Z_\odot$) and metal-poor (~10–20%). Labels are host-galaxy proxies, not yet the O stars’ own abundances.
- Survey-design and first-release paper. Mass-loss rates and full atmosphere abundances are deferred.
- Terminal velocities from C IV, two ways (blue edge and a Sobolev-with-exact-integration fit), stacked with Hawcroft et al. (2024) LMC/SMC using the same method. Smooth decline from the LMC through the SMC through the metal-poor bin, then a steeper drop in the lowest-$Z$ third. Authors flag it as preliminary.
- Blue edge overestimates the model fit by a median ~15% (~270 km/s). Four stars were too weak for a fit.
- Bonus finds: COS G140L at cenwave 800 Å shows a systematic blueshift up to ~200 km/s (do not use it for velocities). Eight of 29 stars (28%) are high-confidence velocity outliers relative to host rotation — runaway candidates, with unresolved binaries not ruled out.

## Physical intuition

Line-driven winds are a saturating bus. Hydrogen and helium barely absorb an O star’s ultraviolet; metal ions are the channels that carry photon momentum. More metals means more channels, but the strongest lines fill up first, so wind strength should fall as a fractional power of $Z$, not one-to-one. Below the SMC the old far-ultraviolet archive was a mismatched patchwork, so a trend and a data-quality glitch looked the same. TEMPOS makes the comparison fair. The lowest-$Z$ third falling off faster than that smooth curve is either a hint that “many lines, one smooth force” stops being statistical when almost no metal ions are left, or a hint that the bins simply hold different kinds of stars.

## Limitations and assumptions

- Both velocity estimators are proxies. True terminal speed and mass-loss rate need the announced non-LTE models, which can also kill the steeper-drop claim.
- Spectral type and luminosity class are uneven across bins (no early-O supergiants in the lowest-$Z$ third). The break may be a sampling artifact. Scatter inside one class is already hundreds of km/s.
- Metallicity bins come from host supergiants and nebulae, not from these O stars.
- A single-epoch velocity offset cannot separate a runaway from orbital motion in an unresolved binary.
- The G140L cenwave-800 bias is real, confirmed in unrelated 2025 data, and still unexplained.

## Connections

- Synthesis: [[high-energy-astrophysics-multimessenger]]
- Low-$Z$ / early-universe neighbors: [[lbt-yp-primordial-helium]], [[early-universe-popiii-flash-ionization]], [[ultra-metal-poor-stars]]

## Source

- `raw/analyses/2026-09-23_doi-10.3847-1538-4365-ae95f6_tempos-treasury-extremely-metal-poor-o-stars.md`
