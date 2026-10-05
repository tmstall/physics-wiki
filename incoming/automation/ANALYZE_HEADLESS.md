# ANALYZE_HEADLESS.md — instructions for headless Claude Code paper analysis

You are running non-interactively (Claude Code `-p`). Nobody can answer questions mid-run, so never stop to ask; make the call the framework would make and note it in the output.

These instructions are general: they apply to any paper type (experiment, theory, simulation, observation, quantum information, condensed matter, astrophysics, speculative preprint, ...). Nothing here is specific to one paper.

**Division of labour:** the framework is the single source of truth for *how to analyze* (sections, checkpoints, depth target, full-paper reading, key figures, claim check, consistency check, referee pass, formatting). This file only adds what is specific to this laptop and to headless Claude Code: which framework file to load, where the files are, which tools to use, and where to save. If anything here ever seems to conflict with the framework on analysis method, the framework wins.

## 1. Resolve and load the framework (mandatory, every run)

1. List the framework files with Glob: `C:\Users\tmsta\Desktop\Gold\Prompts\Academic Paper Analysis Framework v*.md` (Markdown only; ignore the `.pdf` renders and any differently named files such as `Academic_Paper_Analysis_Framework_v3_10.md`).
2. Pick the **highest version number**, comparing the parts numerically (major, then minor, then patch): v3.16 > v3.15 > v3.9. Do not sort as text and do not go by file date. (As of 2026-10-04 the newest is **v3.16**.)
3. Read that file **in full** before doing anything else. The framework is long, so a single Read may be cut off. If it is, keep paging with offset/limit until you reach the last line (the file ends with the changelog and a closing italic footer). Call its version `vX.Y` below (take it from the filename; it should match the file's own `**Version X.Y …**` header line — if they disagree, use the header and say so in the Genuine Uncertainty Disclosure).
4. If no file matches, stop and print `FAIL no framework found in C:\Users\tmsta\Desktop\Gold\Prompts` instead of analyzing.

Apply it **exactly**: this is the Claude Project's *Trigger 4 — Paper Analysis (full)*.

- Apply the full framework. Do not summarize informally. Do not default to a generic overview.
- Use the framework's full nine-section Response Structure, in order, with each section as a `## N. ...` heading.
- Everything the framework marks mandatory is mandatory here: honesty checkpoints, the Depth Target, the full-paper reading rule, the Key Figures rule (if the framework has one), the Claim Check (including its internal consistency check), and the Referee Pass. Follow every section guideline, the Non-Negotiable Formatting Rules, the Style Rules, the Target Reader Profile, and the Source posture rule.
- **Header lines:** per framework Part 1, line 1 of the output is the version prefix `vX.Y` and line 2 is the action line `Analyzing | Framework vX.Y`. Append `| <status note>` only when something is worth flagging, e.g. partial access.
- **Lite mode:** headless runs always produce the FULL analysis. Do not propose lite mode, since no one can answer. If the paper looked like a lite candidate, say so in one line at the opening of the Genuine Uncertainty Disclosure.

## 2. Depth calibration files (laptop locations)

The framework's Depth Target is defined generically. On this laptop, calibrate against the gold exemplars before drafting (paths relative to the repo root `C:\Users\tmsta\Documents\Physics-Wiki`):

- `incoming\analysis-pack\GOLD_EXEMPLARS.md`: paper-type cards. Pick the card matching this paper's type.
- `incoming\analysis-pack\exemplars\*.md`: read the exemplar closest to this paper's type in full, and skim the others for structure and density.
- `incoming\analysis-pack\RUBRIC.md` and `incoming\analysis-pack\PRODUCTION_GATE.md`.

The exemplars were written under v3.10, so they predate the Claim Check and Referee Pass. Use them for explanatory depth only, and take everything else from the framework, including the length target and how much math to show (v3.14+: explain first, few equations, about 5,000-7,500 words; v3.15+: no appendix, small tables, protected origins background; v3.16+: numbers, notation and jargon budgets, Section 4 step template, plain-verdict Claim check), which the longer, more mathematical exemplars predate. Never copy or closely paraphrase exemplar sentences.

**Calibration limits (v3.16+):** `RUBRIC.md`, `PRODUCTION_GATE.md` and the exemplars predate v3.14. Where they reward symbol definitions, "concrete numbers in context", "specific numbers/thresholds", or density, the framework's plain-language rules win (numbers budget, no notation in prose or headings, jargon budget, plain-verdict Claim check). Never use them to set how many numbers, symbols or technical terms the analysis carries; use them only for checkpoint presence and explanatory depth.

## 3. Getting and reading the paper (tool specifics)

The framework's master retrieval protocol and full-paper reading rule govern *what* to read. Here is *how* to do it with the tools in this run:

- **Local full text first:** the pipeline pre-downloads the paper and gives you local paths in the run prompt. These can be the PDF itself, a full-text `.txt` extraction (pdftotext, with `===== PDF PAGE n =====` markers; figures absent, captions present, equations possibly garbled), and/or rendered page images (`.png`). These are the primary full-text source.
  - **Read the PDF directly with the Read tool.** Poppler (`pdftoppm`/`pdftotext`) is installed, so Read can render a `.pdf`. Use its page-range option for long PDFs, at most 20 pages per read, and page through to the end. Use the PDF for equations, figures, tables and layout.
  - Use the `.txt` extraction as a backup and for fast searching (Grep). Use the page images if PDF reading fails.
- WebFetch returns model-summarized extracts, not raw text, so it is **not** an acceptable way to read the paper. Use WebFetch/WebSearch only for metadata (arXiv abs page, journal-ref, publication status) and context (prior work, press, replication, competing results).
- **If no local PDF/text was provided** (or it is unreadable), get the full text yourself:
  - For arXiv papers, try `https://arxiv.org/abs/<id>` (metadata, version, journal-ref), then `https://arxiv.org/html/<id>` (full HTML, including appendices/supplement if present), then `https://arxiv.org/pdf/<id>`.
  - For DOIs, use the DOI landing page or the open-access version.
  - Fetch the supplementary material if it is separate.
  - Check with WebSearch for a journal publication, to set the source posture.
- If web tools are unavailable and no local text was given, follow the framework's Stage 3: output Access Status **Fail** and stop.
- Always output the framework's **Access Status** block right after the header lines and before Section 1. Be honest about what you actually read (e.g. a fetch that truncated, or figures that were unavailable).

## 4. Python for the Claim Check (tool specifics)

The framework's Claim Check defines *what* to verify. In this run:

- Python is allowed (run `python` only; numpy is available).
- Keep scripts short. Save any script files in the **work directory** named in the run prompt.
- Do not install packages or touch files outside the work directory.
- In the analysis, say that the checks were run in Python and name the script file(s).
- The script output stays in the work directory. The analysis reports verdicts and their meaning in plain words, as the framework's Claim Check specifies; do not paste test statistics, fitted values or per-bin results from the script into the analysis.

## 5. Figures (tool specifics)

The framework decides *which* figures to show and how to caption them (v3.13+: Key Figures rule; older versions: the graphics rule). Here is how to do it in this run:

- **Pre-extracted figures:** the pipeline puts them in the run's work directory under `figures\` and names the manifest in the run prompt (`figures\FIGURES.md`). Read the manifest first. It lists:
  - **Figure files** `<prefix>_figN.png` (or `_figNa`, `_figNb` for multi-panel figures built from several files), rendered from the authors' own files in the arXiv source. These are the best copies. They are numbered by the order of figure environments in the LaTeX, so confirm each number against its caption in the PDF.
  - **Page renders** `pages/page-NN.png` of the pages that carry figure captions (150 dpi).
  - Sometimes **raw embedded images** `pdfimages/...`. These are often fragments or single panels.
- **View before you choose:** open the candidate images with the Read tool (it displays PNG/JPG) and pick the key figures the framework asks for. Always include any figure your text calls central.
- **No usable figure file** for a key figure (no arXiv source, an EPS that was not converted, a broken render)? Crop it out of the page render with Python and Pillow (both installed), e.g. `python -c "from PIL import Image; im=Image.open(r'<work>\figures\pages\page-03.png'); im.crop((x0,y0,x1,y1)).save(r'<work>\figures\<prefix>_fig2.png')"`. Check the crop with Read, and redo it if the caption or axis labels are cut off. A whole-page render is acceptable as a last resort. Tables: reproduce the key rows as a Markdown table rather than as an image.
- **Embed syntax:** standard Markdown with a relative path, one image per line, exactly as the file is named in the work directory's `figures\` folder:
  `![Fig. 1: short description](figures/<prefix>_fig1.png)`
  Then the caption line and the What-to-look-at note the framework specifies. Use forward slashes and no `..`, absolute paths or URLs. Use only files that exist in `figures\` (the pipeline refuses to deliver an analysis with a broken embed, and copies the embedded files next to the delivered `.md` in `incoming\md\figures\`, so these paths resolve in Obsidian and in the PDF build). Do not embed page renders that you have not cropped unless no better copy exists. Never embed files you did not check.
- **No figures pre-extracted** (DOI-only paper, extraction failed): describe each key figure in words and reference it by number, as the framework's fallback says. Say so in the Access Status.
- State in the Access Status which figures you viewed and where they came from (arXiv source files, page renders or crops).
- **Concept diagram** (framework v3.13+, optional but encouraged): write it as plain text in a fenced code block, using ASCII characters only (`->`, `|`, `v`, `+-->`) and lines of at most about 70 characters, so it renders the same in Obsidian and in the box PDF build. It is not an image file and needs no embed.
- **Visual micro-example** (framework v3.16+, encouraged): for the hardest unfamiliar concept, you may draw one analyst-built explainer picture with Python into the work directory's `figures\` folder, named `<prefix>_explainer.png` (prefix from the run prompt). matplotlib is **not** installed and you must not install packages; draw with Pillow (`PIL.Image`, `PIL.ImageDraw`: lines, polylines from computed points, rectangles, text), which is installed. Keep it to two or three small labelled panels with a few real numbers, white background, at least 1200 px wide, readable text. View it with Read and redo it if labels overlap or are cut off. Embed it like a paper figure (`![Explainer: short description](figures/<prefix>_explainer.png)`), followed by the caption line *Analyst-built illustration (not from the paper):* ... and a one-sentence What to look at note. If the result is not clean, use a short plain-text sketch in a fenced code block instead.

## 6. Output file

- Write the complete analysis (exactly what would have been delivered in chat) as one Markdown file using the Write tool. Only the final, referee-revised version goes to disk. Do not write a separate draft file.
- Filename: `YYYY-MM-DD_<id>_<slug>.md`
  - `YYYY-MM-DD` = today's date (local).
  - `<id>` = `doi-<doi with / and other unsafe characters replaced by ->` (e.g. `doi-10.1038-s41586-026-01234-5`) or `arxiv-NNNN.NNNNN` (no version suffix). If the run prompt names the id to use, use that one.
  - `<slug>` = short lowercase hyphenated slug of the title (≈4–8 words).
  - If the run prompt asks for a suffix (e.g. `_run3`), add it before `.md`.
- Output directory: the **work directory** given in the run prompt (a per-run folder under `incoming\automation\scratch\work\`).

## 7. Write scope and delivery (Phase 3)

- Write **only** to the work directory named in the run prompt. Python scratch scripts and figure crops, if any, also go there (crops into its `figures\` folder).
- **Delivery is done by the pipeline script, not by you.** After you finish, `incoming\automation\analyze-paper.ps1` checks the file and copies it (plus the figure files it embeds) to `incoming\md\`, Google Drive and the papers-analyzed log, and commits it to git. So do **NOT** write to `incoming\md`, Google Drive, the papers-analyzed log or the wiki, and do no git operations. You have no write access there anyway.
- Do not modify any other file in the repo, and never modify anything in `C:\Users\tmsta\Desktop\Gold\Prompts` (read-only).
- **Self-check before writing (mandatory, v3.16+):** on the final text, count with Python: total words; displayed equations (`$$` blocks); inline symbols in Sections 1-4 (inline `$...$` math, Greek letters other than σ, and sub/superscripted variables, outside displayed equations); and the largest number of numeric values in any one prose paragraph of Sections 1-4. Targets: words at most 7,500 (aim for 5,000-6,500), displayed equations at most 3, inline symbols in Sections 1-4 zero (σ for significance excepted), at most two numbers per paragraph except in the Claim check and result tables. If any target is missed, revise and count again before writing the file.
- After writing, print `SELFCHECK words=<n> display_eq=<n> inline_symbols_s1_4=<n> max_numbers_per_paragraph=<n>`, then one line `FRAMEWORK <resolved framework path> vX.Y`, then the final line `WROTE <full path> <byte count if known>`.
