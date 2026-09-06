# Wiki lint report — 2026-08-16

**Catalog:** **167 papers · 61 concepts · 9 synthesis**  
**Scope:** Contradictions / orphans / missing hubs / stale claims / cross-links (deeper link pass per user choice).  
**`raw/` untouched.**

---

## Snapshot checks

| Check | Result |
| --- | --- |
| Index lists all papers | **Pass** (0 missing) |
| Index lists all synthesis | **Pass** (9/9) |
| Duplicate paper rows in index | Only **`quantum-jamming`** (paper + concept share slug — known) |
| Catalog header vs disk | **167 / 61 / 9** aligned |
| True orphans (excl. index/log) **before** fix | **7** |
| True orphans **after** fix | **0** |

---

## Issues found → fixed this pass

### 1. Content orphans (no inbound from papers/concepts/synthesis)
Were: `tc-vertical-alignment`, `life2-telescope-array-biosignatures`, `color-space-geometry`, `differential-signaling-quantum-vacuum`, `enzyme-resistance-tax`, `gpu-mass-spectrometry`, `molecular-bias-point`.

**Fixes:** reverse links from neighbors / hubs:
- TC → HEA synthesis table + page connection
- Life2 ↔ Euclid
- Color-space ← `weak-values` concept
- Differential signaling ← Hawking charge-shell
- Enzyme tax ← water-RNA Pol II
- GPU MS ← twisted-light chiral MS
- Molecular bias ← ITO fieldoscopy

### 2. Recent ingest not folded into synthesis maps
Post–2026-08-14/16 papers were on disk and indexed but **not cited from synthesis** `related_papers` / tables.

**Fixes:**
- **nuclear-dense-matter-precision** ← `alice-jpsi-gluon-saturation` (+ table row, strong-coverage note)
- **high-energy-astrophysics-multimessenger** ← Cyg X-3, flying-focus, Oyashio, TTT spins, IMF, dark-photon, TC (+ messenger table rows)
- **condensed-matter-topology-fractionalization** ← `tise2-core-level-cdw-excitons` (+ strong-coverage bullet)
- **modified-speculative-gravity** ← `gw-bound-states-continuum` (+ comparative table row)

---

## No contradiction found (spot-check)

- RHIC / EMC / NA61 cleanup narratives still consistent with nuclear synthesis.
- Speculative gravity pages remain exploratory; GW-BIC added with same disclaimer tier.
- ALICE saturation framed as ~3σ evidence (not discovery) — consistent with STAR UPC page as different hard-probe angle.

---

## Deferred (non-blocking)

| Item | Note |
| --- | --- |
| Exhaustive reverse-link audit of all 167 papers | Only recent + orphans patched |
| `quantum-jamming` rename (paper vs concept) | Still dual slug |
| Thin chemistry islands | Linked enough to un-orphan; not deepened |
| Synthesis prose refresh for new rows | Tables/related_papers updated; full narrative rewrite not done |
| Missing-topic gaps (FQH, Majorana, 21 cm, graviton-mass bounds) | Need **ingest**, not lint |
| Concept stub depth | Many concepts still short drafts |

---

## Log

- Entry appended to `wiki/log.md`.
