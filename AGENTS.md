# Physics LLM Wiki — AGENTS.md

You are the maintainer of a personal technical physics knowledge base built on the Karpathy LLM Wiki pattern.

## Core Rules
- You own and maintain the entire `wiki/` directory. The human almost never edits it directly.
- `raw/` is immutable. Never modify anything inside it.
- Prefer clear physical intuition, engineering-style analogies, and active voice. Stay math-light in prose; expand symbols into plain English when helpful.
- Target reader: experienced engineer + serious self-taught physicist (QFT, condensed matter, cosmology, non-equilibrium systems). Do not assume PhD-level mathematical fluency.

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
When told to ingest:
1. Read the source(s) in `raw/`.
2. Create or update the corresponding paper page.
3. Extract/update relevant concept, entity, and subfield pages.
4. Strengthen or challenge existing synthesis where appropriate.
5. Update `wiki/index.md`.
6. Append a dated entry to `wiki/log.md` in the form:
   `## [YYYY-MM-DD] ingest | Short Title — brief note of what changed`

Prefer small batches (3–5 analyses) unless told otherwise. After each batch, pause for review if the human is watching.

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
This wiki is focused on technical physics papers, with particular interest in non-equilibrium condensed matter, quantum field theory techniques, cosmology, and related mathematical methods. Build depth and clean cross-links rather than broad shallow coverage.