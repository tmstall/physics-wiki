---
tags: [papers, machine-learning, scaling-laws, transformers, architecture]
last_updated: 2026-10-09
status: analysis-ingest
related_papers: [extracting-reasoning-traces-proprietary-llms, deep-relu-statmech-realization, oasis-million-agent-social-simulator]
source_analysis: "raw/analyses/2026-10-09_arxiv-2609.19107_model-growth-looping-scaling-exponents.md"
---

# Model Growth, Looping, and Scaling Exponents

**One-line summary:** On two decades of language-model compute, adding depth mid-training and a normalize-and-reinject “boundary operator” make the compute-optimal loss curve *steeper*, not just lower; the best variant needs ~1.55× less compute at the top of the measured ladder. Chen, Vegesna, Dahal & Wilson, arXiv:2609.19107 v2.

## Key claims and results

- **Paper:** Zixi Chen, Akshay Vegesna, Samip Dahal, Andrew Gordon Wilson (NYU / Q Labs), arXiv:2609.19107 v2 (17 Sep 2026). Code: github.com/qlabs-eng/scaling-exponents. Empirical scaling study; one seed per ladder point; no journal reference.
- Family: prelude–core–coda transformer. Three isolated switches: boundary operator (normalize residual stream, add back prelude output), weight sharing vs untying, growth (2 → 4 core passes mid-training). Each variant gets its own compute-optimal recipe (tokens/param, growth timing, LR rule). Giving the operator model the *standard* recipe erases the exponent gain.
- Fit: $L(C) = E + A(C/C_0)^{-\gamma}$ with one shared floor $E$ from the vanilla model. Headline readout is the **compute multiplier** (how many times more compute vanilla needs for the same loss). A constant gain is a flat multiplier; an exponent gain rises with scale.
- At the top of the ~10¹⁸–10²⁰ FLOP ladder: deeper-plain control ~1.08× (constant); operator-only ~1.25× (exponent); untied two-pass ~1.34×; tied growth ~1.35×; untied growth **1.55×**. Fitted exponent gap is ~1 part in 20; fit-free multipliers imply a gap ~1/5 smaller. Direction stands.
- Held-out 7.4B untied-growth run at ~8× the fitted compute lands slightly *better* than its own forecast. Projected advantage ~1.8× at that budget, ~2.7× at a frontier budget (shared-floor extrapolation). No vanilla model was trained at the held-out budget, so the gap is between two extrapolations.
- Repeated-data regime (100M unique tokens, 10 epochs): best loop count climbs from ~1 to ~7 with compute. Extra loops beat extra width at matched compute (~2.2×), even with retuned weight decay. Untied same-depth control does not win — sharing, not depth alone, helps when data repeats.
- Interpretation: compute spent on depth is wasted as (i) late blocks that barely move a growing residual stream (“curse of depth”) and (ii) full depth paid from step one while the net still needs a shallow program. Operator attacks (i); growth attacks (ii). KL effective depth (logit lens) roughly doubles for growth models at the top of the ladder.

## Physical intuition

A decade of lore says architecture moves the constant (a faster clock) and data/task set the exponent (a better complexity class). This paper treats that lore as a tuning failure: if every variant is Chinchilla-tuned on its own, two cheap depth fixes steepen the frontier.

The residual stream is a running total that every block adds to. Once the total is large, a late delta barely moves it. The boundary operator rescales the register back to unit size and re-injects the original request, so each pass still counts. Growth is tiered compilation: run a cheap shallow net until the workload needs depth, then copy the core and keep training.

A rising compute multiplier is the plot that makes a 5% exponent gap look like real money. A lower floor with the *same* exponent also produces a rising multiplier; the paper rules that out by *assumption* (one shared $E$).

## Limitations and assumptions

- Single lab, one seed per point, two decades of compute, web text. Nobody has tested growth’s slope claim at 10× this budget. Nearby work (Schwethelm et al.) agrees that *weight sharing alone* does not steepen the slope.
- Shared-floor fit is load-bearing. A variant with a lower irreducible loss and vanilla’s exponent would also show a rising multiplier inside the window and then diverge on extrapolation (analyst explainer). Quoted exponents slightly overstate the fit-free multiplier growth.
- Frontier 2.7× is an extrapolation of a small exponent gap over many decades. The 7.4B run tests the growth law against itself, not against a matched vanilla at that budget.
- CORE benchmark match to GPT-3 13B is indicative only (different data, eval, five-year-old baseline).
- Not a collective-AI result. It is architecture/scaling for a single transformer; lives next to LLM-agent pages as a training-economics cousin.

## Connections

- Provider-infra / LLM systems neighbor: [[extracting-reasoning-traces-proprietary-llms]]
- Stat-mech exact ReLU mapping (theory cousin, not a scaling law): [[deep-relu-statmech-realization]]
- Population-scale LLM deployment (different question): [[oasis-million-agent-social-simulator]]
- Islands ML/computation shelf; no synthesis hub yet

## Open questions

- Second lab, separately tuned vanilla vs untied-growth, to ≥10× this compute, multiplier still rising?
- Does the shared-floor assumption survive a joint fit of $E$ per family?
- Growth timing vs Liew & Kato’s finding that the benefit shrinks the longer the base was pretrained?

## Source

- `raw/analyses/2026-10-09_arxiv-2609.19107_model-growth-looping-scaling-exponents.md`
