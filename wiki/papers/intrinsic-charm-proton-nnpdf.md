---
tags: [papers, qcd, parton-distributions, nucleon-structure, lhc]
last_updated: 2026-08-19
status: analysis-ingest
related_papers: [emc-effect-marathon-a3, alice-jpsi-gluon-saturation, star-jpsi-spin-interference, high-pt-physics-cern-isr, b-meson-fcnc-anomaly]
source_analysis: "raw/analyses/2026-08-19_doi-10.1038-s41586-022-04998-2_intrinsic-charm-proton-nnpdf.md"
---

# Intrinsic Charm in the Proton (NNPDF4.0)

**One-line summary:** NNPDF’s scheme-based 4FNS→3FNS matching isolates a valence-like intrinsic-charm PDF peaking near $x\approx0.4$; LHCb $Z+$charm-jet and EMC charm data push local significance to ~3σ “evidence” (*Nature* 2022) — not a 5σ discovery.

## Key claims and results

- **Paper:** NNPDF Collaboration, *Nature* **608**, 483–487 (2022). DOI 10.1038/s41586-022-04998-2.
- Question: are charm quarks only radiatively generated, or also **intrinsic** in the proton’s bound-state structure?
- Method: fit unconstrained charm PDF in 4FNS (neural-net NNPDF4.0, 4618 cross-sections); transform to 3FNS via NNLO matching (EKO) where pure radiation must vanish → residual = intrinsic by definition.
- Shape: valence-like bump at $x\approx0.4$; momentum fraction $(0.62\pm0.61)\%$ including theory uncertainty.
- Forcing IC→0 worsens global $\chi^2$ (~2σ-class global effect); peak-region local significance ~2.5σ → ~3σ with out-of-sample LHCb $R_c^j(y_Z)$ and/or EMC charm production.
- Forward LHCb $Z+$charm-jet bin: zero-IC prediction undershoots data ~3σ; IC-inclusive matches.

## Physical intuition

Radiative charm is the part you can **recompute** from light quarks via QCD matching — like memoized derived state. Subtract that recomputable piece; whatever survives in the 3-flavour scheme is the proton’s non-radiative charm residue. The residue prefers carrying a large momentum fraction (~40%), not a soft sea-like smear.

## Limitations and assumptions

- Single PDF collaboration / framework; CTEQ/MSHT have not yet repeated this exact disentangling.
- Matching truncates at finite order; theory error blows up at small $x$.
- EMC data imprecise / contested — used as cross-check, not baseline.
- Title says “evidence” (~3σ tier), not observation/discovery (5σ).

## Connections

- Concepts: [[parton-jets]] (hard-probe / parton structure ladder)
- Nuclear / medium EMC cousin (different question — nuclei, not free-proton IC): [[emc-effect-marathon-a3]]
- Collider hard probes: [[alice-jpsi-gluon-saturation]], [[star-jpsi-spin-interference]], [[high-pt-physics-cern-isr]]
- Flavor neighbor: [[b-meson-fcnc-anomaly]]
- Synthesis: [[nuclear-dense-matter-precision]]
- Reverse-link: [[x2370-pseudoscalar-glueball]]

## Open questions

- Will CT/MSHT reproduce the 3FNS residual with independent fits?
- EIC / FPF / neutrino-telescope sensitivity to the large-$x$ IC peak?
- Lattice or nonperturbative insight into the $x\sim0.4$ shape?

## Source

- `raw/analyses/2026-08-19_doi-10.1038-s41586-022-04998-2_intrinsic-charm-proton-nnpdf.md`
