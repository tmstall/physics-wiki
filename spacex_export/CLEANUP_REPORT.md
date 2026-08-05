# SpaceX attention-list cleanup report

**Date:** 2026-08-04  
**Catalog after cleanup:** 156 papers · 61 concepts · 5 synthesis (unchanged counts)  
**Scope:** No new ingest. No new synthesis or concept stubs.

---

## 1. `rhic-net-proton-fluctuations`

| Item | Detail |
| --- | --- |
| **Issue** | Extract mixed a usable STAR abstract with off-topic “context rot” chat noise; citation was vague (“PRL-style 2025”). |
| **Check** | Verified against **arXiv:2504.00817** (STAR Collaboration, 2025). |
| **Changes** | Rewrote claims from the primary abstract/body; fixed citation; noted BES-II **does not** support non-monotonic $C_4/C_2$ vs Poisson (stays below unity); the reported structure is a **minimum in significance of deviation** (~2–5σ) from non-critical / peripheral baselines near 19.6 GeV; added energies, acceptance, statistics context. |
| **Outcome** | Page is primary-aligned; extract noise annotated as discarded. |

## 2. `emc-effect-marathon-a3`

| Item | Detail |
| --- | --- |
| **Issue** | Conversational extract; gradual paper identification; risk of “isospin medium effect” overclaim. |
| **Check** | Verified against **arXiv:2410.12099** (Abrams et al., MARATHON). |
| **Changes** | Locked kinematics ($x=0.20$–$0.83$, $Q^2=2.7$–$11.9$ GeV², $E=10.59$ GeV); first-tritium claim kept; slopes $^3$He $-0.085\pm0.037$, $^3$H $-0.10\pm0.04$; **corrected** narrative: data agree with **isoscalar** K-P off-shell model and **do not** support a sizable **isovector** EMC component (contra conversational drift). |
| **Outcome** | Page retied to primary; source quality note in front matter. |

## 3. `na61-isospin-kaon-asymmetry`

| Item | Detail |
| --- | --- |
| **Issue** | Extract **filename/title** = “Nuclear Magnetization Observation Breakthrough”; body = NA61 kaon isospin paper. |
| **Check** | Content matches NA61/SHINE *Nat. Commun.* DOI 10.1038/s41467-025-57234-6 ($R_K=1.184\pm0.061$, Ar+Sc @ 11.9 GeV). |
| **Changes** | Strengthened limitations + source section: explicit **filename mismatch** warning; primary DOI listed; note that TRIAGE “nuclear magnetization” NEW handle was consumed by this mislabeled extract (bookkeeping quirk, not a second paper). Content claims unchanged (already correct). |
| **Outcome** | Future readers cannot confuse this page with nuclear magnetization. |

## 4. Shorter pages (heliknoton, positronium)

| Page | Change |
| --- | --- |
| `magnetic-heliknoton-electric-write` | Added clarifying connection: 3D Hopf knots vs 2D skyrmion racetracks; cross-link to [[nonabelian-photonic-braiding]] as another “write topology” platform. |
| `positronium-diffraction-graphene` | Added sentence that Ps diffracts as **one** $2m_e$ de Broglie object; link to [[evanescent-wave-transverse-spin]] as interface-wave cousin. |

## 5. Speculative gravity pages

| Page | Change |
| --- | --- |
| `five-dimensional-classical-gravity` | `status: exploratory`; `speculative` tag; **blockquote disclaimer** at top; limitations: not standard GR/QFT; do not cite as established. |
| `temporal-imbalance-gravity` | Same treatment; explicit note that lab quantum-clock programs do **not** depend on this framework. |

## 6. Light link check — last 7 NEW pages

| Page | Result |
| --- | --- |
| `axion-detector-quantum-erasure` | Links resolve; added one clarifying detector-classicalization sentence. |
| `five-dimensional-classical-gravity` | Links resolve; disclaimer strengthened (item 5). |
| `jwst-ulirg-hydrocarbons` | Links resolve; no change. |
| `phosphorus-radical-hydroamination` | Links resolve; no change. |
| `warp-drive-positive-energy` | Links resolve; added nearby speculative-GR pointers (5D, temporal imbalance) for cluster cohesion. |
| `temporal-imbalance-gravity` | Links resolve; disclaimer strengthened (item 5). |
| `evanescent-wave-transverse-spin` | Links resolve; no change. |

Automated check: **all wikilinks on the last 7 pages resolve** to existing paper/concept/synthesis files.

---

## Not done (by design)

- No new concept stubs
- No new synthesis pages
- No new paper ingest
- Catalog numbers unchanged: **156 / 61 / 5**

## Residual notes (non-blocking)

- “Nuclear magnetization” as a real experimental paper was never present in the extract body; if that topic is desired later, it needs a correct primary source, not the mislabeled file.
- RHIC / EMC quantitative tables remain analysis-light; full supplemental tables not mirrored (by design — math-light wiki policy).
