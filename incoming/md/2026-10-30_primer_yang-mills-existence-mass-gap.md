---
type: primer (not a paper analysis)
title: Yang-Mills existence and the mass gap
date: 2026-10-30
source: MyWiki primer from OpenAI announcement (Oct 26, 2026) + KITP committee statement
status: OpenAI claim unverified; proof not yet released
suggested_pages: concepts/yang-mills-existence, concepts/mass-gap, concepts/constructive-qft, concepts/balaban-rg-program
---

# Yang-Mills existence and the mass gap

*A primer on Yang-Mills as a mathematical problem: what it means for a quantum field theory to exist, why 4D is hard, what Balaban built, why the mass gap is the deep half, and how to read OpenAI's unverified October 2026 existence claim.*

## Contents

1. [What it means for a QFT to exist](#1-what-it-means-for-a-qft-to-exist)
2. [Why four dimensions is hard](#2-why-four-dimensions-is-hard)
3. [The Clay problem: existence plus a gap](#3-the-clay-problem-existence-plus-a-gap)
4. [Balaban's lattice program](#4-balabans-lattice-program)
5. [Mass gap and confinement: the deep half](#5-mass-gap-and-confinement-the-deep-half)
6. [The October 2026 OpenAI claim](#6-the-october-2026-openai-claim)
7. [A reader's checklist for the release](#7-a-readers-checklist-for-the-release)
8. [What is and is not claimed](#what-is-and-is-not-claimed)
9. [Sources](#sources)

> [!WARNING]
> **Status as of Oct 30, 2026:** OpenAI's claimed existence proof is unverified. The proofs have not been released, and the mass gap is not claimed at all.

## 1. What it means for a QFT to exist

Physicists use QCD every day, so in what sense might it fail to exist? The issue is that the textbook machinery (Feynman diagrams, perturbation series, lattice simulations) produces approximations to something that has never been shown to be a well-defined mathematical object. A rigorous QFT has to be built as an actual structure: a Hilbert space of states, field operators acting on it, and a Hamiltonian whose energies are bounded below.

The Wightman axioms (1950s) list what that structure must satisfy. In plain terms: the theory respects special relativity (Poincaré symmetry), there is a unique vacuum, energy is never negative, fields are operator-valued distributions (you can only measure them smeared over a small region, never at a sharp point), and measurements at spacelike separation do not interfere (locality, or microcausality).

Osterwalder and Schrader (1973–75) gave an equivalent route that is far easier to work with. Rotate time to imaginary time, so Minkowski space becomes ordinary 4D Euclidean space. The theory is then described by Euclidean correlation functions, the "Schwinger functions", which behave like moments of a probability measure on field configurations, much like statistical mechanics. If those functions are Euclidean-invariant, obey a positivity condition called reflection positivity, and satisfy a few growth and clustering conditions, a reconstruction theorem hands back a full Wightman theory.

So in practice "constructing a QFT" means: define a Euclidean measure, typically as a limit of regularized versions, and prove that the limit exists and has the OS properties. This is the field called constructive quantum field theory.

## 2. Why four dimensions is hard

Every construction starts with a regularized theory that is mathematically fine: put the fields on a lattice of spacing a (an ultraviolet cutoff) inside a finite box of side L (an infrared cutoff). The hard part is removing both cutoffs. As a goes to 0, naive quantities diverge; renormalization says you must tune the bare coupling g(a) as you go so that physical quantities stay finite. Proving that this tuned limit exists, and is not trivial or free, is the core difficulty.

The difficulty grows with dimension. In 2D, interacting theories such as φ⁴ need only mild renormalization, and Glimm and Jaffe, with others including Nelson and Simon, constructed them in the late 1960s and early 1970s. In 3D, φ⁴ needs genuinely more renormalization, and Glimm and Jaffe's 1973 construction was a landmark, followed by work of Feldman, Osterwalder, Magnen and Sénéor. Those successes rest on the theories being "super-renormalizable": only finitely many divergent terms to tame.

Four-dimensional Yang-Mills is only just renormalizable, with divergences at every order, plus gauge symmetry that must be preserved. Asymptotic freedom is what gives hope: the coupling shrinks logarithmically at short distance, so the cutoff removal is controlled by a theory getting weaker, not stronger.

$$g^2(\mu) \approx \frac{1}{b \cdot \ln(\mu/\Lambda)}$$

Here b is a positive number fixed by the gauge group and Λ is the dynamically generated scale. The flip side is the infrared: at long distance the coupling grows and no small parameter remains, which is exactly where the mass gap and confinement live. Notably, the 4D φ⁴ theory, which lacks asymptotic freedom, is now known to be trivial (Aizenman and Fröhlich, with a 2021 strengthening by Aizenman and Duminil-Copin), so 4D existence for an interacting theory is not automatic.

## 3. The Clay problem: existence plus a gap

In 2000 the Clay Mathematics Institute named Yang-Mills existence and mass gap one of its seven Millennium Prize Problems, with an official description by Arthur Jaffe and Edward Witten. The prize is one million US dollars.

- **Gauge group:** Any compact simple group G, such as SU(2) or SU(3)
- **Spacetime:** Flat ℝ⁴, infinite volume, cutoffs removed
- **Part 1: existence:** A quantum Yang-Mills theory satisfying axioms at least as strong as Wightman or Osterwalder-Schrader
- **Part 2: mass gap:** That theory has a mass gap Δ > 0
- **Matter:** Pure gauge fields; no quarks are required

The mass gap means the Hamiltonian H has the vacuum at energy zero and then nothing until some strictly positive energy Δ. Equivalently, the lightest particle (a glueball, in pure Yang-Mills) has positive mass, and correlations decay exponentially with distance.

$$\mathrm{spec}(H) \subset \{0\} \cup [\Delta, \infty), \quad \Delta > 0$$

Both parts are required. A proof of existence alone, however hard, does not win the prize.

## 4. Balaban's lattice program

Tadeusz Balaban, in a long series of papers in Communications in Mathematical Physics through the 1980s, attacked Yang-Mills on Wilson's lattice using a rigorous version of the renormalization group. The idea is Wilson's block-spin picture made into theorems: average the lattice fields over small blocks, integrate out the short-wavelength fluctuations, and show that the result is again a lattice gauge theory of the same form with a slightly different coupling. Repeat many times, and control the errors at every step.

His main result was ultraviolet stability: on a lattice in a finite box (a torus) in 3D and 4D, the effective actions stay under control uniformly as the lattice spacing shrinks, with gauge invariance preserved. That is the heart of the short-distance problem, and it is widely regarded as the deepest rigorous work on 4D gauge theory.

The program stopped short of a finished theory. It worked at fixed finite volume and did not complete the infinite-volume limit, did not establish the full set of OS properties (in particular full Euclidean invariance and the uniqueness of the limit), and did not touch the strong-coupling infrared regime. The papers are also notoriously long and dense, which partly explains why few people built on them for decades.

> [!NOTE]
> **Why this matters for 2026:** The OpenAI claim says it is built on Balaban's approach. The KITP committee says Balaban's ideas helped follow the theory "all the way to infinite distances", which is precisely the step he never finished.

## 5. Mass gap and confinement: the deep half

Existence is about short distances, where the theory is weakly coupled and asymptotic freedom helps. The mass gap is about long distances, where the coupling is strong and no expansion works. A theory can exist perfectly well without a gap: free massless fields satisfy every axiom and have no gap, and classical Yang-Mills itself has massless waves, like light. The gap is a purely quantum, nonperturbative effect, sometimes called dimensional transmutation: the dimensionless coupling turns into a mass scale Λ.

Confinement is a further, separate statement. In pure Yang-Mills it is usually phrased with Wilson loops: the expectation of a large loop C falls off with the area it encloses, which means a linear potential between static color charges, with string tension σ.

$$\langle W(C) \rangle \sim e^{-\sigma \cdot \mathrm{Area}(C)}$$

Confinement is believed to imply a gap, but the two are not the same claim, and neither is part of the existence statement. Lattice simulations give overwhelming numerical evidence for both, as the KITP statement notes, but evidence is not proof. With quarks added, as in real QCD, confinement is subtler still, because flux strings can break by pair creation.

This is why physicists call the gap the physically deep half: it is the part that explains why the strong force is short-ranged and why hadrons have mass, and nobody has a rigorous handle on it in 4D.

## 6. The October 2026 OpenAI claim

> [!WARNING]
> **Unverified:** Nothing below has been checked by independent mathematicians. The proofs are held by a committee and have not been published.

On Oct 26, 2026 OpenAI announced an AI-produced, mathematically rigorous existence proof for interacting 4D gauge theories with fermions, including QCD and the simplest grand unified theory containing the Standard Model's fields, built on Balaban's approach. Existence of pure Yang-Mills is a subproblem of this. The mass gap is not claimed, so this would not settle the Clay problem.

- **Sep 9** — Natural-language proof of Yang-Mills existence
- **Sep 18** — Natural-language proof for QCD
- **Oct 16** — Lean formalization of Yang-Mills existence (same day David Gross was asked to take custody of the proof)
- **Oct 26** — OpenAI public announcement

The shepherding committee is David Gross (chair), Michael Douglas, Arthur Jaffe, Igor Klebanov and Nikita Nekrasov. Gross was asked by OpenAI to take custody and chose the others; the committee says it has no responsibility to OpenAI. It holds the 1147-page proofs and plans first to check that the Lean definitions and problem statement match the standard ones in physics and mathematics, and that the formal and informal versions align, then release the Lean proof, and later release the full proofs with its assessment.

> The new proof by OpenAI appears to be an important step towards putting QFT on a rigorous mathematical footing. ... But confinement and the mass gap remain very important open challenges.
>
> — KITP shepherding committee statement, Oct 2026

Criticism so far:

- AGMAI group: called for immediate release of the proofs.
- Bauerschmidt (Scientific American): Balaban's papers are incomplete and very hard to read.
- Buckmaster (Scientific American): doubts a Lean verification done in about a month.
- Karch and Kogler (The Verge): criticize the hand-picked review instead of open scrutiny.

Context: earlier, Sussman and Alpöge publicly posted an experiment, an unverified 153-page draft written with Claude, aimed at 4D SU(2) Yang-Mills. It shows AI-assisted attempts on this problem predate OpenAI's, and that drafts of this length can exist without being correct.

## 7. A reader's checklist for the release

Questions to ask when the Lean proof and the 1147 pages appear. None can be answered yet; status as of Oct 30, 2026.

- [ ] **Which gauge groups are covered** — All compact simple G, as Clay asks, or only SU(2), SU(3) and the specific GUT group?
- [ ] **Which axioms are verified** — All OS axioms, including reflection positivity and full Euclidean (rotation) invariance, or only some?
- [ ] **Does the Lean statement match Clay's** — Check the definitions of the measure, the fields and the limit, not only that the proof compiles. A proof of the wrong statement compiles too.
- [ ] **Infinite-volume and continuum limits both taken** — The step Balaban never finished. Is the limit unique, or only along a subsequence?
- [ ] **Is the theory nontrivial** — The limit should be genuinely interacting, not free (compare 4D φ⁴ triviality).
- [ ] **How fermions are handled** — QCD and the GUT add quarks; how is that done rigorously?
- [ ] **Which parts are formalized** — Only Yang-Mills existence was formalized on Oct 16; QCD and the GUT so far are natural-language.
- [ ] **Independent checks** — Experts outside the committee, especially constructive QFT specialists, should read it.
- [ ] **No mass gap claimed** — Watch for coverage that calls the Millennium Problem solved; it is not.

## What is and is not claimed

| Statement | Status |
|---|---|
| Pure Yang-Mills exists in 4D | ⚠️ Claimed, unverified |
| QCD and simplest GUT exist | ⚠️ Claimed, unverified |
| Mass gap Δ > 0 | Not claimed, open |
| Confinement | Not claimed, open |
| Clay Millennium Prize | Not settled |

## Sources

- [Yang-Mills LLM experiment (Sussman and Alpöge)](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment) — GitHub
- [Building scientific understanding with academic communities](https://openai.com/index/building-scientific-understanding-with-academic-communities) — OpenAI, Oct 26, 2026
- [Proof by OpenAI of the Existence of Quantum Yang-Mills theory: statement by the shepherding committee](https://www.kitp.ucsb.edu/sites/default/files/YM_working_group.pdf) — KITP, Oct 2026
- [AGMAI](https://agmai.org/) — agmai.org
- [OpenAI just scooped human researchers on a million-dollar quantum math problem](https://www.scientificamerican.com/article/openai-just-scooped-human-researchers-on-a-million-dollar-quantum-math-problem/) — Scientific American
- [OpenAI breakthrough in math, computer science, physics](https://www.theverge.com/ai-artificial-intelligence/1019921/openai-breakthrough-math-computer-science-physics) — The Verge

Background review, recommended by the committee: Douglas, M. R., *The Yang–Mills Millennium problem*, Nat. Rev. Phys. 8, 86–97 (2026).

---

## Deep dive Q&A

*User-led deep dive on this primer, Oct 30 – Nov 5, 2026. Each entry quotes the primer passage asked about, followed by the explanation.*

### Q1. Regularization and removing the cutoffs (Section 2)

> Every construction starts with a regularized theory that is mathematically fine: put the fields on a lattice of spacing a (an ultraviolet cutoff) inside a finite box of side L (an infrared cutoff). The hard part is removing both cutoffs. As a goes to 0, naive quantities diverge; renormalization says you must tune the bare coupling g(a) as you go so that physical quantities stay finite. Proving that this tuned limit exists, and is not trivial or free, is the core difficulty.

This paragraph describes the basic strategy behind every rigorous construction of a quantum field theory: start with a version you know is well-defined, then prove it still makes sense once you take away the props.

#### 1. Why start with a lattice?

A continuum field has an independent value at every point of space, which is infinitely many variables in any region however small. The "integral over all field configurations" that quantum field theory needs has no rigorous definition over that many variables. Multiplying two fields at the same point also gives infinite answers.

The fix is to replace continuous space with a grid:

- **a, the lattice spacing:** the distance between neighboring grid points. Nothing can vary on scales shorter than a.
- **L, the box size:** the side length of the finite 4D region you keep.

The grid then has N = (L/a)⁴ points, which is a finite number. The theory becomes an ordinary integral over finitely many variables, much like a statistical-mechanics model of a magnet. That is the sense of "mathematically fine": every quantity is a well-defined finite number.

**DSP analogy.** The two cutoffs map directly onto sampling a signal:

| Lattice | Sampling |
|---|---|
| Spacing a sets the highest momentum, about π/a | Sample interval T sets the Nyquist frequency, 1/(2T) |
| Box size L sets the lowest nonzero momentum, about 2π/L | Record length sets the FFT bin width, 1/(record length) |
| **UV (ultraviolet) cutoff** = short distance, high energy | Bandwidth limit |
| **IR (infrared) cutoff** = long distance, low energy | Frequency resolution limit |

"Removing the cutoffs" means taking a → 0 and L → ∞. In DSP terms, that is sampling infinitely fast for an infinitely long time.

#### 2. Why quantities diverge as a → 0

In an interacting theory, quantum fluctuations at every wavelength feed back into what you measure at long distances. Shrinking a lets in more short-wavelength modes, each adding a bit. In 4D these contributions add up logarithmically: there is roughly equal input from every factor-of-2 band between the cutoff and the scale you measure at. As a → 0 the number of bands grows without limit, so a naive calculation that holds the parameters fixed diverges.

#### 3. Renormalization: retune the knob as you shrink a

The **bare coupling g(a)** is the interaction strength you write into the lattice equations at spacing a. It can't be measured directly. What you measure are physical quantities, such as the mass of the lightest glueball or the force between two static color charges at some fixed distance.

Renormalization works like this: pick one physical quantity and hold it fixed. For each lattice spacing a, choose g(a) so that the lattice gives exactly that value. The cutoff dependence is moved into the knob, which keeps the physics finite.

For Yang-Mills, asymptotic freedom tells you how the knob has to move:

$$g^2(a) \approx \frac{1}{b \cdot \ln\!\big(1/(a\Lambda)\big)}$$

- **b:** a positive constant fixed by the gauge group
- **Λ (Lambda):** the physical energy scale the theory generates, which stays fixed while a changes
- **ln:** natural logarithm

As a → 0 the logarithm grows, so g(a) → 0 slowly.

**Analogy 1: process shrink.** When you move a transistor design to a smaller node, you retune the recipe (implant doses, oxide thickness) so the *device spec* stays put, for example threshold voltage or drive current. The recipe parameter isn't the target; the spec is. g(a) is the recipe and the glueball mass is the spec.

**Analogy 2: filter redesign.** Keep an analog filter response fixed while raising the sample rate. The digital coefficients have to change, and as the rate goes to infinity they approach degenerate values (the poles crowd toward z = 1). Yet the frequency response you actually care about stays finite and unchanged. Likewise, g(a) heads to zero while the physics at scale Λ stays the same.

**Where the analogies break down:**

- A process node is a real physical size. Here a → 0 is a mathematical limit, and nothing physical sits at spacing a.
- A linear filter has no mode mixing. The divergences come from interactions that couple every wavelength to every other. That nonlinearity is exactly what makes the QFT problem hard and the filter problem easy.

#### 4. "Proving that this tuned limit exists"

At each (a, L) you have a well-defined theory, formally a probability measure on lattice field configurations. "The limit exists" means this sequence of theories converges to one definite limiting object as a → 0 and L → ∞, and the correlation functions converge.

Lattice simulations show this convergence numerically at a handful of spacings. A proof needs bounds that are uniform: estimates that don't blow up however small a gets or however large L gets. The difference is like watching a numerical scheme behave well on several grid sizes versus proving it converges for every grid.

Both limits are required. Balaban (Section 4) controlled a → 0 at fixed L, but not L → ∞.

#### 5. "…and is not trivial or free"

The limit could exist and still be boring:

- **Free theory:** particles pass through each other without interacting. All correlations are Gaussian and are fixed by the two-point function alone.
- **Trivial:** the standard term for a limit that comes out free, meaning the interaction has disappeared.

The danger is built into the tuning: g(a) → 0. If the interaction vanishes entirely in the limit, you have "constructed" a free theory, which isn't Yang-Mills. This really does happen in 4D φ⁴ theory (a scalar field with a fourth-power self-interaction, φ⁴): tuning forces the effective coupling to zero and the limit is free.

The hope for Yang-Mills is that, even though the bare coupling goes to zero at the cutoff, the theory keeps an interaction at physical distances, set by the scale Λ. Proving that the interaction survives is a separate requirement from proving that the limit exists.

**One-line summary:** you build a finite, sampled version of the theory, retune its single knob as you refine the sampling, and the core difficulty is proving that the refined theories converge to something that still interacts.

### Q2. Existence versus the gap, and dimensional transmutation (Section 5)

> Existence is about short distances, where the theory is weakly coupled and asymptotic freedom helps. The mass gap is about long distances, where the coupling is strong and no expansion works. A theory can exist perfectly well without a gap: free massless fields satisfy every axiom and have no gap, and classical Yang-Mills itself has massless waves, like light. The gap is a purely quantum, nonperturbative effect, sometimes called dimensional transmutation: the dimensionless coupling turns into a mass scale Λ.

This passage explains why the Clay problem has two parts. Existence and the mass gap are problems at opposite ends of the distance scale, and the gap is invisible to every tool that works at the short-distance end.

#### 1. Two regimes, one running coupling

Symbols used below:

- **g:** the Yang-Mills coupling, a pure number with no units
- **μ (mu):** the energy scale you probe at. High μ means short distances, and distance ≈ 1/μ.
- **Λ (Lambda):** the energy scale the theory generates for itself (part 4)
- **b:** a positive constant fixed by the gauge group
- **Natural units:** ħ = c = 1, so energy, mass and 1/distance all have the same units (ħ is the reduced Planck constant, c the speed of light)

The running coupling from Section 2:

$$g^2(\mu) \approx \frac{1}{b \cdot \ln(\mu/\Lambda)}$$

| Regime | μ compared with Λ | Coupling | What works |
|---|---|---|---|
| Short distance (UV, ultraviolet) | μ ≫ Λ | Small, shrinking slowly | Expansions in powers of g; rigorous renormalization-group (RG) control |
| Long distance (IR, infrared) | μ approaches Λ | Grows to order 1; the formula blows up at μ = Λ | No small parameter, so no expansion |

**Why existence lives at short distances.** The hardest step in constructing the theory is a → 0, which is a UV limit. That is exactly where g is small, so you can control each RG step as "free theory plus a small correction." Balaban's program depends on this.

**Clarification on "existence is about short distances."** This is the standard slogan, and it's the core of the existence problem, but it isn't all of it. Existence also needs L → ∞ (the box size going to infinity, from Q1), which does reach long distances. The difference is what you need to know there. For existence, you only need the infinite-volume limit to exist and satisfy the axioms. For the gap, you need a specific quantitative fact about the long-distance physics.

#### 2. What a gap is, and why a free massless field has none

**Mass gap Δ (Delta):** the lowest energy of any state above the vacuum, which has energy 0. For a single particle of mass m and momentum p, the energy is

$$E = \sqrt{p^2 + m^2} \;\geq\; m$$

So the gap is the mass of the lightest particle.

- **Massive free field (m > 0):** every excitation costs at least m, so Δ = m.
- **Massless free field (m = 0):** E = |p|, and a long enough wavelength makes p as small as you like. Excitations exist at arbitrarily low energy, so there is no gap.

A free massless field still satisfies every Wightman axiom. So "the theory exists" and "the theory has a gap" are independent statements.

**Classical Yang-Mills.** Linearize the classical field equations for small amplitudes and you get waves moving at the speed of light, at any frequency, just like electromagnetic waves. In perturbation theory (an expansion in powers of g) the gluon stays massless at every order. So neither the classical theory nor any finite order of perturbation theory shows a gap.

**Semiconductor analogy.**

| QFT | Solid state |
|---|---|
| Gapless theory (free massless field) | Metal: excitations at arbitrarily low energy above the Fermi level |
| Gapped theory | Insulator: a minimum energy cost E_g to excite anything |
| Correlations decay as e^(−Δr) | Insulator response is local; disturbances decay over a finite length |

The closer match is a **Mott insulator**. Band theory treats electrons as non-interacting and predicts a metal. Strong electron-electron repulsion opens a gap anyway. That is the Yang-Mills situation: the weak-coupling picture says gapless, and strong interactions at long distance are expected to open a gap.

**Where the analogy breaks down.**

- An ordinary band gap comes from an external periodic potential, the crystal lattice. Nothing external produces the Yang-Mills gap.
- A Mott gap is set by an energy scale written into the Hamiltonian, the on-site repulsion U. Pure Yang-Mills has no energy scale anywhere in its equations. Where the gap's scale comes from is the dimensional-transmutation point below.

#### 3. Why the gap is "nonperturbative": a short derivation

Solve the running-coupling formula for Λ:

$$\ln(\mu/\Lambda) = \frac{1}{b\,g^2(\mu)} \quad\Longrightarrow\quad \Lambda = \mu \, e^{-1/(b\,g^2(\mu))}$$

Look at the function f(g) = e^(−1/(b g²)) near g = 0:

- f(0) = 0
- Every derivative of f is also 0 at g = 0
- So its Taylor series in g is 0 + 0·g + 0·g² + … , identically zero, even though f itself is not zero

Perturbation theory is a Taylor series in g, so any quantity proportional to Λ is invisible at every order, including the gap, since Δ ∝ Λ. That is the precise meaning of **nonperturbative**: the effect is real but has no power-series expansion around g = 0.

**Why "purely quantum."** The running of g comes from quantum loop effects, and b carries a factor of ħ. As ħ → 0, the exponent −1/(b g²) → −∞, so Λ → 0. The scale, and with it the gap, disappears in the classical limit, which matches the classical theory having massless waves.

**DSP-flavored way to see it:** e^(−1/(b g²)) is like a signal that is exactly flat to every order at the origin but nonzero away from it. You can't recover it from any number of derivatives taken at that point.

#### 4. Dimensional transmutation

**Classically there is no scale.** The pure Yang-Mills equations in 4D contain only the dimensionless g. You can't build a mass from a dimensionless number alone. A classical solution can be rescaled to any size and is still a solution, so the classical theory is scale-invariant.

**Quantum mechanically, a scale appears.** Because g runs, "the coupling" means nothing until you say at which scale μ it is measured. The theory is specified by the pair (μ, g(μ)). Different pairs on the same running curve describe the same theory, and the combination that stays constant along the curve is

$$\Lambda = \mu \, e^{-1/(b\,g^2(\mu))}$$

which is the same for every μ, by construction.

So the theory trades a dimensionless number g for a dimensionful scale Λ. That trade is the **transmutation**. Every mass in pure Yang-Mills must then be a pure number times Λ, including the gap: Δ = c₀·Λ, where c₀ is some fixed number.

**Rough numbers for SU(3), approximate and scheme-dependent:** Λ is a few hundred MeV (million electron-volts). Lattice simulations put the lightest glueball at about 1.6–1.7 GeV (giga-electron-volts), several times Λ.

**One link the primer's wording skips.** Dimensional transmutation gives the theory a scale. It does not by itself prove that the gap is greater than zero, because a theory with a scale can still contain massless particles. Real QCD with massless quarks is the standard example: it has a scale Λ, yet pions would be exactly massless. Pions are Goldstone bosons, massless particles forced by a broken symmetry. Pure Yang-Mills is expected to have no such massless particles, but proving that is precisely the content of "Δ > 0." Transmutation explains where the gap's size would come from; the theorem has to show the gap is actually there.

**One-line summary:** the gap is a long-distance, strong-coupling effect proportional to e^(−1/(b g²)), which no power series in g can see. It exists only because quantum running turns a scale-free classical theory into one with an intrinsic scale Λ.

### Q3. Simplified version of Q2: what it is and why

**What the passage says:** proving Yang-Mills *exists* and proving it has a *mass gap* are two different problems, aimed at opposite ends of the distance scale. Solving the first doesn't solve the second.

**1. Existence is a short-distance problem.**

- **What:** to build the theory rigorously, you shrink the lattice spacing to zero, which means controlling what happens at extremely short distances.
- **Why that's manageable:** at short distances the force between gluons gets weak. That property is called asymptotic freedom; gluons are the force-carrying particles of Yang-Mills. When the force is weak, you can treat the theory as "nearly free plus small corrections" and keep the corrections in check.

**2. The mass gap is a long-distance problem.**

- **What:** the mass gap means the lightest possible particle has a nonzero mass. Equivalently, it costs a minimum amount of energy to create anything at all.
- **Why that's hard:** at long distances the force becomes strong. There is no "small correction" left to expand in, so the standard tools stop working.

**3. A theory can exist without a gap.**

- **What:** light is the example. The photon is massless, and you can make a photon with as little energy as you like by giving it a long enough wavelength. Electromagnetism is a perfectly good theory with no gap.
- **Why it matters:** the existence proof alone can't tell you whether there's a gap. That has to be shown separately.
- **Analogy:** a metal versus an insulator. Both are real materials, but only the insulator has a band gap. Proving a material exists doesn't tell you which kind it is.

**4. On paper, Yang-Mills looks gapless.**

- **What:** the classical (non-quantum) equations describe massless waves moving at light speed, just like light. The usual approximation methods (perturbation theory) also show massless gluons, no matter how far you carry them.
- **Why:** the gap is a purely quantum effect that only appears when the force is strong. Those methods only work when the force is weak, so they can't see it, even in principle.

**5. "Dimensional transmutation": where the gap's size would come from.**

- **What:** the Yang-Mills equations contain no mass or energy scale at all, just a pure number for the force strength. Quantum effects make that strength change with distance. That change picks out one particular scale, called Λ (lambda), where the force becomes strong. Any mass in the theory, including the gap, has to be some multiple of Λ.
- **Why it's called that:** a unitless number (the force strength) gets "transmuted" into a quantity with units (an energy, Λ).
- **Caveat:** having a scale Λ means a gap *could* exist and tells you roughly how big it would be. It doesn't prove the gap is there. That proof is the open half of the Clay problem.

**Bottom line:** existence means the theory is mathematically well-defined, and it's achievable because the force is weak at short distances. The gap means the theory's particles have mass, and it's still open because the force is strong at long distances, where no one has rigorous tools. OpenAI's claim covers only the first part.

### Q4. Confinement, Wilson loops and the "deep half" (Section 5), simplified

> Confinement is a further, separate statement. In pure Yang-Mills it is usually phrased with Wilson loops: the expectation of a large loop C falls off with the area it encloses, which means a linear potential between static color charges, with string tension σ. … Confinement is believed to imply a gap, but the two are not the same claim, and neither is part of the existence statement. Lattice simulations give overwhelming numerical evidence for both, as the KITP statement notes, but evidence is not proof. With quarks added, as in real QCD, confinement is subtler still, because flux strings can break by pair creation. This is why physicists call the gap the physically deep half: it is the part that explains why the strong force is short-ranged and why hadrons have mass, and nobody has a rigorous handle on it in 4D.

**What the passage says:** confinement, the fact that quarks and gluons never appear on their own, is a third claim, separate from both existence and the mass gap. Physicists are convinced it's true from computer simulations, but no one has proved it. The gap is called the "deep half" of the Clay problem because it explains real-world features of the strong force.

**1. Confinement is its own claim.**

- **What:** confinement says you can never pull a color charge free. A color charge is the strong-force version of electric charge, carried by quarks and gluons. The harder you pull two of them apart, the more energy it takes, without limit.
- **Why it's separate:** existence says the theory is well-defined, and the gap says its lightest particle has mass. Neither statement, as worded, says charges can't be separated. Confinement needs its own proof.

**2. The Wilson loop is how you test for confinement.**

- **What:** imagine creating a heavy, stationary color charge and its opposite, holding them a distance R apart for a time T, then letting them annihilate. In spacetime their paths trace out a rectangle, the loop C, with area R × T. The Wilson loop W(C) measures how likely the theory makes that process. ⟨W(C)⟩ means its average value over all quantum fluctuations.
- **Why it works:** quantum mechanics says ⟨W(C)⟩ ≈ e^(−V(R)·T), where V(R) is the energy needed to hold the pair a distance R apart. So how the loop's value falls off tells you how that energy depends on distance.

**3. The "area law" means a constant pulling force.**

- **What:** confinement is the claim that for large loops ⟨W(C)⟩ ≈ e^(−σ·Area) = e^(−σ·R·T).
- **Why that means confinement:** comparing with step 2 gives V(R) = σR. The energy grows in a straight line with distance, so the force stays constant however far apart you pull. The number σ (sigma), the **string tension**, is that constant force.
- **Picture:** a tube of gluon field, a "flux tube," forms between the charges and behaves like an unbreakable rubber band. Every extra meter of stretch costs the same energy.
- **Contrast:** electric charges give V(R) ∝ −1/R. The energy levels off, so you can pull them apart with finite energy. That's why atoms can be ionized but protons can't be split into free quarks.
- **Where the analogy breaks down:** a real rubber band pulls harder the more you stretch it. A flux tube pulls with the same force at any length.

**4. Confinement and the gap are related but not identical.**

- **What:** physicists expect confinement to imply a gap, since a flux tube costs energy to create, so there's a minimum energy. But "the lightest particle has mass" and "charges can't be pulled apart" are different mathematical statements. Proving one doesn't automatically prove the other.
- **Why neither belongs to existence:** existence is a short-distance result (Q3). Confinement and the gap are both long-distance, strong-force effects.

**5. Simulations are convincing but don't count as proof.**

- **What:** lattice computer simulations clearly show both a gap and the area law.
- **Why that's not enough:** simulations run at a few lattice spacings in finite boxes. A proof has to cover the limit of zero spacing and infinite volume. It's like seeing a chip pass on every test vector you ran versus formally verifying the design.

**6. With real quarks, the "string" can break.**

- **What:** in real QCD (quantum chromodynamics, which has quarks as well as gluons), stretch a flux tube far enough and its stored energy becomes enough to create a new quark–antiquark pair out of the vacuum. That's E = mc² at work. The tube snaps, and each end grabs one of the new quarks.
- **Why it's subtler:** you never get a free quark, just two new bound particles. But the energy no longer grows forever, so the clean area-law test from step 3 fails even though quarks are still confined. Defining confinement precisely gets harder.
- **Analogy:** cutting a bar magnet doesn't give you a lone north pole. You get two smaller magnets.

**7. Why the gap is "the physically deep half."**

- **What:** the gap is what explains two everyday facts about the strong force:
  - **It's short-ranged.** Its effects die off within about the size of a proton, unlike gravity or electromagnetism.
  - **Hadrons have mass.** Hadrons are particles made of quarks and gluons, like protons and neutrons. Most of a proton's mass comes from the strong-force field energy, not from the quarks' own masses.
- **Why it's still open:** both effects happen where the force is strong, and in 4D (three dimensions of space plus time) no one has rigorous mathematical tools that work there.

**Bottom line:** confinement means color charges are tied together by flux tubes that never let go; mathematically it's the area law, V(R) = σR. It's believed to imply a gap but is a different claim, and both are supported by simulations but unproved. The gap is the "deep half" because it explains why the strong force is short-ranged and why protons are heavy, and OpenAI's claim addresses neither.
