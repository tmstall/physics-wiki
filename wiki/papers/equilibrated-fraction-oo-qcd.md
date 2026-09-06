---
tags: [papers, heavy-ion, qgp, qcd, phenomenology, alice]
last_updated: 2026-08-29
status: analysis-ingest
related_papers: [alice-oo-nene-nuclear-geometry-flow, rhic-net-proton-fluctuations, alice-jpsi-gluon-saturation, star-jpsi-spin-interference, tracking-baryon-number-nuclear-collisions, na61-isospin-kaon-asymmetry]
source_analysis: "raw/analyses/2026-08-28_arxiv-2604.05307_equilibrated-fraction-qcd-oo-collisions.md"
---

# Equilibrated Fraction in O+O Collisions (DCCI2 Core–Corona)

**One-line summary:** A DCCI2 hybrid hydro calculation for LHC O+O at $\sqrt{s_{NN}}=5.36$ TeV finds core overtaking corona above $\langle dN_{ch}/d\eta\rangle \approx 20$, yet a persistent ~30% corona floor even in 0–10% central events — full equilibration never arrives at this system size (*Phys. Rev. C* 114, 024906; arXiv:2604.05307).

## Key claims and results

- **Paper:** Naoya Ito & Tetsufumi Hirano, *Phys. Rev. C* **114**, 024906 (2026). DOI 10.1103/r39m-l6gz; arXiv:2604.05307v1.
- Framework: DCCI2 (Dynamical Core–Corona Initialization v2) — PYTHIA8 Angantyr + GLISSANDO 2 initial partons → density-based core/corona split → (3+1)D hydro for the core (Cooper–Frye switch at $T=165$ MeV via iS3D) + Lund string fragmentation for the corona → JAM with **hadronic rescattering off** (resonance decays only) to keep core/corona bookkeeping clean.
- Mid-rapidity charged fraction:
  $$R_{\mathrm{core/corona}} = \frac{\langle dN_{ch}/dY\rangle_{\mathrm{core\,(or\,corona)},\,|Y|<0.5}}{\langle dN_{ch}/dY\rangle_{\mathrm{total},\,|Y|<0.5}}$$
  averaged over $10^5$ events.
- **Multiplicity threshold:** core exceeds corona near $\langle dN_{ch}/d\eta\rangle \approx 20$.
- **Persistent corona floor:** even in 0–10% central O+O, ~30% of the mid-rapidity yield stays corona (~41 of ~136 charged particles in the analysis narrative) — unlike central Pb+Pb, where corona shrinks to a few percent and is often neglected.
- **$p_T$-differential / mass ordering:** core dominance extends to higher $p_T$ for heavier species (pions ~3.3 GeV, kaons ~3.8 GeV, protons ~5 GeV); centrality-binned crossings near ~3.7 GeV (0–30%) and ~2.8 GeV (30–60%) — hydrodynamic radial-flow fingerprint inside a still-mixed system.
- **Strangeness:** $\Lambda,\Xi,\Omega$ / pion ratios climb with multiplicity but never reach a pure-core prediction — same incomplete equilibration told in flavor language.
- Timed to the 2025 LHC light-ion run; predictions are falsifiable against ALICE/CMS/ATLAS O+O analyses.

## Physical intuition

Think of each event as a mixed workload: some partons land in a dense enough neighborhood to thermalize and ride a fluid (**core** = warm cache), others never re-scatter enough and fragment like ordinary vacuum pp debris (**corona** = cold fallback). The split is a local-density *classification*, not a star-like core-vs-atmosphere geometry — corona partons still pepper even the most central events. O+O sits in the sweet spot where the mixture is large enough to measure: big enough for a real hydro droplet to form, small enough that the cold fallback never shrinks to a rounding error. “Core exceeds corona” and “fully equilibrated QGP” are different claims; this paper supports the first and rejects the second for oxygen.

## Limitations and assumptions

- Single theory group / single DCCI2 stack — no independent EPOS/AMPT/PACIAE cross-check of these specific O+O fractions yet; absolute core fraction is somewhat framework-dependent.
- GLISSANDO 2 Woods–Saxon geometry is optimized for heavier nuclei and **does not** encode $^{16}$O’s debated $\alpha$-cluster / tetrahedral structure — tension the authors acknowledge and that experimental flow papers target directly ([[alice-oo-nene-nuclear-geometry-flow]]).
- Hadronic rescattering off is load-bearing for clean bookkeeping; “minor” effect is the authors’ characterization, not a with/without scan in the retrieved analysis.
- PYTHIA version mismatch (production 8.315 vs string fragmentation 8.244) for continuity with prior DCCI2 — quantitative impact not separately assessed here.
- Exact density criterion for the core/corona tag lives in the prior DCCI2 methods paper, not re-derived in this application study.

## Connections

- **Same O+O laboratory, complementary question:** [[alice-oo-nene-nuclear-geometry-flow]] (does ab initio nuclear *shape* imprint $v_n$?) vs this page (what *fraction* of the yield is actually equilibrated fluid?). Stack them: geometry-informed hydro assumes a hydro stage; DCCI2 asks how much of that stage is real vs corona contamination.
- Hot-fireball / small-system neighbors: [[rhic-net-proton-fluctuations]], [[tracking-baryon-number-nuclear-collisions]], [[na61-isospin-kaon-asymmetry]]
- LHC hard / diffractive cousins: [[alice-jpsi-gluon-saturation]], [[star-jpsi-spin-interference]]
- Synthesis: [[nuclear-dense-matter-precision]]

## Open questions

- Do ALICE/CMS/ATLAS O+O data confirm the $\approx 20$ multiplicity threshold, ~30% central corona floor, and mass-ordered $p_T$ crossings?
- Does replacing Woods–Saxon $^{16}$O with NLEFT/PGCM clustered configs (as in [[alice-oo-nene-nuclear-geometry-flow]]) move the core fraction appreciably, or only the anisotropic-flow ratios?
- Will an independent hybrid framework reproduce the same floor within a few percent, or is “30%” DCCI2-specific?

## Source

- `raw/analyses/2026-08-28_arxiv-2604.05307_equilibrated-fraction-qcd-oo-collisions.md`
