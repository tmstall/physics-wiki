# SpaceX export — full extraction report

**Date:** 2026-08-04  
**Scope:** Full physics extraction (no wiki ingest).  
**Source:** `SpaceX_exported_data/.../prod-grok-backend.json`  
**Output:** `spacex_export/extracted-analyses/`  
**Manifest:** `spacex_export/FULL_MANIFEST.json`

## Counts

| Metric | Count |
| --- | ---: |
| Conversations examined | 224 |
| Kept (files on disk) | 94 |
| Newly extracted this run | 79 |
| Pilot files already present | 15 |
| Discarded (filter + post-filter) | 130 |

### Discard reasons

| Reason | Count |
| --- | ---: |
| denylist-title | 115 |
| not-physics | 9 |
| too-thin | 4 |
| denylist-body | 1 |
| postfilter-meta-prompt | 1 |

### Topic distribution (tag hits; multi-tag per file)

| Tag | Count |
| --- | ---: |
| condensed-matter | 43 |
| relativity | 40 |
| astro | 36 |
| quantum-info | 34 |
| amo-optics | 28 |
| cosmology | 27 |
| quantum-foundations | 25 |
| gravity-bh | 23 |
| qft | 22 |
| materials | 17 |
| nuclear-particle | 16 |
| chemistry | 14 |
| math-methods | 14 |
| biophysics | 3 |
| physics-general | 2 |

*(Counts after dropping one pure meta “analysis prompt” file.)*

## Cleaning quality

- Mean fraction removed (where measured): **1.7%**
- Same pilot discipline: role normalization (`ASSISTANT`→assistant), `<grok:render>` strip, URL/chrome cleanup, thin-ack drop.

## Filter policy

**Keep:** title physics cues, arrow paper-analyses, or strong body physics + substance.  
**Discard:** medical/digestive/transplant/electrolyte, music/MSL, Tesla/consumer, pure tooling/Obsidian/Grok Build/prompt meta, empty/audio, too-thin.

## Structural notes / surprises

- Sender case split (`assistant` vs `ASSISTANT`) remains real; full extract normalizes both.
- Deepsearch metadata is common but not required for cleaning; science lives in `message` strings.
- Mega-threads (astro, QFT learning series) stay as **one file per conversation** (no section split in this pass).
- Soft wiki overlaps expected (Hawking shell, ion clocks, cats, supersolid, CDW, η′, etc.) — left for **ingest-time** dedupe.
- Chemistry/biotech islands kept when clearly technical (e.g. benzidine, cryo-EM) and not medical protocol series.

## Status

**Extraction complete.** Wiki directory was not modified.
Ready for a separate ingest pass on approval.
