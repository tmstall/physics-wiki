---
type: deep dive (not a paper analysis)
title: Yang-Mills existence and the mass gap: seven-thread deep dive, plus Lean
date: 2026-11-07
source: User-led deep dive on 2026-10-30_primer_yang-mills-existence-mass-gap (Oct 30 primer), run Nov 5-7, 2026
framework: Academic Paper Analysis Framework v3.17 calibration (tiers, plain-language budgets, confidence and source tags)
posture: adversarial for the OpenAI claim (unreleased, unreviewed)
status: OpenAI existence claim unverified; Lean proof expected the week of Nov 9, 2026; mass gap not claimed
suggested_pages: concepts/osterwalder-schrader-axioms, concepts/reflection-positivity, concepts/lattice-gauge-theory, concepts/balaban-rg-program, concepts/cluster-expansion, concepts/triviality-vs-asymptotic-freedom, concepts/grassmann-integration, concepts/fermion-doubling, concepts/lean-proof-assistant, concepts/statement-fidelity
---

# Yang-Mills existence and the mass gap: deep dive

*A seven-thread curriculum built on the Oct 30 primer: what it means for the theory to exist, gauge theory on a grid, Balaban's rigorous coarse-graining, why some theories die in the continuum limit, quarks and the gap toolkit, what Lean can and cannot certify, and a pass/fail checklist for the OpenAI release. Ends with a standalone explainer on Lean.*

## Contents

0. [Status and scope](#0-status-and-scope)
1. [Thread 1: what "existence" means](#thread-1-what-existence-means)
2. [Thread 2: gauge theory on a grid](#thread-2-gauge-theory-on-a-grid)
3. [Thread 3: what Balaban built](#thread-3-what-balaban-built)
4. [Thread 4: why some theories die in the limit](#thread-4-why-some-theories-die-in-the-limit)
5. [Thread 5: quarks, and the gap toolkit](#thread-5-quarks-and-the-gap-toolkit)
6. [Thread 6: can Lean settle it?](#thread-6-can-lean-settle-it)
7. [Thread 7: what would count as failure?](#thread-7-what-would-count-as-failure)
8. [Companion: Lean explained](#companion-lean-explained)
9. [Corrections made during the deep dive](#corrections-made-during-the-deep-dive)
10. [Sources](#sources)

> [!WARNING]
> **Status as of Nov 7, 2026:** OpenAI's claimed existence proof is unverified. No Lean proof or written proof has been released. The mass gap is not claimed.

## 0. Status and scope

**What is claimed.** OpenAI describes the physics work as an existence proof for certain interacting four-dimensional quantum field theories: QCD, and the simplest grand unified theory containing the Standard Model's fields. Existence of pure Yang-Mills is a subproblem. The proof is built on Balaban's approach (Thread 3). Reported timeline: written Yang-Mills proof Sep 9, written QCD proof Sep 18, Lean formalization of Yang-Mills existence completed Oct 16, public announcement Oct 26.

**Committee status.** The shepherding committee (Gross, chair; Douglas, Jaffe, Klebanov, Nekrasov) issued a second statement on Nov 3. It is checking that the Lean definitions and problem statements match the standard ones in physics and mathematics, and that the formal and informal versions agree, and it hopes to release the Lean proof the following week with a full day's notice. Per Woit's blog, the committee's attached rules say the long AI-written proof will stay private for the committee's own use, which differs from the primer's expectation of a later full release. That point comes secondhand; check the rules document directly. For its math and complexity results OpenAI published a scope-of-verification document; for Yang-Mills it has published none.

**Calibration.** Constructive field theory, lattice gauge theory, and rigorous renormalization are built here from first principles (tier 3). Formal verification (Thread 6 and the Lean companion) is taken at colleague speed (tier 1). The primer's Q&A notes lean on signal-processing framings and dense notation; this deep dive routes analogies through computer systems instead and keeps symbols out of the prose.

**Thread map.**

| Thread | Topic | Tier |
| :-- | :-- | :-- |
| 1 | What "existence" means: the axioms as a contract, reflection positivity | 3 |
| 2 | Gauge theory on a grid: links, plaquettes, strong-coupling confinement | 3 |
| 3 | What Balaban built: rigorous coarse-graining and its error budget | 3 |
| 4 | Why some theories die in the limit: triviality vs. asymptotic freedom | 3 |
| 5 | Quarks, and the gap toolkit | 3 |
| 6 | Can Lean settle it? | 1 |
| 7 | What would count as failure? | mixed |

## Thread 1: what "existence" means

**The idea in plain words.** Physicists compute with Yang-Mills every day, but nobody has shown that the thing they approximate is a well-defined mathematical object. "Existence" means building that object. You start from a grid version that is fine, take the limits, and show the result satisfies a short list of properties. A theorem then guarantees that anything meeting those properties is a genuine relativistic quantum theory. You never build the space of states by hand.

```
Analyst-built concept diagram (not from the primer)

 Grid theory (finite spacing, finite box)  <- always well defined
      |  shrink spacing, retune coupling (Q1)
      v
 Bounds that hold however fine the grid   <- Balaban, finite box
      |  grow the box to infinite size
      v
 Limiting imaginary-time theory           <- claimed, unverified
      |  check the contract: symmetry, reflection
      |  positivity, growth, clustering
      v
 Reconstruction theorem
      v
 Relativistic quantum theory              = "existence"
      |
      +--> genuinely interacting?          part of existence
      +--> positive gap?                   open, not claimed
```

Read it top to bottom. Each arrow is a step that has to be proved, not just computed. The two branches at the bottom are separate questions the pipeline does not answer for you.

**Analogy:** the axioms (Osterwalder–Schrader) are an interface specification, and the reconstruction theorem is a conformance guarantee. Any implementation that passes the spec is certified to behave as a full quantum theory.

**Breaks when:** you picture running the conformance suite. Each property has to hold in the limit of an infinitely fine grid in an infinite box. Finite test runs can never establish that, only bounds that hold uniformly at every grid size.

### Why reflection positivity carries the load

In imaginary time the theory looks like a stack of slices. One fixed "step operator" (physicists call it the transfer matrix) advances the system one slice. Reflection positivity is the guarantee that every weight this operator assigns is positive. That matters because energies are read off as minus the logarithm of those weights:

$$E = -\ln(\text{weight})$$

**Symbol definitions:**
$E$ : the energy of one mode of the system (in units of one over the grid spacing)
$\ln$ : the natural logarithm
weight : how much of that mode survives one step of the step operator

**What this actually means:** a mode that fades quickly from step to step has high energy, and one that persists has low energy. A negative weight has no logarithm, so no energy, and with no energy there is no Hamiltonian. Positivity is what licenses reading the weights as energies at all.

The smallest case is a chain of up/down spins:

```
Analyst-built illustration (not from the primer)

Panel 1: the chain read as an imaginary-time axis
  slice 0  slice 1  slice 2  slice 3
   [up]----[dn]-----[up]-----[up]----> imaginary time
       step     step     step          (same step each time)

Panel 2: neighbors prefer to align (positivity holds)
  vacuum mode   weight 3.1   -> energy 0 (reference)
  excited mode  weight 2.4   -> fades to 76% per step
  => correlation length ~3.7 sites, gap = 1 / 3.7

Panel 3: neighbors prefer to anti-align
  vacuum mode   weight 3.1
  excited mode  weight -2.4   <- negative: no energy
  => one-slice Hamiltonian does not exist
```

*What to look at:* compare the two excited-mode weights. In Panel 2 the gap is just how fast the excitation fades relative to the vacuum, and the correlation length is its inverse. In Panel 3 a single sign flip leaves you with nothing to take a logarithm of.

**Breaks when:** you conclude the anti-aligned chain is sick. It is a perfectly good statistical model. Stepping two slices at a time squares the weights and restores a Hamiltonian with a doubled time step. The picture shows what positivity *licenses*, not which models are physical.

**Tie-back to the primer's Q1.** On any grid, a gap like Panel 2's is trivially present. Taking the continuum limit means retuning so the correlation length, counted in grid sites, grows without bound while the physical gap stays fixed. The Clay question is whether a positive gap survives that limit. The reflection-positivity link is **(A) Consensus**: it is the standard textbook route (Osterwalder–Schrader, and Osterwalder–Seiler for lattice gauge theory). **(broader literature)**

## Thread 2: gauge theory on a grid

### Why put the field on the links?

Gauge symmetry says that at every point in space, the quark's "color" (a three-component internal direction) has no absolute reference frame. You can rotate the frame at each point independently, and no measurement changes. That freedom is local: point by point, not one global rotation.

The cost of that freedom is that you can't compare colors at two neighboring points directly. You need a translator that says how a color here corresponds to a color there. Wilson's 1974 move was to put that translator on the **link** between neighboring grid sites. Each link variable is a rotation (for quarks, a three-by-three one) that carries color from one site to the next. When you rotate the frame at one site, every link touching that site absorbs the change at that end. The bookkeeping closes exactly at any grid spacing, with no approximation.

**Analogy:** each grid site is a node with its own private data encoding, and each link is a translation table between neighbors. Re-encode one node, update the tables on its links, and nothing observable changes.

**Breaks when:** you go around a closed loop of tables. In the vehicle, translators built from consistent encodings always compose back to "no change," and a mismatch would be a bug. In gauge theory the link variables are independent degrees of freedom. A mismatch around a loop is not a bug. It *is* the physical field.

### The smallest loop is where the physics lives

The smallest closed loop on the grid is a single square, a **plaquette**. Go around its four links, compose the four rotations, and see how far the result is from "no rotation." That leftover is the field strength through that square, the lattice version of a magnetic flux. The theory's action adds up an energy cost for every plaquette's leftover, and the coupling sets the price.

The simplest version, where each link carries a single angle instead of a three-by-three rotation:

```
Analyst-built illustration (not from the primer)

Panel 1: one plaquette, link angles (counterclockwise)
      D <----- (-5) ------ C
      |                    ^
     (+5)                (+20)
      v                    |
      A ------ (+10) ----> B
  loop total = 10 + 20 - 5 + 5 = 30 deg  <- the "flux"
  energy cost ~ 1 - cos(30 deg) = 0.13

Panel 2: re-frame site B by +40 deg
  A->B gains +40:  10 -> 50
  B->C loses 40:   20 -> -20
  loop total = 50 - 20 - 5 + 5 = 30 deg  <- unchanged
```

*What to look at:* the individual link angles change under the re-framing in Panel 2, but the loop total doesn't. Only closed-loop quantities are physical, and the action is built from nothing else. That's why gauge symmetry is exact on the lattice.

For the real theory, each link is a three-by-three rotation, and rotations don't commute. The loop result depends on the order you go around, and only its trace (the sum of its diagonal) is invariant. That non-commutativity is what makes gluons interact with each other (see the Q&A below).

### Why the grid version is so well behaved

- **Exact gauge invariance**, as above. A naive grid version that took finite differences of the continuum field would break it at every finite spacing.
- **No gauge fixing.** Each link variable ranges over a bounded set (all possible rotations), so you can average over every link with a uniform weight and the integral is simply finite. In the continuum you have to pick a gauge to make sense of the integral, and that choice runs into known global obstructions. The lattice sidesteps them.
- **The Thread 1 contract holds at every spacing.** The plaquette action is reflection positive (Osterwalder–Seiler), so a genuine Hamiltonian exists on every grid.

**(A) Consensus:** these are standard results that define the lattice as the starting point for rigorous work. **(broader literature: Wilson 1974; Osterwalder–Seiler 1978)**

### Confinement is provable, on a coarse grid

Confinement is tested with a **Wilson loop**: a large rectangle traced through the lattice, standing for a quark and antiquark held a fixed distance apart for a long time. How its average value shrinks with size tells you the energy between them.

When the coupling is strong, each plaquette's contribution to the average is a small number, set by the coupling. For a big loop to average to anything nonzero, its interior has to be tiled with plaquettes, and each one multiplies in that small factor. With a factor of one tenth, a three-by-three loop encloses 9 plaquettes and averages about one billionth. Stretch it to three-by-six and it's 18 plaquettes, about a billionth of a billionth.

The suppression grows with the **area**, not the perimeter. That "area law" means the quark–antiquark energy grows in proportion to their separation, like a string that never snaps. At strong coupling this is a theorem: the expansion in the small factor provably converges. **(A) Consensus** **(broader literature: Osterwalder–Seiler 1978)**

### Why that doesn't settle anything

The continuum lives at the opposite end. As the grid spacing shrinks, asymptotic freedom drives the coupling toward *weak*, where the convergent expansion no longer applies.

```
Analyst-built concept diagram (not from the primer)

 STRONG coupling <-----------------------------> WEAK coupling
 (coarse grid)                                   (fine grid =
                                                  continuum limit)
 |== area law PROVED ==|........ no proof ........|

 Three colors (QCD):
   confining ======== smooth crossover? ======== confining?
                      (simulations: yes; proof: none)

 Single angle per link (lattice electromagnetism):
   confining ===|transition|=== NOT confining  (PROVED)
```

Read the bottom row first. The single-angle theory also confines at strong coupling, by the same tiling argument, but it is *proved* to go through a phase transition into an ordinary non-confining phase at weak coupling. So "confines on a coarse grid" is no guarantee about the continuum. For the three-color theory, simulations going back to 1980 show a smooth crossover with no transition, but nobody has proved it.

- **(A) Consensus** for the lattice-electromagnetism transition: it is a rigorous result. **(broader literature: Guth 1980; Fröhlich–Spencer 1982)**
- **(A) Consensus, numerically only** for the absence of a transition in the three-color theory. **(broader literature: Creutz 1980 onward)**

Everything on a coarse grid is provable. Everything interesting happens on the weak-coupling side, and getting there with control is what Balaban's rigorous coarse-graining (Thread 3) was built to do.

### Q&A: why does non-commutativity make gluons interact with each other?

> That non-commutativity is what makes gluons interact with each other.

The sentence compresses a three-step chain.

**Step 1: order matters for rotations, not for angles.** Turning a dial ten degrees and then twenty lands you where twenty-then-ten does. Rotations of an object in three dimensions don't commute:

```
Analyst-built illustration (not from the primer)

Phone flat on a table: screen UP, top edge pointing NORTH
  Move X: tip about the east-west axis (top edge swings up)
  Move Y: roll about the north-south axis (east edge swings down)

  X then Y                       Y then X
  after X: top UP, screen S      after Y: top N, screen E
  after Y: top EAST, screen S    after X: top UP, screen E
           ^^^^^^^^                       ^^^^^^^^^^^^^^^
  Different final orientations: X-then-Y != Y-then-X
```

*What to look at:* same two moves, different order, different result. A quark's color frame rotates the same way, with three-by-three rotations in place of the phone's three axes.

**Step 2: what the plaquette loop picks up.** Go around a plaquette: east, north, west, south. With angles, east and west cancel, as do north and south. The only leftover is how much the links *differ* from one side of the square to the other; a uniform field gives zero. That's ordinary electromagnetism. With rotations, a perfectly uniform set of links still doesn't close: do X, then Y, undo X, undo Y, and you aren't back where you started. So the loop picks up a second piece, present even when nothing varies across the square, built from the product of the two link fields themselves:

$$F = (\text{how the field varies across the square}) + [A_x, A_y]$$

**Symbol definitions:**
$F$ : the field strength, the loop's leftover per unit area
$A_x, A_y$ : the gauge field along the two directions of the square (the continuum version of the link rotations)
$[A_x, A_y]$ : the commutator, "do x then y" minus "do y then x"; zero for angles, nonzero for rotations

**What this actually means:** in electromagnetism the field strength is linear in the field. In Yang-Mills it carries an extra term that's quadratic in the field, and that term exists purely because order matters.

**Step 3: square it, and interactions fall out.** The energy cost is the square of the leftover. In electromagnetism that gives only two-field terms: waves that pass straight through each other, which is why two flashlight beams cross without scattering. (Light does scatter off light, but only through virtual electron pairs, the tiny vacuum-nonlinearity effect.) In Yang-Mills, squaring "linear plus quadratic" gives terms with two, three, and four fields multiplied together: places where three or four gluons meet. Gluons carry color charge themselves, so the gluon field acts as its own source. **(A) Consensus:** textbook since Yang and Mills in 1954. **(broader literature)**

**Analogy:** a 3D renderer's transform stack. Rotating a model about x then y gives a different pose than y then x, and an apply–apply–undo–undo sequence in the wrong order leaves a residual rotation.

**Breaks when:** you ask what the residue *does*. In a renderer the transforms are fixed inputs and the residue is inert. In Yang-Mills the link rotations are dynamical, and the residue carries energy that feeds back to shape them. That feedback loop is the self-interaction.

Three later threads hang on this:

- **Thread 4:** gluon self-interaction reverses how the coupling runs compared with electromagnetism. That reversal is asymptotic freedom. **(A) Consensus** (Gross–Wilczek, Politzer 1973)
- **The mass gap:** without the commutator term, pure Yang-Mills would be free electromagnetism times eight, which trivially exists and has no gap. Every bit of difficulty in the Clay problem traces back to this term. **(A) Consensus**
- **Confinement's flux string:** simulations show the field between a quark and antiquark squeezing into a narrow tube. Self-interaction is clearly involved, but why the field forms tubes has no accepted proof. **(B) Contested:** the tubes are well established numerically; competing mechanisms are debated. **(broader literature)**

## Thread 3: what Balaban built

### The problem this solves

On the weak-coupling side of the grid, where the continuum lives, the obvious tool is perturbation theory, but in four dimensions that series doesn't converge. Worse, a fine grid has fluctuations at every scale from the grid spacing up to the box size, and they all talk to each other. You can't integrate them all at once with control.

The renormalization-group answer is to integrate them out **one scale at a time**. Average the field over small blocks of sites, absorb the fluctuations inside each block into a new effective theory on a coarser grid, and repeat. Physicists had done this approximately since Wilson. Tadeusz Balaban's achievement in the 1980s, across about eleven papers covering Yang-Mills in three and four dimensions, was to do it **with a proof** at every step.

### One step of the procedure

Each step has the same anatomy (as summarized in Dimock's expositions): average over blocks; split space into large-field and small-field regions; pin down the effective action in the small-field regions with a controlled expansion; read off flow equations for the theory's parameters; show the large-field regions contribute almost nothing.

The crucial demand is that the bounds hold **however many steps there are**. The number of steps grows as the grid gets finer, and the continuum limit sends it to infinity. A bound that degrades with the number of levels is worthless.

**Analogy:** a deep reduction tree computing a sum over billions of values, where each level adds rounding error. To trust the result at any depth, the per-level error has to shrink fast enough that the total stays bounded however tall the tree gets.

**Breaks when:** you assume every error component shrinks. In theories where symmetry allows a mass-like term (scalar fields, the QED models Dimock studies), that component *grows* level by level and must be cancelled by fine-tuning the inputs at the finest grid; a reduction tree has no "pre-tune the leaves for what the root will see" step. In pure lattice Yang-Mills, gauge symmetry forbids that growing term, so the only input to set is the starting coupling (see the Q&A below).

### The small-field / large-field split

This is the move that makes the method work. The controlled expansion only works where the field is small: each plaquette's loop is close to "no rotation." Where the field is large, the expansion breaks down. Balaban doesn't analyze those regions in detail. He proves they're *rare*: the plaquette action penalizes large loop leftovers so heavily that the suppression beats the number of ways such regions can be scattered through the box.

```
Analyst-built illustration (not from the primer)

Panel 1: one step, a 2-D slice of the grid
  fine grid, blocks of 3x3 (4-D: 3x3x3x3 = 81 sites)
  +-----+-----+-----+-----+
  |  s  |  s  |  L  |  s  |   s = small field: expand, track
  +-----+-----+-----+-----+       every correction exactly
  |  s  |  s  |  s  |  s  |   L = large field: no expansion,
  +-----+-----+-----+-----+       just prove it's rare
  |  s  |  L  |  s  |  s  |
  +-----+-----+-----+-----+
  each block -> one site of the next, coarser grid

Panel 2: the error budget across levels
  level 1   correction <= 0.10
  level 2   correction <= 0.05
  level 3   correction <= 0.025   ...halving each level
  ---------------------------------------------
  total over ANY number of levels  <= 0.20
```

*What to look at:* Panel 1 shows that the classification is per region and gets redone at every level, because a region that's small at one scale can be large at the next. Panel 2 is the whole point: a bound that holds for an unlimited number of levels, which is what "uniform in the grid spacing" means.

**Analogy:** a CPU fast path and slow path. The common case (small fields) gets a precise, fully accounted fast path. The rare case (large fields) doesn't need to be fast; you only need to prove it's rare enough that its total cost is bounded.

**Breaks when:** on hardware you *measure* how rare the slow path is. Here you need a proof covering every possible arrangement of large-field regions, at every level, re-classified each time. That recursive bookkeeping is where most of Balaban's pages go. Gauge theory adds a twist: "small" only means anything after you pick a local gauge inside each small region, and those choices must be patched together consistently across blocks.

**(A) Consensus** that this is how the method works. **(broader literature: Balaban 1983–89; Dimock 2011–2018)**

### What he actually proved

The result is called **ultraviolet stability**: the partition function (the theory's total weight, a single number) is bounded above and below, uniformly in the grid spacing, in a **fixed finite box**. A 2025 seminar summary (Tanimoto) puts it as bounded partition functions, with convergence still an open question.

That's a real and hard result, but it's one number. A theory is the whole family of correlations. Bounding the total weight shows the construction doesn't blow up; it doesn't show any particular correlation settles down to a limit.

### What was left undone

| Step in the existence pipeline | Status after Balaban |
| :-- | :-- |
| Bounds that hold however fine the grid, finite box | Done (ultraviolet stability) |
| Correlations converge as the grid gets finer | Not done |
| Infinite-volume limit | Not done |
| OS contract in the limit, especially full rotation symmetry restored | Not done |
| Limit is genuinely interacting (not free) | Not done |

Reflection positivity is the *easy* part of the contract, because it survives limits automatically. Rotation symmetry is hard: the grid only has quarter-turn symmetry, and you have to prove full rotation symmetry comes back in the limit. There is a precedent for the next step: in 1986 King proved convergence of correlation functions and some of the OS axioms for a simpler gauge-plus-scalar model in two and three dimensions. Nobody has done the same for four-dimensional Yang-Mills.

- **(A) Consensus** for the table. **(broader literature)**
- **(C) Speculative:** the same seminar notes appear to label the four-dimensional Yang-Mills work "incomplete"; the source is a handwritten slide with garbled text extraction, so treat it as a pointer to check. The primer independently records Bauerschmidt's criticism that Balaban's papers are incomplete and very hard to read. **(analyst inference; primer §6)**

### What this means for the claim

The primer records that the claimed proof builds on Balaban, and that the committee credits his ideas with following the theory "all the way to infinite distances," exactly the step he never finished. The proof therefore inherits a dozen dense papers from the 1980s that few people have checked line by line. That reaches straight into Thread 6: if the Lean proof takes Balaban's results as assumed inputs rather than formalizing them, the Lean check certifies the new part only *conditional on* Balaban being right. **(C) Speculative:** nothing public says which way it went; the release's axiom list will. **(analyst inference)**

### Q&A: the anatomy of one step, unpacked

> Each step has the same anatomy. It averages over blocks, splits space into large-field and small-field regions, and pins down the effective action in the small-field regions with a controlled expansion. That gives flow equations for the theory's parameters. Renormalization means fine-tuning the starting values of those equations, and the large-field regions are shown to contribute almost nothing.

That wording was paraphrased from an abstract about QED in three dimensions, and the "fine-tuning" clause doesn't carry over cleanly to Yang-Mills (corrected below).

**"It averages over blocks."** For an ordinary field, replace each block with its average value. Gauge fields don't allow that: the average of two rotations generally isn't a rotation. Balaban's block step works with translators instead. For each pair of neighboring blocks, take the fine-grid paths that cross from one block's center to the other's, compose the link rotations along each path, average those composed rotations, and snap the result back to the nearest true rotation. That becomes one link of the coarser grid. Re-framing a block shifts every path consistently, so gauge symmetry survives the step exactly.

**"Pins down the effective action with a controlled expansion."** Integrating out a block's internal fluctuations creates a new effective action. The danger is couplings between everything and everything. The cluster expansion proves that doesn't happen in small-field regions: the new action splits into pieces, each depending only on one connected cluster of blocks, with size shrinking exponentially as the cluster grows (unpacked further in the next Q&A).

**Analogy:** a dependency graph that stays local; influence from far away falls off exponentially, so you can bound the total by summing local contributions.

**Breaks when:** you treat locality as a design choice. Here it has to be *proved* at every level, and it fails exactly in large-field regions, which is why they're carved out.

**"That gives flow equations."** After each step the effective action is the **same form** as the start (a plaquette action) plus a remainder. The coupling creeps up slightly at each coarser level (asymptotic freedom read backward), and the remainder shrinks by a fixed fraction per step, the halving in the error-budget panel.

**Correction: "fine-tuning the starting values."** In scalar and QED models, symmetry doesn't forbid a mass-like term, which grows at every coarser level and needs its starting value tuned exquisitely. Pure lattice Yang-Mills is cleaner: gauge symmetry forbids a gluon mass term outright. The only growing piece is a constant overall energy offset, trivially subtracted. What's left is a **single knob**, the starting coupling, chosen as the grid spacing shrinks so you land on a fixed coupling at a fixed physical scale: the dimensional transmutation of the primer's Q2–Q3, not fine-tuning. **(A) Consensus** for the single-knob picture; Balaban's bookkeeping carries extra technical terms, but none of them is a gluon mass. **(broader literature)**

**"The large-field regions contribute almost nothing."** A large field costs energy divided by the coupling, so at weak coupling large fields are suppressed exponentially. The coupling is weakest on the finest grids, where there are the most sites, which is what makes the counting close.

**Why Balaban stops at a finite box:**

```
Analyst-built illustration (not from the primer)

level   coupling (weak -> strong)
  1     #
  2     #
  3     #             creeps up slowly, level by level;
 ...    ##            expansion and error budget hold
  N     ###           <- box size reached: Balaban stops
------------------------------------------------------
 N+1    ####          past the box: coupling keeps
 N+2    ######        growing; small-field expansion
 N+3    ##########    fails; gap and confinement live here
```

*What to look at:* the line between level N and the rest. Every argument here needs weak coupling. Fix the box small enough that the coupling is still weak at its largest scale, and the whole tower is under control. Growing the box means continuing the flow into strong coupling, where Thread 2's tiling argument lives; the two regimes have never been joined with proof. **(A) Consensus:** the finite box is where the weak-coupling method runs out. **(broader literature)** (Thread 5 refines what the infinite-volume limit specifically requires.)

### Q&A: the cluster expansion, unpacked

> The expansion (a "cluster expansion") proves that doesn't happen in the small-field regions. The new action splits into a sum of pieces. Each piece depends only on one connected cluster of blocks, and its size shrinks exponentially as the cluster gets bigger. Big, far-reaching pieces exist, but they're exponentially small.

The passage is right but leaves out the half of the argument that can fail: the *number* of pieces also grows exponentially, so shrinkage has to beat growth.

**Where far-reaching pieces come from.** The fluctuations integrated out at each step straddle block boundaries, so neighboring blocks end up weakly linked through the detail you removed. Block averaging keeps those fluctuations short-ranged: their influence fades by a roughly fixed factor per block of distance. A piece tying together a chain of blocks pays that factor once per extra block.

**Why only connected clusters appear.** The effective action is minus the logarithm of the total weight. If two groups of blocks aren't linked by any chain, their weights multiply, and the logarithm turns the product into a sum of two separate terms. Every surviving piece corresponds to blocks joined by a chain of links: a connected cluster.

**Analogy:** cost accounting for jobs on a machine. Independent jobs add their costs; a cross-term such as contention appears only among jobs connected through a chain of shared resources, and every extra hop makes it weaker.

**Breaks when:** you assume the sharing is given. Here it's created by the integration step itself, and its weakness has to be proved fresh at every level; in large-field regions it isn't true.

**The counting race:**

```
Analyst-built illustration (not from the primer)

Connected clusters containing one marked block (2-D grid)

 size   shapes containing   weight of     total from
 (k)    the marked block    each piece    this size
 ----   -----------------   ----------    ----------
  1            1              1             1
  2            4              0.1           0.4
  3           18              0.01          0.18
  4           76              0.001         0.076
                               --> shrinking ~0.4x per size
                               --> sum converges (about 1.7)

 Same counts, link factor 0.5 instead of 0.1:
  2            4              0.5           2.0
  3           18              0.25          4.5
  4           76              0.125         9.5
                               --> growing ~2x per size
                               --> sum diverges: no bound
```

*What to look at:* shape counts grow about fourfold per size step, so the link factor must be well under a quarter for the totals to shrink. At one tenth the sum closes; at one half, growth wins and the expansion proves nothing. In four dimensions there are more shapes per step, so the factor must be smaller still. **(A) Consensus:** this counting is the standard workhorse of constructive field theory. **(broader literature: Glimm–Jaffe–Spencer 1970s; polymer expansions)**

**Why locality makes the tower stand up.** A convergent expansion makes the new action *local*, so the recursion closes (the next block step has a local action to start from), and the bounds come out proportional to the box size, the healthy "bulk dependence on the volume" Dimock describes.

**Two things to carry forward.** First, the same race decides where the method dies: as the coupling creeps up, the link factor grows until it beats the shape counts, which is the line where Balaban stops, seen from the inside. Second, the strong-coupling side of Thread 2 also rests on a convergent cluster expansion, in the opposite small number. Both ends of the coupling axis are controlled; the middle is where neither small number is small. **(A) Consensus** that both regimes rest on convergent expansions. **(B) Contested** whether the middle is a genuine obstacle or a technical gap. **(broader literature)**

## Thread 4: why some theories die in the limit

### What "dying" means

A theory can survive the continuum limit and still lose everything interesting. "Trivial" means the limit exists but is a **free** theory: the interactions have gone to zero and particles pass through each other untouched. Existence alone is cheap if you accept that outcome. The Clay problem demands the theory with the expected short-distance behavior of real Yang-Mills, which a free theory fails, so nontriviality is part of what has to be proved.

### The coupling depends on how closely you look

The strength of an interaction depends on the scale you probe (the primer's dimensional transmutation). The new point here is the **direction** of the change:

- **The simplest self-interacting field** (one number per point, interacting with itself; the textbook "phi-fourth" model) **and electromagnetism:** the coupling gets *stronger* as you look closer.
- **Yang-Mills:** the coupling gets *weaker* as you look closer. This is asymptotic freedom, and it traces directly to gluon self-interaction (Thread 2 Q&A). Virtual electron pairs screen an electric charge, so it looks weaker from far away and stronger up close. The gluon cloud spreads color out, so color looks stronger from far away and weaker up close.

### Why the direction decides life or death

The continuum limit means fixing the physics at an everyday scale and running the coupling *down* to an ever-finer grid. Track the inverse of the coupling: big means weak, zero means infinitely strong.

```
Analyst-built illustration (not from the primer)
(illustrative numbers, shaped like the leading-order running)

inverse coupling, starting at 10 at the physical scale;
each row = look 10x closer (one more "zoom")

 zoom   Yang-Mills (+2 per zoom)   phi-fourth (-2 per zoom)
 ----   ------------------------   ------------------------
  0       10                         10
  1       12                          8
  2       14                          6
  3       16                          4
  4       18                          2
  5       20                          0   <- coupling infinite:
  6       22                         --      the wall
 ...      keeps growing:             cannot go finer
          coupling -> 0 smoothly
```

*What to look at:* the right column hits zero after a finite number of zooms. To put the grid 10 zooms down, phi-fourth's inverse coupling must start at 20 or more; to make the grid *infinitely* fine, it must start at infinity, which means zero coupling at the physical scale. The continuum limit exists only as a free theory. The left column never hits a wall: the coupling fades smoothly, so Yang-Mills can keep a fixed, nonzero coupling at the physical scale all the way to the continuum.

**Analogy:** the inverse coupling is a counter, decremented once per zoom level in phi-fourth and incremented in Yang-Mills. The decrementing counter underflows after a fixed number of levels; to survive arbitrarily many levels you must start it arbitrarily high, which in the end means "no interaction."

**Breaks when:** you take the underflow as a literal wall. The counter is only the leading-order running. On the actual lattice, phi-fourth is well defined at any coupling, and nothing breaks at a particular scale; what happens is that the continuum limit comes out free. The counter suggests the conclusion but can't prove it, because higher-order or non-perturbative effects might in principle have stopped the countdown.

### The rigorous version

That "might in principle" is why a theorem was needed. In higher dimensions triviality was proved in the early 1980s (Aizenman; Fröhlich). In four dimensions, the marginal case, it was proved by Aizenman and Duminil-Copin in 2021, without leaning on the counter argument. **(A) Consensus:** published in Annals of Mathematics and accepted. **(broader literature)**

Electromagnetism and the Higgs self-interaction run the same direction as phi-fourth, which is a main reason physicists treat the Standard Model as an effective theory valid down to some very short distance. **(A) Consensus** for the effective-theory view. Their rigorous triviality is **(B) Contested:** widely expected but proved only for the simpler scalar model. **(broader literature)**

### The catch: asymptotic freedom cuts both ways

Asymptotic freedom made Balaban's tower possible: weak coupling at fine scales is where his expansions converge. But it's a perturbative statement about short-distance running. It makes a nontrivial continuum *plausible*; it doesn't prove one exists. And it has a price: read the left column upward and the coupling *grows* toward long distances, which is the line in Thread 3's picture where Balaban stops. The property that makes the short-distance limit tractable drives the long-distance behavior into strong coupling, where the gap and confinement live. **(A) Consensus** **(broader literature)**

### What this means for the claim

Nontriviality is a checkable layer. The released material should *prove* that the limit isn't free: for example by showing four-point correlations differ from the pattern a free theory forces, or that short-distance behavior matches asymptotic freedom. A construction that leaves nontriviality implicit would have solved a strictly easier problem. **(C) Speculative:** a proposed test, not a known weakness. **(analyst inference)**

## Thread 5: quarks, and the gap toolkit

**Scope.** The Clay problem is pure Yang-Mills; quarks aren't required for the prize. But the OpenAI claim explicitly includes QCD and a grand unified theory, so quark handling bears on the claim itself (see Thread 7, test 11). Quarks also show why some theories are *easier* to construct than Yang-Mills.

### How quarks get into a rigorous integral

Quarks are fermions: no two can occupy the same state. The integral formulation encodes that with the **Grassmann variable**. Any two anticommute (swap the order and the sign flips), and any one multiplied by itself gives zero. They have no values, so you can't average over them the way you average over link rotations. Integration over them is a purely algebraic rule: pick out the coefficient of the term in which every variable appears exactly once.

Run that rule over all the quark variables and the result is a **determinant**: the signed sum over every way of pairing quarks with antiquarks, built from a large matrix that depends on the gluon links. Rigorous QCD reduces to Yang-Mills with one extra weight factor, the quark determinant, multiplied into every gluon configuration (with two precision notes in the Q&A below).

**Analogy:** each Grassmann variable is a lock that can be held at most once in any product. Integration enumerates every complete assignment of locks, with signs, which is exactly a determinant, computable in polynomial time. Lattice QCD simulations spend most of their compute on it.

**Breaks when:** you try to sample. Locks with signs aren't probabilities, so you can't draw random quark configurations. Simulations integrate the quarks out first. If the determinant turns negative or complex, as it does for dense quark matter, even the gluon sampling loses its probabilistic meaning: the "sign problem" that blocks direct simulation of neutron-star-density QCD.

**The rigorous upside.** The exclusion rule caps the counting race from Thread 3: each quark variable can appear at most once, so fermionic cluster expansions converge *more* easily than bosonic ones. The flagship example is a two-dimensional self-interacting fermion model (Gross–Neveu), asymptotically free like Yang-Mills and fully constructed in 1985: a complete existence proof for an asymptotically free theory, in lower dimension and without gauge fields. **(A) Consensus** **(broader literature: Gawędzki–Kupiainen; Feldman–Magnen–Rivasseau–Sénéor, 1985)**

### Fermion doubling: the grid sees ghosts

The natural lattice version of a slope compares each site with its neighbors on both sides, and that comparison is blind to one pattern:

```
Analyst-built illustration (not from the primer)

symmetric slope at site n = (value at n+1) - (value at n-1)

  site:          1    2    3    4    5    6
  constant:     +1   +1   +1   +1   +1   +1
    slope:            0    0    0    0        <- "smooth"

  alternating:  +1   -1   +1   -1   +1   -1
    slope:            0    0    0    0        <- ALSO "smooth"!

  (site n+1 and site n-1 always match in both rows)

  1 direction:  1 real quark + 1 ghost   =  2 species
  4 directions: 2 x 2 x 2 x 2            = 16 species
```

*What to look at:* the alternating row is the most jagged pattern the grid can hold, yet the slope rule reads it as smooth. One quark on a four-dimensional grid becomes sixteen.

**Analogy:** a sanity check that compares each element only with the one two positions away; it reads 0101 0101 as constant.

**Breaks when:** you try the obvious fix of adding the adjacent compare. A no-go theorem (Nielsen–Ninomiya) says you can't simultaneously keep locality, exactly one quark species, and the chiral symmetry massless quarks should have. Every fix gives something up. Wilson's fix makes the ghosts very heavy, breaking chiral symmetry on the grid but keeping reflection positivity, so Thread 1's contract still holds. **(A) Consensus** **(broader literature)**

### The gap toolkit: what's actually proved

| Setting | Gap status |
| :-- | :-- |
| Lattice Yang-Mills, strong coupling | **Proved**: the cluster expansion gives exponential decay, a gap in grid units |
| Two-dimensional Yang-Mills | **Solved exactly**, but no propagating gluons, so little transfers to four dimensions |
| Two-dimensional fermion model (above) | **Constructed** in full; the existence half is done |
| Two-dimensional O(3) sigma model (Yang-Mills' closest low-dimensional cousin) | **Open.** Expected, supported by exact solutions and simulations, never proved |
| Four-dimensional continuum Yang-Mills | **Open**: the Clay layer |

The O(3) row is the sobering one: asymptotically free, coupling growing at long distances, and even in two dimensions nobody has proved it has a gap. **(A) Consensus** that it's unproved. **(B) Contested** whether a gap exists at all: a small minority (Patrascioiu and Seiler) argued it might not. **(broader literature)** The difficulty follows asymptotic freedom wherever it goes.

### Why the methods stall

The gap is the inverse of the correlation length (Thread 1), so proving a gap means proving correlations die off exponentially at **long distances**. But long distances are exactly where an asymptotically free coupling grows strong (Thread 4). Every rigorous tool here is a convergent expansion in some small number: weak coupling for Balaban, strong coupling for the tiling argument, exclusion for fermions. At long distances in four-dimensional Yang-Mills there is no small number left.

The non-expansion tools don't reach either. Reflection positivity yields bounds that cap correlations from above, which is how phase transitions get proved; a gap needs proof that correlations *fall* fast. The correlation inequalities that settled the phi-fourth question have no known counterpart for non-commuting gauge groups. **(B) Contested:** most experts read this as a missing idea, not just missing labor. **(broader literature + analyst inference)**

**Refinement of Thread 3.** Uniform bounds can sometimes extract *a* limit by a compactness argument, with no long-distance control at all. What genuinely needs long-distance control is showing the limit is unique and that distant regions become independent (clustering). So the place to look first in the claimed proof is how it gets clustering and uniqueness in infinite volume. **(C) Speculative** **(analyst inference)**

### What this means for the claim

The claim is existence, not the gap, which is what this toolkit predicts is within reach of a heroic extension of known methods. A future claim of the *gap* should get much more skepticism: it would need a genuinely new kind of idea, one that controls long-distance decay without a small parameter. The two-dimensional O(3) model is the obvious proving ground: a method that can't settle its gap is unlikely to settle four-dimensional Yang-Mills. **(C) Speculative**, but a concrete benchmark. **(analyst inference)**

### Q&A: Grassmann variables and the determinant

> Quarks are fermions: no two can occupy the same state. The integral formulation encodes that with a strange kind of variable, the Grassmann variable. … So rigorous QCD reduces to Yang-Mills with one extra weight factor, the quark determinant, multiplied into every gluon configuration.

**What "no values" means.** If a variable anticommutes with itself, it equals minus itself, so as an ordinary number it would be zero. Grassmann variables are formal symbols with multiplication rules, not quantities. Two consequences: any product using a variable twice vanishes, so every exponential series stops after finitely many terms (on a finite grid the quark integral is exact, finite algebra); and "integration" is a bookkeeping rule, not a sum over values.

**Analogy:** coefficient extraction from a generating function: expand symbolically and read off the coefficient of one specific monomial ("every variable once").

**Breaks when:** you expect the coefficient to *count* something. Reordering flips signs, so it's a *signed* count, and the signs are where fermion physics lives.

**Where the exclusion principle hides.** If two quarks are forced into the same state, their columns of couplings are identical, the paired terms cancel, and the determinant is zero. Configurations putting two quarks in one state contribute nothing. **(A) Consensus** **(broader literature)**

**What "one extra weight factor" really costs.** The gluon action is local (a sum over plaquettes); the determinant depends on every link at once. Rewritten as an exponential, its exponent is a sum over **every closed path a quark can hop around**, each weighted by the product of link rotations along it: each closed quark path is a Wilson loop from Thread 2. Each hop costs a factor set by the quark's mass. Heavy quarks: long loops heavily suppressed, quarks a small local correction, expansions converge. Light quarks: long loops cheap, the weight genuinely long-range. Real up and down quarks are light, so the physical regime is the hard one. **(A) Consensus** (the "hopping expansion") **(broader literature)**

**Precision note 1: the weight must be non-negative.** On Wilson's lattice a symmetry makes the determinant real, but for one quark flavor it can be negative. With two flavors of equal mass the weight becomes a square, non-negative, so the probability picture and reflection positivity survive. At nonzero quark density it turns complex: the sign problem at its source. **(A) Consensus**

**Precision note 2: quark observables need more than the weight.** For the total weight and purely gluonic quantities, "Yang-Mills times the determinant" is the whole story. A quantity involving quarks, such as a meson mass, also needs the inverse of the same matrix: the quark propagator, the amplitude for a quark to travel between sites through the gluon background. **(A) Consensus**

### Q&A: watching the determinant appear, step by step

Treat it as a game with tokens: antiquark tokens (A1, A2, …) and quark tokens (Q1, Q2, …), multiplied into strings, with three rules:

1. **Swapping two neighbors flips the sign.**
2. **A string that uses any token twice is zero.**
3. **"Integration" is the final read-out:** discard every string that doesn't use each token exactly once; put survivors into one standard order, counting sign flips; add up their numbers.

The theory hands you an exponential, with series 1 + x + x²/2 + x³/6 + … (real physics puts a minus sign in the exponent; it changes nothing about the idea).

**Warm-up: one quark, one antiquark, coupling 3.**

```
exponential  =  1  +  x  +  x²/2  +  ...      (x = 3·A1·Q1)

  1     uses no tokens                 -> rule 3: discard
  x     = 3·A1·Q1, uses each once      -> KEEP: 3
  x²    = 9·A1·Q1·A1·Q1, A1 twice      -> rule 2: zero
  x³... even more repeats              -> zero

  answer = 3   (a one-by-one determinant is just the number)
```

**Two quarks, two antiquarks.**

```
                quark 1    quark 2
 antiquark 1       3          1
 antiquark 2       2          4

x = 3·A1Q1 + 1·A1Q2 + 2·A2Q1 + 4·A2Q2   (four pair-terms)
```

A pair such as A1Q1 can be moved past another pair freely (an even number of swaps, so the sign flips cancel). Pairs behave like ordinary numbers; only individual tokens are touchy.

```
STEP 1 — "1" and "x":
  "1" has no tokens; each term of x has only 2 of the 4
  -> rule 3: all discarded

STEP 2 — x²/2: multiply x by itself (4 x 4 = 16 products)
  most use a token twice and die, e.g.
     A1Q1 · A1Q2   (A1 twice)  -> zero
  survivors use A1, A2, Q1, Q2 once each:
     (3·A1Q1)(4·A2Q2)  and  (4·A2Q2)(3·A1Q1)  -> 2 copies
     (1·A1Q2)(2·A2Q1)  and  (2·A2Q1)(1·A1Q2)  -> 2 copies
  pairs commute, so each survivor appears twice;
  the 1/2 in x²/2 cancels the doubling:
     12 · A1 Q1 A2 Q2   +   2 · A1 Q2 A2 Q1

STEP 3 — x³ and beyond:
  would need 6+ tokens from only 4 kinds -> repeats -> zero

STEP 4 — standard order A1 Q1 A2 Q2:
  straight survivor:  A1 Q1 A2 Q2   already in order  -> +12
  crossed survivor:   A1 Q2 A2 Q1
     swap A2,Q1  ->  A1 Q2 Q1 A2    (flip 1)
     swap Q2,Q1  ->  A1 Q1 Q2 A2    (flip 2)
     swap Q2,A2  ->  A1 Q1 A2 Q2    (flip 3)
     three flips = odd = net minus     -> -2

  read-out:  12 - 2 = 10  =  3·4 - 1·2  (the 2x2 determinant)
```

**Why it's always a determinant.** The only survivors are the **matchings**: ways of assigning each antiquark to a different quark. Each survivor's number is the product of its matched couplings, and its sign is set by whether reordering takes an even or odd number of swaps. That's the definition of a determinant, word for word. With three quarks there are six matchings, with ten about 3.6 million, all sorted out by the same rules.

**Back to physics.** Matchings are the ways quarks and antiquarks pair up through the gluon field; the sign from swapping is the rule that exchanging two identical fermions flips the amplitude's sign; and exclusion comes for free: with identical quark columns (3, 3 on top, 2, 2 below), straight gives 6, crossed gives minus 6, total zero.

**Where people usually get stuck in the two-and-two case:** (1) why most of the sixteen products die (any product reusing a token is zero); (2) why the 1/2 disappears (each survivor shows up twice, once in each order); (3) why the crossed term is negative (an odd number of neighbor swaps). For the rest of the deep dive, the one sentence that matters is: *integrating out quarks is exact algebra, it produces a determinant, and that determinant builds in the exclusion principle.*

## Thread 6: can Lean settle it?

### The Standard Model part, and Thread 4

The claim's "unified completion" is the simplest grand unified theory containing the Standard Model's fields (primer §6). Embedding the forces in one simple gauge group removes the problem of electromagnetism running the "wrong" direction (Thread 4). What remains to check is the scalar sector: if the theory includes Higgs-type scalar fields, their phi-fourth-style self-interaction must also avoid triviality, which requires every coupling in the theory to be asymptotically free, a strong and checkable condition. **(C) Speculative** **(analyst inference)**

### What the kernel actually certifies

A clean Lean build certifies one thing: the proof term type-checks against the stated theorem, using the kernel's rules plus whatever axioms the proof depends on. Mathlib's *proofs* are kernel-checked too, so they aren't part of the trusted base. Its *definitions* are part of the statement's meaning, and that's where trust re-enters. The trusted base:

- **The kernel.** Small, with independent re-checkers available (lean4checker and separate reimplementations).
- **The standard axioms:** propositional extensionality, classical choice, quotient soundness. Uncontroversial for analysis.
- **Anything else the proof leans on:** `sorry`, any declared `axiom`, evaluation shortcuts like `native_decide` (which trusts the compiler), and `implemented_by` or `unsafe` code if the proof relies on it.

`#print axioms` on the main theorem settles the last category in one command. **(A) Consensus** **(broader literature)**

### The real gap: is the statement the right statement?

A clean build proves that the statement written in Lean follows from Lean's axioms. It does not prove that the statement is the theorem the prose claims; a subtly weaker formal statement compiles perfectly. For Yang-Mills this gap is unusually wide, because the spec has never existed.

**Analogy:** a verified compiler. The proof says compiled code behaves exactly as the source language's formal semantics require.

**Breaks when:** you lean on the spec's track record. A verified compiler is trusted because the source-language semantics are a shared, long-debugged artifact. A formal definition of "a quantum Yang-Mills theory on four-dimensional space" has never been written before. It's being written for this proof, by the same side that wrote the proof. The spec has no independent history.

```
Analyst-built concept diagram (not from the primer)

 Clay problem (prose, Jaffe-Witten)
      |   HUMAN JUDGMENT: does the formal statement say
      |   this? (committee is here now)
      v
 Formal statement + definitions (new, bespoke)
      |   MECHANICAL: kernel checks proof term
      v
 Proof term (very large)
      |   AUDIT: #print axioms, sorry, native_decide
      v
 Trusted base (kernel + standard axioms + ???)
```

Lean fully covers only the middle arrow. The top arrow is entirely human and the hardest one here. The bottom arrow is a quick audit, but it decides whether Balaban-style results (Thread 3) were proved or assumed.

### Where a Yang-Mills statement could go subtly wrong

1. **Vacuous witness.** If "a quantum field theory satisfying the axioms" doesn't encode nontriviality, a free theory, or even the zero theory, might satisfy it (Thread 4's lesson in formal clothes).
2. **"Yang-Mills-ness" underspecified.** The Clay text asks for a theory whose local quantities correspond to the gauge-invariant combinations of the curvature, with the short-distance behavior perturbation theory predicts. That correspondence is stated loosely in prose; its formal version is a design choice, and it's what makes the theory Yang-Mills rather than "some interacting theory."
3. **Hypotheses that are never satisfiable.** "If these conditions hold, a theory exists" is worthless if the conditions can't be met. Check that the existence claim is unconditional.
4. **Imported results as axioms.** Balaban's estimates entered as `axiom` rather than proved: a clean build that is also conditional.
5. **Scope drift.** The prize needs existence *and* the gap. An existence theorem should say so plainly.

**(C) Speculative:** none is known to apply; it's the checklist a careful reader should run, and the committee's stated focus suggests it's working the same list. **(analyst inference)**

### Test the spec, not just the proof

Model checking has an established remedy for vacuous specs: vacuity detection and mutation testing of the specification. The analog is a set of **sanity theorems about the definitions**:

- **Positive control:** the free gluon theory should satisfy "quantum field theory" as defined.
- **Negative control:** the free theory should provably *fail* "is Yang-Mills" or "is nontrivial."
- **Short-distance check:** the definition should force asymptotic-freedom behavior, and a deliberately wrong coefficient should fail it.

These are cheap compared with the main proof, and each turns a vague prose worry into a pass/fail compile. **(C) Speculative:** a proposed test, not a known practice for this release. **(analyst inference)**

### Is the Clay problem formalizable at all?

Probably yes in principle, but not off the shelf. Mathlib has the building blocks (Hilbert spaces, measure theory, rapidly decaying test functions, Lie groups), but as far as is known here, no standard formalization of the Wightman or Osterwalder–Schrader axioms. The problem's core definitions would then be bespoke. **(B) Contested:** this picture may be out of date; check what the release imports. **(analyst inference)**

### What the committee's check can and can't certify

**Can:** that the formal statement, in expert judgment, matches the standard definitions; that the kernel accepts the proof; and, via an axiom audit, exactly what the proof assumes.

**Can't:** an independent human understanding of *why* the proof works, which matters scientifically even if the proof is correct, especially if the long AI-written text stays private. It also can't certify the gap, which isn't claimed, or anything about QCD or the unified theory beyond what was formalized.

## Thread 7: what would count as failure?

### The falsifiable handle, stated plainly

An existence proof predicts no new physics. Lattice simulations already agree with Yang-Mills phenomenology and would agree just as well if the proof were wrong. This is a finding, not a gap: the claim certifies that existing physics rests on a real mathematical object, and no experiment can test it. Its handle is **mathematical checkability**, and that handle is sharp: a single unproved assumption, mismatched definition, or broken lemma defeats it. **(A) Consensus** **(broader literature)**

**Analogy:** chip tape-out signoff: automated design-rule and layout checks, then spec review, then silicon validation.

**Breaks when:** you reach the silicon step. There's no silicon here. Validation stops at spec review, so everything rides on the mechanical checks and on whether the spec is the right one.

### The tests, in the order they can be run

**Group 1: mechanical (hours, anyone with Lean)**

1. **It builds.** Pinned Lean and Mathlib versions reproduce the build; an independent kernel checker accepts it. *Fail:* not yet a formal proof. Fatal until fixed.
2. **Axiom audit.** `#print axioms` shows only the three standard axioms: no `sorry`, no custom `axiom`, no `native_decide`. *Fail:* the result is conditional. If the extra axioms are Balaban's estimates, the honest headline becomes "existence, assuming Balaban is correct." *(Threads 3, 6)*
3. **Formalized scope.** Which theorems are in Lean? Only pure Yang-Mills was formalized as of Oct 16. *Pure Yang-Mills alone is the expected outcome;* QCD and the unified theory then stay natural-language claims. *(primer §7)*

**Group 2: statement fidelity (days to weeks, specialists)**

4. **Gauge groups.** Every compact simple group, as the Clay problem asks, or only specific ones? *Partial coverage* is real but short of the Clay existence half. *(primer §7)*
5. **The full contract.** All OS axioms: reflection positivity, full rotation symmetry, clustering, both limits? *Missing rotation symmetry or clustering* means a weaker theorem. *(Threads 1, 3; primer §7)*
6. **Definitions from a reviewed library, or bespoke?** Bespoke is expected; not a fail, but it puts the full burden on human review. *(Thread 6)*
7. **Sanity theorems.** Does the release prove that a free theory satisfies "quantum field theory" but fails "Yang-Mills" or "nontrivial"? *Absence* leaves vacuity unexcluded; a free witness satisfying the main theorem would be fatal. *(Thread 6)*

**Group 3: mathematical content (weeks to months, constructive-QFT experts)**

8. **Nontriviality, explicit.** Proved, not assumed. *Fail:* a strictly easier problem was solved. *(Thread 4)*
9. **Unique limit or subsequence?** Unique infinite-volume limit with clustering? *Subsequence-only* is weaker. *(Thread 5; primer §7)*
10. **The infinite-distance consistency test.** If the method genuinely controls the theory at infinite distances, it should say something about long-range decay, the gap's territory. Then why claim no gap? Acceptable answers: the control is qualitative (enough for existence, too weak for a decay rate), or a gap result is coming. *An unclear answer* is the most important thing to press on. **(C) Speculative** **(analyst inference)**
11. **Quarks and the unified theory.** How are fermion doubling and the determinant's sign handled? Does the scalar sector stay asymptotically free? *Fail* is limited to those claims. *(Threads 4, 5)*
12. **Independent human understanding.** Do constructive-QFT experts outside the committee explain why it works? Until then the result is formally checked but not understood. *(Thread 6; primer §7)*

**Group 4: communication (immediately)**

13. **No gap claimed.** Coverage saying the Millennium Problem is solved is wrong on its face. *(primer §7)*

**(C) Speculative** for the list as a whole: a synthesis of the primer's checklist and this deep dive, not an established protocol. **(analyst inference)**

### Closing ledger

| Layer | Status | Confidence |
| :-- | :-- | :-- |
| Lattice theory well defined, gauge-exact, reflection positive | Proved | (A): textbook |
| Confinement and a gap on a coarse, strongly coupled grid | Proved | (A): convergent cluster expansion |
| Short-distance control in a finite box (Balaban) | Proved, if his papers hold | (B): accepted, but critics call parts incomplete |
| Existence of four-dimensional Yang-Mills, infinite volume | Claimed, unverified | (C): nothing released yet |
| Nontriviality | Claimed implicitly, unverified | (C): watch test 8 |
| QCD and the unified theory | Claimed, natural language only | (C): unformalized |
| Mass gap | Open, not claimed | (A): consensus that it's open |
| Confinement in the continuum | Open, not claimed | (A): consensus that it's open |

The committee expects the Lean release the week of Nov 9. Tests 1–3 can be run within hours of it.

## Companion: Lean explained

### What Lean is

Lean is a programming language in which a theorem is written as a **type** and a proof is written as a **program of that type**. Checking a proof is just type-checking that program. If it type-checks, the proof is correct, relative to the statement and the axioms; if any step is wrong, it doesn't compile. A small core called the **kernel** does that final check, and it's the only part you have to trust.

The closest relative from chip design: after the 1994 Pentium division bug, Intel hired John Harrison, who used a proof assistant in the same family (HOL Light) to formally verify the floating-point division and square-root algorithms. Lean is that idea, grown into a general tool for mathematics. **(A) Consensus** **(broader literature)**

### Why it exists

Some proofs are too long or intricate for human referees to check with confidence:

- **Kepler conjecture.** Hales's 1998 proof left referees 99% sure; he spent about a decade formalizing it, finishing in 2014.
- **Four-color theorem.** Formally verified in 2005 in Coq.
- **Liquid Tensor Experiment** (2020–22). Peter Scholze wasn't sure his own key proof was right and asked the Lean community to check it; they did, and found and fixed a gap.

**(A) Consensus** **(broader literature)** The common thread: when human checking is expensive or uncertain, move the trust onto a small, auditable checker.

### How it works, in three tiny examples

```lean
theorem two_add_two : 2 + 2 = 4 := rfl
```

The statement is the type; `rfl` is the proof: the kernel evaluates both sides and accepts.

```lean
theorem my_add_comm (a b : Nat) : a + b = b + a := by
  omega
```

`by` switches into tactic mode; `omega` *searches* for a proof and emits a term, which the kernel checks like any other.

```
Analyst-built concept diagram

  humans, tactics, automation, AI models
      |  (UNTRUSTED: may be buggy, may hallucinate)
      v
  proof term (a program)
      |
      v
  KERNEL  <- small, trusted, independently re-checkable
      |
      v
  accepted / rejected
```

*What to look at:* everything above the kernel can be wrong without harm; a buggy tactic or a hallucinating model just produces a term the kernel rejects.

**Analogy:** logic synthesis and formal equivalence checking. Synthesis tools are big and untrusted; an equivalence checker proves the netlist matches the RTL, so you trust the small checker.

**Breaks when:** you ask what checks the RTL. Equivalence checking proves "netlist matches RTL," not "RTL matches the architecture spec." Lean has the same blind spot: it proves "proof matches statement," and nothing checks the statement against what you meant. For chips the RTL has years of simulation behind it; for brand-new mathematics the statement may have nothing behind it.

### Mathlib: why the shared library matters

Mathlib is Lean's community library: a few hundred thousand formalized theorems plus the *definitions* they rest on. Its proofs aren't trusted (they're kernel-checked); its definitions are reviewed, so a theorem stated in Mathlib's vocabulary inherits that scrutiny. The Yang-Mills statement needs definitions (a quantum field theory, the OS axioms) that, as far as is known here, aren't in Mathlib, so they get no such inherited review.

### Why AI and Lean are a natural pair

Language models produce proofs that *read* convincingly whether or not they're right. Lean converts "trust the model" into "trust the kernel," and the model can iterate against the checker the way you'd iterate against a compiler. That's why "verified in Lean" is the strongest kind of claim an AI-generated proof can carry.

### Three ways a clean build can mislead

**A wrong definition:**

```lean
def MyPrime (n : Nat) : Prop := n > 1    -- wrong definition!

theorem four_is_prime : MyPrime 4 := by
  unfold MyPrime; omega                  -- compiles fine
```

**A false hypothesis (vacuity):**

```lean
theorem bogus (h : 1 = 2) : 0 = 1 := by
  omega                                  -- compiles fine
```

**A hidden gap:**

```lean
theorem hard_thing : 0 = 1 := sorry      -- compiles, with a warning

#print axioms hard_thing
-- 'hard_thing' depends on axioms: [sorryAx]
```

`sorry` says "trust me"; the build succeeds with a warning, but `#print axioms` exposes it. Declared `axiom`s work the same way, and that one command is how you'd check whether Balaban's results were proved or assumed.

### Bringing it back to Yang-Mills

| Question | Who answers it |
| :-- | :-- |
| Is every step of the proof valid? | The kernel, mechanically and definitively |
| What does the proof assume? | `#print axioms`, in seconds |
| Do the definitions mean what physicists mean? | Humans: the committee's current task |
| Is the statement the Clay problem's statement? | Humans |
| Why does the proof work? | Humans, and nobody yet |

Lean shrinks "is this 1,000-page proof correct?" down to "are these few pages of definitions and statements right, and what's in the axiom list?" That's an enormous reduction in what has to be trusted. For a brand-new formalization of quantum field theory, though, those few pages are where all the remaining difficulty lives.

## Corrections made during the deep dive

- **Thread 3, fine-tuning.** An early paraphrase (borrowed from a QED abstract) said renormalization means fine-tuning starting values, and the reduction-tree analogy described growing error terms cancelled by tuning. For pure lattice Yang-Mills, gauge symmetry forbids a gluon mass term; the only setting is the starting coupling. Corrected in place above.
- **Thread 3 → Thread 5, infinite volume.** Thread 3 tied the infinite-volume limit to the gap. More precisely, a limit can sometimes be extracted by compactness without long-distance control; what needs that control is uniqueness and clustering.
- **Thread 5 scope.** Thread 5 originally said the public claim was pure Yang-Mills only. The claim includes QCD and the simplest grand unified theory, with pure Yang-Mills as a subproblem. Corrected in place above.
- **Thread 6, Standard Model concern.** An initial flag that a "Standard Model completion" collides with triviality was narrowed after re-reading the primer: the completion is a grand unified theory on one simple group, which removes the electromagnetism problem; the open question is the scalar sector.
- **Framework version.** The deep dive was first opened under framework v3.10 and regenerated under v3.17 (plain-language budgets, visual micro-examples, tier labels); only the v3.17 material appears here.

## Sources

- 2026-10-30_primer_yang-mills-existence-mass-gap (wiki primer this deep dive builds on)
- [Proof by OpenAI of the existence of quantum Yang-Mills theory: 2nd statement by the shepherding committee](https://www.kitp.ucsb.edu/sites/default/files/2nd-Statement-About-Quantum-YangMills-Theory_Nov-3.pdf) — KITP, Nov 3, 2026
- [Shepherding committee first statement](https://www.kitp.ucsb.edu/sites/default/files/YM_working_group.pdf) — KITP, Oct 2026
- [Not Even Wrong (Woit) post on the committee's rules](https://www.math.columbia.edu/~woit/wordpress/?p=15948) — Nov 2026
- [OpenAI releases AI claims in maths, computer science](https://itbrief.co.nz/story/openai-releases-ai-claims-in-maths-computer-science) — IT Brief, Oct 2026
- [OpenAI science discoveries (timeline)](https://mezha.ua/en/news/openai-science-discoveries-316562/) — Mezha, Oct 2026
- [OpenAI withholds the physics proofs](https://xenospectrum.com/en/openai-yang-mills-kakeya-eth-release/) — XenoSpectrum, Oct 2026
- [OpenAI publishes ten mathematics claims with Lean proofs](https://dev.to/breachprotocol/openai-publishes-ten-mathematics-claims-with-lean-proofs-and-no-named-authors-5e2p) — on what a clean Lean build does not prove
- J. Dimock, [The Renormalization Group According to Balaban I–III](https://arxiv.org/abs/1108.1335) (arXiv:1108.1335, 1212.5562, 1304.0705)
- J. Dimock, [Ultraviolet stability for QED in d=3](https://arxiv.org/abs/1712.10029) (arXiv:1712.10029)
- Y. Tanimoto, [Renormalization group according to Balaban–Dimock](https://www.mat.uniroma2.it/~tanimoto/romatre250505.pdf) — seminar notes, Roma Tre, May 2025
- T. Balaban, Yang-Mills renormalization-group series, Commun. Math. Phys. (1983–89)
- K. Osterwalder and E. Seiler, gauge field theories on the lattice, Ann. Phys. (1978)
- K. Wilson, confinement of quarks, Phys. Rev. D (1974)
- A. Guth (1980); J. Fröhlich and T. Spencer (1982): phase transition in lattice electromagnetism
- M. Aizenman and H. Duminil-Copin, marginal triviality of four-dimensional phi-fourth, Ann. Math. (2021)
- D. Gross and F. Wilczek; H. D. Politzer: asymptotic freedom (1973)
- K. Gawędzki and A. Kupiainen; J. Feldman, J. Magnen, V. Rivasseau, R. Sénéor: Gross–Neveu construction (1985)
- H. B. Nielsen and M. Ninomiya, no-go theorem for lattice fermions (1981)
- M. R. Douglas, The Yang–Mills Millennium problem, Nat. Rev. Phys. 8, 86–97 (2026) — background review recommended by the committee
- [Lean](https://lean-lang.org) and [Mathlib community](https://leanprover-community.github.io)
- J. Harrison, HOL Light floating-point verification at Intel; T. Hales et al., Flyspeck (2014); G. Gonthier, four-color theorem in Coq (2005); Liquid Tensor Experiment (2020–22)
