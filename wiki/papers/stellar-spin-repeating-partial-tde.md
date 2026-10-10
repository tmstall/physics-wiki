---
tags: [papers, tidal-disruption, black-holes, accretion, hydrodynamics]
last_updated: 2026-08-22
status: analysis-ingest
related_papers: [s301-sgra-spin-sensitive-star, category-79-quasar-wind, radio-changing-look-agn, glimpse-17775-cocoon, magnetar-slsn-2017egm-fermi]
source_analysis: "raw/analyses/2026-08-22_doi-10.3847-1538-4357-ae8f31_stellar-spin-repeating-partial-tidal-disruption.md"
---

# Stellar Spin in Repeating Partial Tidal Disruption Events

**One-line summary:** SPH simulations show that stars arriving already spun near the pericenter orbital frequency (Hills-capture natural) keep spin roughly fixed across passes, letting post-stripping densification drive multi-flare dimming — fixing why zero-initial-spin models failed past ~two encounters (*ApJ* **1007**:181, 2026).

## Key claims and results

- **Paper:** Bandopadhyay, Amend, Coughlin, Nixon, Pasham & Wevers, *ApJ* **1007**:181 (2026). DOI 10.3847/1538-4357/ae8f31.
- Problem: rpTDE light curves often dim over many repeats; prior hydro (incl. same group) either destroyed the star or spun it up from rest until later flares brightened.
- Mechanism: initialize $\lambda=\Omega/\Omega_\star\sim0.7$–0.8 prograde; when $\Omega\sim\Omega_p$, torque per pass is inefficient → spin plateaus → density-increase-on-mass-loss (companion 2025 result for $M_\star\gtrsim1\,M_\odot$) drives monotonic fallback decline over ≥4 passages.
- Four PHANTOM/MESA cases (1–3 $M_\odot$, ZAMS/MAMS/TAMS, selected $\beta$) confirm the pattern; nonspinning controls do not.
- Framing: strong **indirect** evidence for Hills binary-disruption capture supplying pre-spin — consistent with, not unique proof of, that channel.
- Explicit break: AT2018fyk’s ~10× drop needs extra relativistic/three-body physics (higher $M_\bullet$).

## Physical intuition

A star spun from rest is a flywheel getting kicked up each periapse — more fragile, brighter later flares. A Hills-captured star arrives already near the kick’s natural rate — the flywheel barely changes speed, so the “leftover core gets denser” trend can finally show as steady dimming.

## Limitations and assumptions

- Single-group SPH lineage; density-increase foundation from companion paper.
- Retrograde / misaligned spins not simulated.
- Sparse grid of $\lambda$/$\beta$/evolutionary stages — demonstration, not full survey.
- Spin inferred by light-curve match, not measured.

## Connections

- GC / extreme orbits: [[s301-sgra-spin-sensitive-star]]
- AGN variability / feeding: [[category-79-quasar-wind]], [[radio-changing-look-agn]], [[glimpse-17775-cocoon]]
- Transient engines (different): [[magnetar-slsn-2017egm-fermi]], [[grb-220706a-month-long-engine]] (nuclear position raised a TDE reading; X-rays look like a burst)
- Synthesis: [[smbh-stellar-encounters]] (primary — Hills / rpTDE)
- Synthesis: [[black-hole-feedback-and-changing-look-agn]], [[high-energy-astrophysics-multimessenger]]

## Open questions

- Independent hydro code reproduction of the $\Omega\sim\Omega_p$ dimming window?
- Retrograde Hills products — do they anti-dim?
- Can AT2018fyk-class drops be recovered with Kerr + three-body modules?

## Source

- `raw/analyses/2026-08-22_doi-10.3847-1538-4357-ae8f31_stellar-spin-repeating-partial-tidal-disruption.md`
