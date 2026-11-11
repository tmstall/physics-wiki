---
type: primer (not a paper analysis)
title: Lean and formal proof verification
date: 2026-11-07
source: Deep-dive companion to 2026-10-30_primer_yang-mills-existence-mass-gap (Yang-Mills deep dive, Thread 6 follow-up)
framework: Academic Paper Analysis Framework v3.17 calibration (plain-language budgets)
status: general explainer; applies to the OpenAI Yang-Mills claim, whose Lean proof is unreleased as of 2026-11-07
suggested_pages: concepts/lean-proof-assistant, concepts/formal-verification, concepts/statement-fidelity, concepts/mathlib
---

# Lean and formal proof verification

*What Lean is, why mathematicians use it, how it checks a proof, what a clean build does and does not certify, and why that matters for an AI-generated proof of Yang-Mills existence.*

## Contents

1. [What Lean is](#1-what-lean-is)
2. [Why it exists](#2-why-it-exists)
3. [How it works, in three tiny examples](#3-how-it-works-in-three-tiny-examples)
4. [Mathlib: why the shared library matters](#4-mathlib-why-the-shared-library-matters)
5. [Why AI and Lean are a natural pair](#5-why-ai-and-lean-are-a-natural-pair)
6. [What Lean does not do: three ways a clean build can mislead](#6-what-lean-does-not-do-three-ways-a-clean-build-can-mislead)
7. [Bringing it back to Yang-Mills](#7-bringing-it-back-to-yang-mills)
8. [Sources](#sources)

## 1. What Lean is

Lean is a programming language in which a theorem is written as a **type** and a proof is written as a **program of that type**. Checking a proof is just type-checking that program.

If the program type-checks, the proof is correct, relative to the statement and the axioms. If any step is wrong, it doesn't compile. There's no "mostly right." A small core called the **kernel** does that final check, and the kernel is the only part you have to trust.

The closest relative from chip design: after the 1994 Pentium division bug, Intel hired John Harrison, who used a proof assistant in the same family (HOL Light) to formally verify the floating-point division and square-root algorithms. Lean is that idea, grown into a general tool for mathematics. **(A) Consensus:** this is documented history. **(broader literature)**

## 2. Why it exists

Some proofs are too long or too intricate for human referees to check with confidence:

- **Kepler conjecture** (densest packing of spheres). Hales's 1998 proof left the referees saying they were 99% sure. He spent about a decade formalizing it in proof assistants, finishing in 2014, to get to 100%.
- **Four-color theorem.** Formally verified in 2005 in another proof assistant (Coq), ending decades of unease about its computer-assisted proof.
- **Liquid Tensor Experiment** (2020–22). Peter Scholze, a Fields medalist, wasn't sure his own key proof was right and asked the Lean community to check it. They did, and found and fixed a gap along the way.

**(A) Consensus:** all three are standard landmarks. **(broader literature)**

The common thread: when human checking is expensive or uncertain, move the trust onto a small, auditable checker.

## 3. How it works, in three tiny examples

**A proof by computation:**

```lean
theorem two_add_two : 2 + 2 = 4 := rfl
```

The statement `2 + 2 = 4` is the type. `rfl` ("reflexivity") is the proof: the kernel evaluates both sides, sees the same number, and accepts.

**A proof using a tactic:**

```lean
theorem my_add_comm (a b : Nat) : a + b = b + a := by
  omega
```

`by` switches into tactic mode. `omega` is an automated procedure for linear arithmetic. It *searches* for a proof and emits a proof term. The kernel then checks that term like any other.

**The architecture that matters:**

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

*What to look at:* everything above the kernel can be wrong without harm. A buggy tactic, or an AI model inventing nonsense, just produces a term the kernel rejects.

**Analogy:** logic synthesis and formal equivalence checking. Synthesis tools are big, clever, and untrusted. An equivalence checker proves the gate-level netlist matches the RTL, so you trust the small checker instead of the large tool.

**Breaks when:** you ask what checks the RTL. Equivalence checking only proves "netlist matches RTL." If the RTL is wrong against the architecture spec, the check passes anyway. Lean has exactly the same blind spot: it proves "proof matches statement," and nothing checks the statement against what you meant. For chips the RTL has years of simulation behind it. For brand-new mathematics, the statement may have nothing behind it at all.

## 4. Mathlib: why the shared library matters

Mathlib is Lean's community library: a few hundred thousand formalized theorems, plus the *definitions* they rest on (real numbers, measure, Hilbert spaces, groups). It matters in two ways:

- **Proofs aren't trusted.** Mathlib's proofs are kernel-checked like everything else.
- **Definitions are reviewed.** Many people have used and argued over what "measurable" or "compact" means in Mathlib. When a theorem is stated in Mathlib's vocabulary, its meaning inherits that scrutiny.

That's the crux for Yang-Mills. The statement needs definitions (a quantum field theory, the Osterwalder–Schrader axioms) that, as far as is known here, aren't in Mathlib, so their meaning gets no such inherited review. **(B) Contested:** this picture of Mathlib and adjacent physics libraries may be out of date; check what the release imports. **(analyst inference)**

## 5. Why AI and Lean are a natural pair

Language models produce proofs that *read* convincingly whether or not they're right. Lean converts "trust the model" into "trust the kernel." The model can also iterate against the checker: try a step, read the error, fix it, repeat, the way you'd iterate against a compiler. That's why OpenAI formalizes its results, and why "verified in Lean" is the strongest kind of claim an AI-generated proof can carry.

## 6. What Lean does not do: three ways a clean build can mislead

**1. A wrong definition:**

```lean
def MyPrime (n : Nat) : Prop := n > 1    -- wrong definition!

theorem four_is_prime : MyPrime 4 := by
  unfold MyPrime; omega                  -- compiles fine
```

The proof is flawless; the definition is nonsense. This is the statement-fidelity problem in miniature.

**2. A false hypothesis (vacuity):**

```lean
theorem bogus (h : 1 = 2) : 0 = 1 := by
  omega                                  -- compiles fine
```

From a false assumption, anything follows. A theorem whose hypotheses can never be met proves nothing, yet it builds cleanly.

**3. A hidden gap:**

```lean
theorem hard_thing : 0 = 1 := sorry      -- compiles, with a warning

#print axioms hard_thing
-- 'hard_thing' depends on axioms: [sorryAx]
```

`sorry` is a placeholder that says "trust me." The build succeeds with only a warning, but `#print axioms` exposes it. Declared `axiom`s work the same way, and that one command is how you'd check whether Balaban's results were proved or assumed in the Yang-Mills formalization.

## 7. Bringing it back to Yang-Mills

| Question | Who answers it |
| :-- | :-- |
| Is every step of the proof valid? | The kernel, mechanically and definitively |
| What does the proof assume? | `#print axioms`, in seconds |
| Do the definitions mean what physicists mean? | Humans: the shepherding committee's current task |
| Is the statement the Clay problem's statement? | Humans |
| Why does the proof work? | Humans, and nobody yet |

So Lean shrinks the question "is this 1,000-page proof correct?" down to "are these few pages of definitions and statements right, and what's in the axiom list?" That's an enormous reduction in what has to be trusted. For a brand-new formalization of quantum field theory, though, those few pages are where all the remaining difficulty lives.

> [!NOTE]
> **Status as of Nov 7, 2026:** the committee's Nov 3 statement says it is checking that the Lean definitions and problem statements match the standard ones, and hopes to release the Lean proof the week of Nov 9 with a day's notice. The release checklist (Groups 1–4: mechanical, statement fidelity, mathematical content, communication) is in the Yang-Mills deep dive, Thread 7.

## Sources

- [Lean](https://lean-lang.org) — the Lean language and theorem prover
- [Mathlib community](https://leanprover-community.github.io) — Lean's community mathematics library
- J. Harrison, formal verification of floating-point algorithms at Intel with HOL Light (post-1994)
- T. Hales et al., Flyspeck project, formal proof of the Kepler conjecture (completed 2014)
- G. Gonthier, formal proof of the four-color theorem in Coq (2005)
- Liquid Tensor Experiment, Lean formalization of Clausen–Scholze condensed mathematics (2020–22)
- [Proof by OpenAI of the existence of quantum Yang-Mills theory: 2nd statement by the shepherding committee](https://www.kitp.ucsb.edu/sites/default/files/2nd-Statement-About-Quantum-YangMills-Theory_Nov-3.pdf) — KITP, Nov 3, 2026
- Related wiki page: 2026-10-30_primer_yang-mills-existence-mass-gap
