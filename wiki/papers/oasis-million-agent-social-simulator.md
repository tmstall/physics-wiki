---
tags: [papers, complex-systems, multiagent-ai, social-simulation, infrastructure]
last_updated: 2026-08-29
status: analysis-ingest
related_papers: [ai-agents-majority-following, emergent-social-conventions-llm-populations]
source_analysis: "raw/analyses/2026-08-27_arxiv-2411.11581_oasis-million-agent-social-simulator.md"
---

# OASIS: Million-Agent Open Social Interaction Simulator

**One-line summary:** Open-source LLM-agent social-media simulator (X-like and Reddit-like) scales from hundreds to one million concurrent agents; information cascades, polarization, and herd effects persist and visibly intensify around ~$10^{4}$ agents rather than washing out (arXiv:2411.11581).

## Key claims and results

- **Paper:** *OASIS: Open Agent Social Interaction Simulations with One Million Agents*, arXiv:2411.11581 (CAMEL-AI + partners; preprint as of analysis; code at github.com/camel-ai/oasis).
- Infrastructure: environment server (authoritative DB of users/posts/follows/votes), RecSys layer, LLM agent module (21 actions + chain-of-thought), time-of-day activation vectors, distributed asynchronous inferencer.
- Platforms: X-like interest matching (TwHIN-BERT) and Reddit-like hot-score ranking (platform’s public formula reimplemented).
- Large-scale agent brain: mostly Llama3-8b-instruct (cost-driven); GPT-4o-mini used as an *evaluator* for polarization scoring, not as the million-agent workforce.
- Replicated phenomena: (1) information propagation — ~30% NRMSE on cascade scale/breadth vs real data, worse on depth (authors blame simplified RecSys / missing intermediary users); (2) group polarization over ~80 steps, sharper for less safety-tuned models; (3) herd effects — early artificial up/down votes bias later voting, with a stronger pile-on in the *negative* direction than a human-literature baseline suggests.
- Scale sweep (discrete sizes 196; 10,196; 100,196, plus runs to $10^{6}$): group-level effects (opinion diversity / “helpfulness,” and by extension herd/polarization sharpness) strengthen once $N$ crosses roughly ~10,000 — an empirical inflection across sparse scale points, not a fitted critical exponent.
- “One million agents” is primarily an engineering throughput claim (same 8B model + seeded scale-free graph from anonymized user data), not a million richly authored distinct personas.

## Systems intuition

Think game-server architecture for a million LLM NPCs: one authoritative world state, many concurrent clients, a ranking layer deciding what each agent sees, and horizontal inference workers. Classical ABMs use thermostat-like if-then agents; OASIS swaps in junior-employee agents that read a persona/prompt handbook and generate free-text judgment each step — powerful but noisier and more context-window-fragile. The RecSys is a transparent cache/prefetch for attention: Reddit’s hot score is literally a log vote margin plus a decaying recency TTL. The scientific point is scale: small-$N$ LLM-agent papers can fit clean thresholds; OASIS asks whether those group behaviors survive when the sandbox approaches platform-adjacent populations.

## Limitations and assumptions

- Million-agent results use a single small open-source model; frontier-class agents untested at that scale.
- Sparse discrete $N$ grid → “~$10^{4}$” is an order-of-magnitude estimate, not a swept critical point.
- Cascade *depth* systematically underpredicted.
- “Herds more than humans (especially on downvotes)” leans on comparison to the broader human literature rather than a matched human RCT in the same protocol (verify methods before citing as head-to-head).
- Preprint; open-source adoption is usage-based scrutiny, not independent lab replication of the threshold/RMSE numbers.
- Simplified RecSys ≠ opaque production ranking trained on billions of real engagement signals.

## Connections

- Controlled small-$N$ mean-field consensus / $N_c$: [[ai-agents-majority-following]]
- Controlled naming-game convention + collective bias + committed-minority tipping: [[emergent-social-conventions-llm-populations]]
- Same genre, opposite method: those papers fit clean thresholds in instrumented toy games; OASIS scales a reusable platform sandbox and watches qualitative group behavior intensify.
- Synthesis: [[multi-agent-collective-ai]] (Thread C — platform-scale sandbox).
- Index: **Multi-agent systems & collective AI**.

## Open questions

- Does the ~$10^{4}$ inflection survive with frontier models and denser $N$ sampling?
- Can a richer RecSys close the cascade-depth gap?
- Matched human vs LLM herd protocols under identical up/down seeding?
- Independent re-runs of the scale-threshold and NRMSE claims on the open codebase?

## Source

- `raw/analyses/2026-08-27_arxiv-2411.11581_oasis-million-agent-social-simulator.md`
