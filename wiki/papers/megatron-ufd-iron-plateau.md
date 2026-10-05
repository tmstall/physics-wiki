---
tags: [papers, galaxies, ultra-faint-dwarfs, population-iii, chemical-evolution]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [early-universe-popiii-flash-ionization, loki-early-accreted-vmp, ancient-immigrant-lmc-star, tempos-metal-poor-o-stars, imf-variation-milky-way, bottom-heavy-imf-early-galaxies]
source_analysis: "raw/analyses/2026-10-02_arxiv-2510.05232_megatron-pop3-iron-plateau-ultra-faint-dwarfs.md"
---

# MEGATRON: Iron Plateau in the Smallest Dwarf Galaxies

**One-line summary:** In one proto-Milky-Way zoom, ultra-faint dwarfs pile up near [Fe/H] ≈ −2.5 because one pair-instability supernova dumps a few solar masses of iron into a gas tank whose size is pinned by ultraviolet light from the growing galaxy next door. The predicted iron-poor tail is not yet seen. arXiv:2510.05232 (Rey et al.).

## Key claims and results

- **Paper:** Rey et al. (31 authors), arXiv:2510.05232v2 [astro-ph.GA], 4 Sept 2026. Preprint; referees are thanked, but no journal citation was confirmed at analysis time.
- MEGATRON is a RAMSES-RTZ radiation-hydro zoom of VINTERGATAN Halo 599, run only to redshift 8. Resolution ~3 pc and 2.5×10⁴ M☉ dark-matter particles, with non-equilibrium chemistry for 80+ species and individual Population III stars.
- Pop III masses are a lognormal peaking at 100 M☉, identical in all four runs. Outcomes: core-collapse (~10–20 M☉), hypernovae (~20–40), pair-instability supernovae (PISNe, ~140–300 M☉, ~5×10⁵² erg), or direct collapse with no metals. The realized budget is ~3,500 PISNe, ~90 hypernovae, and **no** ordinary core-collapse events, because the mass function is top-heavy.
- The four variants change only Pop II feedback (baseline, burstier supernovae, a varying IMF, hypernovae plus higher star-formation efficiency). Below ~10⁵ M☉ in stars, all four show the same pile-up near [Fe/H] ≈ −2.5 and a tail toward −5. The text says ~78% of faint dwarfs sit between −3 and −2 and ~22% sit below −3. A figure legend (8 / 876 / 303) is closer to 74% / 26%. The high-mass end **does** care about Pop II: the weakest-outflow run overshoots above ~10⁶ M☉.
- Mechanism: almost every faint dwarf hosts exactly one Pop III explosion (~6% have two, ~2% are enriched from outside). Plateau dwarfs mostly saw a heavy PISN (160–300 M☉, a few M☉ of iron). Tail dwarfs often saw a light PISN (140–160 M☉, ~0.5 M☉ of iron) — a factor of ten, one dex in [Fe/H].
- Why the tank is fixed: Lyman–Werner light from the proto-Milky Way destroys H₂, so Pop III stars form in halos of ~5–30×10⁶ M☉. Those wells retain metals from a ~10⁵²–10⁵³ erg blast. Diluting 5 M☉ of iron into the hydrogen of a 10⁷ M☉ halo lands near [Fe/H] ≈ −2.5 to −2.6. The same arithmetic with 0.5 M☉ of iron lands near −3.5, and a core-collapse yield in a 10⁵ M☉ halo can fake −2.5. The plateau value alone does not name the explosion.
- Bridge to redshift 0: most simulated dwarfs are still forming stars at z = 8. The already-quenched subset (3, 28, 17, and 51 galaxies across the four runs) has a statistically compatible iron distribution (p ≥ 0.1). Dark-matter-only tagging says ~1/4 of the faint dwarfs survive as intact satellites today. Aging shifts stellar mass by 0.2–0.3 dex and does not change the shape.
- Carbon and magnesium are broadly acceptable (carbon ~0.5 dex low). Nitrogen is orders of magnitude too low, as expected if PISNe dominate (they make almost no nitrogen).

## Physical intuition

Ultra-faint dwarfs are write-once chips. Reionization heats the intergalactic gas, tiny halos cannot accrete, and star formation stops. Their stars are a frozen record of the first enrichment.

The plateau is division, not a new force law. Ultraviolet light from the neighbor sets a minimum halo size, so the gas tank is about the same galaxy to galaxy. A top-heavy first generation then drops one large iron payload into that tank. Payload over tank is [Fe/H] ≈ −2.5. A smaller payload, still one explosion, is the tail.

The robustness the abstract stresses is robustness to **later** stars. The knobs that set the plateau — Pop III masses, yield tables, and the ultraviolet bath — are shared by all four runs and were not varied.

## Limitations and assumptions

- One zoom, one code, one unusually strong ultraviolet environment. Isolated dwarfs in earlier work lose PISN metals more easily. A different published yield set would, the paper says, fatten the tail and thin the plateau.
- The iron-poor tail is the real prediction, and it is in tension with the sky. Among 38 observed dwarfs used in the paper, none has a galaxy-average [Fe/H] ≤ −3. If those averages were fair draws, the chance of seeing none is ~0.02% (the printed inequality sign looks flipped; the arithmetic matches the tail). The rescue is that averages from a few stars are biased high: Pictor II sits at −2.99, one star at or below −4 has been found, and even plateau dwarfs have individual stars that metal-poor. Plausible, not yet a population test.
- Redshift-8 star-forming galaxies are not local fossils. The quenched subset is small, and the dark-matter tags omit gas, a disk, and baryonic tides.
- Uniform mixing is a toy. Real halos mix imperfectly.
- PISN patterns are scarce in Milky Way halo stars. The authors’ answer is that ultra-faint dwarfs supply at most ~1% of halo stars. That removes a contradiction. It does not show the pattern is there.
- The 100 M☉ peak is an input motivated by older simulations, not a result of this run.

## Connections

- First stars as ionizing engines and heavy seeds (different mass scale, ~10⁵ M☉ vs ~100 M☉): [[early-universe-popiii-flash-ionization]]
- Local chemical fossils of accreted dwarfs: [[loki-early-accreted-vmp]], [[ancient-immigrant-lmc-star]], concept [[ultra-metal-poor-stars]]
- Low-metallicity massive stars today, not Pop III yields: [[tempos-metal-poor-o-stars]]
- IMF shape as a separate lever: [[imf-variation-milky-way]], [[bottom-heavy-imf-early-galaxies]]
- Synthesis: [[cosmology-expansion-history-and-structure]] (assembly fossils, not an expansion-history ruler)

## Open questions

- Does a complete ultra-faint census show ~1 in 5 galaxies with average [Fe/H] ≤ −3? A null would push the first-star mass function even more top-heavy, or to another origin.
- Do nitrogen (and the missing PISN abundance fingerprint) survive once winds and rotation are in the yields?
- Does another code, in a quieter ultraviolet environment, still pin the tank near 10⁷ M☉?

## Source

- `raw/analyses/2026-10-02_arxiv-2510.05232_megatron-pop3-iron-plateau-ultra-faint-dwarfs.md`
