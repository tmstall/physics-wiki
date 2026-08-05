---
source: claude_export
conversation_uuid: 11579b57-57a8-4a14-94ba-5de949eee106
title: "Entanglement detected in macroscopic crystal via neutron scattering"
created_at: 2026-06-17T19:25:15.975655Z
updated_at: 2026-06-17T19:29:41.560646Z
tier: A
score: 245
n_messages: 2
---

# Entanglement detected in macroscopic crystal via neutron scattering

## Human

Analyze this paper

## Assistant

Analyzing — v3.6.3

# Catching Entanglement with a Neutron Beam, Not a Trapped Ion

**Hook:** A crystal you could hold between two fingers just gave up direct evidence that groups of at least nine of its magnetic moments are acting as single quantum-entangled units — and the team found this not by isolating anything, but by hitting the crystal with neutrons and running the response through a quantum-metrology formula.

## 2. Big-Picture Context

Whether genuinely quantum behavior — superposition, entanglement — can survive in a macroscopic object made of billions of particles is one of the oldest open questions in physics, dating back to the Schrödinger's cat thought experiment. Most demonstrations of entanglement live in tightly controlled, isolated few-particle systems: trapped ions, photons, ultracold atoms. The question of whether a solid, sitting on a benchtop at finite temperature, can host and reveal *quantifiable* entanglement among huge numbers of particles has been much harder to answer experimentally.

This paper, from TU Wien, Würzburg, Rice, and the Institut Laue-Langevin (ILL), goes after that question through "strange metals" — materials whose electrical resistivity grows linearly with temperature all the way down to the lowest temperatures probed, in flagrant violation of the textbook (Fermi-liquid) prediction of a T² dependence. Strange metallicity shows up across cuprate superconductors, heavy fermion compounds, pnictides, and moiré flat-band systems, and is widely suspected to be connected to high-temperature superconductivity, but there's no settled microscopic theory. One leading candidate is "Kondo destruction" — the idea that at a quantum critical point, the localized magnetic moments in the material abruptly decouple from the conduction electrons, and that this decoupling, not a conventional order-parameter transition, drives the strange behavior.

This group's strategy is to import a tool from quantum metrology — the quantum Fisher information (QFI) — into a condensed-matter measurement. QFI quantifies how sensitively a quantum state responds to a small perturbation, and it's directly related (via theory work by Hauke, Heyl, Tagliacozzo, and Zoller) to the same dynamic susceptibility that inelastic neutron scattering (INS) experiments already measure. That gives a route to *quantify* entanglement in a real solid using a standard solid-state-physics technique, rather than anything resembling quantum-computing hardware.

**Prior Belief Check:** The result aligns with a specific theoretical prediction — that QFI should diverge as T → 0 at a "strongly entangled" quantum critical point but show no such signature at an ordinary thermal phase transition — while complicating the simpler picture suggested by an earlier spin-chain experiment, where QFI tracked a conventional magnetic order parameter and shrank as that order was suppressed. Here, instead, QFI keeps climbing as the conventional order vanishes, because it's tracking the Kondo-destruction fluctuations themselves rather than the order parameter. That's genuinely surprising to specialists in quantum criticality, not just to outsiders: it's the first time anyone's shown that a rigorous entanglement witness, rather than a qualitative narrative, separates "beyond-Landau" criticality from textbook order-disorder criticality.

**Replication & Convergence Note:** This is a single experimental collaboration, a single material (Ce₃Pd₂₀Si₆), and a single quantum critical point. There is no independent replication yet. Confirmation would mean another, unaffiliated group reproducing the QFI rise at a different Kondo-destruction (or other beyond-Landau) critical point, ideally in a different material class, to rule out an instrument- or calibration-specific artifact in the painstaking absolute-unit conversion the authors describe.

## 3. Necessary Background Crash-Course

**Strange metal resistivity.** A normal metal's resistivity from electron scattering grows as T² at low temperature — the Fermi-liquid result, the condensed-matter equivalent of a well-behaved leakage-current scaling law you'd expect in a semiconductor device. A strange metal's resistivity instead grows linearly in T, all the way down to the coldest temperatures measured, as if the "leakage" never freezes out the way ordinary physics says it should.
*Breaks when:* pushed to explain *why* this particular power law shows up microscopically — the analogy describes the phenomenology, not the mechanism.

**Kondo screening and Kondo destruction.** Picture each cerium magnetic moment as a stray signal sitting on a line; below a characteristic temperature, the surrounding sea of conduction electrons "absorbs" that signal the way a coherent cache write neutralizes a stray bit — the local moment effectively disappears, folded into the itinerant electron sea (this is Kondo screening). Kondo destruction is what happens when you tune a parameter (here, magnetic field) until that screening process abruptly fails: the local moment "unhooks" from the conduction sea, and — crucially — the Fermi surface itself reconstructs, not just the magnetic order.
*Breaks when:* you imagine the unscreened moment as simply reverting to a free, pre-screening state — it doesn't; it enters a new collective regime whose fluctuations are entangled with the fermionic continuum in a way the "cache flush" picture doesn't capture.

**Quantum critical point (QCP).** Tuning a field to the exact point where two competing phases balance is like dialing a bias voltage in a circuit to sit precisely on a metastability boundary, where fluctuations at every timescale become correlated (scale invariance).
*Breaks when:* you picture the QCP as something you can sit at experimentally — you can only approach T = 0 asymptotically, so all "QCP physics" is extrapolated from finite-temperature data, never measured exactly at the point itself.

**Inelastic neutron scattering (INS).** Firing neutrons at the crystal and measuring how much energy and momentum each one loses is like injecting a small test signal into a black-box circuit and reading off the frequency-dependent, phase-lagged response — that response is exactly the dynamic susceptibility

χ′′(**q**, ω, T)

**Symbol definitions:**
χ′′ : imaginary part of the dynamic susceptibility — the system's intrinsic dissipative (energy-absorbing) response
**q** : momentum transferred to the crystal lattice
ω : angular frequency of energy transferred
T : temperature

**What this actually means:** It's the solid-state analogue of measuring a device's frequency-dependent impedance with a weak AC probe — you're reading off exactly how much, and at what frequencies, the material "absorbs" a small perturbation.
*Breaks when:* at large momentum/energy transfer, the neutron beam also picks up lattice vibration (phonon) signal mixed in with the magnetic response — extracting the pure spin response demanded the careful background subtraction the authors describe in their supplementary materials, unlike a clean two-port electrical measurement.

**Quantum Fisher information and entanglement depth.** If N particles respond completely independently to a perturbation, their collective sensitivity (susceptibility) can only grow linearly with N — like N independent antennas, each contributing its own small signal. If groups of k particles are entangled, they respond as single coherent units that can exceed that independent-particle bound — the same resource a phased array exploits to beat a set of independent antennas at detecting a weak signal. Measuring an anomalously large QFI per particle therefore lower-bounds the cluster size k.
*Breaks when:* pushed to claim this is the same kind of clean, long-coherence-time entanglement engineered in trapped-ion or cold-atom qubit registers — QFI here is a witness/lower bound extracted from a thermal, decohered solid, not a verification of a specific pure entangled state.

**Central analogy for this paper: Phased-array antenna of entangled spins.**

## 4. Core Technical Explanation

The team picked Ce₃Pd₂₀Si₆ because its Kondo-destruction physics is already well mapped: a field-tuned QCP near B_Q ~ 1.73 T (field along [001]) continuously suppresses antiferroquadrupolar (AFQ) order, and the material's resistivity crosses over from enhanced Fermi-liquid behavior into the strange-metal linear-in-T form right at that point. They probed the wavevector **q** = (0, −1, 0) — deliberately *not* a structural or magnetic Bragg peak — because Kondo-destruction fluctuations are known to spread broadly across momentum space rather than peaking sharply the way conventional magnetic order does; that choice makes the measurement representative of the critical fluctuations across the whole Brillouin zone, while avoiding contamination from the order parameter itself.

They measured at the ThALES cold-neutron triple-axis spectrometer at ILL (Grenoble), with energy resolution near 0.07 meV, cooling down to 60 mK — that extreme resolution and cold are necessary because the relevant energy and temperature scales near a QCP are tiny, and they invested heavily in converting the raw counts into absolute units with careful background removal, since any uncorrected systematic offset would directly distort the final entanglement number.

From the resulting χ′′(**q**, ω, T), they compute the QFI density via a Kubo-type formula:

f_Q(T) = (4/π) ∫₀^∞ tanh(ħω / 2k_BT) χ′′(ω,T) d(ħω)

**Symbol definitions:**
f_Q(T) : QFI density at temperature T — the entanglement-witness quantity, intensive (counted per spin/moment)
ħ : reduced Planck's constant
ω : angular frequency of energy transferred to the neutron
k_B : Boltzmann's constant
T : temperature
χ′′(ω,T) : the system's dissipative response, as defined above

**What this actually means:** The tanh factor acts like a lock-in amplifier — at low T it weights the low-frequency response close to its full quantum value, while at high T it suppresses that same response, filtering out garden-variety thermal noise and isolating the part of the fluctuation spectrum that's genuinely "quantum" rather than classical.

They found that f_Q(T) rises strongly as T decreases toward the QCP, with no characteristic temperature where the rise levels off — scale-free growth, the hallmark of genuine critical behavior rather than a crossover with some built-in cutoff. Because this was measured at a wavevector tracking the Kondo-destruction fluctuations rather than the AFQ order parameter, the rise reflects the "beyond-Landau" critical fluctuations themselves — contrasting directly with the earlier spin-chain experiment where QFI tracked, and shrank with, a conventional Néel order parameter. Comparing the observed f_Q against the theoretical bound relating QFI to entanglement depth (independent particles cap the achievable QFI; entangled clusters of size k push it higher) implies clusters of at least nine moments acting collectively — too large a response to be explained by independent particles.

**Assumption Audit**

Watch 1: The reader likely assumes the experiment put the crystal into a literal macroscopic superposition, Schrödinger's-cat style. The paper actually never does this — it measures a linear response function (how the crystal dissipates energy from a weak neutron probe) and infers the entanglement witness from that response via the QFI-Kubo relationship. The entanglement is inferred from fluctuation statistics, not observed via interference.

Watch 2: The reader likely assumes "groups of at least nine entangled particles" means nine specific, identifiable spins sit in a clean entangled state, the way you'd describe a 9-qubit GHZ state in a trapped-ion register. The paper actually only establishes a lower bound on entanglement depth from an inequality; the underlying state is a complicated, mixed, finite-temperature many-body density matrix, and "at least nine" is the minimum cluster size consistent with the data — not a count of specific spins or a description of their state.

Watch 3 (the non-obvious one): A reader who's spent time with entanglement entropy in the holographic/QECC/tensor-network sense (a recurring frame in spacetime-emergence discussions) might assume QFI is measuring the same thing — it isn't. QFI is a metrological witness tied to a specific generator (here, total spin/magnetic moment) and a specific measurement channel; it lower-bounds multipartite entanglement depth but isn't interchangeable with von Neumann entanglement entropy, mutual information, or the entanglement measures used in holographic spacetime discussions. Different operational definition, different physical meaning, not simply convertible into each other.

## 5. What's Genuinely New or Clever

First, they moved the QFI technique off a "tame" target — a conventional order parameter in a spin chain, where it was first demonstrated — onto genuinely contested territory: Kondo-destruction strange-metal fluctuations that have no good Landau order-parameter description. Choosing a wavevector deliberately away from any Bragg peak is the technical move that makes this possible; it isolates the beyond-Landau fluctuations rather than the order parameter.

Second, the scale-free, unbounded growth of QFI as T → 0 converts a previously qualitative claim — "Kondo destruction breaks the quasiparticle picture and is unusually entangled" — into a number extracted directly from a neutron-scattering curve, compared against a rigorous mathematical bound. That's new to the field, not just to a general audience: it gives strange-metal theory a quantitative entanglement fingerprint to test future microscopic models against.

## 6. Limitations & Open Questions

This is a single material and a single quantum critical point; generality across the wider strange-metal landscape — cuprates, pnictides, moiré flat-band systems — is untested. **(A) Consensus** — single-system, single-probe results in correlated-electron physics routinely require cross-material validation before claims of universality are accepted; that's standard practice in the field. *(broader literature)*

"At least nine" is a lower bound on entanglement depth, not a measurement of the true cluster size or its internal structure; the real number could be larger, and how tight the bound is depends on the choice of generator and normalization. **(B) Contested** — some specialists treat QFI depth bounds as fairly tight and well-motivated; others argue the bound can meaningfully underestimate depth depending on which channel is probed, so how informative "nine" is in absolute terms isn't fully settled. *(analyst inference, informed by the broader QFI-metrology literature)*

The result hinges on extreme care in absolute-unit calibration and background subtraction of the INS data; any residual systematic offset there would shift the extracted QFI and the inferred depth. **(A) Consensus** — absolute-unit calibration is a universally recognized source of systematic uncertainty in quantitative neutron scattering, and the authors themselves flag it as requiring special treatment. *(paper, methods/intro)*

There's no established path yet for whether this diagnostic generalizes to strange metals lacking a well-defined local moment to "Kondo destroy" — cuprates being the obvious test case. **(C) Speculative** — this is my read on the natural next experimental target; the authors frame their own next step as exploring quantum-metrology applications rather than necessarily cross-material replication, so the field's actual near-term priority may differ from my guess. *(analyst inference)*

## 7. Detailed Summary & Explanation

The team studied the heavy fermion compound Ce₃Pd₂₀Si₆, a well-characterized strange metal whose Kondo-destruction quantum critical point sits near a field of 1.73 tesla. Rather than probing the magnetic order that vanishes at that point, they targeted a momentum location chosen specifically to capture the broader, scale-spanning fluctuations associated with the breakdown of Kondo screening itself. Using one of the world's highest-resolution cold-neutron spectrometers, cooled to 60 millikelvin, they extracted the material's dissipative response with enough precision and absolute calibration to plug directly into the quantum Fisher information formula — a tool borrowed from quantum metrology that converts a system's sensitivity to perturbation into a rigorous entanglement witness.

The headline finding: this quantity grows steadily larger, with no sign of leveling off, as the material is cooled toward its critical point. That unbounded growth is the experimental signature theorists had predicted for a "strongly entangled" quantum critical point — and it's qualitatively different from an earlier experiment on a simpler magnet, where the same quantity tracked, and shrank with, an ordinary magnetic order parameter. Comparing the measured values against a known mathematical bound, the authors show the response is too large to be explained by particles acting independently; it requires clusters of at least nine magnetic moments behaving as single collective units. That's direct, quantitative evidence of high multipartite entanglement in an everyday, centimeter-scale crystal — not a delicate, isolated few-particle system.

The key interpretive choice in this summary is to foreground the QFI-Kubo bridge and the entanglement-depth bound as the methodological core, rather than dwelling on the detailed AFQ/AFM phase diagram of Ce₃Pd₂₀Si₆ — the phase diagram is the experimental staging ground, but the conceptual payoff is the demonstration that a standard solid-state probe can deliver a rigorous quantum-information quantity.

**Where I'm least confident in this analysis:** the precise derivation and normalization behind the "at least nine" depth figure — exactly which generator and channel normalization the authors used to convert their measured f_Q into that specific bound, and how the associated error bars and the "no characteristic scale" claim were quantified. I'm working from the abstract, introduction, and methods excerpts of the arXiv preprint plus secondary press coverage rather than the full Methods and Supplementary Materials with the complete normalization and statistics, so that quantitative step is the part most likely to have lost nuance in translation.

## 8. Three Crystallized Takeaways

1. A fist-sized, ordinary-looking crystal showed groups of at least nine magnetic moments acting as a single quantum-entangled unit — proof that entanglement isn't confined to the carefully isolated qubits of a quantum computer.
2. Nobody put anything into superposition. The team simply measured how hard the crystal pushed back against a neutron beam, then ran that response through a rigorous quantum-metrology formula to extract a guaranteed minimum amount of entanglement.
3. The entanglement signal grew without bound as the material approached its "strange metal" quantum critical point, turning a vague intuition — that strange metals are unusually entangled — into an actual measured, bounded number.

## 9. Shorter Summary

Physicists have long wondered whether quantum entanglement — usually demonstrated in carefully isolated single atoms or photons — can show up, and be quantified, in an ordinary macroscopic solid. A team from TU Wien, Würzburg, Rice, and the ILL neutron facility in Grenoble has now done exactly that, using a centimeter-scale crystal of a heavy fermion "strange metal," Ce₃Pd₂₀Si₆.

Strange metals are materials whose electrical resistance grows in an anomalous, straight-line way with temperature, defying the textbook behavior of ordinary metals, and they're suspected to hold clues to high-temperature superconductivity. One leading explanation involves "Kondo destruction" — a quantum critical point where local magnetic moments abruptly decouple from the surrounding sea of conduction electrons.

Rather than building anything resembling quantum-computer hardware, the team fired neutrons at the crystal and measured how it absorbed energy, then fed that response into the quantum Fisher information, a tool from quantum metrology that quantifies entanglement from a system's sensitivity to disturbance. As they cooled the crystal toward its critical point, this quantity grew steadily larger with no sign of leveling off — exactly the signature theorists had predicted for a deeply entangled quantum critical point. Comparing the result against a rigorous mathematical bound, they showed the response was too strong to come from independently acting particles: it required clusters of at least nine magnetic moments behaving as single, collectively entangled units.

This doesn't mean the crystal was placed in some giant superposition. It means a standard, decades-old experimental technique — neutron scattering — can extract a number that rigorously certifies a minimum degree of multipartite entanglement in a real material, at finite temperature, at a scale you can hold in your hand. The result is from a single experimental collaboration and a single material; independent replication in a different system hasn't happened yet. But it opens a genuinely new bridge between condensed-matter physics and quantum information theory, and the authors' next goal is to explore whether strange metals could themselves become useful quantum-metrology devices.
