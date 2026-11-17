---
tags: [papers, yang-mills, mass-gap, constructive-qft, lean, openai]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [lean-proof-assistant, gluon-production-cgc-bcfw, color-superconductivity-qcd]
source_analysis: "raw/analyses/2026-10-30_primer_yang-mills-existence-mass-gap.md"
---

# Yang–Mills Existence, without a Mass Gap

**One-line summary:** A November 2026 review says OpenAI’s Lean code constructs a relativistic four-dimensional Yang–Mills theory for every compact simple gauge group, as one phase of a subsequential large-volume limit; uniqueness is open, and the mass gap is not claimed. Primer plus deep dive plus the Yang–Mills group assessment.

## Key claims and results

- **Sources, in order.** Primer `2026-10-30_primer_yang-mills-existence-mass-gap.md` (what the Clay problem asks, Balaban’s lattice program, the 26 Oct announcement). Deep dive `2026-11-07_deep-dive_yang-mills-existence-mass-gap.md` (seven threads; status as of 7 Nov: proof still unreleased). Assessment `2026-11-12_ymgroup-assessment-1_openai-yang-mills-validation.md` of Douglas, Jaffe, Nissim, and Rajasekaran for the Yang–Mills group (Gross, chair), 35 pages, 10 Nov 2026, on the Lean submission of 28 Oct. The assessment is the status. The earlier files are the background and the pre-registered tests.
- **What “existence” means.** A grid theory is well defined. Removing the grid spacing and the box size has to leave a theory that meets the Osterwalder–Schrader / Wightman contract: a relativistic quantum theory, not a free field. The mass gap (a nonzero lower bound on the energy of particle-like excitations) and confinement are separate. Lattice numerics support both. Neither is this claim. The Clay prize needs existence **and** the gap.
- **What the assessment certifies.** The code rebuilds, uses only Lean’s standard axioms, and proves the hard lattice estimates rather than assuming them. The construction takes a continuum limit at fixed box size, grows the box along a subsequence by compactness, splits a possibly mixed state into pure phases, and reconstructs a real-time theory from one selected phase. Rotation invariance is restored. The theory is fingerprinted as Yang–Mills by a stress tensor, a trace anomaly with the perturbative coefficient, a one-loop running coupling, and an exclusion of simple free fields. The group says OpenAI’s public target theorem was weaker than the result and checked a stronger target it wrote itself.
- **What it does not certify.** Uniqueness of the infinite-volume limit. A single vacuum. The mass gap. An area law. Continuum confinement. Perturbative agreement past leading order. Universality under other lattice actions. QCD and the grand-unified claims stay in natural language; only pure Yang–Mills was machine-checked. The Jaffe–Witten text treats a compactness subsequence as not enough by itself. The group adopts a weaker existence criterion and invites scrutiny. About 60% of project declarations are unused by the main theorems. The informal manuscript was not what the group read.

## Physical intuition

Physicists compute with Yang–Mills every day. Existence is the proof that the object being approximated survives when the lattice props are removed and is still interacting. Balaban’s program controlled the short-distance problem in a finite box and stopped before a full infinite-volume construction. The new work claims to finish that existence half by a phase-split workaround: do not prove the vacuum is unique; decompose the limit and certify one pure piece. That is a real mathematical object. It is not yet “the” Yang–Mills theory, and it does not explain why the strong force is short-ranged.

Lean shrinks “is every line valid?” to “do these definitions mean the Clay statement, and what is on the axiom list?” [[lean-proof-assistant]]. A clean build of the wrong definition still compiles.

## Limitations and assumptions

- The assessment authors say they do not fully understand the proof and used OpenAI’s model to read the code. Adapters reuse analytic estimates from the submission. Reference formalizations were written on the reviewing side.
- No public human-readable proof. Independent kernel rebuilds and outside constructive-field-theory writeups are the confirmation that is still missing.
- The analysis of the assessment did not read the Lean source.

## Connections

- What a clean Lean build does and does not prove: [[lean-proof-assistant]]
- Everyday Yang–Mills calculations, not this existence question: [[gluon-production-cgc-bcfw]], [[color-superconductivity-qcd]]
- No new concept page. The gap, the axioms, and Balaban’s program stay on this page until a second paper changes a conclusion.

## Open questions

- Does a second kernel, read by people outside the committee, accept the same statement?
- Can uniqueness be proved, or is the subsequential limit the best the method can say?

## Sources

- `raw/analyses/2026-10-30_primer_yang-mills-existence-mass-gap.md`
- `raw/analyses/2026-11-07_deep-dive_yang-mills-existence-mass-gap.md`
- `raw/analyses/2026-11-12_ymgroup-assessment-1_openai-yang-mills-validation.md`
