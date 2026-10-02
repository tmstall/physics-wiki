# Analysis kickoff packet

Emitted by the **Physics Wiki Coordinator** Bot (or by a human).  
**Workers** (Claude / Grok Build) execute the real analysis. The Bot never fills §§1–9.

---

## Template (copy into Claude and/or Build)

```markdown
## Analysis kickoff
- Title / authors:
- DOI / arXiv / PDF:
- Desired mode: A Claude | B Grok | C Both | D Compare
- Posture hint: _(optional — leave blank unless user stated)_ explanatory | adversarial | _(blank)_
- Lite mode: yes / no / ask  _(default: no unless user said short/observational)_
- Deep Dive candidates: optional / yes if theory-heavy / ask
- Shared slug suggestion (for Mode C twins):
- After gate PASS:
  - Claude → `incoming/md/YYYY-MM-DD_<id>_<slug>.md`
  - Grok → `incoming/md/g_YYYY-MM-DD_<id>_<slug>.md` + Drive sync
- Do NOT copy / ingest from this kickoff
- Build queue: yes / no  _(Android: Claude now; Build when at desktop if yes)_
```

---

## Mode C — emit two packets

Same DOI and **shared slug**. Label one `For Claude` and one `For Grok Build`.

## Mode B from Android

If user wants Grok-only while on phone: emit Build kickoff + say clearly **“Paste this in Grok Build when you are at the PC. Analysis is not started yet.”**

## What Bot must not do

- Do not write Necessary Background, Assumption Audit, or any full framework section.
- Do not invent Access Status (“full PDF”) without evidence.
- Do not set posture/lite by guessing from the title alone.
