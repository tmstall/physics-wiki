---
source: claude_export
conversation_uuid: 911cf359-9922-4b08-b867-e3889326fd74
title: "The Third Law Is Dead"
created_at: 2026-06-05T20:07:47.750922Z
updated_at: 2026-06-06T03:23:07.872062Z
tier: A
score: 225
n_messages: 4
---

# The Third Law Is Dead

## Human

Give a very detailed analysis of this paper

## Assistant

**Analyzing** — v3.4.9

Let me fetch the full paper first.

Full paper in hand. Let me now write the complete analysis.

---

**v3.4.9**

---

# 1. Punchy Title & One-Sentence Hook

## The Third Law Is Dead: Cambridge Physicists Numerically Kill a 50-Year Pillar of Black Hole Theory — Using Neural Networks

A black hole can reach absolute zero temperature in finite time from pure vacuum, no exotic matter required, and a Cambridge team just proved it with numerical general relativity powered by neural-network solvers.

---

# 2. Big-Picture Context

Black holes obey four laws that mirror the laws of classical thermodynamics almost exactly — a discovery from the early 1970s by Bardeen, Carter, and Hawking that cemented black holes as thermodynamic objects in their own right. The zeroth through second laws have held up beautifully. But the **third law** — the statement that a black hole can never reach zero surface gravity (zero temperature, zero Hawking radiation) in finite time — has always been the shakiest member of the family.

The third law matters because it protects something deep: an "extremal" black hole, one spinning or charged to its theoretical maximum, is a qualitatively different beast. It has zero surface gravity, emits no Hawking radiation, and sits at the edge of what general relativity normally permits. The third law was supposed to say that the universe conspires to keep black holes away from that edge — that you can push toward extremality but never quite get there, like asymptotically approaching absolute zero in classical thermodynamics.

For decades the law held, more or less. Then in 2022–2025, Christoph Kehle and Ryan Unger (mathematicians, not physicists by training) found that in Einstein-Maxwell theory coupled to charged matter with a very large charge-to-mass ratio, you *can* form an exactly extremal Reissner-Nordström black hole in finite time. The physics community took notice, but the skeptics noted: that required very exotic matter. Maybe the law still holds for vacuum gravity — just Einstein's equations, no matter whatsoever. Kehle and Unger conjectured the answer was no, but constructing the counterexample was orders of magnitude harder. 

This paper by Crump, Gadioux, Reall, and Santos — all at Cambridge's DAMTP — delivers that counterexample. They work in *five spacetime dimensions* because that gives them a more symmetric rotating black hole to work with, use a mathematically rigorous "characteristic gluing" construction, and employ neural networks to find the interpolating spacetime geometry. The result: **the third law is simply false, full stop, independent of any matter model**.

---

# 3. Necessary Background Crash-Course

**The Four Laws of Black Hole Mechanics.** Just like thermodynamics has four laws (zeroth through third), black holes obey a parallel set. Temperature maps to surface gravity κ (the gravitational pull at the horizon). Entropy maps to horizon area. The first law says energy is conserved. The second law says the total horizon area never decreases. The third law says you can never drive κ to zero. The analogy is not just poetic — Hawking showed black holes literally *have* temperature and *do* radiate, cementing the map as physical, not metaphorical. **Analogy: it's like discovering that CPU thermal throttling follows the same equations as a steam engine — the isomorphism is real, not coincidental.**

**Extremal Black Holes.** A black hole has two characteristic parameters: mass and spin (or charge). Push spin to its absolute maximum relative to mass and you get an "extremal" black hole — specifically a Myers-Perry (MP) black hole in 5D, the higher-dimensional cousin of the 4D Kerr black hole. At extremality, the inner and outer horizons merge, surface gravity hits zero, Hawking temperature hits zero, and the horizon becomes what mathematicians call a "degenerate" surface. **Analogy: think of pushing a spinning top to its gyroscopic stability limit — past that, physics changes qualitatively.**

**Characteristic Gluing.** The central technique here is like stitching two spacetime patches together along a null surface (a light-cone boundary). You have an "early" spacetime — say, a Schwarzschild black hole — and a "late" spacetime — an extremal MP black hole. You want to show there exists a smooth intermediate region connecting them. The gluing technique prescribes data on a null hypersurface and proves you can find smooth bridge fields. **Analogy: in chip design, this is exactly like clock domain crossing — you have two synchronous islands (Schwarzschild and extremal MP) and you need a metastable synchronizer bridge between them. The question is whether that bridge can be made smooth and causal.**

**Penrose Diagrams.** These are conformal spacetime maps that compress all of space and time onto a finite page, with light rays always traveling at 45°. They let you read off causal structure at a glance — where horizons are, what the future looks like, whether infinity is reachable. **Analogy: they're like network topology diagrams where the routing rules are built into the geometry itself.**

**Surface Gravity and Temperature.** Surface gravity κ is the proper acceleration needed to hold a stationary object at the horizon, rescaled to infinity. For Hawking radiation, temperature is proportional to κ. At extremality, κ = 0, so T = 0 — a cold, dark black hole that doesn't evaporate. **Analogy: a CPU that has hit absolute zero throttling — it still has state, still has entropy (area), but emits no thermal noise.**

**Myers-Perry Black Holes.** In five spacetime dimensions, you can have two independent rotation planes (instead of one in 4D). Setting both rotation parameters equal gives an "equal-angular-momenta" Myers-Perry black hole with enhanced symmetry group SU(2) × U(1). This cohomogeneity-1 structure reduces the problem from depending on 4 coordinates down to 2 — a massive simplification that makes the numerical problem tractable. **Analogy: like going from a general 3D stress tensor to a purely isotropic one — you lose generality but gain tractability.**

---

# 4. Core Technical Explanation

### The Setup: Why Five Dimensions?

The team works in 5D for a clean reason. The 4D target — an extremal Kerr black hole — is "cohomogeneity-4," meaning the spacetime depends on four independent coordinates. That's an unsolved numerical PDE problem of enormous difficulty. In 5D with equal rotation parameters, the Myers-Perry black hole is cohomogeneity-1, and the whole dynamical problem collapses to cohomogeneity-2 (two coordinates: the double null coordinates U and V). That's still hard, but tractable.

### The Metric Ansatz: What Geometry They're Solving For

They write down a 5D spacetime metric with SU(2) × Z₄ symmetry. The spatial slices look like a deformed 3-sphere (S³), described using Euler angles and left-invariant 1-forms of SU(2). The metric has:

- **Ω** — a conformal factor controlling the null coordinates
- **r** — an areal radius-like function measuring the "size" of the S³ slices
- **B** — a real deformation parameter measuring how squashed the S³ is away from round
- **Φ** — a complex field encoding the rotation/off-diagonal mixing
- **A** — a U(1) gauge field (arising from the geometry, not any physical matter — this is pure gravity)

The key physics lives in how B and Φ vary between V = 0 (the Schwarzschild end) and V = 1 (the extremal MP end) on the gluing null surface C.

### The Characteristic Gluing Construction

They split the problem into two types:

**Type (i):** Start with a pre-existing Schwarzschild black hole (non-rotating, non-extremal, finite temperature) at V ≤ 0. End with an extremal Myers-Perry (EMP) black hole at V ≥ 1. The gluing surface C sits at fixed U = U₀. The problem: find B and Φ on C for V ∈ (0,1) such that the spacetime is smooth across C. This directly violates the third law — a black hole that was Schwarzschild becomes extremal in finite time.

**Type (ii):** Start from flat Minkowski spacetime (no black hole at all!) at V ≤ 0. End with an EMP black hole at V ≥ 1. Gravitational waves alone collapse to form an extremal black hole. Even more radical.

For the gluing to work, the metric and its derivatives must match smoothly at V = 0 and V = 1. Each matching condition at derivative order j introduces constraints. A Cᵏ gluing means k derivative orders must match — and that produces 3k + 3 simultaneous nonlinear conditions the fields B and Φ must satisfy along the entire V ∈ [0,1] interval.

### The Hawking Mass and Angular Momentum

They define the Hawking mass mH — a quasi-local mass measured on S³ cross-sections. The equations of motion guarantee:

- mH decreases as U increases (ingoing direction): no energy escapes inward
- mH increases as V increases (outgoing direction): energy flows in from outside

This is what you'd expect physically — the system gains mass and spin as gravitational waves pile in. They also track the angular momentum J on each cross-section, which must interpolate from J = 0 (Schwarzschild has no spin) to J = J_EMP (the extremal value).

### The Neural Network Solver: The Key Innovation

Here's where it gets genuinely novel. The free data on the gluing surface — the fields B(V) and Φ(V) — need to satisfy all the matching conditions simultaneously. This is a constrained nonlinear optimization problem in function space. They parametrize B and Φ as **single hidden layer neural networks** with tanh activation functions:

$$\chi_0 + \sum_{i=1}^{p} \chi_i \tanh(\mu_i V + \kappa_i)$$

**Symbol definitions:**
- $\chi_0, \chi_i$ : network weights (real numbers, the optimization parameters)
- $\mu_i$ : frequency-like scales for each neuron
- $\kappa_i$ : phase offsets

**What this actually means:** Instead of picking a specific functional form for B and Φ (polynomials, Fourier modes, etc.), they let the neural network be the ansatz. The tanh basis is dense — it can approximate any smooth function given enough neurons. This is exactly like using a neural network as a spectral basis, but with the basis functions themselves being adaptive. Think of it as a self-organizing interpolation table that automatically concentrates resolution where the fields are most curved. **Analogy: it's like using an adaptive mesh refinement scheme where the mesh topology itself is a learnable parameter, not just the resolution.**

### Three-Stage Numerical Optimization

**Stage 1:** Random initialization → Adam gradient descent optimizer (same optimizer used in ML training). They compute gradients using a fourth-order central difference formula (more accurate than the standard two-point formula), with penalty terms to prevent r or ∂ᵤr from going negative (which would mean the gluing surface enters a white hole — physically nonsensical).

**Stage 2:** BFGS quasi-Newton method refines the solution once Adam gets close. BFGS is a workhorse second-order optimizer that approximates the Hessian without computing it explicitly. **Analogy: Adam is the coarse-grain performance sweep, BFGS is the targeted micro-optimization once you're in the right basin.**

**Stage 3:** Extended-precision quasi-Newton (Broyden's method) with a spectral-element discontinuous Galerkin (DG) method for the ODE integration. They verify convergence to residuals below 10⁻²⁰ — essentially machine precision in extended arithmetic. The DG grid clusters near V = 0 and V = 1 (Gauss-Lobatto-Chebyshev clustering), exactly where the fields need to match their boundary conditions most precisely.

### Results: What They Actually Find

**Type (i) solution (k = 2):** They find a C² solution using just 24 neural network parameters (p = 2, 2, 3 for the three fields φ, ω, β). The initial Schwarzschild horizon radius is rᵢ/r₊ ≈ 0.0009 — tiny relative to the final EMP horizon, reflecting that the black hole absorbs a huge burst of gravitational waves to spin up. B and Φ are largest at early V (near the Schwarzschild end), consistent with Raychaudhuri's equation predicting strong focusing of the null generators when the transition begins.

**Type (ii) solution (k = 4):** To get a solution that's C² all the way to r = 0 (the origin of the spacetime), they need k = 4 (a loss of two derivatives at r = 0 is generic for this type of construction). This required 87 parameters. The |Bⱼ| derivatives grow enormous at large j because ∂ᵤr|ᵥ₌₁ is very small — the solution lives dangerously close to a degenerate regime.

**Convergence verification:** The DG scheme shows the expected power-law convergence under h-refinement (scaling exponents γ ≈ 6.2 and 6.5, consistent with theory) and exponential convergence under p-refinement — both exactly what you'd expect from a well-posed problem with smooth fields. This rules out numerical artifacts; the solution is genuinely there.

---

# 5. What's Genuinely New or Clever

**Trick 1: Neural networks as a gravitational ansatz.** Nobody had previously used neural networks directly as the parametrization of the gluing data in numerical GR. The key insight is that the problem is a root-finding problem in an infinite-dimensional function space — you want to zero out 3k+3 conditions by choosing a function. Traditional approaches (spectral expansions, finite element bases) require knowing the right functional form ahead of time. The neural network ansatz is agnostic about shape and lets optimization find it. The fact that it works to residuals of 10⁻²⁰ with only 24–87 parameters is remarkable. **This technique will likely propagate into many other hard constrained-PDE problems in numerical GR.**

**Trick 2: Five-dimensional gravity as the proving ground for four-dimensional conjectures.** The move to 5D is not a cheap trick — it's a principled reduction of the symmetry group that makes a genuinely hard (cohomogeneity-4) problem tractable (cohomogeneity-2), while preserving the essential physics. The equal-angular-momenta Myers-Perry black hole is the 5D analogue of Kerr in every way that matters for the third law question. By proving violation in 5D vacuum, they establish that the third law is false in principle without any matter — and the 4D result (extremal Kerr formation) is now the logical next target with a clear roadmap.

---

# 6. Limitations & Open Questions

**The 5D vs. 4D gap.** The big one. Everything here is 5D. The 4D case (extremal Kerr black hole) remains unproven. The authors acknowledge it: the 4D case is cohomogeneity-4, meaning the problem depends on 4 independent variables instead of 2. This is not a minor extension — it's an entirely different class of numerical PDE. The neural network approach might generalize, but it's not guaranteed. Watch for a follow-up in the next 1–3 years that either delivers the 4D proof or identifies a genuine obstruction.

**No global structure away from C.** The construction proves the existence of a smooth metric on the gluing surface and in local neighborhoods, but the global structure of these spacetimes — what happens far away, whether the full maximal Cauchy development is well-behaved, whether there are additional singularities — is not analyzed. Do type (ii) solutions contain trapped surfaces? The authors flag this explicitly as open.

**Non-uniqueness.** With 24–87 parameters, solutions are not unique. There's a whole moduli space of gluing solutions, and its structure is unexplored. Are there solutions with smaller gradients? Can you construct families continuously parameterized by, say, the mass ratio rᵢ/r₊? 

**The physical scenario.** The type (i) solution has rᵢ/r₊ ≈ 0.0009 — the initial black hole is a factor of ~1000 smaller in horizon radius than the final extremal one. This means the gravitational wave pulse that spins it up must carry an enormous amount of energy and angular momentum. The astrophysical plausibility is zero — this is a mathematical existence proof, not a description of anything that forms in nature. Whether astrophysical processes can get even close to extremality (at say 99.9% of the extremal limit) in finite time remains a separate question.

**The supersymmetric exception.** Reall and McSharry proved earlier (Phys. Rev. D, 2025) that if matter satisfies a "supersymmetric lower bound" on energy in terms of charge, the third law cannot be violated. This means there's a whole class of matter models — consistent with string theory's supersymmetric sector — where the third law survives. The paper violates the *general* third law but not a suitably restricted version. That's a genuine wrinkle for those hoping the violation has deep implications for quantum gravity.

---

# 7. Three Crystallized Takeaways

1. **The third law is false.** In five-dimensional vacuum general relativity, you can form an extremal black hole — with zero temperature and zero Hawking radiation — from a non-extremal one in finite time. No exotic matter required. A 50-year pillar of black hole thermodynamics has been definitively overturned.

2. **Neural networks solved a problem classical numerical GR could not.** The team used tanh neural networks as adaptive basis functions for constrained spacetime geometry optimization, finding solutions with residuals below 10⁻²⁰ using only 24–87 parameters. This technique opens a new toolbox for numerical relativity.

3. **The 4D Kerr case remains open — and is now the most important unsolved problem in classical black hole dynamics.** The 5D proof provides the existence argument and the roadmap, but the prize — extremal Kerr formation in four-dimensional vacuum gravity — still awaits its proof.

---

# 8. Detailed Summary & Explanation

### The Physical Claim

Black holes have four laws analogous to thermodynamics. The third law says: no physical process can reduce a black hole's surface gravity (its effective temperature) to zero in a finite amount of time. An "extremal" black hole — one spinning or charged to its absolute limit — has zero surface gravity. The third law was supposed to say you can approach extremality but never reach it, just as classical thermodynamics says you can approach absolute zero but never reach it through a finite number of steps.

This paper proves that claim is wrong. In five spacetime dimensions, there exist exact solutions of the Einstein equations — no matter fields, just pure spacetime geometry — in which a non-extremal black hole becomes exactly extremal in finite time. The team proves this by constructing two types of solutions: one where a pre-existing ordinary (Schwarzschild) black hole absorbs gravitational waves and becomes extremal, and one where gravitational waves alone collapse and directly form an extremal black hole from nothing.

### Why Five Dimensions?

The natural 4D target would be an extremal Kerr black hole. But constructing that solution requires working with a spacetime that depends on four independent coordinates simultaneously — a computational problem that is, for now, out of reach. In five dimensions, a particular type of rotating black hole called the Myers-Perry black hole (with equal rotation in two independent planes) has much higher symmetry. The problem collapses to depending on just two coordinates, making it numerically tractable while preserving the essential physics of the third law violation.

### The Mathematical Strategy: Characteristic Gluing

The central technique is called "characteristic gluing." Imagine cutting spacetime in half along a surface that light travels along (a null surface). On one side, you have the early spacetime — either a Schwarzschild black hole or empty flat space. On the other side, you have the final extremal Myers-Perry black hole. The challenge: find a smooth interpolating bridge region between them. If such a bridge exists and is smooth, then the two spacetimes can be joined into a single valid solution of Einstein's equations.

This reduces to a constrained optimization problem: find functions (the fields B and Φ describing the shape of the geometry on the gluing surface) such that a specific set of matching conditions are satisfied at the two ends. The more matching conditions you impose — the smoother you want the solution to be — the harder the problem.

### The Neural Network Breakthrough

The innovation that makes the numerical solution tractable is representing the unknown fields on the gluing surface as neural networks with tanh activation functions. This is a dramatic departure from conventional numerical relativity. Rather than using polynomials or Fourier modes as basis functions, the team lets a neural network's weights be the free parameters of the optimization. The network is trained not to predict text or classify images, but to find a spacetime geometry. The objective function is the sum of squared violations of the matching conditions — drive that to zero and you have a valid solution.

They use three stages: first, standard machine learning gradient descent (the Adam optimizer) to get close to the solution from a random start; second, the BFGS quasi-Newton method to sharpen the convergence; third, an extended-precision Newton solver for the final ultra-high accuracy polish. The final solutions satisfy all conditions to residuals smaller than one part in ten to the twentieth — extraordinary numerical precision.

### What the Solutions Look Like

For the type (i) solution (Schwarzschild to extremal Myers-Perry), the initial black hole is about a thousand times smaller in horizon radius than the final extremal one. This means the gravitational wave burst that spins it up carries an enormous amount of energy. The deformation fields B and Φ are largest near the Schwarzschild end and smoothly relax to their extremal values — consistent with the Raychaudhuri equation, which governs how null surfaces focus under energy inflow.

For the type (ii) solution (flat spacetime to extremal black hole), they need higher-order smoothness (four derivative orders matched instead of two), which requires 87 neural network parameters. The fields develop very large derivatives, making this the harder numerical problem. The fact that they solve it demonstrates the approach's robustness.

### What This Means

The third law as originally stated by Bardeen, Carter, and Hawking in 1973 is definitively false. This does not mean the analogy between black holes and thermodynamics breaks down — the zeroth, first, and second laws all hold in strong forms. It means that one specific aspect of the analogy — the impossibility of reaching zero temperature — does not carry over. Extremal black holes, with their zero Hawking temperature and special horizon geometry, can form in finite time from ordinary initial conditions.

The implications for quantum gravity and black hole thermodynamics are still being worked out. Extremal black holes are heavily studied in string theory and supersymmetric contexts. The paper notes that if matter satisfies a "supersymmetric bound" (an energy condition arising from supersymmetry), the third law cannot be violated. So the violation exists in the classical vacuum sector, but may be blocked in the supersymmetric sector — a tantalizing split that may have implications for understanding extremal black holes in string theory.

---

# 9. Shorter Summary

This paper provides the first proof that the third law of black hole mechanics is false in vacuum gravity — no matter of any kind required. Working in five spacetime dimensions, Crump, Gadioux, Reall, and Santos construct exact solutions of Einstein's equations in which a non-extremal Schwarzschild black hole absorbs gravitational waves and becomes an extremal Myers-Perry black hole (zero temperature, zero Hawking radiation) in finite time, directly violating the third law.

They work in five dimensions because the rotating black hole there has higher symmetry, collapsing the problem from a four-coordinate to a two-coordinate PDE — still hard, but now numerically tractable. The key technical innovation is parametrizing the unknown interpolating spacetime geometry as **neural networks with tanh activation functions**, then optimizing the network weights to simultaneously satisfy all geometric matching conditions. Solutions are found with residuals below one part in ten to the twentieth. They solve two variants: starting from a pre-existing Schwarzschild black hole (which directly violates the third law), and starting from pure gravitational waves with no black hole at all.

The team also demonstrated the formation of an extremal black hole from collapsing gravitational waves alone, with no intermediate black hole phase. The third law as stated by Bardeen, Carter, and Hawking in 1973 — that no classical process can drive a black hole's surface gravity to zero in finite time — is simply wrong. The analogous four-dimensional result for extremal Kerr black holes in ordinary spacetime remains unproven and is now the field's primary open target.

## Human

Please do an analysis of this paper the very detailed analysis gave me lots of terms I didn't understand so please help I'm very interested in finding that really what's going on

## Assistant

od — I have everything I need. Now let me write the accessible deep-dive you're actually asking for. The goal here is: **same real physics, but built from the ground up so every concept clicks before we move to the next one.**

---

**v3.4.9**

---

# The Third Law Is Dead — What That Actually Means, and Why It's a Big Deal

## What You're Really Asking

You want to understand what this paper actually *did* — not just what the jargon labels are, but what the physicists were trying to prove, what they found, why anyone cares, and what it means for how we understand the universe. Let's build that from scratch.

---

## Start Here: Black Holes Have a Temperature

This is the weirdest true thing in all of physics, and it's the foundation of everything in this paper.

In the early 1970s, Stephen Hawking proved that black holes aren't completely black. They slowly emit radiation — now called Hawking radiation — because of quantum effects at the edge of the horizon. And radiation means *heat*, and heat means *temperature*. A black hole has a temperature just like a cup of coffee does.

But here's where it gets strange: **a black hole's temperature is inversely proportional to its mass.** The bigger the black hole, the colder it is. A stellar-mass black hole is fantastically cold — far colder than empty space. A tiny black hole would be blazing hot.

The temperature comes from something called **surface gravity** — a measure of how violently the black hole's gravity rips at the edge of the horizon. High surface gravity = high temperature. Low surface gravity = low temperature.

This led physicists to notice something uncanny: black holes seem to obey four laws that look almost *identical* to the four laws of classical thermodynamics. Not metaphorically — the mathematical equations are the same, with surface gravity playing the role of temperature and horizon area playing the role of entropy. This was discovered in 1973 by Bardeen, Carter, and Hawking in a landmark paper.

---

## The Four Laws — and Why the Third One Is the Controversial One

You know the laws of thermodynamics. Here's the black hole version side by side:

| Thermodynamics | Black Hole Mechanics |
|---|---|
| **Zeroth:** All parts of a system in equilibrium have the same temperature | **Zeroth:** Surface gravity is the same everywhere on a black hole's horizon |
| **First:** Energy is conserved | **First:** Mass, spin, and charge are related by a conservation law |
| **Second:** Entropy never decreases | **Second:** Horizon area never decreases |
| **Third:** You can never reach absolute zero temperature | **Third:** You can never reach zero surface gravity |

The first three have held up extremely well. The third is the one this paper destroys.

**What does "zero surface gravity" mean physically?** It means a black hole that is spinning or charged to its absolute theoretical maximum — what physicists call an *extremal* black hole. Think of it like a spinning top that's rotating so fast that any faster and it would fly apart. At that maximum spin, something remarkable happens: the surface gravity at the horizon goes to exactly zero. No Hawking radiation. Zero temperature. A perfectly cold, perfectly dark black hole.

The third law said: *you can get close to that limit, but you can never actually reach it in finite time.* Just like you can cool something to near absolute zero but the last tiny bit of temperature always takes infinite effort to remove.

This paper proves that's wrong. You *can* reach it. In finite time. And you don't need anything exotic to do it — just pure gravity.

---

## What Makes an "Extremal" Black Hole Special

Let's spend a moment here because this is the heart of the paper.

A normal black hole has two characteristic numbers: its **mass** and its **spin** (or its mass and its charge — the physics is similar). There's a hard limit on how much spin a black hole of a given mass can have. If you tried to give it more spin, the math says the horizon would disappear entirely, leaving a "naked singularity" — something most physicists believe the universe doesn't permit. (That's a separate principle called Cosmic Censorship.)

An **extremal black hole** sits exactly at that spin limit. It's the boundary case. Right at that edge, the inner and outer boundaries of the black hole (which are normally two distinct surfaces, like two concentric spheres) *merge into one*. Surface gravity hits zero. Temperature hits zero.

Why does this matter so much? Because:

1. An extremal black hole doesn't evaporate via Hawking radiation. It's stable essentially forever.
2. Its geometry near the horizon is qualitatively different from a normal black hole — the math becomes richer and more interesting.
3. In string theory, extremal black holes are deeply connected to supersymmetry and are used to calculate black hole entropy from first principles (the famous Strominger-Vafa calculation). They're theoretically important far beyond just this one law.
4. The third law was supposed to *protect* extremal black holes from forming — to keep them in the "unreachable" category.

The Cambridge team just showed the fence has a gate.

---

## What the Paper Actually Does

The paper constructs a specific sequence of events in spacetime — a mathematical solution to Einstein's equations — in which an ordinary black hole is transformed into an extremal one in a finite amount of time. No exotic matter. No tricks. Just pure gravity doing what gravity does.

They do this in **five spacetime dimensions** rather than our usual four. I'll explain why in a moment, but don't let that distract you — the physics of the third law is the same in 5D, and proving it in 5D definitively kills the law in general.

### The "Movie" of What Happens

Think of it as a three-act film:

**Act 1 (early times):** A small, non-rotating Schwarzschild black hole sits in space. It has a definite temperature, emits Hawking radiation, perfectly normal. Think of it as a cold but not frozen engine — running, dissipating heat.

**Intermission:** A huge burst of gravitational waves — ripples in spacetime itself, no matter involved — slams into the black hole. These waves carry both energy and angular momentum (spin). The black hole absorbs them, gets heavier and starts spinning.

**Act 3 (late times):** The black hole has absorbed enough angular momentum that it hits the extremal limit exactly. Surface gravity = 0. Temperature = 0. The transformation is complete. Finite time has elapsed.

In a second version of the movie, Act 1 doesn't even have a black hole — just gravitational waves collapsing from empty space directly into an extremal black hole. No intermediate ordinary black hole at all.

Both movies are valid, smooth, exact solutions to Einstein's equations.

### Why Five Dimensions?

Here's the honest reason: it's a mathematical shortcut that preserves the essential physics.

In our normal 4D spacetime, constructing this solution would require solving equations that depend on four independent variables simultaneously. That's an extremely hard computational problem — essentially unsolved with current techniques.

In five dimensions, if you set up the rotating black hole just right (with equal spin in two perpendicular planes — the Myers-Perry black hole), the symmetry is so high that the problem collapses to depending on only *two* variables. That's still hard, but tractable.

The logic is: if the third law can be violated in 5D vacuum gravity, then the statement "the third law holds in vacuum gravity" is false. Full stop. The 5D proof kills the 4D claim just as surely as finding *one* counterexample kills *any* universal claim. The specific question of whether the same thing happens in 4D (with an extremal Kerr black hole) is still open, but it's now widely expected to be true.

---

## The Technical Trick: Characteristic Gluing

The method they use to construct the solution is called **characteristic gluing**, and it's elegant once you see what it's doing.

Imagine you want to prove that two cities can be connected by a road, but you don't want to actually build the whole road — you just want to prove one exists. One approach: show that a road leaving city A heading toward city B can always be made smooth, and a road leaving city B heading toward city A can always be made smooth, and that somewhere in the middle they *must* meet.

That's essentially what characteristic gluing does in spacetime. They split the problem into:

- A "past" region: exactly the Schwarzschild (ordinary) black hole spacetime. Well-known, perfectly described by existing solutions.
- A "future" region: exactly the extremal Myers-Perry black hole spacetime. Also well-known.
- A "bridge" region in between: this is what they have to find.

The bridge lives along a null surface — a surface that light rays travel along, the spacetime equivalent of a cliff face angled at 45°. On this surface, they have to find two field functions (called B and Φ in the paper) that smoothly interpolate between the past and future regions. The conditions they have to satisfy are: the geometry must match to the Schwarzschild values on one end, match to the extremal MP values on the other end, and match at every derivative order in between (so the spacetime doesn't have any "kinks" or "sharp corners").

This is a constrained optimization problem. They have to find two functions of one variable that simultaneously satisfy a long list of conditions. It's like finding the profile of a mountain pass that smoothly connects two peaks at different heights — no cliffs, no overhangs — while satisfying a specific set of slope constraints at both endpoints.

---

## The Neural Network Solver — What It's Really Doing

This is where the paper does something genuinely novel, and it's worth understanding what it actually means.

They represent the unknown functions B and Φ as **neural networks** — specifically, single-layer networks with tanh activation functions. But this is not AI in the sense of ChatGPT or image generation. Think of it this way:

A neural network with tanh activations is mathematically just a sum of S-shaped curves:

$$f(V) = c_0 + c_1 \tanh(a_1 V + b_1) + c_2 \tanh(a_2 V + b_2) + \ldots$$

**Symbol definitions:**
- $V$ : the coordinate along the gluing surface (runs from 0 to 1, 0 = Schwarzschild end, 1 = extremal end)
- $c_0, c_1, c_2$ : heights/amplitudes of each curve
- $a_1, a_2$ : how steep each S-curve is
- $b_1, b_2$ : where each S-curve is centered

**What this actually means:** A single tanh curve looks like a smooth step function — flat at both ends, smooth S-shaped transition in the middle. A sum of them can approximate almost any smooth curve with enough terms. It's like a Fourier series, but instead of sine and cosine waves, you're using S-shaped curves. The magic is that the *shape* of each S-curve adjusts automatically during optimization, concentrating resolution wherever the function changes most rapidly.

Compare this to the usual approach (polynomial or Fourier basis): those bases have fixed shapes, and you just tune the coefficients. The neural network basis has *adaptive* shapes — both the shapes and the coefficients are optimized. Think of it as the difference between a fixed-size pixel grid (traditional) versus a vector image that puts more detail exactly where detail is needed (neural network).

They train this network not on data, but on the constraint violations — how far the current functions are from satisfying all the matching conditions. Drive all constraint violations to zero, and you have a valid spacetime.

The three-stage optimization they use:
1. **Adam optimizer** (same one used to train LLMs): rapid rough approach to the solution region
2. **BFGS quasi-Newton**: precision refinement once close
3. **Extended-precision Newton solver**: final polish to 10⁻²⁰ precision — essentially perfect

The fact that they found solutions with only 24–87 total parameters is remarkable. The whole bridge between Schwarzschild and extremal black hole spacetime, encoded in a few dozen numbers.

---

## Why This Is Genuinely Shocking

For 50 years, the third law was part of the bedrock. Even after Kehle and Unger found violations involving charged matter (2022-2025), it was possible to argue "well, that's because they used exotic matter with unrealistic charge-to-mass ratios." The fallback position was: pure vacuum gravity, no matter at all — *surely* the third law holds there.

This paper removes that fallback. Pure vacuum. No matter. The law is violated.

The implications ripple outward:

**For black hole thermodynamics:** The analogy between black holes and thermodynamics is still remarkably good — three of the four laws hold. But the third law analogy is now broken in a deep way. In real thermodynamics, absolute zero is unreachable for fundamental reasons tied to entropy and quantum statistics. In black hole mechanics, "absolute zero" (extremality) *is* reachable. The analogy was always a map, not the territory — and this is where the map fails.

**For Hawking radiation and black hole evaporation:** If you can form an extremal black hole in finite time, it stops radiating. It becomes a stable cold remnant. Whether this matters observationally is another question — astrophysical black holes are nowhere near extremal — but theoretically, it means there's a new class of stable endpoint for black hole evolution.

**For the cosmic censorship conjecture:** Extremal black holes sit right at the boundary of what's allowed. Forming one in finite time from vacuum tests the limits of cosmic censorship (the conjecture that singularities are always hidden inside horizons). The team's solutions don't obviously violate it, but they probe exactly the dangerous regime.

**For string theory:** Extremal black holes are used as exact calculable objects in string theory, precisely because they were supposed to be unreachable from generic initial conditions. If they can form dynamically from pure gravity, their role in the theory may need reexamination.

---

## The One Remaining Uncertainty

Everything in this paper is 5D. The team explicitly says their next target is 4D — constructing an extremal Kerr black hole in our four-dimensional universe from pure gravitational waves.

The expectation in the community is that this will work. But the computational difficulty is enormous — the 4D problem depends on four independent variables instead of two, and no one has solved it yet. The neural network approach the team developed here is their best tool for attacking it.

When the 4D proof arrives — and it likely will — the third law's death certificate will be complete.

---

## The Three-Sentence Version

1. A 50-year-old rule said black holes can never reach absolute zero temperature — no matter what, it would take infinite time. This paper constructs explicit mathematical solutions to Einstein's equations showing it can happen in finite time, using only gravity and no matter whatsoever.

2. They pulled it off by parametrizing the unknown intermediate spacetime geometry as neural networks and optimizing them to satisfy exact matching conditions — a genuinely new technique in numerical general relativity.

3. The result is the strongest possible counterexample: pure vacuum, five-dimensional spacetime, mathematically rigorous — and the analogous four-dimensional proof, for Kerr black holes in our own universe, is now the field's primary open target.
