# Analysis staging → ingest pipeline

Short stub. Full prompt text lives in `incoming/prompts/`. Bot paste packs: `incoming/bot/`.

**Wiki scope:** physics-first **and** multi-agent / collective AI (same vault). See `AGENTS.md` Current Priority. Ingest triage must not skip multi-agent papers as “non-physics islands.”

| Trigger | Where | Prompt file | Role |
| --- | --- | --- | --- |
| **Bot intake** (Android OK) | Grok Bot — Wiki Coordinator | [`bot/`](bot/) + [`prompts/COORDINATOR.md`](prompts/COORDINATOR.md) | Kickoffs + reminders only — **never** full analysis |
| **`analyze`** | Grok Build | [`prompts/ANALYZE.md`](prompts/ANALYZE.md) | Framework (newest in `Gold\Prompts`, currently v3.12) + gate; `g_` prefix; Drive sync |
| **`analyze`** | Claude Cowork | [`prompts/COWORK_ANALYZE.md`](prompts/COWORK_ANALYZE.md) | Claude analysis → `incoming/md/YYYY-MM-DD_…` |
| **`compare`** | Build and/or Bot | [`prompts/COMPARE.md`](prompts/COMPARE.md) | Rubric scorecard; human picks wiki source |
| **`start deep dive` / `end deep dive`** | Grok Build | [`prompts/DEEP_DIVE.md`](prompts/DEEP_DIVE.md) | Append Q&A on `incoming/md/` file; Drive sync on end |
| **`copy`** | Claude Cowork | [`prompts/COPY.md`](prompts/COPY.md) | Stage inbox → `raw/analyses/` + archive + READY_QUEUE |
| **`ingest`** | Grok Build | [`prompts/INGEST.md`](prompts/INGEST.md) | Queue batches of 5; light lint @10; full lint at end |

## Analyzer modes (A–D)

| Mode | Writers | Filenames |
| --- | --- | --- |
| **A** Claude only | Claude (Android OK) | `YYYY-MM-DD_…` |
| **B** Grok only | Build (desktop) | `g_YYYY-MM-DD_…` |
| **C** Both | Claude + Build | both in inbox |
| **D** Compare | scorecard → human choice | both kept in `raw/`; **one** wiki page |

Unspecified mode: **ask** (no silent default yet). Posture/lite: blank unless user stated. Inbox notify threshold: **5** (learning).

## Paths (source of truth)

| Path | Role |
| --- | --- |
| `incoming/md/*.md` | Drop zone (root only). Claude: `YYYY-MM-DD_…`; Grok: `g_YYYY-MM-DD_…` |
| `incoming/md/archive/` | After successful `copy` |
| `raw/analyses/` | Immutable ingest input |
| `incoming/READY_QUEUE.md` | Written by `copy`; consumed by `ingest` |
| `incoming/analysis-pack/` | Framework, golds, rubric, gate, bakeoffs |
| `incoming/bot/` | Grok Bot profile/skills paste packs (Wiki) |
| `G:\My Drive\Technical Papers\Analyses\` | Drive mirror of analyses + `_PIPELINE_STATUS.md` |
| `incoming/_PIPELINE_STATUS.md` | Local status card (never under `incoming/md/`) |
| `wiki/` | Build-owned |
| `C:\Users\tmsta\Documents\MSL\` | **Separate** MSL project (not this vault) |

## Human seam

1. **Bot** (optional): intake on phone → kickoff(s); ask to queue Build if wanted.
2. **Claude** and/or **Build** `analyze` → files in `incoming/md/` (+ Drive for Grok).
3. Optional: Build deep dive; Bot/Build **`compare`** if twins exist → human picks wiki source.
4. Cowork **`copy`** (Bot may remind at ≥5 files — never copies itself).
5. Build **`ingest`**.
6. Pause tokens: `continue` / `next` / `stop` / `lint now` / `skip <file>`.

Cowork must **not** auto-start Build. Build must **not** modify `raw/` (except reading). Bot must **not** analyze, copy, or ingest. Grok `analyze` / deep dive must **not** auto-`copy` / auto-`ingest`.

### Dual analyses (Mode C/D)

Both Claude and `g_` files may sit in `raw/analyses/`. Ingest creates **one** paper page per DOI/slug unless the user chooses merge. **Prompt** which analysis owns the wiki page (`use A` / `use B` / `merge deep dives` / `defer`) — scorecard from `COMPARE.md` informs the choice.

## Defaults

- READY_QUEUE: Markdown
- Raw collision: skip + warn
- Empty queue ingest: fall back to not-yet-ingested `raw/analyses/`
- Intermediate lint: light @10 successes; final: full AGENTS lint
- Batch size: 5

## Wire-up

1. **Grok Bot** — create Wiki Coordinator from `incoming/bot/`; see `SETUP_CHECKLIST.md`.
2. **Claude Cowork** — bind `copy` → `COPY.md`; bind `analyze` → `COWORK_ANALYZE.md`.
3. **Grok Build** — `analyze` / `ingest` / `compare` / deep dive via `AGENTS.md` + prompts.
4. **MSL** — separate Bot + `Documents\MSL\docs\bot\`; never merge with this pipeline.
