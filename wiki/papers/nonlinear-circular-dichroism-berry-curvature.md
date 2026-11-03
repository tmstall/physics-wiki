---
tags: [papers, berry-curvature, ultrafast, dichroism, 2d-materials]
last_updated: 2026-10-31
status: analysis-ingest
related_papers: [ultrafast-optics-and-solid-state-emitters, condensed-matter-topology-fractionalization, snte-light-topological-inversion]
source_analysis: "raw/analyses/2026-10-13_doi-10.1038-s41566-026-02025-8_nonlinear-circular-dichroism-local-berry-curvature.md"
---

# Nonlinear Circular Dichroism as a Handle on Berry Curvature

**One-line summary:** Nature Photonics DOI 10.1038/s41566-026-02025-8. A below-gap circular pump unravels valley cancellation for a few hundred fs; second-harmonic light comes out slightly twisted, and the twist scales with Berry curvature. Qualitative all-optical room-temperature protocol. The ~6 Å² number in WSe2 still depends on a model splitting and field calibration and sits below cited theory.

## Key claims and results

- Nature Photonics, doi:10.1038/s41566-026-02025-8 (accepted 4 Sep 2026, online 13 Oct 2026). Tornow, Herrmann, Schneider, Evers, Wilhelm, and Soavi. One monolayer of tungsten diselenide, room temperature, in air.
- When a single resonance dominates harmonic generation, the left–right imbalance of the emitted harmonic equals the Berry curvature at that momentum divided by the transition's dipole strength, at any harmonic order. A nonzero signal also needs two second-order response pieces to be out of phase, a requirement symmetry tables do not show.
- Monolayer WSe2 has two mirror valleys with opposite Berry curvature, so they cancel. A circular infrared pump, tuned below the gap so it is not absorbed, shifts one valley relative to the other (optical Stark and Bloch–Siegert) for the duration of the pulse, a few hundred femtoseconds.
- The probe's second harmonic then comes out a few percent handed. The handedness appears only while the pulses overlap, follows the pump's hand, vanishes for a linear pump, and grows linearly with pump power. Colour dependence is roughly the predicted resonance shape, including a sign change. The negative side rests on one point.
- The fit quotes about six square ångströms at the valley centre. The cited 2012 first-principles table lists roughly 9.4 and 16.8 square ångströms for WSe2. On the main text, the measured number sits below those values by more than its quoted error.
- The quoted uncertainty (about ±1.4) is fit scatter only. The extracted value scales as one over field squared. A 20–40% field uncertainty, not folded in, moves the number by a factor of about 1.5–2.
- The valley splitting that sets the absolute scale is not measured here. The paper uses about 10 meV "for typical conditions" from earlier work. Drop that model input and the experiment yields a ratio, not a curvature in absolute units.

## Physical intuition

Berry curvature is a twist in the electron's internal state as momentum changes. It acts like a magnetic field that lives in momentum space, and it is usually computed, not read out. In this crystal the two valleys are mirror images, so their twists cancel and the light comes out untwisted. A circular pump that never gets absorbed still shoves one valley's energy relative to the other, but only while the pulse is on. The cancellation lifts for a few hundred femtoseconds. Doubled-frequency light then prefers one hand by a few percent. How large that preference is tracks the twist. The shapes of the experiment (power, hand, timing, colour) test that story. The conversion of the preference into "six square ångströms" is where the model, not the photon counts, does the work.

## Limitations and assumptions

- Absolute scale inherits a pump-field calibration whose uncertainty is absent from the quoted error, and it inherits a predicted rather than measured valley splitting.
- The probe resonance is the A exciton, a bound electron–hole pair a few hundred meV below the free-particle gap. The formula is a two-band free-particle model. The number is an effective, exciton-dressed quantity. The main text does not treat excitonic corrections to the band Berry curvature.
- "Good agreement" with the cited DFT table is not supported by the numbers in that table. A supplement convention, gap choice, or local-field correction could close the gap. The analysis did not have the supplement.
- The resonance-shape fit uses seven points. Dephasing time and the curvature–time trade-off both depend on it. The sign-change point is about one standard deviation from zero.
- The method reports curvature at the one momentum where the probe is resonant, not a map. It needs well-separated resonances.
- One sample, one material, no temperature scan. The sharp untested checks are sister materials (MoS2, WS2, MoSe2) at matched detuning and an independently measured pump-induced splitting (transient reflectance) at the same field.
- Single group, building on its own earlier harmonic-generation work. Supplement Sections 1–5 were not in the analysis.

## Connections

- Synthesis: [[ultrafast-optics-and-solid-state-emitters]]
- Synthesis: [[condensed-matter-topology-fractionalization]]
- Light-driven topology in a related semiconductor: [[snte-light-topological-inversion]]

## Source

- `raw/analyses/2026-10-13_doi-10.1038-s41566-026-02025-8_nonlinear-circular-dichroism-local-berry-curvature.md`
