---
tags: [papers, qgp, heavy-quarks, transport, heavy-ion]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [cms-jet-diffusion-wake, star-oxygen-jet-quenching, equilibrated-fraction-oo-qcd]
source_analysis: "raw/analyses/2026-11-07_doi-10.1103-7fd5-1kq5_heavy-quark-transport-non-gaussian-qgp.md"
---

# Non-Gaussian Kicks on a Heavy Quark

**One-line summary:** The momentum a fast, infinitely heavy quark exchanges with a weakly coupled plasma has a Gaussian core plus lopsided exponential tails; the tails are what let the quark reach the plasma temperature, and the same shape appears in a strong-coupling toy. Du Plessis and Scheihing-Hitschfeld, *Phys. Rev. Lett.* (2026).

## Key claims and results

- **Paper:** Jean F. Du Plessis and Bruno Scheihing-Hitschfeld. DOI [10.1103/7fd5-1kq5](https://doi.org/10.1103/7fd5-1kq5). arXiv:2604.21895v1. Journal version not compared. Full distribution of longitudinal kicks at first nontrivial order in the coupling, not only drag and diffusion.
- The log-enhanced piece is Gaussian and obeys the Einstein relation. Everything non-Gaussian comes from thermal-scale exchanges. At high speed the Gaussian piece alone breaks detailed balance: a large slowing kick must be more likely than an equal speeding kick by a Boltzmann factor. The tails supply that lean.
- At rest the tail decays as one over twice the temperature. At high speed the slowing tail and the speeding tail differ by speed over temperature. Weak-coupling QCD, weak-coupling supersymmetric Yang–Mills, and an earlier strong-coupling supersymmetric calculation share the lopsided shape. The authors add a third transport number, a volatility exponent, beside drag and diffusion.
- The QCD calculation is at a coupling about 400 times weaker than a realistic plasma. The quark mass is infinite. Charm is only about four times a typical plasma momentum. No collider observable is recomputed. A press line that this shows the plasma is a liquid rather than a gas is not the paper’s result: the tails show up on both sides of that divide.

## Physical intuition

Brownian motion with a bell curve has two knobs, drag and kick size, locked so the particle settles at the bath temperature. For a fast heavy quark those two knobs, computed from QCD, do not lock. Equilibrium still has to happen, so the kick distribution cannot be a bell. Rare shoves lean toward slowing the quark down. Most of the time the quark still jitters. The tails are the part a Gaussian fit misses, and they are required.

## Limitations and assumptions

- Perturbative heavy-quark diffusion converges poorly at realistic coupling. The strong-coupling comparison is a conformal toy.
- Ultra-relativistic and strong-coupling decay rates are summarized from papers marked “to appear.”
- No estimate of how much a Gaussian extraction of the diffusion coefficient shifts.
- Tails are read off a series extended to its radius of convergence, where the series is slowest.

## Connections

- Where lost jet momentum goes, a different medium response: [[cms-jet-diffusion-wake]], [[star-oxygen-jet-quenching]]
- Synthesis: [[nuclear-dense-matter-precision]]

## Open questions

- By how much do extracted heavy-flavor diffusion coefficients move when the tails are put into a transport model?

## Source

- `raw/analyses/2026-11-07_doi-10.1103-7fd5-1kq5_heavy-quark-transport-non-gaussian-qgp.md`
