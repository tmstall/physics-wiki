# Bakeoff scorecard — Dorau & Much relative entropy → semiclassical Einstein

**Date:** 2026-08-26  
**Mode:** full v3.10 + deep-dive appendix  
**Claude gold:** [`claude_gold_quantum-relative-entropy-einstein.md`](claude_gold_quantum-relative-entropy-einstein.md) (also exemplar `02_…`; includes Deep-Dive Discussion Log 2026-08-22)  
**Grok candidate:** [`grok_quantum-relative-entropy-einstein_v3.10.md`](grok_quantum-relative-entropy-einstein_v3.10.md)  
**Source:** arXiv:2510.24491 / *PRL* **136**, 091602 (2026), DOI 10.1103/lmq8-nsty

This is the hard theory bakeoff — user note: most complicated recent paper; many follow-up questions in the deep-dive log.

## Rubric scores

| Dim | Claude gold | Grok bakeoff | Notes |
| --- | ---: | ---: | --- |
| D1 Section spine | 2 | 2 | Both full 1–9 + appendix |
| D2 Access / posture | 2 | 2 | Explanatory (*PRL*); Access Status present |
| D3 Prior Belief + Replication | 2 | 2 | Both: not shocking to experts; assembly novelty; single-group / young |
| D4 Background + analogies | 2 | 2 | Claude’s audit-log is richer; Grok’s WAL/diff analogies land the same checkpoints |
| D5 Core walkthrough | 2 | 2 | Both five-step chain; Grok more explicit that Step 3 leans on Kurpicz et al. 2021 |
| D6 Assumption Audit | 2 | 2 | Both: area law imported; coherent-only; local-only; (Grok adds “math not all new”) |
| D7 Novelty + Predictive Content | 2 | 2 | Both: **relabels rather than predicts**; formalism-load fires |
| D8 Limitations honesty | 2 | 2 | Circularity (B), coherent-only (A), local (A), scrutiny age (C) |
| D9 Uncertainty disclosure | 2 | 2 | Claude: HTML extraction / modular→integral steps; Grok: Kurpicz vs new + δA ansatz |
| D10 Takeaways + §9 | 2 | 2 | §9 under 350 words; no “QI derives gravity from nothing” overclaim |
| D11 Anti-truncation | 2 | 2 | Complete through appendix |
| D12 Calibration / no overclaim | 2 | 2 | Title/takeaways keep imported area law visible |
| **Total** | **24** | **24** | Competitive on rubric |

## Deep-dive appendix (extra, user-critical)

| Question theme | Claude gold | Grok bakeoff | Edge |
| --- | --- | --- | --- |
| Modular / KMS from zero | Excellent, longer | Solid, tighter | Claude (depth) |
| Why modular = boost (Euclidean pie) | Excellent | Present, shorter | Claude |
| What is a boost | Clear | Clear | Tie |
| Central analogy unpacked | Audit-log table in prose | Explicit table | Tie / Grok slightly clearer map |
| Step 2 (horizon algebra, quasifree, coherent) | Excellent | Solid | Claude |
| Step 3 heart (Araki → Noether → $T_{UU}$) | Excellent chain | Excellent + positivity | Tie |
| Step 4 Clausius identification | Clear | Clear | Tie |
| Step 5 Raychaudhuri → Einstein | Clear | Clear; flags “unchanged from 1995” | Tie |
| Synthesis arc | Strong closing paragraph | Strong closing paragraph | Tie |

**Deep-dive verdict:** Grok appendix is **usable for the same reader questions** and hits every theme in the Claude log. Claude remains the **gold for maximal pedagogical unpacking** (especially modular=boost Euclidean argument and Step 2). Grok is competitive for production; for *this* paper, keep Claude’s deep-dive linked when the reader is stuck.

## Qualitative gaps → pack tightenings

| Gap | Severity | Fix |
| --- | --- | --- |
| Theory papers with a deep-dive culture need an optional appendix in ANALYZE | Med | Documented below in ANALYZE bakeoff lessons |
| Crediting prior modular/horizon relative-entropy papers (Kurpicz et al.) avoids over-claiming novelty | Med | Already in Grok Assumption Audit; add to ANALYZE tip for theory |
| Claude deep-dive > Grok on Euclidean uniqueness argument | Low | Acceptable; optional “expand Q2 on request” |

## Verdict

**Phase 0/3 theory bakeoff: PASS — competitive with Claude gold on rubric.**  
Deep-dive: **PASS with note** — covers the user’s question set; Claude still preferred as the maximal explainer for modular/KMS and Step 2.

Do **not** re-ingest to wiki from this bakeoff (paper page already exists from Claude ingest). Bakeoff validates the ANALYZE pack on a foundations/QI-gravity Letter.

## Follow-ups

1. Optional: expand Grok Q2 (Euclidean uniqueness) to Claude length if a third pass is wanted.  
2. Pack: ANALYZE.md bakeoff lesson for theory + deep-dive appendix (done with this scorecard).
