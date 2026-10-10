---
tags: [papers, machine-learning, statistical-mechanics, relu, theory]
last_updated: 2026-10-09
status: analysis-ingest
related_papers: [model-growth-looping-scaling-exponents, quantum-jamming, particle-view-nn-wavefunction]
source_analysis: "raw/analyses/2026-10-09_arxiv-2609.22965_deep-relu-exact-statistical-mechanics-realization.md"
---

# Exact Deep ReLU Computation as a Zero-Temperature Ensemble

**One-line summary:** A single-author preprint proves that a Boltzmann ensemble over all on/off masks of a deep ReLU net, scored with a layer-priority traffic rule, freezes at $T=0$ onto the network’s actual activation pattern — a correct identity whose “temperature,” “phase transition,” and “quantum/fermion” dress are mostly relabeling. Li, arXiv:2609.22965v1.

## Key claims and results

- **Paper:** Junxu Li (Northeastern University, Shenyang), arXiv:2609.22965v1 (19 Sep 2026), 7-page letter + 11-page supplement. No journal, no code, no device.
- Construction: fold biases into matrices, split +/− weights, shrink so each part is a valid probability map. Configurations are binary masks (which units are open). Score = signed traffic through open sites, weighted by downstream throughput, with a factor of $2$ extra for every layer closer to the input. Boltzmann $q(\alpha) \propto \exp(\beta \sum_t 2^{T-t} \pi^{(t)}(\alpha))$.
- Theorem 1: as $\beta\to\infty$ the ensemble condenses on a unique best mask, that mask *is* the forward-pass ReLU pattern at every layer, and averaged signed traffic equals (rescaled) hidden states, output, and squared-error loss. Analyst brute-force enumeration on random nets reproduces this to machine precision.
- Why it works: Lemma 1 (induction) makes earlier-layer terms dominate later ones, so the joint argmax factorizes greedily — “open this site if incoming signed traffic is positive” — which is ReLU. Equal layer weights break the correspondence on ~1/4 of inputs in a deeper test net.
- “First-order phase transitions”: slope of the score vs input jumps at linear-region boundaries when cold. True by construction (max of straight lines kinks where the winner changes). Finite system, zero $T$: a **level crossing**, not a thermodynamic transition.
- Costumes: cascaded quantum circuit blocks with post-selection, and spin-carrying particles hopping a layered lattice. Every block is fully measured; only squared amplitudes enter; particles never interact. Effectively a classical sign-bit random walk. The Boltzmann-over-masks layer is *not* produced by the circuit.

## Physical intuition

A ReLU net is a compiled program with branches “is this partial sum positive?” Once the branch trace (mask) is known, the rest is straight-line linear algebra. The paper treats the mask as a free configuration, writes a score whose unique maximum *is* the trace a forward pass would have taken, and cools a softmax until only that mask survives.

The one real trick is lexicographic priority: earlier layers are the high-order sort bits. A one in a higher bit beats any pattern of lower bits, so the sort settles layer 1, then 2, and so on. That is the device that lifts the textbook two-state switch (ReLU as $T=0$ of a binary unit — Nair & Hinton; softplus as free energy) to arbitrary depth without approximation.

Warm, averaging all masks equally, is a purely linear model. Cold, you get the piecewise-linear facets. Near a crease two masks nearly tie, so even a cold ensemble blurs — the dips in the paper’s Fig. 2d.

## Limitations and assumptions

- ReLU does not “emerge from generic physics.” The score is built from the network’s own weights, the specific input, a downstream-throughput factor, and a hand-chosen doubling. Swap the doubling and the identity breaks. “Without prescribing an activation” means “argmax of an objective designed to have ReLU as argmax.”
- Temperature is a Lagrange multiplier with no physical scale. Doubling the arbitrary shrink constants shrinks the best-vs-second score gap ~8× and raises the needed $\beta$ by the same factor. Near boundaries the gap → 0, so no finite $T$ condenses everywhere.
- Supplement’s quantum embedding implements the *entry-wise squared* weight matrix (amplitudes vs probabilities). Hidden states would be wrong. Fix: encode square roots with column sums ≤ 1. Factors of 2 and 4 in rescaling disagree between supplement and main text. Theorem 1 (stat-mech) is untouched.
- No quantum resource, no fermionic exclusion, no training method, no efficiency claim. Configuration count doubles per unit; circuit readout signal shrinks with the product of shrink factors.
- Does not cite tropical geometry (ReLU nets as max-plus / $T=0$ log-partition) or gated-path decompositions that already write the output as a sum over open paths.

## Connections

- Empirical architecture/scaling (different question): [[model-growth-looping-scaling-exponents]]
- Neural many-body wavefunctions (NN as physics tool, not NN-as-stat-mech): [[particle-view-nn-wavefunction]]
- Foundations neighbor (jamming / constraint language, not this construction): [[quantum-jamming]]
- Islands ML/computation shelf with the scaling paper; no synthesis hub yet

## Open questions

- Independent reading of the quantum-circuit supplement (the place an error was found)?
- Is the layer-priority score interesting as an analysis tool (counting regions, training dynamics), or only as an identity?
- A physical sampler that actually draws masks with those Boltzmann weights? The paper does not provide one.

## Source

- `raw/analyses/2026-10-09_arxiv-2609.22965_deep-relu-exact-statistical-mechanics-realization.md`
