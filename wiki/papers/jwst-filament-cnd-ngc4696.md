---
tags: [papers, black-holes, agn-feedback, jwst, galaxy-clusters]
last_updated: 2026-08-02
status: analysis-ingest
related_papers: [ultramassive-bh-binary-cavity, smbh-inclination-angle, mrk501-double-jet-smbbh, high-z-quasar-pair-merger, dr21-magnetic-accretion]
source_analysis: "claude_export/extracted-analyses/2026-07-19_watching-a-black-hole-set-the-table-a-filament-caught-feedin_2745e811.md"
---

# JWST Filament → Circumnuclear Disk Feeding in NGC 4696

**One-line summary:** JWST/NIRSpec resolves, at ~10 pc scales in the Centaurus BCG NGC 4696, the kinematic handoff where a cooling filament dumps ionized gas into a rotating circumnuclear disk — the missing conveyor belt from kiloparsec cooling flows to sub-100 pc black-hole fueling.

## Key claims and results

- **Object:** NGC 4696 (Centaurus cluster BCG, $z\approx0.01$); ApJL-style Letter with companion MHD simulation (analysis framing: Hlavacek-Larrondo PI dataset).
- Long-standing gap in cold-mode AGN feedback: precipitation predicts cold clouds rain in, but angular momentum should circularize gas far out. Need resolved maps of low-angular-momentum delivery into a circumnuclear disk (CND).
- NIRSpec IFU (Pa$\alpha$ tracer) at ~10 pc sampling over a ~600 pc field turns the HST S-shaped swirl into a **rotating CND** (radius ~120 pc) with ~600 km/s east–west velocity swing, plus a western **ionized filament** ($\gtrsim$350 pc long) kinematically linked at the interface.
- Turbulence proxy $w_{80}$ peaks near the AGN/jet hotspot (~1700 km/s) and bumps at the filament–disk junction (~300 km/s) — disruption where accretion is active.
- Inflow interpretation (by elimination + PV linkage, following the NGC 1275 playbook): filament ⊥ radio jet (not a jet-driven outflow); PV continuity at the interface; disordered kinematics at the disk edge.
- AthenaK 3D MHD sims tailored to the system: magnetic **tethers** (Maxwell stresses) torque angular momentum from descending cool gas so filaments feed a magnetized CND; multi-direction feeding can wobble the disk and reorient jets.
- Second clear case after NGC 1275 — consolidates cold-feedback pattern rather than a one-off.
- Important honesty checks in analysis: $M_{\rm BH}$ still from scaling relations (not a clean dynamical CND mass yet); sims are co-author / system-tuned consistency checks; observed multiphase CND is hotter/stratified than some cold-sim CNDs; inflow is inferred, not a direct 3D velocity vector.

## Physical intuition

Cluster cores should cool and dump gas onto the central black hole; jets reheat the atmosphere and close a feedback loop. The missing movie frame was the last few hundred parsecs: how does raining multiphase gas shed spin so it can fall in? Picture a cargo drone on a magnetic towline. As the cool blob falls, frozen-in field lines stretch behind it; magnetic tension acts like regenerative braking on the tangential motion, so the blob spirals in instead of parking on a huge stable orbit. JWST finally sees the staging buffer — a spinning circumnuclear disk — and the pipe that feeds it, with matching velocity where they join. The black hole’s dinner table is set by weather (cooling, turbulence) and wiring (magnetic stress), not by a smooth hot Bondi straw alone.

## Limitations and assumptions

- Analysis-based ingest; verify kinematics and sim parameters against the ApJL + companion papers.
- Single object, single reduction team; figure interpretation via captions in the export analysis.
- Line-of-sight velocities + single-Gaussian Pa$\alpha$ fits; projection degeneracies remain.
- Sphere of influence ~70 pc straddles the CND — dynamical BH mass still pending dedicated modeling.
- Sim–data agreement is designed consistency, not a blind independent prediction.
- Multiphase thermal structure not fully matched by the cold-dominated simulated CND.

## Connections

- SMBH / AGN cluster: [[ultramassive-bh-binary-cavity]], [[smbh-inclination-angle]], [[mrk501-double-jet-smbbh]], [[high-z-quasar-pair-merger]], [[bh-recoils-agn-survey]]
- Extreme outflow / feedback counterpart: [[category-79-quasar-wind]]
- High-$z$ Lyα filament twin (IGM scale): [[muse-quasar-filament-z3]]
- Magnetic guidance of accretion (different scale): [[dr21-magnetic-accretion]]
- Concepts: [[supermassive-black-hole-binaries]] (feedback/environment neighbors), [[dynamical-friction]]
- Key terms: precipitation / cold-mode accretion, angular-momentum problem, circumnuclear disk (CND), magnetic tether / Maxwell stress, IFU / Pa$\alpha$, $w_{80}$, sphere of influence, NGC 4696 / Centaurus

## Open questions

- How common is filament→CND handoff across BCGs with JWST IFU?
- Can multiline (H$_2$, CO, X-ray) joint modeling close the multiphase mass budget?
- Does disk wobble from multi-direction feeding explain wide-angle jet heating?

- Synthesis: [[black-hole-feedback-and-changing-look-agn]] (feedback / changing-look ladder)

## Source

- `claude_export/extracted-analyses/2026-07-19_watching-a-black-hole-set-the-table-a-filament-caught-feedin_2745e811.md`
