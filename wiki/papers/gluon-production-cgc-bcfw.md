---
tags: [papers, cgc, gluons, bcfw, heavy-ion, qcd]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [alice-jpsi-gluon-saturation, cms-jet-diffusion-wake, yang-mills-existence-mass-gap, parton-jets]
source_analysis: "raw/analyses/2026-11-08_doi-10.1007-jhep08-2026-106_gluon-production-cgc-bcfw.md"
---

# Gluon Production in the CGC without a Bulk Gauge

**One-line summary:** Gelis re-derives the known dilute–dense gluon-production amplitude with off-shell BCFW recursion; source-color precession becomes one class of poles, and the method is shown only at an order that was already tractable. *JHEP* 08 (2026) 106.

## Key claims and results

- **Paper:** François Gelis. *JHEP* **08** (2026) 106. DOI [10.1007/JHEP08(2026)106](https://doi.org/10.1007/JHEP08(2026)106). arXiv:2605.02299. Open access.
- Leading-order gluon production in the color-glass condensate comes from classical Yang–Mills with a shockwave color source. The field depends on the gauge. The gluon count does not. Earlier derivations spend their effort on pieces that cancel.
- This paper builds the same tree amplitude from smaller on-shell amplitudes. Off-shell source momenta are a light-like direction plus two transverse coordinates that do not depend on the reference spinor. A shift along the nucleus direction hides nucleus-side charge precession. Proton-side precession survives as eikonal-propagator poles. The result is the Lipatov vertex of the nucleus’s total transverse momentum, times a Wilson line, matching three older gauges. Only the initial-time gauge is fixed.
- One proton kick, any number of nucleus kicks, infinitely thin sources. The author says the final results are not new. Next order in the proton’s charge, and finite nucleus thickness, are named and not computed. No timing benchmark. The analysis confirmed the algebra that turns the recursion output into the Wilson line and the color-basis reduction.

## Physical intuition

A dense nucleus at collider energy is a flattened sheet of color charge. Solving for the gluon field is like computing in a coordinate system you chose, then throwing away everything that depended on the choice. BCFW never builds those pieces. It only adds the ways an amplitude can split into two smaller physical amplitudes. The CGC’s extra graphs, which keep the color charge’s rotation gauge invariant, collapse into one residue. That is bookkeeping, not a new cross section.

## Limitations and assumptions

- Reproduces a known answer in the easy regime. Whether it wins at the next order, where light-cone gauge is no longer simple, is open.
- Falloff under a large deformation is proved for one shift class and argued for the production shifts.
- The last longitudinal integral and the mixed-direction color relations are asserted by analogy with the scattering case.
- Gauge invariance is assembled from Ward identities and invariant sub-amplitudes, not derived as an independent theorem.

## Connections

- Saturation evidence in data, not this amplitude: [[alice-jpsi-gluon-saturation]]
- Where the produced gluon’s momentum ends up in the medium: [[cms-jet-diffusion-wake]], [[parton-jets]]
- Existence of the theory being calculated, a different question: [[yang-mills-existence-mass-gap]]
- Synthesis: [[nuclear-dense-matter-precision]]

## Open questions

- Does the recursion produce a two-kick dilute–dense amplitude that matches a classical lattice Yang–Mills solve?

## Source

- `raw/analyses/2026-11-08_doi-10.1007-jhep08-2026-106_gluon-production-cgc-bcfw.md`
