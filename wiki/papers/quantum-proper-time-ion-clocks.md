---
tags: [papers, quantum-metrology, relativity, ion-clocks, squeezing]
last_updated: 2026-08-01
status: analysis-ingest
related_papers: [time-goes-quantum]
source_analysis: "raw/analyses/Quantum Proper Time Goes Live in Ion Clocks.md; raw/analyses/Ion Clocks Enter the Quantum Proper-Time Regime.md"
---

# Quantum Signatures of Proper Time in Optical Ion Clocks

**One-line summary:** Sorci et al. show that treating proper time as an operator on a trapped ion yields vacuum, squeezing-induced, and intrinsically quantum SODS corrections — with motional squeezing turning time-dilation entanglement into measurable Ramsey visibility loss.

## Bibliographic

- **Gabriel Sorci, Joshua Foo, Dietrich Leibfried, Christian Sanner, Igor Pikovski**, *Phys. Rev. Lett.* **136**, 163602 (2026). DOI: 10.1103/qhj9-pc2b; arXiv:2509.09573.
- Same paper ingested under two analysis titles (“Quantum Proper Time Goes Live…” and “Ion Clocks Enter the Quantum Proper-Time Regime”).

## Key claims and results

- Classical metrology replaces time dilation with an average \(\langle v^2\rangle\). Keeping **operators** for momentum turns textbook SODS into an **entangling interaction** between internal clock and center-of-mass motion.
- Three quantum extensions of SODS:
  - **vSODS** — zero-point momentum fluctuations already redshift the clock: \(\Delta\nu/\nu \sim -\hbar\omega/(4mc^2)\).
  - **sqSODS** — motional squeezing amplifies the shift \(\propto \cosh(2r)\).
  - **qSODS** — non-classical phase from full unitary evolution (state-dependent squeezing); not reproducible by any semiclassical \(\langle\tau\rangle\).
- Example Al⁺ / 20 MHz trap scales (from analysis): \(\varepsilon_m = \hbar\omega/mc^2 \sim 3\times 10^{-18}\); vSODS \(\sim 5\times 10^{-19}\); realistic squeezing can drive visibility well below unity (e.g. \(V\sim 0.76\) for lighter ions under equal conditions — verify against paper).
- Concrete protocol: prepare squeezed motion → Ramsey on clock transition → read entanglement as contrast loss; optional motional post-selection for qSODS.

## Physical intuition

The ion is a tiny watch whose gears also jiggle from quantum uncertainty. Even in the motional ground state the jiggling slows the gears slightly (vSODS). Squeeze the jiggling and the watch’s face and its motion start to dance in step — different momentum branches tick at different rates — so Ramsey fringes lose contrast. That visibility drop is the smoking gun that proper time was not a single classical number.

## Limitations and assumptions

- Low-velocity expansion; gravity omitted (special-relativistic table-top regime).
- qSODS still tiny; needs excellent squeezing and coherence.
- Multi-ion logic clocks have richer mode structure than the single-mode model.

## Connections

- Complements [[time-goes-quantum]] (revival / characteristic-function view of the same coupling family).
- Core concepts: [[quantum-proper-time]], [[second-order-doppler-shift]], [[motional-squeezing]], [[ramsey-interferometry]].
- Platform: [[optical-ion-clocks]].
- Metrology cousin: [[collective-superradiant-lasing]].
- Synthesis: [[quantum-time-across-platforms]].

## Open questions

- Quantum feedback from clock readout onto motion?
- Two clocks in a gravitational superposition?
- How far can lighter ions push \(\varepsilon_c = \hbar\omega_c/mc^2\)?

- Synthesis: [[measurement-problem-threads]] (foundations: measurement problem threads)

## Source

- Analyses: `raw/analyses/Quantum Proper Time Goes Live in Ion Clocks.md`; `raw/analyses/Ion Clocks Enter the Quantum Proper-Time Regime.md` (base64 images stripped from the latter).
