---
tags: [papers, high-energy-astrophysics, cosmic-rays, pulsars]
last_updated: 2026-08-01
status: analysis-ingest
related_papers: [pulsars-satellite-masses, plasma-relativistic-amplifier]
source_analysis: "raw/analyses/List2_Combined_Clean.md (The Aquila Booster)"
---

# The Aquila Booster (LHAASO PeVatron PWN)

**One-line summary:** LHAASO sees PeV gamma rays from the pulsar-wind nebula of PSR J1849−0001—a pulsar ~50× weaker than the Crab that nonetheless outshines the Crab at PeV energies, forcing acceleration efficiencies \(\gtrsim 27\%\) that strain ideal-MHD termination-shock models.

## Key claims and results

- **Collaboration:** LHAASO; associated *Nature Astronomy*-class result (per analysis; arXiv 2603.15537 cited).
- Source: point-like UHE gamma emission tied to PWN of PSR J1849−0001; spectrum as power law into the PeV band.
- PeV luminosity several times the Crab’s despite far lower spindown power.
- X-ray constraints: nebular \(B \sim 3\,\mu\mathrm{G}\)—very low average field.
- Low \(B\) + high PeV output → acceleration efficiency at least ~27%, approaching or formally exceeding comfortable ideal-MHD ceilings under favorable assumptions.
- Interpretation: non-ideal MHD / magnetic reconnection upstream of (or instead of pure) termination-shock DSA may be required.
- Broader claim: extreme PeVatron efficiency may be generic to PWNe, not a Crab monopoly.

## Physical intuition

Think of the pulsar as a power supply and the nebula as a particle factory. The Aquila system runs on a small supply yet ships more PeV photons than the Crab. With a weak magnetic field (harder to confine / sync-cool), the only way the budget closes is if almost every erg of available power is shoveled into particles—past what standard shock models like to allow. That points to reconnection-style shortcuts in the wind.

## Limitations and assumptions

- Distance from dispersion measure (~20–30% systematics) scales luminosity and efficiency.
- \(B\) is a spatial average; unresolved structure could shift \(\eta\).
- Leptonic (IC) vs hadronic (pp → π⁰) origin not sealed; neutrinos would discriminate.
- Reconnection is implied, not spatially resolved (LHAASO angular scale).
- “Efficiency > 1” language means parameter-space exhaustion of the standard model, not a measured super-unity machine.

## Connections

- Pulsars / multi-messenger: [[pulsars-satellite-masses]]
- Extreme plasma acceleration (lab analog scale): [[plasma-relativistic-amplifier]]
- Direct multi-species spectra / Peters cycle below the knee: [[peters-cycle-cosmic-rays]]; ultraheavy UHECR path: [[beyond-iron-ultraheavy-cosmic-rays]]
- Key terms: a **PeVatron** is a Galactic accelerator reaching ~PeV particle energies (knee-scale), traced by UHE gamma rays.
- Concepts: [[pulsar-wind-nebulae]]

- Related (SpaceX set): [[magnetar-slsn-2017egm-fermi]] — Magnetar-powered SLSN GeV detection
- Synthesis: [[high-energy-astrophysics-multimessenger]] (HEA & multi-messenger map)

## Source

- Analysis: `raw/analyses/List2_Combined_Clean.md` — *The Aquila Booster.md*
