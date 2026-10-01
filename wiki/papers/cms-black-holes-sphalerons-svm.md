---
tags: [papers, lhc, cms, black-holes, machine-learning]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [nuclear-dense-matter-precision, high-pt-physics-cern-isr, primordial-black-holes]
source_analysis: "raw/analyses/2026-09-26_doi-10.31526-PHEP.2026.21_cms-black-holes-sphalerons-phase-space-svm.md"
---

# CMS Limits on Microscopic Black Holes and Sphalerons (Phase-Space SVM)

**One-line summary:** PHEP 2026.21 DOI 10.31526/PHEP.2026.21. No micro-BHs below ~9–11 TeV and no sphalerons in 2016–2018 CMS data. Novelty is embedding events as points in N-body phase space and classifying by SVM distance; generalized to an untrained signal. Proceedings does not prove the method beats standard cuts (~1.5–2× beyond 4× data). Final JHEP numbers may differ.

## Key claims and results

- CMS conference proceedings (PHEP 2026.21; arXiv:2511.10662) report a null search on the full Run-2 dataset (138 fb$^{-1}$) for high-multiplicity isotropic sprays from microscopic black holes and electroweak sphalerons. The underlying note is CMS-PAS-EXO-24-028.
- Proceedings exclusions: black-hole minimum masses about 9.0–11.4 TeV, and a sphaleron pre-exponential factor below 0.0025. The final journal paper (JHEP 08 (2026) 098) shifts these (about 8.4–11.4 TeV, PEF < 0.0034) and adds string balls. Quote the journal for the limits.
- Each collision is padded to 30 objects and embedded on the N-body phase-space manifold (energy-fraction simplex times direction sphere). An SVM cuts on distance in that geometry. One threshold, trained on a black-hole mix, also tags sphalerons it never saw.
- The 2016 cut-based search (35.9 fb$^{-1}$) reached ~10.1 TeV and PEF < 0.021. Four times the data does not explain the whole gain. A rough luminosity scaling leaves about 1.5–2×, mixed with a new sphericity cut. The proceedings shows no ablation.

## Physical intuition

If gravity leaks into large extra dimensions, a 13 TeV collision might make a microscopic black hole that evaporates at once into a democratic spray of jets, leptons, and photons. An electroweak sphaleron — the saddle between neighboring vacua, barrier near 9 TeV — would dump one fermion from each left-handed doublet and look similar. CMS stopped counting objects and asked how far two whole events sit in the geometry of shared energy and directions. That structured similarity search found no excess. The limits already sit near the beam energy, so more luminosity buys little mass reach.

## Limitations and assumptions

- Semiclassical gravity wants $M_{\rm BH} \gg M_D$. The excluded corner is near $M_{\rm BH}/M_D \sim 1$–1.5, so the limits constrain generator ansätze, not reliable black holes.
- The flagship $n = 2$, few-TeV benchmark is already closed by astrophysics. A plot of discrete $n$ does not license “only one extra dimension.”
- Whether a 9 TeV collision actually crosses the sphaleron barrier is contested. The result bounds a phenomenological factor, not a calculated rate.
- Zero-padding makes an event’s distance to itself “small but nonzero,” which is not a true metric. The background transfer factor is checked in a different event topology.
- Proceedings numbers are preliminary and slightly inconsistent on the PEF range. Use the JHEP paper for quotations.

## Connections

- Synthesis: [[nuclear-dense-matter-precision]]
- Earlier hard-scatter program: [[high-pt-physics-cern-isr]]
- Early-universe black holes (different origin): [[primordial-black-holes]]

## Source

- `raw/analyses/2026-09-26_doi-10.31526-PHEP.2026.21_cms-black-holes-sphalerons-phase-space-svm.md`
