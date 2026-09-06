---
tags: [papers, neutrinos, cosmic-rays, multimessenger, ice-cube]
last_updated: 2026-08-19
status: analysis-ingest
related_papers: [pks2233-neutrino-lensing, aquila-booster-pevatron, peters-cycle-cosmic-rays, beyond-iron-ultraheavy-cosmic-rays, lab-blazar-pair-instability, ice-core-fe60-local-cloud]
source_analysis: "raw/analyses/2026-08-16_doi-10.1126-science.adc9818_high-energy-neutrinos-galactic-plane.md"
---

# IceCube: High-Energy Neutrinos from the Galactic Plane

**One-line summary:** Ten years of IceCube cascade events plus a CNN classifier yield ~4.5σ (trial-corrected) evidence that high-energy neutrinos trace the Milky Way’s disk — the hadronic counterpart to Fermi’s diffuse gamma-ray glow.

## Key claims and results

- **Paper:** IceCube Collaboration, *Science* **380**, 1338–1343 (2023). DOI 10.1126/science.adc9818; arXiv:2307.04427.
- Dataset: May 2011–May 2021; 59,592 selected cascade events (~500 GeV–PeV); still background-dominated (~87% atmospheric ν).
- Method: CNN cascade classification + hybrid ML reconstruction; >20× more usable cascades than prior cascade Galactic-plane search; usable threshold ~500 GeV.
- Three Fermi-LAT-informed spatial templates differing mainly in high-energy CR spectral cutoff (π⁰, KRAγ⁵, KRAγ⁵⁰).
- Best template (π⁰): ~4.71σ pre-trial → **~4.48σ trial-corrected** (~4.5σ headline); below conventional 5σ “discovery” bar.
- Galactic contribution ~**6–13%** of the total astrophysical neutrino flux at 30 TeV; rest still extragalactic.
- Injection tests favor diffuse emission over known TeV source catalogs alone; unresolved faint point sources not ruled out.

## Physical intuition

Cosmic-ray nuclei are charged — Galactic B-fields scramble their arrival directions. Photons and neutrinos keep a true “return address.” Neutral-pion decays already paint Fermi’s gamma-ray plane; charged-pion decays should paint a matching neutrino plane. IceCube finally pulls that faint glow out of atmospheric backgrounds by treating cascade light-blobs as images a CNN can classify.

## Limitations and assumptions

- Single collaboration / single detector; no KM3NeT/Baikal confirmation at publication.
- CNN trained on ice Monte Carlo — ice optical mismodeling is a baked-in systematic.
- Cascades: better energy resolution, worse angular resolution than tracks; contours circularized for tractability.
- KRAγ best-fit normalizations undershoot model predictions (cutoff may differ).
- “Observation” in the *Science* title ≠ closed 5σ particle-physics discovery.

## Connections

- Companion neutrino-source candidate (blazar / lensing exploratory): [[pks2233-neutrino-lensing]]
- Concepts: [[astrophysical-neutrinos]], [[pulsar-wind-nebulae]]
- CR / PeVatron neighbors: [[aquila-booster-pevatron]], [[peters-cycle-cosmic-rays]], [[beyond-iron-ultraheavy-cosmic-rays]]
- Lab blazar cascade physics: [[lab-blazar-pair-instability]]
- Multi-messenger ice fossils (different messenger): [[ice-core-fe60-local-cloud]]
- Synthesis: [[high-energy-astrophysics-multimessenger]]

## Open questions

- Diffuse glow vs many unresolved Galactic neutrino sources?
- Will IceCube-Gen2 / KM3NeT push past 5σ with independent systematics?
- Which CR cutoff best matches a higher-statistics spectral shape?

## Source

- `raw/analyses/2026-08-16_doi-10.1126-science.adc9818_high-energy-neutrinos-galactic-plane.md`
