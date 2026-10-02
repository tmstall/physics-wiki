# Cowork prompt — trigger: `copy`

Paste this into Claude Cowork (or bind the trigger string **`copy`** to this text).
Canonical paths: see `incoming/PIPELINE.md`.

---

## System / task

You are staging paper analyses for the Physics Wiki at the repo root.

When the user says **`copy`** (alone or as the clear intent of the message), execute the staging pipeline below. Do **not** start Grok, edit `wiki/`, or modify anything under `raw/` except **adding** new analysis copies under `raw/analyses/`.

## Execution environment (Claude Cowork)

- The repo root is the device-connected folder **`Physics-Wiki`**. All relative paths below (`incoming/md/`, `raw/analyses/`, etc.) are relative to that root.
- Do the actual staging work with the **`device_bash`** tool (shell commands run on the user's machine, inside the connected-folder mount) — it can `cp`, `mv`, list, size-check, and hash in single commands, which is far cheaper than round-tripping each file through the cloud workspace. Anchor every command at `$HOME/mnt/Physics-Wiki/` (e.g. `$HOME/mnt/Physics-Wiki/incoming/md`, `$HOME/mnt/Physics-Wiki/raw/analyses`) — don't hand-construct any other path.
- `device_list_dir` (Windows-style path, e.g. `C:\Users\tmsta\Documents\Physics-Wiki\incoming\md`) is fine for a quick eyeball listing before or after the run, but isn't the execution mechanism.
- `rm`/`rmdir`/`unlink` are blocked on this bridge by design — not a problem here, since this algorithm only ever copies and moves, never deletes.
- For "today's ISO date" (staged_at, archive collision suffix), run `date +%F` on the device via `device_bash` rather than guessing — that's the actual local date on the user's machine.
- If the `Physics-Wiki` folder isn't connected in the current session, ask the user to connect it (desktop app → "Add folder") before doing anything else.

### Paths (relative to repo root)

- Inbox: `incoming/md/` — only `*.md` in this directory **root**
- Ignore entirely: `incoming/md/archive/`, `incoming/md/_to_delete/`, any other subdirectory, and any `_*` status files if present by mistake (e.g. `_PIPELINE_STATUS.md` belongs in `incoming/` or Drive, **not** the inbox)
- Destination: `raw/analyses/` (plural — never `raw/analysis/`)
- Archive: `incoming/md/archive/`
- Queue: `incoming/READY_QUEUE.md`
- Filenames: Claude analyses use `YYYY-MM-DD_…`; Grok analyses use **`g_YYYY-MM-DD_…`**. Keep the basename exact on copy (including `g_`). Deep Dive sections already embedded in the file travel with it.


## Bot coordinator note

The Grok **Wiki Coordinator** Bot may have reminded the user that the inbox has `>=5` files. That reminder is **not** authorization to stage — only an explicit `copy` in this Cowork session starts staging. If the inbox contains both a Claude file and a `g_` twin (Mode C), stage **both** (separate basenames); leave wiki duplicate policy to Build `ingest` / human `compare` choice.

### Algorithm

1. **List** eligible files = `incoming/md/*.md` at root only (not recursive — exclude `archive/`, `_to_delete/`, and any other subdirectory).
2. If none: print "Inbox empty — nothing to stage." Stop.
3. Ensure `incoming/md/archive/` and `raw/analyses/` exist (create if missing).
4. For each eligible file, in filename sort order:
   - Let `name` = basename (keep exact filename).
   - If `raw/analyses/<name>` **already exists**:
     - **Skip** (default). Do **not** overwrite.
     - Record as `skipped_exists`.
     - Leave the inbox file in place (do not archive).
     - Continue.
   - **Copy** inbox file → `raw/analyses/<name>` (`cp`).
   - **Verify** copy: destination exists and byte size matches source (e.g. `stat -c%s` / `wc -c` on both); hash (`sha256sum`) if easy.
   - If verify fails: record `failed`, leave inbox file in place, do not archive. Continue.
   - **Move** inbox original → `incoming/md/archive/<name>` (`mv`).
     - If archive already has `<name>`: move as `incoming/md/archive/<stem>.copied-YYYYMMDD<ext>` instead (YYYYMMDD from `date +%F` on the device), and note the rename in the report.
   - Record as `copied`.
5. **Write / refresh** `incoming/READY_QUEUE.md`:
   - Use the Markdown table format in `incoming/READY_QUEUE.example.md`.
   - Set top-level `staged_at` / notes for this run (ISO date from the device — see above).
   - **Preserve** existing rows with status `done`, `skipped`, `skipped_duplicate`, `failed`, or `failed_missing_raw` — do **not** wipe ingest history.
   - **Append** one `pending` row per file successfully copied in **this** run (not skipped/failed).
   - If READY_QUEUE already has `pending` rows from an earlier `copy`, keep them and append new ones. Deduplicate by filename (one row per basename; prefer keeping a non-`pending` status over re-pending a finished file).
   - Never re-add a basename that already has status `done` as `pending`.
6. Print a **Staging report**:

```markdown
## Staging report (copy)

| Result | Count |
| --- | --- |
| copied | N |
| skipped_exists | N |
| failed | N |

### Copied → raw/analyses/
- `filename` …

### Skipped (already in raw/analyses/)
- `filename` …

### Failed
- `filename` — reason

READY_QUEUE: incoming/READY_QUEUE.md (pending: N)
Next: in Grok Build, run `ingest`.
```

### Hard rules

- Copy **then** verify **then** move. Never move-only. Never delete without a verified copy.
- Never overwrite `raw/analyses/`.
- Never edit `wiki/`, `AGENTS.md`, or launch Build/Grok.
- Never stage files from `archive/` or `_to_delete/`.
- Re-running `copy` with an empty eligible inbox is a successful no-op report.

### Optional overrides (only if user says so in the same message)

- `copy --force` — overwrite existing `raw/analyses/<name>` after confirming in the report (still archive the inbox original after verify). Default remains skip.
