---
tags: [papers, particle-physics, flavor, lhc]
last_updated: 2026-08-01
status: analysis-ingest
related_papers: [high-pt-physics-cern-isr, levinthal-high-pt-isr]
source_analysis: "raw/analyses/List2_Combined_Clean.md (The B-Meson's Forbidden Shortcut; The Flavor Anomaly That Won't Die)"
---

# The B-Meson’s Forbidden Shortcut (LHCb \(b\to s\mu\mu\))

**One-line summary:** Full Run 1+2 LHCb analysis of \(B\to K^*\mu^+\mu^-\) with a true 5D fit and first-ever muon-mass correction still finds the long-standing angular anomaly (notably \(P_5'\)): data prefer a ~23% deficit in the effective vector Wilson coefficient \(C_9\) relative to the Standard Model—new physics or underestimated QCD remains open.

## Key claims and results

- **Paper:** *A comprehensive analysis of the \(B^0 \to K^{*0}\mu^+\mu^-\) decay*, *Phys. Rev. Lett.* (2026). DOI: 10.1103/24g9-yn9d; arXiv:2512.18053.
- Channel: rare FCNC penguin decay \(B\to K^*(892)\mu^+\mu^-\) (final state \(K\pi\mu\mu\)); full 8.4 fb⁻¹ Run 1+2 — definitive Run 1+2 close-out before Upgrade I dominates.
- Analysis upgrades: full 5D unbinned fit (3 angles + \(q^2\) + \(m(K\pi)\)); S-wave / P-wave interference as signal, not nuisance; muon mass effects included; dual independent software frameworks.
- Pattern of deviations since ~2013 confirmed at highest precision; \(P_5'\) systematically low vs SM in key \(q^2\) bins; significance still sub-discovery (~2–3σ class) because **theory**, not stats, is the bottleneck.
- Global EFT fit: \(\Delta C_9 \sim -23\%\) (vector \(bs\mu\mu\) coupling) drives the anomaly; CP asymmetries consistent with zero (rules out large new CP-odd phases in this channel).
- Compatible with prior LHCb and independent CMS patterns. \(R_K\)/\(R_{K^*}\) lepton-universality ratios softened after 2022 background reanalysis—angular anomaly remains the stubborn pillar.
- Open fork: heavy new particles in the loop (Z′, leptoquark, …) vs long-distance charm/QCD pollution.
- **Ingest note:** List2 filed two analyses of the *same* PRL/arXiv result (*Forbidden Shortcut* + *Flavor Anomaly That Won't Die*); consolidated here.

## Physical intuition

A \(b\) quark cannot freely turn into an \(s\) quark plus muons at tree level—flavor rules force a rare quantum detour through virtual W/top loops. That detour is a microscope for anything new that can join the loop. Angular shapes of the four final particles are the fingerprint; \(P_5'\) is a clever ratio that cancels a lot of form-factor fog so the fingerprint stays sharp.

## Limitations and assumptions

- Experiment alone cannot separate new short-distance physics from hadronic long-distance effects.
- Theory uncertainties on non-local charm contributions remain the dominant interpretation risk.
- Run 3 (~3× statistics already collected per analysis) will push significance or wash the tension out—decisive either way only with better theory in parallel.
- Local form-factor and acceptance modeling systematics still matter even with dual frameworks.

## Connections

- HEP historical / collider neighbors: [[high-pt-physics-cern-isr]], [[parton-jets]]
- Key terms: **Wilson coefficients** (e.g. \(C_9\), \(C_{10}\)) package short-distance \(b\to s\ell\ell\) physics in an EFT—experiments fit them when angular shapes deviate from the SM.
- Concepts: [[flavor-changing-neutral-current]]

## Source

- Analysis: `raw/analyses/List2_Combined_Clean.md` — *The B-Meson's Forbidden Shortcut.md*
