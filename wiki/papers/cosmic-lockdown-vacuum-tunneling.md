---
tags: [papers, cosmology, decoherence, vacuum, tunneling]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [cosmology-expansion-history-and-structure, measurement-problem-threads, topological-cosmological-constant]
source_analysis: "raw/analyses/2026-09-24_arxiv-2512.14204_cosmic-lockdown-decoherence-vacuum-tunneling.md"
---

# Cosmic Lockdown — Decoherence and Vacuum Tunneling

**One-line summary:** arXiv:2512.14204. Toy cosmology: expansion rate (heavy vs light field) picks the vacuum; environment/decoherence does not pick it but exponentially throttles later tunneling (finite waiting time, not a hard ban). Not a real Higgs calculation.

## Key claims and results

- Christie, Joo, Kaplanek, Vennin & Wands, arXiv:2512.14204v2. Framed as accepted at JCAP; no DOI was located. Explicitly not a Higgs calculation.
- Toy: one scalar in a lopsided double well, de Sitter expansion, coupled to spectator fields. Master equations are derived from that coupling (a memoryless bath of many heavy fields, and a memory-keeping bath of one light field) and solved numerically.
- Which vacuum wins tracks the adiabaticity ratio $\tilde\mu=\mu/H$. Heavy fields follow the deeper well. Light fields get stretched by the expansion and keep substantial false-vacuum probability. Changing the coupling barely moves that probability; it does speed the loss of purity.
- After the field has landed, the same bath destroys the inter-well coherence tunneling needs. The decoherence rate grows as $e^{6N}$ with the number of e-folds. The mean waiting time to leave the false vacuum is exponentially long and finite — rare hops over the barrier, not a prohibition. The authors read this as a continuous quantum Zeno effect.
- The single light spectator can drive periodic vacuum transitions. The memoryless bath does not.
- No observational target. The checkable object is the model’s own first-passage-time formula.

## Physical intuition

Textbook vacuum decay treats the field as a closed system. Here the environment is an append-only log. It does not choose the valley — that is whether the field can keep up with the expansion. Once a branch writes to the log, interference, which tunneling needs, is gone. Expansion turns the write rate up, not down. Lockdown is a very long timer, not a locked door.

## Limitations and assumptions

- Hand-built potential and a spectral density chosen so the bath forgets instantly. Coarse-graining is at fixed comoving volume, not fixed physical volume. The authors flag both.
- Direct numerics only cover a short stretch of e-folds. The late-time lockdown claim uses an analytic strong-localization approximation.
- “Decoherence does not pick the vacuum” is shown for one coupling channel and does not automatically carry over to another the paper itself compares.
- Analysis basis is a paraphrased arXiv extraction, not a character-checked PDF. The non-Markovian details are the softest part.
- Press language about protecting our Higgs vacuum overshoots the paper. A realistic electroweak model is future work.

## Connections

- Synthesis: [[cosmology-expansion-history-and-structure]], [[measurement-problem-threads]]
- Vacuum / cosmological-constant neighbor: [[topological-cosmological-constant]]

## Source

- `raw/analyses/2026-09-24_arxiv-2512.14204_cosmic-lockdown-decoherence-vacuum-tunneling.md`
