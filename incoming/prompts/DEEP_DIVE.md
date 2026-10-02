# Grok Build prompt — triggers: `start deep dive` / `end deep dive`

Paste into Grok Build (or bind these trigger strings).  
You operate under repo-root `AGENTS.md`. Paths: `incoming/PIPELINE.md`.

**Purpose:** Interactive Q&A on a paper analysis, with every Deep Dive question and answer **appended into the analysis markdown** so Obsidian reading stays self-contained and restartable. Multiple deep-dive sessions **concatenate** on the same file.

---

## Hard rules

- **Never modify `raw/`.**
- Deep-dive writes happen **only** on a file in **`incoming/md/` root** (not `archive/`, not `_to_delete/`, not `wiki/`, not `analysis-pack/` unless the user explicitly overrides).
- Answers are part of the analysis record (concept unpacking), not a separate wiki page — unless the user later asks to promote something into `wiki/concepts/`.
- Do **not** auto-`copy` or auto-`ingest`.

---

## Analyzer file naming (Claude vs Grok)

Same date / id / slug shape as Claude; Grok files prepend **`g_`**:

| Analyzer | Example basename |
| --- | --- |
| Claude | `2026-08-20_doi-10.1103-lmq8-nsty_quantum-relative-entropy-….md` |
| Grok | `g_2026-08-20_doi-10.1103-lmq8-nsty_quantum-relative-entropy-….md` |

Both live in `incoming/md/` before `copy`, then stage to `raw/analyses/` with the **same basename** (including `g_` if present). Ingest treats `g_` as provenance, not a different paper.

---

## Triggers

### `start deep dive '<analysis file name>'`

Fuzzy-ok: basename, stem, or unique substring. Prefer exact basename match under `incoming/md/`.

**Resolve target**

1. Look in `incoming/md/*.md` (root only).
2. If missing: search `incoming/md/archive/`, `incoming/analysis-pack/bakeoff/`, `raw/analyses/` **read-only**.
3. If found only outside the inbox:
   - **Copy** into `incoming/md/` (keep Claude name as-is; if sourcing a Grok bakeoff/draft without `g_`, rename to `g_<original>` when placing in inbox).
   - Tell the user the new inbox path.
4. If ambiguous: list candidates and **STOP**.
5. If not found: say so and **STOP**.

**Open or resume a Deep Dive section**

- Scan the file for `## Deep Dive —` headings.
- If the **last** Deep Dive section has `**Status:** open` → **resume** it (restart-friendly).
- Else **append** a new section at end of file (after §9 / prior deep dives / footer):

```markdown
---

## Deep Dive — YYYY-MM-DD (session N)

**Status:** open
**Analyzer:** Grok
**Started:** YYYY-MM-DDTHH:MM (local)
**Source analysis:** `basename.md`

*Ask questions in chat. Each Q&A is written into this section. Say `end deep dive` when finished.*

```

- `N` = 1 + count of existing `## Deep Dive —` sections in the file.
- Confirm in chat: `Deep dive open on incoming/md/<name> (session N, resumed|new).`

**Then list remaining Deep Dive candidates (required step):**

1. Read `## Deep Dive candidates` in the file (if present). Prefer checkbox form:
   - `- [ ] …` = not yet discussed  
   - `- [x] …` = already discussed (optionally `— session K`)
2. If candidates use plain bullets with no checkboxes, treat any bullet whose topic is clearly covered by an existing `### Q:` in any Deep Dive section as discussed; treat the rest as open. On first touch, you may normalize open items to `- [ ]` (do not invent new candidates).
3. In chat, print only the **undiscussed** ones, numbered:

```markdown
### Remaining Deep Dive candidates
1. …
2. …

Reply with a number to take that candidate, or just ask your own question about the paper.
```

4. If none remain (all `[x]`, or no candidates section): say so — user may still ask freeform questions.
5. **Do not** auto-answer candidates. Wait for the user to pick a number **or** ask something else.

### During an open deep dive (pick a candidate or ask anything)

**If user picks a candidate** (number, quote, or “do #2”):

1. Treat that bullet’s text as the question theme; answer fully in chat.
2. Append to the open Deep Dive section:

```markdown
### Q: <candidate text or tightened one-liner>

<answer — complete enough to reread in Obsidian without the chat>

```

3. In `## Deep Dive candidates`, mark that item done: `- [x] … — session N`.
4. Re-list **remaining** undiscussed candidates (short), or say “candidates cleared.”

**If user asks a freeform question** (not from the list):

1. Answer in chat (math-light, active voice, systems analogies; Framework reader calibration).
2. **Immediately append** to the open Deep Dive section:

```markdown
### Q: <user’s question, tightened to one line>

<answer — complete enough to reread in Obsidian without the chat>

```

3. If the freeform Q clearly exhausts an open candidate, check that candidate off too and say so.
4. Do **not** require choosing from the list — freeform is always allowed.

**Always:**

- If the question names a concept worth a future wiki hub, one-line note at end of that answer: `*Wiki seed: [[concept-slug]] (not created this turn).*` — only when clearly useful; do not spam.
- Keep the spine of the original analysis intact — deep dives **append**, never rewrite §§1–9 unless the user explicitly asks to correct an error in the spine.

### `end deep dive`

1. If no open session: say so; stop.
2. In the open section, set:
   - `**Status:** closed`
   - `**Ended:** YYYY-MM-DDTHH:MM (local)`
3. Optionally add a one-line session summary under the header (`**Session summary:** …`).
4. **Sync to Google Drive (required):** copy the updated analysis file to  
   `G:\My Drive\Technical Papers\Analyses\`  
   (same basename). If `G:` is missing, start Google Drive for Desktop (`GoogleDriveFS.exe`) and wait for the mount, then copy. Confirm byte-size match.
5. Confirm in chat: session N closed · local path · Drive path. File still remains in `incoming/md/` for later `copy` → wiki ingest.

### Related shortcuts

| User says | You do |
| --- | --- |
| `start deep dive` (no name) | List `incoming/md/*.md` and ask which file |
| `deep dive status` | Report active file / session / open vs none |
| `end deep dive` | Close as above |

Typo tolerance: `analaysis` / `analysis`, extra quotes, missing `.md` are fine if resolution is unique.

---

## Obsidian / restart behavior

- Vault can open `incoming/md/` (and later `raw/analyses/` after copy) — deep dives travel with the analysis.
- Mid-session crash or new chat: run the same `start deep dive '<file>'` again → resumes the **open** section and continues appending.
- After `end deep dive`, a later `start deep dive` on the same file starts **session N+1** (concatenated history preserved).

---

## What counts as a Deep Dive question

Any unpacking the reader cannot get from §§1–9 alone: modular/KMS, why a formula, missing background, “slow down Step 3,” analogy stress-tests, rival interpretations, etc.

## Deep Dive candidates (from `analyze`; optional)

Written during **`analyze`** only for paper types that warrant it (see `ANALYZE.md`): theory / foundations, modular or algebraic-QFT heavy, compressed multi-step derivations, adversarial formalism-load papers. **Not** required on every analysis.

Format (checkboxes so Obsidian + `start deep dive` can track what’s left):

```markdown
## Deep Dive candidates

- [ ] Modular flow vs physical time — when they coincide and when they don’t
- [ ] Why coherent states only (what breaks for generic excitations)
- [ ] How Raychaudhuri turns area change into Ricci without assuming Einstein
```

**Good candidates:** background the spine assumed; a compressed derivation step; an Assumption Audit item that needs a worked example; something named in “Where I’m least confident.”  
**Bad candidates:** restating takeaways; vague “tell me more”; rewriting Prior Belief.

On **`start deep dive`**: list only `- [ ]` (undiscussed) items; user picks a number **or** asks freeform.  
When a candidate is answered: flip to `- [x] … — session N`.  
Candidates section stays in place as a checklist; Deep Dive sessions hold the full answers.

---

## Anti-patterns

- Do not put deep-dive-only content in chat without writing the file (Obsidian would lose it).
- Do not overwrite Claude text when deepening a Claude-named file — append only.
- Do not strip or “summarize away” prior Deep Dive sessions.
- Do not invent paper claims in deep-dive answers; if uncertain, say so and tag *(analyst inference)*.
- Do not auto-launch into answering all candidates at `start deep dive` — list remaining, then wait.
- Do not force the user to use the list; freeform questions are first-class.
