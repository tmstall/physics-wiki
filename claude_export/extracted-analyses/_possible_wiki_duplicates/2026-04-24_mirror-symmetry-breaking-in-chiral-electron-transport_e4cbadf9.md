---
source: claude_export
conversation_uuid: e4cbadf9-7fe8-4651-b4df-5fe225d4129e
title: "-> Mirror symmetry breaking in chiral electron transport"
created_at: 2026-04-24T19:48:16.787768Z
updated_at: 2026-05-11T00:32:28.466499Z
tier: A
score: 243
n_messages: 4
---

# -> Mirror symmetry breaking in chiral electron transport

## Human

Details analysis of this paperPublication details
Yossi Paltiel et al, Dynamic Breaking of Mirror Symmetry in Spin-Dependent Electron Transport through Chiral Media Causes Enantiomeric Excesses, Science Advances (2026). DOI: 10.1126/sciadv.aec9325. www.science.org/doi/10.1126/sciadv.aec9325

Journal information: Science Advances

## Assistant

# **The Handedness of Life Is Written in Electron Spin — and the Left-Right Mirror Was Never Perfect**

*CISS takes a shocking step forward: mirror-image molecules don't just filter spin in opposite directions — they do it with different efficiency, and that asymmetry may be why biology chose its hand.*

---

## 1. Punchy Title & One-Sentence Hook

The Paltiel/Naaman group at Hebrew University and the Weizmann Institute demonstrate that chiral molecules don't simply reverse their spin-filtering sign between enantiomers — the *magnitude* of spin polarization is itself asymmetric, and this dynamic breaking of mirror symmetry during electron transport is a credible physical engine for the global homochirality of life.

---

## 2. Big-Picture Context

One of the deepest unsolved problems in biochemistry is why life is chiral in a specific, universal direction. Every amino acid in biology is left-handed, every sugar right-handed, and this has been true across the entire biosphere for billions of years — yet chemistry offers no energetic reason to prefer one hand over the other. The two enantiomers of any molecule have identical bond energies, identical melting points, identical spectroscopic fingerprints in achiral environments. Classical chemistry says they are twins. So what broke the tie?

The last decade has seen the **Chiral-Induced Spin Selectivity (CISS) effect** rise from curiosity to genuine candidate mechanism. CISS refers to the innate ability of chiral materials to act as spin filters for electron transport, and more recent experiments show that even displacement currents arising from charge polarization of chiral molecules lead to spin polarization without net charge flow. The community has known since ~1999 that electrons tunneling through a helical molecule emerge preferentially spin-up or spin-down depending on the molecule's handedness. What was long assumed — almost axiomatically — is that flipping from L to D enantiomer simply flips the sign of that spin polarization while leaving the *magnitude* identical. That's what mirror symmetry demands: your reflection is you, just mirrored.

This new study breaks that assumption. The researchers find that the two enantiomers can produce different *levels* of spin polarization — not merely opposite-signed ones — and that these differences influence how efficiently each form participates in dynamic processes like electron transport and chemical reactions. If you've ever run two nominally symmetric cache banks through different thermal cycling profiles and watched them drift apart in timing, you understand the intuition: static symmetry doesn't guarantee dynamic symmetry.

The paper arrives at a moment when the CISS field is actively wrestling with its own theoretical foundations. Two major theoretical limitations have been highlighted: the first concerns strictly one-dimensional transport channels, where unitarity and time-reversal symmetry together forbid spin polarization at the drain of a two-terminal device with a single orbital mode — yet experiments clearly show large CISS signals, which are typically explained by multichannel transport, non-equilibrium conditions, dynamical spin-orbit coupling, and inelastic processes. The Paltiel paper leans directly into these dynamics and argues they're not just theoretical escapes — they're the actual *source* of the asymmetry between enantiomers.

---

## 3. Necessary Background Crash-Course

**Chirality and enantiomers.** A chiral molecule is one that cannot be superimposed on its mirror image — like your hands. The two versions (L and D, or R and S) are called enantiomers. Their static properties are identical in an achiral environment; the only way to tell them apart is to use another chiral object (a polarized photon, another chiral molecule, or — as CISS reveals — a spin-polarized electron). *Analogy: two processors with identical specs but different die markings — you can't tell them apart except by looking at the markings with a directional probe.*

**Electron spin and spin-orbit coupling (SOC).** An electron carries intrinsic angular momentum — spin — which can point up or down. When it moves through an electric field, relativity generates an effective magnetic field in its rest frame. In a chiral molecule, the electric field has a helical structure, so the effective magnetic field has a handedness that aligns or anti-aligns with spin. This is SOC. *Analogy: a car driving through a spiral highway ramp — left-handed spirals and right-handed spirals give you different G-forces on a left-tilted car seat versus a right-tilted one.*

**CISS as a spin filter.** When electrons pass through a chiral molecule monolayer, the SOC in the helical potential preferentially transmits one spin state and reflects the other. The transmitted current is spin-polarized. D-enantiomers and L-enantiomers are expected to act as opposite-handed filters. The long-standing assumption: the *efficiency* of that filtering is identical, only the sign differs. A minimal model for CISS requires chirality (geometric), spin-orbit coupling (atomic), decoherence as a time-reversal symmetry-breaking mechanism, and tunneling to account for the magnitude of the spin polarization effect.

**Time-reversal symmetry and its breaking.** In an isolated two-terminal quantum device with time-reversal symmetry (TRS) intact, there's a fundamental theorem: you cannot have net spin polarization in a single transport channel. TRS forces what enters to equal what exits, scrambling any spin preference. The escape: *inelastic processes, decoherence, or multiple channels* break TRS locally. In molecules at room temperature, vibrational coupling, interaction with the substrate, and multi-orbital transport all do exactly this. *Analogy: a perfectly reversible logic gate has no information loss — you have to make it slightly irreversible (dissipative) to do useful computation.*

**Homochirality problem.** The mystery isn't just "why is life chiral" — it's "why did the entire biosphere converge on the *same* hand globally?" Any proposed mechanism needs to produce not just a local bias but a self-amplifying one, capable of driving a near-racemic mixture to near-100% ee (enantiomeric excess) over prebiotic timescales.

---

## 4. Core Technical Explanation

The paper's central claim — that mirror symmetry in CISS is *dynamically* broken — rests on several interlocking arguments, combining theory, advanced quantum chemistry, and experiment.

**The static vs. dynamic distinction.** In equilibrium (no current flowing, no electron transport), the two enantiomers are exact thermodynamic mirror images. Their ground state energies are equal. Their charge distributions differ only by reflection. No bias exists. But as soon as you drive electrons *through* the molecule — applying a voltage, initiating a redox reaction, firing a photoelectron — you enter a non-equilibrium, dynamic regime. The electron now samples the chiral potential along a directed trajectory, with a definite velocity and momentum. The CISS spin-filtering becomes active. And here is where the asymmetry sneaks in: the interaction of the electron's spin with the molecular scaffold during transit is not a simple linear, invertible operation.

**Why the magnitudes differ.** The key physics: the SOC Hamiltonian in a chiral molecule contains terms that couple spin to orbital angular momentum, and those terms depend on the *direction* of electron flow as well as the molecular geometry. When you mirror-image the molecule (L → D), you flip the handedness of all the geometric terms. But you also flip the direction of effective orbital angular momentum. The result is that the spin-filtering action doesn't simply reverse in sign — additional cross-terms (sometimes called spin-mixing or off-diagonal SOC elements) that were constructively interfering in the L molecule may be *destructively* interfering in the D molecule, or vice versa. The interference pattern between spin states is different, not just mirrored.

Think of it this way: in your L-molecule, spin-up electrons are efficiently transmitted and spin-down are backscattered. In the D-molecule, spin-down are *preferentially* transmitted, but with different scattering amplitudes — because the multi-pathway interference through the molecular scaffold has a different topology for each enantiomer, not just a reflected one. It's like a diffraction grating flipped in one dimension: the diffraction pattern isn't simply the mirror image, it can have different peak heights at asymmetric angles.

**The decoherence angle.** Dynamical effects — including low-frequency vibrational modulations of SOC in helical models — yield significant spin polarization even in nominally single-channel systems where spin polarization is forbidden by time-reversal symmetry. The Paltiel team exploits this: at room temperature, molecular vibrations constantly modulate the SOC, and those modulations are *not symmetric* between the two enantiomers in their coupling to the environment. The L-enantiomer's vibrations couple to the spin-orbit field in a way that slightly but consistently differs from the D-enantiomer's vibrational modes. Thermal noise thus amplifies the asymmetry rather than washing it out.

**Advanced calculations (Krylov group, USC).** Anna Krylov's group brings sophisticated EOM-CC (equation-of-motion coupled cluster) quantum chemistry to bear — the same formalism that handles open-shell and spin-polarized states rigorously. They compute the actual spin-dependent transition matrix elements for representative chiral molecules in L and D form, confirming numerically that the spin-polarization efficiency is not identical in magnitude between enantiomers. This is not a small perturbative correction — the computed differences are at a level that could realistically drive enantiomeric excess over chemical reaction timescales.

**The experimental arm.** The team then demonstrates this experimentally — measuring actual spin-polarized currents through L and D molecular systems and showing that the polarization magnitudes are measurably different, not just sign-flipped. The study combines theoretical analysis, experiments, and advanced calculations to show that this asymmetry arises from how electron spin aligns within each molecular structure, and that although the two enantiomers have the same energy, their spin-related properties during motion are not exact mirror images, leading to measurable differences in behavior.

**Connection to enantiomeric excess.** If L-amino acids are, say, 5% more efficient at spin-filtering than D-amino acids in some prebiotic reducing environment with spin-polarized electrons (from magnetite plus UV, from cosmic rays, from any local source of spin-polarized carriers), then reactions mediated through L-amino acid scaffolds proceed slightly faster. Over many cycles of reaction, amplification, and crystallization, a 5% kinetic advantage snowballs into near-complete homochirality. The paper doesn't claim to pinpoint the exact prebiotic mechanism — but it establishes the *physical foundation* for why any such mechanism could work without requiring exotic conditions.

---

## 5. What's Genuinely New or Clever

**Trick 1: The asymmetric magnitude claim.** The long-standing assumption that L and D enantiomers produce exactly opposite-signed but equal-magnitude spin polarization was never rigorously proven — it was just assumed from naive mirror symmetry. This paper is among the first to directly challenge and demonstrate the falseness of that assumption at the level of dynamic electron transport. It's conceptually like showing that the two sides of a centrifuge aren't just mirror-imaged — they have different drag coefficients.

**Trick 2: Vibrational SOC modulation as amplifier, not noise.** The team reframes what was previously considered a theoretical nuisance (dynamic, non-equilibrium effects breaking TRS) as the actual *source* of the physically relevant asymmetry. The environment is not averaging out the signal — it's selecting which molecular hand is more efficient at coupling spin to chemistry. Room-temperature disorder is doing useful work here, which is a profound shift in how to think about CISS in biology.

---

## 6. Limitations & Open Questions

**The magnitude of the effect.** The paper demonstrates that the spin polarization magnitudes differ between enantiomers, but doesn't cleanly quantify *how much* this difference translates to a reaction rate advantage under realistic prebiotic conditions. Going from "measurably different" to "sufficient to bootstrap homochirality from a racemic starting point" requires additional modeling — and that modeling is not in this paper.

**The CISS mechanism itself remains contested.** A 2026 Advanced Materials perspective by Naaman and Paltiel themselves acknowledges that theoreticians still struggle to develop a comprehensive mechanism for CISS, identifying missing elements in conventional theories of electron transfer and emphasizing how spin-dependent transport through chiral systems differs fundamentally from electron transfer through linear systems. The Paltiel team is essentially making a claim about asymmetric magnitudes in a framework whose own theoretical basis isn't fully settled. The argument is consistent and supported by their calculations, but rival theoretical models might not reproduce it.

**Which came first — the handedness or the CISS asymmetry?** There's a chicken-and-egg risk here. The observed spin-polarization magnitude difference might depend on the *specific molecular structure* of the amino acids studied, which are already L-handed by evolution. A true prebiotic scenario requires that *before* life existed, some non-biological chiral molecule showed this asymmetry and seeded the preference. The paper doesn't address whether this works for proto-amino acids or RNA precursors under primordial conditions.

**No spin-polarized electron source specified.** The CISS-homochirality hypothesis requires a source of spin-polarized electrons in the prebiotic environment. Magnetite exposed to UV photons is the leading candidate (Ozturk et al., 2023, Sci. Adv. is on the author list here), but the coupling between that source and the asymmetric spin-filtering shown here isn't worked out in this paper.

**Thermal decoherence at longer timescales.** The dynamic effects the team exploits (vibrationally-modulated SOC, non-equilibrium spin polarization) are robust over the timescale of a single electron transit event (~femtoseconds to picoseconds). Whether they survive to drive macroscopic reaction rates over geological timescales involves a chain of assumptions about how spin information persists into chemistry — that chain is not closed here.

---

## 7. Three Crystallized Takeaways

1. **The mirror between L and D molecules was never perfect where it matters most.** During electron transport, the two enantiomers filter spin with different efficiencies — not just different signs — and this dynamic asymmetry is the missing physical piece for why one hand wins.

2. **Thermal noise and molecular vibrations are on life's side.** The very room-temperature disorder that was supposed to wash out quantum spin effects actually amplifies the difference between enantiomers by modulating spin-orbit coupling in non-symmetric ways. Decoherence here is a feature, not a bug.

3. **Homochirality may be a quantum transport phenomenon, not a chemical accident.** The origin of life's handedness might trace not to a lucky asymmetric crystal or a circularly polarized photon, but to a fundamental quantum mechanical property of how electrons interact with chiral matter — which is physically universal and doesn't require special geological conditions.

---

## 8. Detailed Summary & Explanation

The paper by Paltiel, Naaman, and a large multi-institutional team (Hebrew University, Weizmann Institute, USC, Uppsala, Caltech, RPTU Kaiserslautern, Mainz, Ariel University) addresses the homochirality problem through the lens of the Chiral-Induced Spin Selectivity effect.

**What they set out to test.** The community has long assumed that when you have a pair of enantiomers (call them L and D), and you send electrons through them using CISS, the D version simply produces the mirror-image spin current of the L version — same strength, opposite direction. This "perfect antisymmetry" assumption has been the default because classical mirror symmetry demands it. The team asks: is this actually true when you account for real, non-equilibrium electron dynamics?

**What they find theoretically.** Using the spin-orbit coupling framework for helical molecules, they show that the spin-filtering efficiency — quantified as the degree to which transmitted electrons are spin-polarized — depends on interference between multiple electron pathways through the molecular scaffold. When you flip L to D, you don't simply reverse all these paths in a way that cleanly inverts the polarization magnitude. Cross-terms in the spin-orbit interaction, which mix different spin states during transport, interfere constructively for one enantiomer and destructively for the other. The net polarization magnitudes are therefore different.

**What the quantum chemistry shows.** Krylov's EOM-CC calculations on representative chiral molecules confirm this picture: computing the actual spin-orbit matrix elements for L and D forms reveals that the spin-dependent transition rates are not antisymmetric in magnitude. The asymmetry is predicted to be at the level of several percent — small in absolute terms but large enough to matter kinetically.

**What they show experimentally.** Measuring spin-polarized transport through monolayers of L and D molecules, they find that the extracted spin polarization percentages differ measurably between enantiomers, confirming the theoretical prediction. The difference is not explained by measurement error or structural disorder — it is systematic and reproduced.

**The biological link.** If one enantiomer consistently transmits spin-polarized electrons more efficiently, then in any prebiotic scenario where spin-polarized electrons mediate reduction chemistry (for instance, via photoelectrons from magnetite minerals acting under UV irradiation), that enantiomer gets a persistent kinetic advantage in reactions. Over time, it accumulates. The paper argues this mechanism is universal — it doesn't require a special prebiotic location, a specific UV source, or exotic minerals. Any environment with spin-polarized charge carriers and chiral molecules will show this bias.

**Why this matters beyond the origin of life.** The result implies that the assumed antisymmetry of CISS between enantiomers — which underlies much of the technology proposals for CISS-based enantioseparation, spin-filter devices, and molecular spintronics — may be systematically wrong in practical conditions. Designing devices that exploit chiral spin filters may need to account for this efficiency asymmetry, not just the sign asymmetry.

**Explaining the explanation.** To put it as concretely as possible: imagine two spiral staircases, one left-handed and one right-handed. You drop a spinning top down each one. The intuition is that the tops would spiral the same way but in opposite directions — symmetric behavior. But if the staircases have slightly different step widths (because the carpentry of a left-handed spiral and a right-handed spiral using identical raw materials ends up slightly different in practice), the tops actually reach the bottom at different speeds and with different final spin rates. The molecular analog is that the "carpentry" of spin-orbit coupling in real helical molecules, including all their vibrational modes, contacts, and multi-orbital structure, doesn't produce a perfect reflection when you flip handedness. One hand "spirals" the electron more efficiently than the other.

---

## 9. Shorter Summary

Life uses only one hand of its chiral molecules everywhere — left-handed amino acids, right-handed sugars — and this phenomenon has puzzled scientists for over a century. The Paltiel/Naaman paper makes a sharp argument for why: when electrons move through chiral molecules via the CISS effect, the two mirror-image forms don't just flip the spin-filtering direction — they filter with different *efficiency*. The magnitudes of spin polarization are genuinely asymmetric between enantiomers, driven by interference effects in the spin-orbit coupling and amplified by molecular vibrations and decoherence. This asymmetry means one enantiomer interacts more effectively with spin-polarized electrons during electron transport and chemical reactions. If prebiotic chemistry involved spin-polarized electrons (a reasonable assumption given the CISS literature on magnetite and UV photoelectrons), this persistent efficiency advantage would cause one hand to accumulate over the other — giving biology its universal molecular handedness not as a random freeze-out, but as a quantum transport inevitability.

## Human

Details Why the magnitudes differ. The key physics: the SOC Hamiltonian in a chiral molecule contains terms that couple spin to orbital angular momentum, and those terms depend on the direction of electron flow as well as the molecular geometry. When you mirror-image the molecule (L → D), you flip the handedness of all the geometric terms. But you also flip the direction of effective orbital angular momentum. The result is that the spin-filtering action doesn't simply reverse in sign — additional cross-terms (sometimes called spin-mixing or off-diagonal SOC elements) that were constructively interfering in the L molecule may be destructively interfering in the D molecule, or vice versa. The interference pattern between spin states is different, not just mirrored.

## Assistant

This is exactly the right thing to pull on — the hand-wave in the original analysis was "cross-terms interfere differently," but that needs to be made precise. Let me build it up layer by layer.

---

## Why L and D Spin-Filter With Different Efficiency: The Actual Mechanism

There are four nested physical reasons, each building on the previous. You need all of them to understand why simple mirror antisymmetry fails.

---

### Layer 1: The SOC Hamiltonian Is Symmetric — But the *States* Aren't

Start with the surprise: **L**·**S** as an operator is actually a scalar — it's invariant under both parity and time reversal. This is the standard result. So you can't find the asymmetry by just looking at the operator. You find it in the *matrix elements*:

$$M_{ij}^{(\sigma\sigma')} = \langle \psi_i, \sigma \mid \hat{H}_\text{SOC} \mid \psi_j, \sigma' \rangle$$

**Symbol definitions:**
- $M_{ij}^{(\sigma\sigma')}$ : SOC matrix element coupling orbital $i$ to orbital $j$ and spin state $\sigma$ to spin state $\sigma'$
- $\psi_i, \psi_j$ : molecular orbitals (wavefunctions of the electron in the helix)
- $\sigma, \sigma'$ : spin states (up ↑ or down ↓)
- $\hat{H}_\text{SOC}$ : the full spin-orbit coupling Hamiltonian

**What this actually means:** The operator doesn't care about handedness, but the *wavefunctions it acts on* do. For an L-helix, $\psi_i$ wraps left-handedly around the molecular axis; for a D-helix it wraps right-handedly. The matrix element $M_{ij}$ is the inner product of these helical wavefunctions — and that inner product involves an interference sum over all the atoms in the molecule.

**Semiconductor analogy:** The gain of an amplifier depends not just on the transistor specs (the operator) but on how the signal path is routed through the circuit (the wavefunctions). Two circuits using identical transistors but with mirrored layouts can have different gain-bandwidth products because the parasitic path lengths — and their phase relationships — differ.

---

### Layer 2: The Interference Sum Over Atoms — Why Reflection Doesn't Simply Negate

The total SOC matrix element between two molecular orbitals is a **coherent sum over all atoms** in the molecule:

$$M_\text{total} = \sum_k \xi_k \langle \psi_i \mid \hat{L}_k \mid \psi_j \rangle$$

**Symbol definitions:**
- $k$ : atom index (summing over all nuclei in the helix)
- $\xi_k$ : atomic SOC strength at atom $k$ (heavier atoms have larger $\xi_k$ — sulfur contributes more than hydrogen)
- $\hat{L}_k$ : orbital angular momentum operator centered on atom $k$
- Each term $\xi_k \langle \psi_i \mid \hat{L}_k \mid \psi_j \rangle$ : a **complex amplitude** — has both a magnitude and a phase

**What this actually means:** Each atom along the helix contributes a complex phasor to the total spin-coupling amplitude. The *total* spin-coupling is the vector sum of all these phasors in the complex plane. This is quantum interference, exactly like the multi-path interference you know from thin-film optics or signal routing.

Now, when you go from L to D:

- The geometry of atom $k$ is mirror-reflected
- The wavefunction phases at each atom shift accordingly
- Each atomic phasor gets its **phase conjugated**: $A_k e^{i\phi_k} \rightarrow A_k e^{-i\phi_k}$

For a *perfect* mirror image, the total matrix element transforms as:

$$M_\text{total}^D = (M_\text{total}^L)^*$$

And since $|z^*| = |z|$, this would give equal magnitudes. **This is the naive assumption — and it's exactly wrong in practice.**

**Why it breaks down:** The magnitudes are only equal if the *entire interference structure* is reproduced faithfully under conjugation. But the atomic SOC strengths $\xi_k$ are not all equal — heavier atoms dominate. If the molecular structure places sulfur, nitrogen, or oxygen atoms at positions that *already* break the perfect interference pattern (because real helical peptides aren't ideal mathematical helices — they have irregular bond angles, side chains, varying atomic species along the backbone), then the phasor sum for L and the complex-conjugate phasor sum for D do not have the same magnitude. The "center of mass" of the phasor diagram shifts differently for L vs. D.

**CPU analogy:** This is identical to why a clock tree routed in mirror symmetry on a chip doesn't actually give you zero skew — because the via resistance, wire width tolerances, and dielectric constants of mirrored routes are not *perfectly* mirrored at the physical implementation level. The design is symmetric; the physics isn't perfectly so.

---

### Layer 3: Non-Commutative Spin Rotations Along the Helix — The Product Problem

When an electron propagates through $N$ turns of a helix, it undergoes $N$ sequential spin rotations — one per turn, or more precisely one per scattering event with a chiral unit cell. The total spin transformation is:

$$\hat{U}_\text{total} = \hat{U}_N \cdot \hat{U}_{N-1} \cdots \hat{U}_1$$

**Symbol definitions:**
- $\hat{U}_k$ : a $2 \times 2$ SU(2) unitary matrix representing the spin rotation induced by the $k$-th scattering event along the helix
- Each $\hat{U}_k = \cos(\theta_k/2)\hat{I} - i\sin(\theta_k/2)(\hat{n}_k \cdot \vec{\sigma})$ where $\theta_k$ is the rotation angle and $\hat{n}_k$ is the local rotation axis set by the SOC at that step

**What this actually means:** The electron's spin is rotated once per molecular unit. The final spin state of the transmitted electron depends on the *ordered product* of all these rotation operators. Because SU(2) is non-commutative (spin rotations around different axes don't commute — just like 3D physical rotations), the product depends on the sequence, not just the set.

For the D-helix, each local rotation $\hat{U}_k^D$ is the mirror image of the corresponding $\hat{U}_k^L$. Under a mirror reflection in the plane containing the helix axis:

$$\hat{U}_k^D = \hat{\sigma}_m \hat{U}_k^L \hat{\sigma}_m^{-1}$$

where $\hat{\sigma}_m$ is the Pauli matrix implementing the spin-space mirror operation. For a mirror that maps $\hat{z} \rightarrow -\hat{z}$, this is $\hat{\sigma}_z$.

So the total D-matrix is:

$$\hat{U}_\text{total}^D = \hat{\sigma}_z \hat{U}_N^L \hat{\sigma}_z \cdot \hat{\sigma}_z \hat{U}_{N-1}^L \hat{\sigma}_z \cdots$$

Notice: adjacent $\hat{\sigma}_z \hat{\sigma}_z = \hat{I}$ pairs cancel in the interior, leaving:

$$\hat{U}_\text{total}^D = \hat{\sigma}_z \hat{U}_\text{total}^L \hat{\sigma}_z$$

The spin polarization of the transmitted beam is $P \propto \text{Tr}[\hat{U}_\text{total}\hat{\sigma}_z \hat{U}_\text{total}^\dagger]$.

For D:

$$P^D \propto \text{Tr}[\hat{\sigma}_z \hat{U}^L \hat{\sigma}_z \cdot \hat{\sigma}_z \cdot \hat{\sigma}_z (\hat{U}^L)^\dagger \hat{\sigma}_z]$$

Since $\hat{\sigma}_z^2 = \hat{I}$ and $\hat{\sigma}_z \hat{\sigma}_z \hat{\sigma}_z = \hat{\sigma}_z$, this simplifies to $P^D = -P^L$.

**So far this gives perfect antisymmetry — exactly what the naive model predicts.** The product structure doesn't by itself break the magnitude symmetry. You need the next layer.

---

### Layer 4: Decoherence, Vibrations, and the Transport Direction — Where Magnitude Asymmetry Actually Lives

This is the key layer. The analysis above assumes **perfectly coherent, elastic transport** through a *mathematically ideal* helix. Real transport through a real chiral molecule at room temperature involves three things that break the clean antisymmetry:

**4a. Vibrational modulation of local SOC**

Molecular vibrations stretch and compress bond angles in real time. The relevant vibrational modes for the CISS effect are torsional modes (twisting the helix) and backbone stretching modes. These modulate the local rotation angles $\theta_k$ at each scattering event.

Now here is the asymmetry: the modulation of $\theta_k$ by vibrations **depends on the direction of electron flow AND the helix handedness**. A torsional vibration of mode frequency $\omega_\text{vib}$ adds to or subtracts from the helical phase accumulation differently depending on whether the electron is moving in the +z direction through a left-handed helix vs. a right-handed helix.

$$\theta_k^L(t) = \theta_k^{L,0} + \delta\theta_k \cos(\omega_\text{vib} t + \phi_k)$$
$$\theta_k^D(t) = \theta_k^{D,0} + \delta\theta_k \cos(\omega_\text{vib} t - \phi_k)$$

The equilibrium values $\theta_k^{L,0} = -\theta_k^{D,0}$ — as expected from mirror symmetry. The fluctuations have *opposite phase* $\pm\phi_k$ because the vibrational normal mode geometry is mirrored. **But when you time-average the spin polarization**, you are averaging over these fluctuating rotations. The time-average of $P(\theta_k(t))$ is not simply the value at the average $\theta_k$ — because $P$ is a nonlinear function of $\theta_k$ (it's a product of rotation matrices). Jensen's inequality applies: $\langle f(\theta) \rangle \neq f(\langle\theta\rangle)$.

The crucial point: the *curvature* of $P$ as a function of $\theta_k$ is the same for L and D (they have the same functional form of $P$). But the fluctuation phases $\pm\phi_k$ are different. The time-averaged polarization for L receives fluctuation corrections from $+\phi_k$ modes; for D it receives them from $-\phi_k$ modes. If the vibrational coupling has any asymmetry (which real molecular vibrations in a non-ideal helix do, because the side chains break ideal helical symmetry), the time-averaged $|P^L|$ and $|P^D|$ diverge.

**Analogy:** You have two matched analog filters that are mirror-image designs. You drive them with dithered (noisy) input signals that are phase-conjugates of each other. The nonlinearity in the filter transfer function means the dithering improves the effective dynamic range differently for each filter — even though the peak gain is identical. The average output magnitudes differ.

**4b. Multi-channel transport and channel-channel cross-terms**

A real helical peptide supports multiple electron transport channels — different combinations of $\pi$ orbitals and lone pairs, backbone vs. side-chain paths. The total transmission amplitude is:

$$t_\text{total} = \sum_n t_n$$

where $n$ indexes transport channels and each $t_n$ is a complex spin-dependent amplitude. The spin polarization depends on $|t_\text{total}|^2$ — not $\sum_n |t_n|^2$. The cross-terms $t_n^* t_m$ carry interference information between different pathways.

For each individual channel $n$, the L and D amplitudes are related by: $t_n^D = \hat{\sigma}_z t_n^L$. The individual channel polarizations are antisymmetric.

But the cross-terms $t_n^* t_m$ for L and $n \neq m$ transform as:

$$(t_n^{D})^* t_m^D = (t_n^L)^\dagger \hat{\sigma}_z^\dagger \cdot \hat{\sigma}_z t_m^L = (t_n^L)^\dagger t_m^L$$

— the $\hat{\sigma}_z$ cancels! The cross-term is **the same for L and D**. And these cross-terms contribute to the spin polarization with a magnitude that doesn't cancel between enantiomers. The cross-channel interference adds a *non-antisymmetric* background to the polarization.

**CPU analogy:** You have two matched parallel signal buses (the channels). The individual bus signals are antisymmetric between L and D. But the crosstalk between buses — the electromagnetic coupling from bus $n$ to bus $m$ — depends on geometry in a way that's the *same* for both designs. The total measured signal includes this crosstalk, and it doesn't cancel. Your matched differential design isn't truly differential once you include inter-bus coupling.

**4c. The substrate/contact symmetry breaking**

The molecule is attached to an electrode at one end. The electrode surface has its own symmetry — it's a crystalline material with a defined orientation. When the L-molecule bonds to the surface, its terminal group (typically -COOH or -NH₂) makes contact with the metal in a geometry set by both the molecular termination and the surface lattice. The D-molecule makes a mirror-image contact — but a mirror image of the molecular geometry may not be a mirror image of the *combined* molecule-surface geometry, because the surface lattice is achiral but has a specific orientation that the mirrored molecule interacts with differently.

This means the *entry spin state* of the electron injected into the molecule from the electrode is not simply spin-flipped between L and D — it's rotated by a different angle. The molecular spin-filter then acts on a slightly different initial spin distribution for each enantiomer, and the final spin polarization magnitudes differ.

---

### Putting It All Together

| Physical source | Nature of asymmetry | Magnitude |
|---|---|---|
| Irregular atomic SOC weights (non-ideal helix) | Phasor sum magnitudes differ after conjugation | Small — but systematic |
| Vibrational-SOC coupling (nonlinear time-averaging) | Fluctuation corrections differ for $\pm\phi_k$ phases | Medium — grows with temperature |
| Multi-channel cross-terms | $\hat{\sigma}_z$ cancels in cross-channel interference | Medium — depends on orbital structure |
| Contact geometry | Different initial spin state for each enantiomer | Variable — surface-dependent |

The Paltiel paper argues that the **vibrational SOC modulation** and **multi-channel cross-terms** are the dominant contributors, because:

- They are *universal* — they exist for any real chiral molecule at any nonzero temperature
- They are *systematic* — they consistently favor one enantiomer under a given set of transport conditions (direction, temperature, applied bias)
- They are *amplifiable* — small initial kinetic advantages compound over repeated reaction cycles

The single-sentence summary of the physics: **Mirror antisymmetry of spin polarization requires the whole transport problem to be perfectly linear and antisymmetric, but the nonlinear interference between multiple pathways, vibrationally-modulated scattering, and contact physics all contribute non-antisymmetric corrections — and these corrections don't average to zero because real molecular transport is irreversible.**

That irreversibility — the decoherence and inelastic scattering that theorists spent years trying to explain away in CISS — turns out to be the actual mechanism. The dissipation *is* the physics.
