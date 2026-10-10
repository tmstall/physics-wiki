---
tags: [papers, planetary-science, solar-system, pebble-accretion, volatiles]
last_updated: 2026-10-09
status: analysis-ingest
related_papers: [chondrite-pressure-bump, ch3oh-hcn-3i-atlas-outgassing, gw-ori-streamer-misalignment]
source_analysis: "raw/analyses/2026-10-05_doi-10.1038-s41550-026-02984-6_volatile-depletion-hybrid-accretion-earth-mars.md"
---

# Volatile Depletion as a Fingerprint of Hybrid Accretion

**One-line summary:** Earth’s and Mars’s missing sodium, potassium and zinc are read as a mix of two building-block types: pebble-grown bodies that lost volatiles in a hot H/He envelope, plus already-dried planetesimals; Earth is mostly pebbles, Mars is mostly planetesimals. Wang et al., *Nature Astronomy* (2026), DOI 10.1038/s41550-026-02984-6.

## Key claims and results

- **Paper:** Wang, Johansen, Xu, Steinmeyer, Lambrechts, van Kooten, Yang, Zhu, Lauretta & Bizzarro. *Nature Astronomy*, published 25 Sep 2026. Open access. Modelling plus Bayesian mixture fit to existing mantle abundances (13 elements); no new measurements.
- Two depletion shapes: Earth and Mars slope down gently from ~1,400 K sublimation temperature (Earth more depleted); Vesta (HED meteorites) is a cliff near 1,135 K. Ryugu and Bennu sit undepleted on the solar line.
- New pebble channel: a protoplanet bigger than roughly the Moon holds a H/He envelope whose base heats as mass grows. A pebble falling through loses every moderately volatile element whose sublimation temperature sits below that base; convection dumps the vapour back to the disk. A SiO cloud lid seals Mg and Si once the base hits ~1,400 K. 3D tracers in an Earth-mass envelope: ~3% remain after five years.
- Earth fit (reference): ~64% proto-Earth + ~22% impactor + ~14% Vesta-like planetesimals, so ≳75% from pebble-grown bodies. Dropping planetesimals fits equally well (“up to ~25%”). Dropping the impactor costs only ~3.7:1 evidence. Impactor mass is almost unconstrained (flat over ~8–43% of Earth).
- Mars fit (reference): ~27% pebble-grown + ~73% planetesimals. The paper’s own evidence prefers a hotter planetesimal cut-off (~1,363 K, no known meteorite) at ~13:1, moving the split to ~21% pebbles (10–30%). Across variants, pebbles ≳10% and planetesimals ≳65%.
- Held-out sulfur (mostly in the core) lands in recent, higher Earth-core and seismic Mars-core ranges.

## Physical intuition

A growing pebble planet is a storage system whose ingest buffer runs hotter as volume grows. Each chemical “field” has a heat tolerance. Once the buffer passes that temperature, later records lose the field; records already written keep it. Refractory core fields go through a protected path (the silicate lid) and never strip. The retained fraction of a moderately volatile element is then (mass at crossing) / (final mass), which is a *gentle slope* because different elements cross at different masses.

Vesta-like planetesimals are a one-shot hot reboot: everything below a fixed cut-off is flushed. Mix the two signatures and you can reproduce a gentle Earth slope plus a Mars curve that still needs a cliff ingredient.

This answers one pebble-accretion objection (Morbidelli, Kleine & Nimmo): pebbles need not give a single step. They give a family of steps at different masses, which looks gradual after mixing.

## Limitations and assumptions

- The “fingerprint” is a fitted mixture, not a unique measured signature. The only pure-planetesimal rival tested has *fixed* Vesta + CI curves. Freeing the planetesimal cut-off improves both planets a lot; an equally flexible non-pebble rival was not run. “Hybrid is required” is shown against a stiff rival.
- Earth hangs on 100% loss once the envelope crosses an element’s threshold. If recondensation returned even ~1/3 of stripped Na/K, pebble bodies would be too volatile-rich and the fit would need more planetesimals. 3D tracers support fast clearing but use passive particles, one planet mass, and a prescribed escape boundary.
- Mars “27 ± 5%” in the abstract is the *disfavoured* Vesta-fixed model. Quote the wider 10–37% pebble range. Lithium is a ~3σ miss for the reference Mars mix and drives most of the residual.
- Mg/Si sit somewhat below 1 in Earth’s data; the model’s 1,400 K lid puts them at 1, which is the worst Earth mismatch.
- Independent Olson, Sharp & Garai work (arXiv:2601.08958) also likes a depleted ~0.7 $M_E$ target plus less-depleted impactors — convergence inside the pebble school, not a planetesimal-tradition reanalysis.

## Connections

- Disk pebble traps / chondrite chemistry (same solar nebula, different question): [[chondrite-pressure-bump]]
- Circumtriple disk still being fed: [[gw-ori-streamer-misalignment]]
- Volatile inventory in a small body (comet, not planet): [[ch3oh-hcn-3i-atlas-outgassing]]
- Islands planetary shelf; no synthesis hub yet (graduation candidate with Enceladus + chondrites)

## Open questions

- Does a free-curve planetesimal-only mix fit Earth and Mars as well as the hybrid?
- Core sulfur in the predicted windows, from an independent geophysics group?
- White-dwarf pollution and “planet-eating” stars: do their moderately-volatile slopes split Earth-like vs Mars-like?

## Source

- `raw/analyses/2026-10-05_doi-10.1038-s41550-026-02984-6_volatile-depletion-hybrid-accretion-earth-mars.md`
