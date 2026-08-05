# Light global lint + index polish

**Date:** 2026-08-04  
**Catalog after polish:** **156 papers · 61 concepts · 9 synthesis** (unchanged counts)  
**Scope:** Index hygiene, light reverse-link spot-check, front-matter scan. No new pages. No deepening.

---

## 1. Index fixes made

### Primary issue: duplicate “Wave-2 export papers” batch table
- Legacy section listed 36 papers again after they had already been placed (or partially placed) in topical clusters.
- **21 paper slugs** appeared twice in `wiki/index.md` solely because of that batch table.

### Fixes
1. **Folded 16 Wave-2-only papers** into correct existing clusters (they had lived only in the batch table):
   - **Quantum metrology:** `mot-metal-hydride`, `molecular-rotation-superfluid-he`
   - **Quantum foundations:** `color-space-geometry`
   - **Black holes / GR:** `radio-changing-look-agn`, `glimpse-17775-cocoon`, `qg-deep-dive-1`…`4`
   - **Solid-state / optics:** `topo-chirality-structured-light`, `confinement-stiffening-films`, `metal-fall-apart-on-purpose`
   - **QCD / nuclear:** `nucleus-tells-on-itself`
   - **Chemistry islands:** `ultrafast-chemical-shifts`, `two-lasers-one-reaction`, `molecular-bias-point`
2. **Removed** the duplicate Wave-2 paper table.
3. **Replaced** with a short **Inbox / provenance status** table (Claude waves + SpaceX complete; no re-list of papers).
4. **Clarified** `quantum-jamming` concept row (paper + concept hub share the slug; both listings intentional).
5. **Header** updated to note index polish / Wave-2 fold-in.

### Verification
- **0** paper pages missing from index.
- **0** paper pages with multi-cluster *paper* duplicates after fold-in (only dual listing: `quantum-jamming` paper + concept).
- **All 9** synthesis pages listed once in the Synthesis section.

---

## 2. Link fixes made

### Spot-check (not exhaustive)
- High-value reverse links present for recent synthesis cores:
  - topology fractionalization (anyon-trions, supermoiré, 1d-anyons)
  - multi-messenger (magnetar SLSN, ice $^{60}$Fe, MUSE)
  - nuclear precision (RHIC, EMC, NA61)
  - modified gravity (dRGT, warp, temporal imbalance)
  - BH feedback (filament, Category-79, radio changing-look, GLIMPSE)
- Concept hubs with synthesis pointers already in place: `cosmic-web`, `magnons`, `null-energy-condition`, `dark-energy-equation-of-state`.

### Single high-value add this pass
- `desi-evolving-dark-energy` → [[modified-speculative-gravity]] (fluid DE vs IR modified-gravity competition).

No broken `[[wikilinks]]` found among the spot-checked sets.

---

## 3. Front-matter / consistency

- Scan of all `wiki/papers/*.md`: **no** missing YAML front-matter, `tags`, `status`, or H1 title defects.
- Exploratory pages (`five-dimensional-classical-gravity`, `temporal-imbalance-gravity`) already carry explicit non-consensus disclaimers — left unchanged.

---

## 4. Remaining minor issues (deferred to deepening)

| Item | Note |
| --- | --- |
| Thin / short paper pages | e.g. some chemistry islands, color-space-geometry, partial analysis pages — not deepened this pass |
| Exhaustive reverse-link audit | Only spot-check; older papers may still lack synthesis back-links |
| `quantum-jamming` dual slug | Paper + concept share name — works in Obsidian; optional rename later for clarity |
| Concept stubs still thin | Many concept pages remain short drafts by design |
| Attention items already cleaned | RHIC/EMC/NA61/speculative gravity — no further change |
| Synthesis count vs depth | 9 synthesis pages exist; content deepening not requested |

---

## Log

- Entry appended to `wiki/log.md` under polish pass.
