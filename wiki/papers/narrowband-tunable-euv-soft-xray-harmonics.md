---
tags: [papers, hhg, euv, xray, light-sources]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [ultrafast-optics-and-solid-state-emitters, correlated-electrons-xray-hhg, bessy-tes-soft-xray-spectrometer]
source_analysis: "raw/analyses/2026-09-21_doi-10.1038-s42005-026-02791-5_narrowband-tunable-euv-soft-xray-harmonics.md"
---

# Narrowband Tunable EUV and Soft-X-ray Harmonics

**One-line summary:** Popmintchev et al. (*Communications Physics*, 2026, Article in Press; DOI [10.1038/s42005-026-02791-5](https://doi.org/10.1038/s42005-026-02791-5)) slide a whole high-harmonic comb by broadening the infrared driver and frequency-doubling a chosen slice, so a narrow line can park on the Fe, Co, or Ni M-edge. This is source engineering. No imaging or spectroscopy measurement uses the beam yet.

## Key claims and results

- Gas-phase high-harmonic generation emits odd multiples of the driver photon energy. Adjacent teeth sit about $2\hbar\omega_0$ apart — here $4.8$–$5.2\,\mathrm{eV}$ for a $\sim480$–$550\,\mathrm{nm}$ visible driver. Moving a tooth means moving $\omega_0$, without dropping the phase matching that makes the comb bright.
- Chain: a Yb:CaF$_2$ amplifier (1030 nm, 200–270 fs, up to 14 mJ, 0.5–1 kHz) broadens in a 6 m hollow-core fiber. Argon (self-phase modulation) spreads the spectrum both ways; nitrogen (Raman) pushes it red. Chirped mirrors recompress to as short as sub-15 fs. A 300 µm type-I BBO crystal doubles one phase-matched slice into an 8–30 fs visible driver tunable across 480–550 nm. Helium in a variable-length cell generates the harmonics. Helium’s ionization potential keeps the neutral response alive out past 110 eV at $\sim10^{15}\,\mathrm{W/cm^2}$. A pressure scan shows no He$^+$ emission.
- In the 40–75 eV window the tuned teeth fill the gaps between fixed orders and land on the Fe ($\sim53\,\mathrm{eV}$), Co ($\sim59\,\mathrm{eV}$), and Ni ($\sim68\,\mathrm{eV}$) M-edges. A strong-field / ADK yield curve matches the measured roll-off. Flux stays roughly flat across the sweep. Conversion is a modest $\sim10^{-5}$–$10^{-6}$ (about $5\times10^{7}$–$5\times10^{8}$ photons per pulse at the cell exit) — tunability at constant flux, not a brightness record. Filters plus the spectrometer isolate one harmonic at better than 80% efficiency.
- Table 1 limits the slogan “continuous.” With one visible color, full one-way coverage of the inter-order gap starts at the 11th harmonic (24.3 eV), and full bidirectional coverage at the 5th (11.0 eV). Below that, gaps remain. A two-color drive (infrared plus visible) is predicted to push bidirectional coverage down to the 2nd harmonic (2.6 eV). The paper does not demonstrate that configuration.
- Single collaboration (TU Wien and UC San Diego). Article in Press (published online 7 August 2026). No independent replication, and no downstream resonant measurement.

## Physical intuition

A high-harmonic source is a clock multiplier locked to one reference laser. The X-ray lines are the odd multiples, and if none of them sits on a core-level absorption edge you do not get element-specific or magnetic contrast. Retuning the amplifier itself usually spends the pulse energy, the duration, or the coherence you needed for phase matching. The workaround never touches the harmonic process. Stretch the infrared spectrum in a gas fiber, then frequency-double only the slice a crystal angle will accept. That slice is a movable reference, so every harmonic slides with it. Argon and nitrogen push the slice in opposite directions, which is how the same bench closes a gap from both sides. The physics is the usual three-step recollision model. The result is that the comb can be parked on iron, cobalt, or nickel and stay narrow while the flux barely changes. The paper stops at the source.

## Limitations and assumptions

- No resonant imaging, XMCD, XAFS, or $^{229}$Th nuclear-clock search is performed. Those are motivations. Whether this linewidth and flux suffice under a real integration time is open — especially for a narrow nuclear resonance.
- Visible-to-EUV efficiency stays $\sim10^{-5}$–$10^{-6}$ and falls further toward higher photon energy. Statistics, not tuning range, will limit many downstream runs.
- Nitrogen broadening heats the fiber (Raman deposits energy in the gas). Transmission drops. Larger cores, mixed gases, and differential pumping are named and not shown.
- The clean neutral-helium picture is demonstrated near $10^{15}\,\mathrm{W/cm^2}$. It need not survive other gases or the higher intensity required to push cutoff or efficiency, where plasma dispersion joins the phase-matching budget.
- Bidirectional continuous tuning does not cover the whole EUV–soft-X-ray range. Low orders still have gaps on a single color.

## Connections

- Ultrafast source and probe shelf (this page is a tunable HHG driver, not a solid-state emitter result): [[ultrafast-optics-and-solid-state-emitters]]
- A different HHG question — correlated two-electron recombination past the single-electron cutoff, not a tunable comb: [[correlated-electrons-xray-hhg]]
- Soft X-ray spectrometry on a synchrotron (TES at BESSY II), not a tabletop harmonic source: [[bessy-tes-soft-xray-spectrometer]]

## Source

- `raw/analyses/2026-09-21_doi-10.1038-s42005-026-02791-5_narrowband-tunable-euv-soft-xray-harmonics.md`
