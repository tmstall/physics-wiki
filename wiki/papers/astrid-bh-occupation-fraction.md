---
tags: [papers, black-holes, galaxies, simulations, astrid, dwarfs]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [astrid-z0-mbh-lss, direct-bh-mass-lrd-abell2744, early-universe-popiii-flash-ionization, dynamical-friction, glimpse-17775-cocoon]
source_analysis: "raw/analyses/2026-10-03_arxiv-2607.09853_black-hole-occupation-fraction-fossil-record.md"
---

# ASTRID Black-Hole Occupation Fraction

**One-line summary:** In ASTRID, “does this galaxy have a black hole?” splits into three different numbers: nearly every dwarf owns one somewhere, only about half of the smallest keep it in the stellar half-mass radius, and only a few percent are feeding hard enough for an AGN survey to see. ApJL 1008, L54 (2026), DOI 10.3847/2041-8213/ae9c38.

## Key claims and results

- **Paper:** Weller, Natarajan & Burke, ApJ Letters 1008, L54 (2026). arXiv:2607.09853. They do not run a new simulation. They slice the existing ASTRID catalog (the same $250\,h^{-1}$ Mpc box as [[astrid-z0-mbh-lss]]) at z = 5, 4, 3, 2, 1, and 0, for galaxies from 10⁷ to 10¹² M☉ in stars.
- ASTRID seeds one black hole per friends-of-friends halo above ~7×10⁹ M☉ that does not already have one, once the halo has a few million solar masses in stars. Seed masses are drawn at random from about 4.4×10⁴ to 4.4×10⁵ M☉. Holes drift under a subgrid dynamical-friction force. They are not pinned to the potential minimum. They merge when closer than about twice the softening (~4.4 kpc at z = 0) and bound. No gravitational-wave recoil and no three-body slingshots.
- **Total occupation** stays above ~0.92 at every mass and redshift in the sample. At z = 0 below 10⁸ M☉, 92% of galaxies have exactly one black hole, 7% have none, and 1% have more. That near-unity floor restates the seeding rule. It is not a prediction that real dwarfs are all occupied. The z = 0 report card already flagged a seed excess ([[astrid-z0-mbh-lss]]).
- **Location is the interesting split.** “Central” means inside the stellar half-mass radius. At 10⁷ M☉ the central fraction falls from ~0.75 at z = 5 to ~0.48 at z = 0, and the wandering fraction rises from ~0.19 to ~0.44. With one hole per dwarf, those two moves are the same hole. Above ~10¹⁰ M☉ both fractions saturate near 1, because giants have a central hole and a retinue of wanderers. A z = 0 bump near 10^7.5 M☉ (more wanderers, fewer centrals) is flagged by the authors as unexplained.
- **Active** means Eddington ratio above 0.01. At z ≥ 2, active occupation climbs toward 1 in massive galaxies. At z = 0 it never exceeds ~0.16 (near 10¹⁰ M☉) and is ~0.02 at 10⁷ M☉. An AGN-selected census at z = 0 would call most occupied galaxies empty. Wandering holes are rarely active (≤ 0.1): they sit in thin gas.
- **Heavy-seed tag** means the seed, or any swallowed progenitor’s seed, exceeded 10⁵ M☉. The low-mass floor sits near 0.35 at every redshift. Because every ASTRID seed is already “heavy” by the usual 10⁴–10⁶ M☉ language, and the draw does not depend on the host, this tag is the upper part of one distribution, not a second formation channel. A random-lineage count reproduces the floor and the rise with mass. The paper cannot test light seeds.
- Host split at z = 0: primaries are nearly fully occupied; star-forming satellites fall to ~0.6 at 10⁷ M☉. Star-forming primaries at that mass have central occupation ~0.18 and wandering ~0.80; quiescent primaries sit near 0.50 / 0.50. The authors report a correlation and do not claim that a central hole is what quenches the dwarf.
- Compared with Zou et al. (2025) X-ray central occupation (about 93% at 10¹¹–10¹² M☉, ~66% at 10⁹–10¹⁰, ~33% at 10⁸–10⁹), ASTRID’s z = 0 **central** curve lies inside the 3σ band, near the upper 2σ edge at 10^7.5–10^8.5 M☉. The total curve does not. Other codes (Haidar et al. 2022) span nearly 0 to nearly 1 at 10⁹ M☉, mostly because their seeding rules differ, and several of them force “central” by repositioning.

## Physical intuition

A dwarf is a shallow parking lot. Mergers deliver black holes on wide orbits. Dynamical friction is the tow truck. In a deep galaxy the tow finishes. In a dwarf it often does not, so the hole is still in the outskirts at z = 0. Count the lot and the galaxy looks occupied. Count only the reserved space at the center and it looks empty. Count only the engines that are running (AGN) and almost nobody is home.

The title’s “fossil of seeding” is the question the field wants. This simulation has one heavy-seed channel, so the fossil it actually keeps is of **dynamics and duty cycle**. Matching an X-ray “central” fraction to a half-mass-radius cut, or an AGN fraction to a total occupation, compares different quantities.

## Limitations and assumptions

- No light seeds. The introduction’s light-versus-heavy test is not available inside ASTRID. Minimum seed ~3×10⁴ h⁻¹ M☉.
- At z = 0 the softening is 2.2 kpc and the merger radius ~4.4 kpc. A 10⁷ M☉ dwarf has ~20 star particles, so the half-mass boundary is at the resolution scale. Physical softening grows about sixfold from z = 5 to z = 0, which is the same direction as the central-fraction decline. No convergence test is shown. The unexplained bump sits in this regime.
- Satellite under-occupation is partly the seeding rule: a subhalo inside an already-seeded group never gets its own seed.
- Missing recoil and three-body kicks would likely make still more wanderers.
- “Central” in an X-ray nuclear search is often ~100 pc, not a half-mass radius of kiloparsecs. ASTRID’s central fraction can be an upper bound on what that search would count. The authors ask for forward-modelled, selection-matched fractions.
- The printed seed-mass formula (probability rising with mass) does not reproduce the ~37% heavy-seed floor. A steeper draw does. The implementation and the equation may not match. It does not change the “one channel” conclusion.
- Star formation versus location: stellar feedback can shove holes outward, or a noisy stellar centroid can move the boundary. The causal arrow is open.

## Connections

- Same box, z = 0 report card (mass function, wandering bias, seed excess): [[astrid-z0-mbh-lss]]
- Drag that fails to finish in dwarfs: [[dynamical-friction]]
- A single high-z dynamical mass, not a dwarf census: [[direct-bh-mass-lrd-abell2744]]
- Heavy seeds from a Pop III.1 flash, a different channel this simulation does not contain: [[early-universe-popiii-flash-ionization]]
- Synthesis: [[black-hole-feedback-and-changing-look-agn]] (census rung), [[cosmology-expansion-history-and-structure]]

## Open questions

- Does the central/wandering split at 10⁷–10⁸ M☉ survive a zoom with a half-mass radius well above the softening?
- Do nuclear X-ray or radio searches find fewer black holes in star-forming dwarfs than in quiescent dwarfs of the same mass, after correcting for who is actually accreting?
- What does the same matrix look like in a live-dynamics code that also has light seeds?

## Source

- `raw/analyses/2026-10-03_arxiv-2607.09853_black-hole-occupation-fraction-fossil-record.md`
