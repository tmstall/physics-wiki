---
tags: [papers, soft-matter, photopolymerization, fibers]
last_updated: 2026-10-31
status: analysis-ingest
related_papers: [chemistry-biotech-methods]
source_analysis: "raw/analyses/2026-10-11_doi-10.1103-yh2j-b3wq_gravity-stretched-jet-light-solidified-fibers.md"
---

# Gravity-Stretched, Light-Solidified Fibers

**One-line summary:** PRL DOI 10.1103/yh2j-b3wq. A falling resin jet frozen by light: the weight of the already-solid fiber, not the chemistry, sets the final thickness. Freeze distance is a stopwatch for the photochemistry. A race with droplet breakup decides smooth fiber vs beads, and can be called in advance.

## Key claims and results

- PRL 137, 144004 (2 Oct 2026), Editors' Suggestion. Smink, Visser, and Lhuissier. A light-curable resin jet falls freely into a water bath. Ultraviolet LEDs just under the nozzle start a chain reaction. A few centimetres down, the liquid locks into a thinner, solid-like fiber.
- Brightness moves the freezing point without changing the flow. That splits chemistry (when the liquid freezes) from mechanics (what freezing does to the thread).
- A textbook polymerization model, radicals made only in the light and then annihilating in pairs, collapses the delay data onto one curve with two fitted constants. Delays are tens of milliseconds. The front is about a millimetre long.
- A momentum balance at that front predicts the final width with no fitted knobs. The hanging solid's weight pulls slow liquid into fast solid. Width matches across nozzle speeds, fall distances, and freezing positions, and barely cares where the front sits. From 14 cm to 39 cm of fall the thread comes out about a fifth thinner.
- The same balance, with a growing hanging mass, predicts the first half-second after switch-on, including a fiber that accelerates at half of gravity until it lands, and the taper of short fibers from a pulsed lamp.
- With the light off, the jet breaks into drops. The beads-versus-fiber boundary sits where the freezing distance equals the breakup distance. The map calls the winner before the run.
- "Parameter-free" means no fitted width knobs. It still assumes a sharp front, negligible air drag, negligible density change, a bath that carries the landed fiber, and the falling-stream model for the liquid above the front.

## Physical intuition

Force-driven spinning usually tangles the recipe with the pull. Stretch the liquid harder and it hardens somewhere else, which changes the stretch. Here the lamp is a switch with a known place. Once the front is sharp, chemistry only chooses where the stop-line sits. Below that line the fiber is already solid, so its weight is a known load on the liquid still coming through. Volume in per second is fixed by the pump. Faster solid means a thinner solid. The distance to the front is also a clock: the jet's speed is known, so "froze 3 cm down" means "the reaction took this many milliseconds." Smooth fiber versus a string of beads is a race between that clock and the capillary breakup clock.

## Limitations and assumptions

- Air drag is about a percent of the weight in this setup and grows with speed squared. Electrospinning and blow-spinning sit outside the model.
- Only sharp, complete solidification is treated. Melt cooling, solvent evaporation, and most electrospinning put the chemistry–flow coupling back in.
- The propagation rate scales with an assumed one-percent freezing threshold. Agreement with a literature rate is partly built in, not an independent measurement.
- Uniform absorption, no oxygen inhibition, and nearly constant temperature are justified for these thin, degassed jets (heating under a degree). Thicker or strongly absorbing resins would reopen them. Those estimates lean on an unread supplement.
- The model tracks average thinning. Fast capillary ripples are not thinned in proportion. The front damps them.
- Breakup distance comes from a simplified, light-off calibration. Breakup is noise-driven, so the boundary shifts with nozzle quality.
- One resin, one rig, one group. A core–shell alginate check lives in the unread supplement. The reaction-stopwatch idea is demonstrated at tens of milliseconds, not yet as a sub-millisecond kinetics tool. Faster, thinner jets bring drag and heating back.

## Connections

- Synthesis: [[chemistry-biotech-methods]]

## Source

- `raw/analyses/2026-10-11_doi-10.1103-yh2j-b3wq_gravity-stretched-jet-light-solidified-fibers.md`
