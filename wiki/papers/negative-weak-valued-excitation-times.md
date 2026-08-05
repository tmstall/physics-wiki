---
tags: [papers, quantum-optics, weak-values, foundations]
last_updated: 2026-07-31
status: analysis-ingest
related_papers: [time-goes-quantum]
source_analysis: "raw/analyses/Experimental Observation of Negative Weak Values for the Time.md"
---

# Negative Weak-Valued Atomic Excitation Times

**One-line summary:** For photons transmitted through cold atoms, the weak-valued time atoms spend excited equals the optical group delay — including **negative** values near resonance — first observed experimentally with a cross-Kerr probe.

## Key claims and results

- **Paper:** Angulo, Thompson, Nixon, Jiao, Wiseman & Steinberg, *Phys. Rev. Lett.* **136**, 153601 (13 Apr 2026); arXiv:2409.03680.
- System: cold ⁸⁷Rb MOT; near-resonant signal pulse; far-detuned probe reads excitation via cross-Kerr phase.
- Post-select on **transmitted** signal photons; integrated probe phase → weak value of atomic excitation dwell time \(\tau_T\).
- Measured \(\tau_T / \tau_0\) from **−0.82 ± 0.31** (narrowband, near resonance → negative group delay) to **+0.54 ± 0.28** (broadband → positive delay).
- Quantitative agreement with theory \(\tau_T = \tau_g\) across pulse bandwidth and optical depth.
- Not time travel: conditional average over a post-selected ensemble; unconditional averages stay causal.

## Physical intuition

Near resonance, anomalous dispersion can make a pulse peak exit *earlier* than vacuum would allow (pulse reshaping). Theory says the weak-valued “how long were the atoms excited for this transmitted photon?” equals that group delay. Negative group delay ⇒ negative weak-valued excitation time. The early front of the transmitted pulse is sculpted by coherent forward scattering and interference; weak values can sit outside the eigenvalue spectrum.

## Limitations and assumptions

- All results conditional on transmission; absorbed photons are a different story.
- Large error bars (~30–60% relative); strongest negative case ~2.6σ from zero but theory-consistent.
- Media “negative time” framing needs the weak-value / post-selection qualifier.
- Technical noise hard; substantial upgrades over Sinclair et al. 2022.

## Connections

  - Concepts: [[weak-values]], [[group-delay]], [[coherent-forward-scattering]]
- Time-as-interaction-theme cousin: [[quantum-proper-time]] / [[time-goes-quantum]] (different physics: relativistic operator time vs. optical dwell-time weak values).
- Platform: cold atoms — also appears in [[massive-tunneling-schrodinger-cats]].
- Synthesis: [[quantum-time-across-platforms]]

## Open questions

- Tighter statistics and broadband mapping of \(\tau_T(\omega)\)?
- Implications for quantum memories and storage-time definitions?
- Clearer pedagogical framing that avoids “time travel” misconceptions?

- Synthesis: [[measurement-problem-threads]] (foundations: measurement problem threads)

## Source

- Analysis: `raw/analyses/Experimental Observation of Negative Weak Values for the Time.md`
