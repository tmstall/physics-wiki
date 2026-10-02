# Grok Build / Bot prompt — trigger: `compare`

**Purpose:** Score two analyses of the **same paper** (usually Claude + Grok `g_`) with the analysis-pack rubric so the human can choose which feeds the wiki paper page (or what to merge).

Works in:
- **Grok Build** — full compare when both files are in the repo / attached
- **Wiki Bot** — lighter scorecard when both files are attached or readable from Drive; same anti-paraphrase rules

---

## Hard rules

1. **Do not rewrite** either analysis into a third “merged” manuscript unless the user explicitly asks for a merge draft **after** scores.
2. **Anti-paraphrase:** treating one file as gold means extract **gap labels** only — never paste or lightly edit the other prose into a “fix.”
3. Output a **scorecard**, not a new §§1–9 spine.
4. End with an explicit **recommendation prompt** for the human: which file should own `wiki/papers/…` (Claude / Grok / merge deep dives / defer).

---

## Inputs

- Path or attachment A (often Claude `YYYY-MM-DD_…`)
- Path or attachment B (often Grok `g_YYYY-MM-DD_…`)
- Optional: paper PDF/DOI if needed to settle factual disputes (do not re-analyze from scratch unless asked)

---

## Procedure

1. Confirm both are analyses of the **same** DOI/arXiv/title. If not, stop.
2. Load themes from `incoming/analysis-pack/RUBRIC.md` and fail conditions from `PRODUCTION_GATE.md` (Build should read files; Bot may use a compressed rubric list if files are attached).
3. For each dimension, score A and B separately with **one-line evidence** (quote location / section heading — not a paraphrase rewrite).
4. Call out:
   - Explanatory flow (§§2–4 teach before jargon?)
   - Assumption Audit density
   - Framework/acronym first-use
   - §5 / §6 honesty density
   - Truncation / missing sections
5. Totals + **which is stronger overall** and **which is stronger for wiki ingest** (may differ if one is denser but less accurate).
6. **Ask the human** which to use for the wiki page. Do not auto-ingest.

---

## Output shape

```markdown
## Compare scorecard — <short title>
**A:** <filename> (Claude|Grok|other)
**B:** <filename>
**DOI/arXiv:**

| Dimension | A | B | Note |
| --- | --- | --- | --- |
| … | /2 | /2 | … |

**Totals:** A x/24 · B y/24
**Stronger pedagogy:** …
**Stronger honesty/density:** …
**Factual concerns:** …

### Wiki decision (human required)
Reply with one of:
- `use A` — wiki paper from A; keep B in raw only
- `use B` — wiki paper from B; keep A in raw only
- `merge deep dives` — base page from A|B; fold listed Deep Dive sessions from the other
- `defer` — leave both in raw; no wiki change yet
```

---

## After human chooses

- **Build ingest:** follow `INGEST.md` duplicate/`g_` policy; only create/update one paper page.
- **Bot:** record the choice in-thread; remind user to tell Build at ingest time if not ingesting now.
