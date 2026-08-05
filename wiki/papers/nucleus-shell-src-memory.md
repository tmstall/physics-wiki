---
tags: [papers, nuclear-physics, short-range-correlations, jefferson-lab]
last_updated: 2026-08-02
status: analysis-ingest
related_papers: [beyond-iron-ultraheavy-cosmic-rays, star-jpsi-spin-interference]
source_analysis: "claude_export/extracted-analyses/2026-06-05_the-nucleus-has-a-memory_9f350308.md"
---

# The Nucleus Has a Memory: Shell Structure Controls Short-Range Correlations

**One-line summary:** Jefferson Lab Hall C ($e,e'p$) ratios on $^{40}$Ca, $^{48}$Ca, and $^{54}$Fe show short-range nucleon–nucleon pair rates track *which orbital is filling*, not just mass or $N/Z$ — shell “architecture” reaches down into sub-femtometer dynamics that models treated as universal.

## Key claims and results

- **Collaboration / venue (analysis framing):** Jefferson Lab Hall C; Nature-letter-style report (Nguyen, Yero, Szumila-Vance, Wertz et al.).
- Long-standing working assumption: short-range correlations (SRCs) are nearly universal once two nucleons get within ~0.5 fm — rates scale mainly with mass $A$ and neutron-to-proton ratio.
- Controlled “CaFe” trio: $^{40}$Ca (doubly magic), $^{48}$Ca (+8 neutrons in $1f_{7/2}$), $^{54}$Fe (+6 protons into the same $f_{7/2}$ ladder) isolates orbital filling vs bulk composition.
- Kinematics: high missing momentum (roughly 375–700 MeV/$c$), $x_B > 1.2$, $Q^2 \gtrsim 1.8$ GeV$^2$, tight proton-angle cuts — the SRC-dominated hard-scattering window.
- Per-nucleon ($e,e'p$) **cross-section ratios** deviate systematically from state-of-the-art shell-model, QMC, and RG-based predictions; orbital identity drives larger variations than models allow.
- Implication: SRC matrix elements need **angular-momentum-dependent selection rules** — scale separation between mean-field shell structure and hard-core physics is incomplete.
- Prior established fact used as baseline: ~90% of SRCs are $pn$ pairs (tensor-force channel dominance).

## Physical intuition

Nuclear physics long ran two toolboxes that barely talked. The shell model is a register file: nucleons occupy labeled orbitals with definite angular momentum. SRCs are bumper-to-bumper crashes when two nucleons briefly approach closer than half a femtometer and the hard core + tensor force flings them to high relative momentum. The old story said the crash rate forgets which orbital the nucleons came from — only the bulk density and $n/p$ mix matter. The CaFe experiment is a surgical firmware test: fill the *same* $f_{7/2}$ “pipeline stage” first with neutrons, then with protons, and watch the crash statistics. They do not match universal-contact forecasts. Geometry of the orbital (lobes, relative orientation, allowed spin–orbit alignments) apparently gates how often the tensor force can fire in a hard approach — architecture controls the short-range “exception path.”

## Limitations and assumptions

- Analysis-based ingest from secondary writeup; verify numerical ratios and model bands on the primary paper.
- Letter-length format: systematics and FSI discussions may be compressed.
- Final-state interactions and single-Gaussian / kinematic cuts still matter even in ratios.
- Three nuclei, one orbital ladder — generalization across the nuclear chart is open.
- Theory failure may mean missing $J$-dependence, incomplete many-body currents, or both.

## Connections

- Hard scattering / particle context: [[star-jpsi-spin-interference]], [[high-pt-physics-cern-isr]]
- Nuclear abundance at cosmic extremes: [[beyond-iron-ultraheavy-cosmic-rays]]
- EMC / medium-modified PDFs: [[emc-effect-marathon-a3]]
- Key terms (folded, no stubs): nuclear shell model, magic numbers, short-range correlations (SRC), missing momentum, tensor force, $pn$ dominance, ($e,e'p$), angular-momentum selection rules
- Synthesis: [[nuclear-dense-matter-precision]] (nuclear & dense-matter precision map)

## Open questions

- Can ab initio methods absorb orbital-dependent SRC weights without spoiling spectroscopy?
- Do other orbital ladders (e.g. $g_{9/2}$) show the same memory?
- How does this reweight high-momentum tails used in neutrino–nucleus and EMC analyses?

- Lint link: [[nucleus-tells-on-itself]]

## Source

- `claude_export/extracted-analyses/2026-06-05_the-nucleus-has-a-memory_9f350308.md`
