# Paper-analysis automation pipeline config

```yaml
ingest_threshold: 10
framework_source_dir: C:\Users\tmsta\Desktop\Gold\Prompts
canonical_framework: C:\Users\tmsta\Desktop\Gold\Prompts\Academic Paper Analysis Framework v3.11.md
canonical_framework_sha256: D1E504720391F001F23B319D95E1181F9ED10A59E96D8A42EED8C6788E91ACCF
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