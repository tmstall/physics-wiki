---
tags: [papers, pulsars, general-relativity, binary-neutron-stars]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [pulsars-satellite-masses, gw170817-jet-hubble, second-order-gw-strain-gauge, horizon-direct-wave-gw250114]
source_analysis: "spacex_export/extracted-analyses/2026-02-17_long-term-timing-of-psr-j1906-0746-binary_19e0bfc4.md"
---

# Long-Term Timing of PSR J1906+0746

**One-line summary:** Eighteen years of multi-telescope timing of the young relativistic binary pulsar J1906+0746 tightens post-Keplerian parameters (total mass ~2.61 $M_\odot$), characterizes a Vela-scale glitch, and finds tentative $\dot x$ hints of companion spin–orbit coupling (Vleeschower et al., arXiv:2602.05947).

## Key claims and results

- **Paper:** L. Vleeschower et al., arXiv:2602.05947 (2026) — long-term timing of PSR J1906+0746.
- System: young (not recycled) radio pulsar, $P\sim144$ ms, orbital period ~4 h.
- Data: Arecibo, FAST, Green Bank, Lovell, MeerKAT, Nançay over ~18 years; TEMPO2 DD relativistic binary model + Gaussian-process red noise.
- Post-Keplerian: periastron advance, Einstein delay, orbital decay (GW-dominated); GR-assumed total mass ~2.6133 $M_\odot$, components ~1.3 $M_\odot$ each (analysis framing).
- Major glitch near MJD 56664 with permanent + decaying frequency components (Vela-class size in a non-Vela pulsar).
- Tentative secular change in projected semi-major axis $\dot x$ (~3σ) — first such claim for a young pulsar — possibly companion spin–orbit coupling / quadrupole.
- Geodetic precession evolves pulse profiles; red noise shows ~2 yr power that may be astrophysical (planet, magnetosphere) or residual modeling.
- Advances prior 2015 solutions with modern arrays and longer baseline.

## Physical intuition

A binary pulsar is a clock on a warped train track. Years of arrival-time residuals encode how strong-field gravity twists the orbit, stretches time, and leaks energy as gravitational waves. Extending the track record from 2015 to 2023 is like lengthening the integration time on a phase-noise measurement: post-Keplerian knobs tighten, a giant crust glitch becomes characterizable, and a whisper of $\dot x$ may reveal that the companion itself is spinning and tugging the orbit.

## Limitations and assumptions

- Masses assume GR; alternate gravity would shift post-Keplerian mapping.
- $\dot x$ significance modest; can mimic noise or profile evolution.
- Red-noise power-law model may miss the ~2 yr spectral feature.
- No proper motion yet biases $\dot P_b$ decomposition (Galactic acceleration, Shklovskii).
- Companion WD vs NS still open without optical/IR ID.
- Analysis-based ingest; verify masses and significance against primary arXiv paper.

## Connections

- Pulsar mass / acceleration work: [[pulsars-satellite-masses]]
- Multi-messenger neutron-star binaries: [[gw170817-jet-hubble]]
- GW strain / timing language: [[second-order-gw-strain-gauge]], [[horizon-direct-wave-gw250114]]
- Concepts: [[pulsar-timing-arrays]] (population context)
- Key terms: post-Keplerian parameters, geodetic precession, pulsar glitch, DD timing model

## Source

- `spacex_export/extracted-analyses/2026-02-17_long-term-timing-of-psr-j1906-0746-binary_19e0bfc4.md`
