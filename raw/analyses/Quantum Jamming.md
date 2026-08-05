


## You said: See if you can find a paper which matches this information.

See if you can find a paper which matches this information. If you can, then do do detailed and ls is using the version 3.4.9 framework

Apr 18

## Claude responded: It looks like you may have forgotten to include the information you wanted me to search against — no paper details, abstract snippet, or description came throu…

Identified missing paper details and sought clarification

Identified missing paper details and sought clarification

It looks like you may have forgotten to include the information you wanted me to search against — no paper details, abstract snippet, or description came through with your message. Could you paste the text, title, DOI, or description you'd like me to match?

## You said: Quantum ‘Jamming’ Explores the Truly Fundamental Principles of Nature

Quantum ‘Jamming’ Explores the Truly Fundamental Principles of Nature By Matt von Hippel April 17, 2026

Some quantum cryptographers want to find ways to keep messages secret even if the rules of quantum mechanics don’t hold. The recently rediscovered idea of quantum jamming complicates things. Right I forgot it. Here it is

Apr 18

## Claude responded: No worries!

Thought for 1s

Thought for 1s

No worries! Let me go find that paper now.

Searched the web

Searched the web

Good — got the full article. Now let me pull the actual underlying papers.

Synthesized quantum jamming debate across foundational physics and cryptography implications

Synthesized quantum jamming debate across foundational physics and cryptography implications

**Analyzing** v3.4.9


## Quantum Jamming: The Spooky Action That Could Silently Break Every Quantum Secret

**One-sentence hook:** A 1996 thought experiment, quietly rediscovered, threatens to silently corrupt quantum cryptography — and the fight over whether it's physically possible is cracking open the deepest questions about causality, spacetime, and what physics even *means*.


### 1. Big-Picture Context

Quantum cryptography is supposed to be the unbreakable vault. The security guarantees don't rest on the hardness of math problems (as classical crypto does) — they rest on *physics*. Specifically, device-independent quantum key distribution (DIQKD) leans entirely on a property called monogamy of entanglement: if Alice and Bob share a maximally entangled pair, no third party can be correlated with that pair without Alice and Bob detecting the intrusion. It's the quantum equivalent of a wire that physically burns if anyone taps it.

But quantum mechanics is a theory, not a law of the universe. The history of physics is one of apparent bedrock principles getting swallowed by deeper ones — Newtonian mechanics looked complete until it wasn't; Maxwell's electromagnetism looked complete until it wasn't. A growing community of researchers has spent the past decade asking: *what if quantum mechanics gets superseded?* What survives? What breaks?

The answer, it turns out, depends on whether something called **quantum jamming** is physically possible. Jamming is a hypothetical operation — imagined in 1996 by Grunhaus, Popescu, and Rohrlich, then essentially ignored for twenty years — in which a third party silently rewrites the correlation between two distant entangled particles *without* leaving any local fingerprints and *without* sending information faster than light. If jamming is possible in some post-quantum theory, then the monogamy of entanglement fails, and device-independent cryptography is broken at its foundation.

What makes this episode remarkable is the collision it has triggered. Three groups — Weilenmann (Nat. Commun. 2025), then Eckstein, Miller, both Horodeckis and Ramanathan (arXiv:2512.23702, Dec. 2025) — have published directly contradictory results about whether jamming is compatible with no-faster-than-light signaling. The disagreement is not about arithmetic; it's about what the right *operational* definition of causality is. This is foundational physics at full boil.


### 2. Background Crash-Course

**Entanglement and Monogamy.** When two quantum particles are entangled, measuring one instantly fixes the correlator with the other — even across a galaxy. The monogamy principle says: this "budget" of correlation is finite and conserved. A maximally entangled Alice-Bob pair can't *also* be entangled with Charlie. Think of it like a marriage license in quantum mechanics: you can be maximally committed to one partner, or spread thinner across several, but never both. DIQKD security proofs use monogamy as their trip wire: any eavesdropper trying to share entanglement with Alice and Bob burns their marriage license, and Bell inequality violations drop, revealing the intrusion.

**No-Signaling (NSS) vs. No-Superluminal-Causation (NSC).** Einstein gave us "no faster-than-light signals" (NSS) as a load-bearing pillar of relativity — you can't *use* nonlocal correlations to send a message. But there's a subtler principle hiding underneath: no superluminal *causal influence* at all (NSC). In a two-party scenario, NSS and NSC are the same. In a three-or-more-party scenario, they come apart. Think of NSC as "the wires don't reach across the galaxy at all," while NSS is "the wires might reach, but you can't control them." Jamming lives in that gap.

**Bell Inequalities as Correlation Meters.** A Bell inequality is essentially a correlation budget — a ceiling on how strongly distant particles can be correlated if *no* influence crosses between them. Quantum mechanics violates the classical Bell ceiling (the Tsirelson bound). Jamming, if possible, could push correlations around *without* Alice or Bob seeing their local statistics change. Analogy: imagine a network switch (the jammer) that can reroute packets between two distant servers without either server's CPU utilization changing — the endpoints only notice when they compare logs.

**The Spacetime Geometry of Multipartite Correlations.** In a three-party experiment, where Bob, Alice and Charlie all make measurements, the *spacetime geometry* of who measures when matters. Horodecki and Ramanathan (Nat. Commun. 2019) showed that in certain spacetime configurations, only a *subset* of the usual no-signaling constraints is required to prevent causal loops. The "surplus" constraints — the ones that aren't needed — are exactly the ones jamming violates. It's like discovering that some of your access control rules are redundant for preventing data races, and an attacker exploits the gap.


### 3. Core Technical Explanation

The central debate spans five papers across thirty years. Let me walk through the chain.

**Grunhaus, Popescu & Rohrlich (1996): The Original Thought Experiment.** They imagined "super-entanglement": a hypothetical state involving three parties, Alice, Bob, and Charlie, in which Bob (Jim the Jammer) has a device that influences the *type* of correlation between Alice and Charlie's outcomes — flipping them from anticorrelated to correlated — while leaving Alice's and Charlie's marginal statistics untouched. They argued this could be done without violating no-signaling (NSS), because neither Alice nor Charlie notices anything locally until they classically compare their results. The paper was unusual and was promptly shelved.

**Horodecki & Ramanathan (Nat. Commun. 2019): Jamming Reactivated.** Ramanathan and Paweł Horodecki were working on device-independent cryptography when they rediscovered the 1996 paper. They realized that in multiparty spacetime configurations — specifically, those where Bob's measurement event lies in the *mutual past* of Alice's and Charlie's measurements but in a region where the usual no-signaling constraints are "overdetermined" — Bob could in principle jam the Alice-Charlie correlation without enabling superluminal communication. They called these "relativistically causal correlations," distinct from the usual no-signaling polytope. This directly broke monogamy of entanglement, demolishing DIQKD security in these configurations.

**Vilasini & Colbeck (PRL 2022): Jamming Requires Superluminal Causation.** Using a sophisticated causal modeling framework (think directed acyclic graphs but for quantum correlations, with relativistic spacetime baked in), Vilasini and Colbeck showed that any theory generating jamming correlations must involve *superluminal causal influence* (violates NSC), even if it doesn't allow superluminal *signaling* (preserves NSS). Their argument: you can't get jamming without fine-tuning — the correlations require the kind of "hidden wiring" that only works with retrocausal or superluminal causal structure. They argued this makes jamming theories unphysical: they require a mechanism you can never observe directly, yet which must act at speeds beyond light. Fine-tuning plus hidden superluminal causation — both red flags.

**Weilenmann (Nat. Commun. 16, 269, 2025): Monogamy Kills Jamming.** Weilenmann showed that correlations satisfying only the subset of no-signaling constraints relevant for relativistic causality must obey highly nonlocal entropic monogamy relations, and that any physical mechanism capable of producing such correlations would necessarily lead to superluminal signaling. Her argument: if a jammer can be *turned on and off* (a reasonable operational requirement — otherwise it's just a passive correlation, not a jamming *device*), then the change in correlations when Bob flips the switch constitutes a signal faster than light. The ability to *control* the jam is itself the superluminal channel. Jamming is therefore not a feature of any physically realizable theory — it's self-defeating. [Nature](https://www.nature.com/articles/s41467-024-54855-1)

**Eckstein, Miller, R. Horodecki, Ramanathan, P. Horodecki (arXiv:2512.23702, Dec. 2025): Jamming Survives (With Caveats).** This December 2025 preprint is the direct rebuttal. The team constructs what they call an "operational no-signaling" (ONS) framework — a purely operational framework grounded in spacetime geometry and the concept of a spacetime random variable, which identifies the necessary and sufficient conditions for the impossibility of operational superluminal signaling. Their key moves: [arXiv](https://arxiv.org/html/2512.23702)

First, they argue Weilenmann's "turn it on and off" assumption is the crux. They show that turning on or off a jamming device in a given scenario does not directly decide whether jamming occurs — the jamming outcome is set by a highly nonlocal mechanism that accounts for all potential parties that may attempt to jam. In other words, Bob doesn't freely *flip a switch* in the way Weilenmann assumed — the jammer is a *property of the joint spacetime configuration*, not a local control. Remove that assumption, and the superluminal signaling argument collapses. [arXiv](https://arxiv.org/html/2512.23702)

Second, they identify *spacetime configurations* — specifically including black hole geometries — where jamming is fully compatible with ONS. In black hole spacetimes, certain nonlocal correlations under and across the event horizon can be jammed by any agent without spoiling the operational no-signalling constraints. The event horizon acts as a natural "causal shield" that creates the spacetime asymmetry jamming needs. [arxiv](https://arxiv.org/abs/2512.23702)

Third, they dispute Vilasini & Colbeck's 2022 claim about causal loops in Minkowski space — they show that violation of the operational no-signalling constraints in Minkowski spacetime implies either a logical paradox or an operational infringement of Poincaré symmetry, essentially saying flat spacetime rules out jamming but *curved* spacetime near horizons may not. [arxiv](https://arxiv.org/abs/2512.23702)


### 4. What's Genuinely New or Clever

**The Operational No-Signaling Framework.** The Eckstein et al. paper's main technical innovation is replacing the usual "no-signaling constraints on correlations" (which are just algebraic conditions on probability distributions) with *operational* conditions grounded directly in spacetime geometry and the causal structure of interventions. This is clever because it disentangles two things that had been quietly conflated: the statistics of correlations vs. the operational power of agents. You can have "no signaling" in the statistical sense while still having "signaling" in the operational sense — if an agent can *change* their input and the distant output changes as a result. The framework distinguishes these cleanly.

**Black Holes as Natural Jammers.** The most striking new finding is that black hole event horizons provide exactly the spacetime geometry that permits jamming without operational superluminal signaling. From a quantum gravity standpoint, this is fascinating: the information paradox, Hawking radiation, and questions about what happens to entanglement across a horizon all lurk here. Jamming across event horizons might be related to the non-unitary evolution that black hole evaporation produces. This wasn't the paper's focus, but it's a genuinely new connection.


### 5. Limitations & Open Questions

**The dispute is not resolved.** Both the Weilenmann and Eckstein et al. results are technically correct given their respective definitions of "jamming mechanism." The debate is fundamentally definitional — what does it mean for an agent to *operate* a jamming device? This sounds trivial but isn't. Physics needs a consensus operational definition of "causal agency" that works across classical, quantum, and post-quantum theories. Nobody has that yet.

**The black hole result needs more work.** Showing jamming is *consistent with* ONS near a black hole horizon is not the same as showing it's *realizable* by any specific physical mechanism. The paper doesn't construct an explicit Hamiltonian or quantum channel that implements jamming — it shows the constraints permit it. There's a large gap between "not forbidden" and "achievable."

**No experimental handle.** Jamming involves correlations between spacelike-separated measurements that only manifest when results are classically compared. There's currently no experimental protocol that could confirm or deny its occurrence, even in principle. It's purely a foundational/theoretical question.

**Implications for DIQKD security proofs need revisiting.** The cryptographic community has largely moved on, treating monogamy of entanglement as given. If jamming is possible in *any* post-quantum theory — even a physically exotic one — the security proofs need to explicitly state which assumptions they rely on and whether those assumptions are falsifiable.


### 6. Three Crystallized Takeaways

1. **Quantum security rests on an assumption, not a law:** Device-independent cryptography's unbreakability depends on monogamy of entanglement, which is a quantum mechanical result — not a theorem about all possible physics. Post-quantum theories could silently violate it.

2. **"No signaling" is not one principle, it's two:** No superluminal *signaling* (NSS) and no superluminal *causation* (NSC) come apart in multiparty scenarios. Jamming lives in the gap, and that gap has opened a years-long productive argument about what causality fundamentally means.

3. **Black holes might be natural jamming devices:** The new finding that event horizons provide the exact spacetime geometry jamming needs hints at deep connections between quantum foundations, the information paradox, and what causality looks like in curved spacetime.


### 7. Detailed Summary and Explanation

The story traces a thirty-year arc from a curiosity to a live controversy with cryptographic stakes.

**Origins.** In 1996, Grunhaus, Popescu, and Rohrlich asked a simple but profound question: how far beyond quantum mechanics could a theory go while still respecting special relativity's prohibition on faster-than-light communication? They imagined a hypothetical operation they called "jamming" — a third party who could modify the type of quantum correlation between two distant entangled parties without either party noticing locally and without sending a signal. The idea was unusual enough that it sat dormant for twenty years.

**The cryptographic trigger.** In 2016, Ravishankar Ramanathan and Paweł Horodecki were studying device-independent quantum key distribution. This protocol proves its security from Bell inequality violations: if Alice and Bob observe strong enough correlations, they can certify that no eavesdropper shares entanglement with them, because monogamy of entanglement prevents three-way maximal correlations. Rediscovering the 1996 paper, they realized that if jamming were possible, monogamy fails completely in certain spacetime configurations — and the entire security architecture of device-independent cryptography collapses. The jammer doesn't eavesdrop; they *corrupt* the correlation between Alice and Charlie without either noticing, breaking the Bell inequality guarantees silently.

**The causal modeling counterattack.** Vilasini and Colbeck (2022) brought causal inference tools into the debate. Using directed causal models with relativistic spacetime structure, they showed that jamming requires *superluminal causal influence* (violating the stronger "no-superluminal-causation" principle, NSC) even when it doesn't permit superluminal *signaling* (NSS). Their argument: you can't get jamming correlations without hidden wiring that reaches across the light cone. Furthermore, they showed that if an agent can turn a jammer on and off, the change in distant correlations constitutes operationally detectable superluminal influence. This suggested jamming was a red herring — a mathematical curiosity that no real physical theory could support.

**Weilenmann's entropic argument.** In 2025, Mirjam Weilenmann derived entropic monogamy relations — inequalities that any multiparty correlation must obey if it satisfies only the relativistic subset of no-signaling constraints. The key result: any mechanism capable of producing jamming correlations must, when the jammer can be turned on and off, allow superluminal signaling. The "monogamy" here is entropic rather than quantum mechanical — it constrains what correlations any post-quantum relativistic theory can produce. This looked like a death knell for jamming as a physical phenomenon.

**The rebuttal and the black hole surprise.** The December 2025 Eckstein-Miller-Horodecki-Ramanathan paper pushes back by arguing Weilenmann's "switch" assumption is not operationally valid. In the jamming scenario, Bob's device doesn't *freely* flip a binary switch — instead, the jamming outcome is determined by the entire joint configuration of the spacetime scenario, including all other parties. The jammer is not a local controller but a relational property of the spacetime correlation structure. Once this distinction is made, jamming scenarios can be constructed that satisfy the operational no-signaling constraints. More strikingly, they identify black hole spacetimes as natural environments where jamming is possible without violating no-signaling: the event horizon creates a directional causal asymmetry that permits a party to influence correlations across the horizon without the parties inside or outside being able to signal to each other. This black hole result is unexpected and potentially deep, connecting jamming to the information paradox and quantum gravity.

**Why it matters beyond cryptography.** The real prize in this debate is a clearer understanding of what causality fundamentally is. Quantum mechanics gives us no-signaling as a derived property; it also gives us monogamy of entanglement as a theorem. If there is a post-quantum theory that preserves no-signaling but allows jamming, then monogamy is not a fundamental principle — it's an accident of quantum mechanics specifically. Finding the *deeper* principle that truly forbids jamming (if one exists) would be a step toward understanding what constraints any theory of nature must satisfy, regardless of its specific rules. This is the same program that produced information causality, Tsirelson's bound, and the entropic derivations of the Born rule — and it may ultimately help us understand why quantum mechanics looks the way it does.


### 8. Shorter Summary

Quantum jamming is a hypothetical operation in which a third party silently rewrites the correlation between two distant entangled particles — changing them from anticorrelated to correlated, for instance — without either party's local statistics changing and without sending a superluminal signal. If possible, it would break the monogamy of entanglement, which is the foundation of device-independent quantum cryptography.

The concept was proposed in 1996 but ignored until Ramanathan and Horodecki realized in 2016 that it would silently destroy quantum key distribution security in certain spacetime configurations. A debate then erupted about whether jamming is physically realizable. Vilasini and Colbeck argued it requires hidden superluminal causal influence; Weilenmann showed it implies superluminal signaling if the jammer can be switched on and off. In December 2025, Eckstein, Miller, and both Horodeckis disputed Weilenmann's switch assumption and showed that jamming is compatible with operational no-signaling in certain scenarios — including, surprisingly, near black hole event horizons. The deeper question now is whether there is a new fundamental principle, beyond ordinary no-signaling, that truly forbids jamming — and what that principle would tell us about the nature of causality in any possible theory of the universe.


[Claude is AI and can make mistakes. Please double-check cited sources.](https://support.anthropic.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on)




  

