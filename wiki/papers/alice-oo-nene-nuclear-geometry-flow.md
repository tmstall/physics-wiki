---
tags: [papers, heavy-ion, qgp, nuclear-structure, alice]
last_updated: 2026-08-29
status: analysis-ingest
related_papers: [equilibrated-fraction-oo-qcd, rhic-net-proton-fluctuations, alice-jpsi-gluon-saturation, star-jpsi-spin-interference, nucleus-shell-src-memory, na61-isospin-kaon-asymmetry, tracking-baryon-number-nuclear-collisions]
source_analysis: "raw/analyses/2026-08-20_doi-10.1103-gymp-vp87_nuclear-geometry-anisotropic-flow-oo-nene.md"
---

# ALICE O+O / Ne+Ne: Nuclear Geometry Imprinted in Anisotropic Flow

**One-line summary:** First ALICE $v_2$/$v_3$ in O+O and Ne+Ne at $\sqrt{s_{NN}}=5.36$ TeV match ab initio shape-informed hydro (NLEFT/PGCM→Trajectum); Ne/O ratios favor small subnucleon width (~0.1–0.2 fm) and confirm tetrahedral vs bowling-pin geometry contrast in central collisions (APS DOI 10.1103/gymp-vp87).

## Key claims and results

- **Paper:** ALICE Collaboration — DOI 10.1103/gymp-vp87 (Letter); ~3×10⁹ O+O and ~4×10⁸ Ne+Ne events (July 2025 light-ion run).
- Observables: $v_2\{2\}$, $v_2\{4\}$, $v_3\{2\}$ with $|\Delta\eta|>1.4$ gap on 2-particle cumulants; $v_2\{4\}$ nonzero → collective many-body anisotropy.
- Hydro + NLEFT nuclear configs reproduce $v_n$ trends to ~50% centrality; PGCM slightly worse centrally.
- Ne–Ne/OO $v_2$ ratio ~1.05–1.08; NLEFT/PGCM slightly overestimate; IP-Glasma ($w_q\sim0.11$ fm) matches better than Trajectum’s Pb-Pb-tuned $w_q\sim0.40$ fm.
- Central $v_3/v_2$ larger in O+O than Ne+Ne — as expected if ¹⁶O tetrahedral octupole &gt; ²⁰Ne bowling-pin quadrupole.
- pp “sign problem” in some flow-fluctuation observables **not** seen in these light-ion systems.
- Near-simultaneous ATLAS/CMS measurements on the same run (cited) — multi-detector, one beam delivery.

## Physical intuition

The QGP is a mold cast: initial nuclear shape → pressure gradients → momentum anisotropy. Protons are bad molds (unknown guts). Oxygen (tetrahedral α clusters) and neon (bowling pin) are calculable molds — if hydro is real, their different casts must differ by the amount nuclear theory predicts.

## Limitations and assumptions

- Ground states are lab-frame spherical ($J^\pi=0^+$); “tetrahedron/bowling pin” are intrinsic, model-interpreted shapes.
- Subnucleon-width tension across frameworks remains open.
- One short dedicated run — not an independent-facility repeat.
- Mapping flow→shape is complementary to low-energy structure, not a replacement.

## Connections

- **Same O+O run, complementary question:** [[equilibrated-fraction-oo-qcd]] — DCCI2 core/corona fractions ask how much of the yield is equilibrated fluid (~30% corona floor even centrally); this page asks whether ab initio nuclear *shape* imprints $v_n$ once a hydro stage is assumed.
- Nuclear / dense-matter neighbors: [[rhic-net-proton-fluctuations]], [[tracking-baryon-number-nuclear-collisions]], [[nucleus-shell-src-memory]], [[na61-isospin-kaon-asymmetry]]
- Hard probes at LHC: [[alice-jpsi-gluon-saturation]], [[star-jpsi-spin-interference]]
- Synthesis: [[nuclear-dense-matter-precision]]

## Open questions

- Bayesian re-fit of $w_q$ jointly to light-ion + Pb-Pb + HERA incoherent J/ψ?
- Will a second light-ion run stabilize the Ne/O ratio systematics?
- How small can systems go before hydro fails once geometry is controlled?
- Does clustered $^{16}$O geometry (NLEFT/PGCM) change DCCI2-style core fractions, or mainly anisotropic-flow ratios ([[equilibrated-fraction-oo-qcd]])?

## Source

- `raw/analyses/2026-08-20_doi-10.1103-gymp-vp87_nuclear-geometry-anisotropic-flow-oo-nene.md`
