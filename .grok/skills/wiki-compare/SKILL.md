---
name: wiki-compare
description: Compare two Physics Wiki paper analyses (usually Claude vs Grok g_) with the analysis-pack rubric and prompt which file should own the wiki page. Use when the user says compare, bakeoff, Mode D, or which analysis for wiki, or runs /wiki-compare.
---

# Wiki compare

Follow **`incoming/prompts/COMPARE.md`** in full.

Hard rules:
- Scorecard only — do not rewrite either analysis into a third manuscript.
- Anti-paraphrase: gap labels / evidence pointers, not sentence mimicry.
- End by asking: `use A` | `use B` | `merge deep dives` | `defer`.
- Do not auto-ingest or modify `raw/`.
