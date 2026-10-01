---
tags: [papers, ultracold-molecules, dipolar-gases, amo]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [amo-quantum-state-control, molecular-rotation-superfluid-he, quantum-droplets-bose-fermi]
source_analysis: "raw/analyses/2026-09-21_doi-10.1126-science.adz0521_extreme-loss-suppression-dipolar-molecular-gas.md"
---

# Extreme Loss Suppression in a Dipolar Molecular Gas

**One-line summary:** Yuan, Zhang, Bigagli, Kwak, Warner, Karman, Stevenson, and Will (*Science*, DOI [10.1126/science.adz0521](https://doi.org/10.1126/science.adz0521); arXiv:2505.08773) use two microwave fields on ultracold NaCs to suppress sticky short-range loss by more than $10{,}000\times$ while a second knob still sets the strength and sign of the long-range dipole. Groundwork: the sample is a thermal cloud of a few thousand molecules, not a many-body quantum phase.

## Key claims and results

- One circularly polarized microwave already dresses rotational states and builds a long-range barrier, but shielding depth and induced dipole share one knob. Push the detuning too far and a new two-molecule bound state opens three-body loss. A second, linearly polarized field (Rabi frequency $\Omega_\pi$ beside $\Omega_\sigma$) splits those jobs.
- The dressed state mixes $|0,0\rangle$, $|1,0\rangle$, and $|1,1\rangle$. The $|1,0\rangle$ piece adds to the induced dipole; the $|1,1\rangle$ piece subtracts. Their ratio sweeps the interaction through zero, from dipolar to anti-dipolar. A negative dipolar length is a property of that superposition, not a flip of the bare permanent dipole in the lab frame.
- Inside $0.6 < \Omega_\pi/\Omega_\sigma < 1.1$ the dipolar length runs from about $-21{,}000\,a_0$ to $+12{,}000\,a_0$ while the suppression holds across essentially that whole window. Outside it, loss rises again where coupled-channels theory puts new bound states.
- Numbers, from about 4,000 NaCs molecules at $100(20)\,\mathrm{nK}$ and density $0.7(1)\times10^{12}\,\mathrm{cm^{-3}}$: undressed $1/e$ lifetime $3.0(3)\,\mathrm{ms}$; circular dressing alone $0.9(1)\,\mathrm{s}$ (about $300\times$); both fields $6.6(5)\,\mathrm{s}$. The one-body ceiling (background gas and trap heating) is $8.5(1.5)\,\mathrm{s}$. Two-body loss drops by more than $10{,}000\times$ and three-body loss by more than $1{,}000\times$. Collisional loss becomes subdominant. It does not vanish.
- The coupled-channels calculation (Karman, a co-author) tracks where three-body loss returns. That match is part of the result, not an independent lab.
- The same Columbia group’s 2024 NaCs molecular condensate is a separate paper. This work does not put the shielded gas into that condensate. The discussion treats the combination as the next step.

## Physical intuition

Atoms in a typical ultracold gas bounce and survive. Polar molecules usually do not: at short range they react or stick, and the pair leaves the trap. Lifetimes of milliseconds are too short to evaporate into a condensate and then sit still long enough to see a many-body phase. Microwave dressing mixes rotational states so two approaching molecules meet a repulsive wall before the sticky core. With one microwave, raising that wall also drags the long-range dipolar strength, and eventually digs a bound state that eats molecules three at a time. The second microwave is an independent knob. Keep the wall up, and still dial the long-range force from attraction, through zero, to repulsion. The cloud that died in 3 ms now lasts several seconds, close to the lifetime set by ordinary vacuum and heating. Electric dipoles this large are a much stronger long-range interaction than the magnetic dipoles of dysprosium or erbium. That is why the tuning range matters. The sample that demonstrates it is still a warm gas of a few thousand molecules.

## Limitations and assumptions

- Thermal gas only ($100\,\mathrm{nK}$, $\sim4{,}000$ molecules). Suppression at condensate density, and any droplet or supersolid, is not shown. A new loss channel at higher density remains possible.
- One species (NaCs) and one pair of rotational transitions. Other bialkalis (KRb, NaK, NaRb, RbCs) are plausible by analogy and untested with this two-field recipe. Quantitative factors depend on level spacings and transition dipoles.
- Single apparatus. The theory co-author is a long-term collaborator, not an outside check. A second lab and a second species are the replication that would rule out a trap-light-assisted loss that happened to fall along with the intended channel.
- Residual two-body and three-body loss is still present under the 6.6 s lifetime. “Collisionally stable” means collisions no longer set the clock.
- This ingest uses the arXiv companion because the Science HTML was paywalled. Introduction, dressing theory, lifetimes, tuning range, discussion, and figure captions were in hand; the full Methods and some loss-fit prose were not. Re-check fit details against the Version of Record or the supplement.

## Connections

- AMO state-engineering shelf (design a protected state; this page is collisional shielding of a molecular gas, not a cat or cavity attractor): [[amo-quantum-state-control]]
- Molecules as probes, different setting (optical centrifuge inside a helium nanodroplet, not a bulk dipolar gas): [[molecular-rotation-superfluid-he]]
- The many-body phase this shielding is meant to enable later — a self-bound droplet theory for a Bose–Fermi mixture, not a molecular-gas experiment: [[quantum-droplets-bose-fermi]]

## Source

- `raw/analyses/2026-09-21_doi-10.1126-science.adz0521_extreme-loss-suppression-dipolar-molecular-gas.md`
