---
tags: [papers, black-holes, direct-collapse, high-z, jwst, seeding]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [early-universe-popiii-flash-ionization, glimpse-17775-cocoon, direct-bh-mass-lrd-abell2744, euclid-high-z-quasar-census, astrid-bh-occupation-fraction]
source_analysis: "raw/analyses/2026-09-22_doi-10.1093-mnras-stag1230_hunting-first-cosmic-giants-direct-collapse-black-holes.md"
---

# Local Ultraviolet Weather and Direct-Collapse Seeds

**One-line summary:** Tracking the ultraviolet light each proto-galaxy actually receives from its neighbors, instead of a region-wide average, turns on direct-collapse black-hole seeds by $z \approx 22$ in one massive quasar halo; most of those seeds barely grow, and the testable product is a few faint JWST companions. Trinca et al., *MNRAS* (2026).

## Key claims and results

- **Paper:** Alessandro Trinca, Alessandro Lupi, Zoltán Haiman, Marta Volonteri, Rosa Valiante, Raffaella Schneider, Roberto Decarli. *MNRAS* **551**, 1–19 (2026). DOI [10.1093/mnras/stag1230](https://doi.org/10.1093/mnras/stag1230). Accepted 18 June 2026.
- One zoom-in merger tree (Lupi et al. 2019): a halo of about $3 \times 10^{12}\,M_\odot$ at $z = 6$, walked by the Cosmic Archaeology Tool across ~30,000 progenitors. Light Pop III remnants and heavy seeds run in parallel. Heavy seeds are fixed at $10^5\,M_\odot$ and need an atomic-cooling halo, near-pristine gas, and a Lyman–Werner flux above $J_{\rm crit}$.
- Local flux is a point-source sum, $J_{\rm LW} \propto \sum L_i / r_i^2$, not a radiative-transfer solve. Fiducial $J_{\rm crit} = 300\,J_{21}$ gives **54** heavy seeds versus **47** for the old uniform background. The count barely moves. The clock does: local hot spots start at $z \approx 22$, and about 10 of 54 are already in by $z > 17$, while the average-field run waits until $z \approx 17$–18. A stricter bar at $1000\,J_{21}$ still yields 24 seeds, earliest again near $z \approx 22$.
- Metal winds cut the channel and do not close it. A conservative 7 kpc enrichment sphere leaves 13 of 54 seeds in pristine gas; a 2 kpc sphere leaves 24 of 54.
- Formation is not growth. Only 5 seeds (6 by $z = 7$) pass $\log(M/M_\odot) = 6.5$. The rest stay near the birth mass and sit as faint satellites. Synthetic spectra then predict **~3–5** AGN-like companions in deep NIRCam F444W ($m \sim 29$–31) around a bright $z \approx 7$ quasar, and a cosmological heavy-seed density of roughly $3 \times 10^{-8}$ to $4 \times 10^{-7}$ per comoving cubic megaparsec.
- CAT matches the parent hydro run to about 0.5 dex on the main branch. Accretion uses a calibrated boost $\alpha = 90$ and an Eddington cap.

## Physical intuition

Eddington-capped growth is compound interest with a hard rate. From a $100\,M_\odot$ stellar remnant to $10^9\,M_\odot$ takes on the order of 800 Myr of uninterrupted maximum growth. A $10^5\,M_\odot$ seed needs about 460 Myr, which can fit before $z \approx 7$ with room for stalls. Direct collapse is the buffer that holds the gas: Lyman–Werner light shuts off molecular cooling, the halo keeps growing, and atomic cooling later dumps the whole reservoir in one collapse.

The new move is local weather. A galaxy next to one bright neighbor crosses the suppression threshold long before the neighborhood average does. The seeds that matter for a JWST search are mostly the ones that never became the central quasar.

## Limitations and assumptions

- One halo, one merger tree. The authors say the next step is less extreme environments.
- The flux is inverse-square bookkeeping on top of a volume-averaged metallicity floor, with two unquantified biases (too much enrichment in close pairs, too little in the outskirts).
- Seed mass is a single number. Other groups argue fragmentation can cap direct collapse nearer $10^4\,M_\odot$.
- Detectable counts assume a dust-to-metal ratio of 0.3 and an SMC attenuation law. Little red dots may be dustier than that.
- No direct-collapse object has been identified. The JWST companion count is a prediction.

## Connections

- Different heavy-seed channel (WIMP-heated supermassive stars, and a much higher comoving density): [[early-universe-popiii-flash-ionization]]. Do not add the two number densities.
- Grown high-$z$ holes, not the starved satellites: [[glimpse-17775-cocoon]], [[direct-bh-mass-lrd-abell2744]], [[euclid-high-z-quasar-census]]
- Occupation versus seeding rules in a different simulation: [[astrid-bh-occupation-fraction]]
- Synthesis: [[black-hole-feedback-and-changing-look-agn]], [[cosmology-expansion-history-and-structure]]

## Open questions

- Does the $z \approx 22$ head start survive a second group’s chemistry and a second halo?
- Do deep quasar fields show the predicted faint, variable companions, or a systematic null?

## Source

- `raw/analyses/2026-09-22_doi-10.1093-mnras-stag1230_hunting-first-cosmic-giants-direct-collapse-black-holes.md`
