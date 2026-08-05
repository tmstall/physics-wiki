# SpaceX / xAI export inventory
**Scanned:** 2026-08-04  
**Source root:** `SpaceX_exported_data/`  
**Primary payload:** `prod-grok-backend.json` (~61.0 MB)

## Tree layout
```
SpaceX_exported_data/
  list.txt                 # recursive path listing
  ttl/30d/export_data/<user_uuid>/
    prod-grok-backend.json  # conversations + projects + media_posts
    prod-mc-auth-mgmt-api.json
    prod-mc-billing.json
    prod-mc-asset-server/   # profile pics + binary content blobs
```

## File counts
- **Total files:** 1138
- **Total size:** ~700.8 MB

| Extension / kind | Count |
| --- | ---: |
| `(asset content)` | 1120 |
| `.webp` | 7 |
| `(no extension)` | 7 |
| `.json` | 3 |
| `.txt` | 1 |

## Conversations
- **Conversations:** 224
- **Projects:** 3
- **Media posts:** 12
- **Tasks:** 0
- **Sender histogram (raw):** human 2892; `assistant` 1438; **`ASSISTANT` 1490** (case-variant — normalize on extract); `grok-4` 2; `model` 2
- **Conversations with non-empty response.metadata:** 204 (request/UI/deepsearch fields — not Claude-style tool_use blocks)
- **Conversations with URL/chrome-like message text:** 127
- **Metadata keys (sample):** request_metadata, deepsearchPreset, ui_layout, llm_info, request_trace_id, memoryReferences, …

### Content mix (manual read of titles)
Rough buckets among **224** threads:
- **Physics / paper analysis / QFT / condensed / astro:** large minority (dozens of clean titles; many short “-> paper” analyses + long learning threads)
- **Medical / digestive / electrolyte / transplant:** large multi-thread series (high character volume)
- **Music / MSL setlists / audiophile:** moderate
- **Tooling (Obsidian, Grok Build, prompts, WSL):** moderate
- **Consumer / Tesla / chrome / misc:** rest

Naive keyword scoring over-counts medical hits (e.g. “atom”/“electron” false positives). **Title-first + denylist** is required for full extraction.

### Representative physics titles (not exhaustive)
| Date | Title |
| --- | --- |
| 2025-02-28 | I - Astrophysics (and Black Holes) |
| 2025-03-01 | I - Quantum Mechanics & Quantum Field Theory |
| 2025-05-07 | Quantum Field Theory |
| 2025-11-08 | Massive Gravity/Gluon Magic |
| 2026-05-09 | -> Hawking Radiation from Charged Shell |
| 2026-05-05 | -> Collapse, Gravity & Proper-Time Uncertainty |
| 2026-05-06 | -> Quantum Proper Time Signatures in Ion Clocks |
| 2026-05-17 | Cluster Tunneling Forges Scalable Schrödinger Cats |
| 2026-06-03 | Photon Truncation Creates Infinite Particle Zoo |
| 2026-05-08 | -> Photonic Supersolid Nature Paper |
| 2025-10-01 | Quark-gluon plasma Discussion |
| 2026-07-20 | Einstein and Riemann Geometry in Relativity |

### Structural notes vs Claude export
- Claude: top-level array of conversations with `chat_messages` / structured `content[]` blocks (text/thinking/tool_use).
- Grok: `{conversations:[{conversation, responses:[{response, share_link}]}]}`; message is a plain `message` string; `sender` is `human` or `assistant`.
- Titles are first-class (`conversation.title`).
- Asset server holds mostly binary `content` blobs + webp avatars — **not** analysis text.
- Auth/billing JSON are non-content noise for physics extraction.

### Noise assessment
- Structured tool noise is **different from Claude**, not absent: metadata holds deepsearch/UI/llm_info; message body may embed `<grok:render …>` image/search cards and bare URLs.
- Sender field is **case-inconsistent** (`assistant` vs `ASSISTANT`) — extractors must normalize.
- Non-physics bulk (medical, music, tooling) dominates raw character volume; do not rank by size alone.
- Soft topic overlap with existing wiki (Hawking shell, ion clocks, cats, supersolid, etc.) expected at **ingest** time.

### Status
- Inventory complete.
- Pilot extract: `spacex_export/PILOT_REPORT.md` (15 files).
- **Full extraction complete:** `spacex_export/FULL_EXTRACTION_REPORT.md` + `FULL_MANIFEST.json`.
- Kept **94** physics analyses under `spacex_export/extracted-analyses/`.
- Wiki not modified (ingest is a separate step).
