---
tags: [papers, qcd, critical-point, heavy-ion, star]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [nuclear-dense-matter-precision, rhic-net-proton-fluctuations, equilibrated-fraction-oo-qcd]
source_analysis: "raw/analyses/2026-09-24_doi-10.1103-2xsn-rgx3_nonmonotonicity-transverse-momentum-correlations-star.md"
---

# Non-monotonic Transverse-Momentum Correlations at STAR

**One-line summary:** PRL DOI 10.1103/2xsn-rgx3. STAR fixed-target: dip in a temperature-fluctuation proxy near the guessed QCD critical point. “5σ” means 5σ from a smooth baseline, not 5σ discovery. Published comment: ordinary nuclear effects can fake the dip. Next test is 3D-Ising finite-size scaling, not more precision on the same proxy.

## Key claims and results

- STAR Collaboration, Phys. Rev. Lett. 137, 132301 (2026); DOI 10.1103/2xsn-rgx3; arXiv:2609.26449. First transverse-momentum correlation measurement in this fixed-target, high-density corner. Framed as a constraint, not a discovery.
- Au+Au fixed-target at $\sqrt{s_{NN}}=3.0$–$5.2$ GeV, plus 7.7 GeV in both fixed-target and collider mode. Baryon chemical potential about 760–400 MeV.
- The correlator $C_{p_T}$ isolates dynamical covariance between distinct particles’ transverse momenta and divides by the event-averaged mean. It is a proxy for temperature-fluctuation size. A critical point should raise the heat capacity and **suppress** those fluctuations, so the search target is a dip, not a peak.
- In the most central (0–5%) collisions the low-energy points sit ~**5σ** below a monotonic curve anchored on 20–200 GeV data. The same procedure on the non-critical transport model AMPT gives ~1.4σ. The 30–40% bin gives ~2σ even though the raw correlator is larger there.
- Internal control: fixed-target and collider-mode results at 7.7 GeV agree, so the acceptance edge of the fixed-target geometry is unlikely to fake that point.
- Lacey, arXiv:2609.17279 (about a week later): distance from an assumed baseline is not evidence for criticality. Baryon transport, a shifting meson/baryon mix, hadronic rescattering, and resonance decays can be non-monotonic with no critical point.

## Physical intuition

There is no thermometer on the fireball, so momentum jitter stands in. At a critical point the heat capacity is enormous: pour energy in and the temperature barely moves, so the proxy should dip. A boring fireball of independent sources should instead shrink as one over the square root of the number of participants. STAR found a real dip, relative to a smooth reference, in the densest matter this probe has seen, near where people have guessed the QCD critical point sits. A dip in the proxy does not by itself prove you found the regime boundary. Ordinary nuclear physics moves the same counter.

## Limitations and assumptions

- One experiment. No near-term independent fixed-target beam-energy scan. The 7.7 GeV cross-check tests the measurement, not the interpretation.
- “5σ” is distance from a chosen monotonic baseline (and from independent-source scaling), not a discovery significance for the critical point. STAR’s own wording is “may be sensitive,” and collaboration members have said other explanations remain open.
- No finite-size-scaling test against 3D-Ising exponents. That shape test is the next discriminator, not a tighter error bar on the same proxy.
- AMPT missing the dip is weak exclusion. The paper notes AMPT also fails ordinary bulk momentum spectra in this regime.
- At the two lowest energies the scaling exponent is fixed by hand to $-1/2$. Systematics dominate statistics.
- Mid-central magnitude versus significance sits awkwardly with a pure critical-origin reading. The Letter reports the numbers and does not resolve the tension.

## Connections

- Synthesis: [[nuclear-dense-matter-precision]]
- Other heavy-ion / QCD pages: [[rhic-net-proton-fluctuations]], [[equilibrated-fraction-oo-qcd]]

## Source

- `raw/analyses/2026-09-24_doi-10.1103-2xsn-rgx3_nonmonotonicity-transverse-momentum-correlations-star.md`
