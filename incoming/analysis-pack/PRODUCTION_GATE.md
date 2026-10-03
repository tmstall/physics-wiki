# Production gate — when a Grok analysis may enter `incoming/md/`

Analyses that fail this gate stay in chat or in `incoming/analysis-pack/bakeoff/` as drafts. Passing analyses may be written to `incoming/md/` for Cowork **`copy`** → Grok **`ingest`**.

## Hard fails (any one blocks)

1. **Truncation** — missing sections for the chosen mode; ends mid-paragraph; placeholder “TBD” / “continued”; honesty checkpoints named but empty.
2. **Wrong posture** — explanatory fluff on an unreviewed preprint that never earned a load-bearing core (or the reverse: hostile tone instead of adversarial earning).
3. **Access laundering** — analyzed from abstract/title only without Access Status and without lite/halt as appropriate.
4. **Overclaim** — title/takeaways state a result the paper only forecasts or interprets (classic: “spin measured” when only “spin-sensitive star discovered”).
5. **Rubric zeros** on D1, D2, D4, D5, D7, or D11 (see [`RUBRIC.md`](RUBRIC.md)).
6. **Glossary-only pedagogy** — §§3–4 that define jargon and list package names without teaching intuition (the “just the facts” failure mode). D4 or D5 at 0 blocks; prefer both ≥1 with real paragraph teaching.
7. **Honesty-section telegrams** — Assumption Audit / §5 / §6 that are only short correct bullets while omitting the paper’s loudest quantitative self-critique (e.g. a >1 dex BHAD miss) or elevating novelty only as a slogan. Cap D6–D8 and rewrite before staging if denser Claude-comparable prose is missing.

## Soft requirements (fix or annotate)

- Rubric total ≥18/24 (full) or lite-rescaled equivalent; D4 ≥1 and D5 ≥1; prefer D6–D9 ≥1 with teaching-density watches, numbered falsifiable handles, and a least-confident tied to the novel claim.
- Filename convention matches pipeline: Grok → `g_YYYY-MM-DD_doi-..._slug.md` (or `g_…_arxiv-…` / `g_…_eso…`); Claude omits the `g_` prefix. Same date/id/slug shape either way.
- First line / action line includes `Framework vX.Y` for the framework version actually used (newest in `Gold\Prompts`, currently v3.12).
- Closing footer notes analyzer + date + posture (optional but preferred for provenance).
- Deep Dive Q&A (if any) lives **on this same file** via `start deep dive` / `end deep dive` — not required for gate pass; append after staging to `incoming/md/` is fine.

## Human seam

For the first **3** production Grok analyses after this pack lands, pause for a human skim of the scorecard before `copy`. After that, Grok may self-gate and drop to `incoming/md/` unless the user asks to keep pausing.

## Relation to wiki ingest

Passing this gate ≠ wiki quality. Wiki ingest still follows [`../prompts/INGEST.md`](../prompts/INGEST.md): paper page, concepts, synthesis touch, index, log. Thin or orphan-prone topics still need hub judgment at ingest time.
