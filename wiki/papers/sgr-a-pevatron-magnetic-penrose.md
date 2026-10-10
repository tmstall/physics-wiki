---
tags: [papers, galactic-center, pevatron, cosmic-rays, sgr-a, penrose-process, multimessenger]
last_updated: 2026-10-09
status: analysis-ingest
related_papers: [s301-sgra-spin-sensitive-star, aquila-booster-pevatron, cygnus-x3-pevatron-bubble, icecube-galactic-plane-neutrinos, magnetar-slsn-2017egm-fermi]
source_analysis: "raw/analyses/2026-10-09_arxiv-2609.04051_sgr-a-pevatron-magnetic-penrose-process.md"
---

# Sgr A* as a Galactic PeVatron: Magnetic Penrose Process

**One-line summary:** A preprint argues that neutrons from Sgr A*’s hot flow decay in the ergosphere and the hole’s spin–magnetic voltage flings protons to a few–tens of PeV; the energy arithmetic holds, but the predicted γ-ray/neutrino flux assumes every arriving neutron decays in the few seconds it spends there. arXiv:2609.04051.

## Key claims and results

- **Paper:** arXiv:2609.04051v1 (3 Sep 2026), 27 pages, no journal reference. Unreviewed theory/phenomenology chain: ADAF → p+He neutron production → Kerr geodesics → Wald vacuum magnetosphere → CMZ transport → H.E.S.S./HAWC/IceCube/CTAO/SWGO comparison. Builds on Tursunov et al. and Oh & Park (*Phys. Rev. D*).
- Genuine front-end improvement: neutron energies from measured p+He breakup kinematics in the colliding-ion frame, not a thermal ion distribution. Fewer fast neutrons; gravitational escape several times lower than the thermal shortcut.
- Survival to the ergosphere is tracked on exact spinning-hole paths with each neutron’s own clock (15 min lifetime). Inner-flow neutrons arrive almost intact. The calculation answers “does it get there?”, not “does it decay once there?”
- Energy gain from Wald’s aligned vacuum field, every decay placed at the equatorial outer ergosphere edge: $E_p \approx E_n(1 + e B G M a_*/(2 m_p c^4))$. Benchmark ($a_*=0.94$, $B=100$ G) → max ~10 PeV, proton power ~$9\times10^{37}$ erg/s. LOW-B / HIGH-B span ~3–55 PeV.
- Predicted fingerprint: γ-ray and neutrino spectra that rise steeply and peak between a few hundred TeV and a few PeV. Published curves sit below existing H.E.S.S./HAWC points and approach SWGO/CTAO sensitivity near a PeV.

## Physical intuition

A spinning hole stores rotational energy in the ergosphere, where energy-at-infinity can go negative. The gravity-only Penrose split is inefficient. The magnetic upgrade is a dam: a neutral neutron arrives, decays into p + e, the electric field (spin twisting B) dumps the electron down the drain and shoots the proton through the full voltage. A ~100 G field across Sgr A* is tens of petavolts, so the proton energy is set by the reservoir height, not by the neutron’s few-tens-of-MeV birth speed.

The hot, starved flow (ADAF) is a reactor with no moderator: ions near 10¹² K knock neutrons off helium; the gas is so thin the neutrons free-stream on gravity paths. Escaping protons light the Central Molecular Zone in pion-decay γ-rays and neutrinos.

## Limitations and assumptions

- **Decay probability omitted (load-bearing).** Crossing the equatorial ergosphere takes ~7–25 s at $a_*=0.94$ against a 15 min lifetime, so only ~1 in 35–140 arriving neutrons decay inside (thinner band at low spin: ~1 in 250–500). Unless something holds neutrons in the band, proton rate, power, and all fluxes are overstated by ~40–140× (more at low spin). Maximum *energies* are unaffected. After the correction, SWGO/CTAO detectability claims do not survive. Oh & Park appear to include this factor; this paper’s figures do not.
- Vacuum Wald field vs magnetically arrested plasma: standard expectation is near-complete screening of $E_\parallel$ outside thin gaps. PeV claim needs ≳10% of the vacuum voltage to survive. Published Benchmark power is ~15× a standard spin-powered jet estimate; proton current would drain the induced charge in under a minute. Decay correction brings power back under the jet estimate; the vacuum premise stays unproven.
- Every decay at the outer edge picks the *largest* gain in the band; decays spread through it smear the “sharp PeV hump” fingerprint by ~2× in energy.
- Spin $a_*\approx0.94$ is an EHT simulation-library preference, not a measurement. [[s301-sgra-spin-sensitive-star]] is the star that may eventually measure it.
- At PeV the CMZ diffusion step is comparable to the zone radius (streaming, not wandering). Flux change ≲2×, small next to the decay factor. Steady-state assumed despite X-ray echoes and Fermi bubbles.
- “Consistent with H.E.S.S. and HAWC” is non-exclusion: predictions sit below every measured point and peak where there are no data.

## Connections

- Sgr A* spin as a future measurement, not an input: [[s301-sgra-spin-sensitive-star]]
- Galactic PeVatrons (different engines): [[aquila-booster-pevatron]], [[cygnus-x3-pevatron-bubble]]
- Galactic-plane neutrinos as the hadronic screen: [[icecube-galactic-plane-neutrinos]], [[astrophysical-neutrinos]]
- Synthesis: [[high-energy-astrophysics-multimessenger]] (PeVatron / messenger map); light touch [[smbh-stellar-encounters]] (same hole, star vs neutron-seed)

## Open questions

- Recompute the proton rate with ergosphere decay probability (and any retention mechanism) stated explicitly?
- Does a CTAO/SWGO Galactic Center spectrum stay a power law through a PeV, or show a hump? Shape is the sturdier handle; amplitude after the decay correction is expected to miss.
- Plasma-filled GRMHD: what fraction of the Wald voltage survives in the inner ergosphere?

## Source

- `raw/analyses/2026-10-09_arxiv-2609.04051_sgr-a-pevatron-magnetic-penrose-process.md`
