---
tags: [papers, quantum-foundations, quantum-crypto, causality]
last_updated: 2026-07-31
status: analysis-ingest
related_papers: [certified-randomness-amplification]
source_analysis: "raw/analyses/Quantum Jamming.md"
---

# Quantum Jamming

**One-line summary:** A hypothetical third-party operation can silently rewrite nonlocal correlations without changing local statistics or sending superluminal signals — and whether that is physically allowed is an open fight over causality, monogamy, and DIQKD security.

## Key claims and results

- **Jamming** (Grunhaus, Popescu & Rohrlich, 1996): a jammer influences the *type* of correlation between two distant parties while leaving each party’s local outcome statistics untouched and without enabling faster-than-light messaging.
- If jamming is possible in any post-quantum theory, [[monogamy-of-entanglement]] fails in certain multiparty spacetime geometries — a direct threat to device-independent QKD security proofs that treat monogamy as a tripwire.
- Modern debate (2019–2025):
  - Horodecki & Ramanathan: “relativistically causal” multiparty configs leave room for jamming.
  - Vilasini & Colbeck (2022): jamming requires superluminal *causation* even if no-signaling holds.
  - Weilenmann (2025): if a jammer can be switched on/off, that control is itself superluminal signaling.
  - Eckstein, Miller, Horodeckis & Ramanathan (arXiv:2512.23702): reject the free “switch” assumption; introduce operational no-signaling (ONS); claim jamming can survive in some geometries — including near **black hole horizons**.

## Physical intuition

Alice and Charlie share a correlation budget. Bob sits in a spacetime sweet spot and rewrites whether their outcomes agree or disagree — but neither sees anything weird until they later compare notes. No local alarm, no FTL telegram. Device-independent crypto assumes that kind of silent rewrite is impossible because monogamy forbids three-way maximal correlation. Jamming asks: is that a law of *nature*, or only a theorem of *quantum mechanics*?

Engineering analogy: a network switch that reroutes packets between two servers without changing either server’s CPU graph — endpoints only notice when they reconcile logs.

## Limitations and assumptions

- The dispute is largely **definitional**: what counts as “operating” a jammer vs. a fixed nonlocal correlation structure.
- Black-hole compatibility is “not forbidden by ONS,” not “we have a Hamiltonian that does it.”
- No experimental protocol currently tests jamming; it is foundational theory.
- Analysis synthesizes a multi-paper arc from popular + research sources; verify citations against primaries.

## Connections

  - Concepts: [[quantum-jamming]], [[monogamy-of-entanglement]], [[no-signaling]], [[device-independence]], [[bell-tests]]
- Crypto / hardware cousin: [[certified-randomness-amplification]] also leans on loophole-free Bell structure, but for entropy extraction rather than key monogamy.
- Opens a quantum-gravity adjacent question: horizons as natural causal shields — compare causal-structure work in [[evaporating-charged-black-holes]] and [[black-hole-interiors]].

## Open questions

- Is there a deeper principle (beyond ordinary no-signaling) that forbids jamming in all physical theories?
- Can ONS + horizon scenarios be made constructive (explicit channel / dynamics)?
- How should DIQKD security proofs state post-quantum assumptions explicitly?

- Synthesis: [[measurement-problem-threads]] (foundations: measurement problem threads)

## Source

- Analysis: `raw/analyses/Quantum Jamming.md` (von Hippel / Quanta-style synthesis of the 1996–2025 literature arc).
