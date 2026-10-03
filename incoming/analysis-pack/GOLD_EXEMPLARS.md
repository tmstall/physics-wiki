# Claude gold exemplars (rubric fuel, not a training set)

Four Claude (Cowork) analyses chosen for **complete v3.10 checkpoint coverage**, honest calibration, pedagogical flow, and paper-type diversity. Use them to **score** Grok output for structure, honesty, *and* explanatory density (teach before jargon; paragraphs over glossary). Do **not** paste full gold bodies into context as style-transfer exemplars — match depth of explanation, not wording.

**Framework version note:** the golds were written under v3.10. The current framework is the newest `Academic Paper Analysis Framework v*.md` in `C:\Users\tmsta\Desktop\Gold\Prompts` (currently v3.14); it adds a Depth Target, Claim Check (with internal consistency sweep), full-paper reading rule, and Referee Pass that the golds predate. Use the golds for depth, density, and checkpoint *presence*; take those newer requirements from the framework itself.

Copies live in [`exemplars/`](exemplars/). Archive originals remain under `incoming/md/archive/` (also mirrored in `raw/analyses/` after copy).

---

## Selection criteria

1. Full (or near-full) Framework v3.10 section spine with honesty checkpoints actually firing — not just headings.
2. Strong physical intuition + CS/systems analogies with explicit **Breaks when:** lines.
3. Clear Prior Belief / Replication / Predictive Content / Assumption Audit / Where I’m least confident.
4. Diverse failure modes: experiment vs theory vs ultrafast CM vs adversarial preprint.

---

## The four golds

### 1. Experimental — ALICE OO / NeNe nuclear geometry → flow

| | |
| --- | --- |
| **File** | [`exemplars/01_experimental_alice-oo-nene.md`](exemplars/01_experimental_alice-oo-nene.md) |
| **Paper** | ALICE Collaboration — nuclear geometry from anisotropic flow in O–O and Ne–Ne (DOI 10.1103/gymp-vp87) |
| **Why gold** | Clean experimental chain: what was smashed → what was measured → what geometry claim survives systematics. Worked intuition for “debris remembers shape.” Strong Assumption Audit on what flow does and does not prove. |
| **Emulate structurally** | Paper Type & Stakes early; replication/single-experiment honesty; falsifiable handle tied to a concrete observable; don’t oversell nuclear-structure claims beyond the data. |
| **Do not copy** | Specific ALICE jargon density or section length — match checkpoint *presence*, not word count. |

**Exemplar card — experimental**

- Lead with the measurement, not the theory wishlist.
- Name the control / null / cross-check that would kill the claim.
- Keep detector and analysis assumptions in the Assumption Audit, not buried in prose.
- Predictive Content: next run, next system, or next observable with a number or clear qualitative signature.

---

### 2. Theory — quantum relative entropy → semiclassical Einstein equations

| | |
| --- | --- |
| **File** | [`exemplars/02_theory_quantum-relative-entropy-einstein.md`](exemplars/02_theory_quantum-relative-entropy-einstein.md) |
| **Paper** | Dorau & Much, *PRL* — from quantum relative entropy to semiclassical Einstein equations (DOI 10.1103/lmq8-nsty) |
| **Why gold** | Best-in-pack theory treatment: Jacobson lineage framed honestly (incremental for specialists, rigorous upgrade not a new equation); modular theory via systems analogies; exact relative-entropy identity explained with symbol definitions + “what this means”; formalism-load half of Predictive Content used correctly. |
| **Emulate structurally** | Separate “new route to old equation” from “new physics”; Central Analogy locked once; math-light display blocks; Genuine Uncertainty names the thinnest math. |
| **Do not copy** | Length (~48 KB). Grok should hit the same checkpoints more compactly if needed — completeness ≠ verbosity. |

**Exemplar card — theory / foundations**

- Prior Belief: is this surprising to *experts*, or only to outsiders?
- Replication for theory = independent check of the calculation, not a second experiment — say so.
- Formalism-load test: would deleting the math delete a prediction, or only the costume?
- Never invent a Central Analogy for hollow formalism (adversarial posture catches this).

---

### 3. Ultrafast / condensed matter — competing CDW in ErTe₃ (time domain)

| | |
| --- | --- |
| **File** | [`exemplars/03_ultrafast-cm_erte3-competing-cdw.md`](exemplars/03_ultrafast-cm_erte3-competing-cdw.md) |
| **Paper** | Time-domain competing charge-density waves in ErTe₃ (*Nature Physics*; DOI 10.1038/s41567-026-03382-5) |
| **Why gold** | Ultrafast pump–probe logic made concrete; competing orders without drowning in sample folklore; clear “what’s new vs what’s known CDW lore”; good Breaks-when on analogies. |
| **Emulate structurally** | Mechanism picture first; timescale hierarchy; what the time-domain observable uniquely sees that static probes miss. |
| **Do not copy** | Material-specific acronym soup without definitions. |

**Exemplar card — ultrafast / CM**

- Define the order parameter and the probe in plain English before jargon.
- State the non-equilibrium protocol (pump energy, delay window) as engineering constraints.
- Limitations must include recovery, heating, and whether the transient state is the equilibrium phase.
- Falsifiable handle: a delay-dependent signature or a competing-order smoking gun another group can remeasure.

---

### 4. Speculative / adversarial preprint — X(2370) as lightest pseudoscalar glueball

| | |
| --- | --- |
| **File** | [`exemplars/04_speculative_x2370-pseudoscalar-glueball.md`](exemplars/04_speculative_x2370-pseudoscalar-glueball.md) |
| **Paper** | arXiv:2607.20366 — X(2370) as lightest pseudoscalar glueball (preprint; **adversarial posture**) |
| **Why gold** | Explicit adversarial posture on line 1; tempered by BESIII track record without laundering uncertainty; Predictive Content and limitations refuse to treat a preferred interpretation as settled fact. |
| **Emulate structurally** | Posture flag; earn every upgrade from “candidate” to “identification”; separate data quality from interpretive leap. |
| **Do not copy** | Cynicism. Adversarial ≠ hostile — matter-of-fact earning. |

**Exemplar card — speculative / unreviewed**

- Default: no load-bearing core until earned (Framework Part 1).
- Extra weight on Predictive Content (predicts vs relabels) and on confidence tags in §6.
- If the paper only reinterprets existing peaks, say “relabels rather than predicts” as a *finding*.
- Crystallized Takeaways must not smuggle the speculative claim as established.

---

## How to use during a Grok run

1. Identify paper type → open the matching **card** above (a few bullets).
2. After drafting, score with [`RUBRIC.md`](RUBRIC.md).
3. Only if a checkpoint failed: open the gold **long enough to name gap labels** (e.g. “seed mass is free input,” “BHAD >1 dex omitted”), then **close the gold** and rewrite from the paper. Do **not** keep Claude’s sentences on screen while drafting. Near-paraphrase of Watch / §5 / §6 / least-confident prose is a pack failure (ASTRID v2 incident).

## Intentionally not chosen (still useful elsewhere)

| Analysis | Why not gold for this pack |
| --- | --- |
| Gravity-as-compression-error (GfE / Bianconi) | Excellent speculative theory, but Predictive Content checkpoint incomplete relative to v3.10 pipeline golds |
| S301 / Sgr A* spin-sensitive star | Reserved as **bakeoff** target (not a gold used for coaching the same paper) |
| mmWave optical microcomb | Strong alternate ultrafast/photonics gold if ErTe₃ is too domain-specific for a given bakeoff |
