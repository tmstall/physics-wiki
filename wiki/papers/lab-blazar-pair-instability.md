---
tags: [papers, plasma, high-energy-astrophysics, blazars, laboratory-astrophysics]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [mrk501-double-jet-smbbh, beam-driven-plasma-mirror, plasma-relativistic-amplifier, aquila-booster-pevatron, dense-plasma-opacity-revision]
source_analysis: "spacex_export/extracted-analyses/2026-01-14_laboratory-suppression-of-blazar-instabilities_fcdb46c3.md"
---

# Laboratory Suppression of Blazar Pair-Beam Instabilities

**One-line summary:** Arrowsmith et al. (*PNAS* 2025) fire CERN SPS pair beams through meter-scale plasma and find no strong Weibel-like filamentation or amplified $B$ — realistic beam divergence and energy spread suppress growth, so missing blazar cascade GeV signals still favor primordial intergalactic magnetic fields over plasma instabilities.

## Key claims and results

- **Paper:** Charles D. Arrowsmith et al., *Proceedings of the National Academy of Sciences* (7 Nov 2025), DOI 10.1073/pnas.2513365122.
- **Astro puzzle:** TeV blazar photons pair-produce on the EBL → $e^\pm$ beams that should inverse-Compton CMB photons to GeV; Fermi sees little cascade GeV → something deflects or thermalizes pairs. Contenders: **IGMF** ($\sim10^{-15}$ G over Mpc) vs **beam–plasma instabilities**.
- Lab analogue: $3\times10^{11}$ 440 GeV protons → graphite–Ta target → $\sim10^{13}$ $e^\pm$ pairs (power-law GeV spectra, finite divergence) through 1 m argon plasma at $\sim10^{12}$ cm$^{-3}$.
- Diagnostics: Faraday rotation (TGG crystal, 532 nm) $B$ sensitivity $\sim5$ mT on 0.4 ns scales; Chromox screen for filamentation; OSIRIS PIC for cold vs realistic beams.
- Idealized cold collimated beams: PIC fields $\to\sim60$ mT, $\Gamma\sim2.1$ ns$^{-1}$.
- Realistic spread: saturated fields $\sim7$ mT, $\Gamma\sim0.2$ ns$^{-1}$; experiment sees **no $B$ above noise** ($\le5$ mT), smooth profiles → $\Gamma_{\rm exp}\le0.7$ ns$^{-1}$.
- Blazar scaling: $\Gamma_{\rm blz}\lesssim4\times10^{-10}$ s$^{-1}$; saturated self-fields $\ll$ IGMF deflection needs before IC cooling.
- Conclusion of the analysis: instability fix is **insufficient**; primordial IGMF remains the leading explanation for missing cascade GeV.

## Physical intuition

A laser-straight beam through plasma filaments like a traffic jam on a single-lane bridge — currents clump, magnetic fields explode. Real pair beams (and real blazar cascades) are **spray cans**: angular and energy spread lets particles cross filament scales before the field grows, damping the instability the way defocusing kills optical self-focusing damage. If the lab spray already kills growth, the ultra-dilute blazar spray cannot thermalize pairs before they IC-cool — so the missing GeV light is still a **magnetometer for primordial B**, not a plasma short-circuit.

## What “favor IGMF” does and does not mean

Ruling out strong beam–plasma dissipation strengthens the case that **something else** deflects or cools cascade pairs before GeV upscattering — with intergalactic magnetic fields the standard candidate. It does **not** by itself measure $B_{\rm IGMF}$ or prove a single magnetogenesis channel (inflation, phase transitions, battery mechanisms). Observational halo searches, pair-echo timing, and multi-TeV blazar samples remain the astronomical half of the argument; this page is the **laboratory half**. On [[high-energy-astrophysics-multimessenger]] it sits next to PeVatron and SLSN γ-ray engines as a different messenger: lab plasma physics informing cosmological $B$.

## Limitations and assumptions

- Residual protons seed seed $B_0$; assumed not to dynamo the measured modes, but higher densities could change that.
- Argon lab plasma ≠ hydrogen IGM composition; damping details may differ.
- Meter / ns scale misses quasi-linear evolution over kpc and long cooling times.
- Lab GeV pairs vs blazar TeV-class Lorentz factors: relativistic suppression may be under- or overestimated.
- Analysis-based ingest; verify $\Gamma$, Faraday limits, and Monte Carlo scaling against primary *PNAS*.

## Connections

- Blazar / SMBH jets: [[mrk501-double-jet-smbbh]], [[category-79-quasar-wind]]
- Lab / relativistic plasma tools: [[beam-driven-plasma-mirror]], [[plasma-relativistic-amplifier]], [[filming-plasma-birth]]
- Extreme HEA accelerators: [[aquila-booster-pevatron]]
- Dense-plasma context: [[dense-plasma-opacity-revision]], [[warm-dense-matter]]
- Key terms: blazar pair cascade, Weibel-like instability, IGMF, inverse Compton cooling, laboratory astrophysics, CERN SPS
- Synthesis: [[high-energy-astrophysics-multimessenger]] (HEA & multi-messenger map)

## Source

- `spacex_export/extracted-analyses/2026-01-14_laboratory-suppression-of-blazar-instabilities_fcdb46c3.md`
