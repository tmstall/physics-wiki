---
tags: [papers, pulsars, neutron-stars, gravitational-waves, general-relativity]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [psr-j1906-binary-timing, rapid-orbital-decay-erassu-j060839, neutrino-flavor-failed-supernovae, gw170817-jet-hubble, color-superconductivity-qcd]
source_analysis: "raw/analyses/2026-10-03_arxiv-2607.27333_psr-j1856-0039-lightest-double-neutron-star.md"
---

# PSR J1856−0039: Lightest Double Neutron Star

**One-line summary:** Five years of FAST timing give PSR J1856−0039 a total mass of 2.48841 M☉, the lightest precisely weighed double neutron star, with orbital decay matching general relativity at the 1.4% level. The individual masses are only known to about 2%. PRL 137, 121401 (2026), DOI 10.1103/hmjp-htd1.

## Key claims and results

- **Paper:** Yang et al., Phys. Rev. Lett. 137, 121401 (2026). arXiv:2607.27333. Fifth double neutron star from FAST’s Galactic Plane Pulsar Snapshot survey.
- The pulsar spins every 23.4 ms (about 43 Hz). Orbital period 2.36 hours, eccentricity 0.106. About 21 hours on source across 17 sessions and five years. Arrival-time residuals ~6 µs. Three post-Keplerian parameters: periastron advance $\dot{\omega} \approx 17.6$ deg/yr, Einstein delay γ ≈ 0.445 ms, and orbital decay.
- Assuming general relativity, $\dot{\omega}$ fixes the total mass at **2.48841 ± 0.00015 M☉**. γ splits it into a pulsar of about 1.304 M☉ and a companion of about 1.185 M☉, each ±0.022 M☉. The two errors match because the masses are almost perfectly anti-correlated: the total is fixed, and mass moved off one star lands on the other. The secure record is the **total**. The companion’s rank among the lightest neutron stars is provisional. 1.185 ± 0.022 easily straddles both the previous low companion near 1.17 M☉ and the ~1.192 M☉ floor from recent 3D supernova simulations.
- The orbit shrinks by about 40 µs per year. Observed over GR-predicted $\dot{P}_b$ is 1.009 ± 0.014 (0.6σ from 1). That is a real consistency check and a weak one: about 15 times looser than PSR J1946+2052 and about 100 times looser than the double pulsar. The masses used in the prediction already assume general relativity. The third relation is independent of the two used to weigh the stars, which is the standard method. It says nothing anomalous at 1.4%, in a compactness and mass-ratio regime those tighter systems already cover.
- Coalescence time 82 Myr (Peters’ formula). A stacked remnant estimate ~2.26 M☉ sits 0.05 M☉ under one TOV mass (2.31, with +0.36/−0.21). The paper’s hedge — stable neutron star or black hole — is the right reading. The margin is smaller than the inputs.
- Lense–Thirring (frame dragging) is a forecast, not a detection. The periastron route needs the decay known well enough to subtract the GR piece, which the authors put at about half a century plus a few-percent distance. The projected-semimajor-axis route is larger here because the orbit is tilted (i ≈ 47° or 133°, the same inclination), but only if the spin–orbit misalignment δ is a few degrees. The quoted δ ≥ 5.9° ± 3.4° is 1.7σ from zero, comes from a rotating-vector fit the paper itself calls systematically shaky for recycled pulsars, and is not established by three years of stable pulse profile. Geodetic precession is only ~5° per year, so three years would not have shown a profile change even for a few-degree tilt.
- The next system up in total mass sits ~0.04 M☉ higher. That gap is hundreds of times the total-mass error bar, so the total-mass record is secure **given** the GR mass formulas. A 2PN plus frame-dragging correction to $\dot{\omega}$ largely cancels and is ~14 times below the present error for realistic moments of inertia. It will matter once $\dot{\omega}$ improves by ~15×.

## Physical intuition

A recycled pulsar is a clock in a clean two-body lab. No disk, no mass transfer. The orbit’s slow turn is a scale for the total mass, the way Mercury’s extra precession scales with the Sun, except ~10⁵ times faster. The Einstein delay is the clock running fast and slow around the oval, and that is what splits the two masses. Gravitational waves then steal orbital energy, and the period shortens. You use two relativistic effects to weigh the stars and the third to see whether the energy-loss formula still balances.

Distance is the coming bottleneck. Dispersion-measure distances disagree (about 1.3 versus 2.0 kpc). A Galactic acceleration term of order 10⁻¹⁵ in $\dot{P}_b$ is negligible beside today’s error and dominant beside the precision needed for frame dragging. The source is faint for VLBI.

## Limitations and assumptions

- Single telescope, sparse early snapshots. Those early times carry leverage on $\dot{P}_b$ and proper motion. Residuals look clean. An independent timing campaign would still help.
- The quoted uncertainty on the GR-predicted decay in one table tracks the total-mass error and omits the mass-split error, which is ~15–20 times larger. It does not move today’s 1.4% test. It does eat a large piece of the future Lense–Thirring error budget. The “half a century” estimate is optimistic unless γ, or a Shapiro delay, improves faster than assumed.
- Kinematic correction today is still ~10 times below the decay error unless the distance is absurdly large. For the frame-dragging goal it is the main requirement, not a footnote.
- Merger outcome stacks a fitted mass relation, an ejecta mass borrowed from another event, and a cold non-rotating conversion. Equation-of-state choices can land this remnant on either side of the threshold.
- Higher-order terms in $\dot{\omega}$ can stay omitted now. The authors’ own 19-year forecast improves the error past the point where they must be modelled, as they already are for J1946+2052.

## Connections

- Another long-timed young binary, different science (geometry and a glitch, not a DNS mass record): [[psr-j1906-binary-timing]]
- A different compact binary whose decay already matches GR: [[rapid-orbital-decay-erassu-j060839]]
- Why simulations struggle to make neutron stars this light, and how flavor conversion changes who explodes: [[neutrino-flavor-failed-supernovae]]
- The merger this system will not be for 82 Myr, as a siren: [[gw170817-jet-hubble]]
- Dense-matter theory the moment of inertia would touch: [[color-superconductivity-qcd]]
- Synthesis: [[gravitational-wave-strong-field-probes]]

## Open questions

- Does a Shapiro delay appear and land on the γ-based split (range ~5.8 µs, sin i ≈ 0.73)?
- Does polarimetry over the next few years show geodetic profile evolution, which would pin δ and open or close the frame-dragging route?
- Does a timing parallax pick between the 1.3 and 2.0 kpc dispersion distances before the decay test becomes distance-limited?

## Source

- `raw/analyses/2026-10-03_arxiv-2607.27333_psr-j1856-0039-lightest-double-neutron-star.md`
