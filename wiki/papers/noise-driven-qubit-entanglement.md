---
tags: [papers, quantum-information, superconducting-qubits]
last_updated: 2026-08-01
status: analysis-ingest
related_papers: [w-state-entangled-measurement, certified-randomness-amplification, shor-algorithm-budget]
source_analysis: "claude_export/extracted-analyses/2026-07-16_the-qubits-that-entangled-themselves_694c81b2.md"
---

# Noise-Driven Entanglement of Distant Superconducting Qubits

**One-line summary:** Two frequency-detuned qubits half a meter apart entangle in ~300 ns by absorbing two-mode correlated microwave noise from a Josephson parametric converter—no inter-qubit photons, pulses, or post-selection (Kraus–Cirac mechanism).

## Key claims and results

- **Paper:** arXiv:2510.07139 (per analysis).
- Correlated noise from JPC: individually thermal-looking beams with locked fluctuations.
- Dark state of joint system is the unique state invisible to the noise → system falls into entanglement.
- Concurrence ~0.10 (weak); wiring/backscattering limits ceiling ~0.26 unless terminated properly.
- Closes a 2004 theory loop experimentally.

## Physical intuition

Ordinary noise destroys quantum order. **Matched** noise on two lines is different: there is one joint state the noise cannot “see,” and the qubits drain into it like balls into a bowl’s bottom—without ever talking to each other.

## Limitations and assumptions

- Weak concurrence; engineering fixes (termination) needed for usefulness.
- Microwave-specific; scaling to many qubits open.

## Connections

- QI cluster: [[w-state-entangled-measurement]], [[certified-randomness-amplification]], [[device-independence]]
- Complementary “noise/dissipation as resource” theory: [[dissipative-cavity-entanglement]] (engineered collective decay → dark entangled many-body states)
- Concepts: key terms folded — two-mode squeezing as correlated bath; dark-state cooling into entanglement

- Synthesis: [[amo-quantum-state-control]] (AMO state control)

- Synthesis: [[measurement-problem-threads]] (foundations: measurement problem threads)

## Source

- `claude_export/extracted-analyses/2026-07-16_the-qubits-that-entangled-themselves_694c81b2.md`
