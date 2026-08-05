---
tags: [papers, cosmic-rays, high-energy-astrophysics]
last_updated: 2026-08-02
status: analysis-ingest
related_papers: [beyond-iron-ultraheavy-cosmic-rays, aquila-booster-pevatron]
source_analysis: "claude_export/extracted-analyses/2026-05-02_peters-cycle-confirmed-charge-dependent-cosmic-ray-spectral_a9c50c9b.md"
---

# Peters Cycle Confirmed: Charge-Dependent Softening Below the Knee

**One-line summary:** DAMPE measures primary cosmic-ray spectra from proton through iron and finds spectral softenings that line up at a common rigidity (~15 TV), confirming Peters’s 1961 charge-dependent acceleration limit and pointing to a nearby magnetic accelerator contributing to the local flux.

## Key claims and results

- **Paper framing:** Nature / arXiv:2511.05409 — charge-dependent spectral softenings of primary cosmic rays below the knee (DAMPE collaboration analysis).
- Direct space measurements of C, O, Fe (plus p, He context) over roughly tens of GV to multi-TV rigidity with nine years of data.
- All five species show a spectral **softening near $R_{\rm break}\approx15$ TV** — i.e. break energy scales with charge $Z$, not mass $A$. Mass-dependent softenig rejected at very high confidence in the analysis framing.
- Earlier **hardening** near ~600 GV (light species) also roughly rigidity-aligned; interpreted as propagation or second-component physics, separate from the 15 TV feature.
- Combined with large-scale anisotropy, the picture favors a **nearby source** whose magnetic ceiling imprints both the multi-species kink and directional excess.
- First clean, multi-species direct verification of the Peters cycle below the knee (not air-shower species inference alone).

## Physical intuition

Magnetic accelerators (supernova shocks, etc.) care about how hard it is to bend a particle — **rigidity** $p/Z$ — not how many neutrons it carries. Peters argued each nucleus should hit the same voltage ceiling at energy $E_{\max}=Z\,R_{\max}$. DAMPE’s calorimeter + tracker can tag charge and reconstruct rigidity species-by-species from orbit. Plot the flux cliffs in energy: iron’s cliff sits ~26× higher than the proton’s. Replot in rigidity: the cliffs stack. That is a railgun that stops at a fixed voltage, not a mass-dependent speed bump.

## Limitations and assumptions

- Analysis-based ingest; confirm break rigidities, significances (esp. iron ~2.7σ in the analysis framing), and anisotropy joint fit against primary paper.
- “Nearby source” is still unidentified (Vela / Geminga / Monogem-class candidates).
- Softening is a **sub-knee** Peters feature; the PeV knee itself may involve a different source population.
- Hardening at ~600 GV needs a separate or extended model.
- Secondary-to-primary ratios at TV rigidities would further separate acceleration limits from propagation.

## Connections

- Composition / extreme end: [[beyond-iron-ultraheavy-cosmic-rays]]
- Galactic PeV accelerators: [[aquila-booster-pevatron]], [[pulsar-wind-nebulae]]
- Key terms: rigidity, Peters cycle, DAMPE, spectral knee, smoothly broken power law, dipole anisotropy, DSA

## Source

- `claude_export/extracted-analyses/2026-05-02_peters-cycle-confirmed-charge-dependent-cosmic-ray-spectral_a9c50c9b.md`
