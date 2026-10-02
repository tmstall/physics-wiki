# Wiki Coordinator — skills to save in Grok Bot

In the Bot conversation, ask to **save each block as a skill** with the given name. Enable skills on this Bot under Settings → Plugins → Yours.

---

## Skill: `wiki-analyze-intake`

**When to use:** User says analyze / new paper / pastes DOI, arXiv, PDF, or title from phone.

**Steps:**
1. Collect title, authors, DOI/arXiv/PDF (ask for what’s missing; don’t block forever).
2. If mode A/B/C/D not stated → **ask**. Do not default silently.
3. Posture/lite: blank unless user stated or confirmed.
4. Emit kickoff(s) using the template in spirit of `ANALYZE_KICKOFF.md`.
5. If Mode A or C: tell user to paste into **Claude** now (Android OK).
6. If Mode B or C and Build requested: ask to queue Build; if yes, emit Build kickoff + “paste in Grok Build on desktop — not started yet.”
7. Reminder: after files land in `incoming/md/`, Cowork `copy` then Build `ingest`.

**Must not:** Write the analysis body. Auto-copy. Auto-ingest.

**Returns:** Kickoff markdown + next human action (one line).

---

## Skill: `wiki-compare-request`

**When to use:** compare / bakeoff / which analysis for wiki / Mode D.

**Steps:**
1. Identify files A and B (paths, Drive names, or attachments).
2. If a worker hasn’t written the second analysis yet, emit dual kickoffs first (Mode C), then stop.
3. If both exist: produce a **COMPARE scorecard** (dimension scores, short evidence notes, totals). Follow anti-paraphrase: gap labels only; no third manuscript.
4. End with required human choice: `use A` | `use B` | `merge deep dives` | `defer`.

**Must not:** Overwrite either analysis. Auto-ingest the winner.

---

## Skill: `wiki-inbox-watch`

**When to use:** “check inbox” or scheduled routine.

**Steps:**
1. Count `incoming/md/*.md` at **root** only (exclude archive/_to_delete), via connected folder/Drive if available; else ask for listing or read `_PIPELINE_STATUS.md`.
2. If count ≥ **5**: list filenames; tell user to run Cowork **`copy`** (exact trigger); then Build **`ingest`**.
3. If count &lt; 5: report count only (routine: stay silent or one quiet line — prefer silent on schedule if below threshold).
4. On connector failure: say so; do not use stale invented numbers.

**Must not:** Copy, move, or delete files.

---

## Skill: `wiki-queue-status`

**When to use:** what’s pending / READY_QUEUE / ingest status.

**Steps:**
1. Prefer `_PIPELINE_STATUS.md` or connected `incoming/READY_QUEUE.md`.
2. Else ask user to paste the READY_QUEUE table.
3. Summarize pending / done recently. Never invent rows.

---

## Skill: `wiki-handoff-card`

**When to use:** hand off / what next / continue on desktop.

**Steps:** Emit a short card:

```markdown
## Handoff
- Next action:
- Tool: Claude Cowork | Grok Build
- Paste trigger: copy | ingest | analyze | compare | start deep dive
- Paths / filenames:
- Blockers:
```

---

## Optional routine (after skill works)

**Name:** Wiki inbox ≥5 reminder  
**Schedule:** every 2–3 days  
**Action:** `wiki-inbox-watch` — message **only** if count ≥5 or connector failed  
**Approval:** notify only — no writes
