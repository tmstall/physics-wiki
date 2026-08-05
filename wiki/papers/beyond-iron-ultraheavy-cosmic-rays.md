---
tags: [papers, cosmic-rays, nuclear-astrophysics, high-energy-astrophysics]
last_updated: 2026-08-02
status: analysis-ingest
related_papers: [aquila-booster-pevatron, gamma-glow-pbh-detector, supernova-onion-expansion]
source_analysis: "claude_export/extracted-analyses/2026-06-14_beyond-iron-the-universe-s-most-violent-events-may-be-firing_344a8eb5.md"
---

# Beyond Iron: Ultraheavy Nuclei as Ultrahigh-Energy Cosmic Rays

**One-line summary:** Ultrahigh-energy events such as Amaterasu may be ultraheavy nuclei (beyond iron) from r-process sites; once photodisintegration tables are extended past iron, bulk nuclei survive intergalactic transit *better* than naive “bigger target” intuition suggests.

## Key claims and results

- **Topic:** Propagation and composition of ultrahigh-energy cosmic rays (UHECRs) above ~EeV; analysis frames Zhang, Murase, and collaborators.
- Standard propagation toolkits (e.g. CRProPa) historically stopped at iron ($A=56$). The work builds photodisintegration cross-section tables up toward uranium and tracks thousands of isotopes plus radioactive decay.
- Counterintuitive propagation result: photodisintegration loss length scales only weakly with mass ($\sim A^{-0.21}$ in the analysis framing) because larger geometric cross section is nearly cancelled by smaller inelasticity per photon hit (~$1/A$).
- At ~100–500 EeV, Bethe–Heitler pair production (scaling strongly with charge $Z$) can dominate losses for ultraheavy (UH) species, yet UH nuclei can still out-range protons and iron-group nuclei in key windows.
- Hillas-type acceleration ceilings scale with $Z$, so platinum-class nuclei can start higher in energy in the same source.
- Joint spectrum + shower-maximum fits: UH as a second population improves Telescope Array high-energy tail fits more than Auger; tension between detectors becomes partially composition-related.
- Higher $Z$ also means stronger Galactic magnetic deflection — Amaterasu’s void backtrack may mislead if the particle is UH rather than a proton.
- Energy budget check: UH injection rates of order ~$10^{43}$ erg Mpc$^{-3}$ yr$^{-1}$ sit in the ballpark of binary neutron-star merger ejecta energetics with a few-percent cosmic-ray efficiency (order-of-magnitude, analysis-level).

## Physical intuition

Think of a UHECR nucleus as a truck of freight crates, not a single bullet. Each CMB/EBL photon collision knocks off a small fraction of the cargo. A single-crate truck dies in one pothole; a 195-crate truck can lose many crates and still be a truck. That is why “heavier = more fragile” fails at the energies that matter: total target size grows with $A$, but each hit removes only ~$1/A$ of the energy budget. Charge $Z$ still taxes the nucleus via electromagnetic pair production — more charge means more drag — yet the mass reservoir often wins the long-haul race compared with protons, which can dump energy in bulk pion-producing collisions (GZK-style opacity).

## Limitations and assumptions

- Analysis-based ingest: verify numerics and fit $\chi^2$ against the primary paper.
- Computational/theoretical propagation study with observational consistency checks — does **not** prove UH nuclei dominate the UHECR flux.
- Photodisintegration tables and nuclear-reaction codes (e.g. TALYS) inherit nuclear-model uncertainties at high $A$.
- Source spectra, extragalactic magnetic fields, and Auger–TA systematics remain major composition degeneracies.
- r-process abundance and acceleration efficiency in mergers/collapsars are order-of-magnitude inputs.

## Connections

- High-energy astrophysics island: [[aquila-booster-pevatron]], [[pulsar-wind-nebulae]]
- Sub-knee rigidity spectrum (same messenger class): [[peters-cycle-cosmic-rays]]
- Extreme messengers / dark-sector neighbors: [[gamma-glow-pbh-detector]], [[synchrotron-dm-detector]]
- Explosive nucleosynthesis context: [[supernova-onion-expansion]]
- Key terms (no separate stubs): UHECR, GZK horizon, photodisintegration / Giant Dipole Resonance, r-process, rigidity $E/Z$, Hillas limit, Telescope Array vs Auger composition tension

## Open questions

- Do Auger and TA converge once UH templates enter both pipelines?
- Which r-process environments dominate the UH injection budget?
- Can multi-messenger counterparts (GW mergers, kilonovae) pin the source class?

- Related (SpaceX set): [[ice-core-fe60-local-cloud]] — Local 60Fe supernova ash in ice

## Source

- `claude_export/extracted-analyses/2026-06-14_beyond-iron-the-universe-s-most-violent-events-may-be-firing_344a8eb5.md`
- Caveat: bulk export analysis; confirm claims against primary paper.
