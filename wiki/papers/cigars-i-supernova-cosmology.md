---
tags: [papers, cosmology, astrophysics, machine-learning]
last_updated: 2026-07-31
status: analysis-ingest
related_papers: [cosmos-web-cosmic-web]
source_analysis: "raw/analyses/CIGaRS I.md"
---

# CIGaRS I: Physics-Based Supernova Cosmology

**One-line summary:** A single hierarchical forward model (galaxies → Type Ia progenitors → light + dust + selection) inverted with set-based neural ratio estimation recovers cosmology and the physical origin of the supernova “mass step” from photometric data alone.

## Key claims and results

- Replaces the ad-hoc host-galaxy **mass step** correction with end-to-end physics: Prospector-β galaxy evolution + delay-time distribution (DTD) + metallicity/age-dependent intrinsic brightness + correlated dust + LSST-like selection (Simple-BayeSN SN summaries).
- Inference engine: **set-based TMNRE** (truncated marginal neural ratio estimation) — treats each host + its SNe as an unordered set; marginalizes huge latent stacks without MCMC sampling every object.
- On mocks (~16 000 SNe + hosts to \(z = 0.9\)): recovers input cosmology, DTD, metallicity/age slopes; photometric redshifts with median scatter ~0.01 and no catastrophic outliers in the reported challenge; cosmology constraints ~4× tighter than spectroscopic-subset style analyses (per analysis).
- Finding: metallicity trend largely *mimics* the classic mass step — the patch was hiding a chemical/age effect.

## Physical intuition

Type Ia supernovae are almost-standard candles after shape/color corrections, but residual brightness correlates with host properties. The community’s “5% offset above 10¹⁰ solar masses” is a hardcoded performance patch. CIGaRS rebuilds the whole plant model: star-formation history sets metallicity and age, those set explosion rate and intrinsic brightness, the same dust reddens host and SN, cosmology dims the light, selection decides who enters the catalog — then a neural net reads the whole photometric set at once.

## Limitations and assumptions

- Still **mocks**; real LSST purity, host mismatch, and typing errors not fully injected.
- Fidelity limited by stellar-population synthesis and assumed linear slopes / DTD forms.
- Scaling from 16k to millions needs more compute / algorithmic work.
- Explicitly “Paper I” — science payoff on real data is future work.

## Connections

- Concepts: [[type-ia-supernovae]], [[photometric-redshifts]]
- Cosmology neighbor: [[cosmos-web-cosmic-web]] (environment and structure at high \(z\); different observables, same LSST/JWST era of large photometric samples).
- Independent \(H_0\) path (lensed SLSN time delays, not ladder standardization): [[holismokes-sn-winny]]; tension context: [[hubble-tension]].
- Dark-energy expansion history (BAO + SN combinations prefer evolving DE over pure \(\Lambda\)): [[desi-evolving-dark-energy]], [[dark-energy-equation-of-state]], [[baryon-acoustic-oscillations]] — CIGaRS-style host physics feeds the SN systematics that those combinations depend on.

## Open questions

- Performance on real photometric samples with realistic contamination?
- More flexible progenitor physics (scatter, viewing angles)?
- Joint inference with large-scale structure density fields?

## Source

- Analysis: `raw/analyses/CIGaRS I.md`
