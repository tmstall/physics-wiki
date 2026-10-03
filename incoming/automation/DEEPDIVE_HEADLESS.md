# DEEPDIVE_HEADLESS.md - instructions for a headless Claude Code deep dive

You are running non-interactively (Claude Code `-p`). Nobody can answer questions mid-run, so never stop to ask; make a reasonable call and say so in the answer.

A **deep dive** answers one question about a paper that has **already been analyzed** with the Academic Paper Analysis Framework. It unpacks something the reader can't get from the nine sections alone: a derivation step, missing background, an Assumption Audit item that needs a worked example, a rival interpretation, a number to re-check, or a "slow down Step 3". It is part of the analysis record, not a new analysis.

## 1. Inputs (paths are given in the run prompt)

1. **The existing analysis** (`.md`). Read it **in full** first. It sets the vocabulary, the claim-check results and the confidence tags you build on.
2. **The paper PDF**, when provided. Read the parts the question touches **directly** (Read tool, at most 20 pages per call); read more if the answer depends on it. Never answer from the analysis alone when the PDF can settle the point.
3. **The framework** (newest `Academic Paper Analysis Framework v*.md` in `C:\Users\tmsta\Desktop\Gold\Prompts`, resolved by version number as in `incoming\automation\ANALYZE_HEADLESS.md` section 1). Read its **Target Reader Profile, Style Rules, Non-Negotiable Formatting Rules and confidence tags**. You do not run the nine-section structure here.
4. **Deep-dive conventions** in `incoming\prompts\DEEP_DIVE.md` (Q/A format, "complete enough to reread in Obsidian without the chat", no invented claims, *(analyst inference)* tags, optional wiki-seed note). If the run prompt names a `deep-dive-workflow.md`, read it too; where it is more specific than this file, it wins.

## 2. How to answer

- Answer the question that was asked, fully, at the framework's reader calibration: assume real background, build up machinery from other fields, draw analogies from computer systems (not signal processing), active voice.
- Ground every paper claim in the paper (section / equation / figure). Mark your own reasoning *(analyst inference)*. Use the framework's confidence tags where a claim is uncertain.
- Numbers: re-derive them when the question is quantitative. Python is allowed (run `python` only; scripts go in the work directory). Say which script you ran.
- Other papers: check the **latest arXiv version** via its abs page or listing and cite the version you used; do not rely on a tool summary of an older version. If you only saw an abstract or an older version, say so.
- If the question exposes an **error or gap in the existing analysis**, say so plainly in a short **Correction to the analysis** paragraph at the end. Do not edit the analysis file.
- Length: whatever the question needs, usually 800-2,500 words. No padding, no restating the analysis.

## 3. Output file

Write one Markdown file with the Write tool into the **work directory** named in the run prompt, with the **exact filename** the prompt gives. Format:

```markdown
# Deep dive: <short form of the question>

**Paper:** <title> (<arXiv/DOI>) | **Source analysis:** `<analysis basename>.md` | **Date:** YYYY-MM-DD | **Analyzer:** Claude (headless, Opus) | **Framework:** vX.Y
**Sources read:** <analysis; PDF pages/sections read; other sources with versions>

### Q: <the question, tightened to one line>

<the answer>
```

Everything from the `### Q:` line to the end of the file is what gets appended to the analysis when the user asks for it, so keep it self-contained.

## 4. Write scope

- Write **only** to the work directory named in the run prompt. The pipeline script (`incoming\automation\deep-dive.ps1`) copies the answer to `incoming\deep-dives\`, Google Drive and (on request) appends it to the analysis.
- Do not modify the analysis, the wiki, `incoming\md`, Google Drive, or anything in `C:\Users\tmsta\Desktop\Gold\Prompts`. No git.
- Finish with one line: `WROTE <full path> <byte count if known>`.
