# Coordinator lessons (append-only)

## [2026-08-29] pack landed

- Threshold set to **5** while learning (raise to 10 later).
- Analyzer: **always ask** (no silent Claude default yet).
- Android: Claude analyze OK; Build analyze = queued kickoff only.
- Posture/lite: never guess from title alone.
- Dual analyses: both in `raw/`; human chooses wiki source; Bot/Build may scorecard.
- Status card: `incoming/_PIPELINE_STATUS.md` + Drive `Analyses/_PIPELINE_STATUS.md` — **not** in `incoming/md/`.
- MSL truth under `Documents/MSL/docs/bot/` only.
