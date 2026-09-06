---
tags: [papers, complex-systems, multiagent-ai, statistical-mechanics]
last_updated: 2026-08-29
status: analysis-ingest
related_papers: [emergent-social-conventions-llm-populations, oasis-million-agent-social-simulator]
source_analysis: "raw/analyses/2026-08-18_doi-10.1126-sciadv-aea6091_ai-agents-majority-following-coordination.md"
---

# AI Agent Groups Coordinate Like a Curie–Weiss Ferromagnet

**One-line summary:** Across ten LLM architectures, emergent majority-following in fully connected agent groups collapses onto the Curie–Weiss / Glauber $P(m)=\tfrac12[\tanh(\beta m)+1]$ law; a single majority-force $\beta$ predicts critical group size $N_c$ before coordination splinters (*Sci. Adv.* 2026).

## Key claims and results

- **Paper:** De Marzo, Castellano & Garcia, *Science Advances* **12**(33), eaea6091 (2026). DOI 10.1126/sciadv.aea6091.
- Protocol: $N=10$–$1000+$ agents, binary opinions, asynchronous updates, **no** instruction to follow the majority — only a peer-opinion list.
- Universal fit of majority-adoption probability vs magnetization $m$; curves collapse after rescaling by model-specific $\beta$ (GPT-3.5 Turbo is the outlier: anti-majority at small $m$).
- Equilibrium $m^*=\tanh(\beta m^*)$; coordination time crossover $\beta_t(N)\approx\tfrac12\log N$ → critical size $N_c$.
- Examples: Llama 3 70B $N_c\sim30$; GPT-4o $\sim80$; Claude 3.5 Sonnet / GPT-4 Turbo **extrapolated** $N_c\gtrsim1000$ (lower bounds; largest runs expensive).
- MMLU correlates with $\beta$ and $N_c$ ($r\approx0.79$).
- Recursive splitting of uncoordinated large groups empirically confirms the size transition.

## Physical intuition

Treat each agent’s opinion as a spin. Fully connected majority pull is mean-field ferromagnetism: below a critical “inverse temperature” $\beta$, the group stays disordered; above it, consensus snaps. Larger $N$ makes the fluctuation needed for *full* lock-in rarer — so even a strong majority force eventually fails past $N_c$. The surprise is how cleanly black-box LLMs from different labs sit on one solvable physics curve.

## Limitations and assumptions

- Single research team; no independent lab replication yet.
- Closed models (GPT/Claude) can change silently under the same API name.
- Binary opinions, no memory/stakes/network topology — phenomenological, not a cognitive model of humans.
- Largest $N_c$ values are extrapolations, not measured collapse points.
- **Index / synthesis:** [[multi-agent-collective-ai]] (Thread A — majority lock-in / $N_c$).

## Connections

- Synthesis: [[multi-agent-collective-ai]]
- Naming-game conventions, collective bias, committed-minority tipping: [[emergent-social-conventions-llm-populations]]
- Platform-scale LLM-agent sandbox / herd & polarization at large $N$: [[oasis-million-agent-social-simulator]]
- Loose engineering cousin to collective / mean-field control themes on [[amo-quantum-state-control]] (different physics).
- Do **not** fold into measurement-problem or foundations syntheses.

## Open questions

- What training / RLHF mechanism sets $\beta$?
- Do sparse networks or multi-opinion tasks keep the Curie–Weiss form?
- Independent replications on newer model generations?

## Source

- `raw/analyses/2026-08-18_doi-10.1126-sciadv-aea6091_ai-agents-majority-following-coordination.md`
