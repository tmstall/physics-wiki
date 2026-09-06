---
tags: [papers, astrophysics, star-formation, protoplanetary-disks, streamers, alma]
last_updated: 2026-08-29
status: analysis-ingest
related_papers: [chondrite-pressure-bump, iras-21204-fuor, dr21-magnetic-accretion]
source_analysis: "raw/analyses/2026-08-26_doi-10.3847-1538-3881-ae8bae_streamer-misalignment-gw-ori-circumtriple-disk.md"
---

# Streamer-Driven Misalignment in the Circumtriple Disk of GW Ori

**One-line summary:** Combined ALMA mosaics map a ~12,000 au infalling streamer onto GW Ori’s Class II circumtriple disk; TIPSY trajectory fitting puts the streamer’s angular-momentum axis within 3° of the outermost dust ring (~1-in-1,400 random chance), favoring external streamer-driven tilt of the outer disk over a purely internal origin.

## Key claims and results

- **Paper:** *Astronomical Journal* article, DOI 10.3847/1538-3881/ae8bae (peer-reviewed, open-access AJ; analysis from full PDF).
- Target: hierarchical triple GW Ori (A–B ~1 au; C ~8 au) with a warped circumtriple disk — three dust rings at ~11°, ~35°, and ~40° tilt relative to the inner binary plane (prior continuum work).
- New + archival ALMA $^{12}$CO / $^{13}$CO / C$^{18}$O $J=2$–1 mosaics (12 m + 7 m + Total Power) roughly double the mapped streamer extent (~14″ → ~30″, ~5,600 → ~12,000 au).
- Streamer mass from optically thin $^{13}$CO under LTE at ~15 K: $1.6\pm0.8\,M_{\mathrm{Jup}}$; C$^{18}$O non-detection upper limit ~4.6 $M_{\mathrm{Jup}}$.
- TIPSY ballistic trajectory fit: bound (negative specific energy) infall; timescale ~0.03–0.05 Myr; $\dot{M}_{\mathrm{in}}\sim(3.64\pm3.19)\times10^{-8}\,M_\odot\,\mathrm{yr}^{-1}$ — about $10\times$ below the star’s present accretion rate (~$3\times10^{-7}\,M_\odot\,\mathrm{yr}^{-1}$), read as a late-stage trickle after a stronger past episode.
- Angular-momentum alignment: streamer vs outer / middle / inner rings ≈ **3° / 8° / 32°**; random 3° alignment probability ≈ 0.07% (~1/1400).
- Impact zone of the best-fit trajectory falls in the radial range of the more massive middle/outer rings (~168 and ~245 $M_\oplus$ dust), not the light innermost ring (~7 $M_\oplus$).
- Total Power diffuse emission toward Orion cloud lies within a Bondi–Hoyle capture radius ~$31{,}000\pm18{,}000$ au; theoretical BH rate ≫ observed streamer rate — again consistent with declining late-stage accretion.
- Streamer’s present specific angular momentum is *smaller* than the disk’s; causal misalignment claim therefore leans on an inferred stronger past infall, not today’s measured torque budget alone.

## Physical intuition

A Class II disk is supposed to look settled — turntable already spinning. A streamer is fresh cloud gas still joining from outside; its orbital angular momentum can reorient the outer disk the way an off-axis cargo load twists a spinning platform’s edge. Matching 3D spin axes (not just sky-plane morphology) is the forensic test: which ring got hit. The inner ring’s large mismatch leaves room for the classic internal torque from the triple stars themselves. CO isotopologues act like different logging verbosity levels — rare $^{13}$CO sees through the optically thick $^{12}$CO surface and gives a usable mass census.

## Limitations and assumptions

- Single-system, single-facility case study; TIPSY method is widely used elsewhere, but this GW Ori causal claim has no independent re-derivation yet.
- Mass inherits LTE, temperature, abundance, and isotopic-ratio assumptions; authors fold ~10% continuum flux tension into uncertainties.
- Causation ≠ alignment: present-day streamer is angular-momentum-poor relative to the disk; “stronger in the past” is inferred from accretion-rate and ring-mass arguments, not multi-epoch torque measurements.
- Cloud connection is projected proximity + similar line-of-sight velocity inside $R_{\mathrm{BH}}$, not a proven continuous 3D flow.
- Split / double-component streamer structure left open (hollow cylinder, rotating cylinder, two overlapping streamers, …).
- SO non-detection ambiguous (no shocks vs insufficient sensitivity).

## Connections

- Synthesis (structure / assembly context): [[cosmology-expansion-history-and-structure]]
- Planet-forming disk traps / pressure-bump physics (streamers can seed bumps in the broader literature): [[chondrite-pressure-bump]]
- Young stellar / disk accretion neighbor: [[iras-21204-fuor]]
- Larger-scale star-forming filament / magnetic accretion context: [[dr21-magnetic-accretion]]
- Competing internal explanations still live for the *inner* ring: stellar torques from the triple, or an unseen embedded planet — this paper’s strongest claim is specifically for the *outer* misalignment channel.

## Open questions

- Higher-resolution shock-tracer (SO / related) search at the predicted impact zone ($x\approx-0.082''$, $y\approx-0.87''$).
- Does the same angular-momentum alignment signature appear in a TIPSY population study of other streamer+warped-disk systems?
- What resolves the streamer’s split brightness / dual-velocity structure?
- Direct constraints on whether past infall was strong enough to deliver the required angular momentum budget.

## Source

- `raw/analyses/2026-08-26_doi-10.3847-1538-3881-ae8bae_streamer-misalignment-gw-ori-circumtriple-disk.md`
