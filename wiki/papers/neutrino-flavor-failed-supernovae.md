---
tags: [papers, supernovae, neutrinos, compact-objects, failed-supernovae]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [supernova-onion-expansion, magnetar-slsn-2017egm-fermi, ice-core-fe60-local-cloud, rapid-orbital-decay-erassu-j060839, astrophysical-neutrinos, psr-j1856-lightest-dns]
source_analysis: "raw/analyses/2026-10-02_arxiv-2605.16504_neutrino-flavor-conversion-failed-supernova-rate.md"
---

# Neutrino Flavor Conversion and the Failed-Supernova Fraction

**One-line summary:** In 195 one-dimensional collapse runs, forcing neutrinos to share flavors evenly below a density cutoff raises the failed-explosion share from about a quarter of the models to between half and nearly all, concentrated at 16–30 solar masses. The deep cutoffs clash with the sky, and the birth-rate-weighted percentages do not reproduce cleanly from the figure. arXiv:2605.16504, Phys. Rev. D 114, L061304 (2026).

## Key claims and results

- **Paper:** Gogilashvili & Tamborra, arXiv:2605.16504v3 (18 Aug 2026), published as Phys. Rev. D 114, L061304 (2026). Companion on where flavor conversion helps or hurts a single star: arXiv:2605.18972.
- Grid: 195 of the 200 solar-metallicity Sukhbold et al. (2016) progenitors, 9–120 M☉, sampled every 0.1 M☉ from 13 to 30. Each is run in GR1D with the STIR turbulence stand-in (α_MLT = 1.51), the SFHo equation of state, once with no flavor conversion and once at each of four density cutoffs. About 975 runs. The five dropped models are not identified.
- The switch is schematic. From 20 ms after bounce, every cell below a cutoff density ρ_c is forced into full flavor equipartition, energy bin by energy bin. Cutoffs: 10⁹, 10¹⁰, 10¹¹, and 10¹³ g cm⁻³. Shallow mixing sits in the outer gain region, where hardening the electron-flavor spectrum should help heating. Deep mixing reaches the neutrinosphere, converts electron flavor at the source, and starves the gain region.
- Raw failed fractions (share of 195 models): 25.6% (no conversion), 50.8%, 77.4%, 93.3%, 96.4%. Salpeter-weighted fractions printed in the paper: 27.0%, 47.6%, 61.9%, 73.9%, 88.3%. The authors call 74% and 88% in tension with observations and say the numbers are a caution, not a forecast. A Kroupa IMF is said to look similar (not shown).
- The new failures concentrate at 16–30 M☉: 19/140 models fail with no conversion (~14%), then 62, 107, 133, and 135 of 140 as the cutoff deepens. A handful near 19.6–20.4 M☉ explode in every row. An analyst pixel read of Fig. 1 finds **no** model that fails without conversion and explodes with it, including at 10⁹ g cm⁻³ where the companion paper’s rule says heating should increase. The “help” shows up only as earlier, more energetic revival in stars that already explode.
- Remnant masses: exploding models leave slightly less baryonic mass inside the neutrinosphere (typically ~0.03–0.06 M☉ lower between 15 and 22 M☉). Much of the shift of the **population** toward lighter neutron stars, once ρ_c ≥ 10¹⁰, is selection. The 22–25 M☉ stars that made the heaviest neutron stars (~1.5–1.65 M☉ gravitational) stop exploding and become black holes. Footnote: one-dimensional masses of successful explosions are lower bounds, because downflows are missing. Failed-model masses at 1 s are not final black-hole masses. Fallback can add a lot.
- Why only electron flavor heats: charged-current absorption on neutrons and protons. Heavy-flavor neutrinos stream out of the energy budget that revives the shock. The shock needs only ~0.3% of the ~3×10⁵³ erg binding energy. A tens-of-percent change in capture efficiency moves a marginal star across the line.

## Physical intuition

The stalled shock is a server with a heavy request queue (infalling stellar matter) and a compute budget (neutrino heating behind the shock). Explosion means the backlog clears. Failure means the queue grows until the core becomes a black hole, often with only a faint optical dimming.

Flavor conversion is a load balancer that can drain the only workers who can do the writes (electron neutrinos). How early in the pipeline it acts is the whole experiment. Near the shock it mostly reshuffles energies where heating happens. At the neutrinosphere it cuts the electron-flavor crew at the factory gate. Deeper cutoff, more failures. In this code the islands of explodability only sink. They do not reshuffle both ways.

The overlap with the red-supergiant problem is suggestive and soft. Stars seen before ordinary Type IIP supernovae top out near 16–18 M☉, while red supergiants exist up to ~25–30 M☉. This is the mass band flavor conversion kills. The same code already fails a 13–15 M☉ band that **should** produce visible supernovae, so the reference model has a tension in the other direction.

## Limitations and assumptions

- Instant, complete equipartition below a free density is an extreme stand-in. Real fast flavor conversion needs angular crossings, need not finish, and moves in space and time. Read the table as a sensitivity sweep. No row is the best estimate.
- One-dimensional physics omits the standing accretion shock instability and proto-neutron-star convection. Both can restore explosions, especially for the compact, high-accretion 16–30 M☉ stars this lever hits. The paper says the landscape is biased toward failure. The **relative** rise may be more robust than the absolute fraction.
- Multi-dimensional work points the other way at low mass. Ehring et al. in 2D and Akaho et al. with multi-angle transport find flavor conversion **helping** some low-mass, low-accretion progenitors. Those stars dominate a birth-rate weight. This population shows no rescues.
- The Salpeter column is the one compared with the sky, and the analysis could not reproduce it from Fig. 1 under standard weightings. Every trial came out higher (roughly 39–44% failed with no conversion, and ~55–60% at 10⁹ g cm⁻³), largely because several of the IMF-heavy 9–13 M☉ models already fail. The weighting procedure is not stated. A missed convention or a few misread bars could close part of the gap. Until it is documented, “27% matches observations” is unverified.
- Observational anchors are soft. Direct failed-supernova searches (LBT; Neustadt et al.) give a failed fraction ~0.16 with a 90% interval about 0.04–0.39. The deep rows (74–88%) sit above that. The red-supergiant problem may be partly a mass-estimate bias. One progenitor set, one equation of state, solar metallicity, single stars only. Most massive stars are in binaries.
- Explosion means the shock reaches 1,000 km within 1–3 s. Marginal models can cross that line and still fail to unbind the envelope. Late revival is not in the window.

## Connections

- Ejecta structure and local supernova ash, not the explosion engine: [[supernova-onion-expansion]], [[ice-core-fe60-local-cloud]]
- A luminous magnetar engine, not a failed collapse: [[magnetar-slsn-2017egm-fermi]]
- Compact-object birth rates feed GW population models; a measured double neutron star is a different question: [[rapid-orbital-decay-erassu-j060839]]
- A weighed light companion (1.185 ± 0.022 M☉) near the simulation floor this paper discusses: [[psr-j1856-lightest-dns]]
- High-energy astrophysical neutrinos (IceCube) are a different energy and a different source class: [[astrophysical-neutrinos]]
- Synthesis: [[high-energy-astrophysics-multimessenger]]. Birth-rate consequences also sit next to [[gravitational-wave-strong-field-probes]] without being a waveform measurement.

## Open questions

- Does a dynamical, angle-aware subgrid model, in place of the density switch, still raise the 16–30 M☉ failure rate?
- How many of those failures survive in two-dimensional runs that can host the standing accretion shock instability, and does proto-neutron-star convection reverse the deepest rows?
- Can the per-model outcome table and the IMF weights be published so the 27–88% column is reproducible?
- Do failed collapses’ hotter neutrino spectra show up in the diffuse supernova neutrino background (Super-Kamiokande-Gd, JUNO)?

## Source

- `raw/analyses/2026-10-02_arxiv-2605.16504_neutrino-flavor-conversion-failed-supernova-rate.md`
