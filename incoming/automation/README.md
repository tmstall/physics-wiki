# incoming/automation - paper pipeline (Phase 3)

Headless paper analysis on this laptop with Claude Code (Opus) and the newest Academic Paper Analysis Framework in `C:\Users\tmsta\Desktop\Gold\Prompts` (resolved by version number, currently v3.12).

## Files

| File | What it does |
| --- | --- |
| `analyze-paper.ps1` | One command per paper: duplicate check, latest arXiv PDF, Claude Code (Opus) run, verified delivery. |
| `deliver-analysis.ps1` | Delivery only, for an existing `.md` (same code `analyze-paper.ps1` uses). Has overrides for testing. |
| `deep-dive.ps1` | Answers one question about an already-analyzed paper (Claude Code, Opus). |
| `queue-worker.ps1` | Processes queued jobs one at a time under `queue\worker.lock`. |
| `submit-job.ps1` | Adds a job file to `queue\` (and with `-RunNow`, starts the scheduled task). |
| `register-queue-task.ps1` | Registers the scheduled task `PhysicsWiki-PaperQueue` (`-Remove` to delete it). |
| `run-hidden.vbs` | Starts the worker without a console window (the task's action). |
| `pipeline-lib.ps1` | Shared functions. |
| `ANALYZE_HEADLESS.md` / `DEEPDIVE_HEADLESS.md` | Instructions Claude follows in headless runs. |
| `run-claude.ps1` | Finds the newest `claude.exe` bundled with Claude Desktop. |
| `papers-analyzed-log.md` | One row per delivered analysis. |
| `scratch\work\<stamp>_<id>\` | Per-run work folder (PDF, text, prompt, `claude.jsonl`, `run.log`, output). Git-ignored. |
| `queue\` | Job files and worker logs. Git-ignored. |

## Analyze a paper

```powershell
cd C:\Users\tmsta\Documents\Physics-Wiki\incoming\automation
.\analyze-paper.ps1 2605.16504                    # arXiv ID, arXiv URL, DOI or doi.org URL
.\analyze-paper.ps1 10.1103/pz3y-3lv5 -Title 'Neutrino flavor conversion ...'
.\analyze-paper.ps1 2605.16504 -DryRun            # no Claude call, no delivery (checks + PDF + prompt only)
```

Options: `-NoDeliver` (leave the output in the work folder), `-NoPush`, `-Force` (ignore duplicate hits).
Exit codes: `0` done, `1` failed, `2` duplicate (skipped), `3` usage limit (stopped cleanly).

What it does:

1. **Metadata.** arXiv API (latest version, DOI, journal ref). For a DOI, Crossref finds the arXiv preprint (`has-preprint`, else an exact title match on arXiv).
2. **Duplicate check.** Searches `wiki\papers`, `raw\analyses`, `incoming\md` (all subfolders) and `papers-analyzed-log.md` for the arXiv ID, DOI, filename id and title. A filename, title or log hit, or an id hit in the first 40 lines of a file, is **strong** and stops the run. Id mentions deeper in other files are reported as **weak** and don't stop it.
3. **Full text.** Downloads the latest arXiv PDF, plus a `pdftotext` copy, into the work folder.
4. **Claude Code on Opus.** Follows `ANALYZE_HEADLESS.md`, which loads the newest framework. Claude can write only to `scratch\**`, through absolute `Write`/`Edit` rules. Output is captured as UTF-8 stream-json in `claude.jsonl`. The run prompt also includes this rule: when comparing with other papers, check each one's latest arXiv version (abs page or listing), not a tool summary of an older version.
5. **Blocked save.** If the save was blocked, the analysis is recovered from the jsonl (permission denials and Write calls).
6. **Usage limit.** If the usage limit is hit, the run stops cleanly with exit `3`, and a queued job stays queued as `limit`.
7. **Delivery.** Every copy is checked for size and SHA-256:
   1. `incoming\md\<YYYY-MM-DD>_<id>_<slug>.md`
   2. `G:\My Drive\Technical Papers\Analyses\`. If G: isn't mounted, Google Drive for Desktop is started; if it's still missing, the copy is queued in `queue\drive-retry.txt`. The laptop has no pandoc/LaTeX, so the PDF is listed in `queue\pdf-todo.txt` and built on the box (pandoc + xelatex).
   3. A row is appended to `papers-analyzed-log.md`: date | title | arXiv/DOI | file | model | words.
   4. `git add` and commit of just the analysis and the log (never wiki/raw or other changes), then `git push`. A failed push is retried by the next worker run.
8. **Inbox count.** Prints how many `.md` files are in `incoming\md` root (pending ingest).

## Queue (works while the laptop sleeps)

Job files live in `queue\` as `<stamp>_<type>_<paper>.<status>.json`, where status is `pending`, `running`, `done`, `failed` or `limit`. The scheduled task **PhysicsWiki-PaperQueue** runs `queue-worker.ps1`:

- **Triggers:** at logon (+2 min), on wake from sleep (System log, Microsoft-Windows-Power-Troubleshooter event 1, +3 min) and every 30 min.
- **Account:** user-level, runs only while logged on, no admin needed.

Each worker run:

1. Retries a failed git push and failed Drive copies.
2. Imports Drive inbox files.
3. Resets orphaned `running` jobs.
4. Works through `pending` jobs oldest first.

A usage limit parks the job as `limit` with `retryAfter` (the reset time from Claude's rate-limit event) and stops the queue until then. Duplicates end as `done` with `result.status = duplicate`.

### Submit a job: laptop awake (Shell on the laptop)

```powershell
cd C:\Users\tmsta\Documents\Physics-Wiki\incoming\automation
.\submit-job.ps1 2605.16504 -Source box -RunNow
.\submit-job.ps1 10.1103/pz3y-3lv5 -Title 'Optional title' -Source box -RunNow
.\submit-job.ps1 2605.16504 -Type deepdive -Question 'Why does deep mixing hurt 20 Msun stars?' -Append -Source box -RunNow
.\submit-job.ps1 2602.03456 -DryRun -RunNow       # test: no Claude call
```

`-RunNow` starts the scheduled task right away. Without it, the job runs at the next 30-minute tick.

### Submit a job: laptop asleep (Drive inbox)

Put a small `.txt` or `.json` file in **`G:\My Drive\Technical Papers\Queue\`**. From the box, use `UploadFile` to the Google Drive connection with destination path `Technical Papers/Queue`. After wake, Drive for Desktop syncs it down. The worker (wake trigger or next 30-minute tick) turns it into a queue job and moves the original to `Queue\_picked\`; unreadable files go to `Queue\_rejected\`. Files younger than 15 s are left until the next run, in case they are still syncing.

Text format: either plain lines (line 1 = arXiv ID/URL or DOI, line 2 = optional title), or `key: value` lines:

```text
paper: 2605.16504
title: Neutrino Flavor Conversion Shapes the Rate of Failed Core-collapse Supernovae
```

```text
type: deepdive
paper: 2605.16504
question: Re-derive the 1.9x / 2.6x supernova-rate deficits from Table I.
append: true
```

Keys: `paper`, `title`, `type` (`analyze` | `deepdive`), `question`, `append`, `dryRun`, `force`. JSON with the same keys also works.

### Check status

`queue\*.json` holds each job and its result: status, output path, words, run time, usage before/after, delivery details. Worker logs are `queue\worker.log` and `queue\last-job-console.log`. Each run's own log is `scratch\work\<run>\run.log`.

## Deep dives

```powershell
.\deep-dive.ps1 2605.16504 'Why does flavor equipartition below the neutrinosphere cool the gain region?'
.\deep-dive.ps1 neutrino-flavor 'Re-derive the rate deficits' -Append      # filename substring works too
.\deep-dive.ps1 2602.03456 'question' -DryRun                              # no Claude call
```

1. **Finds the analysis.** Searches `incoming\md` root first, then its subfolders, then `raw\analyses`.
2. **Finds the PDF.** Reuses one already in `scratch`, else downloads the latest arXiv version.
3. **Runs Claude Code on Opus** with `DEEPDIVE_HEADLESS.md`, which uses the framework's reader profile and style rules plus the `incoming\prompts\DEEP_DIVE.md` Q/A conventions. If a `deep-dive-workflow.md` is ever copied into `incoming\automation\` or `incoming\prompts\`, it is loaded too.
4. **Saves the answer** to `incoming\deep-dives\<date>_<id>_dd-<slug>.md` and to `G:\My Drive\Technical Papers\Deep Dives\`, then commits and pushes it.
5. **`-Append`** also appends the Q&A to the analysis as a closed `## Deep Dive - <date> (session N)` section, in the DEEP_DIVE.md format, and re-syncs that analysis to Drive Analyses. This only works for an analysis in `incoming\md` root, per DEEP_DIVE.md.

## Not here (later phases)

The threshold-10 ingest reminder (Phase 4), the 5-paper pause, and the `copy` / INGEST staging step (Phase 4/5) are not built.
