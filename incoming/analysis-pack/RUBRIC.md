# Analysis scoring rubric (written for v3.10; applies to the current framework — newest in `Gold\Prompts`, currently v3.12)

Score a finished analysis **0–2** on each dimension (0 = missing/wrong, 1 = partial, 2 = solid). Max **24**. Use Claude golds as calibration anchors for what a **2** looks like — not as text to imitate.

## Dimensions

| ID | Dimension | What a 2 looks like |
| --- | --- | --- |
| D1 | **Section spine** | All required sections present for mode (full 1–9 or lite 1,2,5,6,8,9). Action line + `Framework vX.Y` (the version actually used; currently v3.12). |
| D2 | **Access / posture** | Access Status when needed; adversarial vs explanatory posture correct for source type. |
| D3 | **Prior Belief + Replication** | Expert-calibrated surprise/incremental call; single-group vs convergence named; confirmation path stated. |
| D4 | **Background + analogies (pedagogy)** | §3 *teaches* in flowing paragraphs: intuition before operational defs; frameworks/acronyms explained on first use; ≥1 strong systems/CS (or chemistry) analogy woven into the narrative (not bolted under a glossary bullet); each has **Breaks when:**; **Central analogy** locked once. Glossary-only §3 = max 1, usually 0. |
| D5 | **Core technical walkthrough (pedagogy)** | Active voice *story* of what authors did and why each step exists; tools named as tools (e.g. “authors’ DCCI2 framework”); math-light with symbol defs + “what this means”; concrete numbers in context. Pipeline-of-package-names with no teaching prose = max 1. |
| D6 | **Assumption Audit** | 2–4 real Watch items; each teaches the trap in 3–6 sentences (reader-might-assume → why wrong → number/citation when available); includes ≥1 non-obvious (method≠resolved physics, match≠unique recipe, headline range partly free input). Telegram one-liners = max 1. |
| D7 | **Novelty + Predictive Content** | What’s new to the field vs packaging; flowing §5 that elevates the sharpest novel result + mechanism sketch; falsifiable handle with **specific numbers/thresholds** when the paper has them. Slogan-only §5 or vague “sim vs survey” handle = max 1. |
| D8 | **Limitations honesty** | Brutal but fair; author-flagged quantitative misses first (do not omit >1 dex self-critiques); each item (A)/(B)/(C) + justification + source; contested items name rival causes when given. One-liner laundry list missing loudest miss = max 1. |
| D9 | **Uncertainty disclosure** | Explicit “Where I’m least confident…” on a **load-bearing** thin spot — prefer the novel claim’s under-verified mechanism over “I didn’t re-fit their plots.” |
| D10 | **Takeaways + §9** | Three dinner-table takeaways; §9 ≤350 words, plain English, no smuggled overclaim. |
| D11 | **Anti-truncation** | Analysis ends after §9 (or lite equivalent) with closing line; no mid-section cutoff; no “continued later”; no missing honesty blocks. |
| D12 | **Calibration / no overclaim** | Title/hook don’t claim spin measured when only sensitivity forecast, etc.; stakes match evidence. |

## Pass bars

| Use | Bar |
| --- | --- |
| **Bakeoff “competitive with Claude gold”** | ≥20/24 and **no zero** on D1, D4, D5, D7, D8, D9, D11; D4 and D5 both ≥1 (prefer 2) |
| **Production gate (into `incoming/md/`)** | ≥18/24 and **no zero** on D1, D2, D4, D5, D7, D11; D4 ≥1, D5 ≥1, D12 ≥1 |
| **Lite mode** | Same bars on the lite subset; mark N/A for skipped full-only dimensions and rescale (multiply average of scored dims × 12) |

## Scoring notes

- Prefer **1** over a charitable **2** when a checkpoint is present but soft (e.g. Prior Belief without saying whether *experts* are surprised).
- A beautiful truncated analysis scores **0 on D11** and fails production — completeness is part of quality.
- **Exact** voice/phrasing mismatch with Claude is **not** a deduction. **Pedagogy mismatch is:** if Claude teaches thermalization with a sustained analogy and Grok only dumps “Core: … Corona: …”, score D4/D5 harshly (0–1). Structural honesty without explanatory flow is incomplete quality.
- Score D4/D5 on the *whole* spine habit: if §7 and §9 stay telegram-terse while §3 is fine, cap D5 at 1.
- Score D6–D9 on **density**, not presence: Claude-style explanatory watches / novel-result prose / quantitative self-critiques beat terse correct bullets. Presence-only Audit or §6 that skips the paper’s loudest dex miss → cap at 1.

## Quick scorecard template

```
Paper:
Mode: full | lite
Scorer / date:

D1  __/2   D2  __/2   D3  __/2   D4  __/2
D5  __/2   D6  __/2   D7  __/2   D8  __/2
D9  __/2   D10 __/2   D11 __/2   D12 __/2
Total __/24

Gaps to fix before production:
-
```
