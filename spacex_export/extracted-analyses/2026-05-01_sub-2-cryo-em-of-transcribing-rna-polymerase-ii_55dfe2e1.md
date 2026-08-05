---
source: spacex_export
conversation_id: fbe21ca2-e079-41b0-a46f-4c9e22713f67
title: "-> Sub-2 Å Cryo-EM of Transcribing RNA Polymerase II"
created_at: 2026-05-01T23:45:23.241758Z
updated_at: 2026-05-10T03:20:12.294533Z
n_responses: 2
platform: grok/xAI
pilot: false
---

# -> Sub-2 Å Cryo-EM of Transcribing RNA Polymerase II

## Human

Explain the following Cryo-EM at sub-2 Å. With ~2 million particles, the authors computationally sort populations into distinct states along the reaction coordinate: (1) pre-translocation, (2) post-translocation (NTP-free), (3) Michaelis complex (NTP bound, trigger loop closed, pre-chemistry), and (4) product complex (pyrophosphate still in site). At resolutions below 2 Å, you can see not just amino acid side-chain rotamers but ordered water molecules — individual H₂O molecules placed unambiguously in the electron density. This

## Assistant

**Cryo-EM at sub-2 Å resolution** represents a major leap in structural biology, especially for large, dynamic complexes like RNA polymerase II (Pol II) during transcription. The quoted text summarizes a breakthrough 2026 paper in *Molecular Cell* ("Sub-2 Å cryo-EM structures of transcribing RNA polymerase II reveal critical roles of water molecules in catalysis") on *Saccharomyces cerevisiae* (yeast) Pol II elongation complexes.

### What the experiment achieved
Researchers collected a massive dataset of **~2 million individual particle images** (single Pol II molecules embedded in thin vitreous ice). Each 2D projection is noisy and low-contrast, but by computationally aligning and averaging them, they produced 3D electron density maps.

Key technical advances enabled this:
- Affinity grids (streptavidin-lipid monolayers) minimized preferred particle orientation and air-water interface damage.
- Optimized data collection on high-end microscopes (Titan Krios with K3 or Falcon 4 detectors).
- Extensive 3D classification and focused/local refinement in software like cryoSPARC.

They sorted the heterogeneous particles into distinct **conformational states along the nucleotide addition / translocation reaction coordinate**. This is possible because the ~2 million particles provide enough statistics to separate subpopulations that differ subtly in structure (e.g., trigger loop position, nucleic acid register, ligand occupancy). The four states mentioned are:

1. **Pre-translocation** — Post-chemistry but before the enzyme advances one base pair along the DNA template/RNA transcript.
2. **Post-translocation (NTP-free)** — The complex has slid forward; the active site is empty and ready for the next nucleotide.
3. **Michaelis complex** — Cognate NTP (e.g., ATP or CTP) is bound in the active site, the trigger loop (TL) is fully closed, two catalytic Mg²⁺ ions are positioned, and the system is poised for chemistry (the classic enzyme-substrate complex before the reaction).
4. **Product complex** — The new phosphodiester bond has formed between the RNA 3′-OH and the NTP α-phosphate; pyrophosphate (PPi) is still bound in the active site before release.

They ultimately reported three high-resolution reconstructions (two pre-catalysis variants at **1.96 Å** and **2.26 Å**, one post-catalysis at **2.33 Å**), with local resolution in the active site reaching ~1.9–2.2 Å.

### Why sub-2 Å resolution is transformative
At ~3–4 Å (typical for many earlier cryo-EM structures), you can trace the protein backbone and see bulky side chains as blobs. At **sub-2 Å**, the map becomes essentially “atomic”:

- **Amino acid side-chain rotamers** are unambiguous — you see exactly which conformation each side chain adopts (e.g., the precise orientation of a catalytic arginine or the closed trigger-loop residues like Gln1078/Leu1081).
- **Individual ordered water molecules (H₂O)** appear as clear, spherical densities. The paper placed **700–1,350 well-ordered waters per structure** (many with high confidence scores, density >4σ). These are not noise or bulk solvent; they are stably bound and functionally critical.

This level of detail had been rare for such a large, flexible complex (~500 kDa + nucleic acids). Prior crystal structures of Pol II were limited to ~3 Å or worse and often lacked clear waters or full active-site details.

### What the waters reveal (the real scientific payoff)
The waters are not passive bystanders — they are **integral catalytic participants**:

- **Substrate recognition** — Specific waters bridge the NTP’s 2′-OH and triphosphate to Pol II residues, helping discriminate correct vs. incorrect nucleotides.
- **Proton transfer in catalysis** — The reaction is an SN2 nucleophilic attack. Waters form proton-shuttle chains: one network deprotonates the RNA 3′-OH (activating the nucleophile), while others protonate the pyrophosphate leaving group. This resolves long-standing questions about the exact chemical mechanism.
- **Trigger-loop dynamics** — Dozens of waters stabilize the closed TL conformation (the “catalytic” state) and help it refold/unfold.
- **Translocation “lubrication”** — Waters at the protein–nucleic acid interface act like molecular ball bearings, reducing friction and electrostatic repulsion to allow smooth sliding of the DNA/RNA hybrid.
- **Evolutionary conservation** — Many of these waters (and their positions) are shared with bacterial RNA polymerase, indicating they have been part of the transcription machinery for billions of years.

The paper emphasizes that this moves us beyond a purely “protein-centered” view of catalysis to one that includes water as an active, evolutionarily conserved component.

### Why this matters
This work provides the most detailed “movie frames” yet of Pol II in action, directly visualizing the chemical steps of RNA synthesis at near-atomic resolution. It explains how fidelity, speed, and regulation are achieved at the molecular level and opens the door to understanding mutations, drugs, or transcription factors that perturb these water networks.

In short, the ~2 million particles + advanced classification gave clean snapshots of four functional states; sub-2 Å resolution turned those snapshots into a high-definition view where individual water molecules become visible and reveal their starring roles in making transcription chemistry work. This is a landmark for both cryo-EM methodology and mechanistic enzymology.
