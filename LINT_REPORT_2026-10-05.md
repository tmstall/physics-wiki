# LINT_REPORT_2026-10-05

Full AGENTS lint after the headless ingest of the 2026-10-05 queue (13 rows). The 10th new paper page closed the queue, so this is the one full lint. No separate light lint.

## Catalog
- Papers on disk: **250** (index header 250). Every `wiki/papers/` file appears in `wiki/index.md`.
- Concepts: **62** (all named in the index)
- Synthesis hubs: **18**, plus companion `measurement-threads-1-7-refresher.md` on disk (19 files). Header matches.

## Queue
- READY_QUEUE pending: **0**
- `incoming/md/` root markdown: **0**

## Unresolved wikilinks
- Unique targets with no page: **0** (`wiki/log.md` exists; it is not an orphan)

## Contradictions (this run)
- CHIME vs MeerKAT: [[chime-21cm-autopower-z1]] points at the revised MeerKAT **3.2σ / 3.5σ**, and [[hi-intensity-mapping-meerkat]] keeps those numbers. The older 8–11σ draft is not restored.
- ASTRID: near-unity total occupation on [[astrid-bh-occupation-fraction]] is the seeding rule. It matches the seed-excess flag on [[astrid-z0-mbh-lss]]. It is not a second box and not a light-versus-heavy test.
- Failed supernovae: [[neutrino-flavor-failed-supernovae]] still says the birth-rate column did not reproduce and that deep cutoffs clash with searches. [[astrophysical-neutrinos]] now says this is not an IceCube source.
- No stale “21 cm experiment page missing” line remains in the synthesis hubs. The open gap is reionization-era 21 cm.

## Cross-links patched
Primary cousins that the new pages named and that did not link back:
- [[nonabelian-photonic-braiding]] ← [[photonic-momentum-space-topology]]
- [[massive-gravity-drgt]] ← [[gauss-bonnet-qnm-spectral-atlas]]
- [[ultraheavy-dm-levitated-magnet-polonaise]] and [[dissipative-cavity-entanglement]] ← [[levitated-oscillator-stationary-entanglement]]
- [[astrophysical-neutrinos]] ← [[neutrino-flavor-failed-supernovae]] (distinguish only)
- [[tempos-metal-poor-o-stars]] ← [[megatron-ufd-iron-plateau]]
- `related_papers` YAML filled where the Connections prose was already updated: MeerKAT, ASTRID z=0, looking-inside, PSR J1906, neutrino-flavor

Distant see-also links (DESI, GW170817, color superconductivity, and similar) were not force-mirrored.

## Frontmatter
- Removed a second `last_updated` key on [[black-hole-thermodynamics]] (kept 2026-09-05), [[quantum-proper-time]] (kept 2026-08-16), and [[type-ia-supernovae]] (kept 2026-08-16). Pre-existing. No other duplicate `last_updated` keys remain.

## Orphans and concepts
- No new orphan pages. No paper file is absent from the index.
- Pre-existing index table repeats (not introduced today): `multi-agent-collective-ai`, `parton-jets`, `quantum-jamming`.
- Not created: a post-reionization 21 cm autopower concept. Two experiment pages plus [[baryon-acoustic-oscillations]] already say neither detection is a BAO ruler. A hub can wait until a third measurement or a reionization-era page arrives.

## New pages
- All 10 have `source_analysis`, Key claims, Physical intuition, Limitations, Connections, and Source.
- No figure embeds. Source files exist. CHIME’s `source_analysis` is the `_plain` file. The levitated page uses the non-`sonnet_` file.

## Verdict
- **PASS**
