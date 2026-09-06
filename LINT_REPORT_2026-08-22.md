# Wiki lint report — 2026-08-22 (full AGENTS lint after staged ingest)

**Catalog:** **183 papers · 62 concepts · 15 synthesis**  
**Trigger:** End of READY_QUEUE ingest (10 papers) + 2 new synthesis hubs.  
**`raw/` untouched.**

---

## Snapshot

| Check | Result |
| --- | --- |
| Index lists all papers | **Pass** (0 missing) |
| Unresolved wikilink targets | **0** |
| New ingest pages with ≥1 Synthesis link | **10/10** |
| True orphans (excl. index/log) | **2** (known islands) |
| Paper↔paper asymmetries (inline YAML counted) | **71** — deferred exhaustive re-rlink |
| Paper→concept missing reverse | **8** — deferred |
| Paper→synth / synth→paper gaps | Mostly neighbor-list noise; **patched** for two new synths |

---

## What this run added (context)

**Ingest (10):** bottom-heavy IMF; ErTe₃ competing CDW; Bose–Fermi droplets; S301; X(2370); mm-wave microcomb; Rydberg CFT spectra; ALICE O+O/Ne+Ne flow; relative-entropy Einstein; rpTDE stellar spin.

**New synthesis (2):**
- [[smbh-stellar-encounters]] — S-stars / rpTDE / Hills
- [[entropic-information-gravity]] — relative entropy + GfE lane

Skipped a third synth (would have been thin: single-paper microcomb or single-paper light-ion flow).

---

## Issues fixed this lint

1. **Synth→paper reverse links** for new hubs — added `Synthesis:` lines on:
   - `evaporating-charged-black-holes`, `hawking-radiation-charge-shell`, `temporal-imbalance-gravity`, `topological-cosmological-constant` → [[entropic-information-gravity]]
   - `category-79-quasar-wind`, `glimpse-17775-cocoon`, `smbh-inclination-angle` → [[smbh-stellar-encounters]]

---

## Known orphans (accepted)

| Page | Why kept |
| --- | --- |
| [[ai-agents-majority-following]] | Complex-systems island; outside AGENTS physics priority |
| [[tc-vertical-alignment]] | Earth-system island; previously peeled from HEA |

---

## No contradiction found (spot-check)

- S301 page does **not** claim measured Sgr A* spin (forecast only).
- ErTe₃ nucleation framed as timing+TDGL inference, not real-space imaging.
- Relative-entropy Einstein page keeps $S=A/4G$ as **imported**.
- X(2370) keeps preprint / single-facility / mixing-angle caveats.
- Bottom-heavy IMF keeps descendant→JWST inference (not direct $z\sim5$ IMF).

---

## Deferred (non-blocking)

| Item | Note |
| --- | --- |
| Exhaustive paper↔paper rlink (71 asymmetries) | Re-opened by volume + YAML parser; schedule dedicated rlink pass |
| Remaining paper↔concept gaps (8) | Low urgency |
| HEA / modified-gravity residual synth asymmetries | Neighbor citations without body reverse — intentional peel leftovers |
| Deepen thin [[gravity-from-entropy]] paper page | Still analysis-short |
| Dual slug `quantum-jamming` | Known |

---

## Log

- Entry appended to `wiki/log.md`.
