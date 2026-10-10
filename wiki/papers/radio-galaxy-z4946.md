---
tags: [papers, radio-galaxies, high-redshift, agn, lyman-alpha]
last_updated: 2026-10-09
status: analysis-ingest
related_papers: [euclid-high-z-quasar-census, high-z-quasar-pair-merger, jet-aligned-halpha-cgm, muse-desi-lens-confirmation]
source_analysis: "raw/analyses/2026-10-09_arxiv-2609.28632_most-powerful-radio-galaxy-z4946.md"
---

# A Powerful Radio Galaxy at $z=4.946$ (Headline Power Overstated)

**One-line summary:** A VLT spectrum confirms an r-dropout radio galaxy at $z=4.946$ — a solid high-$z$ discovery, and not ultra-steep-spectrum — but the claimed rest-frame 500 MHz record (~$6.2\times10^{29}$ W Hz$^{-1}$) is missing a standard $1+z$ factor of ~6 and drops to ~fifteenth place. arXiv:2609.28632, A&A in press.

## Key claims and results

- **Paper:** Italian-led short discovery note (5 pages), arXiv:2609.28632v1, comments “A&A, in press.” Method: TGSS 150 MHz sources, VLASS 3 GHz positions, Subaru HSC r-dropouts (gone in $g$ and $r$, present in $i$), then a ~40 min VLT FORS2 spectrum.
- Redshift 4.946 from a lopsided Lyman-α line at 7220 Å (sharp blue edge, red tail, ~1000 km s$^{-1}$) plus a faint NV bump at 7368 Å (~4σ, on a sky line; 244 other slit positions show no similar bump). Colour break already rules out a $z\sim1$ [O II] impostor. Light emitted ~1.2 Gyr after the Big Bang.
- Observed-frame Lyα equivalent width ~900 Å → ~150 Å in the galaxy frame (ordinary). Resolved nebula ≳6 kpc along a slit nearly *perpendicular* to the jets, so size and line flux are lower limits.
- Radio: power-law slope ~0.94 from 74 MHz to 4.8 GHz (not ultra-steep). Barely resolved, ~15 kpc along the jet after deconvolution. Host WISE detection converted to ~$2\times10^{12}\,M_\odot$ under a 100 Myr mass-to-light assumption (authors call this highly uncertain; a younger population cuts it ~10×).
- **Power ranking does not reproduce.** Paper quotes $P_{500}=6.2\times10^{29}$ W Hz$^{-1}$, twice the 2008-compendium record holder TN J0924−2201. Standard conversion $P_{500}=4\pi D_L^2 S_\nu(\nu_{\rm obs})/(1+z)$ with the paper’s own fit (~2.2 Jy at 84 MHz) and cosmology gives ~$1.0\times10^{29}$ W Hz$^{-1}$. Omitting the $1+z$ division recovers ~$5.8\times10^{29}$, within a few percent of the quoted value. Like-for-like, this source is ~3× *less* powerful than TN J0924−2201 and sits below ~15 entries in the 2008 table.
- Lyα luminosity in Table 2 is also high by ~12× vs the tabulated flux and the same cosmology. Arguments that use *flux ratios* are unaffected.

## Physical intuition

A radio galaxy is a closed data centre: dust hides the accretion-disk lights; you study the building from the cooling-tower plumes (the jets) and the outline (the host). At $z\sim5$ the Lyman break sits between HSC $r$ and $i$, so a real high-$z$ source vanishes in the blue filters and pops in $i$ — a dropout, not a proof. The spectrum’s lopsided Lyα is the proof.

Rest-frame radio power is a units-conversion audit for a compressed file. Expansion squeezes a given emitted frequency slice into a band $(1+z)$ narrower, inflating flux per hertz by that factor. You must divide it back out. Forgetting the division is reporting compressed density as raw throughput. The discovery (redshift, radio-galaxy ID, not-ultra-steep spectrum) does not need that number; the title does.

Finding a $z\sim5$ radio galaxy *without* an ultra-steep spectrum supports the view that the classic steep-spectrum filter misses a large hidden population.

## Limitations and assumptions

- Single VLT spectrum, one strong line, one modest NV. Independent lock: NIR carbon/helium lines or ALMA cold-gas redshift.
- “Most powerful radio galaxy known” and “second-most-distant” are the two superlatives. The first fails a standard recalculation. Distance rank is less fragile but still depends on later revisions (one previous distant claim has already moved much closer).
- Weighted spectral fit gives slope ~1.06 and a poor single-power-law χ² (150 and 400 MHz scatter). “Not ultra-steep” survives a 1.3 cut; a looser cut of 1.0 is closer.
- Host mass is order-of-magnitude, oxygen-line contaminated, and population-age dependent.
- No black-hole mass, no cluster environment, no demonstrated dusty cocoon — those are the picture the paper *adopts*, not what it measures.

## Connections

- High-$z$ AGN census (mostly unobscured quasars): [[euclid-high-z-quasar-census]], [[high-z-quasar-pair-merger]]
- Jets lighting ambient gas (nearby analog, Hα not Lyα): [[jet-aligned-halpha-cgm]]
- Spectroscopic confirmation of optically selected rare objects (lenses, not radio galaxies): [[muse-desi-lens-confirmation]]
- Synthesis: [[black-hole-feedback-and-changing-look-agn]] (hidden early radio-loud population); light touch [[high-energy-astrophysics-multimessenger]] (jets as messengers)

## Open questions

- Independent $P_{500}$ with the $1+z$ factor, published as an erratum?
- NIR or ALMA redshift lock, and a jet-aligned Lyα map (the slit was perpendicular)?
- How many more $z\sim5$ radio galaxies does the dropout method yield once the steep-spectrum cut is dropped?

## Source

- `raw/analyses/2026-10-09_arxiv-2609.28632_most-powerful-radio-galaxy-z4946.md`
