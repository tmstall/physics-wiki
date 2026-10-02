# Grok Bot Coordinator — Physics Wiki

Canonical contract for the **Physics Wiki Coordinator** Bot (grok.com / Grok app) vs **Claude** vs **Grok Build**.  
See also: `ANALYZE_KICKOFF.md`, `COMPARE.md`, `PIPELINE.md`, `incoming/bot/`.

**Locked defaults (Wave 0):**
- Analyzer when unspecified: **always ask** (no silent default; may add a default later)
- Inbox notify threshold: **5** while learning (raise to 10 later)
- Bot **does not** write paper analyses or wiki pages
- MSL is a **separate** project (`Documents/MSL/`) — not this Bot

---

## Hard boundaries

| Actor | May | Must not |
| --- | --- | --- |
| **Wiki Bot** | Intake; ask analyzer mode; emit kickoffs; inbox count/remind; queue status from paste or connected files; **rubric scorecard** when both analyses are available (to help wiki choice) | Full §§1–9 analysis; edit `wiki/`; touch `raw/`; auto-`copy` / auto-`ingest` |
| **Claude** | Full analyze; `copy` staging | Edit `wiki/`; auto-start Build |
| **Grok Build** | Full analyze; deep dive; `ingest`; lint; Build-side `compare` | Modify `raw/` (except via Cowork `copy`); auto-copy |

---

## Analyzer modes (A–D)

| Mode | Who writes | Filename | Notes |
| --- | --- | --- | --- |
| **A — Claude only** | Claude (works from **Android**) | `YYYY-MM-DD_<id>_<slug>.md` | Preferred mobile path |
| **B — Grok only** | Grok Build `analyze` | `g_YYYY-MM-DD_<id>_<slug>.md` | Needs Build session (desktop); Bot **asks** whether to queue a Build kickoff |
| **C — Both** | Claude + Build | Both files in `incoming/md/` | Parallel quality check |
| **D — Compare** | Both exist; score | Keep both; scorecard helps human pick wiki source | After C, or when second analysis arrives |

### Android reality

- **Claude analysis can be started from Android** (paste kickoff → Claude app / Cowork).
- **Grok Build cannot** be driven from the phone the same way. After intake, Bot **asks**: “Also queue a Grok Build analysis?” If **yes**, emit a Build kickoff + handoff card for the next desktop Build session. Do **not** pretend Build already ran.
- Remote auto-start of Build (ACP/API) is **out of scope** until explicitly enabled later.

---

## Posture hint and lite mode (no paper access)

Bot often **cannot** read the PDF. Therefore:

- **Posture hint** and **lite mode** are **optional**. Leave blank unless:
  - the user states them, or
  - the user pasted title/abstract and **explicitly** agrees with a suggested hint, or
  - the user says the paper is short/observational → offer lite, don’t assume.
- Never invent “adversarial” / “explanatory” from the title alone.

---

## Intake → workers

1. Collect title / authors / DOI / arXiv / PDF link (whatever the user has).
2. **Ask** mode A / B / C / D (required if unspecified).
3. Emit kickoff packet(s) per `ANALYZE_KICKOFF.md`.
4. Mode A or C: user runs Claude on Android (or desktop).
5. Mode B or C (Build requested): queue Build kickoff for desktop.
6. Analyses land in `incoming/md/` (+ Drive sync for Grok).
7. Inbox ≥**5**: remind Cowork **`copy`** (never copy from Bot).
8. User runs Build **`ingest`**.

---

## Dual analyses → which one enters the wiki?

When Claude + `g_` twins both reach `raw/analyses/`:

1. Ingest **skips** a second paper page for the same DOI/slug (existing policy).
2. **Prompt the human** which analysis should own the wiki paper page (or merge deep dives).
3. Bot (or Build `compare`) may produce a **rubric scorecard** — scores and gap labels only — to inform that decision. Bot must **not** rewrite either analysis into a third manuscript.

---

## Status card

- Drive: `Technical Papers/Analyses/_PIPELINE_STATUS.md`  
- Local mirror: `incoming/_PIPELINE_STATUS.md` (**not** under `incoming/md/` — must never be staged by `copy`)

Bot may **read** it; human or Build updates after copy/ingest. Bot must not invent counts.
