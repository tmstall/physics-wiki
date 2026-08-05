---
tags: [papers, black-holes, general-relativity, numerical-relativity]
last_updated: 2026-08-02
status: analysis-ingest
related_papers: [evaporating-charged-black-holes, entropy-maximization-bh-mergers, horizon-direct-wave-gw250114, gravastar-dust-collapse]
source_analysis: "claude_export/extracted-analyses/2026-06-05_the-third-law-is-dead_911cf359.md"
---

# Black Hole Third Law Violation (Vacuum, 5D)

**One-line summary:** Crump, Gadioux, Reall, and Santos construct smooth vacuum spacetimes in five dimensions that drive a black hole to extremality (zero surface gravity / zero Hawking temperature) in finite time — including from pure gravitational waves — falsifying the third law of black-hole mechanics without exotic matter.

## Key claims and results

- **Authors / setting (analysis):** Cambridge DAMTP; numerical GR + characteristic gluing; neural-network ansatz for free data.
- Classical third law (Bardeen–Carter–Hawking analogy): surface gravity $\kappa$ cannot be driven to zero in finite advanced time.
- Prior mathematical counterexamples (Kehle–Unger) needed charged matter with large charge-to-mass ratio. Open question: does pure vacuum gravity still protect the third law?
- This work: **no** — in 5D Einstein gravity with equal-angular-momenta Myers–Perry symmetry, extremal endpoints form in finite time.
- Two constructions: (i) Schwarzschild → extremal Myers–Perry by absorbing gravitational waves; (ii) Minkowski → extremal MP from vacuum gravitational collapse alone.
- Method: characteristic gluing along a null surface; free data $B(V)$, $\Phi(V)$ parametrized as small tanh neural networks; multi-stage optimization (Adam → BFGS → extended-precision quasi-Newton + spectral DG) to residuals $\sim 10^{-20}$.
- 5D equal-spin reduction drops cohomogeneity enough to make the PDE problem tractable while preserving the extremality question.
- Type (i) $C^2$ solutions with $\mathcal{O}(20)$ parameters; type (ii) needs higher matching order near $r=0$.

## Physical intuition

Black-hole mechanics maps temperature to surface gravity and entropy to area. The third law was the safety rail that said “you never quite reach the absolute-zero, extremal edge in finite time” — the same folklore that classical thermodynamics never hits $T=0$ in a finite number of steps. Extremal holes are special: $\kappa=0$, no Hawking glow, degenerate horizon. Earlier counterexamples smuggled in weird charged dust. Here the Cambridge team stitches spacetime patches like a carefully certified clock-domain crossing: early non-extremal (or empty) data, late extremal Myers–Perry data, and a smooth null-surface bridge found by treating the interpolating geometry as a tiny neural network whose weights are optimized until every matching constraint dies. The message is structural: vacuum GR already knows how to pour enough spin (and mass) into a hole to hit the edge of the Kerr/MP bound in finite time. The third law is not a theorem of pure gravity.

## Limitations and assumptions

- Analysis-based ingest; confirm residual levels, smoothness class, and exact theorem statements against the primary paper.
- Construction is **five-dimensional** with high symmetry (equal angular momenta). Full 4D Kerr is cohomogeneity-4 and remains open numerically/analytically at this rigor.
- Numerical existence of highly accurate solutions is extremely strong evidence but is not a classical pure-math uniqueness theorem for all data.
- Astrophysical reach: real 4D Kerr extremality under realistic accretion/spin-up still needs separate arguments.
- Does not by itself settle information paradox or semiclassical evaporation endpoints — it rewrites a classical mechanical law.

## Connections

- Thermodynamics hub: [[black-hole-thermodynamics]], [[hawking-radiation]]
- Interiors / endpoints: [[black-hole-interiors]], [[evaporating-charged-black-holes]], [[reissner-nordstrom]]
- Other classical GR extremes: [[gravastar-dust-collapse]], [[naked-black-hole-candidate]]
- Observational horizon thermodynamics neighbor: [[horizon-direct-wave-gw250114]]
- Synthesis: [[black-hole-evaporation-energy-conditions]] (third-law status affects how seriously one treats “eternal extremal remnants”)
- Key terms: surface gravity $\kappa$, extremal Myers–Perry, characteristic gluing, cohomogeneity, Hawking mass, neural-network spectral ansatz

## Open questions

- Does an analogous vacuum counterexample exist in 4D Kerr?
- How does third-law failure interact with cosmic censorship and near-extremal instability lore?
- Can semiclassical back-reaction restore an effective third law for astrophysical holes?

## Source

- `claude_export/extracted-analyses/2026-06-05_the-third-law-is-dead_911cf359.md`
