---
tags: [papers, photonics, metrology, thz, microcomb]
last_updated: 2026-08-22
status: analysis-ingest
related_papers: [two-clocks-one-laser, freeze-fiber-brillouin, photon-number-optical-analogy-control, ito-nanocrystal-fieldoscopy]
source_analysis: "raw/analyses/2026-08-20_doi-10.1038-s41467-026-76747-2_mmwave-comb-optical-microcomb.md"
---

# Direct mm-Wave Comb from an Unamplified Optical Microcomb

**One-line summary:** A ~49 GHz laser-cavity-soliton microcomb (~5 mW, no EDFA) drives a commercial photoconductive THz antenna to emit a broadband mm-wave harmonic comb; multisoliton states reshape the envelope, and GPS-referenced locking cuts timing jitter ~40× (*Nat. Commun.* 2026).

## Key claims and results

- **Paper:** *Nature Communications* (2026), DOI 10.1038/s41467-026-76747-2.
- Source: doped-silica microring (FSR ≈ 48.9 GHz, Q ~ 1.3×10⁶) in an Er/Yb fibre laser; filtered ~5 mW LCS output → Menlo TERA15 antennas **without** optical amplification for the headline demo.
- Conversion: $E_{\rm THz}\propto dI/dt$ → single-cycle bipolar pulse; Fourier comb harmonics out past ~0.6–1 THz at cavity spacing.
- Two-soliton states keep line spacing fixed but redistribute harmonic strengths (interference); reconstruction matches TDS traces after receiver convolution.
- Locking (piezo fibre + EO sideband PID to GPS-disciplined ref): jitter ~6.3 ps → &lt;150 fs; Allan deviation of selected harmonics ~10⁻¹² (1–100 s) for the locked chain.
- Long-delay coherence: +8 m (~27 ns, &gt;10³ periods) on receiver path — no significant spectral change.

## Physical intuition

Sub-picosecond soliton edges are optical “sharp clocks”: a photoconductive switch differentiates intensity into a broadband electrical comb. Extra circulating solitons are a free spectral shaper — same tooth spacing, different envelope — without RF synthesizer chains.

## Limitations and assumptions

- Single collaboration; no independent lab replication yet.
- Allan numbers describe the locked reference chain’s transfer coherence more than standalone free-running microcomb absolute stability.
- Optional ~120 mW amp used only for SNR in some scans — not required for basic conversion.
- Engineering/demo paper, not a new fundamental effect.

## Connections

- Metrology / timing neighbors: [[two-clocks-one-laser]], [[freeze-fiber-brillouin]]
- Photonic control: [[photon-number-optical-analogy-control]], [[ito-nanocrystal-fieldoscopy]]
- Synthesis: [[amo-quantum-state-control]], [[ultrafast-optics-and-solid-state-emitters]]

## Open questions

- On-chip antenna + microcomb co-integration for 6G / TDS front ends?
- Independent replication with a different Kerr/LCS platform?
- How far can shorter pulses push the usable harmonic ceiling?

## Source

- `raw/analyses/2026-08-20_doi-10.1038-s41467-026-76747-2_mmwave-comb-optical-microcomb.md`
