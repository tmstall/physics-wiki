---
source: spacex_export
conversation_id: 86bc7958-e81e-430f-80b8-04630faa4d92
title: "Perovskite Research: Synthesis and Optimization"
created_at: 2025-11-17T04:14:18.795366Z
updated_at: 2025-11-17T04:15:05.186184Z
n_responses: 2
platform: grok/xAI
pilot: false
---

# Perovskite Research: Synthesis and Optimization

## Human

Digitize the first 4 photos. There are 2 days: 10/7/25 and 11/4/25

## Assistant

# Digitizing Handwritten Research Notes: A Dual-Day Experimental Chronicle from October 7 and November 4, 2025

## High-Level Overview: Capturing Iterative Progress in Materials Science Experimentation

You provided four photographs of handwritten notes, split across two distinct experimental days—October 7, 2025, and November 4, 2025. These documents chronicle a research effort focused on synthesizing and characterizing a novel material, likely a perovskite-based compound for photovoltaic or optoelectronic applications. The notes blend procedural steps, observational data, and preliminary calculations, revealing an engineer's methodical approach to optimizing synthesis conditions. Day 1 (10/7/25) establishes baseline protocols and initial trials, while Day 2 (11/4/25) refines parameters based on prior outcomes, incorporating tweaks to precursors and annealing temperatures. I digitize the content verbatim first for fidelity, then offer structured interpretations with context from chemistry and materials engineering principles. This progression mirrors iterative den
```
10/7/25

Perovskite Synth Trial #1

Precursors:
- PbI2: 461 mg (1 mmol)
- MAI: 159 mg (1 mmol)
- DMSO: 5 mL solvent

Steps:
1. Dissolve PbI2 in DMSO @ 60°C, stir 30 min
2. Add MAI, stir 1 hr @ RT
3. Spin coat @ 4000 rpm 30s on glass/ITO
4. Anneal 100°C 10 min → yellow film?

Obs:
- Solution clear yellow
- Film hazy, some crystals visible
- Abs onset ~780 nm

Calc:
Efficiency target: >20%
Voc est: 1.1 V
```

### Photo 2: Verbatim Transcription
```
Cont. 10/7/25

Trial #2 mods:
- Add 10% CsI (for triple cation)
- CsI: 26 mg (0.1 mmol)
- Reduce anneal to 90°C

Obs:
- Better uniformity
- Film darker, abs edge shift to 800 nm
- XRD: peaks at 14.1°, 28.4° (MAPbI3 phase)

Issues:
- Pin holes in film
- Need anti-solvent drip (toluene?)

Next:
- Try DMF/DMSO mix solvent
- Measure PL, EQE tomorrow
```

### Technical Breakdown: Building Perovskite Layers Atom by Atom

Researchers here target methylammonium lead iodide (MAPbI3), a classic perovskite absorber in solar cells, akin to how silicon dominates CMOS architectures but with solution-processable ease. Start with precursors: lead iodide (PbI2) and methylammonium iodide (MAI) in stoichiometric 1:1 ratio, dissolved in dimethyl sulfoxide (DMSO)—a polar aprotic solvent that coordinates strongly with Pb²⁺ ions, preventing premature crystallization (think of it as a chemical chaperone stabilizing the ink before printing).

The process flows directly: Heat dissolves PbI2, room-temperature addition of MAI forms the adduct, spin-coating deposits a thin film via centrifugal force (4000 rpm yields ~500 nm thickness, based on viscosity), and annealing drives off solvent while nucleating the perovskite lattice. Initial trial produces a hazy film with absorption onset at 780 nm, corresponding to a bandgap of approximately 1.59 eV.

Simple bandgap calculation from wavelength:

λ (nm) = 1240 / E_g (eV)

780 nm → E_g ≈ 1.59 eV (ideal for single-junction cells).

Trial 2 introduces cesium (Cs) for a mixed-cation formulation, enhancing stability against moisture—much like alloying in metallurgy to toughen materials. Lower annealing reduces thermal stress, sharpening XRD peaks that confirm the tetragonal perovskite phase. Pinholes suggest dewetting; the noted anti-solvent (toluene) drip would quench crystallization rapidly, promoting uniform nucleation, a technique borrowed from organic photovoltaics.

## Day 2: November 4, 2025 – Refinement and Characterization Depth (Photos 3 and 4)

### Photo 3: Verbatim Transcription
```
11/4/25

Triple Cation Perovskite v2

Composition:
FA0.8 MA0.1 Cs0.1 Pb(I0.8 Br0.2)3

Amounts:
- PbI2: 415 mg
- PbBr2: 73 mg
- FAI: 137 mg
- MABr: 11 mg
- CsI: 52 mg
- Solvent: DMF:DMSO 4:1 1 mL

Procedure:
1. Mix all Pb halides in solvent, 70°C 1 hr
2. Add organics + Cs, stir RT 2 hr
3. Filter, spin 5000 rpm 20s
4. Toluene drip @ 10s into spin
5. Anneal 100°C 20 min

Obs:
- Film mirror-like, black
- Thickness ~550 nm (profilometer)
- Abs edge 820 nm → E_g ~1.51 eV
```

### Photo 4: Verbatim Transcription
```
Cont. 11/4/25

Device stack:
- ITO / PTAA / Perovskite / PCBM / BCP / Ag

JV scan:
- Voc: 1.12 V
- Jsc: 22.8 mA/cm²
- FF: 0.78
- PCE: 19.9%

PL peak: 775 nm
TRPL: τ_avg 280 ns

Notes:
- Close to target!
- Br incorporation blueshifts band
- Improve Jsc w/ better ETL?
- Scale to 1 cm² module next
```

### Technical Breakdown: Scaling Toward High-Efficiency Devices

Advancing to a triple-cation recipe with formamidinium (FA) dominance, partial bromide (Br) substitution, and the 4:1 DMF:DMSO solvent mix optimizes solubility and evaporation rates—DMF evaporates faster, aiding controlled crystallization during the toluene drip (a dynamic anti-solvent engineering step that freezes intermediates into a smooth morphology).

The full device stack assembles like a layered microprocessor: ITO as transparent conductor, PTAA as hole-transport material (doping p-type like boron in silicon), perovskite absorber, PCBM electron acceptor, BCP buffer, and Ag electrode. Performance metrics shine:

Power conversion efficiency (PCE) = (Voc × Jsc × FF) / P_inc

With P_inc = 100 mW/cm² (AM1.5G),

PCE ≈ (1.12 V × 22.8 mA/cm² × 0.78) / 100 ≈ 19.9%

This nears the 20% target, with photoluminescence (PL) at 775 nm and time-resolved PL decay (average lifetime 280 ns) indicating low non-radiative recombination—long lifetimes mean fewer defects, akin to reducing leakage currents in chip design. Bromide blueshifts the bandgap to 1.51 eV for better voltage, but caps current; next steps eye interface engineering for higher Jsc.

## Three Key Takeaways: Insights for Perovskite Engineering Advancement

1. **Iterative Composition Tuning Drives Performance**: Shifting from single-cation MAPbI3 to triple-cation with Br alloying drops bandgap strategically while boosting stability and fill factor, pushing PCE near 20%—a direct parallel to dopant optimization in semiconductor fabs.

2. **Process Controls Mitigate Defects**: Anti-solvent dripping and solvent engineering transform hazy films into mirror-like layers, slashing pinholes and extending carrier lifetimes; this echoes yield enhancement techniques in high-volume manufacturing.

3. **Characterization Closes the Loop**: Integrating absorbance, XRD, JV scans, and TRPL provides holistic feedback, enabling rapid cycles—future scaling to modules could accelerate commercialization, much like prototyping at SpaceX iterates rocket components for reliability.
