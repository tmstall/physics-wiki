# Refresher: Measurement Problem Threads 1–7  
### Prep for Thread 8 (experimental leverage)

Companion map: [[measurement-problem-threads]] · Source study: `claude_export/extracted-analyses/2026-07-28_measurement-problem-threads-1-7_19ad1981.md`

**What Thread 8 will cash:** Threads 1–7 leave one family with a **live lab handle** — objective collapse (GRW/CSL). Everything else is mostly empirically quiet metaphysics. This sheet rebuilds the arc so that fork is obvious when you start.

---

## The one sentence the whole problem lives in

Unitary evolution is **linear**. A linear map applied to a superposition returns the **superposition of the outputs** — never one of them.

If measurement sends $|0\rangle|r\rangle \to |0\rangle|\text{“0”}\rangle$ and $|1\rangle|r\rangle \to |1\rangle|\text{“1”}\rangle$, then linearity **forces**

$$(\alpha|0\rangle+\beta|1\rangle)|r\rangle \;\longrightarrow\; \alpha\,|0\rangle|\text{“0”}\rangle + \beta\,|1\rangle|\text{“1”}\rangle$$

The apparatus is entangled with **both** readings — the **“and.”** What you experience is one reading — the **“or.”** Every interpretation is bookkeeping about that gap.

In CS terms: the dynamics are branch-free dataflow ($f(a+b)=f(a)+f(b)$). Observation looks like a branch instruction. **Where is the `if`?** It is not in $U$.

---

## Master tool — two-column sort

| Left — interpretation-**neutral** (serious views share this) | Right — interpretation-**dependent** (the real commitments) |
| --- | --- |
| Linear unitary micro-dynamics (to spectacular precision) | Outcome-realism: is exactly one branch “the real one”? |
| Measurement = entanglement → superposition of records | Physical collapse as a real event / new law? |
| Decoherence suppresses *accessible* inter-branch interference | Branch ontology: do all branches exist and get inhabited? |
| Einselection picks a robust **pointer** basis from the coupling | Observer-relativity of facts (QBism / RQM)? |
| Improper mixture *matches* “definite but unknown” **statistics** | Origin of Born weights: earn $\|\psi\|^2$ or assume it? |
| Born **frequencies** as observed regularity; no-signaling | |

**Decoherence’s mechanism (why it stays on the left):** the pointer couples to ~$10^{20}$ environmental degrees of freedom; each effectively CNOT-copies the which-branch bit. Environment records go orthogonal → off-diagonals of the *reduced* density matrix die. Global state is still the pure superposition. Decoherence is **lossless broadcast**: coherence moved into correlations, not deleted. So nothing was **selected**.

**Improper vs proper mixture (the silent import):** After decoherence, $\rho \approx \mathrm{diag}(1/2,1/2)$ looks identical to “a coin was flipped and I don’t know which.” In the coin case there *is* a hidden fact. In the decoherence case both branches are still in the global pure state. Reading the diagonal as “one outcome really happened” **imports** the coin ontology. That import is the left→right jump.

**Two asterisks worth remembering:**

1. “Unitary everywhere” is **not** fully neutral — GRW/CSL deny exact universal unitarity *testably* (Thread 8’s on-ramp).
2. Born **frequencies** are neutral; Born’s **provenance** is not (Thread 7).

---

## The trilemma

You cannot keep all three:

1. **Completeness** — ψ is the whole story  
2. **Linearity** — Schrödinger always  
3. **Definite outcomes** — exactly one objective result  

| Family | Breaks | Thread |
| --- | --- | --- |
| Collapse | Linearity (or parks an unphysical cut) | 3 |
| Bohm | Completeness (add positions) | 4 |
| Everett | Definite outcomes (all branches real) | 5 |
| Epistemic / relational | Premise *under* the trilemma (absolute facts) | 6 |

---

## Thread 1 — Make the problem inescapable

**Job:** Kill the vibe (“observation is weird”) and seal soft exits.

**The forced “and”:** A Z-detector is defined by how $U$ acts on basis states. Linearity then forces entangled superposition for superposed input. A fixed linear deterministic map cannot emit “0” *or* “1” with probability — probabilistic single outcomes are not the kind of thing linear maps produce.

**Exit A fails — “ψ is just knowledge / ignorance.”** Superpositions are empirically not ignorance mixtures (interference). Under stated assumptions, PBR-type results fence off naive epistemic readings: if there’s an underlying ontic state λ that ψ is about, ψ is forced toward ontic. (Sophisticated escape: deny λ entirely → QBism in Thread 6.)

**Exit B fails — “Born handles it.”** Born is a **separate postulate** bolted onto unitary dynamics. It is the **seam**, not the solvent. Saying “Born picks the branch” just names Process 1 without explaining where the branch instruction lives in the microphysics.

**Payoff:** Every remaining thread answers: the “or” enters through a bolted-on structure — so is that structure **real dynamics** (3), **hidden positions** (4), **ignored other branches** (5), or **agent bookkeeping** (6)? Underneath: does the view **earn** $\|\psi\|^2$ (7)?

---

## Thread 2 — Decoherence’s gifts (and the overclaim)

**Job:** Not “remind you decoherence doesn’t pick outcomes” — unpack what it **does** earn on the left.

### Gift 1 — Interference is not merely unobserved; it’s practically dead
Environment-induced decoherence timescales for macros are absurdly short. That is a theorem of the coupled dynamics, not a vibe about “looking.”

### Gift 2 — Einselection (preferred basis)
The environment + interaction Hamiltonian picks which observables stay robust. Local couplings typically favor **position** (or other QND / approximately conserved monitored observables): those eigenstates get copied without being churned; their superpositions do not survive monitoring.

**Worked intuition:** Monitoring $\sigma_z$ means the coupling is a constant of motion for $z$-eigenstates — QND copying. Superpositions of $z$ get which-path information written into the environment and lose coherence in that basis. That is **why classicality is about definite pointers**, not arbitrary bases.

### What decoherence does **not** do
- Pick *which* pointer reading occurs.
- Turn an improper mixture into a proper one.
- Justify reading diagonal entries as probabilities without re-invoking Born (subtle seam → Thread 7).

**Slogan diagnosis:** “Decoherence solves the measurement problem” is **half right**. It solves preferred-basis / appearance-of-classicality. It does not move the right column.

**Open crack:** What *is* “the system”? The system⊗environment split is usually **imposed**. Different factorizations can yield different “classical worlds.”

**Forward gifts:**
- To **Everett** (Thread 5): preferred basis for free.
- To **Thread 8**: molecule interferometry pushes the mass×separation frontier where collapse models could deviate from pure decoherence.

---

## Thread 3 — Collapse pictures (the family Thread 8 will pressure-test)

**Job:** Fill the “or” by making Process 1 **real**.

### Copenhagen / movable cut
Collapse (or “classical apparatus”) at a Heisenberg cut. Decoherence now tells you where the cut *wants* to sit pragmatically (after einselection) and why sliding it doesn’t change predictions — but that is **not** making collapse physical. Bell’s complaint stands: “measurement” remains a primitive term in laws that were supposed to explain measurement.

### Consciousness-collapse
Relocates the cut to a mind. Inherits Wigner’s friend worse; no new dynamics; no lab handle.

### GRW / CSL — collapse as modified dynamics
- Rare spontaneous localization per particle; near-certain for macroscopic superpositions.
- Localization center weighted by $|\psi|^2$ → Born statistics **by construction**.
- **Structural gain:** one dynamical law does smooth evolution *and* selection — the two-process seam dissolves.
- **Honest caveat:** $\|\psi\|^2$ weighting is still **put in by hand** (Thread 7 still bites on provenance).

**The contrast that seeds Thread 8:**

| | Decoherence | CSL / GRW |
| --- | --- | --- |
| Needs environment? | Yes | **No** — intrinsic to dynamics |
| Isolate a massive superposition perfectly | Coherence loss **stops** | Coherence loss **continues** |
| Global state after “classical appearance” | Still pure “and” | Genuine reduction toward one branch |

So the clean experimental signature is: **superposition that decoheres even when environmental decoherence is ruled out** — plus related handles (matter-wave interferometry at large mass, spontaneous X-ray emission, heating). Thread 3 only sketched the shape; **Thread 8 verifies current bounds**.

**Wiki already connected:** [[collapse-models-clock-precision]] / [[spontaneous-collapse-models]] — CSL/DP as spacetime jitter → tiny proper-time floor; currently compatible with clocks, not ruled out or detected.

---

## Thread 4 — Bohm (mirror image of collapse)

**Job:** Keep Schrödinger **exact always**; buy the “or” by breaking **completeness**.

- Add actual particle positions (beables). ψ is a real field on **configuration space** ($3N$ dimensions) that guides particles via $v \propto \nabla S$ (phase gradient — Hamilton–Jacobi-like).
- After measurement + decoherence, branches separate in configuration space; the **actual configuration** sits in one branch → that is the outcome. Other branches are **empty waves** (still in ψ, guide nothing).
- Deterministic; empirically equivalent to textbook QM in pure form → **no distinct prediction** like CSL.
- **Pays with:** explicit nonlocality (entangled guidance depends on distant actual positions) + preferred-foliation tension with relativity.
- **Born:** equivariance is a **theorem** — if distributed as $|\psi|^2$ once, guidance preserves it. Why start at $|\psi|^2$? Posit or contested typicality argument (Thread 7).

**Hinge into Thread 5:** Bohm admits all branches are fully alive in ψ. Everett asks: then why add the bead?

**Central picture:** velocity field fills configuration space, not 3D space — nonlocality is already in that sentence.

---

## Thread 5 — Everett / many-worlds

**Job:** Keep Completeness **and** Linearity; break Definite outcomes. The “and” *is* reality.

- Ontology: only ψ, always Schrödinger, ψ physical. Measurement = ordinary entanglement. No cut, no collapse, no hidden variables — fewest postulates, richest ontology.
- Experienced “or” is **indexical**: which branch-copy you are (like “which hospital did I wake up in?”).
- Preferred basis: import Thread 2’s einselection for free. Branches are **emergent, approximate, not sharply countable** (like tigers — robust patterns, not discrete fundamental objects). That kills naive branch-counting.

### Probability problem (two pieces)
1. **Incoherence:** Probability needs uncertainty. But every outcome happens with certainty. What are you uncertain *about*?
2. **Quantitative:** Why Born weights? Counting branches on $\sqrt{0.9}|0\rangle+\sqrt{0.1}|1\rangle$ gives 50/50, not 90/10. “Split into 9+1 sub-branches” is question-begging (needs amplitudes already) and ill-defined (no sharp count).

**Weight ≠ existence.** A low-amplitude branch’s inhabitant is fully real; “less probable” cannot mean “less existent.”

### Three serious attempts to earn Born (all contested)
- **Envariance (Zurek):** environment-swap symmetry → equal amplitudes equiprobable → fine-grain to $\|\psi\|^2$. Critics: indifference / reduced-state assumptions smuggle Born.
- **Deutsch–Wallace decision theory:** rational agents forced to weight by $\|\psi\|^2$. Critics: branching-indifference axiom may forbid caring about copy-count by fiat.
- **Self-locating uncertainty (Sebens–Carroll):** post-branch, pre-observation “which copy am I?” Ignorance + epistemic separability → Born. Critics: does that window exist without a hidden fact of location?

**Selling point often missed:** Everett’s dynamics are **local** (branching local; Bell correlations appear only on later local comparison). Contrast Bohm’s ineliminable nonlocal guidance.

**Falsification shape:** Everett = exact unitarity taken literally → no distinct prediction from unitary QM. A confirmed GRW/CSL signal (**Thread 8**) would kill Everett, Bohm, and unitary-Copenhagen together. Everett-vs-Bohm is metaphysics; Everett-vs-GRW is lab.

---

## Thread 6 — Information-first / observer-relative (dissolve by denying absolute facts)

Threads 3–5 all assumed outcomes are **observer-independent facts**. Thread 6 says that premise is the mistake.

### QBism
- ψ = one agent’s personal bets about *that agent’s* future experiences — not a physical field.
- Collapse = Bayesian update after an action that returns an experience.
- Born = **normative** coherence constraint on gambles (not a law nature “obeys”).
- Escapes naive PBR by denying any underlying ontic λ for ψ to be about.
- Relocates the hard question: what must the world be like such that agents’ experiences are Born-structured? (Fuchs: open program.)

### Relational QM (Rovelli)
- Values are **relative to the interacting system** — any physical system can be the “observer,” not just agents.
- Relative to apparatus A: definite “or.” Relative to outsider C: still “and.” Both correct — different reference systems.
- Needs extra work (e.g. cross-perspective links) so perspectives cohere when they finally interact.

### What dissolves vs relocates
- **Dissolves:** technical and→or seam (no physical ψ-transition to explain); preferred-observer cut.
- **Relocates:** ontology of the external world / consistency of perspectives — mass conserved, moved into metaphysics-of-“for whom.”

### Wigner’s friend (sorting table)

| View | Friend’s definite “0” | Wigner’s superposition |
| --- | --- | --- |
| Collapse / GRW | Real; collapsed | Wrong — coherence gone |
| Everett | Indexical (one copy) | Correct — both copies real |
| QBism | Friend’s experience | Wigner’s personal belief — both valid |
| RQM | Fact relative to friend | Fact relative to Wigner — both correct |

**In-principle teeth:** If Wigner can still do interference on friend+lab, coherence survived (no-collapse). If not, something destroyed it (collapse). That is again the **Thread 8 fork** in a coat.

### Frauchiger–Renner (CAP-shaped trilemma)
Cannot keep all three: **(Q)** QM universal for agents, **(S)** single outcomes, **(C)** certainties chain across agents.

| Drop | Get |
| --- | --- |
| Q | Objective collapse |
| S | Everett |
| C | QBism / RQM |

So “dissolve by relativizing” is not soft preference — it’s one of three forced exits, with a precise cost: **no combinable cross-observer narrative.**

---

## Thread 7 — The Born bill (sharpest sorting tool)

Born hides **two** questions:

| | Question | Who struggles? |
| --- | --- | --- |
| **Q1** | Why probabilities *at all* in a deterministic dynamics? | Everett hardest |
| **Q2** | Why *squared* modulus specifically? | Gleason closes this for dim ≥ 3 |

### Gleason (the universal lemma)
Any non-contextual probability assignment on Hilbert space dim ≥ 3 must be $\mu(P)=\mathrm{Tr}(\rho P)$ → Born for pure states. **Squared form is forced by geometry** (over-determination across overlapping bases). In 2D impostors exist; dim ≥ 3 crushes them.

**Gleason does *not*:** explain why probabilities exist (silent on Q1); rule out *contextual* hidden variables (Bohm lives in that loophole); run the program — it type-checks the form.

### Six-way scorecard (compressed)

| View | Q1 (why probability) | Q2 (why $\|\psi\|^2$) | Verdict |
| --- | --- | --- | --- |
| Copenhagen | postulated | postulated | Bald postulate |
| GRW/CSL | physical (stochastic term) | written into the law | Postulate relocated into dynamics |
| Bohm | posit or typicality | **equivariance theorem** | Partially earns |
| Everett | *must* derive | *must* derive | Forced to earn; contested |
| QBism | dissolved (norm, not world-fact) | normative reframe | Reframes the *kind* |
| RQM | info axioms (programmatic) | aimed-at | Attempts; incomplete |

**Meta-moral for Thread 8:** Born *provenance* alone makes no distinct lab prediction — every view is built to reproduce the same frequencies. The only way Q1 becomes empirically exposed is to answer it with **new physics** — which is exactly dynamical collapse. Follow Born’s bill to the end and you regenerate the single **collapse vs no-collapse** fork.

---

## Arc in one paragraph

Thread 1 seals the and/or gap. Thread 2 fills the left column (appearance of classicality + pointer basis) and stops. Threads 3–6 are competing bids for the right column: break linearity, break completeness, break definiteness, or relativize facts. Thread 7 asks every bid whether it earned $\|\psi\|^2$ or assumed it — and shows only collapse answers “why randomness” with modified dynamics. **Thread 8 asks what the experiments say about that bid.**

---

## Carry into Thread 8

1. Isolation test: decoherence needs E; CSL does not.  
2. Push molecule interferometry / related bounds; verify numbers, don’t recall.  
3. Wiki clock floor: collapse compatible with metrology so far — not vindicated, not dead.  
4. A confirmed collapse signal would clear Everett, Bohm, and unitary-Copenhagen together; null results squeeze CSL parameter space without automatically crowning Everett.

---

## 90-second verbal recap

> Linear QM forces an “and” of records. Decoherence makes the “and” locally invisible and picks a pointer basis, but never selects. Collapse buys selection with new stochastic dynamics — testable if you can beat the environment. Bohm buys selection with hidden positions — empirically quiet, nonlocal. Everett keeps the “and” as ontology and owes a derivation of probability. QBism and RQM dissolve absolute outcomes into “for whom” and pay with no view from nowhere. Gleason forces the squared form; the live fight is why there are probabilities at all. Thread 8: pressure-test the only family that answered that with physics you can try to see in a lab.
