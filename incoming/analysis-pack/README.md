# Grok analysis-quality pack

Raise Grok paper analyses to the same **structural honesty and completeness** bar as the best Claude (Cowork) analyses under the current Framework (newest in `C:\Users\tmsta\Desktop\Gold\Prompts`, currently **v3.15**) — without training Grok to mimic Claude’s voice.

## What this pack is

| Piece | Role |
| --- | --- |
| `C:\Users\tmsta\Desktop\Gold\Prompts\Academic Paper Analysis Framework v*.md` (newest version; currently v3.15) | Canonical analysis contract (sections, checkpoints, posture, lite mode, depth target, claim check, referee pass) |
| [`Academic_Paper_Analysis_Framework_v3_10.md`](Academic_Paper_Analysis_Framework_v3_10.md) | **Historical** v3.10 copy, kept for reference only — not canonical |
| [`prompts/ANALYZE.md`](../prompts/ANALYZE.md) | Grok Build trigger: **`analyze`** — output contract + anti-truncation |
| [`GOLD_EXEMPLARS.md`](GOLD_EXEMPLARS.md) | Four Claude gold analyses + **exemplar cards** (what to emulate structurally) |
| [`RUBRIC.md`](RUBRIC.md) | Scoring dimensions for bakeoffs and production gate |
| [`exemplars/`](exemplars/) | Copies of the four gold markdown analyses (reference only) |
| [`bakeoff/`](bakeoff/) | Phase 0/3 bakeoff artifacts (S301) |
| [`PRODUCTION_GATE.md`](PRODUCTION_GATE.md) | When an analysis is allowed into `incoming/md/` |

## What this pack is *not*

- **Not a training set.** Do not paste whole gold analyses into the model context and ask it to “write like these.” Gold files fuel the **rubric** and exemplar cards: checkpoints present, depth, honesty, anti-truncation.
- **Not a Cowork replacement for copy/ingest.** Staging and wiki ingest stay on `copy` / `ingest` ([`PIPELINE.md`](../PIPELINE.md)).
- **Not the Grok Bot.** Mobile coordination / kickoffs / compare *requests* live in [`../bot/`](../bot/) and [`../prompts/COORDINATOR.md`](../prompts/COORDINATOR.md). Build-side compare: [`../prompts/COMPARE.md`](../prompts/COMPARE.md) or `/wiki-compare`.

## How to run an analysis (Grok Build)

1. Read [`../prompts/ANALYZE.md`](../prompts/ANALYZE.md) (or say **`analyze`** if bound).
2. Load the current Framework: the newest `Academic Paper Analysis Framework v*.md` in `C:\Users\tmsta\Desktop\Gold\Prompts` (currently v3.15).
3. Optionally skim **one** exemplar **card** in `GOLD_EXEMPLARS.md` matching the paper type — not the full gold markdown unless debugging a failed bakeoff.
4. Produce the full 9-section analysis (or lite when appropriate).
5. Self-check against the anti-truncation checklist in `ANALYZE.md`.
6. Score with [`RUBRIC.md`](RUBRIC.md). Pass [`PRODUCTION_GATE.md`](PRODUCTION_GATE.md) before writing to `incoming/md/` as **`g_YYYY-MM-DD_…md`**.

## Deep dives (Obsidian-restartable)

Any analysis in `incoming/md/` can take live Q&A:

1. `start deep dive '<analysis file name>'` — opens/resumes a session and lists **remaining** `## Deep Dive candidates` (`- [ ]` only), if any.
2. Pick a candidate by number **or** ask your own question — each Q&A is **appended** under `## Deep Dive — … (session N)`; answered candidates flip to `- [x]`.
3. `end deep dive` — marks the session closed **and re-syncs** the file to Google Drive `Technical Papers/Analyses`.
4. Later `start deep dive` on the same file resumes an open session or starts session N+1 (history concatenates).

Candidates themselves are **optional** at analyze time (theory / modular / compressed-derivation papers). Full protocol: [`../prompts/DEEP_DIVE.md`](../prompts/DEEP_DIVE.md). Never writes `raw/`.

**Drive path:** `G:\My Drive\Technical Papers\Analyses\` (Drive for Desktop). Gated analyses are copied there when finished so Obsidian on a tablet can open them without waiting for wiki `copy`/`ingest`.

## Phase status

| Phase | Status | Notes |
| --- | --- | --- |
| Pack scaffold (framework + gold + ANALYZE + rubric + gate) | **Done** | This folder |
| Phase 0/3 bakeoff #1 (S301 vs Claude gold) | **PASS** | [`bakeoff/SCORECARD_s301.md`](bakeoff/SCORECARD_s301.md) — 24/24 |
| Phase 0/3 bakeoff #2 (relative entropy → Einstein) | **PASS** | [`bakeoff/SCORECARD_relative-entropy-einstein.md`](bakeoff/SCORECARD_relative-entropy-einstein.md) — 24/24; deep-dive covers user Qs (Claude still max pedagogy) |
| Tighten pack from bakeoff gaps | **Done** | ANALYZE lessons: posture drift, forecast≠measurement, theory proven/imported/assembled, optional deep-dive appendix |
| Production use | **Ready** (human skim first 3) | Drop gated analyses into `incoming/md/`, then `copy` → `ingest` |
