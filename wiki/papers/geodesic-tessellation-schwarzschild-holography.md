---
tags: [papers, black-holes, holography, geodesics, entropy]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [entropic-information-gravity, qg-deep-dive-2-info-holography, qg-deep-dive-3-holographic-codes, black-hole-thermodynamics]
source_analysis: "raw/analyses/2026-09-28_arxiv-2609.21471_geodesic-tessellation-schwarzschild-holography.md; raw/analyses/2026-09-29_arxiv-2609.21471_geodesic-tessellation-schwarzschild-holography-v2-foundations.md"
---

# Geodesic Tessellation of Schwarzschild (Holography Foundations)

**One-line summary:** Same arXiv:2609.21471, two analyses (application + foundations). Lambertian geodesic spray from a surrounding sphere fills space uniformly so crossing counts measure area (curved-space white-furnace / 70-year theorem). At 10 $r_s$ only ~1% of rays hit the horizon yet they encode its area; wormhole: one side sees only to the throat. Assigning $1/4G$ per ray recovers BH entropy by calibration, not derivation; simplest network undercounts light-bending by more than one BH entropy.

## Key claims and results

- One paper, arXiv:2609.21471v1 (hep-th, 18 Sep 2026, 33 pp.), read twice: an application pass and a foundations rewrite. Both agree on the split below. The threads are spatial geodesics of the $t = 0$ Schwarzschild slice, not light rays.
- Launch from an outer sphere with cosine (Lambertian) weight, and count returning chords once. Areal radius along a geodesic has only minima, so every chord touches the outer sphere and one source is complete.
- The gas is uniform and isotropic down to the horizon, independent of the detailed radial function. Crossing count divided by $\pi$ equals the area of any surface (Crofton). An analyst Monte Carlo of $2 \times 10^6$ samples at ten horizon radii matches $\pi \times$ area to 0.01%.
- That transport is Santaló’s 1952 formula, which the paper does not name. The new bookkeeping is the one-sided source and the bridge sector split, not the symplectic proof.
- At ten horizon radii only $(r_h / R_+)^2 = 1\%$ of the source weight reaches the horizon, and that slice equals $\pi$ times the horizon area. On the Einstein–Rosen bridge a one-sided source reconstructs only to the throat. The far side needs its own source; the two gases share the crossing sector.
- Assign $1/(4G)$ to each thread by hand and the network reprints Bekenstein–Hawking entropy, an RT formula on the outer sphere, and left–right entropy as ER=EPR. The body calls the dual a hypothesis and does not name a theory on the sphere. The abstract is stronger. No boundary state produces the measure.
- The factorized (point-to-point) network fails here. Spatial geodesics bend toward the hole and sweep more than $\pi$, so some same-side threads cross a totally geodesic cut twice. At ten horizon radii the hemisphere count sits ~6% below area$/4G$, a shortfall of about $1.7$ horizon areas — more than one black-hole entropy — and the absolute gap grows as the sphere moves out. The random-tensor min-cut still counts repeats, so that fallback survives. A hemisphere’s RT entropy is volume-law ($\sim 2500$ times $S_{\rm BH}$ at $100$ horizon radii).

## Physical intuition

Think of a white-furnace test: a matte glowing enclosure should look equally bright in every direction if radiance is conserved along bent rays. Here the “light” is a gas of spatial geodesics. A uniform gas means area is a crossing count. The wormhole throat is a bottleneck — only steep aims get through, and one side’s furnace cannot illuminate past it. Stamping $1/4G$ on each ray reprints the area law. It does not derive entropy.

## Limitations and assumptions

- The geometric core is Santaló (1952) on a non-trapping region. The authors argue that the black-hole assembly is the novelty. Whether that clears the bar is contested.
- $1/4G$ per thread is chosen to match the RT formula. Geometry fixes the measure, the measure fixes the network, and the network returns the areas it was given.
- The factorized shortfall is analyst work (equatorial disk plus the northern half-horizon as the cut). Bending past a half-turn is solid. The exact 6% and $1.7$ horizon-area figures are the soft part. Both analyses agree on the direction and on a miss larger than one black-hole entropy. Do not read the miss as photon-sphere trapping: these are frozen-space geodesics.
- Static, time-symmetric slices only. No HRT or Lorentzian measure. The continuum random-tensor step is an identification, not a finite-graph proof. The construction never uses Einstein’s equations, so it cannot tell a matter-supported metric from an arbitrary non-trapping one.
- A dual on a large outer sphere would have volume-law entanglement (Li & Takayanagi 2011, cited but not engaged). Bit threads and non-vacuum kinematic space already cover related ground.

## Connections

- Entropic and information-theoretic routes to Einstein: [[entropic-information-gravity]]
- From the information paradox to holography: [[qg-deep-dive-2-info-holography]]
- Holographic codes and bulk reconstruction: [[qg-deep-dive-3-holographic-codes]]
- Area-law thermodynamics the calibration targets: [[black-hole-thermodynamics]]

## Source

- `raw/analyses/2026-09-28_arxiv-2609.21471_geodesic-tessellation-schwarzschild-holography.md`
- `raw/analyses/2026-09-29_arxiv-2609.21471_geodesic-tessellation-schwarzschild-holography-v2-foundations.md`
