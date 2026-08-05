---
tags: [papers, general-relativity, topology, plasma-analogy]
last_updated: 2026-08-01
status: analysis-ingest
related_papers: [evaporating-charged-black-holes, topological-cosmological-constant]
source_analysis: "raw/analyses/frozen gravity.md; List2_Combined_Clean.md (frozen gravity.md)"
---


# Frozen-In Gravitational Fields

**One-line summary:** Einstein’s equations force curvature field lines and the two-surfaces they thread to freeze topologically — like magnetic flux in ideal MHD — so gravitational flux and helicity stay conserved through full nonlinear spacetime evolution.

## Key claims and results

- **Paper:** Asenjo, Winkler & Comisso, *Physical Review Letters* (2026) — “Frozen-In Gravitational Fields” (title as framed in the analysis).
- Rewrite GR curvature evolution in an electrodynamic / 3+1 language where the Weyl tensor plays a gravito-magnetic role.
- Ideal-gravity **Ohm condition** (gravitational analog of \(\mathbf{E}+\mathbf{v}\times\mathbf{B}=0\)) implies conservation of:
  - gravitational **flux** through comoving two-surfaces,
  - gravitational **helicity** (linking of curvature field lines),
  - connectivity of field-line bundles.
- Invariants are claimed to survive the **full nonlinear** Einstein dynamics — vacuum spacetime itself acts as the perfect conductor; no plasma required.
- Illustrative regimes: black-hole interiors, gravitational-wave propagation, large-scale evolution (brief examples in analysis).

## Physical intuition

In ideal MHD, magnetic field lines are sewn into the plasma fabric: stretch the cloth, do not cut or re-tie the threads. Here the fabric *is* spacetime. Curvature structures ride along with the geometry; ordinary nonlinear GR evolution can warp and bend them but cannot freely reconnect their topology unless some effective “gravitational resistivity” appears.

Cache-coherency analogy: once ownership flags lock a line, the protocol forbids silent corruption across cores — topology is hardware-enforced.

## Limitations and assumptions

- Ideal (zero-resistivity) limit; real astrophysical or quantum regimes may allow reconnection.
- Classical GR only — near singularities, evaporation, or strong matter coupling the condition may fail.
- Turning invariants into practical numerical-relativity tools still needs algorithmic work.
- Details reconstructed from analysis / news framing; verify against the PRL text.

## Connections

- Concepts: [[frozen-in-gravity]]
- GR neighbor: [[evaporating-charged-black-holes]] (different angle: causal structure of evaporating interiors vs. topological constraints on evolution).
- Topological protection of Λ (different topology story — θ-vacua / CSK, not flux freeze): [[topological-cosmological-constant]], [[gravitational-theta-vacua]]
- Name-adjacent early-universe cousin (different physics — freeze-in DM, not curvature topology): [[gw-induced-fermion-freeze-in]]
- Method heritage: plasma MHD frozen-in theorem ported to vacuum gravity.
- Synthesis: [[black-hole-evaporation-energy-conditions]]
- **Ingest note (List2 final batch):** List2 re-analyzes the same frozen-gravity result already filed from the standalone analysis—no second paper page.

## Open questions

- When and how does effective gravitational resistivity appear?
- Can topology-preserving schemes improve binary black-hole or cosmology simulations?
- Quantum-gravity corrections near singularities?

## Source

- Analysis: `raw/analyses/frozen gravity.md` (base64 images stripped before ingest).
