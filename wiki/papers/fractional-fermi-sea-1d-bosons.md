---
tags: [papers, cold-atoms, one-dimensional-physics, quantum-criticality]
last_updated: 2026-08-02
status: analysis-ingest
related_papers: [problem-of-time-cold-atoms, massive-tunneling-schrodinger-cats, three-body-quantum-company]
source_analysis: "claude_export/extracted-analyses/2026-06-19_the-sea-that-forgot-half-its-water-bosons_27a5c392.md"
---

# Fractional Fermi Seas in a 1D Bose Gas

**One-line summary:** Cyclic holonomy through the Lieb–Liniger interaction space (repulsive ↔ attractive) “clicks” a 1D Bose gas into fractional Fermi seas with occupancy $1/\ell$ over stretched momentum support — critical states whose correlations sit outside ordinary Tomonaga–Luttinger liquid universality.

## Key claims and results

- Setting: integrable 1D Bose gas (Lieb–Liniger); experimental companion from Innsbruck Cs (Nägerl) with theory (Bastianello et al.); analysis cites PRL + arXiv:2602.17657-class experimental companion.
- Protocol: adiabatic ramps and fast jumps that trace a loop $g_{\rm 1D}:0\to+\infty\to-\infty\to0$, using Feshbach + confinement-induced resonance knobs.
- Each full cycle increments a Haldane-like exclusion parameter (super-fermionic $\alpha=\ell$), stretching the quasi-momentum support and diluting occupancy per mode ($1/\ell$).
- Path goes through Tonks–Girardeau (TG) and super-Tonks–Girardeau (sTG) branches; repulsive and attractive paths are not the same holonomy in Hilbert space.
- Resulting states are claimed to produce Friedel / correlation structure **structurally incompatible** with a standard two-parameter TLL (not merely a weird Luttinger $K$).
- Integrability’s conserved charges protect the exotic excited manifold from immediate thermalization during the protocol.

## Physical intuition

In one dimension you cannot walk around someone: collisions are mandatory, so statistics and interactions fuse. Strongly repulsive 1D bosons “fermionize” (Tonks–Girardeau) and grow an effective Fermi edge. Usually that edge is a solid block of occupancy 1 up to $k_F$. Here experimentalists drive the interaction strength around a closed loop in parameter space — a quantum gear shift. Each lap redistributes the same particle number over a wider momentum sea with thinner occupancy, like parking the same cars in stalls that are twice as wide and half as full. Ordinary Luttinger-liquid lore says everything low-energy collapses to two numbers $(v,K)$; these fractional seas are argued to live at a different kind of critical fixed point entirely.

## Limitations and assumptions

- Analysis-based ingest; verify holonomy increments, $\ell$ sequence, and correlation diagnostics on the primary theory + experiment papers.
- Experimental companion may still have been under review at analysis time; independent platform replication pending.
- Claim of “beyond TLL” is strong — community scrutiny of correlation functional forms is expected.
- Protocol relies on integrability and controlled jumps; imperfections, three-body losses on the attractive side, and finite temperature can degrade the ladder.
- Scaling to large $\ell$ thins occupancy and makes diagnostics harder.

## Connections

- Cold-atom foundations neighbors: [[problem-of-time-cold-atoms]], [[massive-tunneling-schrodinger-cats]], [[three-body-quantum-company]]
- 2D moiré fractional optical fingerprints: [[anyon-trions-twisted-mote2]]
- 1D anyon momentum tails (theory): [[1d-anyons-momentum-tails]]
- Key terms: Lieb–Liniger, Tonks–Girardeau, super-Tonks–Girardeau, Tomonaga–Luttinger liquid, Haldane exclusion statistics, quantum holonomy, Friedel oscillations

- Synthesis: [[amo-quantum-state-control]] (AMO state control)
- Synthesis: [[condensed-matter-topology-fractionalization]] (fractionalization & topology map)

## Source

- `claude_export/extracted-analyses/2026-06-19_the-sea-that-forgot-half-its-water-bosons_27a5c392.md`
