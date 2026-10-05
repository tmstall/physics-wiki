---
tags: [papers, black-holes, ringdown, quasinormal-modes, quantum-gravity]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [black-hole-evaporation-energy-conditions, black-hole-interiors, horizon-direct-wave-gw250114, entanglement-islands-page-curves-kerr-ads, gauss-bonnet-qnm-spectral-atlas]
source_analysis: "raw/analyses/2026-09-28_arxiv-2609.20788_looking-inside-a-quantum-black-hole.md"
---

# Looking Inside a Quantum Black Hole via Ringdown Overtones

**One-line summary:** arXiv:2609.20788. Highest quasinormal overtones profile the center: how the spin-dependent ringing shrinks with overtone number encodes the blow-up exponent. Difference of two azimuthal numbers cancels path dependence in the complex plane. In an exact quantum-corrected example the exponent climbs 0→1/4; in the 4D lift that “quantum core” is a classical singularity on a slice.

## Key claims and results

- Letter arXiv:2609.20788v2 (hep-th): highly damped quasinormal modes of a 2+1-dimensional quantum BTZ black hole read the near-center blow-up exponent $s$ of the metric function $f(r)$.
- Near the center the radial wave is a Bessel function with index $\nu = s / (2(s+1))$. Classical BTZ ($s = 0$, $f$ finite) gives $\nu = 0$. The quantum piece ($s = 1$, a $1/r$ blow-up) gives $\nu = 1/4$.
- The leading tone ladder sits at $n\pi$ plus an offset fixed by $s$ — but that offset also depends on an assumed Stokes-line layout in the complex radial plane. Subtract two azimuthal numbers $m$. Layout-sensitive pieces cancel. The leftover scales as $(m_1^2 - m_2^2)\, n^{-2\nu}$, and the power of $n$ does not depend on the layout constant.
- A local estimator $\nu_{\rm eff}$ reads that shrink rate between neighboring overtones. A layered center makes $\nu_{\rm eff}$ drift with $n$.
- Exact quantum BTZ has a classical constant term and a backreaction term $\propto 1/r$. Numerics: for weak quantum strength $\ell$, $\nu_{\rm eff}$ climbs from $0$ toward $1/4$; larger $\ell$ moves the switch to lower $n$. The smallest $\ell$ needs hundreds of thousands of overtones.
- The ringing returns one Kasner mix, $q = 2(1 - p_\phi)/(1 - p_t)$, not both exponents separately. One blackening factor ties them: quantum core $(-1/3, 2/3)$, classical BTZ $(0, 1)$.
- Hartnoll & Zhiboedov (arXiv:2609.07514) reached a version of the readout in parallel. The companion (arXiv:2609.26724) was abstract-only in this analysis.

## Physical intuition

A very wiggly wave ignores gentle terrain and responds only where the geometry is sharpest — the center. Sweeping the overtone number is a memory-mountain profiler: moderate $n$ sees the mild classical layer, huge $n$ sees the core. The absolute ladder shift still depends on which complex-plane route you assumed. Subtract two swirl rates, the way a microbenchmark subtracts an empty loop, and the shrink rate of the difference is the center’s exponent.

## Limitations and assumptions

- In principle only. Overtones from $n \sim 100$ to $\sim 10^5$ damp far too fast for any detector. The dual description in which they might be observable is not computed.
- The Stokes layout is an assumption (Schwarzschild-AdS-like). The claim that the exponent survives other layouts is argued, not proved, and checked numerically for one black hole.
- The readout returns one combination of stretch-and-squeeze exponents. Two blackening factors leave them entangled.
- Quantum BTZ is semiclassical: a classical geometry sourced by a large quantum field, built as a braneworld slice. The pair $(-1/3, 2/3)$ matches the time and angle directions of the 4D Schwarzschild interior, so the “quantum core” is a classical singularity seen on a slice (analyst identification).
- The probe is a scalar wave on a static, uncharged, 2+1D hole. Charge, other asymptotics, higher dimensions, and matter are open. Older power-law-center QNM papers (hep-th/0410209, hep-th/0510186) are not cited in the Letter.

## Connections

- What can be inferred past the horizon: [[black-hole-interiors]]
- Semiclassical endpoints and energy conditions: [[black-hole-evaporation-energy-conditions]]
- Observed ringdown versus a horizon-locked direct wave: [[horizon-direct-wave-gw250114]]
- Higher-D Gauss–Bonnet tone catalogue (classical spectrum, not an interior probe): [[gauss-bonnet-qnm-spectral-atlas]]
- Information and islands on the interior side: [[entanglement-islands-page-curves-kerr-ads]]

## Source

- `raw/analyses/2026-09-28_arxiv-2609.20788_looking-inside-a-quantum-black-hole.md`
