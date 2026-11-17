---
tags: [papers, ligo, squeezing, quantum-noise, review]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [lvk-o4a-cosmological-gwb, horizon-direct-wave-gw250114, quantum-state-sculptor]
source_analysis: "raw/analyses/2026-11-08_arxiv-2611.07074_ligo-quantum-noise-engineering-review.md"
---

# Frequency-Dependent Squeezing in Advanced LIGO

**One-line summary:** A review of how Advanced LIGO replaces dark-port vacuum with squeezed vacuum and rotates it in a 300 m filter cavity; broadband gain is real, the sub-SQL curve is inferred quantum noise, and further source strength does almost nothing at today’s optical loss. Kabagöz, arXiv:2611.07074 (2026).

## Key claims and results

- **Paper:** single-author review, arXiv:2611.07074v1, 4 Nov 2026. Not a new measurement. Plots use the author’s model and an unrefereed companion preprint. A deep-dive log is appended in the analysis and does not add a separate result.
- Quantum noise enters at the dark port. One quadrature is readout imprecision (falls as arm power rises). The other is radiation-pressure back-action on the 40 kg mirrors (rises with power). Their uncorrelated balance is the standard quantum limit.
- Fixed squeezing in O3: about 3 dB above 50 Hz, and worse radiation-pressure noise at low frequency. A 300 m detuned filter cavity rotates the ellipse by frequency (about 78° at low frequency, none above a few hundred hertz). O4: about 4–6 dB less shot noise at high frequency and 1–2 dB less total noise at 60–100 Hz.
- At intermediate frequencies the filter cavity prepares a correlated state. After the interferometer shears it, the correlation term is negative, so the total can sit below either piece alone. At Livingston, inferred quantum noise (measured total minus an estimate of classical noise) falls below the SQL by up to about 3 dB between roughly 35 and 75 Hz.
- Loss budget: about 18 dB generated, about 23% loss, about 6 dB delivered. At present phase noise, 10 dB at the readout needs roughly 6% total loss. A stronger squeezer adds essentially nothing until the loss drops. The cavity was designed for about 750 kW arm power; LIGO runs near 285 kW.

## Physical intuition

The laser is not the quantum-noise source. Empty-port vacuum is. Squeezing trades noise between two axes of that vacuum. One axis is quiet at all frequencies only if you rotate the ellipse as the frequency changes, which a detuned cavity does because different frequencies pick up different phase. The mid-band win is cancellation between readout noise and mirror kicks, not a quieter source. Loss rounds the ellipse back toward a circle, which is why the optics now matter more than the crystal.

## Limitations and assumptions

- Review, LIGO only. Virgo’s squeezing program is absent.
- The sub-SQL curve depends on the classical-noise subtraction at 35–75 Hz, where classical noise is comparable. The review states it more flatly than that.
- Mode mismatch does not fit in a single ellipse per frequency. It enters as an effective loss.
- Budget numbers are given without uncertainties. The analysis reproduced the rotation curve, the loss arithmetic, and the SQL line from the stated inputs.

## Connections

- What the same detectors did *not* hear (a cosmological background): [[lvk-o4a-cosmological-gwb]]
- A waveform read with this noise floor: [[horizon-direct-wave-gw250114]]
- Other engineered nonclassical states: [[quantum-state-sculptor]]
- Synthesis: [[gravitational-wave-strong-field-probes]], [[amo-quantum-state-control]]

## Open questions

- How much squeezing does A+ actually keep at higher arm power, and does balanced homodyne add a further dip under the SQL?

## Source

- `raw/analyses/2026-11-08_arxiv-2611.07074_ligo-quantum-noise-engineering-review.md`
