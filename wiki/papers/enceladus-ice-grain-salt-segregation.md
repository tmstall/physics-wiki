---
tags: [papers, planetary-science, enceladus, cassini, ocean-worlds, ice-grains]
last_updated: 2026-10-09
status: analysis-ingest
related_papers: [chondrite-pressure-bump, ch3oh-hcn-3i-atlas-outgassing, volatile-depletion-hybrid-accretion]
source_analysis: "raw/analyses/2026-10-05_doi-10.1126-sciadv.aee7256_enceladus-ice-grain-salt-segregation-cassini-cda.md"
---

# Enceladus Ice Grains: Slow Freeze, Then Shatter

**One-line summary:** Cassini CDA Type 3 (salty) ice grains from Enceladus mostly carry *one* salt each; the working picture is slow freezing of large ocean droplets in the lower vents, then wall-collision shattering into micrometre one-salt fragments. Postberg et al., *Science Advances* 12(39), eaee7256 (2026).

## Key claims and results

- **Paper:** Frank Postberg, Zenghui Zou, Yasuhito Sekine, Minori Koga, Jürgen Schmidt, Mark Fox-Powell, Fabian Klenner, Jon K. Hillier, Nozair Khawaja et al. (13 authors; Ralf Srama last). DOI 10.1126/sciadv.aee7256. Open access. Combined CDA reanalysis, lab freezing, equilibrium chemistry, and a published vent model (Pankine 2023).
- Sample: 961 salty E-ring grains from 7,353 spectra (2004–2008, before plume-crossing contamination). Chloride and carbonate grains ~23% each; only 12 grains (1.2%) carry both. Phosphate: 9 grains, none mixed with chloride or carbonate. Independence would predict ~88 chloride+carbonate grains among 627 classifiable sodium grains; chance of the observed split is ≪10⁻¹⁰.
- Almost every grain also shows Na/K hydroxide (exactly one grain lacks it). Potassium appears only as chloride, never carbonate or phosphate; ~2/3 of K-rich grains also carry sodium.
- Lab: 200 µm analog droplets on a cold plate. At 5–10 K/min, Cl sits in sharp hot spots matching K, while carbonate fills the rest. Flash freeze and 20 K/min mix the salts. 15 µm droplets barely separate (no room). At 1 K/min, K moves into carbonate (K-carbonate, never seen by Cassini) — so the window is slower than ~20 K/min, faster than ~1 K/min.
- Equilibrium sequence: phosphate ~−1 °C, carbonate ~−4 °C, then KCl and NaCl together ~−22.5 to −24 °C. Maps onto Cassini subtypes (pure phosphate; carbonate without phosphate; K often with NaCl).
- Vent: droplet cooling rate = wall gradient × rise speed. Pankine 1,500 m crack: slow zone (≲20 K/min) in the lowest ~75% of the vent, ~1–2 minutes, gas ~10 m/s. Upper vent accelerates to hundreds of m/s; ice-fragmentation thresholds then shatter ≳10–100 µm parents into the 1–2 µm grains Cassini measured.

## Physical intuition

The old Type 3 picture was flash-frozen seawater: each micrometre grain is a tiny cup of the whole ocean. Averaging cups gives the recipe. This paper says the factory is two-stage. Lower vent: slow conveyor through a gently cooling oven. Each salt crystallizes in its own temperature window and gets walled in by ice. Upper vent: high-speed chute into a crusher. Weak salt–ice boundaries prefer to break, so fragments are mostly one salt.

A bulk melt of many grains still recovers ocean *ratios*. Absolute concentrations get noisier (fragments need not keep the parent’s salt fraction; all pick up condensed ice). Rare ingredients (rarer than phosphate) appear in very few grains at high concentration — so the next plume mission wants single-grain instruments, not a blender.

## Limitations and assumptions

- Single collaboration (reanalysis, lab, interpretation). Confirmation needs another team on public CDA spectra, a second lab with free-floating low-pressure droplets, and eventually a plume fly-through.
- Hydroxide is not in the equilibrium sequence. Lab Na–O spots near CO₂ voids are a lead, not a demonstration. Hydroxide also forms away from voids.
- Text says slow cooling holds until gas drops below 255 K. Digitized Fig. 11 ends the slow zone near 262 K (~−11 °C); 255 K is already >40 K/min. Fallback (only phosphate and carbonate must precipitate slowly) keeps the mechanism; the 255 K match is overstated.
- Plate-frozen droplets flatten ~4:1; 15 µm lab grains barely sort, so parent droplets need to be tens to hundreds of micrometres. Fragmentation thresholds used are for *pure* ice; salt–ice boundaries should be weaker (unmeasured).
- Vent treated as steady. Real tiger-stripe cracks change shape, and tides raise and lower the water table by tens of metres each 33-hour orbit.
- Ensemble ocean recipe survives; grain-by-grain reading does not replace it. Organics-sorting is proposed, not shown.

## Connections

- Solar-system chemistry / small-body volatiles: [[ch3oh-hcn-3i-atlas-outgassing]], [[chondrite-pressure-bump]]
- Rocky-planet volatile loss (different body, same “what the missing salts record” question): [[volatile-depletion-hybrid-accretion]]
- Islands planetary shelf; no synthesis hub yet

## Open questions

- Independent re-classification of public CDA Type 3 spectra?
- Free-floating droplet freeze at Enceladus vent pressure, not on a steel plate?
- ESA Enceladus / NASA Orbilander dust instruments: single-grain vs bulk melt?

## Source

- `raw/analyses/2026-10-05_doi-10.1126-sciadv.aee7256_enceladus-ice-grain-salt-segregation-cassini-cda.md`
