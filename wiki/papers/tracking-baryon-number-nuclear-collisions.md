---
tags: [papers, heavy-ion, qcd, nucleon-structure, star, rhic]
last_updated: 2026-08-29
status: analysis-ingest
related_papers: [rhic-net-proton-fluctuations, star-jpsi-spin-interference, alice-jpsi-gluon-saturation, alice-oo-nene-nuclear-geometry-flow, intrinsic-charm-proton-nnpdf, x2370-pseudoscalar-glueball, na61-isospin-kaon-asymmetry]
source_analysis: "raw/analyses/2026-08-23_doi-10.1126-science.ads5962_tracking-baryon-number-nuclear-collisions.md"
---

# Tracking Baryon Number with Nuclear Collisions (STAR)

**One-line summary:** STAR’s three-channel RHIC program (isobar Ru+Ru/Zr+Zr, γ+Au UPCs, Au+Au energy scan) finds enhanced mid-rapidity baryon transport that disfavors a pure valence-quark carrier and favors a soft, gluon-based baryon junction — without closing a hybrid picture (*Science* 2026; DOI 10.1126/science.ads5962).

## Key claims and results

- **Paper:** STAR Collaboration, “Tracking the baryon number with nuclear collisions,” *Science* **393**(6812), 727–731 (2026). DOI 10.1126/science.ads5962; arXiv:2408.15441 companion.
- Question: is baryon number $B$ physically carried as $B=1/3$ per valence quark, or by a Y-shaped gluon “baryon junction” (Kharzeev 1996)?
- **Isobar double ratio:** Ru+Ru vs Zr+Zr at $\sqrt{s_{NN}}=200$ GeV (~2×10⁹ events each). Central (0–10%) $B/\Delta Q = 1.84 \pm 0.02\ \mathrm{(stat.)} \pm 0.09\ \mathrm{(syst.)} \pm 0.16\ \mathrm{(feed\text{-}down)}$ — far above unity and above valence-only generators (PYTHIA/HERWIG/UrQMD ~0.5–0.7). PYTHIA with color-reconnection Mode 2 reaches only $0.99\pm0.03$.
- **Photonuclear γ+Au:** photon carries $B=0$, so net-proton asymmetry traces target transport. Fitted slope $\alpha_B = 1.04\pm0.22$ in $f(y)\propto e^{\alpha_B y}$; Regge+junction band $0.42<\alpha_B<1$ — consistent within error, central value at the upper edge.
- **Au+Au reanalysis** ($\sqrt{s_{NN}}=7.7$–$200$ GeV): average $\alpha_B=0.64\pm0.05$, centrality-independent, within ~1.7σ of the photonuclear result.
- Framing: gluons carry baryon number **at least in part**; result *disfavors* clean valence-only bookkeeping rather than proving quarks carry zero $B$.

## Physical intuition

Think of the three valence quarks as high-bandwidth data links and the junction as a soft control channel carrying the routing header (baryon number). At high enough collision energy, fast quarks keep barreling near beam rapidity while soft gluonic structure is easier to strip off and leave near mid-rapidity ($y\approx0$). STAR measures that mid-rapidity pile-up three independent ways — including photonuclear collisions where the projectile itself has no baryon number to contribute.

## Limitations and assumptions

- Evidence is statistical transport asymmetries over billions of events — not a per-event image of a Y-shaped junction.
- Largest isobar uncertainty is neutron feed-down (±0.16), estimated from protons plus deuteron/antideuteron coalescence, not direct neutron tracking.
- Best junction-friendly model still undershoots measured $B/\Delta Q$ (0.99 vs 1.84) — data lead available theory.
- Single facility (STAR/RHIC); no independent LHC/elsewhere replication of these three signatures yet.
- Analysis text retrieved via paraphrase-mediated arXiv (2024) vs final *Science* (2026); exact final systematics may differ slightly.

## Connections

- Same STAR / baryon-number laboratory: [[rhic-net-proton-fluctuations]] (fluctuations of net protons vs this paper’s *transport* of mean net baryon)
- Photonuclear / UPC neighbors: [[star-jpsi-spin-interference]], [[alice-jpsi-gluon-saturation]]
- Heavy-ion geometry cousin: [[alice-oo-nene-nuclear-geometry-flow]]
- Nonperturbative nucleon / gluonic structure: [[intrinsic-charm-proton-nnpdf]], [[x2370-pseudoscalar-glueball]]
- Isospin / isobar-style control: [[na61-isospin-kaon-asymmetry]]
- Synthesis: [[nuclear-dense-matter-precision]]

## Open questions

- Will a hybrid quark+junction carrier model close the $B/\Delta Q$ gap to 1.84?
- Independent-facility analog (LHC UPC / isobar-like ratios) of $\alpha_B$ and the isobar double ratio?
- How should BES-II net-proton *fluctuation* baselines talk to this *mean-transport* junction claim without conflating the two?

## Source

- `raw/analyses/2026-08-23_doi-10.1126-science.ads5962_tracking-baryon-number-nuclear-collisions.md`
