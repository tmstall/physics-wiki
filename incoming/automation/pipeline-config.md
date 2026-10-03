# Paper-analysis automation pipeline config

```yaml
ingest_threshold: 10
framework_source_dir: C:\Users\tmsta\Desktop\Gold\Prompts
canonical_framework_rule: newest 'Academic Paper Analysis Framework v*.md' in framework_source_dir, by version number (numeric compare)
canonical_framework: C:\Users\tmsta\Desktop\Gold\Prompts\Academic Paper Analysis Framework v3.12.md   # current as of 2026-10-02
canonical_framework_sha256: 94FB578234AB97C770D67EBB3B46E25013E6B746ECF5EDABEA881F40224A31F2
analysis_runner: Claude Code (bundled with Claude Desktop) on laptop
delivery:
  - incoming\md
  - G:\My Drive\Technical Papers\Analyses
  - incoming\automation\papers-analyzed-log.md   # papers-analyzed log in repo; to be created in Phase 3
picks: 4-5 per request
phases_status:
  phase_0: done 2026-10-02
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
