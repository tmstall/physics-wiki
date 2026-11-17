---
tags: [papers, lean, formal-verification, proof-assistants]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [yang-mills-existence-mass-gap, eml-single-operator]
source_analysis: "raw/analyses/2026-11-07_primer_lean-proof-assistant.md"
---

# Lean, and What a Clean Build Does Not Prove

**One-line summary:** Lean checks that every inference step follows from the stated definitions and axioms; a compiling proof can still define the wrong object, assume a false hypothesis, or hide a `sorry`. Primer, written for the Yang–Mills release.

## Key claims and results

- **Source:** primer `2026-11-07_primer_lean-proof-assistant.md`, not a journal paper. Status inside the file is 7 Nov 2026, before the Yang–Mills group’s 10 Nov assessment. The current Yang–Mills verdict is on [[yang-mills-existence-mass-gap]].
- Lean is a proof assistant. The kernel accepts a theorem only if each step is valid. Language models can iterate against that kernel the way a programmer iterates against a compiler. “Verified in Lean” means the steps follow. It does not mean the statement is the one physicists meant.
- Three clean-build traps, from the primer:
  1. A wrong definition. `MyPrime n := n > 1` lets a proof that 4 is prime compile.
  2. A false hypothesis. From `1 = 2`, anything follows, and the file still builds.
  3. A hidden gap. `sorry` compiles with a warning. `#print axioms` shows `sorryAx` and any declared axioms.
- For a long formalization, the kernel answers “are the steps valid?” and the axiom list answers “what was assumed?”. Humans still have to check that the definitions match the mathematical statement, and whether that statement is the Clay problem. Those few pages are where a new quantum-field-theory formalization can still be wrong.

## Physical intuition

A compiler will happily build a program that implements the wrong specification. Lean is that compiler for proofs. The reduction is real: a thousand pages of steps collapse to a short list of definitions plus an axiom audit. The list is the whole remaining argument.

## Limitations and assumptions

- Teaching primer. No new theorem.
- Written before the assessment. Do not use its “proof still private” line as the wiki’s status.

## Connections

- The release this primer was written to read: [[yang-mills-existence-mass-gap]]
- A different “one operator generates a calculus” claim, not a proof assistant: [[eml-single-operator]]
- Islands shelf (formal mathematics). No concept stub.

## Source

- `raw/analyses/2026-11-07_primer_lean-proof-assistant.md`
