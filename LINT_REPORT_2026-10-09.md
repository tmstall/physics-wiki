# LINT_REPORT_2026-10-09

Full AGENTS lint after the headless ingest of the 2026-10-09 queue (10 pending rows). The 10th new paper page closed the queue, so this is the one full lint. No separate light lint.

## Catalog
- Papers on disk: **260** (index header 260). Every `wiki/papers/` file appears in `wiki/index.md`.
- Concepts: **62** (all named in the index)
- Synthesis hubs: **18**, plus companion `measurement-threads-1-7-refresher.md` on disk (19 files). Header matches.

## Queue
- READY_QUEUE pending: **0**
- `incoming/md/` root markdown: **0**

## Unresolved wikilinks
- Unique missing page targets: **0**
- `wiki/log.md` contains two historical mentions of the literal token `[[wikilinks]]` in old lint notes. Those are meta wording, not missing pages. `wiki/log.md` itself is linked from the index as `[[log]]`.

## Contradictions (this run)
- 4D PBH γ-glow vs 5D Dark Dimension: [[gamma-glow-pbh-detector]] still uses 4D Hawking bookkeeping. [[primordial-black-holes-are-5d]] states the ceiling and the slower 5D evaporation *only if* the micron extra dimension is real, and [[dark-matter-detection-channels]] Thread B flags it as a possible weakening, not a replacement bound.
- Sgr A* spin: [[s301-sgra-spin-sensitive-star]] remains a forecast. [[sgr-a-pevatron-magnetic-penrose]] takes a high spin as a model input and does not claim a measurement.
- Radio-galaxy superlative: [[radio-galaxy-z4946]] records the redshift and ID as solid and the $P_{500}$ ranking as unreproduced (missing $1+z$). Index summary matches.
- Mars pebble fraction: [[volatile-depletion-hybrid-accretion]] quotes the wider 10–37% range, not the abstract’s 27±5% from the disfavoured Vesta-fixed model.
- No stale “21 cm experiment page missing” line remains. The open gap is still reionization-era 21 cm.

## Cross-links patched
Primary cousins that the new pages named and that now link back:
- [[gamma-glow-pbh-detector]], [[pre-bang-leftovers]], [[five-dimensional-classical-gravity]], [[cms-black-holes-sphalerons-svm]] ← [[primordial-black-holes-are-5d]]
- [[chondrite-pressure-bump]], [[ch3oh-hcn-3i-atlas-outgassing]] ← [[volatile-depletion-hybrid-accretion]], [[enceladus-ice-grain-salt-segregation]]
- [[life2-telescope-array-biosignatures]] ← [[tesla-thermoformed-tactile-sensor]]
- [[s301-sgra-spin-sensitive-star]], [[aquila-booster-pevatron]], [[cygnus-x3-pevatron-bubble]], [[icecube-galactic-plane-neutrinos]] ← [[sgr-a-pevatron-magnetic-penrose]]
- [[extracting-reasoning-traces-proprietary-llms]] ← [[model-growth-looping-scaling-exponents]]
- [[magnetar-slsn-2017egm-fermi]], [[stellar-spin-repeating-partial-tde]] ← [[grb-220706a-month-long-engine]]
- [[particle-view-nn-wavefunction]] ← [[deep-relu-statmech-realization]]
- [[euclid-high-z-quasar-census]], [[high-z-quasar-pair-merger]], [[jet-aligned-halpha-cgm]] ← [[radio-galaxy-z4946]]
- [[holismokes-sn-winny]], [[fdm-wave-lensing-hs0810]] ← [[muse-desi-lens-confirmation]]

Distant see-also links were not force-mirrored.

## Frontmatter
- No duplicate `last_updated` keys in `wiki/`.

## Orphans and concepts
- No new orphan pages. No paper file is absent from the index.
- Pre-existing index table repeats (not introduced today): `multi-agent-collective-ai`, `parton-jets`, `quantum-jamming`.
- Not created: Dark Dimension / PeVatron / tactile-sensor / ReLU-ensemble stubs (single-paper). [[primordial-black-holes]] and [[strong-gravitational-lensing]] / [[time-delay-cosmography]] already cover the multi-paper questions.
- Islands: planetary shelf is now 4 papers (graduation candidate; not moved). New ML/computation Islands subsection holds the two neural-net theory/scaling pages. Tesla patent stays under instrumentation.

## New pages
- All 10 have `source_analysis`, Key claims, Physical intuition, Limitations, Connections, and Source.
- No figure embeds. Source files exist in `raw/analyses/`.

## Verdict
- **PASS**
