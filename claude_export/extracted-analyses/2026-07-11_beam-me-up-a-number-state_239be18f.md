---
source: claude_export
conversation_uuid: 239be18f-fcb6-49a5-8b20-4c3fb21930b0
title: "Beam Me Up a Number State"
created_at: 2026-07-11T03:25:07.112053Z
updated_at: 2026-07-11T17:10:06.165110Z
tier: A
score: 47
n_messages: 6
---

# Beam Me Up a Number State

## Human

Analyze this paper

## Assistant

The full paper is on arXiv. Let me retrieve it for a complete analysis.

Analyzing | Framework v3.7.1

**Access Status**
Full paper: retrieved from arXiv (2601.10325v1, main text + full Supplementary Materials).
Abstract: retrieved from Nature Physics landing page (published version, DOI 10.1038/s41567-026-03370-9).
Supplementary material: full SM retrieved via arXiv HTML (Secs. I–VII, Figs. S1–S10, Table S1).
Analysis basis: full text. Note: the arXiv title ("...Scalable Manipulation of Giant Quantum States") differs cosmetically from the Nature Physics title ("...for the scalable manipulation of large quantum states") — same paper, same authors, same figures.

Pre-read note: full Nature Physics article with substantial theory + experiment. Not a lite candidate — proceeding directly to full analysis.

---

## 1. Punchy Title & Hook

**"Beam Me Up a Number State: Doing Classical Optics Inside a Single Cavity's Photon Ledger."**

By treating the photon-number index as a spatial axis, the authors show that a single microwave cavity under a weak drive obeys the *same* paraxial wave equation as a light beam — so they build a prism, a lens, a spectrometer, a double-slit, and an imaging system entirely out of one mode's Fock amplitudes, focusing a 150-photon state with 10× better efficiency than prior art.

---

## 2. Big-Picture Context

The hard problem in bosonic quantum information is that a cavity mode's Hilbert space is huge (formally infinite), and the workhorse methods for sculpting states in it — GRAPE, SNAP, optimal-control pulse-finding — scale badly. Every additional photon level you want to touch adds parameters to a numerical optimization that grows expensive fast. That's why deterministic control historically topped out at a handful of photons, and why the one prior demonstration reaching ~100 photons did so probabilistically (2.2% success for |100⟩) rather than scalably.

This paper attacks the scaling wall not with a better optimizer but with a *change of coordinates*. The photon-number axis $n$ is reinterpreted as a synthetic spatial dimension. A weak coherent drive hops population between adjacent Fock states $|n\rangle \leftrightarrow |n{\pm}1\rangle$; in the large-photon limit those hops become approximately uniform in strength, which is exactly the condition for a discrete lattice to support "discrete diffraction" like a waveguide array. Once the dynamics reduce to a diffusion/paraxial equation, three centuries of optical engineering intuition become directly importable.

The landscape before this: synthetic dimensions in photonics (Yuan, Fan and others) and Fock-state lattices were established ideas, and space–time duality in optics (Kolner) is textbook. What was missing was a *systematic, experimentally demonstrated optical toolbox* — prism, lens, dispersion, interference, imaging — operating deep in the large-photon regime of a real circuit-QED device, plus the efficiency payoff that comes with it.

**Paper Type & Stakes.** This is an experimental demonstration paper that also introduces a conceptual reframing: it maps a known piece of physics (single-mode Schrödinger evolution under weak drive) onto a known equation (paraxial diffraction) and then exploits the mapping to do state engineering that would otherwise be numerically intractable. Stakes: a scalable, intuition-driven alternative to brute-force optimal control for large bosonic states, with an immediate metrology dividend.

**Prior Belief Check.** This does not overturn any consensus and would not shock an expert at the "that can't be true" level — the underlying duality is analytically clean and sits comfortably in the synthetic-dimension / space-time-duality tradition. What experts *would* find genuinely notable is the combination of (a) coherent control demonstrated at up to 180 photons in circuit QED, (b) the order-of-magnitude jump in efficiency for reaching high-$n$ squeezed states (17% for |150⟩ vs. 2.2% for |100⟩ prior), and (c) the time-reversal "concave lens" trick that has no classical analog. Call it elegant unification plus a strong experimental result, not a paradigm break.

**Replication & Convergence Note.** Single collaboration (Tsinghua / USTC, the Sun–Zou group), one device. There is a closely related companion paper from essentially the same group projecting Fock states beyond 10,000 photons (arXiv:2601.05118), but that is not independent confirmation. The *concept* rests on solid analytics, so it isn't fragile; the specific experimental figures of merit (17% success, 19.7 dB sensing gain, 84–90% imaging similarity) are what independent labs — a Yale/ETH-lineage cavity group, say — would need to reproduce before those numbers are treated as settled rather than promising.

---

## 3. Necessary Background Crash-Course

**Fock space and the coherent state.** A cavity mode's state is a stack of amplitudes $c_n$ over photon-number rungs $|n\rangle$. A coherent state (what a classical-looking drive produces) has a Poissonian spread over $n$; when the mean $\bar n$ is large, that Poissonian is essentially a Gaussian bump centered at $\bar n$ with width $\sqrt{\bar n}$.

*Analogy:* the amplitude profile $\{c_n\}$ is a **wavefront sampled across the elements of a phased array**, with each Fock rung $n$ playing the role of one antenna element.
*Breaks when:* you slide the bump down toward $n=0$. The array has a hard wall at the vacuum (no negative $n$), and near it the element-to-element coupling stops being uniform — the clean "free space" picture only holds deep in the large-$n$ bulk.

**Why large $n$ matters (the uniform-hopping trick).** The drive couples neighbors with strength $\propto\sqrt{n}$. That $\sqrt{n}$ dependence is the villain that makes small-photon control ugly. But for $n\gg 1$, $\sqrt{n{+}1}\approx\sqrt{n}\approx\sqrt{\bar n}$ — the coupling flattens out.

*Analogy:* it's like a **memory bus where per-hop latency becomes constant** once you're far enough from address zero — every step costs the same, so a packet spreads smoothly instead of getting distorted hop-to-hop.
*Breaks when:* the distribution gets broad enough that its edges sample meaningfully different $\sqrt{n}$ values; the "constant latency" approximation frays and the beam picks up aberration.

**Paraxial propagation / diffraction.** A Gaussian beam spreading as it travels obeys a diffusion-like equation: the transverse profile diffuses along the propagation axis. The whole point is that this one equation governs refraction, focusing, and interference across wildly different platforms.

*Analogy:* a **Gaussian pulse broadening as it runs down a dispersive fiber** — group-velocity dispersion spreads the packet exactly as diffraction spreads a beam. Mack, this is the transfer-function/pulse-broadening picture you already carry.
*Breaks when:* the medium is strongly nonlinear or the "paraxial" (small-angle) assumption fails — then the simple second-derivative diffusion no longer captures the dynamics.

**Phase imprinting = optical elements.** In real optics a prism adds a *linear* phase across the beam (steering it) and a lens adds a *quadratic* phase (focusing it). Here the same phases are written across the $n$-axis: the pump phase gives a linear ramp (prism), and the cavity's self-Kerr nonlinearity gives a quadratic profile (lens).

*Analogy:* **phased-array beam steering vs. radar pulse compression.** A linear phase ramp across array elements steers the beam (prism); a quadratic phase — a chirp — followed by propagation compresses a broad packet to a narrow spike, which is exactly matched-filter pulse compression (lens).
*Breaks when:* you try to dial in an *arbitrary* phase profile. The linear phase is freely programmable via the drive, but the quadratic "lens" comes from a genuine Hamiltonian nonlinearity (Kerr), so you only get the phase profiles the physics offers — and higher-order Kerr ($K_6$) adds real optical-style aberration.

**Central analogy for this paper:** *the Fock-amplitude profile is a beam; elapsed time is the propagation distance.*

---

## 4. Core Technical Explanation

The engine of the whole paper is one substitution. The Schrödinger equation for the amplitudes $c_n$ under a weak drive, in the large-$n$ limit, becomes a discrete diffusion equation; smoothing it into a continuous envelope yields the paraxial form. The correspondence they extract is:

$$
\xi \to n,\qquad \zeta \to t,\qquad D \to \sqrt{\bar n}\,\varepsilon_{\mathrm p}
$$

Symbol definitions:
$\xi$ : the transverse (across-the-beam) coordinate in optics → replaced by photon number $n$.
$\zeta$ : the propagation axis in optics → replaced by elapsed time $t$.
$D$ : the diffusion coefficient (how fast the beam spreads) → set by $\sqrt{\bar n}\,\varepsilon_{\mathrm p}$.
$\bar n$ : mean photon number ($\approx 150$ in most experiments here).
$\varepsilon_{\mathrm p}$ : strength of the weak single-photon pump (0.88 MHz in the device).

What this actually means: **letting the state evolve in time is literally "propagating the beam a distance."** The pump strength sets how fast the number-distribution diffuses, the way a fiber's dispersion sets how fast a pulse broadens. Turn the pump off ($\varepsilon_{\mathrm p}=0$) and the beam freezes in place — you can then write a phase onto it without it moving, i.e., insert an optical element, and resume propagation.

With that, each demonstration is a swapped-in element:

**Free propagation & prism (Fig. 2a–d).** A coherent $\bar n=150$ Gaussian either drifts straight (pump phase $\phi_p=0$, "free space") or refracts — its center marches linearly in $n$ — when $\phi_p=\pi/2$. The pump phase imprints $c_n\to c_n e^{in\phi_p}$, a linear ramp = a momentum kick = beam steering.

**Lens (Fig. 2e–k).** Free evolution under the self-Kerr accumulates a *quadratic* phase centered at $n=150$ (detuning $\Delta_L$ is tuned to place the vertex there). A subsequent pump then propagates the chirped state and it focuses — the broad $\sigma\approx12$ Gaussian collapses toward a narrow spike. This is matched-filter pulse compression in the number basis. They report 17% population landing in |150⟩, versus 2.2% for |100⟩ in prior work.

**Time-reversed / concave lens.** Set $\phi_p=\pi$ and the sign of the diffusion term flips. Because Schrödinger evolution is time-reversal symmetric under complex conjugation, this runs the propagation *backward* — a converging lens becomes diverging. The authors flag this as having no direct classical counterpart, and it's the most physics-flavored trick in the paper: you're exploiting the conjugation symmetry of QM to get a negative-index-like element for free.

**Newton's prism / dispersion (Fig. 3).** The pump frequency plays the role of "color." Different detunings $\tilde\Delta$ impose different linear ramps, so the final focal photon number lands at $n\approx\bar n+\Delta/K_4$. Sweep the frequency, sweep the focus — a spectrometer entirely inside the number axis (focus to $n=140$ or $n=160$ from a $\bar n=150$ input).

**Young's double slit (Fig. 4).** They prepare a double-Gaussian state — two narrow peaks at $n_1,n_2$ with controllable relative phase $\theta$ — using a clever "phase-space slingshot" (prepare a small, low-photon squeezed-cat near the origin with GRAPE, then displace it up to $n\approx150$, sidestepping the intractability of direct high-$n$ preparation). Under propagation the peaks diffract and interfere; fringe spacing goes as $1/d$ (Fourier reciprocity — wider slit separation, finer fringes), and $\theta$ slides the pattern over $2\pi$. A deliberately *incoherent* mixture shows no fringes — the coherence control experiment.

**Imaging (Fig. 5).** Two propagation segments sandwiching a lens, obeying the thin-lens relation $1/t_u+1/t_v=1/t_f$, produce an inverted, magnified copy of an arbitrary input distribution. This is the headline capability claim: a single physically-motivated pulse sequence performs a unitary over a large Hilbert space that would otherwise demand optimizing thousands of GRAPE parameters. Cosine similarity to the ideal: 84% and 90%.

**Detection — the "Fock-space camera."** Number-splitting: a large cavity population shifts the ancilla qubit's frequency by $\approx n\chi$, so a frequency-selective π pulse reads out population in a chosen $|n\rangle$. Calibrated $|0\rangle$ through $|180\rangle$. This is the readout backbone that makes all the "photographs" of the beam possible.

**Assumption Audit.**

**Watch:** The reader likely assumes the focusing lens *deterministically prepares the pure Fock state* |150⟩. The paper actually delivers a narrow *Gaussian bump* in number (a strongly photon-number-squeezed state, $\sigma=1.26$), and "17% success for |150⟩" is the population in that single rung after a projective confirmation — corrected for readout it's ~21%. It's a squeezed distribution, not a clean number eigenstate.

**Watch:** The reader likely assumes "weak pump ⇒ linear optics, no nonlinearity involved." In fact the *propagation* is the linear (diffusive) part, but the *elements* — lens and dispersion — are manufactured from the cavity's self-Kerr nonlinearity plus detuning. The medium is genuinely nonlinear; only the beam transport is linear.

**Watch:** The reader likely assumes the optics analogy is exact. It is an approximation valid only for $n\gg1$ (uniform hopping) and for broad-$n$/narrow-$k$ distributions (the paraxial small-angle step $\cos k\approx1-k^2/2$). Push toward the vacuum boundary or toward very narrow distributions and the mapping degrades.

**Watch:** The reader likely reads "scalable control of large quantum states" as "universal control." The toolbox realizes the specific class of transformations expressible as linear/quadratic phases plus diffusion. That's a powerful but bounded set — arbitrary unitaries over the giant Hilbert space are not claimed to be efficiently reachable this way.

---

## 5. What's Genuinely New or Clever

The load-bearing insight is the *reframing itself*: recognizing that weak-drive single-mode evolution in the large-$n$ limit is formally the paraxial wave equation, which converts high-dimensional state engineering from a numerical optimization problem into an intuitive optical-design problem. You reason with rays and lenses, then read off a pulse sequence — no full Schrödinger solve. That's new to the field as a *systematic experimental toolbox*, even though the ingredient dualities (synthetic dimensions, space-time duality, Fock-state lattices) were each individually known.

The second genuinely clever piece is the **time-reversed concave lens** via pump phase $\phi_p=\pi$, exploiting QM's conjugation symmetry to flip the diffusion sign — a "negative element" with no classical counterpart. Honorable mention to the **phase-space slingshot** for double-Gaussian preparation, which is a neat practical dodge around the intractability of directly building high-$n$ superpositions.

Distinguishing new-to-reader vs. new-to-field: waveguide-array discrete diffraction and synthetic dimensions are old news to the community; the *demonstrated 180-photon optical toolbox in circuit QED, plus the efficiency and imaging results*, is the new-to-field contribution.

---

## 6. Limitations & Open Questions

The measured lifetime of |150⟩ is 4.8 μs, worse than the 11 μs predicted by the naive $T_1(n)=T_1(1)/n$ scaling, attributed to transmon dressing / possible ionization draining energy. **(A) Consensus** — decoherence at large $n$ is the acknowledged ceiling and the mechanism is explicitly discussed. *(paper §V.C)*

The focal-point fidelity is limited by readout ($\sim$80%) and the shortened lifetime, so the "17%" is as much a detection-and-decoherence number as a physics number; the true focal population is inferred, not directly clean. **(A) Consensus** — standard caveat for high-$n$ circuit-QED readout, acknowledged. *(paper §V.C)*

The scheme fundamentally requires $n\gg1$ and paraxial (broad-$n$) conditions; it offers no help in the low-photon regime where the couplings are non-uniform. **(B) Contested** — whether this is a "limitation" or simply the intended operating regime is a matter of framing, but it does bound applicability. *(analyst inference / paper §II)*

Imaging is scored by cosine similarity (84–90%), which is a fairly forgiving metric — it's insensitive to certain phase errors and to normalization, so it likely overstates fidelity relative to something like state overlap or a Wigner-based measure. The magnification also came out low (1.26–1.27 vs. expected 1.36). **(C) Speculative** — the paper doesn't foreground this; I'm inferring that the metric flatters the result and that the magnification shortfall hints at unmodeled aberration. Verify against the SM's own error analysis. *(analyst inference)*

The headline scalability (thousands of photons, >27 dB sensing) is *projected* from the demonstrated 180-photon results, not measured; the companion 10,000-photon paper is from the same group. **(A) Consensus** — extrapolation clearly labeled as such in the paper. *(paper Discussion)*

The toolbox is not shown to be universal — it realizes a specific transformation class. Whether adding "mirrors, gratings, metasurfaces" (their forward-looking list) genuinely extends this toward universal control, or just adds more special-case elements, is open. **(C) Speculative** — my read; a controls theorist may already know reachability results here. *(analyst inference)*

Twelve-to-twenty-four-month follow-ups I'd expect: independent reproduction in another cavity platform; pushing the demonstrated (not projected) photon count; a rigorous fidelity metric for the imaging unitary; and a controls-theory characterization of exactly which state transformations the optical toolbox can and cannot reach efficiently.

---

## 7. Detailed Summary & Explanation

I adapted the section order only lightly — grouping the five optical elements thematically in Section 4 rather than marching through the paper's figure order — because the physics is clearer as "one duality, then five swapped-in elements" than as a figure-by-figure recount. The honesty checkpoints are all present and unmodified.

The paper's core claim is that a single microwave cavity, driven weakly, evolves its photon-number amplitudes according to the same equation that governs a light beam spreading through space. Concretely: the strength of coupling between neighboring photon-number rungs grows with the square root of the photon number, and that square-root dependence is what has historically made large-photon control awkward. But once you are working with many photons, that coupling flattens into a constant, and constant nearest-neighbor coupling is exactly what a uniform optical lattice provides. The upshot is that the mean photon number behaves like the position of a beam, letting the state evolve in time is the same as letting the beam travel a distance, and how fast the number-distribution spreads is set by the pump strength.

From there the authors show they can insert the standard optical elements by writing phase patterns across the photon-number axis. A phase that increases linearly with photon number steers the "beam" (a prism, producing refraction — the mean photon number drifts). A phase that increases quadratically focuses it (a lens — a broad distribution compresses to a narrow one), and here that quadratic phase is supplied by the cavity's intrinsic Kerr nonlinearity. Reversing the sign of the pump phase runs the evolution backward and turns a focusing lens into a defocusing one, a move that leans on quantum mechanics' time-reversal symmetry and has no ordinary optical equivalent. Tuning the drive frequency shifts where the beam focuses, reproducing Newton's demonstration that a prism sorts colors — here, drive frequency maps to output photon number. Preparing two narrow number-peaks and letting them spread reproduces Young's double-slit interference, complete with fringes whose spacing shrinks as the peaks separate and whose position tracks the relative phase; scrambling that phase erases the fringes, confirming the effect is genuinely coherent. Stacking a lens between two propagation stages builds an imaging system that inverts and magnifies an arbitrary input distribution in one physically-motivated shot.

The practical takeaways: they controlled these effects with up to 180 photons; they focused a 150-photon coherent state into a distribution barely more than one photon wide, roughly a tenfold squeezing of the number spread, which in turn implies a large sensing advantage (about 19.7 dB below the standard quantum limit for detecting tiny displacements); and they reached the 150-photon target with an order-of-magnitude better efficiency than prior methods. The reason to frame the story around the single duality — rather than five separate tricks — is that the whole value proposition is that one change of perspective replaces a lot of expensive numerical optimization with design-by-intuition.

The key interpretive choice a reader should hold onto: the "success" numbers and the focused state are real but qualified. The focused state is a squeezed number-distribution, not a pure Fock state, and the efficiency and fidelity figures are entangled with readout and decoherence at large photon number. The physics is clean; the metrology numbers are promising single-group results that want independent confirmation.

**Where I'm least confident in this analysis:** the exact quantitative fidelity of the imaging demonstration. Cosine similarity is a lenient metric and I flagged (speculatively) that it likely flatters the result, but I did not independently reconstruct what a stricter overlap measure would give from their data, and the magnification shortfall (1.26 vs. 1.36) may encode a systematic I'm not fully diagnosing rather than mere noise. A reader wanting to trust the imaging claim quantitatively should dig into SM Sec. V/VI directly.

---

## 8. Three Crystallized Takeaways

1. **They turned a photon counter into an optical bench.** By calling "photon number" a position and "time" a distance, a single cavity's quantum state propagates like a light beam — so you can build a prism, lens, spectrometer, and double-slit out of nothing but that one mode's amplitudes.

2. **Design-by-intuition beats brute-force optimization for a whole class of tasks.** Instead of numerically hunting for control pulses over thousands of parameters, you sketch the optical system you want and read off the sequence — and they used it to make a 150-photon squeezed state ten times more efficiently than before.

3. **Quantum mechanics gives you a lens with no classical twin.** Flipping the drive phase runs the "beam" backward in time, converting a focusing lens into a defocusing one — a free consequence of the time-reversal symmetry of the Schrödinger equation.

---

## 9. Shorter Summary

Controlling quantum states of light inside a cavity gets rapidly harder as you add photons, because the standard methods rely on numerically searching for control pulses over an enormous space of possibilities. This paper sidesteps that wall with a change of perspective. It treats the photon number — how many photons are in the cavity — as if it were a position along a line, and time as if it were distance traveled. Under a weak drive and with many photons present, the cavity's quantum state then spreads and evolves according to exactly the same equation that describes a beam of light diffracting through space.

Once that equivalence is in hand, the entire toolbox of classical optics becomes available. Writing a phase that grows steadily across the photon-number axis steers the "beam" like a prism; a phase that grows quadratically focuses it like a lens (supplied here by the cavity's natural nonlinearity); reversing the drive phase runs the evolution backward and flips a focusing lens into a defocusing one — a trick with no everyday optical counterpart. Tuning the drive frequency reproduces Newton's color-sorting prism, and preparing two narrow peaks reproduces Young's double-slit interference, fringes and all. Stacking these elements builds an imaging system that inverts and enlarges an arbitrary state in a single step.

Experimentally, the team controlled these effects with up to 180 photons in a superconducting microwave cavity. Their optical "lens" squeezed a 150-photon state into a distribution only about one photon wide — roughly a tenfold tightening — which translates into a substantial sensitivity gain for detecting tiny signals, and they hit the target far more efficiently than earlier approaches.

The honest caveats: the focused state is a very narrow spread of photon numbers, not a perfect single number; the efficiency and fidelity figures are entangled with readout imperfections and with faster-than-hoped decoherence at high photon number; the impressive scaling to thousands of photons is projected, not yet measured; and this is one group's result awaiting independent replication. The idea is elegant and well-grounded — an intuitive, scalable path for sculpting large quantum states — with the specific numbers still earning their confidence.

---

Want me to go deeper on any piece — the derivation of the uniform-hopping approximation and where it fails, the time-reversal/concave-lens mechanism, or the metrology claim (how $\sigma=1.26$ becomes 19.7 dB below the SQL)?

## Human

This sounds very interesting but I'm going to need lots of explanation. Start with thisFock space and the coherent state. A cavity mode's state is a stack of amplitudes c n over photon-number rungs |n rangle. A coherent state (what a classical-looking drive produces) has a Poissonian spread over n; when the mean bar n is large, that Poissonian is essentially a Gaussian bump centered at bar n with width the square root of bar n.

## Assistant

Explaining

Let's build this from the ground up. There are really four ideas stacked on top of each other here — the oscillator and its rungs, the amplitude stack, what makes a state "coherent," and why that state is Poissonian-then-Gaussian. I'll take them in order.

## The cavity mode is one quantum harmonic oscillator

A "cavity mode" or "bosonic mode" is a single electromagnetic mode — one frequency, one standing-wave pattern in the box. Quantum-mechanically, that mode is a harmonic oscillator, and a harmonic oscillator has evenly spaced energy levels. Each level corresponds to a definite number of photons: zero photons (the vacuum), one photon, two, and so on. Those definite-number states are the **Fock states** $|n\rangle$, and because they're energy eigenstates they're the natural "rungs of a ladder."

*Analogy:* think of it as a **register whose value is the photon count** — a hardware counter that can hold 0, 1, 2, … excitations, where each increment costs exactly one quantum of energy $\hbar\omega$.
*Breaks when:* you take the register metaphor too literally and imagine the mode is *in* one definite value at all times. A register always holds a specific integer; a quantum mode can be in a blend of many counts at once, which is the whole next point.

## Any state is a stack of complex amplitudes over the rungs

The mode doesn't have to sit on one rung. In general it's a superposition — a weighted stack across all the rungs at once:

$$|\psi\rangle = \sum_n c_n\,|n\rangle$$

Symbol notes: $|n\rangle$ is the state with exactly $n$ photons; $c_n$ is a **complex** number, the amplitude on rung $n$.

Two things about $c_n$ are worth separating carefully, because the paper leans on both:

The **magnitude** $|c_n|^2$ is the probability of finding exactly $n$ photons if you measured. Those are real, non-negative, and sum to 1 — an ordinary probability distribution over photon number. This is the "intensity profile" in the optics analogy.

The **phase** $\arg(c_n)$ is the extra quantum information — a rung can carry the same probability but a different phase. That phase is invisible to a plain photon-counting measurement, but it governs how the amplitudes interfere when the state evolves. In the paper's language, the magnitudes are the beam's brightness and the phases are its **wavefront**.

*Analogy:* the state is a **complex-valued array indexed by $n$** — like a spectrum or a phasor histogram, where each bin has both a height (probability) and an angle (phase). Mack, this is exactly the amplitude-and-phase pair you'd carry through a DFT bin.
*Breaks when:* you treat the array as classical data you can freely read out. You can't read all the $c_n$ from one copy of the state — a measurement collapses it. The array is a description of the amplitudes, not a buffer you can peek at losslessly.

## The coherent state: what a "classical-looking" drive produces

Now, a specific state. If you drive the mode with an ordinary classical signal — a microwave tone into the cavity — you don't get a Fock state. You get a **coherent state** $|\alpha\rangle$, which is the closest a quantum oscillator comes to behaving like a classical oscillating field with a well-defined amplitude and phase. It's the state of a laser beam, or of the field in your driven cavity.

The defining property is subtle but illuminating: a coherent state is an **eigenstate of the annihilation operator**, $\hat a|\alpha\rangle = \alpha|\alpha\rangle$. In words: *remove one photon and the state is unchanged* (up to the number $\alpha$).

*Analogy:* a **laser beam is so many photons deep that plucking one out changes nothing** — the field looks identical. That "robust to losing a quantum" property is what makes a coherent state feel classical.
*Breaks when:* you scale down to a near-vacuum coherent state ($\bar n \sim 1$). Then removing a photon is a big fractional change, the "classical field" picture gets shaky, and the state's quantum graininess dominates.

The number $\alpha$ is complex: its magnitude sets the amplitude, its angle sets the phase of the oscillating field. The paper writes $\alpha=\sqrt{\bar n}$, meaning they've chosen the phase to be zero and $\bar n = |\alpha|^2$ is the mean photon number.

The word **coherent** is doing real work: it means the amplitudes $c_n$ across the rungs have a *fixed, definite phase relationship* to one another. That locked phase relationship is what lets a coherent state interfere cleanly — and it's precisely what the paper's double-slit experiment tests (scramble the phase relationship into a statistical mixture, and the interference fringes vanish).

## Why the photon-number spread is Poissonian

Here's the shape of the bump. For a coherent state, the probability of finding exactly $n$ photons follows the **Poisson distribution**:

$$P(n) = e^{-\bar n}\,\frac{\bar n^{\,n}}{n!}$$

Symbol notes: $\bar n$ is the mean photon number; $P(n)$ is the probability of counting exactly $n$.

The reason it's Poisson is the deep part. A coherent state's photons behave like **independent random arrivals at a fixed average rate** — each photon "decides" to be there independently of the others. The count of independent events at a fixed rate is *always* Poisson-distributed. This is the same math as radioactive decay counts in a fixed window, or packets landing on a network interface at a steady average load, or photon shot noise on a detector.

*Analogy:* **shot noise.** A coherent state is the quantum-optics embodiment of shot noise — photons sprinkled independently, so the count fluctuates Poissonian-style around the mean.
*Breaks when:* the light is nonclassical. Squeezed or Fock states have *sub-Poissonian* counts (narrower than shot noise) or *super-Poissonian* (bunched). The Poisson shape is special to coherent states; it's the dividing line, not a universal rule. The paper's whole metrology payoff is beating this shot-noise width.

A hallmark of Poisson worth burning in: **mean equals variance.** So for a coherent state, the variance in photon number is also $\bar n$, and the standard deviation — the width of the bump — is $\sqrt{\bar n}$.

## Why it's a Gaussian bump at large $\bar n$, with width $\sqrt{\bar n}$

Poisson with a small mean is lopsided and spiky (at $\bar n = 0.5$ it's nothing like a bell curve). But as the mean grows, the Poisson distribution smooths into a **Gaussian** — this is the de Moivre–Laplace / central-limit behavior. By $\bar n = 150$ it's essentially a clean bell curve.

So the coherent state at large $\bar n$ is a Gaussian bump on the photon-number axis:

- **centered** at $\bar n$,
- with **standard deviation** $\sqrt{\bar n}$.

Plug in the paper's number: $\bar n = 150 \Rightarrow \sqrt{150} \approx 12.2$. So their input "beam" is a Gaussian sitting at rung 150, about 12 rungs wide, effectively spanning roughly rungs 114–186 (three sigma each way). *That* is the "Gaussian beam" they later squeeze down to a width of 1.26 with their Fock-space lens.

There's one more scaling fact that's the quiet hero of the whole field. The **absolute** width grows like $\sqrt{\bar n}$, but the **relative** width shrinks:

$$\frac{\text{width}}{\text{mean}} = \frac{\sqrt{\bar n}}{\bar n} = \frac{1}{\sqrt{\bar n}}$$

*Analogy:* this is the **shot-noise SNR law** you already know cold — signal $\propto N$, noise $\propto \sqrt N$, so signal-to-noise $\propto \sqrt N$, and relative fluctuation falls as $1/\sqrt N$. It's the same reason averaging $N$ samples tightens your estimate by $1/\sqrt N$.
*Breaks when:* you read "relative width shrinks" as "it becomes classical/exact." It never gets to zero — there's always a $1/\sqrt{\bar n}$ residual quantum fuzz. That residual is the standard quantum limit, and the entire point of the paper's squeezing is to punch below it.

## Landing it back on the paper

Put together: a classical drive gives you a coherent state; at large $\bar n$ that's a Gaussian bump of amplitudes on the photon-number axis, centered at $\bar n$, width $\sqrt{\bar n}$, with a locked phase relationship across the rungs. The paper reinterprets that bump as a **Gaussian beam** living on a synthetic spatial axis (the axis *is* the photon number), the phase relationship as the beam's **wavefront**, and then does optics to it.

And now you can see *why they work at $\bar n = 150$ specifically*, not at small photon number: only at large $\bar n$ does the Poisson turn Gaussian (so it looks like a real beam), does the neighbor-to-neighbor coupling flatten into "free space," and does the bump sit far enough from the vacuum wall at $n=0$ that the beam has room to propagate, refract, and focus without slamming into the boundary.

Want me to go next into *why the coupling between rungs flattens at large $\bar n$* — the $\sqrt{n+1}\approx\sqrt{n}$ step that turns this stack of amplitudes into a genuine propagating beam — or would you rather I stay on coherent states a bit longer, say the phase-vs-number tradeoff and what "squeezing" the bump actually costs you?

## Human

Explain Paraxial propagation / diffraction. A Gaussian beam spreading as it travels obeys a diffusion-like equation: the transverse profile diffuses along the propagation axis. The whole point is that this one equation governs refraction, focusing, and interference across

## Assistant

Explaining

This is the load-bearing physics of the whole paper, so let me build it in layers: first *why a beam spreads at all* (the real mechanism), then *the one equation that captures it*, then the crucial detail that makes it a **wave** diffusion rather than plain heat-smearing, and finally *why that single equation delivers refraction, focusing, and interference for free*.

## Why a beam spreads at all: the angular spectrum

Start with the deepest "why," because everything else is bookkeeping on top of it. Take a beam traveling along $z$ with some finite transverse profile in $x$ — say a bright stripe of width $w$. Decompose that profile into plane waves, each traveling at a slightly different angle. This is just a **spatial Fourier transform**: a narrow stripe in $x$ requires a *broad* spread of transverse wavevectors $k_x$ (angles), and a wide stripe requires a narrow spread. Standard time-bandwidth reciprocity, moved into space.

Now let those angled plane waves propagate. Each one heads off in its own slightly-different direction, so after some distance $z$ they no longer overlap as tightly as they did at the start — the profile smears out. **That fan-out of angles is diffraction.** A beam spreads *because* confining it transversely forced a spread of directions, and directions diverge.

*Analogy:* it's the **spatial twin of an uncertainty relation** — pin the beam down in position (narrow $w$) and you pay with a wide spread in transverse "momentum" (angle $k_x$), which then unavoidably widens the beam downstream. Mack, this is the same $\Delta x\,\Delta k \gtrsim 1$ bookkeeping as time-bandwidth product in a pulse.
*Breaks when:* the angular spread gets large — a beam focused to near a wavelength has components at steep angles, some of which become evanescent (don't propagate at all). Then the tidy Fourier-of-angles picture and its small-angle approximation both fail. That's the boundary of "paraxial."

The immediate consequence, worth burning in: **narrow beams spread fast, wide beams spread slowly.** A tight waist has a broad angular spectrum, so it diverges quickly; a fat beam is nearly collimated. Same reciprocity, restated — and it's exactly why the paper's *narrow* double-Gaussian peaks ($\sigma=5$) diffract strongly enough to overlap and interfere.

## The one equation

If you keep only small angles (the **paraxial approximation** — the beam's spread along $z$ is slow compared to its transverse structure), the full wave equation collapses to a single clean statement:

$$
i\,\frac{\partial E}{\partial z} = -\frac{1}{2k}\,\frac{\partial^2 E}{\partial x^2}
$$

Symbol definitions:
$E(x,z)$ : the beam's complex envelope — amplitude *and* phase of the field across the beam.
$z$ : the propagation axis (how far the beam has traveled).
$x$ : the transverse coordinate (position across the beam).
$k = 2\pi/\lambda$ : the wavenumber; large $k$ (short wavelength) means slow spreading.

What this actually means: **the rate of change along the direction of travel is set by the transverse curvature of the profile.** Where the profile is sharply peaked (large second derivative), it changes fast — it wants to flatten. This is structurally a **diffusion equation**: the second spatial derivative is the same operator that spreads heat through a metal bar or smears a concentration gradient. The coefficient $1/2k$ plays the role of a diffusion constant — small wavelength, small "diffusivity," slow spread.

*Analogy for Mack:* propagation is a **quadratic-phase all-pass filter in the angle domain.** Fourier-transform the profile into its angular spectrum, multiply every component by a phase that grows as the *square* of its angle, transform back. No amplitudes are touched — it's pure phase, a dispersive transfer function — but that quadratic phase dephases the components and blurs the profile. In the position domain the same operation is a **convolution with a chirp kernel** (Fresnel propagation), which is precisely the chirp you'd recognize from radar pulse compression.
*Breaks when:* you leave small angles. The exact phase per angle is $\sqrt{k^2 - k_x^2}$; the paraxial equation keeps only the first quadratic term of that square root. Steep angles need the full expression, and the diffusion form no longer holds.

## The imaginary $i$ is the whole story

Here's the detail that separates optics from a heat bar, and it's the single most important thing in this explanation. The heat equation has a real coefficient; this one has an **$i$** out front. That $i$ changes the character completely:

- **Heat diffusion** (real coefficient) is irreversible and dissipative — gradients smooth out, energy spreads and is lost, and you can never run it backward. Sharp features decay away permanently.
- **Wave/paraxial diffusion** (imaginary coefficient) is **reversible and lossless** — the profile spreads, but no energy is destroyed, and the process oscillates. The $i$ turns "monotone smearing" into "phase evolution," which means components can spread *and then come back into phase and constructively add elsewhere.*

That reversibility-plus-oscillation is exactly where **interference** lives. A pure heat equation could never produce a fringe pattern; the $i$ is what lets two overlapping beams reinforce here and cancel there instead of just averaging into mush.

*Analogy:* this is the **Schrödinger equation wearing an optics costume.** Line them up: $i\,\partial\psi/\partial t = -(\hbar/2m)\,\partial^2\psi/\partial x^2$ for a quantum particle. Map $z \leftrightarrow t$ and $k \leftrightarrow m/\hbar$, and a spreading light beam *is* a spreading quantum wavepacket. A tightly focused beam diverges fast for the same reason a tightly localized electron's wavefunction disperses fast — light wavelength $\leftrightarrow$ particle mass.
*Breaks when:* you push the particle analogy to include a potential or measurement. Free-space paraxial optics matches only the *free-particle* Schrödinger equation; add a lens (a potential term) and the correspondence holds, but there's no optical analog of wavefunction collapse.

There's a second twin worth naming because the paper uses it explicitly: **space–time duality.** Run the *same* equation with $x$ reinterpreted as *time* and it describes a **short pulse broadening as it travels down a dispersive fiber** — group-velocity dispersion. Diffraction in space and dispersion in time are the same math. You already carry the fiber-pulse-broadening intuition; a diffracting beam is that, rotated into a spatial axis.

## The Gaussian beam: the clean solution

Feed a Gaussian profile into this equation and something tidy happens: **it stays Gaussian forever.** Only two things change as it propagates — its **width grows** and its **wavefront curves.**

Near the waist (the narrowest point) the beam is nearly flat and barely spreading. Past a characteristic distance — the **Rayleigh range**, set by how tight the waist is — the width starts growing roughly linearly with distance, fanning out into a cone whose half-angle is the divergence you'd predict from the angular spread. Tight waist → short Rayleigh range → wide cone. Fat waist → long Rayleigh range → nearly collimated. (Same reciprocity, third time — it's genuinely the backbone of the subject.)

The wavefront curvature is the other half. At the waist the wavefront is flat; downstream it bulges into a spherical curve, as if the light were emanating from a point back at the waist. That curvature is a **quadratic phase across $x$** — hold onto this, because it's the exact thing a lens manipulates.

## Why *one* equation gives refraction, focusing, and interference

This is the payoff, and it comes from two facts: the equation is **linear**, and "optical elements" are just **phase patterns** you stamp across the beam. Because propagation faithfully carries any phase you imprint, you get every element by choosing the phase's shape:

**Refraction / a prism = a linear phase ramp.** Stamp a phase that grows steadily across $x$ — $E \to E\,e^{i\,k_0 x}$. In the angle domain that's a rigid shift of the whole angular spectrum: you've kicked every component's direction by the same amount, so the beam **tilts and its center drifts sideways as it propagates.** A boundary between two media does exactly this (that's Snell's law); so does a prism. One linear phase, and the equation turns it into steady deflection.

*Analogy:* **phased-array beam steering** — a linear phase gradient across the emitters points the beam. Identical operation, identical result.

**Focusing / a lens = a quadratic phase.** Stamp a phase that grows as $x^2$ — $E \to E\,e^{-i\,\phi_0 x^2}$. This is the *inverse* of the curvature that free propagation builds up, so it pre-curves the wavefront to converge. Propagate afterward and the beam **contracts to a focus**, then re-expands. Flip the sign and it diverges (a concave lens).

*Analogy:* **matched-filter pulse compression.** A quadratic phase is a chirp; propagation is the matched filter that collapses the chirped, spread-out packet into a narrow spike at the focus. This is *precisely* the mechanism behind the paper's Fock-space lens squeezing a 12-wide coherent bump down to width 1.26.

**Interference = linearity plus the $i$.** Because the equation is linear, if two beams are each solutions, their sum is too. Send in two overlapping beams and the measured intensity is $|E_1 + E_2|^2 = |E_1|^2 + |E_2|^2 + 2\,\mathrm{Re}(E_1^\*E_2)$. That last **cross term** — alive only because the amplitudes are complex and the $i$-driven evolution keeps their relative phase meaningful — oscillates between reinforcement and cancellation as position changes. **Those oscillations are the fringes.** No new physics beyond the one linear equation; interference is just what superposition looks like when you square it.

*Breaks when:* the two beams lose a definite relative phase — an incoherent *mixture* rather than a coherent superposition. Then the cross term averages to zero and the fringes vanish. This is exactly the control experiment the paper runs (mixed state → no fringes) to prove its interference is genuinely coherent.

## Landing it back on the Fock-space paper

Now the reinterpretation should feel inevitable. The paper takes this whole apparatus and swaps the axes: the transverse position $x$ becomes the **photon number $n$**, and the propagation distance $z$ becomes **elapsed time $t$**. The diffusion coefficient $1/2k$ becomes $\sqrt{\bar n}\,\varepsilon_p$ — set by the pump strength instead of the wavelength.

So "a Gaussian beam spreading as it travels" becomes "**the photon-number distribution spreading as time passes under a weak drive**." A linear phase across $n$ steers the distribution's center (their prism/refraction). A quadratic phase across $n$ — supplied by the cavity's self-Kerr — focuses it (their lens, the pulse-compression trick). Two number-peaks let time-evolution overlap and interfere them (their double slit). Every optical element you just met has a Fock-space doppelgänger, and the reason is that both live under the *same* paraxial equation — the central analogy holding firm: **the amplitude profile is a beam; time is the distance it travels.**

The one honest asterisk, which the paper depends on and which is your natural next question: this beautiful mapping only holds *because* the rung-to-rung coupling flattens out at large photon number. That flattening — the $\sqrt{n+1}\approx\sqrt{n}$ step — is what promotes a messy quantum stack into a genuine free-space beam.

Want me to take that next: **why the coupling between rungs flattens at large $\bar n$**, turning the photon ledger into "free space"? Or would you rather I go deeper on the lens — the quadratic-phase / chirp-compression mechanism — now that the optics groundwork is in place?
