---
tags: [papers, quantum-optics, trapped-ions, electron-microscopy, quantum-metrology]
last_updated: 2026-08-29
status: analysis-ingest
related_papers: [quantum-state-sculptor, massive-tunneling-schrodinger-cats, dissipative-cavity-entanglement, 3d-electron-diffraction-osc, positronium-diffraction-graphene, quantum-proper-time-ion-clocks]
source_analysis: "raw/analyses/2026-08-24_arxiv-2601.11446_coupling-free-electrons-trapped-ion-quantum-computer.md"
---

# Coupling Free Electrons to a Trapped-Ion Quantum Computer

**One-line summary:** Theory proposal: insert a $^{40}$Ca$^+$ surface-electrode trap into a TEM sample plane and use Coulomb phase shifts on a motional cat state to turn a passing free electron into a resolvable qubit flip — with Heisenberg-like multi-electron metrology that remains fragile under electron loss (arXiv:2601.11446; not peer-reviewed at analysis time).

## Key claims and results

- **Paper:** Pescoller et al., arXiv:2601.11446v1 [quant-ph] (16 Jan 2026) — theoretical feasibility study; no apparatus built.
- Architecture: chip-scale ion trap in the TEM specimen plane; free electrons couple to the ion only through the long-range Coulomb field (impact parameter, not impact).
- Scattering operator $\hat{S}$ derived under paraxial + stroboscopic approximations from a relativistic electron + trapped-ion Hamiltonian (Apps. B–C).
- Headline: for already-demonstrated cat size $\alpha\approx6.5$ and slow electrons (100 eV–1 keV), single-electron qubit-flip probability reaches order $0.1$–$1$ (Fig. 3).
- Mechanism: a global Coulomb phase on an ordinary coherent motional state is useless; the same differential phase on the two branches of a motional cat, after recombination, becomes a qubit rotation.
- Multi-electron metrology (App. G): ideal Fisher information $F(\varphi)=n^2$ (Heisenberg); with per-electron loss $\varepsilon$, $\mathrm{E}[F]=n^2(1-\varepsilon)^n$, optimum $n^*=-1/\ln(1-\varepsilon)$. At $\varepsilon=0.01$, $n^*\sim100$ still yields a large expected advantage over SQL ($\sim n$). Advantage on average survives only up to roughly ~30% loss.

## Physical intuition

Electron microscopes usually treat each electron as an independent classical probe. Here the ion’s motion is a quantum antenna: prepare a Schrödinger-cat superposition of two swinging trajectories tagged by the internal qubit, and a faint capacitive nudge from a fly-by electron phases the two branches differently. Recombine, and that invisible phase becomes a bit flip on a universal quantum processor — wiring the microscope into quantum-metrological scaling for dose-limited samples.

## Limitations and assumptions

- Proposal only: vacuum (~$10^{-9}$ mbar), fs-synchronized RF trap drive, and fitting a ~15×25 mm chip into a few-mm pole-piece gap are separately known elsewhere but not co-integrated.
- Heisenberg advantage assumes near-maximal coupling ($g\approx\pi$) and narrow prior knowledge of $\varphi$ (standard adaptive-metrology precondition).
- Losing even one electron in the maximal-entanglement protocol collapses the accumulated register.
- Internal-state excitation bound uses free K/Ca atomic scattering cross-sections as a proxy (App. E), not a first-principles trapped-ion calculation.
- Adversarial posture: every quantitative claim is a prediction about an unbuilt system.

## Connections

- Trapped-ion motional cats / CV sculpting: [[quantum-state-sculptor]]
- Cat metrology / sub-SQL sensing cousin: [[massive-tunneling-schrodinger-cats]], [[dissipative-cavity-entanglement]]
- Ion motion as metrological resource: [[quantum-proper-time-ion-clocks]], [[motional-squeezing]], [[optical-ion-clocks]]
- TEM / electron-probe neighbors: [[3d-electron-diffraction-osc]], [[positronium-diffraction-graphene]]
- Synthesis: [[amo-quantum-state-control]] (state engineering); dual interest for dose-limited imaging, not an ultrafast-optics result

## Open questions

- Can anyone co-integrate the vacuum, timing, and geometry constraints inside one TEM?
- Do measured single-electron flip probabilities match Fig. 3 once a cat of size $\alpha\sim6.5$ is prepared in situ?
- How far can partial (non-maximal) coupling soften the single-loss collapse while keeping a net advantage?

## Source

- `raw/analyses/2026-08-24_arxiv-2601.11446_coupling-free-electrons-trapped-ion-quantum-computer.md`
