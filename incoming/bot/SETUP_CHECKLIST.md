# Wave 2–3 setup checklist (human)

## Create Wiki Bot (grok.com / Grok app)

- [ ] New Bot → name **Physics Wiki Coordinator**
- [ ] Paste `WIKI_BOT_PROFILE.md` into Edit Profile
- [ ] Save skills from `WIKI_BOT_SKILLS.md` (intake, compare, inbox-watch, queue-status, handoff)
- [ ] Enable skills on this Bot
- [ ] Optional: connect read access to Google Drive `Technical Papers/Analyses` and/or Physics-Wiki folder
- [ ] Optional routine: inbox ≥5 every 2–3 days (notify only)
- [ ] Android smoke: DOI → Mode A kickoff → Claude

## Create MSL Bot

- [ ] New Bot → name **MSL Curator**
- [ ] Paste profile from `C:\Users\tmsta\Documents\MSL\docs\bot\MSL_BOT_PROFILE.md`
- [ ] Save skills from `MSL\docs\bot\MSL_BOT_SKILLS.md`
- [ ] Do **not** enable Wiki skills on this Bot

## Cowork

- [ ] Re-paste `incoming/prompts/COPY.md`
- [ ] Paste / bind `incoming/prompts/COWORK_ANALYZE.md` for `analyze`
- [ ] Confirm device folder Physics-Wiki mounts

## Build

- [ ] Open Physics-Wiki; `compare` / `/wiki-compare` available
- [ ] Open sibling `Documents\MSL` as its own Build project when doing releases

## Smoke

- [ ] Bot Mode A → Claude analyze → file in `incoming/md/`
- [ ] Bot asks Build queue → handoff card
- [ ] `copy` → one READY_QUEUE pending → `ingest` batch of 1
- [ ] Dual analyses → Bot or Build `compare` scorecard → human `use A|B|…`
