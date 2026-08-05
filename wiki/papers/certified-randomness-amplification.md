---
tags: [papers, quantum-info, quantum-crypto, superconducting-qubits]
last_updated: 2026-07-31
status: analysis-ingest
related_papers: [quantum-jamming]
source_analysis: "raw/analyses/Certified Perfect Randomness Machine.md"
---

# Certified Randomness Amplification (ETH Zurich)

**One-line summary:** A loophole-free Bell test on two superconducting qubits linked by a 30 m cryogenic hallway turns a public imperfect random seed into private, device-independently certified near-perfect randomness.

## Key claims and results

- **First experimental randomness amplification** that simultaneously hits: loophole-free Bell closure, high enough CHSH violation, and enough trials for a classical extractor to output certified bits (analysis cites arXiv:2412.17931; ETH / Wallraff + Renner groups).
- Hardware: two **transmon** qubits in separate dilution refrigerators (~15 mK), modular cryogenic microwave link **~30 m** (light-travel time ~100 ns closes the locality loophole with fast readout).
- Protocol: Santha–Vazirani (SV) imperfect public bits choose measurement settings → Bell outcomes + seed feed a **two-source extractor** → shorter string close to uniform and private even against an adversary who knows the public seed.
- Device-independence: security rests on the Bell violation, not on trusting the internals of the chips.
- Prior same-group context: high trial counts and CHSH \(S\) values (analysis quotes example \(S \approx 2.236\) in related self-testing work) that finally clear the entropy-extraction threshold.

## Physical intuition

Classical math says you cannot purify a single weak random source into perfect bits. Quantum mechanics offers one escape hatch: if two labs violate a Bell inequality loophole-free, their measurement outcomes cannot have been pre-written by any local program — so the outcomes carry certified fresh entropy. Amplification is “use imperfect public coins to choose bases, then extract private perfect coins from the quantum answers.”

Analogy: a CRC validated against a physical oracle that classical compression theory forbids — the Bell test is the oracle.

## Limitations and assumptions

- **Bit rate is tiny** — certified seed for high-value crypto, not a bulk TLS RNG replacement.
- Security proofs currently require the SV bias parameter not be too large (analysis mentions \(\varepsilon \lesssim 0.013\) scale for relevant proofs).
- Millikelvin, 30 m cryogenic infrastructure — not field-deployable; trapped-ion network follow-ups already exploring less co-located setups.
- Assumes no superdeterminism (standard Bell-test philosophical escape hatch).
- Details should be checked against the primary paper / Nature report.

## Connections

- Concepts: [[bell-tests]], [[device-independence]], [[no-signaling]]
- Contrast: [[quantum-jamming]] attacks [[monogamy-of-entanglement]] assumptions behind device-independent crypto; this paper *uses* device-independent Bell structure as a constructive entropy engine.
- Crypto timeline neighbor (different threat model): [[shor-algorithm-budget]] revises how soon cryptographically relevant factoring might become feasible on neutral-atom + qLDPC machines — certified randomness is one post-quantum resource; Shor is the algorithm that forces classical public-key migration.
- Platform kinship with precision quantum hardware (ion clocks elsewhere in the wiki use different physics but similar control culture).

## Open questions

- Composable end-to-end key services using these certified bits?
- How far can rate and temperature requirements improve?
- Networked / non-cryogenic platforms for the same certification?

- Synthesis: [[measurement-problem-threads]] (foundations: measurement problem threads)

## Source

- Analysis: `raw/analyses/Certified Perfect Randomness Machine.md`
