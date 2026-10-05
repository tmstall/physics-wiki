---
tags: [papers, cosmology, black-holes, simulations, large-scale-structure, agn]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [dual-agn-green-pea, high-z-quasar-pair-merger, mrk501-double-jet-smbbh, ultramassive-bh-binary-cavity, smbh-inclination-angle, s301-sgra-spin-sensitive-star, stellar-spin-repeating-partial-tde, gamma-glow-pbh-detector, 43gev-gamma-ray-line-clusters, bottom-heavy-imf-early-galaxies, astrid-bh-occupation-fraction]
source_analysis: "raw/analyses/2026-08-28_doi-10.3847-1538-4357-ae3c08_astrid-simulation-z0-black-holes-large-scale-structure.md"
---

# ASTRID at $z=0$: Massive Black Holes, Galaxies, and Large-Scale Structure

**One-line summary:** Zhou et al. (*ApJ* **999**:41, 2026) deliver the present-day report card for ASTRID — a ~0.33-trillion-particle hydro box that sinks black holes with dynamical friction instead of teleporting them — matching many local MBH/galaxy/cluster benchmarks while flagging BHAD overprediction, seed excess, and a GSMF knee dip (DOI 10.3847/1538-4357/ae3c08).

## Key claims and results

- **Paper:** Yihao Zhou, Tiziana Di Matteo, et al., *The Astrophysical Journal* **999**:41 (2026). DOI [10.3847/1538-4357/ae3c08](https://doi.org/10.3847/1538-4357/ae3c08).
- **Setup:** MP-Gadget SPH; ~$2\times5500^{3}$ particles; box $250\,h^{-1}$ Mpc (~370 Mpc); evolved $z=99\to0$; ~896M CPU-hours.
- **Dynamics upgrade:** black holes feel a **dynamical-friction** subgrid drag (Tremmel/Chen lineage) and merge only when close *and* bound — not repositioned to the potential minimum each step.
- **Local wins:** MBH mass function and AGN X-ray LF look decent above ~$10^{7}\,M_{\odot}$; median $M_{\mathrm{BH}}$–$M_{*}$ / $M_{\mathrm{BH}}$–$\sigma$ relations track observations with **broader scatter** than many repositioning peers; dust-attenuated colors recover red/blue bimodality; seven halos above $10^{15}\,M_{\odot}$; group/cluster stellar budgets scale reasonably.
- **Novel LSS claim:** MBH clustering **bias vs abundance is non-monotonic** — attributed to low-mass **wandering** holes diluting intermediate samples (impossible under pure repositioning).
- **Honest misses:** BHAD at $z=0$ overpredicted by **>1 dex**; excess $M_{\mathrm{BH}}<10^{7}\,M_{\odot}$ seeds; missing undermassive holes in some $M_{*}\sim10^{11}$–$10^{11.5}\,M_{\odot}$ galaxies; GSMF underdense by up to ~0.5 dex near $10^{11}\,M_{\odot}$ (kinetic-feedback critical mass suspected).

## Physical intuition

Repositioning is a teleport script: every black hole is glued to a halo’s potential minimum. Dynamical friction is a drag recipe — still subgrid, still softened — but it lets holes wander, sink slowly, and keep merger-clock information LISA/PTA care about. ASTRID’s bet is that one huge finished box with better traffic rules is more useful infrastructure than another repositioning twin that only matches median scaling relations.

## Limitations and assumptions

- Dynamical friction here is **not** resolved final-parsec stellar dynamics.
- Seed masses are a free stochastic prior (LISA-bracket motivated), not an ab initio seeding theory.
- Matching classic $M_{\mathrm{BH}}$–$M_{*}$ / $\sigma$ medians is a weak uniqueness test across the simulation zoo.
- Single flagship volume: cosmic variance remains for the rarest clusters.
- Analysis ingest from Claude v3.10 full-text read of the published *ApJ* article.

## Connections

- Concept: [[dynamical-friction]], [[supermassive-black-hole-binaries]], [[dual-agn]], [[pulsar-timing-arrays]], [[cosmic-web]]
- Feedback / pairing ladder: [[dual-agn-green-pea]], [[high-z-quasar-pair-merger]], [[mrk501-double-jet-smbbh]], [[ultramassive-bh-binary-cavity]], [[smbh-inclination-angle]]
- One-star / local SMBH probes: [[s301-sgra-spin-sensitive-star]], [[stellar-spin-repeating-partial-tde]]
- Structure / DM-adjacent: [[bottom-heavy-imf-early-galaxies]], [[gamma-glow-pbh-detector]], [[43gev-gamma-ray-line-clusters]]
- Same box, occupation decomposed into total / central / active: [[astrid-bh-occupation-fraction]]
- Synthesis: [[black-hole-feedback-and-changing-look-agn]], [[gravitational-wave-strong-field-probes]], [[cosmology-expansion-history-and-structure]]

## Open questions

- Will another large-volume non-repositioning run reproduce the non-monotonic MBH bias curve?
- Can lowering the kinetic-feedback critical mass fix the GSMF knee without wrecking other successes?
- How much of late-time BHAD overprediction is fixable with spin-dependent feedback vs retuning $\chi_{\mathrm{thr}}$?

## Source

- `raw/analyses/2026-08-28_doi-10.3847-1538-4357-ae3c08_astrid-simulation-z0-black-holes-large-scale-structure.md`
