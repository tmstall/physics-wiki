# Pedagogy bakeoff — O+O equilibrated fraction (Ito & Hirano)

**Paper:** arXiv:2604.05307 / DOI 10.1103/r39m-l6gz  
**Date:** 2026-08-28

| Version | Path | Role |
| --- | --- | --- |
| Claude gold | `claude_gold_equilibrated-fraction-oo-qcd.md` | Pedagogy target |
| Grok v1 (terse) | `grok_oo_qcd_v1_terse.md` | Failed explanatory-flow bar |
| Grok v2 (rewrite) | `../../md/g_2026-08-27_doi-10.1103-r39m-l6gz_equilibrated-fraction-oo-qcd.md` | Post-contract rewrite |

## Failure diagnosed (v1)

- §3 was glossary (`**Core:**` / `**Corona:**`) without teaching why thermalization is the dividing line
- DCCI2 used as if known; Claude explained it is the authors’ framework
- Analogies bolted under dry bullets instead of carrying the narrative
- Same “just the facts” habit across §§2–7, not only §3

## Pack changes after this feedback

- `ANALYZE.md`: **Explanatory flow** section (whole spine); hard-fail patterns; compress rule flipped (don’t gut §§3–4 teaching)
- `RUBRIC.md`: D4/D5 now score pedagogy; bakeoff/production require D4/D5
- `PRODUCTION_GATE.md`: glossary-only pedagogy is a hard fail

## Score (harsh)

| Dim | Claude | Grok v1 | Grok v2 |
| --- | --- | --- | --- |
| D4 Background pedagogy | 2 | 0–1 | 2 |
| D5 Core walkthrough pedagogy | 2 | 0–1 | 2 |
| Honesty spine (other dims) | 2s | mostly 2s | 2s |
| **Readability for non-subfield engineer** | High | Low | High (aim) |

v2 self-score 24/24 — human skim still recommended (first production pedagogy rewrite).
