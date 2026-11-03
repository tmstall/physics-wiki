---
tags: [papers, xuv, raman, helium, fel, coherent-control]
last_updated: 2026-10-31
status: analysis-ingest
related_papers: [ultrafast-optics-and-solid-state-emitters, amo-quantum-state-control, two-lasers-one-reaction]
source_analysis: "raw/analyses/2026-10-20_Eichmann-2026-XUV-Raman-phase-control_xuv-stimulated-raman-phase-control-helium.md"
---

# XUV Stimulated Raman Phase Control in Helium

**One-line summary:** Eichmann et al. 2026 (analysis filename; seeded FEL). Two XUV colors move helium between bound states via the continuum — presented as the first XUV stimulated Raman demonstration — while the same light ionizes most atoms in the focus. A weak second path makes a phase-tunable interferometer; a filter kills the oscillation. Methods milestone: fringes modulate a sub-percent population; intensities uncertain by a large factor.

## Key claims and results

- Eichmann et al., *Nature Photonics*, doi:10.1038/s41566-026-02024-9 (online 9 Oct 2026). FERMI seeded free-electron laser: one ultraviolet seed clocks the XUV harmonics so they stay phase-locked.
- Main result: harmonics four orders apart (pump above the ionization threshold, Stokes bringing the atom down) populate helium's metastable singlet $2s$. Neither colour can reach $2s$ in one photon. The team counts neutral metastables ~1 m downstream after a weak field sweeps ions and electrons aside.
- Raman identification: opposite circular handedness drops the yield to a few percent (angular momentum cannot close); four harmonic pairs peak at the same seed energy (~5.15 eV); the width matches nearly transform-limited pulses.
- One-electron simulation reproduces the line shape only after intensities are cut fourfold and pulses are lengthened ~10%. Absolute yields were never measured; theory is scaled to the data by eye. The simulation saturates the $2s$ population just under 1% once the ground state in the focus is mostly ionized. At the stated pulse energies the focal centre is stripped; even at a quarter intensity, roughly nine in ten ground-state atoms ionize.
- Phase control: leftovers complete a second route to the same state (unamplified 4th harmonic at ~$10^{-3}$ of the pulse energy, or the seed itself at ~100 nJ). A phase shifter on the highest harmonic makes the yield oscillate with a period of one full turn. An aluminium filter that removes only the seed flattens the scan. A configuration with no usable third harmonic shows no fringes.
- Swings are about a fifth of the mean for the 4th-harmonic route. The paper's "about 50%" visibility on the seed route is peak-to-trough over peak; the usual contrast is ~0.3 and ~0.2 respectively. The 4th-harmonic strength in the simulation was chosen to match the fringe size; the seed-route comparison is the predictive one.

## Physical intuition

Coherent control is two routes to one outcome adding or cancelling — two clock branches with one trimmable delay. At XUV energies the brutal one-photon ionization channel swamps the gentle Raman step, so the experiment needs a scoreboard that ignores the storm: count only atoms that stored energy in a state one photon cannot reach, after the charged debris is gone. Harmonic arithmetic does the rest. Every pair four orders apart hits the same energy gap, so a weak leftover automatically finishes a second route. Fringe height scales with the product of the two amplitudes, and lower harmonics have much larger Raman cross-sections, so a thousandth of the energy is still enough to wobble the count. Blocking that colour with a filter is the null that turns a periodic wiggle into an interferometer.

## Limitations and assumptions

- Intensities are uncertain by a factor of several. Focal overlap is uncharacterized, stated intensities assume no beamline losses, and the best-fitting runs use a quarter of those values. The "no Stark shift" reading survives only if the reduced intensities are the true ones.
- The phase scan sets a relative phase from an unknown offset. Simulations were shifted by a few degrees by hand to line up.
- The second route is machine leakage, not a calibrated arm. Fig. 3b agreement is partly a fit.
- One-active-electron helium misses doubly excited resonances and misplaces the target by ~53 meV. The supplement (autoionizing-resonance predictions, pulse characterization) was not in the local copy and was not read.
- Fig. 3c–d may not share one yield scale; late points drift above the fringe. Many phase points are single shots. The interference itself is not in doubt; route strengths and coherence inferred from the figures are.
- "First XUV stimulated Raman" is the authors' framing for transfer between two bound states. Žitnik et al. (2022, FERMI) already interfered an absorb-high/emit-low route onto a short-lived doubly excited state; that comparison rests on summaries, not the full text.
- The steered population is under one percent of a closed-shell valence state. Inner-shell control in molecules needs X-ray energies, resonant enhancement, and a stronger, independently tunable second colour. None of that is tested here. Pump and Stokes are locked harmonics of one seed.

## Connections

- Synthesis (ultrafast / XUV toolkit): [[ultrafast-optics-and-solid-state-emitters]]
- Synthesis (state control): [[amo-quantum-state-control]]
- Two-colour reaction control: [[two-lasers-one-reaction]]

## Source

- `raw/analyses/2026-10-20_Eichmann-2026-XUV-Raman-phase-control_xuv-stimulated-raman-phase-control-helium.md`
