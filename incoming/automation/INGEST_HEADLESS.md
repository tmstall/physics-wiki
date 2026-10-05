# Headless wiki ingest (Phase 4)

Used by incoming/automation/ingest-wiki.ps1. Canonical human/Build prompt remains incoming/prompts/INGEST.md. This file only overrides the interactive seams for a non-interactive Grok CLI run.

## Task

Run a full **ingest** of every pending row in incoming/READY_QUEUE.md (already staged into 
aw/analyses/). Follow incoming/prompts/INGEST.md and repo-root AGENTS.md for wiki structure, page conventions, duplicate detection, batch size 5, lint cadence, and style.

## Headless overrides (required)

1. **No pauses.** Do **not** wait for continue / 
ext / human review. After every batch summary and after every lint, immediately continue to the next step until the queue is empty and the final full lint is done.
2. **No triage stop.** Treat the trigger as ingest all / 
o triage. Skip the optional pre-ingest triage STOP.
3. **Batch size** remains 5 unless the queue has fewer.
4. **Twins / wiki source (this run, no human prompt):**
   - One wiki paper page per DOI / arXiv id.
   - If both a normal analysis and a sonnet_* twin exist for the same paper: use the **non-sonnet_** file as source_analysis; mark the twin READY_QUEUE row done with note 	win kept in raw; wiki from <chosen-basename>.
   - If both a normal analysis and a *_plain.md twin exist for the same paper: use the **_plain** file as source_analysis (plain-language rewrite); mark the other done with note 	win kept in raw; wiki from <chosen-basename>.
   - If a matching wiki/papers/ page already exists (DOI/arXiv/title): mark skipped_duplicate and do **not** create a second paper page. Optionally strengthen the existing page only if the new analysis adds clear Deep Dive material the page lacks; otherwise skip.
5. **Never modify 
aw/.** Never delete analyses. Update READY_QUEUE statuses (done / skipped_duplicate / ailed) as you go.
6. **Figures:** analyses may embed igures/<file> relative to 
aw/analyses/ (files live in 
aw/analyses/figures/). Wiki paper pages stay text/wikilink-first like existing pages; do not invent a new figure layout.
7. **Lint:** light lint after every 10 successful new/updated paper pages; full AGENTS lint when the queue is empty. If the final success lands on a 10-boundary, run one **full** lint only. Write LINT_REPORT_YYYY-MM-DD.md at repo root for the final lint (today is 2026-10-05). Append a lint line to wiki/log.md.
8. **Status card:** when finished, update incoming/_PIPELINE_STATUS.md (updated_at, inbox_count_incoming_md_root, READY_QUEUE pending, last_ingest, brief 
otes). Do not place status files under incoming/md/.

## Work order

1. Read AGENTS.md, incoming/PIPELINE.md, incoming/prompts/INGEST.md, current incoming/READY_QUEUE.md, and skim wiki/index.md + recent wiki/log.md for catalog counts and duplicate cues.
2. Build the queue from READY_QUEUE pending rows (preferred). Resolve each to 
aw/analyses/<filename>.
3. Ingest in batches of 5: create/update wiki/papers/, multi-paper concept hubs only, synthesis only when warranted, update wiki/index.md, append wiki/log.md, update READY_QUEUE rows.
4. Print each batch summary in the INGEST.md table format (also fine to write incoming/automation/scratch/ingest-batch-K.md).
5. After all pending work: full lint + LINT_REPORT + status card.
6. Final reply must include:
   - Papers ingested (count + wiki slugs)
   - Pages created vs updated vs skipped (with reasons)
   - Concepts/synthesis touched
   - Catalog before/after counts
   - Any failures

## Hard rules

- Follow existing wiki page shape (YAML frontmatter with source_analysis, one-line summary, Key claims, Physical intuition, Limitations, Connections, Source). Match nearby pages; do not invent a new structure.
- Prefer clear physical intuition, active voice, math-light prose (AGENTS.md).
- Multi-agent / collective-AI papers are in-scope.
- Do not edit .gitignore, Obsidian workspace files, or unrelated dirty files.
- Do not commit or push (the wrapper script handles git).
