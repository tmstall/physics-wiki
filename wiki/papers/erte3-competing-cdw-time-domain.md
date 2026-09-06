---
tags: [papers, condensed-matter, cdw, ultrafast, trarpes]
last_updated: 2026-08-22
status: analysis-ingest
related_papers: [quantum-metallurgy-cdw, tise2-core-level-cdw-excitons, snte-light-topological-inversion, hot-electron-coherent-phonons-ptcu, attosecond-stm-lightwave]
source_analysis: "raw/analyses/2026-08-19_doi-10.1038-s41567-026-03382-5_time-domain-competing-cdw-ErTe3.md"
---

# Competing CDWs in ErTe₃: Time-Domain Transition-Order Diagnostic

**One-line summary:** trARPES + TDGL modeling show ErTe₃’s dominant c-CDW recovers like a continuous (second-order) order while the subdominant a-CDW recovers fluence-independently — consistent with first-order nucleation — resolving X-ray vs Raman soft-mode contradiction (*Nat. Phys.* 2026).

## Key claims and results

- **Paper:** Su, Lv, Zong et al., *Nature Physics* (2026), DOI 10.1038/s41567-026-03382-5; arXiv:2503.13936.
- Material: ErTe₃ — dominant c-CDW (~265 K, $\Delta_c\sim0.14$ eV, soft-phonon textbook); subdominant a-CDW (~160 K, $\Delta_a\sim0.04$ eV, no soft phonon in IXS; Raman claimed softening).
- Method: pump–probe trARPES (1.2 eV pump; 10.8 eV probe) capturing **both** gaps in one momentum window; fluence-dependent recovery times 0.1–2 ps.
- Discriminant: c-CDW recovery slows nearly linearly with fluence (second-order-like); a-CDW recovery stays flat (~<10% variation over ~10× fluence) → nucleation/first-order scenario, not coupled second-order for both.
- Broader claim: fluence dependence of non-equilibrium recovery as a transferable probe of transition order when equilibrium probes disagree.

## Physical intuition

Same crystal, same electrons, two ripples. Knock both down with a laser. A continuous order rebuilds slower after a harder hit (more fluctuations to dump). A first-order order rebuilds by seeding and growing at a rate set by free-energy drive — roughly independent of how hard you hit. Flat vs linear recovery-vs-fluence is the tell.

## Limitations and assumptions

- Nucleation inferred from timing + TDGL, **not** real-space imaging of domains.
- Single collaboration; no independent ultrafast replication yet.
- Preprint→journal gap: analysis used arXiv paraphrase; verify final *Nat. Phys.* numerals.
- Wiedemann–Franz anomaly below $T_a$ is consistent with, not proven caused by, first-order a-CDW.

## Connections

- CDW neighbors: [[quantum-metallurgy-cdw]], [[tise2-core-level-cdw-excitons]], [[snte-light-topological-inversion]]
- Ultrafast probes: [[attosecond-stm-lightwave]], [[hot-electron-coherent-phonons-ptcu]]
- Synthesis: [[condensed-matter-topology-fractionalization]], [[ultrafast-optics-and-solid-state-emitters]]

## Open questions

- Ultrafast diffraction confirmation of fluence-flat a-CDW recovery?
- Apply the same diagnostic to another CDW with known transition order as a method validation?
- Microscopic origin of first-order character for the subdominant order?

## Source

- `raw/analyses/2026-08-19_doi-10.1038-s41567-026-03382-5_time-domain-competing-cdw-ErTe3.md`
