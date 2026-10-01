---
tags: [papers, agn, jets, cgm, radio-galaxies]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [black-hole-feedback-and-changing-look-agn, radio-changing-look-agn, category-79-quasar-wind, jwst-filament-cnd-ngc4696]
source_analysis: "raw/analyses/2026-09-26_doi-10.3847-2041-8213-ae9cbd_jet-aligned-halpha-cgm-radio-galaxies.md"
---

# Jet-Aligned Hα in the CGM of Radio Galaxies

**One-line summary:** ApJL DOI 10.3847/2041-8213/ae9cbd. Angle-averaged Hα looks normal; along the jet axis the halo is ~100× brighter. Mg II (column) shows no jet dependence while Hα ($n^{2}$) does → jets light existing clouds, they do not add much cool gas. Angular detection robust; luminosity/mass/energy are order-of-magnitude (pressure-balance density; redshift caveat).

## Key claims and results

- Roy, Borthakur, Heckman & Singh (*ApJL* 1009:L34, 2026; arXiv:2606.30088) stack 324 DESI quasar sight lines through LoTSS double-lobed radio galaxies at projected radii ~20–800 kpc, split by angle to the jet.
- Within 20° of the jet (74 sight lines), Hα is $1.19\times10^{-17}\,{\rm erg\,cm^{-2}\,s^{-1}}$ at >5σ. Off-axis bins are empty. The all-angle stack is <2σ, about what dilution of the on-axis signal predicts. Leave-one-out jackknife moves the flux by 4–7%.
- Jet-aligned surface brightness sits ~10–100× above stacked Hα around normal galaxies of similar stellar mass. The angle-averaged radio-galaxy halo sits in the normal band.
- Mg II covering fraction is 22% on-axis vs 16% off-axis ($p = 0.24$); equivalent widths, columns, and line widths overlap. Hα scales as density squared; Mg II tracks column. The jet lights existing clouds rather than adding much cool gas.
- Emission is strongest near jet breakout and rises again near the lobes. That radial split rests on three bins inside the 74-sight-line subsample.

## Physical intuition

Cool halo gas is too faint to photograph one galaxy at a time, so many quasar backlights are averaged. Averaging over angle washes the signal out. Sort by jet direction and a pencil beam along the jet glows about a hundred times brighter than a normal halo, while the same halos look ordinary in every other direction. Absorption says the cool gas was already there. Emission says a few clouds got denser or re-ionized, because brightness goes as density squared: a few hot lines, not a larger cache. Compression, shocks, and AGN photons down an ionization cone can all do that. The spectra do not say which.

## Limitations and assumptions

- One sample (DESI DR1 × LoTSS DR2). The stack is a mean. Leave-one-out does not rule out a handful of bright sight lines. No median stack is reported.
- Quoted luminosity and ionized mass use a mean redshift ~0.66, but DESI only sees Hα for $z \lesssim 0.47$. The same flux at $z \sim 0.38$ is ~4× fainter. Treat luminosity, mass, and jet-power fraction as order-of-magnitude.
- Mass scales as $1/n_e$. The adopted density (~$10^{-2}\,{\rm cm^{-3}}$) is a pressure-balance floor. Compressed clumps weigh less. The number is one fiber (~10 kpc), not the whole halo.
- The Mg II null cannot rule out a ~30–40% column increase. Projection mixes true jet alignment with chance alignment.
- The SIMBA map is one galaxy, ultraviolet background only, and ~$10^{3}$ times too faint. It illustrates angular structure. It does not fit the brightness.

## Connections

- Synthesis: [[black-hole-feedback-and-changing-look-agn]]
- Radio state changes, winds, and cold-gas fueling: [[radio-changing-look-agn]], [[category-79-quasar-wind]], [[jwst-filament-cnd-ngc4696]]

## Source

- `raw/analyses/2026-09-26_doi-10.3847-2041-8213-ae9cbd_jet-aligned-halpha-cgm-radio-galaxies.md`
