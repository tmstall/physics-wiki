---
tags: [papers, condensed-matter, graphene, moire, superconductivity]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [brown-zak-nonlinear-transport, bata2s5-field-induced-sc, quantum-metallurgy-cdw, anyon-trions-twisted-mote2]
source_analysis: "spacex_export/extracted-analyses/2026-02-16_supermoir-trilayer-graphene-superconductivity_f38a787f.md"
---

# Supermoiré Lattice Superconductivity in Asymmetric Twisted Trilayer Graphene

**One-line summary:** Mirror-asymmetric twisted trilayer graphene forms a ~31 nm supermoiré that dices flat bands into mini-bands, driving isospin-broken insulators and a cascade of superconducting domes fragmented by half-filling gaps (Zhou et al., *Nature Physics* 2026).

## Key claims and results

- **Paper:** Zekang Zhou et al., *Nature Physics* (2026); arXiv:2509.24670 (analysis framing).
- Unequal twists (e.g. $\theta_{12}\approx1.33^\circ$, $\theta_{23}\approx-1.79^\circ$) break mirror symmetry → interfering moirés → supermoiré period $\lambda_{\rm sm}\approx30.8$ nm (commensurate ratio ~3/4).
- Transport: Brown–Zak oscillations and Hofstadter structure diagnose band folding into mini-flat bands and satellite Dirac points.
- Interaction-driven isospin polarization at quarter-fillings of mini-bands.
- Superconductivity on electron and hole sides, fragmented into multiple domes separated by insulators at half mini-band fillings; BKT $T_c\sim0.5$ K.
- Continuum multi-layer Hamiltonian models interlayer tunneling under the hierarchical lattice.

## Physical intuition

One moiré is an L1 cache that slows electrons into flat bands. A supermoiré is an L2 cache misaligned on top: it further partitions the flat band into mini-drawers. Electrons fight harder in smaller drawers, so Coulomb interactions win more easily — insulators appear at simple fillings, and superconductivity survives only in the leftover pockets. Asymmetric trilayer twists are the knob that turns the second drawer on.

## Limitations and assumptions

- Mini-band spacing variations (±~5%) from strain/twist error.
- Assumes near-commensurability; irrational ratios may quasicrystalize.
- Transport-only; spectroscopic mini-Dirac satellites not yet direct.
- Pairing glue (phonon vs electronic) open.
- Analysis-based ingest; verify angles, densities, and $T_c$ against primary paper.

## Connections

- Brown–Zak / moiré diagnostics: [[brown-zak-nonlinear-transport]]
- Other tunable SC: [[bata2s5-field-induced-sc]], [[nickelate-nodeless-gap-arpes]]
- Moiré fractional neighbors: [[anyon-trions-twisted-mote2]]
- Correlated lattice order: [[quantum-metallurgy-cdw]]
- Key terms: supermoiré, mini-flat band, isospin polarization, BKT transition
- Synthesis: [[condensed-matter-topology-fractionalization]] (fractionalization & topology map)

## Source

- `spacex_export/extracted-analyses/2026-02-16_supermoir-trilayer-graphene-superconductivity_f38a787f.md`
