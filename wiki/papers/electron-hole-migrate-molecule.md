---
tags: [papers, attosecond, ultrafast, molecular, xfel]
last_updated: 2026-09-05
status: analysis-ingest
related_papers: [chemistry-biotech-methods, ultrafast-optics-and-solid-state-emitters, ultrafast-chemical-shifts]
source_analysis: "raw/analyses/2026-09-04_doi-10.1038-s41567-026-03360-x_electron-hole-migrate-molecule.md"
---

# Watching an Electron Hole Migrate Across a Molecule

**One-line summary:** Attosecond XFEL pulse pairs track hole migration on aromatic molecule atom-by-atom; spectrum-only benchmarks miss ionization amplitude phases; coherence ~7 fs before nuclear decoherence. Nat Phys DOI 10.1038/s41567-026-03360-x.

## Key claims and results

- First attosecond X-ray pump / attosecond X-ray probe of coherent electron dynamics in a polyatomic molecule (para-aminophenol) at LCLS.
- Pump (~260 eV, ~700 as) ionizes valence shell; probe near the oxygen K-edge (~523–529 eV) reports local hole density at oxygen via transient X-ray absorption (Auger-Meitner readout).
- Three timescales: sub-fs super-Coster-Kronig autoionization of states above the DIP (~21 eV; lifetimes 0.35–0.86 fs); few-fs coherent charge-migration oscillations (~2–8 fs); overall decay with fit constant ~6.8 fs (~7 fs coherence window) attributed to nuclear motion.
- Two state-of-the-art calculations (ADC and RAS-SXD) both match the photoelectron spectrum (amplitude magnitudes) but disagree on the time-domain trXAS signal — phases of ionization amplitudes control the dynamics and are invisible to the spectrum.
- Agreement with experiment is qualitative; absolute trXAS magnitudes are scaled; nuclear decay enters as a phenomenological factor, not first-principles nuclear dynamics.

## Physical intuition

Sudden ionization launches a coherent superposition of cation states — a hole that can slosh across the molecular framework on attosecond-to-few-femtosecond timescales without needing nuclei to move. The oxygen K-edge probe is a conditional read: it only absorbs strongly when valence hole density sits near oxygen. The photoelectron spectrum is like a checksum of ionization amplitudes — it checks populations, not coherences. Time-domain absorption is the integrity check that catches phase disagreements spectrum-only benchmarks miss.

## Limitations and assumptions

- Fixed-nucleus calculations; the ~7 fs decay is a fit parameter, not simulated nuclear motion.
- Absolute cross-sections not predicted; methods scaled to experiment.
- Pump–probe overlap region poorly treated; randomly oriented gas-phase sample averages away orientation dependence.
- Single-facility, single-group result; no independent experimental replication yet.

## Connections

- Methods / chemistry: [[chemistry-biotech-methods]]
- Ultrafast sources and probes: [[ultrafast-optics-and-solid-state-emitters]], [[ultrafast-chemical-shifts]]

## Source

- `raw/analyses/2026-09-04_doi-10.1038-s41567-026-03360-x_electron-hole-migrate-molecule.md`
