---
tags: [papers, nuclear-physics, qcd, deep-inelastic-scattering]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [nucleus-shell-src-memory, high-pt-physics-cern-isr, star-jpsi-spin-interference, color-superconductivity-qcd, na61-isospin-kaon-asymmetry, rhic-net-proton-fluctuations]
source_analysis: "spacex_export/extracted-analyses/2025-08-29_emc-effect-quarks-and-gluons_a467bb47.md"
cleanup_note: "2026-08-04: claims retied to arXiv:2410.12099 abstract/body; conversational extract drift corrected"
---

# EMC Effect in Tritium and ³He (JLab MARATHON)

**One-line summary:** MARATHON at Jefferson Lab Hall A reports the first tritium EMC measurement and precise $A=3$ mirror EMC ratios for $^3$H and $^3$He ($0.20<x<0.83$), consistent with isoscalar off-shell models and **without** evidence for a large isovector EMC component (arXiv:2410.12099).

## Key claims and results

- **Paper:** D. Abrams et al. (Jefferson Lab Hall A Tritium Collaboration), “The EMC Effect of Tritium and Helium-3 from the JLab MARATHON Experiment,” arXiv:2410.12099 [nucl-ex] (15 Oct 2024); also *Phys. Rev. Lett.* lineage (2025).
- Setup: 10.59 GeV electron beam; cryogenic gas targets ($^2$H, $^3$H, $^3$He) at ~40 K; Hall A High Resolution Spectrometers.
- Kinematics: Bjorken $x$ from **0.20 to 0.83**; $Q^2$ from **2.7 to 11.9 (GeV/$c$)$^2$**; $W>1.84$ GeV/$c^2$ (DIS regime).
- EMC-type ratios: per-nucleon nuclear / deuterium cross sections, with isoscalarity corrections using MARATHON’s own $R_{np}=\sigma_n/\sigma_p$.
- **First** direct tritium EMC measurement; $^3$He and $^3$H as mirrors constrain isospin-dependent medium modifications.
- Isoscalar $A=3$ combination $(\sigma_h+\sigma_t)/(2\sigma_d)$ matches the $A$-dependent SLAC-E139 parametrization trend for light nuclei.
- Linear slopes of isoscalar EMC ratios for $0.3<x<0.7$: $^3$He **$-0.085\pm0.037$**, $^3$H **$-0.10\pm0.04$** (comparable magnitudes within uncertainties).
- Agreement with Kulagin–Petti (K-P) nuclear convolution + **isoscalar** off-shell correction over the full $x$ range ($\chi^2$/dof ~1 for relevant comparisons).
- **Does not** support a sizable **isovector** EMC component of the kind argued in Tropiano et al. (TEMS) fits — an important correction relative to conversational “$^3$H vs $^3$He difference proves isospin medium effect” narratives.
- Consistency with overlapping HERMES $^3$He data; Hall C E03-103 $^3$He data mutually consistent after ~2.5% normalization discussion in the paper.

## Physical intuition

A free nucleon’s quark PDFs are its internal traffic map. Drop that nucleon into a three-body nucleus and Fermi motion, binding, and off-shell dressing redraw the map. Measuring $^3$H (two $n$, one $p$) against $^3$He (two $p$, one $n$) is the cleanest isospin swap available — but after proper isoscalarity corrections, MARATHON finds the two EMC slopes nearly the same and well described by a single isoscalar off-shell function. The nuclear medium modifies structure; a large *proton-vs-neutron-different* EMC dressing is not required by these data.

## Limitations and assumptions

- **Source quality:** SpaceX extract is conversational Grok Q&A that only gradually identified arXiv:2410.12099; early turns mixed general EMC lore and wrong paper guesses. **This page is retied to the primary arXiv**, not the chat path.
- Isoscalarity corrections use model super-ratio $\mathcal{R}_{ht}$ (K-P); residual model dependence at the $\lesssim1\%$ level for most $x$.
- SRC-linked and few-body light-front calculations also compared; model discrimination remains active.
- Low-$x$ shadowing is not the focus of this DIS valence-region result.

## Connections

- Nuclear short-range structure: [[nucleus-shell-src-memory]]
- High-energy nuclear / partons: [[high-pt-physics-cern-isr]], [[star-jpsi-spin-interference]]
- Dense QCD context: [[color-superconductivity-qcd]]
- SPS isospin / strangeness neighbor: [[na61-isospin-kaon-asymmetry]]
- Critical-point fluctuation scan: [[rhic-net-proton-fluctuations]]
- Key terms: EMC ratio, DIS, Bjorken $x$, MARATHON, isoscalar off-shell correction, $A=3$ mirrors
- Synthesis: [[nuclear-dense-matter-precision]] (nuclear & dense-matter precision map)

## Source

- `spacex_export/extracted-analyses/2025-08-29_emc-effect-quarks-and-gluons_a467bb47.md`
- Primary: arXiv:2410.12099
