---
tags: [papers, heavy-ion, jet-quenching, oxygen, rhic]
last_updated: 2026-10-31
status: analysis-ingest
related_papers: [nuclear-dense-matter-precision, equilibrated-fraction-oo-qcd, alice-oo-nene-nuclear-geometry-flow, parton-jets]
source_analysis: "raw/analyses/2026-10-21_STAR-2026-OO-jet-quenching-2604.13935_star-oxygen-jet-quenching-rhic.md"
---

# STAR Oxygen–Oxygen Jet Quenching at RHIC

**One-line summary:** arXiv:2604.13935. In the busiest O+O collisions the away-side jet is ~20% less often seen than in quiet collisions; the trigger jet is unchanged. Energy pushed out is under 1 GeV, ~1/4 of Au+Au, above the p+Pb upper limit. Onset of jet quenching sits between p+A and O+O. Strong evidence, not yet an observation: depends on the no-quenching baseline.

## Key claims and results

- STAR Collaboration, arXiv:2604.13935v1 (15 Apr 2026; no journal reference in the analysis). 2021 RHIC oxygen–oxygen run. Per-trigger yields: one high-momentum charged hadron as trigger, partners counted per trigger so the uncertain number of hard scatterings cancels.
- Busiest tenth versus a mid-activity band (about 40–60%). Recoil hadron yield ~16% below the reference; wide-cone recoil jets ~19% below. Near-side yield consistent with no change at every activity level. Narrow and wide cones agree. The ratio versus jet momentum sits roughly flat near $0.75$–$0.8$ from ~8 to ~19 GeV.
- Five no-quenching baselines (Table I): exactly one gives $4.3\sigma$ (hadrons and wide-cone jets) and $3.5\sigma$ (narrow jets); the same-event near side gives $3.3\sigma$; three nuclear-parton-density calculations span $2.7$–$5.2\sigma$. The abstract's "strong evidence" matches that range. The title's "measurement" and the closing "has been observed" overshoot it.
- Spectrum shift that reproduces the deficit: $\Delta p \approx 0.70 \pm 0.18$ GeV/$c$ (wide) and ~0.8 GeV/$c$ (narrow), equal within errors — under 1 GeV pushed outside the cone. About a quarter of STAR's gold–gold wide-cone shift, and above ALICE's proton–lead ceiling. That ceiling was set at a different energy, cone, and jet momentum, so the ladder is suggestive, not a direct comparison.
- Nuclear-parton-density calculations (Gebhard, Mazeliauskas, Takacs) predict a ratio a few percent *above* one. Wrong sign for a cold-nuclear explanation. They compare minimum-bias oxygen with proton–proton, not busy oxygen with mid-activity oxygen.
- A hidden recoil-only, non-plasma suppression of ~5% (hadrons) or ~6% (wide jets) would drop the main channels below $3\sigma$. The near side, flat to ~3%, is the strongest defence against a bias that moves the whole hard process.

## Physical intuition

A hard scatter throws two sprays back to back. The near side is fragments of the trigger jet, which in a large droplet is born near the surface and crosses little plasma. The away side has to cross the droplet. In oxygen the droplet is only sixteen nucleons across, so the question is whether it is thick enough to matter. Counting partners per trigger sidesteps the geometric model that has swamped inclusive small-system searches. Busy events show the far-side partner about a fifth less often while the trigger's own side sits still. That pattern is energy lost on the long path, not a change in how often the hard scatter happens. The energy that leaves even the wide cone is under 1 GeV — a dent, not a quench of the gold–gold kind — which is why the onset sits between a proton hitting a nucleus (upper limits only) and two oxygen nuclei.

## Limitations and assumptions

- Not an observation. Significance is $2.7$–$5.2\sigma$ depending on the null. The most data-driven null, the near side, is $3.3\sigma$.
- The reference is mid-activity oxygen, which may already quench. The ~20% deficit is a difference between two oxygen populations, not an absolute loss against proton–proton. Absolute energy loss in the busiest events could be larger than ~0.7 GeV/$c$. This paper has no same-energy proton–proton jet reference.
- The no-quenching theory curves are not an apples-to-apples prediction for the measured ratio. They have no spatial dependence of the nuclear modification.
- Forward-activity selection at RHIC can bias the incoming parton momentum fractions (Park et al.). Correlations are less exposed than raw yields, but the paper does not simulate that bias. A recoil-only fake of ~5% is not excluded by anything except the near-side control, and the near side and the recoil do not sample the same momentum fraction.
- The momentum shift assumes the busy spectrum is a pure translation of the reference. Energy rearranged inside the cone is invisible. Cone-size independence says most of the lost energy went outside even the wide cone.
- "Trigger jet unchanged" is read from a near-side ratio of one. In this small a droplet the trigger may not be strongly surface-biased. A photon-triggered recoil would test that.
- Jets only span ~8–19 GeV, where background subtraction is hardest. Quoted event count and luminosity disagree by about a factor of three; per-trigger results do not use luminosity, so the physics claim is unaffected.

## Connections

- Synthesis (dense nuclear matter): [[nuclear-dense-matter-precision]]
- O+O core–corona equilibration: [[equilibrated-fraction-oo-qcd]]
- LHC oxygen/neon geometry and flow: [[alice-oo-nene-nuclear-geometry-flow]]
- Jet concept: [[parton-jets]]

## Source

- `raw/analyses/2026-10-21_STAR-2026-OO-jet-quenching-2604.13935_star-oxygen-jet-quenching-rhic.md`
