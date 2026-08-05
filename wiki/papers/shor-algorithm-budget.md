---
tags: [papers, quantum-computing, cryptography, error-correction]
last_updated: 2026-08-01
status: analysis-ingest
related_papers: [certified-randomness-amplification, quantum-jamming]
source_analysis: "raw/analyses/List2_Combined_Clean.md (Shor's Algorithm on a Budget)"
---

# Shor’s Algorithm on a Budget (Neutral Atoms + qLDPC)

**One-line summary:** Stacking high-rate qLDPC codes, surgery-based logical gates, and neutral-atom reconfigurability cuts cryptographically relevant Shor resource estimates from millions of physical qubits to roughly \(10^4\)–\(10^5\)—with a sharp space–time trade-off the “10,000 qubit” headline can hide.

## Key claims and results

- **Paper:** Caltech / Oratomic resource-estimate work (arXiv ~30 Mar 2026); coauthors include Bluvstein group experimentalists and John Preskill (per analysis).
- Three stacked gains: lifted-product (LP) qLDPC codes (~30% encoding rate vs ~0.1% surface code); Pauli-product measurement / code-surgery logical gates; native all-to-all connectivity by moving atoms in tweezers.
- **ECC-256:** ~10,000 physical qubits → ~117-year runtime; ~26,000 qubits → order ~10 days (assumes ~1 ms stabilizer cycle).
- **RSA-2048:** much harder—century-scale at minimal space, or ~10⁵ qubits for ~months-scale runtime under same assumptions.
- Architecture zones: memory (LP blocks), processor, operation (PPM ancilla), resource (magic states), reservoir (atom reload).

## Physical intuition

Error correction is the real cost of crypto-breaking quantum computers. Surface codes are RAID-1000; high-rate qLDPC is closer to RAID-3—but only if any qubit can check any other. Neutral atoms give that connectivity by physically rearranging the array. Shor still needs both *space* (enough logical qubits) and *time* (enough parallel lanes). Minimum space is not minimum useful wall-clock.

## Limitations and assumptions

- 1 ms cycle is optimistic vs multi-ms demonstrated systems; 10× slower cycles stretch all runtimes 10×.
- Real-time classical decoding of qLDPC syndromes at scale is assumed, not demonstrated end-to-end.
- Atom loss/reload and transport decoherence over months-to-years runs are partially modeled.
- Community critique: abstract “10,000 qubits” mixes space-optimal and time-optimal regimes.
- Building blocks exist (k-atom arrays, small FT demos); integrated 26k-atom crypto machine is multi-year engineering.

## Connections

- Quantum info / foundations cluster: [[certified-randomness-amplification]], [[quantum-jamming]], [[device-independence]].
- Key terms (stubs folded here): **qLDPC codes** = high-rate quantum LDPC error correction (~tens of % encoding vs ~0.1% surface codes); **neutral-atom qubits** = tweezer-array atoms with reconfigurable connectivity that makes nonlocal qLDPC checks practical.

## Source

- Analysis: `raw/analyses/List2_Combined_Clean.md` — *Shor's Algorithm on a Budget.md*
