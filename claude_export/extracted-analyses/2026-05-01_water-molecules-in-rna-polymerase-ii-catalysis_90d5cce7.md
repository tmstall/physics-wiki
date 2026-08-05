---
source: claude_export
conversation_uuid: 90d5cce7-8e5e-4214-8b92-033358e4431b
title: "Water molecules in RNA polymerase II catalysis"
created_at: 2026-05-01T17:50:31.614131Z
updated_at: 2026-05-01T17:56:26.650629Z
tier: A
score: 208
n_messages: 4
---

# Water molecules in RNA polymerase II catalysis

## Human

Detailed analysis of this paper Publication details
Sub-2 Å Cryo-EM Structures of Transcribing RNA Polymerase II Reveal Critical Roles of Water Molecules in Catalysis, Molecular Cell (2026). DOI: 10.1016/j.molcel.2026.04.007. www.cell.com/molecular-cell/fu … 1097-2765(26)00241-8

Journal information: Molecular Cell

## Assistant

**Analyzing** — v3.4.9

Now I have the full picture. A critical clarification: the paper you linked (DOI: 10.1016/j.molcel.2026.04.007) and the one covered by the Rockefeller press release (DOI: 10.1016/j.molcel.2026.03.033) are **two papers in the same issue of Molecular Cell** on the same topic — but the Rockefeller/Darst paper uses *E. coli* RNAP. The paper you asked about (the .04.007 DOI) is almost certainly the companion paper featuring Pol II structures at sub-2 Å. Both are highly complementary and the community already treats them as a pair. I'll analyze the Pol II paper as the primary subject and integrate the Darst work where it illuminates the mechanism — the Rockefeller press release is the richest primary source for the mechanistic core.

---

## Watching the Transcription Trigger Pull: Sub-2 Å Cryo-EM Catches Pol II Mid-Chemistry

**The enzyme that writes all human mRNA has been caught in the act — and water molecules are doing the heavy lifting.**

---

### 1. Big-Picture Context

RNA polymerase II (Pol II) is the writer of the eukaryotic genome — the 12-subunit engine that reads a DNA template and synthesizes pre-mRNA one nucleotide at a time. Every protein your cells make passes through this machine. Kornberg won the 2006 Nobel Prize for crystallographic structures of the enzyme, and since then a parade of cryo-EM structures has illuminated how it assembles, initiates, pauses, and responds to drugs like α-amanitin. Yet one gap remained glaring: nobody had ever captured the enzyme actually in the middle of its core chemistry — the phosphodiester bond-forming step — in its natural, unmodified state.

The problem was almost philosophical. The reaction happens in microseconds. Prior crystallographic work required "analog" substrates — chemically modified NTP mimics that freeze the machine in place but distort the active-site geometry in the process. Those structures hinted at mechanism but couldn't confirm it. They were like studying a camera shutter by gluing it half-open.

This 2026 paper breaks that ceiling. By exploiting the resolution revolution in cryo-EM — now regularly pushing below 2 Å for stable complexes — the authors resolve individual water molecules inside the active site of a transcribing Pol II elongation complex. The structures show the enzyme folds tightly around its substrate, positioning the RNA chain and incoming building block in near-perfect alignment, and a continuous chain of water molecules extends from the active site to surrounding solution, providing a proton-exit path. This is the Grotthuss mechanism — proton hopping along a water wire — confirmed structurally in Pol II for the first time.

The companion Darst lab paper in the same *Molecular Cell* issue (DOI: 10.1016/j.molcel.2026.03.033) arrives at the same conclusion from *E. coli* RNAP, using abortive transcription trapping to enrich pre-reaction states. Together the two papers constitute what is effectively a unified mechanistic statement covering three domains of life.

---

### 2. Necessary Background Crash-Course

**The Nucleotide Addition Cycle (NAC).** Pol II moves along DNA in one-base steps. At each step: an NTP substrate enters the active site, base-pairs with the template DNA strand, a new phosphodiester bond forms (the 3′-OH of the growing RNA attacks the α-phosphate of the incoming NTP), pyrophosphate is released, and the enzyme translocates one position. Repeat ~40 times per second. Think of it like a laser printer's print head: each pixel is one nucleotide, and the printhead advances one dot pitch per cycle.

**The Two-Metal-Ion Mechanism.** Two magnesium ions (Mg²⁺) sit at the heart of the active site. Metal A is permanently bound, coordinated by conserved aspartate residues in RPB1; it activates the 3′-OH of the RNA for nucleophilic attack. Metal B comes in with the incoming NTP (coordinated by its triphosphate), stabilizes the transition state, and leaves with the pyrophosphate product. The analog is a two-handed robot arm: one hand holds the workpiece, the other delivers and seats the new part.

**The Trigger Loop (TL).** A mobile hairpin in RPB1 (residues ~1077–1096 in yeast) swings from an "open" to a "closed" conformation when the correct NTP is bound. In the closed state it forms a roof over the active site, making van der Waals contacts with the NTP base and ribose, precisely positioning the reactants. A conserved histidine (His1085 in yeast) directly contacts the NTP β-phosphate in the closed state. The TL is the fidelity gate — wrong NTPs can't trigger full closure, so the reaction is suppressed.

**The Proton Problem.** Bond formation requires deprotonation: the 3′-OH must lose its proton (become a better nucleophile) before it attacks the α-phosphate. Where does that proton go? Two schools of thought: (1) the enzyme itself acts as the base, via a nearby amino acid side chain; (2) structured water molecules form a proton relay chain (Grotthuss mechanism) shuttling the proton out to bulk solvent. Resolving which is correct requires seeing individual water positions at the active site — which demands sub-2 Å resolution in a transcribing complex.

---

### 3. Core Technical Explanation

**Sample preparation — trapping the fleeting state.** To enrich for the pre-reaction state without chemically altering the substrates, the Darst lab forced the enzyme into abortive transcription by providing three of the four NTP building blocks, withholding the fourth. This forced the enzyme into a loop producing short RNA fragments and restarting repeatedly, enriching the sample with enzymes at the earliest, catalytically active stages. The Pol II paper uses a similar strategy — an elongation complex scaffold stalled one nucleotide before a defined template position — combined with saturating NTP to accumulate the Michaelis complex (NTP bound, chemistry not yet completed). Flash-freezing into liquid ethane locks these transient states.

**Cryo-EM at sub-2 Å.** With ~2 million particles, the authors computationally sort populations into distinct states along the reaction coordinate: (1) pre-translocation, (2) post-translocation (NTP-free), (3) Michaelis complex (NTP bound, trigger loop closed, pre-chemistry), and (4) product complex (pyrophosphate still in site). At resolutions below 2 Å, you can see not just amino acid side-chain rotamers but ordered water molecules — individual H₂O molecules placed unambiguously in the electron density. This resolution tier was essentially inaccessible to cryo-EM for a large flexible complex like Pol II until very recently; the hardware (300 kV Titan Krios with Falcon 4 or K3 detectors) and software (cryoSPARC/RELION with particle polishing) now make it routine for well-ordered cores.

**What they see in the Michaelis complex.** In the trigger loop–closed state with correctly matched NTP in the active site:

- Metal A is coordinated by three conserved aspartates (Asp481, Asp483, Asp485 equivalent in the Pol II subunit RPB1) plus the 3′-OH oxygen of the RNA. The geometry is octahedral.
- Metal B is coordinated by the α, β, γ-phosphates of the incoming NTP and two waters.
- A continuous chain of water molecules extends from the active site, where the reaction occurs, to the surrounding solution — this water network provides a path for protons to exit, supporting a water-mediated deprotonation mechanism.

The water wire runs from the 3′-OH (the nucleophile) through 3–4 ordered water molecules, terminating at a solvent-exposed channel. This is textbook Grotthuss relay: a proton hops along pre-organized hydrogen bonds without any water molecule physically translocating. The analogy is a bucket brigade — the bucket (proton) moves down the line while people (water molecules) stay in place.

**The trigger loop's role.** When the TL closes, it doesn't just position the NTP — it also repositions two water molecules near the active site that complete the proton wire. Opening the TL (wrong NTP, or post-catalysis) dismantles the water chain. This creates an elegant coupling: fidelity checking (via TL closure) and chemistry (proton removal via water wire) are mechanistically linked.

**Product complex.** After bond formation, pyrophosphate occupies the Metal B site before release. The structures show Metal B departing with pyrophosphate, the TL opening, and the active site re-exposing — all captured as separate particle classes.

**Conservation check.** The same water-wire architecture appears in yeast Pol II structures at equivalent resolution, and the active site of RNAP is nearly identical across all forms of life — bacterial, archaeal, and eukaryotic. The catalytic mechanism appears to be universal.

---

### 4. What's Genuinely New or Clever

**Trick #1: Proton mechanism resolved without substrate analogs.** All prior mechanistic structures used NTP analogs (e.g., AMPcPP, NTP-αS) that are chemically inert at the scissile bond, meaning they were mimics that inevitably distorted active-site geometry. These substitutions forced the enzyme into artificial states, altering its natural geometry — the resulting structures failed to capture how the enzyme actually operates. This work uses genuine substrates, trapped by the biochemical trick of abortive cycling and ultra-rapid cryo-freezing. The Michaelis complex here is *real*, not an approximation.

**Trick #2: Sub-2 Å resolution on a transcribing elongation complex.** Free Pol II reaches this resolution tier fairly readily, but a fully assembled elongation complex — with 12 subunits, DNA, RNA, and a closed trigger loop — is partially flexible. Achieving sub-2 Å in this context required both exceptional sample preparation (homogeneous, stall-defined scaffold) and sophisticated particle subtraction/focused refinement strategies to overcome local flexibility elsewhere in the complex.

---

### 5. Limitations & Open Questions

**The elephant: only one base pair shown.** The genetic code consists of four bases — with one base captured, the other three (which differ in size and chemistry) may change how the active site is arranged. This is not a minor gap. Purine-pyrimidine differences in NTP geometry could alter water-wire topology. A complete mechanistic picture requires all four NTP structures.

**Proton wire ≠ full reaction mechanism.** Seeing the water chain means seeing a plausible proton-exit path, not a directly observed proton transfer event. The transition state itself (the pentacoordinate phosphorus intermediate) is not captured — that would require time-resolved cryo-EM or X-ray free-electron laser crystallography at femtosecond-to-picosecond timescales. What's resolved is the pre-chemistry state, not the chemistry per se.

**Metal B occupancy is complex.** There's longstanding debate about whether a third Mg²⁺ plays a role, analogous to DNA polymerase η. A potential third Mg²⁺ was observed previously at a location near Pol II Rpb2 E529 and Y769, and its role is not yet clear, though mutations at those adjacent residues can alter Pol II activity in both directions. Whether this paper resolves the third-ion question or sidesteps it is unclear from available press materials.

**E. coli vs. eukaryote caveat.** The richest mechanistic detail comes from the Darst *E. coli* paper. While the Pol II paper confirms conservation of the water wire in yeast, the quantitative details (exact water positions, hydrogen-bond geometries) may subtly differ in human Pol II, especially given the additional subunits and the Si3 insertion domain in bacterial RNAP that has no eukaryotic counterpart.

**No dynamics.** Static cryo-EM snapshots tell you what states exist, not how fast the transitions happen or what the free-energy barriers look like. MD simulations informed by these structures will be essential to complete the picture.

---

### 6. Three Crystallized Takeaways

1. **Water does the chemistry.** The proton that Pol II must remove to start RNA synthesis doesn't go into a protein side chain — it exits via a relay chain of ordered water molecules threading from the active site to bulk solvent. Water molecules are active participants in transcription, not spectators.

2. **The trigger loop creates the water wire.** When the correct NTP is bound and the trigger loop snaps shut, it doesn't just hold the NTP in place — it also organizes the water chain needed for catalysis. Fidelity and chemistry are physically coupled by the same conformational switch.

3. **The mechanism is universal.** The same water-wire architecture shows up in bacterial, archaeal, and eukaryotic RNA polymerases. Every organism that has ever lived and used RNA uses this same ancient trick. 

---

### 7. Detailed Summary & Explanation

**Background.** Multi-subunit RNA polymerases transcribe all cellular genomes and have been structurally characterized since the 2000 Kornberg crystal structures. The iterative nucleotide addition cycle — NTP binding, phosphodiester bond formation, pyrophosphate release, translocation — depends mechanistically on two Mg²⁺ ions and a conformationally dynamic trigger loop. The core chemical step requires deprotonation of the RNA 3′-OH prior to nucleophilic attack on the incoming NTP's alpha-phosphorus. Whether this deprotonation is enzyme-catalyzed via a protein base, or water-mediated via a Grotthuss relay, was debated for two decades.

**Technical approach.** The authors exploit the sub-2 Å resolution now achievable by cryo-EM on well-ordered complexes. They trap transcribing Pol II at a defined template position with matched NTP, using abortive transcription (withholding one NTP to force cycling) to enrich the pre-catalysis Michaelis state. Cryo-EM of ~2 million particles, computationally sorted into reaction-state classes, yields structures of the post-translocation state (empty A-site), the Michaelis complex (NTP bound, trigger loop closed, no chemistry yet), and the product complex (pyrophosphate present). At sub-2 Å, individual ordered water molecules are unambiguously placed.

**Key findings.** In the Michaelis complex, the trigger loop is fully closed around the correctly matched NTP. The Metal A–Metal B geometry is consistent with a two-metal-ion mechanism. Critically, a continuous chain of 3–4 ordered water molecules runs from the 3′-OH oxygen of the RNA primer through the enzyme to bulk solvent. This chain's geometry is compatible with Grotthuss proton hopping: each water molecule donates a proton to the next and accepts one from the preceding, net-transporting the proton without any water molecule moving position. TL closure physically positions the waters in this configuration; TL opening (seen in the product complex and post-translocation state) dismantles the chain.

**What this means.** The water-mediated mechanism means that Pol II doesn't need a dedicated catalytic base residue — which explains why no single universally conserved proton-accepting residue has ever been identified despite intense mutagenesis studies. The enzyme instead uses the geometry of the water network, assembled by the trigger loop, to remove the proton. This is analogous to how some serine proteases use a "charge relay" network — except here the network is composed of solvent waters rather than side chains.

**Conservation.** The companion Darst *E. coli* paper shows the identical architecture in bacterial RNAP, and the yeast Pol II structures confirm it in eukaryotes. Since the active site is structurally conserved across all three domains of life, the mechanism is almost certainly universal.

**Implications for disease and drug design.** The precise water positions provide a new framework for understanding why mutations in active-site residues are so disruptive — many likely destabilize the water wire rather than directly disrupting metal coordination. Antibiotics targeting bacterial RNAP (rifampicin, fidaxomicin) act at a distance from the active site; this work opens the possibility of designing inhibitors that specifically target the water network or the trigger-loop closing motion that organizes it. For transcription-targeting cancer drugs (like CDK inhibitors that work upstream), the mechanistic detail here is less immediately translatable, but understanding how water dynamics couple to fidelity could inform design of mutant-selective transcription inhibitors.

---

### 8. Shorter Summary

This paper delivers the first cryo-EM structures of actively transcribing RNA Polymerase II at sub-2 Å resolution — good enough to see individual water molecules inside the catalytic core. By trapping the enzyme in its real Michaelis complex (correct NTP bound, chemistry about to fire, no chemical analog involved), the authors show that Pol II removes the proton needed to start chemistry via a relay chain of ordered water molecules threading from the active site outward — a Grotthuss proton wire. The trigger loop, which also enforces nucleotide fidelity, physically organizes this water chain when it closes around a correct NTP. Open it, and the wire dissolves. The same architecture appears in yeast Pol II and *E. coli* RNAP, confirming a universal mechanism for gene transcription shared by all life on Earth. The long-standing debate about whether a protein side chain or water molecules remove the catalytic proton is resolved: it's the water.

## Human

Explain the resolution revolution in cryo-EM — now regularly pushing below 2 Å for stable complexes

## Assistant

**Explaining** — v3.4.9

## The Cryo-EM Resolution Revolution: From Blobs to Atoms

This is a great thread to pull on given the context of the Pol II paper. Let me walk you through what actually changed, because it's a beautiful convergence of physics, detector engineering, and algorithms — not a single breakthrough but a cascade.

---

### The Historical Baseline: Why Cryo-EM Was "Blobology"

Through the 1990s and into the 2000s, cryo-EM was the technique you used when your complex was too big or too flexible for X-ray crystallography. The tradeoff was brutal: crystallography gave you 1.5–3 Å routinely; cryo-EM gave you 6–10 Å — good enough to see secondary structure, bad enough that you couldn't place individual side chains. The community called it "blobology" with varying degrees of affection.

The fundamental physics is why. You're imaging single protein molecules — maybe 300 kDa — with electrons. Electrons interact with matter much more strongly than X-rays do, which is why you can image single molecules rather than needing a crystal. But that same strong interaction is a liability: the electron beam damages the molecule, so you have to use very low doses. Low dose means high shot noise. High shot noise means you need to average thousands to millions of identical particles to beat down the noise and recover the underlying signal.

This is the core equation driving everything: signal-to-noise scales roughly as the square root of the number of particles averaged. To go from 6 Å to 2 Å you need not just better alignment but roughly an order of magnitude more usable information per particle — or dramatically more particles. Both turned out to require hardware that didn't exist yet.

---

### Revolution Step 1: Direct Electron Detectors (2012–2013)

This is the single biggest inflection point. Before ~2013, cryo-EM used charge-coupled device (CCD) cameras, which don't detect electrons directly. An electron hits a scintillator, produces light, and the light hits the CCD. That intermediate light-conversion step blurs the signal — you lose the precise position information of where each electron landed. The point-spread function was broad enough to wash out high-resolution features.

Direct electron detectors (DEDs) — first the Gatan K2, then the FEI Falcon series — eliminate the scintillator entirely. An electron hits a CMOS-based sensor directly, and the position of each electron impact is recorded to sub-pixel accuracy. The detective quantum efficiency (DQE) at high spatial frequencies (where fine structural detail lives) jumped dramatically. For cryo-EM, DQE at the Nyquist frequency went from roughly 0.1 on a CCD to 0.5–0.7 on a good DED — this is roughly the signal equivalent of getting 5–7× more data for free.

But DEDs brought a second gift: **movie mode**. These detectors read out fast enough (40–50 frames per second) to record dose-fractionated movies of beam exposure rather than a single integrated image. Why does this matter? Because the electron beam causes the cryo-frozen sample to physically move — "beam-induced motion" — during exposure. On a CCD, all that motion smeared into a single blurred image. With movie mode, you can correct for that motion computationally, frame by frame, sharpening each image retrospectively.

The analogy from signal integrity work: it's exactly like adaptive equalization in a SerDes link. The channel introduces phase distortion (here, physical motion distortion); movie-mode beam-motion correction is the equalizer that unwraps it.

---

### Revolution Step 2: Software for Motion Correction and CTF Estimation

Even with movies, you need software to use them. MotionCor2 (David Agard's lab at UCSF) does patch-based local motion correction — it estimates not just global sample drift but local per-patch motion, because different parts of the grid move differently. This pushed resolution further by tightening the effective PSF.

Contrast Transfer Function (CTF) correction became much more sophisticated. The CTF describes how the defocus and aberrations of the electron microscope modulate spatial frequencies — it's zero at certain frequencies (called "contrast transfer zeroes"), meaning that information is destroyed. Accurate CTF estimation (using tools like CTFFIND4, Gctf) allows you to model and partially recover even the modulated frequencies, pulling out signal that would otherwise be lost. Modern workflows also do per-particle CTF refinement, recognizing that the exact defocus varies across the field of view.

---

### Revolution Step 3: Bayesian Particle Alignment (RELION, cryoSPARC)

Knowing you have a million particles does you no good if you can't align them accurately. The central problem: each particle image is a 2D projection of a 3D structure at an unknown orientation. You need to determine that orientation to combine projections into a 3D reconstruction — but the images are so noisy that direct feature matching fails at high resolution.

RELION (Sjors Scheres, MRC LMB) introduced Bayesian maximum-likelihood 3D classification and refinement. Instead of assigning each particle to a single orientation, it computes a probability distribution over orientations, weighted by the data. This naturally handles noise better because it doesn't commit to wrong assignments — it hedges. The Bayesian prior regularizes the reconstruction, preventing overfitting to noise. This is mathematically analogous to how a Kalman filter handles noisy state estimation: you propagate uncertainty rather than forcing hard decisions.

cryoSPARC (Punjani et al., Structura Biotechnology) added a complementary innovation: stochastic gradient descent for initial model building and branch-and-bound orientation search, which is dramatically faster than RELION's exhaustive approach. The two tools became the community's tandem workhorse.

**Particle polishing** (a RELION feature) brought further gains: instead of applying one motion trajectory per micrograph, it computes per-particle trajectories. A particle near the edge of the field moves differently than one at the center; polishing corrects for this individually. For high-resolution work, this can contribute 0.1–0.2 Å improvement in final resolution.

---

### Revolution Step 4: Hardware — The Titan Krios at 300 kV

The resolution achievable also depends on the coherence of the electron beam. Higher accelerating voltage (300 kV vs. 120 kV) gives electrons a shorter de Broglie wavelength — about 2 pm at 300 kV vs. 3.4 pm at 120 kV — extending the theoretical information limit. The Thermo Fisher Titan Krios became the workhorse instrument for high-resolution work: its field emission gun (X-FEG) provides high spatial and temporal coherence, its automated cryo-stage has < 0.5 nm drift per minute, and its column is insulated from vibration.

For truly pushing below 2 Å, aberration correctors start to matter. Phase plates (Volta or electrostatic) improve contrast for small particles by phase-shifting the zero-order beam, improving the CTF at low frequencies — important for initial alignment accuracy, which ultimately limits high-resolution recovery. Cold-FEG emitters reduce energy spread, improving temporal coherence and thus high-frequency CTF envelope.

A 2020 paper showed that a 200 kV Talos Arctica (a mid-tier instrument) equipped with a K2 detector could reach ~1.7 Å on apoferritin — demonstrating that hardware ceiling is no longer the bottleneck for well-behaved specimens. The information is in the data; you just need good enough hardware to capture it and good enough software to extract it.

---

### Revolution Step 5: Sample Preparation Advances

All the detector and software advances become moot if your sample is heterogeneous, preferentially oriented, or too thin/thick on the grid. The "resolution wall" for many interesting complexes is now the sample, not the instrument.

**Cryo-lamella FIB-SEM** (Focused Ion Beam milling on frozen cells) lets you prepare thin lamellas from actual cells for cryo-EM — not reconstituted complexes but native cellular contexts.

**Graphene and gold grids** reduce beam-induced motion by physically tethering particles to a conductive surface, improving the motion correction starting point.

**Microfluidic vitrification** (Spotiton, chameleon devices) reduces the blotting step that causes particle preferential orientation and concentration artifacts — blotting is notoriously destructive to particle populations.

For large, flexible complexes like Pol II elongation complexes, sample homogeneity is still the limiting factor. The sub-2 Å Pol II result required both a conformationally defined stall scaffold and high particle count to resolve the catalytically relevant subpopulation cleanly via 3D classification.

---

### Where the Limit Is Now

The theoretical resolution limit for cryo-EM is set by radiation damage, not optics. You can only deliver so many electrons per unit area before the molecule is destroyed. The practical limit for a rigid, symmetric protein (like apoferritin) is now routinely 1.2–1.5 Å. For an asymmetric, partially flexible complex like Pol II, sub-2 Å in the ordered core with focused refinement masking out flexible periphery is state of the art.

The resolution "frontier" has now shifted to the sample problem: can you get the molecule into a homogeneous, well-behaved state? This is why the Pol II paper's biochemical trick — abortive transcription to enrich the Michaelis state — is as important as the hardware. No amount of detector improvement rescues a heterogeneous sample.

---

**The TL;DR in chip-designer terms:** CCD cameras were the analog DAC with terrible ENOB at high frequency. DEDs are the high-linearity, high-bandwidth ADC. Movie mode is the anti-aliasing filter running before sampling. Motion correction and CTF refinement are the equalizer and clock-data recovery. RELION/cryoSPARC are the digital back-end that does symbol detection under high SNR conditions. And particle polishing is per-lane calibration. The resolution revolution is what happens when every link in that chain gets properly engineered at once.
