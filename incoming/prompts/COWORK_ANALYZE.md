# Claude Cowork prompt — trigger: `analyze`

Paste into Claude Cowork (or bind **`analyze`**). Thin wrapper for the Physics Wiki inbox — Claude’s own analysis quality/framework still applies.

---

## System / task

When the user says **`analyze`** (with PDF, DOI, arXiv, or paste), or pastes an **Analysis kickoff** from the Grok Wiki Coordinator Bot:

1. Confirm it is a technical/academic paper (or meaningful excerpt).
2. Run your usual full paper analysis (flowing, explanatory — teach before jargon).
3. Write the finished markdown into the connected repo:

   `incoming/md/YYYY-MM-DD_<id>_<slug>.md`

   - **No** `g_` prefix (that is Grok Build only).
   - Inbox **root** only (not `archive/`, not subfolders).
4. If the kickoff says **Mode C**, leave room for a Grok twin (`g_…` same slug); do not delete or overwrite a `g_` file.
5. **Do not** run `copy` or edit `wiki/` or `raw/` from this trigger.
6. Tell the user: when ready, say **`copy`** in Cowork (or wait for Bot inbox reminder at ≥5 files).

### Android

Full Claude analysis **can** run from Android. Prefer completing the file into `incoming/md/` via the connected folder when available; otherwise return the markdown for the user to save, and note that staging still needs the file in `incoming/md/` before `copy`.

### Kickoff fields

Honor mode A/C, optional posture/lite **only if set**. If posture/lite blank, use your normal judgment — do not invent an “adversarial” label without cause.

### After write

Print path + basename + reminder: Bot Coordinator does not replace `copy`/`ingest`.
