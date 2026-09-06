---
tags: [synthesis, multiagent-ai, complex-systems, collective-behavior, llm-agents]
last_updated: 2026-09-05
status: synthesis
related_papers: [ai-agents-majority-following, emergent-social-conventions-llm-populations, oasis-million-agent-social-simulator, urban-congestion-routing-app, extracting-reasoning-traces-proprietary-llms, deepmind-hurricane-forecasting]
---

# Multi-Agent Systems and Collective AI

**One-line summary:** This wiki’s LLM-agent papers form one systems ladder — **does a group lock**, **what label does it lock onto (and how fragile is that)**, and **do those group effects survive at platform-adjacent scale** — plus a **human-network contrast** (routing apps / selfish vs system-optimal traffic) — without pretending the agents are spins or that social media is a Hamiltonian.

## Why pull these together

Four papers are enough for a hub when they answer adjacent questions with incompatible methods:

| Question | Paper | Method |
| --- | --- | --- |
| Will this group coordinate at all, and up to what size? | [[ai-agents-majority-following]] | Controlled binary-opinion game; Curie–Weiss / Glauber fit → $N_c$ |
| Given that it coordinates, *which* convention wins, and can a tiny minority flip it? | [[emergent-social-conventions-llm-populations]] | Naming game; win-stay/lose-shift; collective bias; committed minority |
| Do herd / polarization / cascade effects intensify rather than wash out as $N\to 10^{4}$–$10^{6}$? | [[oasis-million-agent-social-simulator]] | Open platform sandbox (X-like / Reddit-like); engineering scale + qualitative phenomena |
| Can a production router nudge *human* traffic from selfish toward system-optimal paths? | [[urban-congestion-routing-app]] | Live Google Maps field experiment; shadow tolls; ten US cities |

They belong in **one vault** with the physics wiki (Karpathy pattern): same ingest bar, same honesty about limits, optional analogies only when they earn their keep. They do **not** belong inside [[measurement-problem-threads]] or [[amo-quantum-state-control]].

**Out of scope here:** single-agent prompting tricks and model-card evals without a population — **except** provider-infra security that leaks *population-scale* agent traces (Thread E). Human field experiments *are* in scope when they share the collective-coordination question (Thread D). Pure NWP / weather-ML (Thread F) sits as a complex-systems cousin, not an LLM-agent result. Unrelated Earth-system one-offs (e.g. [[tc-vertical-alignment]]) stay Islands.

---

## Shared systems picture

Think of three layers of a distributed system:

1. **Consensus machinery** — will replicas converge, and does convergence fail past a scale? ([[ai-agents-majority-following]])
2. **Payload / schema** — once they talk, which string becomes the shared name, and how poisonable is that choice? ([[emergent-social-conventions-llm-populations]])
3. **Production deployment** — does the phenomenon still matter when the “cluster” looks like a social network with a recommender, not a fully connected toy? ([[oasis-million-agent-social-simulator]])

**Intuition:** Small-$N$ instrumented games give clean thresholds ($\beta$, $N_c$, critical-mass %). Large-$N$ sandboxes give existence proofs that group pathologies intensify. Neither replaces the other.

---

## Thread A — Majority lock-in and critical size

**Paper:** [[ai-agents-majority-following]]

Across ten LLM architectures, majority-adoption probability vs magnetization collapses onto a Curie–Weiss / Glauber form after a model-specific majority force $\beta$. That single parameter predicts a critical group size $N_c$ beyond which full coordination splinters (Llama 3 70B ~30; GPT-4o ~80; some frontier models extrapolated $\gtrsim1000$).

**Intuition:** Fully connected peer lists act like mean-field coupling. Stronger $\beta$ locks small groups; larger $N$ makes the fluctuation needed for unanimous lock rarer.

**Limits:** Binary opinions, no topology/memory/stakes; closed models can drift under the same API name; largest $N_c$ values are extrapolations.

**Safety read:** “More capable → larger coherent mob” is the correlated MMLU–$\beta$ worry, not a theorem about real institutions.

---

## Thread B — Convention choice, collective bias, tipping

**Paper:** [[emergent-social-conventions-llm-populations]]

Unstructured naming-game populations invent a shared label in ~15 rounds. Microscopic behavior approximates win-stay / lose-shift. Individuals can look fair in isolation while the population outcome is strongly biased. A committed minority (reported range ~2%–~67%, model- and convention-dependent) can flip the group.

**Intuition:** Leaderless gossip with a hijackable tiebreaker. Early lucky matches snowball; committed agents are a poisoning attack with a non-universal tipping fraction.

**Relation to Thread A:** A asks *whether* consensus locks and *until what $N$*. B assumes interaction continues and asks *which attractor* and *how fragile*. Different games; same population-safety genre.

**Limits:** Toy letter conventions; uniform random pairing; single-group study; verify extreme critical-mass percentages against the supplement before citing a single number.

---

## Thread C — Platform-scale sandbox

**Paper:** [[oasis-million-agent-social-simulator]]

OASIS is infrastructure: environment server, RecSys, LLM agents, distributed inference — X-like and Reddit-like modes, up to ~$10^{6}$ concurrent agents (mostly Llama3-8B workforce). Cascades, polarization, and herd effects persist; group-level measures intensify around an empirical ~$10^{4}$ inflection on a sparse $N$ grid.

**Intuition:** Game-server architecture for a million LLM NPCs. Thread A/B fit thermostats in a lab; OASIS asks whether the weather still matters in a city.

**Relation to A/B:** Opposite method — reusable platform vs instrumented toy. Cascade *depth* underpredicted; “herds more than humans” needs matched-protocol caution; million-agent claim is throughput + seeded graph, not a million rich personas.

**Limits:** Preprint; small open model at extreme $N$; simplified RecSys ≠ production ranking.

---

## Thread D — Human network coordination (routing contrast)

**Paper:** [[urban-congestion-routing-app]]

Not an LLM-agent paper. Google Maps ran a six-month, ten-city switchback experiment that added internal “shadow tolls” so some recommended routes were slightly worse for the individual driver and better for the city (Wardrop / price-of-anarchy territory). Targeted segments gained ~2% median speed; CO₂ savings are median-positive but tail-uncertain. Proprietary data; unreplicated mechanism at this scale.

**Intuition:** Threads A–C ask how *synthetic* agents coordinate. Thread D asks whether a production system can steer *human* agents away from selfish equilibrium without building roads or charging real money.

**Relation to A–C:** Same systems genre (collective inefficiency under local optimization); different substrate (drivers + Maps, not chat models). Do **not** cite Curie–Weiss $N_c$ as explaining traffic; do cite price-of-anarchy / load-balancing intuition when comparing “what a coordinator can buy.”

**Limits:** In-house Google study; capped heuristic ≠ solved system optimum; consent/disclosure issues in the source analysis.

---

## Thread E — Reasoning-trace security (provider infra)

**Paper:** [[extracting-reasoning-traces-proprietary-llms]]

Not a population-dynamics paper. Encrypted “reasoning” blobs from frontier APIs can be read aloud by cheaper models that share the provider’s decryption context (~$720 attack budget in the analysis). AEAD protects transit eavesdroppers, not same-infra decryption. Published agent traces can leak PII and secrets users thought they had sanitized from visible chat.

**Relation to A–C:** Threads A–C study what *groups of agents do*. Thread E studies what *providers leak about those agents’ private scratchpads*. Same vault because agent deployments are the threat surface; different science (security/crypto boundary vs coordination).

**Limits:** Provider-specific; mitigations (context binding) may ship; do not treat as a permanent universal break.

---

## Thread F — Weather ML cousin (not LLM agents)

**Paper:** [[deepmind-hurricane-forecasting]]

WN-C-style cyclone forecasting: one model competitive on track *and* intensity; large fast ensembles; NHC operational use reported. Lives in the multi-agent **index section** as complex-systems / ML forecasting, next to [[tc-vertical-alignment]]’s observational cousin — **not** as an LLM-population result.

**Limits:** Not agent coordination; do not cite as evidence for Threads A–C.

---

## Comparative map

| Axis | Majority / $N_c$ | Conventions / bias | OASIS scale | Urban routing | Trace security | Weather ML |
| --- | --- | --- | --- | --- | --- | --- |
| Primary output | $\beta$, $N_c$ | Winning label, tipping % | Phenomena vs $N$, NRMSE | ~2% speed; trip/CO₂ proxies | Decryptability / leak demos | Track + intensity skill |
| Interaction graph | Fully connected | Random pairwise | Scale-free / platform graph | City road network | Provider API / shared keys | Atmosphere / NWP data |
| Agent brain | Many model families | Several 70B-class chat models | Mostly 8B at $10^{6}$ | Human drivers + Maps | Frontier + cheap siblings | Weather foundation model |
| Falsifiable handle | Collapse of $P(m)$ / measured $N_c$ | Critical-mass curves; bias vs isolation fairness | Scale sweep; cascade stats vs real data | New cities / longer rollout | Patched binding / new providers | Independent seasons / centers |
| Main wound | Extrapolated large $N_c$; binary toy | Exact % verify; toy norms | Sparse $N$ grid; RecSys simplicity | Proprietary data; CO₂ tails | Vendor-specific; arms race | Not an agent-pop result |

---

## Tensions and open questions

1. **Do $N_c$ and the ~$10^{4}$ OASIS inflection talk about the same scale physics?** Probably not yet — different observables, graphs, and models. Bridging experiment: run Thread A’s protocol inside OASIS-like topology at overlapping $N$.
2. **What sets $\beta$ and basin depth?** Training / RLHF / prompting — still largely unknown.
3. **Topology:** Sparse or hub-dominated contact graphs should move both coordination and tipping thresholds (naming-game literature already says so for non-LLM agents).
4. **Replication:** Closed-model drift and single-group studies dominate; OASIS’s open code is the easiest external stress test.
5. **Human baseline:** Matched human vs LLM herd protocols under identical seeds — still thin. Thread D is a *different* human baseline (traffic, not opinion games).
6. **Can LLM populations learn system-optimal routing?** Open bridge between A–C toys and D’s production shadow-toll idea — not claimed by any current page.

---

## How to use this hub

- Reading for **coordination risk / group size** → start Thread A.
- Reading for **norm formation / minority takeover** → Thread B.
- Reading for **engineering scale / platform phenomena** → Thread C.
- Reading for **human selfish vs system-optimal networks** → Thread D.
- Reading for **encrypted reasoning / agent-trace leaks** → Thread E.
- Reading for **operational weather ML** (cousin only) → Thread F / [[deepmind-hurricane-forecasting]].
- Do **not** cite Curie–Weiss language from A as a claim that OASIS agents are Ising spins, or that traffic obeys $N_c$.
- Future papers in this cluster should land in the index section **Multi-agent systems & collective AI** and add a row here when they change a thread’s conclusion.

## Related wiki neighbors (optional, non-load-bearing)

- Collective / mean-field *control* culture (different physics): [[amo-quantum-state-control]]
- Island graduation policy: true one-offs stay Islands until ≥2–3 related papers + a clear reader question exist (`AGENTS.md`)
