# Bakeoff scorecard — S301 / Sgr A* spin-sensitive star

**Date:** 2026-08-26  
**Mode:** full v3.10  
**Claude gold:** [`claude_gold_s301-sgra.md`](claude_gold_s301-sgra.md) (Cowork, Framework v3.10, analyzed as ESO preprint eso2612a — **adversarial** posture)  
**Grok candidate:** [`grok_s301-sgra_v3.10.md`](grok_s301-sgra_v3.10.md) (arXiv:2607.12664 + *Nature* DOI 10.1038/s41586-026-10894-w — **explanatory** posture)

Posture difference is **correct**, not a defect: the gold was written against an unreviewed draft; the bakeoff uses the published / arXiv full text.

## Rubric scores

| Dim | Claude gold | Grok bakeoff | Notes |
| --- | ---: | ---: | --- |
| D1 Section spine | 2 | 2 | Both complete 1–9 |
| D2 Access / posture | 2 | 2 | Each correct for its source state |
| D3 Prior Belief + Replication | 2 | 2 | Both calibrate “incremental object / significant capability” |
| D4 Background + analogies | 2 | 2 | Both: PN digit / camera-depth / compounding; Breaks when + Central analogy |
| D5 Core walkthrough | 2 | 2 | Grok slightly leaner on CLEAN / Peißker catalog tension |
| D6 Assumption Audit | 2 | 2 | Grok 4 Watch items; Claude 3 — both real |
| D7 Novelty + Predictive Content | 2 | 2 | Both: discovery vs forecast; Brackett-γ + decade χ forecast; formalism-load fired |
| D8 Limitations honesty | 2 | 2 | Orientation lottery, no RV, single facility, perturbers |
| D9 Uncertainty disclosure | 2 | 2 | Claude: Hills/timescale appendices; Grok: mock-data→2035 systematics |
| D10 Takeaways + §9 | 2 | 2 | §9 under ceiling; no spin-overclaim |
| D11 Anti-truncation | 2 | 2 | Both finish cleanly |
| D12 Calibration / no overclaim | 2 | 2 | Both keep “sensitive” ≠ “measured” |
| **Total** | **24** | **24** | Competitive |

## Qualitative gaps (tighten pack, not fail bakeoff)

| Gap | Severity | Pack fix |
| --- | --- | --- |
| Grok thinner on competing short-period star claims (Peißker et al.) | Low | ANALYZE tip: when paper adjudicates rival catalogs, devote an explicit subsection — specialists care |
| Grok thinner on Hills progenitor a_bin ~0.1 AU / v_rot test | Low | Optional depth under Origin; not required for gate |
| χ² number: gold said 29.1; arXiv HTML says 26 / 34 dof | Info | Prefer full-text numbers; gold may reflect draft PDF variance |
| Self-score 24/24 is optimistic if used alone | Process | PRODUCTION_GATE: first 3 Grok productions still need human skim |

## Verdict

**Phase 0/3 bakeoff: PASS — Grok analysis is competitive with Claude gold on rubric dimensions.**  
Voice differs (good). Structural honesty matches. Safe to use ANALYZE.md in production with the human seam in [`../PRODUCTION_GATE.md`](../PRODUCTION_GATE.md).

## Follow-ups

1. Optional second bakeoff on a **theory** gold (quantum relative entropy) if experimental-only confidence feels thin.  
2. Do **not** promote this bakeoff file into `incoming/md/` — S301 was already ingested to the wiki from the Claude analysis; this run is quality-pack validation only.
