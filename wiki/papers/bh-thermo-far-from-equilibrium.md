---
tags: [papers, black-holes, thermodynamics, gr, horizons]
last_updated: 2026-09-05
status: analysis-ingest
related_papers: [black-hole-thermodynamics, black-hole-evaporation-energy-conditions, entropic-information-gravity, hawking-radiation]
source_analysis: "raw/analyses/2026-09-04_arxiv-2512.11659_bh-thermo-far-from-equilibrium.md"
---

# Black-Hole Thermodynamics Far from Equilibrium

**One-line summary:** Non-perturbative dynamical first law treats black-hole entropy on a marginally trapped surface (quasi-local), not the teleological event horizon; finite-process energy budget of matter + gravitational waves recovers BCH at equilibrium (arXiv:2512.11659; PRL + companion).

## Key claims and results

- **Paper:** Ashtekar, Paraizo & Shu, dynamical first law far from equilibrium (PRL Editors’ Suggestion; companion arXiv:2604.00170 carries proofs).
- Classic BCH first law compares neighboring *equilibria* and uses the **event horizon**, whose location needs the entire future — unusable mid-accretion, mid-merger, or mid-evaporation, and invisible to NR codes until a run finishes.
- Replace EH with a stack of **marginally trapped surfaces** (outgoing expansion $\theta_{(k)}=0$): dynamical horizon segments (DHS) when flux crosses (spacelike); isolated horizon segments (IHS) when flux switches off (null).
- Projection $\Pi$: every non-equilibrium horizon state maps to the unique Kerr equilibrium sharing areal radius $R$ and horizon spin $J_H$, handing each wild state well-defined $\mathring\kappa$ and $\mathring\Omega$.
- Unique energy vector $\xi^a$ fixed by demanding dynamical Komar-like charge match the equilibrium charge on every momentary IHS.
- Finite balance law (their Eq. 4): flux of horizon energy across a DHS segment equals $\Delta(\mathring\kappa A/4\pi G)+2\Delta(\mathring\Omega\mathcal J_{\mathcal H})$ — intensive parameters stay *inside* the finite difference.
- Gravitational-wave flux density on a spacelike DHS carries both familiar shear $\|\sigma\|^2$ and an extra $\|\zeta\|^2$ term (4 phase-space dof on a spacelike surface vs 2 on a null one).
- Smarr reconciliation: infinitesimal projection back to equilibrium collapses to textbook $\delta M=(\mathring\kappa/8\pi G)\delta A+\mathring\Omega\delta J$.
- Combined with Ashtekar–Krishnan area-increase / quantitative flux: dynamical entropy is $A/4G\hbar$ of the **MTS**, which sits *inside* the EH mid-process (Vaidya example: entropies can disagree by up to ~×4 during accretion; equal only at equilibrium).

## Physical intuition

Event horizons are offline batch jobs — you need the whole future trace. Quasi-local horizons are online: at each timestep, find where outgoing light is held still. The old first law was a passive snapshot comparison between two calm Kerr holes. The new one is an active ledger: what energy (matter + waves) crossed the wall between two snapshots equals how the hole’s temperature×entropy and spin books changed. Uniqueness theorems let black holes keep a well-defined “temperature” and spin even far from equilibrium — tidier, in that one respect, than a box of gas.

## Limitations and assumptions

- Entirely classical GR; $A/4G\hbar$ still enters via the Hawking-temperature analogy — no microscopic state count.
- MTSs are foliation-dependent and non-unique (“jumpiness”); paper manages with genericity + a chosen horizon, does not eliminate the issue.
- Letter restricts to axisymmetric DHS (authors claim inessential; full non-axisymmetric case deferred).
- Semiclassical evaporation (negative-energy flux, area *decrease*) is motivated but not treated — flux law uses classical stress-energy.
- Leverage is theoretical + numerical-relativity self-consistency ($\|\zeta\|^2$ coefficient on simulated mergers), not a new sky observable.
- Destination (entropy on apparent / MTS area) already converged perturbatively (Hollands–Wald–Zhang; Davies–Reall; Furugori et al.); novelty is the non-perturbative finite law and unique $\xi^a$.

## Connections

- Concept hub: [[black-hole-thermodynamics]], [[hawking-radiation]]
- Synthesis (interiors / NEC / evaporation): [[black-hole-evaporation-energy-conditions]]
- Synthesis (entropic / QI gravity lane): [[entropic-information-gravity]]
- Related classical / NR neighbors: [[black-hole-third-law-violation]], [[horizon-direct-wave-gw250114]], [[entropy-maximization-bh-mergers]]

## Source

- `raw/analyses/2026-09-04_arxiv-2512.11659_bh-thermo-far-from-equilibrium.md`
