# SpaceX export pilot — quality report

**Date:** 2026-08-04  
**Scope:** Pilot only (15 targeted physics conversations). No wiki ingest.

## Counts

- Requested pilot titles: 15
- Found in export: 15
- Usable analyses written: 15
- Skipped: 0
- Output dir: `spacex_export/extracted-analyses/`

## Noise removal

- Mean fraction of characters removed by cleaning: **~0.9%** (higher on some threads with image cards; e.g. Massive Gravity ~6.5%)
- Cleaning removed:
  - `<grok:render …>` image/search cards
  - bare URL lines and `[n] https://…` citation tails
  - Thinking stubs / tool-marker patterns
  - common web chrome phrases
  - excess blank lines
- **Pilot bug fixed:** assistant role often stored as `ASSISTANT` (uppercase); normalized to `assistant` before keep/drop logic.
- Unlike Claude, there is no rich `content[]` thinking/tool_use tree — noise is mostly **inline cards + URLs**, not separate tool blocks.

## Usability

- **15 / 15** targeted physics conversations produced usable technical markdown.
- All files exceed substance threshold (assistant body ≫ short chit-chat).
- Quality ranges from long multi-topic learning threads (astro/QFT) to focused paper analyses (Hawking shell, ion clocks, cats, supersolid, truncated photon).

## Structural differences from Claude export

| | Claude export | Grok / SpaceX export |
| --- | --- | --- |
| Payload | `conversations.json` array | `prod-grok-backend.json` object |
| Message shape | `content[]` typed blocks | flat `message` string |
| Roles | user/assistant | `sender`: human / assistant / **ASSISTANT** |
| Titles | often in `name` | `conversation.title` |
| Assets | rare | large `prod-mc-asset-server` binary tree |
| Auth/billing | n/a | separate small JSON (ignored) |
| Paper-analysis style | often framework sections | same when user asks; also long free-form teaching |

## Files written

| File | Title | Clean chars | % removed |
| --- | --- | ---: | ---: |
| `2025-02-28_i-astrophysics-and-black-holes_5d552948.md` | I - Astrophysics (and Black Holes) | 322389 | 0.0% |
| `2025-03-01_i-quantum-mechanics-quantum-field-theory_c6667db7.md` | I - Quantum Mechanics & Quantum Field Theory | 305696 | 0.6% |
| `2025-05-07_quantum-field-theory_5568829a.md` | Quantum Field Theory  | 183819 | 1.2% |
| `2025-11-08_massive-gravity-gluon-magic_a16227af.md` | Massive Gravity/Gluon Magic | 149905 | 6.5% |
| `2025-05-18_nuclear-magnetization-observation-breakthrough_d40be7a8.md` | Nuclear Magnetization Observation Breakthrough | 154747 | 0.3% |
| `2025-02-28_materials-science-semiconductors-nanostructures_afa0fe4c.md` | Materials Science (Semiconductors & Nanostructures) | 153785 | 0.5% |
| `2026-05-09_hawking-radiation-from-charged-shell_7a92c9cf.md` | -> Hawking Radiation from Charged Shell | 144267 | 0.3% |
| `2025-10-01_quark-gluon-plasma-discussion_88f679b7.md` | Quark-gluon plasma Discussion | 26105 | 0.8% |
| `2026-05-05_collapse-gravity-proper-time-uncertainty_4a24df05.md` | -> Collapse, Gravity & Proper-Time Uncertainty | 123057 | 0.1% |
| `2026-05-06_quantum-proper-time-signatures-in-ion-clocks_57902025.md` | -> Quantum Proper Time Signatures in Ion Clocks | 46560 | 0.1% |
| `2026-05-17_cluster-tunneling-forges-scalable-schr-dinger-cats_19c6e325.md` | Cluster Tunneling Forges Scalable Schrödinger Cats | 45452 | 0.0% |
| `2026-06-03_photon-truncation-creates-infinite-particle-zoo_771b4084.md` | Photon Truncation Creates Infinite Particle Zoo | 139522 | 2.0% |
| `2026-07-20_einstein-and-riemann-geometry-in-relativity_3c9369d4.md` | Einstein and Riemann Geometry in Relativity | 57488 | 0.4% |
| `2026-02-10_bec-superfluid-he4_6bdb7007.md` | BEC, superfluid He4 | 14316 | 0.2% |
| `2026-05-08_photonic-supersolid-nature-paper_1390a395.md` | -> Photonic Supersolid Nature Paper | 43583 | 1.0% |

## Notes for full extraction (pending approval)

- Full pass should use a **title + body classifier** that excludes medical/digestive, music/MSL, pure tooling (Obsidian/Grok Build), and Tesla/consumer chat.
- Many physics titles already overlap wiki topics (Hawking shell, ion clocks, cats, supersolid) — dedupe against `wiki/papers/` at ingest time, not at extract time.
- Large multi-topic mega-chats (`I - Astrophysics`, `I - QM & QFT`) may need section-splitting later; pilot keeps one file per conversation.

**STOP:** Pilot complete. Await explicit approval before full extraction.
