---
tags: [papers, spin-ice, colloids, frustration, soft-matter]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [magnetic-heliknoton-electric-write, nonabelian-photonic-braiding]
source_analysis: "raw/analyses/2026-11-01_doi-10.1038-s41467-026-77905-2_particle-anti-spin-ice-charge-frustration.md"
---

# Particle Anti-Spin Ice

**One-line summary:** Attractive colloidal “spins” reverse the ice rule: square and honeycomb lattices crystallize into staggered charge in simulation, and a pentaheptite lattice of pentagons and heptagons keeps about one junction in four only partly charged, in both simulation and experiment. Baillou, Terkel, Nisoli, and Tierno, *Nature Communications* (2026).

## Key claims and results

- **Paper:** *Nature Communications* **17**, 11152 (2026). DOI [10.1038/s41467-026-77905-2](https://doi.org/10.1038/s41467-026-77905-2). One magnetic bead per elongated trap. A spinning in-plane field averages the dipole interaction into an isotropic attraction. Supplementary movies and the square-ice frequency study were not in the upload.
- Ordinary particle ice is repulsive: each vertex wants to be neutral, and the ice rule is the compromise. Attraction makes each vertex want every bead or none (topological charge $\pm 1$).
- Square and honeycomb can be two-colored, so simulations reach a perfect staggered charge crystal. Honeycomb, which is frustrated when the beads repel, orders when they attract. Those two lattices are simulation only.
- The pentaheptite (pentagons and heptagons) cannot two-color. Odd loops force a floor: at least two of every eight vertices stay partly charged. Experiment and simulation both show that plateau, neighbor correlation saturating near −0.6 rather than −1, and leftover loop circulation near 1/5 on pentagons and 1/7 on heptagons. The leftover states are mapped to a dimer model. The residual entropy is not counted.
- The lab spin rate is about fifty times slower than the simulation. A field rescaling of 2.4, fit for agreement, sets where the crossover sits. The plateau fractions are counting, so they do not depend on that fit.

## Physical intuition

Frustration is usually “every junction wants to be neutral, and the lattice will not allow it.” Here every junction wants to be maximally charged, which is a two-coloring, and odd loops forbid two-colorings. The failure is to maximize, not to minimize. The spinning field is the dial that flips the sign without building a new sample.

## Limitations and assumptions

- Bipartite crystals are not yet a lab result. Grain boundaries in the snapshots are argued to be kinetic.
- Trap-length constraints split vertex energies by about a percent. In a frustrated manifold that can select a unique ground state.
- Odd loops are necessary for this frustration and not sufficient: some lattices with odd loops still order.
- Annealing rates in the text disagree by up to tenfold.

## Connections

- Other writable classical spin textures, different platform: [[magnetic-heliknoton-electric-write]]
- Soft-matter and photonic emulators: [[nonabelian-photonic-braiding]]
- Synthesis: [[condensed-matter-topology-fractionalization]]

## Open questions

- Does an experimental square or honeycomb anti-ice actually crystallize, and how large is the pentaheptite degeneracy?

## Source

- `raw/analyses/2026-11-01_doi-10.1038-s41467-026-77905-2_particle-anti-spin-ice-charge-frustration.md`
