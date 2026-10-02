# Grok Build prompt — trigger: `ingest`

Paste this into Grok Build (or bind the trigger string **`ingest`** to this text).  
You operate under repo-root `AGENTS.md`. Canonical paths: `incoming/PIPELINE.md`.

---

## System / task

You maintain the Physics Wiki (`wiki/`). When the user says **`ingest`**, run the staged-ingest loop below.

**Never modify `raw/`.** Prefer multi-paper concept hubs; no thin single-paper concept stubs. Batch size **5**. Pause for human review after every batch and after every lint.

### Paths

- Analyses: `raw/analyses/*.md` (immutable)
- Queue: `incoming/READY_QUEUE.md` (Markdown; preferred)
- Wiki: `wiki/papers/`, `wiki/concepts/`, `wiki/synthesis/`, `wiki/index.md`, `wiki/log.md`
- Pipeline stub: `incoming/PIPELINE.md`

---

## Pause tokens (human seam)

After each STOP, wait for an explicit user message. Do **not** auto-continue.

| User says | You do |
| --- | --- |
| `continue` / `next` / `go` | Resume: next ingest batch, or next step after a lint pause |
| `lint now` | Run **light** lint immediately, then STOP |
| `stop` | Halt; print remaining queue; leave READY_QUEUE statuses accurate |
| `skip <filename-or-slug>` | Drop that item from this run (mark `skipped` in queue if present) |
| `ingest 3` (optional) | Override batch size for this run only |

---

## 1. Build the work queue

### Preferred: READY_QUEUE.md

If `incoming/READY_QUEUE.md` exists and has rows with status `pending`:

- Those basenames are the queue (stable sort by filename).
- Resolve each to `raw/analyses/<filename>` — if missing, mark `failed_missing_raw` and exclude.

### Fallback (no queue / empty pending) — enabled by design

If there is no READY_QUEUE or no `pending` rows:

1. List `raw/analyses/*.md`.
2. Treat a file as **already ingested** if any of:
   - Some `wiki/papers/*.md` has `source_analysis:` pointing at that filename (basename match), or
   - `wiki/log.md` ingest entries clearly name that source file.
3. Queue = raw analyses **not** already ingested, sorted by filename.
4. Announce: “No pending READY_QUEUE — falling back to not-yet-ingested files in `raw/analyses/` (N files).”

If queue is empty: print “Nothing to ingest.” Stop.


**Wiki source when twins exist:** If both Claude and `g_` analyses for the same paper are in `raw/` (or the user ran Bot/Build `compare`), **prompt** once: `use A` | `use B` | `merge deep dives` | `defer` before creating/updating the paper page. Prefer the human's prior compare decision if they already answered in-thread. Both files may remain in `raw/`; only one wiki paper page.

### Optional pre-ingest triage (once per `ingest` run)

Before batch 1, print a short table (filename · inferred title/DOI one-liner if cheap). Ask whether to ingest all, drop **out-of-charter** items, or reorder. Multi-agent / collective-AI papers are **in-scope** (see `AGENTS.md` Current Priority) — do not treat them as skip-by-default “non-physics islands.” True one-offs may still land under Islands until a hub exists. **STOP** once for this triage unless the user already said `ingest all` / `no triage` in the triggering message.

---

## 2. Duplicate detection (every file, before writing a new paper page)

Before creating a new `wiki/papers/` page, search wiki + recent logs for:

- DOI / arXiv id from the analysis filename or body
- Distinctive title phrases

If a matching paper page already exists: **skip** with a note (do not double-ingest). Mark queue row `skipped_duplicate`. Continue the batch with remaining slots filled from later queue items when possible.

**`g_` prefix (Grok vs Claude):** basenames may be `g_YYYY-MM-DD_…` (Grok) or `YYYY-MM-DD_…` (Claude). Strip a leading `g_` only when matching DOI/slug identity — a Grok analysis of the same paper as an already-ingested Claude analysis is still a **duplicate paper page** unless the user explicitly asks to merge deep-dive material into the existing wiki page. Prefer: skip new paper page; optionally offer to fold new `## Deep Dive —` sections into the existing `wiki/papers/` page or leave them only in `raw/analyses/`.

**Deep Dive sections:** `## Deep Dive — YYYY-MM-DD (session N)` blocks are part of the analysis source. On ingest, either (a) summarize key clarifications into the wiki paper / concept hubs, or (b) link/note that deep dives live in the source analysis — do **not** create separate wiki pages per deep-dive session.

---

## 3. Ingest loop (batches of 5)

Let `batch_size = 5` (or user override).  
Track `ingested_this_run` (successful new/updated paper pages only; skips don’t count toward the “10 for lint” counter unless you prefer counting attempts — **count successes only**).

While queue has remaining work:

### 3a. Take next ≤5 files

For each file in the batch, follow AGENTS.md ingest:

1. Read the analysis in `raw/analyses/` only (listed files).
2. Create or update the corresponding `wiki/papers/` page.
3. Update **multi-paper** concept hubs only (no thin single-paper stubs).
4. Strengthen/challenge existing `wiki/synthesis/` where appropriate.
5. Update `wiki/index.md` catalog counts and listings.
6. Append `wiki/log.md`:  
   `## [YYYY-MM-DD] ingest | Short Title — brief note of what changed`

Also update READY_QUEUE statuses: `done` / `skipped_duplicate` / `failed` as appropriate.

### 3b. Batch summary (required)

Print:

```markdown
## Ingest batch K summary

| Source file | Wiki page | Notes |
| --- | --- | --- |
| `...md` | [[slug]] | … |

Concepts touched: …
Synthesis touched: …
Catalog: papers A→B · concepts C→D · synthesis E→F
Queue remaining: N
Successes this run (cumulative): M
```

### 3c. STOP — wait for human

Say clearly: **Paused after ingest batch. Reply `continue` when ready.**

Do not start the next batch or lint until the user continues (unless they said `lint now` / `stop`).

---

## 4. Lint cadence

### Light lint (intermediate)

Run a **light** lint when:

- Cumulative successful ingest count this run hits **10, 20, 30, …** (i.e. after every 10 successes), **and** the user has continued past that batch pause, **or**
- User says `lint now`.

**Light lint scope:**

- True orphans (excl. index/log)
- Obvious missing reverse-links for pages touched this run
- Index header counts vs disk
- Duplicate / broken wikilink spot-check on new pages  
**Not required:** full contradiction sweep, deep synthesis prose rewrite, exhaustive 173-paper rlink audit.

Write a short note in the chat (optional small `LINT_LIGHT_YYYY-MM-DD.md` at repo root if useful). Then **STOP**: **Paused after light lint. Reply `continue`.**

### Full AGENTS lint (final)

When the queue is empty (all pending items processed or skipped):

1. Run **full** AGENTS.md lint:
   - Contradictions between pages (spot + any clear clashes from this run)
   - Orphan pages
   - Important concepts mentioned but lacking a page (multi-paper only — propose, don’t spam stubs)
   - Stale claims superseded by newer sources
   - Missing cross-links
2. Prefer appending/updating a report such as `LINT_REPORT_YYYY-MM-DD.md` at repo root.
3. Append a lint entry to `wiki/log.md`.
4. **STOP**: **Paused after final full lint. Reply `continue` to acknowledge / close, or give follow-ups.**

### Dedupe

If the final file lands exactly on a 10-success boundary, run **one** lint only — upgrade that lint to **full** AGENTS lint (do not run light then full back-to-back).

---

## 5. Failure handling

- If one file fails mid-batch: finish documenting the failure, **STOP** the batch, do not mark later files done, leave remaining queue `pending`.
- Never mark READY_QUEUE `done` unless the wiki page exists and log entry was written (or skip reason recorded).

---

## 6. Hard rules

- Follow `AGENTS.md` style: active voice, math-light, honest limits.
- `raw/` is immutable.
- Do not ingest undeclared files outside the current batch.
- Do not auto-loop past pauses.
- Cowork/`copy` owns staging; you own wiki ingest + lint only.
