# Paper-analysis automation pipeline config

```yaml
ingest_threshold: 10
framework_source_dir: C:\Users\tmsta\Desktop\Gold\Prompts
canonical_framework_rule: newest 'Academic Paper Analysis Framework v*.md' in framework_source_dir, by version number (numeric compare)
canonical_framework: C:\Users\tmsta\Desktop\Gold\Prompts\Academic Paper Analysis Framework v3.15.md   # current as of 2026-10-03
canonical_framework_sha256: 605AF9B29439994DF943ECFEF39627799B7B73FC35833CE435BEFBAA7CB8757A
analysis_runner: Claude Code (bundled with Claude Desktop) on laptop
delivery:
  - incoming\md
  - G:\My Drive\Technical Papers\Analyses
  - incoming\automation\papers-analyzed-log.md   # papers-analyzed log in repo (created in Phase 3)
picks: 4-5 per request
to_read_dir: G:\My Drive\To Read   # every delivered analysis (.md + figures/) is also copied here for phone/tablet reading
to_read_retention_days: 14   # prune-to-read.ps1 deletes .md files older than this (LastWriteTime) and unreferenced figures
phases_status:
  phase_0: done 2026-10-02
  phase_2: done 2026-10-02 (headless test runs, scratch only)
  phase_3: built 2026-10-03 (live delivery, queue, scheduled task, deep dives)
```

## Notes (Phase 0)

- Canonical framework = Gold\Prompts v3.11 (.md, 2026-09-19 23:22 PT). Desktop copy is byte-identical.
- Stale: `Claude outputs\Academic_Paper_Analysis_Framework_v3_11.md` (different hash, earlier draft/encoding) and `incoming\analysis-pack\Academic_Paper_Analysis_Framework_v3_10.md` (v3.10).
- Files still pinned to v3.10: AGENTS.md:54, incoming\PIPELINE.md:10, incoming\prompts\ANALYZE.md, incoming\analysis-pack\{README,RUBRIC,PRODUCTION_GATE,GOLD_EXEMPLARS}.md.
- 5-paper batch/pause rule: incoming\prompts\INGEST.md:12,33,83-126; AGENTS.md:58,74; incoming\PIPELINE.md:15,64.

## Notes (framework switch, 2026-10-02)

- Canonical framework is now v3.12 (Gold\Prompts, 2026-10-02). v3.11 stays in Gold\Prompts as history.
- ANALYZE_HEADLESS.md resolves the newest `Academic Paper Analysis Framework v*.md` in Gold\Prompts by version number, so future versions are picked up without edits; the rules now inside the framework (depth target, full-paper reading, claim check, consistency sweep, referee pass) were removed from ANALYZE_HEADLESS.md.
- The v3.10 pins listed in the Phase 0 notes (AGENTS.md, PIPELINE.md, ANALYZE.md, analysis-pack README/RUBRIC/PRODUCTION_GATE/GOLD_EXEMPLARS) now point to the newest framework in Gold\Prompts (currently v3.12). `incoming\analysis-pack\Academic_Paper_Analysis_Framework_v3_10.md` is kept as a historical copy.

## Notes (Phase 3, 2026-10-03)

- One command: `incoming\automation\analyze-paper.ps1 <arXiv ID | DOI | URL> [-Title]`; delivery is done by the script (Claude writes only to `scratch\work\<run>\`). See `incoming\automation\README.md`.
- Queue: `incoming\automation\queue\` + scheduled task `PhysicsWiki-PaperQueue` (logon, wake from sleep, every 30 min); Drive inbox `G:\My Drive\Technical Papers\Queue\`.
- PDFs: no pandoc/LaTeX on the laptop, so PDFs are built on the box from `queue\pdf-todo.txt`.
- Deep dives: `deep-dive.ps1` -> `incoming\deep-dives\` + `G:\My Drive\Technical Papers\Deep Dives\`.

## Notes (framework v3.13 + figures, 2026-10-03)

- Canonical framework is now v3.13 (Gold\Prompts, 2026-10-03): Key Figures rule, optional ASCII concept diagram, a shorter explanatory Claim Check (~400-800 words), consistency check reports significant findings only. v3.12 stays in Gold\Prompts as history. The "currently v3.x" pointers (AGENTS.md, PIPELINE.md, ANALYZE.md, analysis-pack) now say v3.13.
- Figures: analyze-paper.ps1 extracts figures before the Claude run (arXiv source tarball first, then pdftoppm page renders, then pdfimages) into scratch\work\<run>\figures\ with a FIGURES.md manifest; Claude embeds its picks as figures/<prefix>_figN.png; delivery copies the embedded files to incoming\md\figures\ and Drive Analyses\figures\ and commits them. See README.md "Figures".
- Re-runs: analyze-paper.ps1 -Replace overwrites the existing incoming\md analysis (same file name), replaces its papers-log row (note "re-run <date>, framework vX.Y") and commits as "Replace analysis".

## Notes (framework v3.14, 2026-10-03)

- Canonical framework is now v3.14 (Gold\Prompts, 2026-10-03): length target about 5,000-7,500 words (was 5,000-9,500); Sections 3-4 explain first, then support (plain words, then key numbers / a table / a figure), only the few equations that carry the main result, derivations in a short optional appendix or cut; the v3.12 'do not compress Sections 3-4' rule removed; Claim Check hard cap 800 words, results and meaning only. Everything else unchanged from v3.13. v3.13, v3.12 and v3.11 stay in Gold\Prompts as history. The 'currently v3.x' pointers (AGENTS.md, PIPELINE.md, ANALYZE.md, analysis-pack, automation README, ANALYZE_HEADLESS.md) now say v3.14.

## Notes (framework v3.15, 2026-10-03)

- Canonical framework is now v3.15 (Gold\Prompts, 2026-10-03): protected 'Origins & Big Picture' subsection in Section 3 (~400-700 words, e.g. DNS formation: recycling, Case BB, ultra-stripped supernovae) that the length limits do not cut; no math appendix (derivations cut, not moved); physics before forecasts (explain the phenomenon, then a short plain-language note on difficulty, no exponents or error budgets); significant findings always reported in plain words, never trimmed; parameter tables cut to the 4-6 numbers that matter; total target still ~5,000-7,500 words. v3.14 and earlier stay in Gold\Prompts as history. The 'currently v3.x' pointers now say v3.15.

## Notes (To Read folder, 2026-10-03)

- `G:\My Drive\To Read\` (Drive folder 'To Read' in My Drive) holds recent analyses as Markdown only (no PDFs), with embedded images in `To Read\figures\` so the `figures/<file>` links resolve. The Android phone and tablet sync it into a local Obsidian vault with DriveSync Pro.
- Delivery step b2 (Invoke-Delivery) copies each delivered `.md` and its figures there, non-fatal (a failure only logs a warning). Target = `to_read_dir` above.
- `prune-to-read.ps1` (`-DryRun` to preview) deletes `.md` files older than `to_read_retention_days` by LastWriteTime and figures no longer referenced by a remaining `.md`; it never touches `README.md`. The queue worker runs it at most once per calendar day (stamp `queue\prune-to-read.last`, log `queue\prune-to-read.log`).
