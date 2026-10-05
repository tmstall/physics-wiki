---
tags: [papers, cosmology, 21cm, chime, intensity-mapping]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [hi-intensity-mapping-meerkat, baryon-acoustic-oscillations, desi-evolving-dark-energy, cosmology-expansion-history-and-structure]
source_analysis: "raw/analyses/2026-10-04_arxiv-2511.19620_chime-21cm-auto-power-detection-z1_plain.md"
---

# CHIME 21 cm Autopower at Redshift ~1

**One-line summary:** CHIME detects the unresolved 21 cm autopower at z ≈ 1.16 at 12.4σ by cleaning every 10-second snapshot before averaging; the detection is hydrogen on fine scales, and the baryon-acoustic ruler the telescope was built for is filtered out on purpose. arXiv:2511.19620.

## Key claims and results

- **Paper:** CHIME collaboration, arXiv:2511.19620v2 (26 March 2026). Unrefereed preprint at analysis time. Wiki source is the plain-language rewrite; the technical twin is kept in raw. Companion interpretation: arXiv:2603.25680 (read at abstract level in the analysis).
- Data: 94 clean nights from 2019, a band around redshift 1.16, about 2,200 square degrees. Daytime data are dropped. Three interference detectors throw out ~40% of the night-time data in this band. The beam is weighted so its shape does not change with frequency.
- The measurement is an auto-power: even-night maps crossed with odd-night maps, no optical catalog in the detection itself. Foregrounds are ~10⁴ times brighter and spectrally smooth. The new pipeline filters every 10 s snapshot with that snapshot’s own mask **before** any average, and records what the filter did so simulations can be passed through the same operator. HyFoReS (a shared leakage template from a daily calibration error) is a modest extra layer, not the main fix. Antenna cross-talk is subtracted. About a third of the patch is masked around bright sources, plus 40 narrow hydrogen absorbers (1 known, 39 new candidates).
- Result: 12.4σ by the most conservative of three noise tests (the others ~13σ). Each frequency half detects the signal on its own at ~9σ with agreeing amplitudes. The imaginary part, even-minus-odd, the polarized map, two sky halves, short versus long baselines, and tighter source masks behave as noise or as unchanged signal. Stacking on 33,000 quasars recovers a consistent amplitude at 9σ. Junk would inflate the auto-spectrum without knowing where quasars are.
- What is measured is one combination: hydrogen amount times clumpiness, plus two loose shape knobs. The amplitude carries roughly ±30% statistical and ~17% systematic uncertainty. 12σ means “not zero,” not “known to 8%.” Most of the detection weight sits in the three largest bins that survive, right next to the filter edge. Dropping them still leaves ~7σ. The error bars are noise-only, so they omit the signal’s own sample variance.
- The companion paper (abstract-level here) says IllustrisTNG misses the small-scale hydrogen clustering by ~3–4σ, apparently through motions inside galaxies rather than the total hydrogen budget.

## Physical intuition

Every hydrogen atom is a 21 cm tuning fork. Expansion turns frequency into distance, so a radio cube is a 3-D map of unresolved gas. Cross-correlating with a galaxy catalog is the safe way to find that glow: foregrounds do not know where the galaxies are. An autopower has no outside catalog. Any leftover that repeats from night to night looks exactly like signal.

The failure mode this pipeline kills is manufactured roughness. Two smooth nights with different interference masks, averaged first, become a jagged map. Cleaning each snapshot before the average never creates that jaggedness. The price is the filter itself: it also deletes the large-scale modes, including the baryon-acoustic ruler. What remains is the fine-scale hum.

## Limitations and assumptions

- One instrument, one year, one patch, closest antenna spacings excluded. No independent telescope has confirmed an autopower at this redshift. Seven more years of CHIME would test stability. They would not be an independent experiment.
- Large scales, including BAO, are thrown away. This is not yet a dark-energy measurement. See [[baryon-acoustic-oscillations]] for the ruler this detection does not use.
- The shape model is loose, and its best-fit parameters sit in an odd place. The authors say the averaged answers are what count.
- Measured noise is a couple of percent higher than theory, for reasons not understood. A 10% noise underestimate would move 12.4σ by about 1σ.
- Null tests can miss a small consistent offset. The analysis notes that all eight imaginary points, and seven of eight polarized bins, sit slightly above zero. Each official null test still passes. That pattern was read by eye and chosen after looking. It does not threaten the detection. It matters only for percent-level amplitude claims.
- “No galaxy survey” is true of the detection. The unit conversion uses a beam model, redshift trends use outside fitting formulas, and the strongest anti-contamination argument is the quasar stack.
- MeerKAT’s lower-redshift autopower, which CHIME cites at high significance, is the revised ~3–3.5σ result on [[hi-intensity-mapping-meerkat]], not the earlier 8–11σ draft numbers.

## Connections

- Lower-redshift interferometric autopower, different claim and lower significance after review: [[hi-intensity-mapping-meerkat]]
- The ruler this pipeline discards: [[baryon-acoustic-oscillations]], [[desi-evolving-dark-energy]]
- Synthesis: [[cosmology-expansion-history-and-structure]]

## Open questions

- Does a gentler filter recover the large-scale ruler without reintroducing the mask-induced ripples?
- Does the amplitude stay put as the seven-year archive and tighter masks are added? Shrinkage would mean some of the power was contamination.
- What are the 39 absorber candidates, and does another telescope (CHORD, HIRAX, Tianlai, or MeerKAT at higher redshift) recover the same fine-scale amplitude?

## Source

- Wiki source (plain-language twin): `raw/analyses/2026-10-04_arxiv-2511.19620_chime-21cm-auto-power-detection-z1_plain.md`
- Technical twin kept in raw: `raw/analyses/2026-10-03_arxiv-2511.19620_chime-21cm-auto-power-detection-z1.md`
