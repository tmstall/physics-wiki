# SpaceX Waves 1–3 — lint report

**Date:** 2026-08-04  
**Scope:** 15 newly ingested paper pages from SpaceX Waves 1–3. No new ingest.  
**Catalog after lint:** 144 papers · 61 concepts · 5 synthesis

## Summary

| Check | Result |
| --- | --- |
| Pages in `wiki/index.md` | **15 / 15** present in correct clusters |
| Broken `related_papers` targets | **0** |
| Missing reverse paper↔paper links (before lint) | 33 |
| Reverse links added this pass | **~36** |
| Remaining missing reverse pairs | **0** (high-value paper↔paper) |
| New single-paper concept stubs | **0** (policy held) |
| Concept hubs expanded | `cosmic-web`, `magnons`, `pulsar-timing-arrays` |

## Links added or strengthened

### Paper ↔ paper (bidirectional)

- **Condensed-matter / moiré SC cluster:** nickelate ARPES ↔ BaTa₂S₅, Brown–Zak, CDW, supermoiré, quantum metric; anyon-trions ↔ supermoiré, fractional Fermi sea, 1D anyons; heliknoton ↔ SAF, quantum metric, photonic supersolid.
- **Nuclear / QCD cluster:** RHIC net-proton ↔ STAR J/ψ, high-pT ISR, NA61 isospin, EMC MARATHON, color SC; EMC ↔ SRC memory, NA61, RHIC.
- **Astro / multi-messenger:** MUSE filament ↔ JWST CND filament, dual quasars, Euclid, COSMOS-Web, feedback synthesis; magnetar SLSN ↔ supernova onion, Aquila PeVatron, gamma-glow, dense-plasma opacity; PSR J1906 ↔ pulsars-satellite-masses, GW170817, GW strain, horizon direct wave, PTA concept.
- **AMO / topology / ISM:** 1D anyons ↔ non-Abelian photonic braiding, three-body, anyon-trions; positronium diffraction ↔ 3D ED, SPDC ghost imaging, truncated photon, twisted-light; ice-core ⁶⁰Fe ↔ supernova onion, SPHEREx ice, sulfur ice, beyond-iron UHECR.

### Concept hubs

| Hub | Change |
| --- | --- |
| [[cosmic-web]] | Added MUSE filament + local JWST CND filament as multi-scale filament anchors; updated related_papers |
| [[magnons]] | Pointed to heliknoton as 3D topological spin texture cousin of magnon physics |
| [[pulsar-timing-arrays]] | Added PSR J1906 as single-binary TOA laboratory sharing PTA craft |

### Index cluster placement (confirmed)

| Cluster | Pages |
| --- | --- |
| Solid-state / materials | nickelate, supermoiré, anyon-trions, quantum metric, heliknoton, non-Abelian photonics, positronium diffraction |
| QCD / dense matter | RHIC net-proton, EMC MARATHON, NA61 isospin |
| Quantum foundations & information | 1D anyons momentum tails |
| Cosmology / LSS | MUSE filament, PSR J1906, ice-core ⁶⁰Fe |
| High-energy astrophysics (Islands) | magnetar SLSN Fermi |

## Pages that still need attention (optional, non-blocking)

| Page | Note |
| --- | --- |
| `rhic-net-proton-fluctuations` | Source extract mixed with off-topic chat; claims should be verified against full STAR paper when deepening. |
| `emc-effect-marathon-a3` | Conversational Grok analysis; arXiv:2410.12099 numbers provisional. |
| `na61-isospin-kaon-asymmetry` | Extract filename mislabeled “nuclear magnetization”; science is isospin/kaon — page body is correct, title/source note already flags this. |
| `magnetic-heliknoton-electric-write` | Solid but shorter; could deepen micromagnetic / Hopf-index detail later. |
| `positronium-diffraction-graphene` | Solid but shorter; beam-coherence numbers worth primary-paper check. |

None of these block catalog use; they are “deepen when convenient,” not structural failures.

## Link-density assessment

| Metric | Assessment |
| --- | --- |
| Outgoing wikilinks per new page | Typically **5–10** (papers + concepts/synthesis) |
| Intra-set connectivity | **Good:** CM moiré trio cross-linked; nuclear trio cross-linked; anyon 1D/2D linked; photonics topology linked |
| Hub leverage | New pages hang off existing multi-paper hubs rather than orphan stubs |
| Overall | **Healthy for a bulk experimental ingest set.** Density matches mid-quality Claude export pages; better than thinnest bulk pages, thinner than hand-crafted early wiki pages. |

## Actions taken

1. Full reverse-link audit of all paper↔paper edges from the 15 pages.
2. Added ~36 reverse (or cross) links on existing pages.
3. Expanded three multi-paper concept hubs only.
4. Confirmed index cluster placement for all 15.
5. Logged lint pass in `wiki/log.md`.

## Status

**Lint complete.** Remaining 12 TRIAGE NEW files **not** ingested.
