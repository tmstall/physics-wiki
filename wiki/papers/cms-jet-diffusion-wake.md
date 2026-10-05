---
tags: [papers, qcd, heavy-ions, quark-gluon-plasma, jets]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [tracking-baryon-number-nuclear-collisions, alice-oo-nene-nuclear-geometry-flow, equilibrated-fraction-oo-qcd, star-pt-correlations-qcd-critical, parton-jets]
source_analysis: "raw/analyses/2026-10-02_doi-10.1103-g49y-8cjl_cms-jet-diffusion-wake-dijets-heavy-ion.md"
---

# CMS Jet Diffusion Wake in Heavy-Ion Dijets

**One-line summary:** CMS reports a ~1% deficit of soft charged particles opposite a subleading jet in central lead–lead collisions, with the angular pattern a diffusion wake should have; five standard deviations say the dip is real, and the identification of that dip as the wake is still an inference. PRL 137, 071902 (2026), DOI 10.1103/g49y-8cjl.

## Key claims and results

- **Paper:** A. Hayrapetyan et al. (CMS Collaboration), “Observation of the Jet Diffusion Wake Using Dijets in Heavy-Ion Collisions,” Phys. Rev. Lett. 137, 071902 (2026). Editors’ Suggestion. Companion preprint arXiv:2602.19431. The geometry follows a theory proposal by Yang & Wang.
- Data: ²⁰⁸Pb–Pb at 5.02 TeV per nucleon pair (2018, 0.66 nb⁻¹) and pp at the same energy (2017) as the no-plasma reference. Centrality bins 0–30%, 30–50%, 50–80%.
- Dijets: anti-$k_T$ radius 0.4. Leading jet $p_T > 130$ GeV and $|\eta| < 1.0$. Subleading jet $p_T > 50$ GeV and $|\eta| < 2.0$. Azimuthal separation > 150°. Events are binned by the η gap between the two jets, from < 0.5 up to 1.5–2.0. The leading jet is defined as the one at higher η (the axis is flipped if needed), so the subleading jet always sits at negative Δη.
- Observable: charged tracks with 1–4 GeV, projected onto the near side of the leading jet. A difference of differences,

  $$W(\Delta\eta) = \big[R^{\mathrm{asym}} - R^{\mathrm{sym}}\big]_{\mathrm{PbPb}} - \big[R^{\mathrm{asym}} - R^{\mathrm{sym}}\big]_{\mathrm{pp}}$$

  Large-gap minus small-gap cancels structure shared by both dijet geometries. Subtracting the same procedure in pp cancels what a plasma-free collision does under that selection. The underlying event is measured in a near-side patch at positive Δη where no wake is expected.
- In 0–30% PbPb, 1–2 GeV tracks show a dip across roughly $-2.4 < \Delta\eta < -0.6$. It is weaker at 2–4 GeV, weaker in peripheral collisions (those agree with pp), absent in pp, and absent in PYTHIA8. Integrated over that window, the central 1–2 GeV points are more than 5σ from zero by a χ² test, for both large-gap selections. As the gap grows, the dip’s mean moves to more negative Δη, which is where a subleading-jet wake should go.
- The dip is about 1% of the local background (~0.25 particles per unit angle against a yield of order 35). Dominant systematic: residual underlying-event mismatch between large- and small-gap samples (0.01–0.04), about 5–15% of the central dip. Track-finding efficiency and pair acceptance are smaller. Jet energy scale and resolution cancel between the two geometries in the paper’s tests, so no correction is applied.
- Models with a medium response get the dip’s location. HYBRID overpredicts the 1–2 GeV depletion and predicts a much larger enhancement near Δη = 0 than the data show. CoLBT-hydro is closer on both sides but is shown for 0–10% centrality, not 0–30%, and model bands are statistical only.

## Physical intuition

A jet is a hard parton that has to cross the quark-gluon plasma. Quenching measures what the jet loses. Momentum conservation says that loss has to reappear in the medium. One response is a sonic boom (a Mach cone) wrapped around the jet, hard to see because it sits on the jet’s own fragments. The other is drag: the jet pulls fluid forward and leaves a thin deficit on the opposite side. That deficit is the diffusion wake.

The trick is geometric. Two jets can be back-to-back around the beam and still sit at different latitudes along it. The subleading jet’s wake then lands on the leading jet’s near side, but shifted in η, clear of the leading jet’s own peak. At small gap the wake hides under that peak. Subtracting the hidden case from the exposed case, then subtracting proton–proton, is how a 1% hole becomes visible.

A bus through a crowd is the everyday picture: people are pulled into the slipstream and a gap opens behind the bus. It breaks down because the plasma also supports a pressure wave, and the two responses can couple. The measurement is built to see the gap, not to separate that coupling cleanly.

## Limitations and assumptions

- Five standard deviations mean the depletion is not zero. They do not by themselves mean the cause is the diffusion wake. That step uses the pattern (centrality, soft particles, gap size and position) plus the claim that no other known mechanism makes this structure in the underlying event opposite the jet. Collective flow that differs between the two dijet samples is not fully killed by a pp reference. The no-medium Monte Carlo has a simplified underlying event.
- The small-gap sample is not wake-free. The wake is present and hidden, and the paper notes that jet-peak modifications interfere more at small gaps. The subtraction removes a mixture.
- The χ² recipe (bin correlations, how systematics enter) is not spelled out in the Letter. The analysis did not read a supplement or HEPData.
- Earlier searches disagree in strength. A CMS Z+jet analysis (same experiment, different channel) was a hint. ATLAS photon+jet saw nothing significant. An independent dijet repeat is the clean test, because a 1% signal is where analysis choices can imitate physics.
- No scan in jet $p_T$ or jet radius. Only 1–4 GeV charged particles and one near-side projection.

## Connections

- Where baryon number goes in the same fireball, a different question from where jet momentum goes: [[tracking-baryon-number-nuclear-collisions]]
- Light-ion geometry and how much of the collision is equilibrated: [[alice-oo-nene-nuclear-geometry-flow]], [[equilibrated-fraction-oo-qcd]]
- Soft correlations near a possible critical point, not a hard-probe wake: [[star-pt-correlations-qcd-critical]]
- Concept: [[parton-jets]]
- Synthesis: [[nuclear-dense-matter-precision]]

## Open questions

- Does ATLAS recover the same dip with the same η-gap geometry?
- Can a centrality-matched hydro-plus-jet model hit the ~1% depth without inventing the large near-zero enhancement HYBRID predicts?
- Do Z+hadron, photon+jet, and dijet wakes agree once they are written as one response, including the three-dimensional structure?

## Source

- `raw/analyses/2026-10-02_doi-10.1103-g49y-8cjl_cms-jet-diffusion-wake-dijets-heavy-ion.md`
