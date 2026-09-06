---
tags: [concepts, quantum-crypto, quantum-info]
last_updated: 2026-08-16
status: draft
related_papers: [certified-randomness-amplification, quantum-jamming, dissipative-cavity-entanglement, noise-driven-qubit-entanglement, shor-algorithm-budget, w-state-entangled-measurement]
---

# Device-Independence

**One-line summary:** Security or certification from observed input–output statistics (e.g. Bell violation) without trusting the internal implementation of the quantum devices.

## Physical picture

Black-box chips: you do not need a correct Hamiltonian model of the qubits. If they violate a Bell inequality under loophole-free conditions, certain statements about entropy or key secrecy follow from physics assumptions (no-signaling, free choice), not from the manufacturer’s datasheet.

Used constructively in [[certified-randomness-amplification]]; challenged at the foundational level by [[quantum-jamming]] scenarios that attack monogamy assumptions behind some DI protocols.

## Related pages

- Reverse-link: [[dissipative-cavity-entanglement]]
- Reverse-link: [[noise-driven-qubit-entanglement]]
- Reverse-link: [[shor-algorithm-budget]]
- Reverse-link: [[w-state-entangled-measurement]]

- Synthesis: [[measurement-problem-threads]] (foundations: measurement problem threads)


- [[bell-tests]]
- Randomness Amplification
- [[monogamy-of-entanglement]]
