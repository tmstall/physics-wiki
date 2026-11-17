---
tags: [papers, precision-measurement, cpt, antimatter, penning-trap, positron]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [positronium-diffraction-graphene, quantum-jumps-of-sound, coupling-free-electrons-trapped-ion]
source_analysis: "raw/analyses/2026-10-24_doi-10.1103-gbkc-6nlj_one-positron-quantum-cyclotron.md"
---

# One-Positron Quantum Cyclotron

**One-line summary:** A single positron has been held for months at 300 mK in a Penning trap and watched taking one-quantum cyclotron steps and spin flips; no magnetic moment is reported yet, and the advertised CPT gain is a forecast. Myers et al., *Phys. Rev. Lett.* (2026).

## Key claims and results

- **Paper:** T. G. Myers, L. Soucy, B. A. D. Sukra, B. Sinha, G. Gabrielse. *Phys. Rev. Lett.* **137**, 173001 (2026). DOI [10.1103/gbkc-6nlj](https://doi.org/10.1103/gbkc-6nlj). Editors’ Suggestion. Open access. A capability Letter: no new constant.
- Apparatus: sealed trap under a dilution refrigerator, electrodes and enclosure near **300 mK**, inside a 4.2 K solenoid at **5.6 T**. Cyclotron frequency about **156 GHz**. One quantum is about 7.5 K, so thermal excitation at 300 mK is negligible if the cyclotron motion really sits at the wall temperature. The magnet drifts by about 2 parts per billion per day.
- Loading: a weak $^{22}$Na source rides a nylon cable onto the enclosure. Positrons slow in tungsten, form neutral Rydberg positronium, and pass a **640 μm** hole. The trap field ionizes them inside. One positron every **8–11 hours**. The source is then lifted. A positron has been held for months. The hole is the compromise that keeps the electrodes a microwave cavity.
- Readout: two saturated nickel rings make a magnetic bottle. Each cyclotron quantum or spin flip shifts the axial frequency by about **3.8 Hz**, read by a swept drive and a Fourier transform about once a second. A coaxial ring resonator around the electrodes is new for this kind of detection. The cavity stretches the free-space cyclotron lifetime from about 83 ms to about **4 s** (roughly 50-fold inhibition; the paper’s “up to 200” is the design ceiling, not this trap).
- Demonstrated: one-quantum jumps, a two-quantum climb that decays one rung at a time, and spin flips that stay flipped. Full-size steps match the calculated one-positron bottle shift. Two positrons would show half-size steps. That check uses the calculated bottle, not a counted charge.
- The 2023 electron moment is about 0.13 parts per trillion. The positron’s last comparison is 1987. The paper’s “more than 30 times” matches the positron *measurement* relative to 1987. The electron–positron *comparison* improves by roughly 11–16 times if both sides reach the 2023 electron precision, unless shared systematics cancel harder than that. Nothing in this Letter is that measurement.

## Physical intuition

The electron quantum cyclotron has existed since 1999. The positron was stuck because it is born hot and the precision trap must stay a closed cavity. The trick is a disguise: send the charge in as a neutral atom so a hair-thin hole is enough, then let the trap’s own field strip it. After that, the machine is the electron apparatus with an antiparticle in it. Cold means the cyclotron ladder is empty except for the bottom rung. The bottle turns “which rung, which spin” into a few-hertz shift of the slow bounce, read without changing the rung. The cavity is what makes the rung last long enough to see.

## Limitations and assumptions

- No moment, no frequency ratio, no error budget. The closing paragraph says a measurement now seems feasible.
- Figures are example traces. No attempt count, fidelity, or public dataset.
- One-particle evidence is inferential. A factor-of-two error in the bottle would let two positrons mimic one in step size; the spin pattern and the slow load rate argue against that.
- Only the cyclotron motion is shown to be at 300 mK. Axial and magnetron temperatures are a different story, and they matter for the future precision run.
- The strong bottle that enables readout also smears the frequencies the moment measurement must control. The readout here is the simpler swept drive, not the electron experiment’s self-excited oscillator.
- Single group. A CPT test is only as good as the systematics that do not cancel when an electron and a positron share one trap. Sidereal time matters if the violation is a fixed background field.

## Connections

- Different antimatter experiment (diffraction, not a moment): [[positronium-diffraction-graphene]]
- Other single-quantum mechanical readouts: [[quantum-jumps-of-sound]]
- Free electrons coupled to a trap, not an antiparticle moment: [[coupling-free-electrons-trapped-ion]]
- Synthesis: [[amo-quantum-state-control]]

## Open questions

- What positron moment, with what error budget, does this trap actually deliver?
- Does a same-trap electron–positron swap cancel the systematics that dominated 1987?

## Source

- `raw/analyses/2026-10-24_doi-10.1103-gbkc-6nlj_one-positron-quantum-cyclotron.md`
