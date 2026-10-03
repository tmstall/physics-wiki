# Physics LLM Wiki — AGENTS.md

You are the maintainer of a personal technical knowledge base built on the Karpathy LLM Wiki pattern. The vault began as a **physics** wiki and remains physics-first; it also holds an explicit **multi-agent / collective AI** cluster in the same vault (one compounding graph, not a second wiki).

## Core Rules
- You own and maintain the entire `wiki/` directory. The human almost never edits it directly.
- `raw/` is immutable. Never modify anything inside it.
- Prefer clear physical intuition, engineering-style analogies, and active voice. Stay math-light in prose; expand symbols into plain English when helpful.
- Target reader: experienced engineer + serious self-taught physicist (QFT, condensed matter, cosmology, non-equilibrium systems), plus the same reader following multi-agent / collective-behavior papers. Do not assume PhD-level mathematical fluency.
- Do **not** force fake physics metaphors onto multi-agent papers. Cross-link where analogies earn their keep; otherwise keep the cluster’s own vocabulary.

## Directory Structure

physics-wiki/
├── raw/
│   ├── analyses/          ← existing paper analyses (primary input)
│   ├── papers/            ← original PDFs or clean markdown if available
│   └── assets/
├── wiki/
│   ├── index.md           ← master catalog (always keep current)
│   ├── log.md             ← append-only activity log
│   ├── papers/            ← one page per important paper
│   ├── concepts/          ← physical concepts, methods, frameworks
│   ├── entities/          ← key people, experiments, models, theorems
│   ├── subfields/         ← QFT, condensed matter, cosmology, quantum chemistry, etc.
│   └── synthesis/         ← higher-level reviews, tensions, open questions
└── AGENTS.md              ← this file


## Page Conventions
Every wiki page should have:
- Clear title
- One-sentence summary at the top
- YAML frontmatter when useful (`tags`, `last_updated`, `related_papers`, `status`)
- Bidirectional `[[wikilinks]]`
- Explicit notes when a new source strengthens, weakens, or contradicts earlier claims

### Paper pages (`wiki/papers/`)
- Key claims and results (in plain language first)
- Physical intuition / what the result actually means
- Limitations and assumptions
- How it connects to other papers and concepts already in the wiki
- Open questions it raises

### Concept pages (`wiki/concepts/`)
- Clear definition + physical picture
- Key results and methods associated with it
- Important tensions or unresolved issues
- Links to the papers that most strongly shape the current understanding

## Standard Operations

### Ingest
When the user says **`analyze`** (or clearly means a Framework paper analysis), follow **`incoming/prompts/ANALYZE.md`** in full — current Framework contract (newest `Academic Paper Analysis Framework v*.md` in `C:\Users\tmsta\Desktop\Gold\Prompts` (currently v3.15)), anti-truncation, rubric self-score, production gate before `incoming/md/`. Grok analyses use the `g_` filename prefix. Quality pack: `incoming/analysis-pack/`. Headless Claude Code runs follow `incoming/automation/ANALYZE_HEADLESS.md`. See also `incoming/PIPELINE.md`.

When the user says **`start deep dive`** / **`end deep dive`** (or clearly means that session), follow **`incoming/prompts/DEEP_DIVE.md`** in full — append Q&A onto the analysis file in `incoming/md/` (never `raw/`); concatenate multiple sessions; resume open sections for Obsidian restarts.

When the user says **`ingest`** (or clearly means the staged ingest run), follow **`incoming/prompts/INGEST.md`** in full — queue/READY_QUEUE handling, batches of 5, human pause tokens, light lint every 10 successes, full AGENTS lint at end. See also `incoming/PIPELINE.md`.

When the user says **`compare`** (two analyses of the same paper, or clearly a bakeoff/wiki-source choice), follow **`incoming/prompts/COMPARE.md`** — rubric scorecard only; anti-paraphrase; prompt `use A` / `use B` / `merge deep dives` / `defer`. Do not auto-ingest the winner.

### External coordinator (Grok Bot)
Mobile / chat **coordination** may come from the grok.com **Physics Wiki Coordinator** Bot (`incoming/bot/`, contract `incoming/prompts/COORDINATOR.md`). That Bot emits **kickoffs and reminders only** — it must **not** write Framework analyses, edit `wiki/`, touch `raw/`, or run `copy`/`ingest`. Analysis remains **Claude** and/or **Grok Build**. Analyzer mode A–D: ask if unspecified. Inbox notify threshold while learning: **5**. Dual analyses: both may live in `raw/`; human chooses which owns the wiki page (scorecard optional). MSL / Tesla music is a **separate** project under `Documents/MSL/` — never merge into this vault.

Core wiki work each batch still does:
1. Read the source(s) in `raw/analyses/` (only the current batch).
2. Create or update the corresponding paper page.
3. Extract/update relevant concept, entity, and subfield pages (multi-paper hubs; no thin single-paper stubs).
4. Strengthen or challenge existing synthesis where appropriate.
5. Update `wiki/index.md`.
6. Append a dated entry to `wiki/log.md` in the form:
   `## [YYYY-MM-DD] ingest | Short Title — brief note of what changed`

Never modify `raw/`. Prefer small batches (default 5). After each batch and after each lint, pause for review when the human is watching.

### Query
Answer from the wiki first. Cite specific pages. When an answer is valuable, offer to file it back into `wiki/synthesis/` or the relevant concept page.

### Lint
On request, scan for:
- Contradictions between pages
- Orphan pages
- Important concepts mentioned but lacking their own page
- Stale claims superseded by newer sources
- Missing cross-links

## Style Constraints
- Active voice only.
- Math-light: prioritize physical meaning and intuition.
- Use vivid analogies from engineering, computer architecture, networking, or everyday systems when they clarify.
- Be precise about claims and limitations. Do not overstate certainty.
- Keep the wiki coherent and compounding — every ingest should leave it more useful than before.

## Math Formatting Rules

When writing or updating any page in this wiki:

- Prefer simple, clean math notation that renders well in Obsidian.
- Use `$ ... $` for inline math and `$$ ... $$` for display math.
- Good examples:
  - `$r_{\pm} = M \pm \sqrt{M^{2} - Q^{2}}$`
  - `$\delta$`, `$z \sim 7$`, `$J_0/U \approx 1$`
- Avoid:
  - Broken/escaped LaTeX such as `r\_\{\\pm\}`
  - Duplicated or mangled expressions that mix Unicode + escaped TeX
  - Overly complex LaTeX that is hard to read in raw Markdown
- When in doubt, prefer clear Unicode (e.g. `r± = M ± √(M² − Q²)`) over complicated markup.
- The goal is readability first, both in raw Markdown and in Obsidian’s rendered view.

## Current Priority
**Physics-first, wider than physics-only.** Primary focus remains technical physics — non-equilibrium condensed matter, QFT techniques, cosmology, nuclear/dense matter, ultrafast/AMO, gravity and multimessenger threads, and related mathematical methods.

**Also in-scope (same vault):** multi-agent systems and collective AI — LLM population conventions, coordination / majority effects, large-scale agent social simulators, and closely related complex-adaptive-systems work. Index these under the first-class **Multi-agent systems & collective AI** section, not as permanent “non-physics islands.”

**Still use Islands** for true one-offs that lack a topical home (e.g. some Earth-system or mission-concept papers) until enough related papers exist to graduate them. Prefer depth and clean cross-links over broad shallow coverage in every cluster.

**Mobile coordination:** Grok Bot (Wiki Coordinator) may start intake from Android; analysis still Build/Claude. See `incoming/prompts/COORDINATOR.md`.

### Island graduation policy
An Islands shelf (or singleton) **graduates** to a first-class `wiki/index.md` section when **all** of:
1. **≥2–3 related papers** (or one paper + a clear multi-paper concept hub) share a reader question.
2. That question is **not already owned** by an existing top-level section / synthesis (otherwise fold there).
3. You can name the section in plain language without forcing a fake physics metaphor.

**Audit, then move** — propose graduations in chat / log; do not silently mass-migrate. Singletons (one paper, no cousins) stay Islands. Large Islands *subsections* that already behave like mini-catalogs (e.g. chemistry, plasma HED, HEA paper lists) are prime graduation candidates.