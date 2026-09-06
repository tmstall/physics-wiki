---
tags: [papers, quantum-foundations, path-integral, single-photons, weak-values]
last_updated: 2026-08-31
status: analysis-ingest
related_papers: [negative-weak-valued-excitation-times, weak-values, atomic-scale-double-slit-si, measurement-problem-threads, w-state-entangled-measurement]
source_analysis: "raw/analyses/2026-08-31_doi-10.1126-sciadv.aeh1011_feynman-path-integral-postulates-single-photons.md"
---

# Feynman Path-Integral Postulates Tested with Single Photons

**One-line summary:** A South China Normal University optics experiment reconstructs complex path amplitudes via weak-value pointer measurements on single photons and directly checks Feynman’s two path-integral postulates (combine amplitudes then square; equal magnitudes, path-dependent phases) (*Sci. Adv.* 2026).

## Key claims and results

- **Paper:** *Science Advances* (2026). DOI [10.1126/sciadv.aeh1011](https://doi.org/10.1126/sciadv.aeh1011).
- Postulate I: observed probabilities match coherent sum of complex path amplitudes, not classical sum of probabilities.
- Postulate II: reconstructed path magnitudes stay flat vs path length / classical action; phases carry the dynamics (~1.4×10⁶ paths on a discretized spacetime grid).
- Technical advance: weak-coupling / pointer method engineered to survive multiplicative reconstruction of many path amplitudes.
- Foundational-but-confirmatory: equivalent to standard QM; does not threaten Schrödinger dynamics.
- Single-lab continuation of earlier Nature Photonics work from the same group.

## Physical intuition

The path integral says the photon “tries every route,” tagging each with a complex weight, then adding before you take a probability. This experiment builds a discrete maze of positions and times, weakly reads the complex tags without hard-collapsing every step, and checks that the two textbook rules for combining those tags actually hold in the lab.

## Limitations and assumptions

- Discretized path space ($N$ sites × $M$ time steps) — tests the postulates in that encoding, not continuum QFT.
- Weak values / postselection carry interpretational baggage; the paper tests the postulates’ empirical content, not a unique ontology of “which path.”
- Equal magnitude ≠ equal contribution to the final camera image (phases still interfere).

## Connections

- Weak values: [[negative-weak-valued-excitation-times]], [[weak-values]]
- Spatial interference / slits: [[atomic-scale-double-slit-si]]
- Synthesis: [[measurement-problem-threads]]
- Photonic QI: [[w-state-entangled-measurement]]

## Source

- `raw/analyses/2026-08-31_doi-10.1126-sciadv.aeh1011_feynman-path-integral-postulates-single-photons.md`
