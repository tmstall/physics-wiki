---
tags: [papers, elementary-functions, symbolic-computation, preprint]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [lean-proof-assistant, deep-relu-statmech-realization]
source_analysis: "raw/analyses/2026-11-11_arxiv-2603.21852_eml-single-operator-elementary-functions.md"
---

# One Binary Operator for the Elementary Functions

**One-line summary:** $\mathrm{eml}(x,y) = e^{x} - \ln y$, plus the constant 1, builds the elementary functions by hand-checkable trees; the circuits are numerically fragile, and symbolic regression recovers them reliably only to depth 2. Odrzywołek, arXiv:2603.21852v2.

## Key claims and results

- **Source:** A. Odrzywołek, “All elementary functions from a single binary operator,” arXiv:2603.21852v2 (4 Apr 2026). Single-author preprint. The wiki page follows a plain-language primer, not a full Framework pass. Supplementary formal verification was not read. Some extracted table cells are garbled.
- The operator is a Sheffer stroke for the calculator: with the constant 1 it produces $e$, $\exp$, $\ln$, arithmetic, powers, roots, trigonometric functions, and $e$, $\pi$, and $i$. Example: $\mathrm{eml}(1,1) = e$, and $\mathrm{eml}(x,1) = e^{x}$.
- Three conditions: the constant 1 is an extra input (unlike NAND, which needs no constant bit), intermediate values are complex, and branches and infinities have to be fixed by convention. The completeness argument is the author’s proof sketch.
- Evaluation cost is worse than calling the functions directly. Exact symbolic recovery is reliable to depth 2, partial at depths 3–4, and fails beyond that without a good initialization. Relatives (EDL, −EML) need their own constants. A ternary gate that might supply its own constant is marked “in preparation.”

## Physical intuition

NAND trees build every digital circuit because one gate is functionally complete. Continuous math did not have that gate. EML is a choice of basis: exp and log are inverses in a way that lets subtraction, then addition and multiplication, fall out of nested calls. It does not reveal a new property of sine or of $\pi$. It shows those buttons are one button plus wiring.

## Limitations and assumptions

- Not formally verified in the main text.
- No computational advantage. Fragile numerics.
- Regression results are a proof of concept on small depths.

## Connections

- A different “the machine checked it” story: [[lean-proof-assistant]]
- Another exact identity that is not a new physical law: [[deep-relu-statmech-realization]]
- Islands shelf (formal mathematics). No concept page.

## Source

- `raw/analyses/2026-11-11_arxiv-2603.21852_eml-single-operator-elementary-functions.md`
