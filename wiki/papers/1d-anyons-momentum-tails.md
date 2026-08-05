---
tags: [papers, cold-atoms, anyons, one-dimensional-physics]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [fractional-fermi-sea-1d-bosons, three-body-quantum-company, anyon-trions-twisted-mote2]
source_analysis: "spacex_export/extracted-analyses/2026-05-10_1d-anyons-momentum-tails_6e74a90c.md"
---

# Universal Momentum Tails of 1D Anyons

**One-line summary:** Hidalgo-Sacoto, Busch, and Blume (*Phys. Rev. A* 2025) show 1D anyons split into bosonic and fermionic families; when even- and odd-parity zero-range lengths match, high-momentum tails of $n(k)$ carry universal Tan contacts weighted by trigonometric factors of the statistical angle $\alpha$.

## Key claims and results

- Companion PRA papers: many-body momentum tails + two-body exchange/scattering map (analysis cites DOI 10.1103/zf6z-2jjs and 10.1103/h2vs-ll9d).
- Two families: bosonic anyons (overall $+$) and fermionic anyons (overall $-$) under exchange, each with fractional phase set by $\alpha\in[0,1]$.
- Hamiltonian with even-parity ($g_+\delta$) and odd-parity ($g_-\partial\delta\partial$) contacts; when $a_+=a_-=a_{\rm any}$, both families are exact eigenstates (anyon–anyon mapping).
- Large-$|k|$ tails: $1/k^2$ and $1/k^3$ terms with prefactors $\propto C_2,C_3$ (Tan contacts, $\alpha$-independent) × $\sin$/$\cos$ of $\pi\alpha$.
- $k^{-3}$ term vanishes for ordinary bosons and for fermionic anyons at $\alpha=1$ but survives for generic bosonic anyons — statistical smoking gun.
- Contacts themselves independent of $\alpha$; statistics live only in the trigonometric weights.
- Checked on few-body bound states and small traps.

## Physical intuition

In 1D you cannot walk around someone — exchange is a collision. Anyons put a tunable phase on that handshake. Dress ordinary Bose or Fermi wavefunctions with a position-dependent statistical flag and you get anyons “for free.” The sharp edges at particle coincidence Fourier-transform into power-law momentum tails: the edges tell interaction strength (Tan contacts), the flag tells statistics (sines and cosines of $\alpha$). Same contacts, different tail ratios → you read fractional statistics off a TOF image, in principle.

## Limitations and assumptions

- Strictly zero-range; finite range adds non-universal $k^{-4}+$ terms.
- Single-component continuum gas; lattices/mixtures change allowed $\alpha$.
- Experimental anyon TOF at large $|k|$ not yet demonstrated.
- Analysis-based ingest; verify formulas against primary PRA papers.

## Connections

- 1D fractional holonomy / seas: [[fractional-fermi-sea-1d-bosons]]
- Few-body composites: [[three-body-quantum-company]]
- Optical fractional fingerprints in 2D: [[anyon-trions-twisted-mote2]]
- Key terms: 1D anyons, Tan contact, Bose–Fermi / anyon–anyon mapping, momentum-distribution tail

- Related (SpaceX set): [[nonabelian-photonic-braiding]] — Programmable non-Abelian photonic braiding
- Synthesis: [[condensed-matter-topology-fractionalization]] (fractionalization & topology map)

## Source

- `spacex_export/extracted-analyses/2026-05-10_1d-anyons-momentum-tails_6e74a90c.md`
