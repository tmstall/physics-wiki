---
tags: [papers, complex-systems, multiagent-ai, collective-bias, naming-game]
last_updated: 2026-08-29
status: analysis-ingest
related_papers: [ai-agents-majority-following, oasis-million-agent-social-simulator]
source_analysis: "raw/analyses/2026-08-26_doi-10.1126-sciadv.adu9368_emergent-social-conventions-collective-bias-llm-populations.md"
---

# Emergent Social Conventions and Collective Bias in LLM Populations

**One-line summary:** Unstructured populations of LLM agents spontaneously invent a shared naming convention in ~15 pairwise rounds; the outcome can be collectively biased even when individuals look fair in isolation, and a committed minority as small as ~2% can flip the whole group (*Sci. Adv.* / arXiv 2410.08948).

## Key claims and results

- **Paper:** Ashery, Aiello & Baronchelli, *Science Advances* (DOI 10.1126/sciadv.adu9368); arXiv companion 2410.08948v2.
- Protocol: naming game — $N=24$ (robustness $N=200$) agents, random pairwise meetings, reward $+100$ on match / $-50$ on mismatch, private memory of last $H=5$ interactions; name pool $W=10$ (also $W=2$, $W=26$).
- Models tested: Llama-2-70b-Chat, Llama-3-70B-Instruct, Llama-3.1-70B-Instruct, Claude-3.5-Sonnet.
- Three of four models reach a dominant convention by ~population round 15; Llama-2 converges more slowly or incompletely in the same window.
- Microscopic rule that emerges without programming: win-stay ~99.4%, lose-shift ~97.3% — the same reinforcement naming-game physics models assume by construction.
- **Collective bias:** for some $W=2$ pairs, round-1 / empty-memory preference is consistent with a coin flip, yet repeated interaction still yields strongly lopsided population outcomes across runs.
- **Critical mass:** committed agents that always push a fixed alternative tip the population once their fraction crosses a model- and convention-dependent threshold — reported range roughly ~2% to ~67%; stronger conventions need larger minorities; Llama-3.1 can abandon a weak convention with *zero* committed adversaries.
- Exact headcount→percentage mapping for the extreme critical-mass figures should be checked against the paper’s Table S3 / Fig. 3B (analysis flagged a retrieval discrepancy between extraction passes).

## Systems intuition

This is a leaderless gossip protocol with a hijackable tiebreaker. Each agent only sees its own interaction log — never the global vote tally — yet pairwise anti-entropy still drives eventual consistency on one shared label. Early lucky matches snowball via win-stay/lose-shift the way a warm cache replica attracts more traffic after a tiny timing asymmetry. A committed minority is a poisoning attack: non-adaptive nodes that always broadcast one fixed value. Unlike textbook BFT, the tipping fraction is not a designed constant; it swings by more than 30× across models.

## Limitations and assumptions

- Numbers bound to the tested models, prompt template, and toy letter/string conventions — authors say so explicitly.
- Population is unstructured (uniform random pairing); real multi-agent deployments have network topology that naming-game literature already knows changes convergence and reachable outcomes.
- Conventions are toy labels, not socially loaded norms; mechanism demo, not yet a deployed-harm case.
- Single research group; no outside-lab replication; frontier GPT/Gemini-class agents not in the tested set.
- Critical-mass percentages: treat qualitative shape (huge, model-dependent range; strong-vs-weak asymmetry) as solid; treat any single exact % as verify-against-supplement before citing.

## Connections

- Closest wiki cousin — different game, same population-safety worry: [[ai-agents-majority-following]] (Curie–Weiss majority force / $N_c$; asks *whether* consensus locks; this paper assumes consensus and asks *what* it lands on and *how fragile* it is).
- Platform-scale infrastructure / herd & polarization at large $N$: [[oasis-million-agent-social-simulator]].
- Synthesis: [[multi-agent-collective-ai]] (Thread B — conventions / bias / tipping).
- Index: **Multi-agent systems & collective AI**.

## Open questions

- How do critical-mass thresholds move under sparse, clustered, or hub-dominated contact graphs?
- Do socially loaded conventions (identity, norms) preserve the individual–collective bias dissociation?
- Independent replications on newer model generations with the same protocol?
- What training / prompting ingredients set basin depth for a given convention?

## Source

- `raw/analyses/2026-08-26_doi-10.1126-sciadv.adu9368_emergent-social-conventions-collective-bias-llm-populations.md`
