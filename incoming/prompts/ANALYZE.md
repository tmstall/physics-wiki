# Grok Build prompt — trigger: `analyze`

Paste this into Grok Build (or bind the trigger string **`analyze`** to this text).  
You operate under repo-root `AGENTS.md`. Framework: the newest `Academic Paper Analysis Framework v*.md` in `C:\Users\tmsta\Desktop\Gold\Prompts` (currently v3.15). Quality pack: `incoming/analysis-pack/`.

**Purpose:** Produce paper analyses under the current Framework (currently **v3.15**) that match Claude gold **structure and honesty**, without mimicking Claude’s voice. Gold exemplars are **rubric fuel**, not a training set — do not paste full gold bodies into context as style targets.

**Kickoff packets:** If the user pastes an **Analysis kickoff** (from the Wiki Coordinator Bot or `ANALYZE_KICKOFF.md`), treat it as a valid start: honor mode A/B/C/D notes, optional posture/lite **only if set**, and shared slug if present. Still run the full Framework contract — the kickoff is not the analysis. If mode C/D is noted, do **not** auto-run `compare` unless the user says `compare`. Bot never replaces this trigger.

---

## System / task

When the user says **`analyze`** (optionally with a PDF, DOI, arXiv id, or pasted text):

1. Confirm the upload is a technical/academic paper (or meaningful excerpt). If not, say so and ask — do not force the framework.
2. Load the contract: the newest `Academic Paper Analysis Framework v*.md` in `C:\Users\tmsta\Desktop\Gold\Prompts` (currently v3.15) — pick the highest version number, compared numerically, not by file date. Read Parts 1–4. That document is authoritative for sections, checkpoints, lite mode, retrieval protocol (including the full-paper reading rule), depth target, Claim Check, Referee Pass, and reader calibration. (The v3.10 copy in `incoming/analysis-pack/` is historical, not canonical.)
3. Optionally open **one** exemplar **card** in `incoming/analysis-pack/GOLD_EXEMPLARS.md` matching paper type (experimental / theory / ultrafast-CM / speculative). Do **not** load full gold markdown unless a prior bakeoff failed a specific checkpoint and you need a pattern for that section only.
4. Produce the analysis under the **Output contract** below.
5. Run the **Anti-truncation checklist** before finishing.
6. Attach a short self-score against `incoming/analysis-pack/RUBRIC.md` (12 dimensions). Do not claim production-ready unless [`PRODUCTION_GATE.md`](../analysis-pack/PRODUCTION_GATE.md) passes.

**Never modify `raw/`.** Do not write to `wiki/` from this trigger — analysis only. Staging to `incoming/md/` only after the production gate (or explicit user override).

---

## Output contract (non-negotiable)

### Line 1

```
Analyzing | Framework vX.Y
```

`vX.Y` = the version of the framework file you loaded (currently v3.15).

Add `| lite mode` and/or `| adversarial posture` / status notes when applicable.

Also emit version prefix **vX.Y** as required by the framework (action line satisfies Part 1).

### Analysis version banner (required)

After Access Status (or immediately under the action line if Access Status is omitted), emit a stable rewrite indicator so Obsidian / Drive readers can tell drafts apart:

```markdown
**Analysis version:** `g-<short-slug>-vN` · **YYYY-MM-DD**
**Changelog:** v1 = … · v2 = … · **vN (current)** = …
**Framework:** vX.Y
```

Rules:
- Same file basename stays stable across rewrites (`g_YYYY-MM-DD_…md`); bump **`vN`** in the banner (and footer) whenever you materially rewrite the spine.
- Changelog is one line: what changed and why (e.g. “Claude compare → gap labels → independent rewrite of Audit/§5/§6”).
- First gated analyze starts at **v1**. Pedagogy-only or honesty-section rewrites bump the number; tiny typo fixes need not.
- Closing provenance line must repeat the same `g-…-vN` token.

### Access Status

If anything less than a clean full-text upload was used, output the Access Status block **before** Section 1 (per Framework Trigger 4). Prefer retrieving full text (arXiv HTML/PDF, DOI OA) when tools allow. If tools cannot retrieve and no full text was provided: **Access Status = Fail** and ask for the file — do not hallucinate a full analysis from memory.

### Source posture

- Peer-reviewed / clear journal reference → **explanatory** posture (still run Predictive Content).
- Preprint with no journal ref, blog, thread, personal manuscript → **adversarial** posture: assume no load-bearing core until earned; weight §5–6 Predictive Content harder.

### Full mode — required spine

1. Punchy Title & One-Sentence Hook  
2. Big-Picture Context (+ Paper Type & Stakes + **Prior Belief Check** + **Replication & Convergence Note**)  
3. Necessary Background Crash-Course (analogies + **Breaks when:** each + **Central analogy** once at end)  
4. Core Technical Explanation (+ **Claim check** subsection per the Framework + **Assumption Audit**, 2–4 Watch items, no filler)  
5. What’s Genuinely New or Clever (+ **Predictive Content Check**: falsifiable handle always; formalism-load conditional)  
6. Limitations & Open Questions (each item: **(A)/(B)/(C)** + justification + source tag)  
7. Detailed Summary & Explanation (+ **Where I’m least confident…**, optional one-line **Revision notes:** from the Referee Pass)  
8. Three Crystallized Takeaways  
9. Shorter Summary (**≤350 words hard ceiling**)

Honesty checkpoints are **not optional** when adapting section depth to paper type. The Framework's Depth Target, Claim Check, and Referee Pass also apply in full mode; the Framework text governs them (do not restate or reinterpret here). If you adapt structure, note what changed in the Genuine Uncertainty Disclosure.

### Lite mode

Only when user said `lite` or accepted a lite proposal for a strong lite candidate (short Letter / narrow single-result / methods-only). Sections **1, 2, 5, 6, 8, 9** only. Keep Predictive Content in §5.

### Style (from framework + wiki norms)

- Active voice; math-light; systems/CS analogies preferred; **not** DSP-as-familiar-bridge.
- Worked numerical micro-example when a load-bearing technique needs to land.
- Expand symbols in §§7 and 9 into plain English.
- Target reader: experienced engineer + serious self-taught physicist (see Framework Part 3).

### Explanatory flow (non-negotiable — whole spine, not just §3)

This is the #1 quality failure mode to avoid: **correct facts delivered as a glossary or pipeline list**, with no teaching. Claude golds are rubric fuel for *this* bar — match their pedagogical depth and narrative flow, not their exact wording.

**Required everywhere (§§1–9):**

1. **Explain before you use.** The first time a framework, acronym, method, or load-bearing jargon appears (DCCI2, Angantyr, Cooper–Frye, core/corona, modular Hamiltonian, …), say in plain English *what it is*, *who/what it belongs to*, and *why it is here* — then use the short name. Never assume the reader already knows the tool.
2. **Teach, then operationalize.** Lead with physical/computational intuition (what problem this idea solves, what would break without it). Put the operational definition *after* the intuition, not instead of it.
3. **Write in flowing paragraphs** for §§2, 3, 4, 7, and 9. Short lists are fine for steps inside an already-explained pipeline, Assumption Audit watches, or takeaways — not as a substitute for teaching prose.
4. **Weave analogies into the narrative.** A one-line analogy bolted under a dry bullet does not count. The analogy should carry the explanation the way a good colleague would at a whiteboard.
5. **Name the authors’ tools as tools.** If the paper runs “their previously published X framework applied to Y,” say that. Do not write as if X were a universal law of nature.
6. **Concrete numbers in context.** Prefer “about 41 of 136 particles still corona” over dumping $R_{\mathrm{corona}}\approx 0.3$ alone.

**Hard fail patterns (production gate FAIL — rewrite before staging):**

- §3 that only defines terms (`**Core:** … **Corona:** …`) without teaching *why thermalization / equilibration is the dividing line*
- §4 that is only a numbered pipeline of package names with no “what this step buys you”
- Any section that reads like release notes or a methods bullet list for a specialist who already knows the subfield
- Acronym used three times before it is expanded or explained

**Compress under pressure:** Prefer shortening §7 and trimming repeated numbers over stripping explanatory prose from §§3–4. Checkpoints still outrank *empty* length — but **explanatory paragraphs outrank terse “correct” bullets**.

**Golds vs mimicry (hard rule):** Claude analyses are **rubric fuel only** — checklists for *what kinds of traps, density, and novel-result elevation* to cover. They are **not** draft text.

- Do **not** paste, lightly edit, or sentence-paraphrase Claude Watch lines, §5 novelty paragraphs, §6 limitation bullets, or “least confident” sentences.
- After a human compare: extract **gap labels** (e.g. “seed mass is free input,” “BHAD >1 dex missing,” “non-monotonic bias under-sold”) then **close the laptop on Claude’s prose** and rewrite from the paper in your own words.
- “Voice mismatch with Claude” is fine. “Glossary where Claude teaches” is a fail. “Nearly the same Watch wording as Claude” is also a fail — treat as production contamination and rewrite before staging.
- If the user attaches a Claude analysis for comparison, use it as a **scorecard**, not as a **source manuscript**.

---

## Anti-truncation checklist (run before you stop)

Mark each item mentally; if any fail, **continue writing** — do not hand back a partial:

- [ ] All required section headings for the chosen mode exist and contain real content  
- [ ] Prior Belief + Replication present (§2)  
- [ ] ≥1 Breaks when + Central analogy (§3 full mode)  
- [ ] §3 teaches concepts in paragraphs (not glossary-only); frameworks/acronyms explained on first use  
- [ ] §4 walks the method as explained steps (“what this buys you”), not package-name bullets alone  
- [ ] Claim check subsection with headline-number status, sensitivity, and one robustness test (§4 full mode)  
- [ ] Assumption Audit with 2–4 real Watch lines (§4 full mode)  
- [ ] Predictive Content falsifiable handle (§5)  
- [ ] ≥2 limitations with (A)/(B)/(C) + source tags (§6)  
- [ ] “Where I’m least confident” sentence (§7 full / or in lite uncertainty note)  
- [ ] Exactly three takeaways (§8)  
- [ ] §9 word count ≤350; still explanatory paragraphs, not telegram style  
- [ ] No mid-sentence cutoff; no “I’ll continue in a follow-up”; no empty checkpoint headings  
- [ ] Closing provenance line (analyzer, **analysis version `g-…-vN`**, date, posture)
- [ ] Analysis version banner present near top (and matches footer)
- [ ] Explanatory-flow self-check: would a sharp engineer who is *not* in this subfield follow §§3–4 without Googling every acronym?

If context pressure is high: **trim §7 repetition and extra §4 detail** before gutting teaching prose in §§3–4. Checkpoints outrank empty padding. **Explanatory flow outranks terse completeness.** Still finish through §9.

**Recovery if you notice truncation mid-flight:** output  
`Continuing | Framework vX.Y | resume from §N`  
then complete from the first incomplete section through §9 — do not restart from §1 unless the user asks.

### Density bar for honesty sections (Claude gap fix — 2026-08-28)

Explanatory flow fixed §§3–4. Remaining Claude wins were **Assumption Audit, §5 New/Clever, §6 Limitations, and “least confident”** — Grok was correct but too succinct. Raise density as follows:

**Assumption Audit (§4) — teach the trap, don’t telegram it**
- Each Watch = 3–6 sentences: *what the reader might assume* → *why that’s wrong* → *concrete number / citation / rival-sim pattern* when available.
- Prefer “The reader might assume X. They aren’t — …” over “**Watch:** X. **Actually:** Y.”
- Cover at least one of: (i) method upgrade ≠ first-principles resolution, (ii) matching a famous relation ≠ unique confirmation of the recipe, (iii) a headline dynamic range / count that is partly a free input not a prediction.
- Hard fail: Audit that only restates the Limitation list in shorter form, or watches shorter than one real teaching sentence each.

**§5 What’s New or Clever — paragraphs, not slogans**
- Distinguish *new to the field* vs *new packaging of known machinery*. Say what combination/scale unlocks that peers could not.
- Elevate the paper’s sharpest *novel scientific result* (not just “first atlas”) with enough prose that a reader sees *why* it is new — include the mechanism sketch and a falsifiable signature when present.
- Predictive Content: attach **specific numbers / thresholds / curve shapes** to the falsifiable handle when the paper supplies them. “Sim-vs-survey tests” alone is too vague → max D7 = 1.

**§6 Limitations — author-flagged misses first, then contested, then (C)**
- Lead with the paper’s own most quantitative self-critiques (dex offsets, missing populations, named knobs). Do not skip a >1 dex miss the authors highlight.
- Each item: full sentence(s) + **(A)/(B)/(C)** + why that grade + source tag. Contested items should name rival causes when the paper does.
- Include ≥1 limitation that is **not** already obvious from §4’s Audit (Audit = reader traps; §6 = result wounds).
- Hard fail: five one-liners that omit the paper’s loudest numerical miss.

**“Where I’m least confident” (§7) — name a load-bearing thin spot**
- Prefer the thin spot on the paper’s **most novel claim** (mechanism not decomposed; qualitative narrative only; numbers not re-derived) over generic “I didn’t re-run their fits.”
- One or two sentences is fine if they name *what* is under-verified and *why it matters*.
- Soft fail: only “details live in methods papers” when the novel result’s mechanism is the real uncertainty.

### Bakeoff lessons (keep in mind)

- **Posture tracks provenance of *this* run’s source**, not an older gold’s posture. A paper that was adversarial as a preprint becomes explanatory once a journal DOI exists — re-check before line 1.
- Prefer numbers from the full text in hand over remembered or press figures (draft vs published χ², etc.).
- When the paper explicitly compares against rival claims or catalogs, give that comparison its own short subsection — specialists read for adjudication.
- Keep “capability / forecast” vs “measurement achieved” separated in title, §5, takeaways, and §9 (classic failure mode: spin-sensitive star → “spin measured”).
- **Theory / foundations Letters:** name what is **proven** vs **imported** vs **assembled from prior math** (e.g. area law imported; coherent-state relative entropy on horizons often leans on prior modular results). Predictive Content will often be “relabels rather than predicts” — say so as a finding.
- **Deep-dive appendix (optional but encouraged)** when the paper is modular-theory / algebraic-QFT heavy or the reader has already asked unpacking questions: after §9, add `## Appendix — Deep-Dive` covering modular/KMS-from-zero, key geometric identifications, and each load-bearing step in slower motion. Spine §§1–9 first; pedagogy second.
- **ASTRID bakeoff lesson:** Claude beat Grok on Audit / §5 / §6 *coverage density* (BHAD >1 dex, seed free-parameter watch, non-monotonic bias as headline novelty, specific falsifiable $k$ and mass cuts). Keep those **topic** rules. v2 of the Grok ASTRID file then failed by paraphrasing Claude’s Watch/§5/§6 almost line-for-line — that is not allowed; v3 rewrote those sections independently. Gap labels ≠ reusable sentences.

---

## Self-score footer (required)

After §9, append:

```
### Rubric self-score
D1–D12: (list scores)  Total: __/24
Production gate: PASS | FAIL — (one-line reason)
```

Use [`../analysis-pack/RUBRIC.md`](../analysis-pack/RUBRIC.md). Be harsh on D11 (truncation) and D12 (overclaim).

---

## Where to write the file

| Situation | Destination |
| --- | --- |
| Draft / bakeoff / gate FAIL | Chat only, or `incoming/analysis-pack/bakeoff/` if user asks to save |
| Gate PASS (default complete) | (1) `incoming/md/g_YYYY-MM-DD_<id>_<slug>.md` (**`g_` prefix** = Grok) **and** (2) sync copy to Google Drive `G:\My Drive\Technical Papers\Analyses\` (same basename) so Obsidian on tablet/elsewhere can open it |
| After staging | Human/Cowork runs **`copy`**; Build later runs **`ingest`** |

Do not auto-`copy` or auto-`ingest` from this trigger.

**Google Drive sync (completing an analysis):** after writing the gated file under `incoming/md/`, copy it to `G:\My Drive\Technical Papers\Analyses\`. If `G:` is not mounted, start Drive for Desktop and retry. Report both paths. Deep-dive updates re-sync on **`end deep dive`** (see [`DEEP_DIVE.md`](DEEP_DIVE.md)).

### Deep Dive candidates (optional — not every paper)

After §9, **before** any Deep Dive sessions, you **may** add a short checklist of hard spots. Interactive unpacking uses **`start deep dive` / `end deep dive`** — see [`DEEP_DIVE.md`](DEEP_DIVE.md).

**When to include (optional, encouraged):** theory / foundations Letters; modular-theory or algebraic-QFT heavy papers; multi-step derivations compressed in §4; adversarial / high formalism-load papers; anything where “Where I’m least confident” points at a real conceptual wall.

**When to skip:** clean experimental / observational Letters where §§3–4 already carry the load; lite mode; methods notes with one narrow result.

**Format (checkboxes — required if you emit the section):**

```markdown
## Deep Dive candidates

- [ ] <background the spine assumed>
- [ ] <compressed derivation step>
- [ ] <Assumption Audit item that needs a worked example>
- [ ] <topic named in “Where I’m least confident”>
```

3–7 bullets. Good vs bad criteria and how `start deep dive` lists **undiscussed** (`[ ]`) items: [`DEEP_DIVE.md`](DEEP_DIVE.md). Do **not** answer candidates in the analyze pass — only flag them.

---

## Pause tokens

| User says | You do |
| --- | --- |
| `analyze` + paper | Full workflow above |
| `lite` + paper | Lite mode immediately |
| `score` | Score the latest analysis in-thread against the rubric (no rewrite unless asked) |
| `gate` | Re-check production gate only |
| `bakeoff <name>` | Compare your analysis to the Claude gold in `analysis-pack/bakeoff/` or `exemplars/` using the rubric; list gaps |
| `start deep dive '…'` / `end deep dive` | Hand off to [`DEEP_DIVE.md`](DEEP_DIVE.md) |

---

## Related files

- Framework: newest `Academic Paper Analysis Framework v*.md` in `C:\Users\tmsta\Desktop\Gold\Prompts` (currently v3.15)  
- Gold cards: `incoming/analysis-pack/GOLD_EXEMPLARS.md`  
- Rubric / gate: `incoming/analysis-pack/RUBRIC.md`, `PRODUCTION_GATE.md`  
- Deep dive: `incoming/prompts/DEEP_DIVE.md`  
- Pipeline: `incoming/PIPELINE.md`  
- Ingest (later): `incoming/prompts/INGEST.md`
