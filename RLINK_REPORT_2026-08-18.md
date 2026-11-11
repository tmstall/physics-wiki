# Full reverse-link (rlink) audit — 2026-08-18

**Catalog:** **167 papers · 61 concepts · 9 synthesis**  
**Scope:** Exhaustive bidirectional link check across `wiki/papers/`, `wiki/concepts/`, `wiki/synthesis/`.  
**`raw/` untouched.**

---

## Final metrics

| Check | Before this pass | After |
| --- | --- | --- |
| Paper ↔ paper asymmetries | 15 (inline YAML related_papers visible after parser fix) | **0** |
| True orphans (excl. index/log) | 0 | **0** |
| Paper → concept missing reverse | 0 | **0** |
| Paper → synth missing reverse | 0 | **0** |
| Synth → paper missing reverse | 41 | **0** |
| Unresolved wikilink targets | 0 | **0** |

Prior session (partial) had already closed most paper↔paper edges under a stricter body-only scan; re-audit with inline `related_papers: [...]` parsing exposed the remaining 15 asymmetries plus 41 synthesis reverse gaps.

---

## What was fixed

### 1. Paper ↔ paper (15 Reverse-link lines)

Added `- Reverse-link: [[source]]` on the missing side under `## Connections`:

| Target page | Gains reverse from |
| --- | --- |
| `levinthal-high-pt-isr` | `b-meson-fcnc-anomaly` |
| `entropy-maximization-bh-mergers` | `black-hole-third-law-violation` |
| `negative-weak-valued-excitation-times` | `collapse-models-clock-precision` |
| `lab-blazar-pair-instability` | `cygnus-x3-pevatron-bubble` |
| `b-meson-fcnc-anomaly` | `eta-prime-mesic-nucleus`, `star-jpsi-spin-interference` |
| `jwst-filament-cnd-ngc4696` | `glimpse-17775-cocoon` |
| `high-z-quasar-pair-merger` | `horizon-direct-wave-gw250114` |
| `mrk501-double-jet-smbbh` | `horizon-direct-wave-gw250114` |
| `shor-algorithm-budget` | `noise-driven-qubit-entanglement` |
| `siv-hydrostatic-strain-symmetry` | `photonic-supersolid` |
| `desi-evolving-dark-energy` | `quantum-damping-cosmological-shear`, `second-order-gw-strain-gauge` |
| `frozen-in-gravitational-fields` | `smbh-inclination-angle` |
| `hawking-radiation-charge-shell` | `smbh-inclination-angle` |

### 2. Synthesis → paper (41 Synthesis lines)

Added `- Synthesis: [[synth-slug]]` on paper pages that synthesis maps cited in YAML / body but that did not yet point back. Touch clusters:

- **amo-quantum-state-control** (4): certified-randomness, sunlight-spdc, truncated-photon-DCE, two-clocks-one-laser
- **black-hole-evaporation-energy-conditions** (2): qg-deep-dive-3, quantum-jamming
- **black-hole-feedback-and-changing-look-agn** (1): dr21-magnetic-accretion
- **condensed-matter-topology-fractionalization** (8): BaTa₂S₅, nickelate ARPES, photonic supersolid, quantum-metallurgy-cdw, SnTe, spin-flip-flop, three-body, twisted-light MS
- **high-energy-astrophysics-multimessenger** (11): beyond-iron, category-79, cosmos-web, dense-plasma, DESI, DR21, Euclid, gamma-glow PBH, high-z pair, interstellar sulfur, Peters cycle
- **measurement-problem-threads** (1): quantum-state-sculptor
- **modified-speculative-gravity** (11): Alena tensor, third-law, evaporating RN, frozen-in, gravastar, Hawking charge-shell, Newton–kSZ, problem-of-time, quantum proper time, retrocausal channel, topological Λ
- **nuclear-dense-matter-precision** (2): b-meson FCNC, Levinthal ISR
- **quantum-time-across-platforms** (1): collective-superradiant-lasing

**47 paper files** touched in total (some received both paper and synth reverse lines).

---

## Method notes

- Wikilinks `[[slug]]` / `[[slug|display]]` plus YAML `related_papers` (inline lists and block lists) count as outbound edges.
- Orphan = paper with no inbound from any other paper/concept/synthesis page (index/log excluded).
- Concept and synth hubs already held the complementary `related_papers` entries; remaining work was mostly paper-side `Reverse-link` / `Synthesis` lines.
- Reusable auditor: `_rlink_audit.py` (repo root).

---

## Deferred (non-blocking)

| Item | Note |
| --- | --- |
| `quantum-jamming` dual paper/concept slug | Known; not renamed this pass |
| Synthesis prose depth for new reverse edges | Links only; no narrative rewrite |
| Concept stub depth | Unchanged |
| Entity / subfield pages | Still empty dirs |

---

## Log

- Entry appended to `wiki/log.md`.
