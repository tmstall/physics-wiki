---
tags: [papers, lhcb, flavor, rare-decays, b-physics]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [b-meson-fcnc-anomaly, baryon-semileptonic-polarization-entanglement]
source_analysis: "raw/analyses/2026-11-08_arxiv-2611.00230_lhcb-b0-mumu-evidence-bs-mumu-run3.md"
---

# LHCb Run 3: $B^0 \to \mu^+\mu^-$ at Evidence Level

**One-line summary:** With the upgraded detector and 18 fb$^{-1}$ of 2024–2025 data, LHCb measures $B_s \to \mu^+\mu^-$ to about 10% and reports 3.0σ evidence for the rarer $B^0$ mode; every central value sits within about 1.3σ of the Standard Model, and the effective lifetime does not yet test anything. arXiv:2611.00230, submitted to *Phys. Rev. X*.

## Key claims and results

- **Paper:** LHCb collaboration. arXiv:2611.00230v1 (30 Oct 2026), CERN-EP-2026-287. Preprint, so the analysis used an adversarial check. Internal LHCb review is not the same as a journal report.
- Rates: $B_s$ about 3.3 per billion, the most precise single-experiment measurement, about 1σ below the Standard Model value 3.66 per billion. $B^0$ about 1.3 per ten billion, versus 1.03 per ten billion, at **3.0σ** (3.2σ combined with older LHCb data). The ratio of the two rates agrees with the predicted 0.028, with an experimental uncertainty around 40% against a theory uncertainty around 6%.
- Effective lifetime of the $B_s$ mode: 1.42 ps in this dataset, 1.60 ps combined. The Standard Model heavy-state lifetime is about 1.62 ps. The uncertainty (about 1.8 alone) is larger than the whole physical range of the mixing asymmetry, from −1 to +1. Switching that assumption from +1 to −1 moves the $B_s$ rate by 9%.
- The software trigger does not require muon identification at the candidate stage, so signal and the two-hadron reference share a path. That is what the precision rests on. The dominant $B_s$ systematic uses a $B_s/B^0$ production ratio from a paper still in preparation. Misidentified hadrons set the $B^0$ systematic at about 4%.

## Physical intuition

These decays are rare because the Standard Model forces a loop, a spin mismatch, and, for $B^0$, a disfavored quark transition. A heavy new particle in the loop could move the rate without ever being produced. The upgraded detector’s job here is statistics and a shared trigger path, not a surprise. The lifetime is the second handle: new physics can leave the rate at the Standard Model value and still change which $B_s$ state decays. This measurement cannot see that yet.

## Limitations and assumptions

- Evidence, not observation. The rate is about 20% above the Standard Model, which helps the significance. A 2015 hint in this channel faded. CMS and ATLAS Run 3 results are not in yet.
- The two LHCb lifetime measurements differ by about 1.9σ. The combined central value should not be read as support for the heavy state.
- Minimal flavour violation needs a much sharper ratio.

## Connections

- Different LHCb muon-mode tension ($b \to s\mu\mu$ angular observables): [[b-meson-fcnc-anomaly]]
- Another flavor-precision program: [[baryon-semileptonic-polarization-entanglement]]
- Synthesis: [[nuclear-dense-matter-precision]] (flavor row, not the heavy-ion rows)

## Open questions

- Does more Run 3 data push $B^0$ to 5σ at the Standard Model rate, and does CMS agree?

## Source

- `raw/analyses/2026-11-08_arxiv-2611.00230_lhcb-b0-mumu-evidence-bs-mumu-run3.md`
