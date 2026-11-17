---
tags: [papers, aurora, magnetosphere, alfven-waves, optical-methods]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: []
source_analysis: "raw/analyses/2026-10-26_doi-10.1029-2026JA035658_alfvenic-modulation-quasi-static-potential-optical.md"
---

# Two Optical Rulers for an Auroral Voltage

**One-line summary:** On one 25-second auroral arc, two ground-camera estimates of the overhead electric field agree at 2–3.5 kV where a static U-shaped potential should hold, and disagree on the poleward edge in time with ~1 Hz pulsing; the motion ruler is seeded by the energy ruler, so the disagreement is the sturdier result. Brindley & Whiter, *JGR Space Physics* (2026).

## Key claims and results

- **Paper:** N. Brindley and D. Whiter. *Journal of Geophysical Research: Space Physics* **131**, e2026JA035658 (2026). DOI [10.1029/2026JA035658](https://doi.org/10.1029/2026JA035658). One event: 25 seconds on 28 February 2017, ASK imager on Svalbard, 20 frames per second, ~45 m pixels, an 11.5 km patch. The authors say about 0.5% of ASK data are usable for this.
- The arc is 3–6 km wide and drifts equatorward at about 200 m/s. Its sides counter-stream at median speeds near 10 km/s. That pattern is the textbook footprint of a U-shaped potential of a few kilovolts, somewhere between about 1,000 and 13,000 km up.
- Ruler one converts optical-flow speed to a field, $E \approx u B$, and keeps only the gradient part. Ruler two turns the 777.4 nm / 673 nm brightness ratio into a characteristic energy and takes the sideways slope. Flux conservation makes their ratio independent of altitude.
- Along a cut, both rulers give voltage drops of about **2–3.5 kV** for most of the interval, and the energy peak tracks the flow-reversal line. Within about 750 m poleward of that line, the two fields often point opposite ways. Those spikes line up with energy pulsing near **1 Hz**, the Alfvén-resonator band. The motion ruler reads low at the largest fields (flow speeds uncertain by 25–50%).
- A faint neighbor arc at 12.8–13.1 s is about half the size and half the energy of a spur in the main arc. A toy model says one wave could hit twice: near 1.4 Earth radii (~9,000 km) and near 0.5 Earth radii (~3,400 km), with energies close to twice the local wave speed (a bounce off a moving front) and a wave voltage of roughly 400–750 V. If the wave acts above the static drop, the drop’s base lands near 1,600 km. The model predicts a 1 km sideways split; the sky shows about 3 km.

## Physical intuition

In a static circuit, two paths around a loop must agree. A changing magnetic field is what lets them disagree. Here the two “voltmeters” are both made of light: how fast the curtain moves, and how the color ratio changes across it. Agreement says the accelerator is mostly a standing voltage. A poleward, flickering disagreement says something time-varying is shoving the energy peak off the flow-reversal line. Spacecraft catch an arc for a second. A camera can stare, and can tell a satellite when to look.

## Limitations and assumptions

- One arc. The method is a demonstration.
- The flow algorithm is seeded with the energy-ruler field and rewarded for shear. Agreement is partly built in. The poleward anti-alignment shows up anyway, which makes the disagreement more trustworthy than the agreement.
- “Energy” is one Maxwellian number per pixel from two colors. An Alfvén burst plus a static beam would be averaged together.
- The single-wave story needs a fixed wave width. If the wave narrows as field lines converge, it fails, and a two-wave picture fits better. Altitudes move by several tenths of an Earth radius if the size ratio is 2.5 instead of 2.
- A steady mixed U/S potential can also shift the energy peak. The intermittent 1 Hz timing argues for a wave, and it does not rule a static asymmetry out.
- Staged copy note: the queue recorded figure files `brindley-035658_fig4`, `fig5`, `fig7`, and `analyst-ushape` as missing. The claims above follow the analysis text, which describes those figures.

## Connections

- No multi-paper auroral hub yet. This page stays on the Islands shelf until a second ground-based or in-situ arc paper shares the question.
- Lab laser–plasma pages ([[plasma-hed-lab]]) are a different regime. Do not fold this event into that map.

## Open questions

- Do other counter-streaming ASK arcs show the same poleward-only, ~1 Hz disagreement?
- Does a satellite on the same field line, during a disagreement spike, see broadband Alfvénic electrons within a kilometre of the flow reversal?

## Source

- `raw/analyses/2026-10-26_doi-10.1029-2026JA035658_alfvenic-modulation-quasi-static-potential-optical.md`
