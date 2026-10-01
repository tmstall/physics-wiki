---
tags: [papers, metrology, gravitation, big-g]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [quantum-proper-time-ion-clocks, thorium-229-nuclear-clock]
source_analysis: "raw/analyses/2026-09-20_doi-10.1088-1681-7575-ae570f_redetermination-gravitational-constant-bipm-torsion-balance-nist.md"
---

# NIST Redetermination of Big G with the BIPM Torsion Balance

**One-line summary:** Schlamminger et al. (*Metrologia* **63**, 025012, 2026; DOI [10.1088/1681-7575/ae570f](https://doi.org/10.1088/1681-7575/ae570f)) ship the BIPM torsion balance to NIST, rebuild masses, metrology, and software, and still disagree with that hardware’s earlier $G$ by $2.5\times10^{-4}$ — evidence the big-$G$ scatter lives in environment, procedure, and the calibration chain, not in one frozen instrument flaw. A new systematic: wall temperature gradients drive a residual-gas spurious torque.

## Key claims and results

- Result: $G = (6.67387 \pm 0.00038)\times10^{-11}\,\mathrm{m^3\,kg^{-1}\,s^{-2}}$, relative uncertainty $5.7\times10^{-5}$. Four sub-runs (copper and sapphire source masses $\times$ free deflection and electrostatic servo) enter a Bayesian model that assigns each configuration its own “dark uncertainty” because they disagree by more than the budgeted errors.
- The NIST value sits $2.5\times10^{-4}$ below the same apparatus’s BIPM Mark II number, several times either team’s quoted uncertainty. Offset from CODATA-22 is $-6.4\times10^{-5}$ and not significant ($p = 0.29$). The paper does not claim new short-range gravity; it treats unrecognized systematics as the working explanation of the historical scatter.
- This is the first like-for-like $G$ replication that moves the physical instrument, not a blueprint. NIST still requalifies almost everything else: a Zeiss Xenos CMM, new diamond-turned test masses (the originals had a tri-lobed form error), a rewritten mass-integration and control stack, a different vacuum system, and a sapphire mass set aimed at an AC magnetic coupling that copper could not rule out.
- New systematic, derived and checked: small temperature gradients on the chamber wall push residual gas (Waldmann’s thermophoretic force). A kinetic-theory model fit to the slow natural pressure rise then predicts both the pressure slope and the absolute torque in a separate 24-minute heater cycle. The fake torque is roughly a thousand times smaller than the gravitational signal and still large enough to matter.
- Free deflection (angle plus oscillation frequency; inertial calibration) and electrostatic servo (nulling voltage and capacitance gradient; electrical calibration) differ by a stable $\approx 1.8$–$2.1\,\mathrm{pN\cdot m}$ in both copper and sapphire. A search for cable dielectric loss and servo transients finds nothing. Mark II showed a similar split. The origin stays unknown.
- Dominant uncertainty terms are systematic, not more averaging: mass integration $16.2\,\mathrm{ppm}$, autocollimator nonlinearity up to $85.7\,\mathrm{ppm}$ on sapphire-free runs, and the pressure/thermal correction up to $21.5\,\mathrm{ppm}$.

## Physical intuition

A torsion balance is a mechanical integrator. Laboratory masses write a few tens of nanonewton-meters into a ribbon, and $G$ is whatever converts that twist into a constant. Move the same ribbon to a new room, replace the rulers and the software, and the constant still jumps by more than the error bars. That jump says the bug is not etched into one piece of hardware. One bug they did catch is a tiny gas wind: a warm patch of wall kicks residual molecules hard enough to twist the pendulum in a way that looks like gravity and scales with pressure. Heat the wall on purpose and the torque follows the kinetic-theory prediction. Catching that term does not close the book. Two independently calibrated readouts of the same torque still disagree by a couple of piconewton-meters, and the NIST number still misses BIPM’s number from this balance.

## Limitations and assumptions

- The authors state they have no conclusive explanation for the NIST–BIPM offset, and no single dominant cause.
- The free-deflection versus servo offset is also unexplained. Calling it “apparatus-intrinsic” only restates that Mark II saw something similar.
- Source-mass form error is corrected with partial-arc versus full-circle scans on the same CMM, not a second machine. The new test masses got a tighter independent cylindricity spec ($<0.25\,\mu\mathrm{m}$); the source masses did not.
- Dark-uncertainty prior widths follow an expert ranking of the four configurations (scaled $1\times$ through $4\times$), not widths fit from the data alone. A different ranking would reweight the average; the four values already sit close enough that the headline is unlikely to move much.
- The quoted uncertainty will not shrink just by running longer. The leading terms are calibration and geometry.

## Connections

- Precision-metrology cousins (clocks and proper time, not a $G$ measurement): [[quantum-proper-time-ion-clocks]], [[thorium-229-nuclear-clock]]

## Source

- `raw/analyses/2026-09-20_doi-10.1088-1681-7575-ae570f_redetermination-gravitational-constant-bipm-torsion-balance-nist.md`
