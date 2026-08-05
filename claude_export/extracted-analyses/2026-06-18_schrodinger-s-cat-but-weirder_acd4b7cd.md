---
source: claude_export
conversation_uuid: acd4b7cd-2422-45cd-aaf3-35a885c3ff59
title: "Schrödinger's Cat, But Weirder"
created_at: 2026-06-18T17:56:51.960805Z
updated_at: 2026-06-19T00:39:52.495708Z
tier: A
score: 264
n_messages: 10
---

# Schrödinger's Cat, But Weirder

## Human

Analyze this paper

## Assistant

v3.6.3

---

# 1. Schrödinger's Cat, But Weirder: Making Superpositions Out of Already-Exotic Quantum States

**The Oxford team didn't just put a quantum oscillator in two places at once — they put it in a superposition of two *already deeply weird, non-classical* states, each of which individually has no classical analogue, and then showed they can pick any combination they want.**

---

## 2. Big-Picture Context

The quantum harmonic oscillator — think of a pendulum, a vibrating ion, a mode of light — is the workhorse of quantum physics. Unlike a qubit, which only has two levels (up/down, 0/1), the oscillator has infinitely many rungs on its energy ladder. That infinite-dimensional Hilbert space is enormously powerful: you can encode quantum information in patterns of these rungs, protect it with error-correcting codes, and run computations that qubits alone can't efficiently handle. This is the whole premise of *continuous-variable quantum computing*.

For decades, the go-to "exotic" oscillator state has been the *coherent state* — the quantum state that most closely mimics a classical oscillating object, like a laser beam or a gently rocking pendulum. Superpositions of coherent states are called *cat states* (Schrödinger's famous analogy: the cat is in a superposition of alive and dead), and they've been the workhorses of quantum optics experiments. The next step up is the *squeezed state*, which trades uncertainty in one quadrature (say, position) for reduced uncertainty in the other (momentum), beating the standard quantum limit. Squeezed states are already non-classical — they can't be described by classical probability distributions — but superpositions of squeezed states were purely theoretical.

This paper goes further. The Oxford group doesn't just make a superposition of two squeezed states. They introduce *trisqueezed* (third-order) and *quadsqueezed* (fourth-order) states — non-Gaussian deformations of the vacuum with three- and four-fold rotational symmetry in phase space — and then create *superpositions* of these. None of these combined states existed in a lab before this paper.

**Prior Belief Check:** This result is genuinely surprising to experts, not just to a general audience. The experimental barrier wasn't conceptual — theorists knew these states were desirable — it was that the required *nonlinear spin-dependent interactions* were too weak in most platforms to reliably generate higher-order squeezing, let alone in the middle of a coherent superposition protocol. The Oxford group's own 2024 companion paper (Băzăvan et al., arXiv:2403.05471) first demonstrated strong trisqueezing and quadsqueezing at all; this paper then immediately exploits those tools to build superpositions. The field broadly sees this as a substantial leap, not an incremental step.

**Replication & Convergence Note:** This result comes from a single group at Oxford with no independent replication yet reported. Independent confirmation would require a separate lab demonstrating the same nonlinear spin-dependent interaction toolkit and then reconstructing Wigner functions showing negativity in superpositions of trisqueezed or quadsqueezed states. Given the technical difficulty of the platform, replication may take 2–4 years.

---

## 3. Necessary Background Crash-Course

**The Quantum Harmonic Oscillator (QHO)**
A pendulum swinging forever, no friction, quantized into discrete energy rungs called *Fock states* (0 phonons, 1 phonon, 2 phonons…). Most real experiments start the oscillator in its ground state — the lowest rung, the vacuum. The QHO matters because every bosonic field mode, every vibrational mode of a trapped ion, every microwave resonator in a superconducting chip is mathematically identical to it.

**Squeezed States**
In quantum mechanics, position and momentum can't both be sharp simultaneously (Heisenberg). A coherent state splits the uncertainty equally between them — a circular blob in phase space. A *squeezed state* squishes that blob into an ellipse: one direction gets sharper at the cost of making the other fuzzier. Think of a ball of clay that you flatten in one direction — same volume, different shape.

*Breaks when:* you push this to ask about the "shape" in 3D space. The squeezing lives in *phase space* (position vs. momentum axes), not in real physical space. Squeezing a motional state doesn't mean the ion's wavefunction is literally squeezed spatially — it means the probability distribution over its possible momenta and positions has been reshaped.

**Trisqueezed and Quadsqueezed States**
Standard squeezing uses a second-order interaction (two-phonon, k=2), producing a Gaussian-shaped phase-space distribution. *Trisqueezing* (k=3) uses a three-phonon interaction and produces a three-pointed star shape in phase space. *Quadsqueezing* (k=4) produces a four-pointed shape. These states are *non-Gaussian* — they can't be described by any bell-curve-shaped probability distribution — and they're deeply non-classical.

Analogy: standard squeezing is like pressing clay into an ellipse with two opposing thumbs. Trisqueezing is like pressing it with three equally-spaced thumbs simultaneously, creating a three-lobed shape. Quadsqueezing uses four thumbs.

*Breaks when:* you try to picture the "thumbs" as physical forces. The k-fold interaction isn't k separate pushes in sequence — it's a single quantum interaction with k-fold symmetry, applied all at once. The sequencing analogy doesn't capture the coherence requirement.

**Wigner Function**
A quasi-probability distribution over phase space: it's the closest thing to a classical probability distribution for a quantum state, but it's allowed to go *negative*. Negative regions in the Wigner function are a smoking gun for non-classicality — no classical state can have them. Think of it as a topographic map of the quantum state, where valleys below sea level mean "this state cannot be explained classically."

*Breaks when:* you treat the Wigner function as a true probability. You can't interpret a negative value as a negative probability for any physical measurement outcome. It's a mathematical tool, not a literal distribution.

**Mid-Circuit Measurement**
Normally, measuring a quantum system destroys its superposition. A *mid-circuit measurement* reads out only the ancilla (here, the ion's spin) while leaving the oscillator (the ion's motion) untouched — provided the measurement is designed to not scatter photons when the spin is in the "desired" state. It's like checking whether a coin is heads or tails by looking at its shadow, without touching the coin itself.

*Breaks when:* you assume this works perfectly. In this experiment, the non-destructive measurement only works when the spin is detected in the dark state (|1_s⟩). If photons scatter, motion is disturbed. The protocol is designed so that the *desired* output always corresponds to the dark-state outcome.

**Central analogy for this paper:** *spin as a programmable filter for oscillator states*

---

## 4. Core Technical Explanation

**The Key Idea**

The experiment uses a single trapped strontium-88 ion ($^{88}$Sr$^+$) in a Paul trap. The ion has two useful degrees of freedom: its *motion* along the trap axis (the QHO, vibrating at 1.2 MHz) and its *internal electronic levels* (the spin). The trick is to use the spin as a programmable switch that controls what happens to the motion.

**Step 1: Build the Spin-Dependent Nonlinear Interaction**

They drive the interaction

$$\hat{H}_k = \frac{\hbar\Omega_k}{2}\hat{\sigma}_z(\hat{a}^k e^{-i\phi} + (\hat{a}^\dagger)^k e^{i\phi})$$

Symbol definitions:
- $\hat{H}_k$ : the Hamiltonian (energy operator) for the k-th order squeezing interaction
- $\hbar$ : reduced Planck's constant (units of energy × time)
- $\Omega_k$ : coupling strength — how fast the interaction drives the oscillator
- $\hat{\sigma}_z$ : spin Pauli operator, equals +1 when spin is |1_s⟩, equals −1 when spin is |0_s⟩
- $\hat{a}^k$ : annihilation operator raised to the k-th power — removes k phonons at once
- $(\hat{a}^\dagger)^k$ : creation operator raised to k-th power — adds k phonons at once
- $\phi$ : phase angle, sets the orientation of the squeezing axis in phase space
- $k$ : order of the interaction; k=2 is squeezing, k=3 is trisqueezing, k=4 is quadsqueezing

What this actually means: the spin controls the *sign* of the kick. When the spin is up (+1), the oscillator gets pushed one way; when the spin is down (−1), it gets pushed the other. This sign-conditional pushing is what lets them create a superposition of two states squeezed in opposite directions — by first putting the spin in a superposition of up and down, then applying the push.

**Step 2: Create the Superposition via the Quantum Circuit**

The sequence works as follows:
- Initialize: oscillator in near-ground state, spin in |0_s⟩
- Apply a π/2 spin rotation: puts spin in (|0_s⟩ + |1_s⟩)/√2 — now the spin is in superposition
- Apply the nonlinear interaction: the oscillator entangles with the spin — spin-up evolves to |ζ_k⟩, spin-down to |−ζ_k⟩
- Apply another π/2 spin rotation: maps the entangled state into a form where even and odd superpositions of the oscillator are correlated with specific spin states
- Perform mid-circuit measurement of the spin: collapses the spin while leaving the oscillator in the desired superposition, heralded by which spin outcome was detected

This is elegant: the measurement isn't a bug (decoherence) — it's the feature. It's used *deliberately* to disentangle the spin from the oscillator while projecting the oscillator into the target state.

**Step 3: Generalize to Arbitrary Superpositions**

To create the most general superposition a|ζ_k⟩ + b|ζ_{k'}⟩, where a, b, ζ_k, and ζ_{k'} are all independent complex numbers, the team extends the spin to a *qutrit* — a three-level system using two ground states and one excited state of the strontium ion. They use one level as a "hiding spot": after creating the first constituent state, they shuffle it into the auxiliary level |2_s⟩ where it's protected from the second nonlinear interaction. They then build the second constituent independently, before combining them and measuring.

This is the "arbitrary" in the title — full independent control over amplitude, phase, and squeezing order for each constituent.

**Step 4: Verify with Wigner Tomography**

They reconstruct the full Wigner function via *characteristic function* measurements. They apply a spin-dependent displacement to the oscillator and read out the spin — scanning over the complex displacement parameter β samples the full phase-space distribution. A Fourier transform converts the characteristic function to the Wigner function. Negative regions confirm non-classicality.

---

**Assumption Audit**

**Watch:** Reader likely assumes the "superposition" here is like a qubit superposition — two clean discrete options with well-defined amplitudes. The paper actually creates superpositions of continuous-variable states, where each constituent is itself an extended object in phase space, with its own internal structure (lobes, interference fringes, rotational symmetry). The "amplitude" a and b control the *weighting* between these extended objects, not between two point-like states.

**Watch:** Reader likely assumes Wigner negativity just confirms "quantum weirdness" in a qualitative sense. The paper actually quantifies this using *Wigner logarithmic negativity (WLN)* as a resource measure, and directly compares the WLN of the new states against benchmark states (Fock states, cat states) at the same mean phonon number. The superpositions created in this work exhibit larger WLN than Fock or cat states at fixed average phonon occupation — this is a quantitative claim that these states are *more* useful for quantum computation than the previous best experimental alternatives.

**Watch:** Reader likely assumes the mid-circuit measurement is what makes this probabilistic — i.e., the probabilism is purely a measurement artifact. The paper actually reveals something subtler: the probability of getting the even vs. odd superposition depends on the *overlap* between |ζ_k⟩ and |−ζ_k⟩, which is set by the squeezing magnitude. At weak squeezing, the two states nearly overlap, so the odd superposition is almost impossible to generate. Only at large squeezing do both outcomes become equally likely. The probabilism is a physical feature of the state structure, not just measurement noise.

---

## 5. What's Genuinely New or Clever

**1. Measurement-as-a-tool for superposition generation**

The central insight is using *mid-circuit measurement as a constructive element*, not just a readout. Previous experiments either built oscillator superpositions from the outside (coupling a resonator to multiple drives) or relied on carefully engineered dissipation. Here, the measurement actively disentangles the spin from the motion in a way that *projects* the oscillator into the desired target state — and because the desired state is always correlated with the non-photon-scattering outcome, the measurement is non-destructive. This is clever and generalizable: the same trick works for any platform with a spin-coupled oscillator.

**2. Concatenation and the "hiding" trick**

The use of a qutrit "hiding" level to protect a partially built state from a subsequent nonlinear interaction, enabling sequential construction of superposition constituents, is a genuinely new protocol element. It converts a one-shot entanglement scheme into a composable, modular circuit where each component of the superposition can be built and tuned independently. This is the key to "arbitrary" — it scales to more complex superpositions in a way that two-level schemes cannot.

---

## 6. Limitations & Open Questions

**1. Single ion, single mode — no scaling demonstrated.**
Everything here happens with one $^{88}$Sr$^+$ ion and one motional mode. Continuous-variable quantum computation and metrological applications ultimately need multi-mode entanglement. (A) Consensus — this is the standard next-step critique in trapped-ion QHO work, universally acknowledged. (paper §discussion, broader literature)

**2. Probabilistic generation with no post-failure recovery.**
Independent control over probability amplitudes is demonstrated, but the protocol is *heralded* — you get the desired state only when the mid-circuit measurement gives the right outcome. At low squeezing, the success probability can be small. There is no adaptive feedback demonstrated to deterministically recover or retry. (B) Contested — some would argue heralded generation is acceptable in the NISQ era; others require deterministic preparation for fault-tolerant applications. (analyst inference + broader literature)

**3. Thermal initial state and heating rate.**
The oscillator starts not in a pure vacuum but in a near-ground thermal state with average occupation n̄ = 0.1, and the coherence time is limited by a heating rate of 300 quanta/second. For the short sequences here, this is manageable, but for deeper circuits building more complex superpositions, thermal noise and heating will degrade fidelity. (A) Consensus — acknowledged in the paper; standard limitation of room-temperature Paul traps. (paper §experiment)

**4. Quadsqueezing fidelity is notably lower.**
The quadsqueezed superpositions show larger discrepancies between experimental and simulated Wigner functions compared to the squeezed case. The fourth-order interaction requires higher-order control over two non-commuting spin-dependent forces, and errors compound. (B) Contested — whether this is a fundamental limitation of the method or an engineering problem solvable with better pulse calibration is unclear. (analyst inference)

**5. No demonstrated entanglement between two oscillators.**
The method is described as general — applicable to any spin-oscillator system — but the paper doesn't demonstrate two-oscillator entanglement, which is needed for most quantum computing and sensing applications beyond single-mode. (C) Speculative — I am extrapolating from the architecture; the authors acknowledge generality but don't claim multi-oscillator results. (analyst inference)

---

## 7. Detailed Summary & Explanation

The Oxford group starts with a theoretical landscape that's been well-mapped for decades: we know that superpositions of nonclassical oscillator states are powerful resources for quantum computing, sensing, and error correction. The problem wasn't imagination — it was engineering. You need strong, controllable, *nonlinear* interactions between the oscillator and some ancilla, and you need to measure the ancilla without disturbing the oscillator. Both of those were hard.

Their solution exploits a trapped ion's dual nature: the ion's *motion* is the oscillator (a 1.2 MHz vibration along the trap axis), and the ion's *internal electronic levels* are the ancilla spin. The key nonlinear interaction — the spin-dependent k-phonon drive — was demonstrated in a companion paper (Băzăvan et al. 2024). This paper takes that tool and builds a complete state-generation protocol on top of it.

The core quantum circuit is beautifully simple in structure: (1) put the spin in superposition; (2) apply the nonlinear spin-dependent interaction, which entangles spin with oscillator; (3) rotate the spin again to map the entangled state into a form where even/odd oscillator superpositions are correlated with distinct spin outcomes; (4) measure the spin non-destructively. The spin measurement projects the oscillator into the target superposition and simultaneously *disentangles* the spin, leaving the oscillator free for further use or tomography.

The generalization to arbitrary superpositions uses a three-level spin (qutrit). One electronic level acts as a "parking lot" — the first oscillator constituent is built, then tucked into the auxiliary level while the second constituent is built independently. They then recombine. This gives full independent control over four complex parameters: the amplitude of each constituent, its squeezing magnitude, its squeezing axis orientation, and its order (k=2, 3, or 4).

They demonstrate all of this experimentally and verify it through full Wigner function tomography — measuring the characteristic function of the oscillator state by scanning a spin-dependent displacement over the phase-space grid. The reconstructed Wigner functions show clear negative regions, confirming the non-classical character. The match between experimental Wigner functions and numerical simulations using independently measured parameters is excellent for squeezed and trisqueezed cases, and good (with expected degradation) for quadsqueezed.

Crucially, the team quantifies not just "it's quantum" but "it's more quantum than the alternatives." Their states outperform Fock states and cat states on Wigner logarithmic negativity at equivalent phonon cost — a direct measure of resource advantage for continuous-variable quantum computing.

**Why the summary is framed this way:** The central interpretive choice here is to foreground the *measurement-as-construction* insight over the specific states demonstrated. The trisqueezed and quadsqueezed superpositions are the flashy experimental results, but the architectural innovation — using heralded mid-circuit measurement modularly, with qutrit parking — is the methodological contribution that will generalize to other platforms and more complex states. That's what will matter in five years.

**Where I'm least confident in this analysis:** The quantitative comparison of Wigner logarithmic negativity between the new states and Fock/cat states (Section 5 above). The paper presents this comparison, and I've reported it accurately, but the *meaning* of WLN as a resource measure for *practical* quantum computational advantage (versus theoretical advantage) is an active research question. I may be slightly over-interpreting the WLN comparison as a definitive practical benchmark when it may be more of a theoretical resource-theoretic statement.

---

## 8. Three Crystallized Takeaways

1. **They made Schrödinger's cat states, but each "dead" and "alive" branch is itself a deeply exotic quantum state — not a simple coherent state.** This is qualitatively new: the building blocks are already non-classical, and superposing them creates states with more quantum weirdness (Wigner negativity) than anything previously built in a lab at comparable cost.

2. **The key trick is using measurement as a constructive element, not just a readout.** By carefully designing the circuit so that the desired oscillator state is always correlated with the non-photon-scattering spin outcome, the mid-circuit measurement disentangles the spin from the oscillator without disturbing it — turning a potential source of decoherence into the mechanism of state synthesis.

3. **The platform is a blueprint, not just a result.** The protocol works for any spin-coupled oscillator — trapped ions, superconducting qubits coupled to microwave cavities, optomechanical systems. What Oxford demonstrated here isn't just new states; it's a new general method for building the most quantum-resource-rich oscillator states currently known.

---

## 9. Shorter Summary (≤350 words)

A quantum harmonic oscillator — the universal model for vibrating things, from ion motion to light modes — can exist in "superposition states" where it occupies multiple distinct quantum configurations at once. For decades, the building blocks of these superpositions were ordinary coherent states (the quantum equivalent of a classical wave) or simple Gaussian squeezed states. This Oxford team asked: what if the building blocks themselves were already deeply non-classical?

Their answer is to superpose *generalized squeezed states* — exotic states with three- and four-fold rotational symmetry in quantum phase space that can't be described by any classical probability distribution. These "trisqueezed" and "quadsqueezed" states, and more importantly their superpositions, had never been experimentally realized before.

The platform is a single trapped strontium ion. Its vibration along the trap axis acts as the quantum oscillator; its internal electronic levels act as a two-level spin (or, when needed, a three-level qutrit). The central innovation is a spin-dependent nonlinear interaction that kicks the oscillator differently depending on the spin state. By first putting the spin in superposition and then applying this kick, the spin and oscillator become entangled — each spin outcome is correlated with a different oscillator state. A mid-circuit measurement of the spin then projects the oscillator into the desired superposition, non-destructively, because the protocol is designed so the target state always corresponds to the outcome that doesn't scatter photons.

To build superpositions of *different* constituents — say, a squeezed state plus a trisqueezed state — the team extends the spin to three levels. One level acts as a "parking lot": store the first constituent there, build the second independently, then recombine. This gives complete independent control over all four parameters of the superposition.

The team verifies everything through full quantum state tomography, reconstructing the Wigner quasi-probability distributions of the oscillator states. The negative regions confirm non-classicality, and quantitative comparison shows these states carry more quantum computational resource than previously demonstrated cat states or Fock states at comparable energy cost.

The method generalizes to any spin-coupled oscillator system, making this a practical blueprint for continuous-variable quantum computing and enhanced sensing.

## Human

Explain What this actually means: the spin controls the sign of the kick. When the spin is up (+1), the oscillator gets pushed one way; when the spin is down (−1), it gets pushed the other. This sign-conditional pushing is what lets them create a superposition of two states squeezed in opposite directions — by first putting the spin in a superposition of up and down, then applying the push.

## Assistant

Responding

Let's build this up from scratch, with a concrete picture at every step.

---

**First: what does "squeezing" look like physically?**

Imagine the oscillator's quantum state as a blob of uncertainty plotted on a 2D map — the horizontal axis is position (where the ion is), the vertical axis is momentum (how fast it's moving). A ground-state oscillator is a circular blob — equal uncertainty in both directions. A *squeezed* state is that same blob, but squashed into an ellipse: tighter in one direction, stretched in the other.

Crucially, *which direction* the ellipse points is what the squeezing *phase* φ controls. Squeezing "along x" means the ellipse is horizontal. Squeezing "along y" means it's vertical. Squeezing "at 45°" tilts it diagonally.

---

**Now: what does the Hamiltonian actually do?**

The interaction is:

$$\hat{H}_k = \frac{\hbar\Omega_k}{2}\hat{\sigma}_z(\hat{a}^k e^{-i\phi} + (\hat{a}^\dagger)^k e^{i\phi})$$

The critical piece is $\hat{\sigma}_z$. This operator has eigenvalue **+1** when the spin is in state |1⟩, and **−1** when the spin is in state |0⟩.

So the full Hamiltonian that the oscillator *actually experiences* is:

- Spin up: the oscillator sees $+\frac{\hbar\Omega_k}{2}(\hat{a}^k e^{-i\phi} + \hat{a}^{\dagger k} e^{i\phi})$
- Spin down: the oscillator sees $-\frac{\hbar\Omega_k}{2}(\hat{a}^k e^{-i\phi} + \hat{a}^{\dagger k} e^{i\phi})$

Flipping the sign of the entire squeezing Hamiltonian is *exactly equivalent* to rotating the squeezing axis by 90° (for k=2) or by the appropriate fraction of a full rotation for higher orders. It's like telling the squeezing to go in the opposite direction.

Concretely: spin up squeezes the ellipse pointing northeast-southwest. Spin down squeezes it pointing northwest-southeast. Same magnitude, opposite orientation.

---

**Now add superposition**

Before applying the push, the team rotates the spin into:

$$|{+_s}\rangle = \frac{|0_s\rangle + |1_s\rangle}{\sqrt{2}}$$

The spin is genuinely in both states at once. Quantum mechanics now demands that the oscillator evolve under *both* versions of the Hamiltonian simultaneously. The system's joint state becomes entangled:

$$|\text{joint}\rangle = \frac{1}{\sqrt{2}}\Big(|\zeta_k\rangle|1_s\rangle + |-\zeta_k\rangle|0_s\rangle\Big)$$

Where $|\zeta_k\rangle$ is the oscillator squeezed one way, and $|-\zeta_k\rangle$ is it squeezed the opposite way. The oscillator is in *both* squeezed orientations at once, each locked to a different spin state.

---

**The measurement closes the loop**

The entangled joint state isn't yet the target — the spin and oscillator are still linked. The mid-circuit spin measurement breaks that link. When the measurement finds spin in |1_s⟩, the oscillator is projected into a *superposition* of $|\zeta_k\rangle$ and $|-\zeta_k\rangle$ — an even or odd combination depending on one more spin rotation just before the measurement.

The oscillator is now in a superposition of two blobs pointing in different directions in phase space, with quantum interference between them — visible as the oscillating fringes you see between the lobes in the Wigner function plots.

---

**The one-line intuition**

The spin acts like a coin flip that happens *in quantum superposition*. Because the coin is both heads and tails when the push is applied, the oscillator gets pushed both ways simultaneously — and you get a superposition of two squeezed states rather than just one.

## Human

What is the push that rotates the spin

## Assistant

Responding

Great question — and it's easy to conflate two different things here, so let's be precise.

---

**The spin rotation and the oscillator push are completely separate operations.**

The spin rotation is just a standard qubit gate. The oscillator push is the nonlinear interaction. They do different jobs.

---

**The spin rotation: a laser pulse**

The $R_y(\pi/2)$ rotation — the one that puts the spin into superposition before the push — is driven by a **674 nm laser** tuned to the quadrupole transition between the two electronic levels of the strontium ion:

$$|0_s\rangle \equiv |5S_{1/2}, m_j = -\tfrac{1}{2}\rangle \quad \longleftrightarrow \quad |1_s\rangle \equiv |4D_{5/2}, m_j = -\tfrac{3}{2}\rangle$$

This transition connects the ground electronic state to a long-lived excited state (the D state has a lifetime of ~400 ms, making it an excellent qubit). A precisely timed pulse at 674 nm drives a coherent rotation on the Bloch sphere — a $\pi/2$ pulse takes the spin from |0⟩ to $(|0\rangle + |1\rangle)/\sqrt{2}$.

This is completely standard atomic physics. There's nothing exotic here — it's the same kind of operation used in every trapped-ion qubit experiment. The laser doesn't touch the ion's motion at all; it only acts on the internal electronic state.

---

**The oscillator push: two non-commuting spin-dependent forces**

This is where the physics gets nontrivial. The nonlinear Hamiltonian $\hat{H}_k$ isn't generated by a single laser beam. It requires combining **two spin-dependent forces (SDFs)** that don't commute with each other.

Each individual SDF is a *linear* interaction — it displaces the oscillator conditioned on the spin state, generating first-order (k=1) coupling. But when you apply two SDFs whose phases are offset in a specific way, their *combined* effect, through the Baker-Campbell-Hausdorff algebra of non-commuting operators, generates the higher-order k-phonon interaction. Two 674 nm beams with carefully chosen frequencies, phases, and timing produce the effective $\hat{a}^k$ coupling.

The key point: **the spin rotation and the oscillator push are driven by the same laser system, but they're doing entirely different things.** The rotation is a resonant transition between two electronic levels. The SDF is an off-resonant, motional-sideband drive that couples spin and motion. They're interleaved in time — rotation first, then push, then rotation again — but they're physically distinct pulses.

---

**So the sequence is:**

1. 674 nm pulse, resonant — rotates spin to superposition (no effect on motion)
2. Two 674 nm beams, sideband-tuned — apply spin-dependent nonlinear push (entangles spin and motion)
3. 674 nm pulse, resonant again — rotates spin to set up measurement basis
4. Fluorescence detection on the $5S_{1/2} \leftrightarrow 5P_{1/2}$ transition — measures spin non-destructively (if dark state is detected)

The spin rotation doesn't know about the oscillator. The oscillator push doesn't work without the spin being in superposition first. They're separate controls on the same physical object — the ion — that happen to be sequenced together to produce the entanglement.

## Human

Explain? This is where the physics gets nontrivial. The nonlinear Hamiltonian hat H k isn't generated by a single laser beam. It requires combining two spin-dependent forces (SDFs) that don't commute with each other.
Each individual SDF is a linear interaction — it displaces the oscillator conditioned on the spin state, generating first-order (k=1) coupling. But when you apply two SDFs whose phases are offset in a specific way, their combined effect, through the Baker-Campbell-Hausdorff algebra of non-commuting operators, generates the higher-order k-phonon interaction. Two 674 nm beams with carefully chosen frequencies, phases, and timing produce the effective hat a to the k coupling.

## Assistant

Responding

Good — this deserves a proper unpacking. Let me build it from the ground up.

---

**Start with one SDF alone**

A single spin-dependent force is conceptually simple. The laser drives a motional sideband transition: it pushes the ion's motion *left* if the spin is up, and *right* if the spin is down. In phase space, this is a *displacement* — it moves the blob without changing its shape.

The Hamiltonian for one SDF looks schematically like:

$$\hat{H}_{\text{SDF}} = g \cdot \hat{\sigma}_z(\hat{a} + \hat{a}^\dagger)$$

- $g$ : coupling strength
- $\hat{\sigma}_z$ : spin operator, gives ±1
- $(\hat{a} + \hat{a}^\dagger)$ : position-like operator for the oscillator — this is a *linear* function of the ladder operators

This is k=1. It shifts the oscillator's phase-space blob left or right depending on spin. It does **not** squeeze, deform, or reshape the blob. It just translates it.

---

**Why k=1 can never give you squeezing alone**

Squeezing requires a k=2 interaction — terms like $\hat{a}^2$ and $(\hat{a}^\dagger)^2$. These *deform* the blob into an ellipse. You can't get $\hat{a}^2$ from a single linear drive, for the same reason you can't get $x^2$ by applying the function $f(x) = cx$ once. You need something nonlinear.

The question is: how do you *build* $\hat{a}^2$ out of things you can actually apply in the lab?

---

**The Baker-Campbell-Hausdorff trick**

Here's the key mathematical fact. If you have two operators $\hat{A}$ and $\hat{B}$ that *don't commute* — meaning $\hat{A}\hat{B} \neq \hat{B}\hat{A}$ — then applying them in sequence is not the same as applying their sum. Specifically:

$$e^{\hat{A}}e^{\hat{B}} = e^{\hat{A} + \hat{B} + \frac{1}{2}[\hat{A},\hat{B}] + \ldots}$$

The extra term $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ is the *commutator* — it measures how much the two operators fail to commute. This is the Baker-Campbell-Hausdorff (BCH) formula.

The crucial point: **the commutator of two linear operators can be quadratic.** Schematically:

$$[\hat{\sigma}_z(\hat{a}e^{i\theta_1} + \hat{a}^\dagger e^{-i\theta_1}),\ \hat{\sigma}_z(\hat{a}e^{i\theta_2} + \hat{a}^\dagger e^{-i\theta_2})]$$

When you work this out, the $\hat{\sigma}_z \cdot \hat{\sigma}_z$ terms combine to give the identity (since $\hat{\sigma}_z^2 = 1$), and the cross terms between $\hat{a}$ and $\hat{a}^\dagger$ give you things like $\hat{a}^2$, $(\hat{a}^\dagger)^2$, and $\hat{a}\hat{a}^\dagger$. The phase offset $(\theta_1 - \theta_2)$ between the two SDFs controls which combination dominates.

In other words: **two linear spin-dependent pushes, applied in the right sequence with the right phase offset, conspire through their non-commutativity to generate a quadratic interaction.** The nonlinearity emerges from the *order-dependence* of sequential operations, not from any single nonlinear element.

---

**A concrete analogy**

Imagine you're in a room and you can only walk in straight lines. Two moves:
- Move A: walk 1 step north
- Move B: walk 1 step east

If the room is flat (commuting), A then B lands you in the same place as B then A. No new territory.

Now imagine the room is curved — like the surface of a sphere. Walking north then east lands you somewhere *different* from east then north. That difference — the gap between the two paths — traces out a *curve*, something qualitatively new that neither straight-line move could reach alone.

BCH is exactly this: the "curvature" of the operator algebra generates new terms that neither operator contained individually. The commutator is the area enclosed between the two paths.

*Breaks when:* you push the geometry analogy to ask about the shape of the curved space. The operator algebra isn't a Riemannian manifold — the BCH series has infinitely many terms in general (though for the specific operators here, the series truncates cleanly because the commutator structure is simple).

---

**How this generalizes to k=3 and k=4**

For trisqueezing (k=3), you need $\hat{a}^3$. You can get there by applying *three* SDFs in sequence, or by applying two SDFs where one of them is already a k=2 interaction. Each additional layer of BCH nesting pushes you up by one order.

For quadsqueezing (k=4), you need $\hat{a}^4$ — another layer deeper. This is why the quadsqueezed results in the paper show the most experimental degradation: each additional layer of non-commuting operations requires more precise pulse calibration, and errors compound. You're building a higher-degree polynomial from linear tools, and the scaffolding gets taller with each step.

---

**The one-line version**

A single SDF pushes. Two SDFs with mismatched phases, applied in sequence, *squeeze* — because their non-commutativity generates quadratic operator terms that neither push alone contained. The nonlinearity is not in any individual laser pulse; it lives in the *algebra of sequential operations*.

## Human

What is meant by push?

## Assistant

Responding

Really good question to ask — "push" is intuitive but imprecise. Let me make it exact.

---

**In phase space, a push is a displacement**

Remember the 2D map — horizontal axis is position (x), vertical axis is momentum (p). The oscillator's quantum state is a blob sitting somewhere on that map.

A *displacement* moves the center of that blob from one point to another — say from the origin to the point (x₀, p₀). The shape of the blob doesn't change. The size doesn't change. It just *slides*.

That's the push. Formally it's generated by the *displacement operator*:

$$\hat{D}(\alpha) = e^{\alpha \hat{a}^\dagger - \alpha^* \hat{a}}$$

- $\alpha$ : a complex number specifying how far and in what direction to move — its real part shifts position, its imaginary part shifts momentum
- $\hat{a}^\dagger, \hat{a}$ : creation and annihilation operators — they're the phase-space coordinates repackaged

What this actually means: applying $\hat{D}(\alpha)$ to any state rigidly translates its entire phase-space distribution by the vector $\alpha$. Nothing else happens.

---

**Why "spin-dependent" makes it interesting**

A plain displacement moves the blob unconditionally. A *spin-dependent* displacement moves it in *opposite directions* depending on the spin state:

- Spin up: blob moves to $+\alpha$
- Spin down: blob moves to $-\alpha$

So if you start with the spin in superposition and the oscillator as a single blob at the origin, after the spin-dependent displacement you have an *entangled* state — blob at $+\alpha$ correlated with spin up, blob at $-\alpha$ correlated with spin down. Two copies of the blob, pushed apart in opposite directions.

This is already a kind of cat state — it's just built from coherent states (round blobs), not squeezed ones.

---

**The SDF is specifically a momentum kick**

In the trapped ion context, the spin-dependent force drives the ion at its motional resonance frequency. This means the laser is continuously pushing the ion's oscillation — accelerating it, in the mechanical sense. Over the duration of the pulse, this builds up a net displacement in phase space.

The direction of that displacement — whether it moves the blob along the position axis, the momentum axis, or some diagonal — depends on the *phase* of the laser relative to the oscillator's natural oscillation. You tune the phase, you choose the direction of the push.

---

**So to be fully precise:**

When this analysis says "push," it means: **a coherent, reversible, rigid translation of the oscillator's phase-space distribution**, conditioned on spin state, with no change to the blob's shape or size.

The squeezing and deformation — the ellipse, the lobes, the rotational symmetry — all come later, as an emergent consequence of applying two such pushes in sequence with incompatible directions. The push itself is the simplest possible thing you can do to an oscillator state short of doing nothing.
