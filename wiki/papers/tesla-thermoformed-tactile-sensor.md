---
tags: [papers, patents, robotics, tactile-sensing, manufacturing, tesla]
last_updated: 2026-10-09
status: analysis-ingest
related_papers: [life2-telescope-array-biosignatures]
source_analysis: "raw/analyses/2026-10-08_tesla-patent-US20260310299A1_thermoformed-3d-tactile-sensor-robot-hand.md"
---

# Tesla Thermoformed 3D Tactile Sensor (US 2026/0310299 A1)

**One-line summary:** Tesla’s published application describes two manufacturing orders for a crossing-grid tactile array on curved plastic — print-flat-then-thermoform, or mould-first-then-print-on-the-curve — a recipe for making robot-skin parts, not a demonstration that a part works or that Optimus uses it.

## Key claims and results

- **Document:** US 2026/0310299 A1, *Three-Dimensional Soft Compliant Array Tactile Sensor with Multi-Modal Sensing and Scalable Manufacturing Methods.* Tesla, Inc. Inventors: Hung Sheng Lin, Nitin Sitaraman, Yi Quan Xiong et al. (12). Priority 4 Apr 2025 (prov. 63/783,580); filed 11 Sep 2025; published 8 Oct 2026. **Pending application, not a grant.** 20 claims; independents 1 (build flat, then form), 10 (form first, then build), 19 (thermoformed stack as apparatus).
- Sensing principle is textbook: two layers of conductor strips, soft separator, each crossing a taxel. Capacitive (squeeze raises C) or piezoresistive (squeeze drops R), chosen by separator. No taxel pitch, force range, sensitivity, or durability number appears. The only numeric definition in the document is “about” = ±10%, unused in claims.
- Route A (claims 1–9, 19–20): pattern conductors on thermoplastic sheets (TPU, PET, or polyimide; screen print or laser-cut channels filled with paste), laminate a separator, heat-form the sandwich over a fingertip-shaped mould.
- Route B (claims 10–18): mould the base first, then draw traces on the curve (dispense, laser-activate + plate, or pad print), dispense separator (optionally as dots at crossings), add a conforming second layer. Conductors never stretch.
- Claims do not mention a hand, robot, Optimus, or vehicle. The 3D target shape is unconstrained. Title’s “multi-modal” is capacitive *or* resistive (claim 20 “one of”), never two modes in one sensor. No throughput, yield, or cost.

## Physical intuition

A fingertip is a dome. A flat flex circuit wraps a cylinder and wrinkles on a sphere, because a sphere needs extra area near the rim. Thermoforming solves that the way in-mould electronics already put touch buttons on curved dashboards: heat the sheet above its glass transition so chains slide, stretch it over a mould, cool. The price is non-uniform stretch. Ink flakes separate; the separator thins most at the dome top; every taxel’s resting C or R shifts by more than a press does, so each cell needs its own zero.

Route B is the phone-antenna answer: never stretch the conductors, pattern them on the finished curve. Slower, serial, harder top-layer alignment.

The hinge for Route A is the separator’s two jobs. It must be heat-formable *and* soft enough that a fingertip-scale press changes C or R by a usable amount. A stiff thermoplastic film barely compresses next to silicone; the signal sits near noise unless the separator is a soft TPE or foam (mentioned as options, not specified).

## Limitations and assumptions

- No built device, no post-forming sensitivity, no grasp-cycle life, no cost. Examination state unknown (Patent Center not retrieved on publication day). Face lists no cited art.
- Prior art is thick: Apple US 2021/0089170 (thermoformed curved touch panel with pre-distorted electrodes); Sun Chemical thermoformable inks; Choi et al. 2021 KAIST fingertip-shaped capacitive film; Sakai et al. 2017 moulded fingertip transistor array; LDS / pad print / 3D dispense for Route B.
- Claim 19 requires the *stack* to be thermoformed, so Route B products arguably sit outside the only apparatus claim. “Isolated by the separator” sits awkwardly next to claim 20’s piezoresistive branch, which conducts between layers.
- Polyimide as a thermoformable substrate (claim 2) is questionable for common grades; TPU and PET are the routine choices. No grade named.
- FIG. 7’s uniform spacing is a hoped-for schematic, not a measured post-form stack.

## Connections

- Other Islands instrumentation / mission concept (different domain): [[life2-telescope-array-biosignatures]]
- No multi-paper robotics hub yet; stay on the Islands instrumentation shelf

## Open questions

- Does an examiner narrow claims 1 and 10 against Apple / KAIST / in-mould electronics?
- Force sensitivity after forming, with a named separator thickness and taxel pitch?
- Continuation that actually claims a hand, a cover, or two sensing modes together?

## Source

- `raw/analyses/2026-10-08_tesla-patent-US20260310299A1_thermoformed-3d-tactile-sensor-robot-hand.md`
