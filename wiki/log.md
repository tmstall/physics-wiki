# Wiki activity log

Append-only. Newest entries at the bottom.

---

## [2026-07-31] ingest | Batch 1 — quantum clocks, massive cats, superradiant laser

Ingested four analyses from `raw/analyses/` (left `Quantum Jamming.md` for a later batch).

### Papers created
- `wiki/papers/time-goes-quantum.md` — from *Time Goes Quantum.md*
- `wiki/papers/quantum-proper-time-ion-clocks.md` — from *Quantum Proper Time Goes Live in Ion Clocks.md*
- `wiki/papers/massive-tunneling-schrodinger-cats.md` — from *Quantum Tunneling…608-Dalton…*
- `wiki/papers/collective-superradiant-lasing.md` — from *The Atom-Synchronized Clock…* (Reilly et al. PRL 2026)

### Concepts created
- Quantum relativity / ion metrology: `quantum-proper-time`, `second-order-doppler-shift`, `optical-ion-clocks`, `motional-squeezing`, `ramsey-interferometry`
- Cold atoms: `collective-tunneling`, `noon-states`, `optical-lattices`, `mott-insulator`
- Active clocks: `superradiance`, `cavity-pulling`, `active-atomic-clocks`

### Index
- Created `wiki/index.md` as master catalog

### Notes / caveats
- Writing kept intuition-first and math-light per AGENTS.md.
- Several analyses note reconstructed details without full PDF verification; paper pages mark provisional numerical claims.
- Cross-links established between the two proper-time ion-clock papers; Ramsey page links all three sensing papers.
- Empty root-level `index.md` / `log.md` left untouched; schema lives under `wiki/`.

---

## [2026-07-31] ingest | Batch 2 — six analyses (jamming, randomness, cosmology, soft matter, ISR)

Ingested remaining + newly dropped analyses in `raw/analyses/`.

### Papers created
- `wiki/papers/quantum-jamming.md` — multipaper jamming / monogamy / ONS debate
- `wiki/papers/certified-randomness-amplification.md` — ETH loophole-free Bell randomness amplification
- `wiki/papers/boronate-velcro-synthetic-cells.md` — one-pot MCM protocells
- `wiki/papers/cigars-i-supernova-cosmology.md` — hierarchical SN Ia + TMNRE
- `wiki/papers/cosmos-web-cosmic-web.md` — Hatamnia et al. ApJ 2026 cosmic web to \(z\sim7\)
- `wiki/papers/levinthal-high-pt-isr.md` — ISR high-\(p_T\) thesis chapter (*thin source*: outline only)

### Concepts created
- Foundations/crypto: `quantum-jamming`, `monogamy-of-entanglement`, `no-signaling`, `device-independence`, `bell-tests`, `randomness-amplification`
- Cosmology: `cosmic-web`, `environmental-quenching`, `photometric-redshifts`, `type-ia-supernovae`, `mass-step`, `simulation-based-inference`
- Soft matter: `coacervates`, `dynamic-covalent-chemistry`, `synthetic-cells`
- Particle physics: `high-pt-scaling`, `parton-jets`

### Index
- Rebuilt `wiki/index.md` with themed paper/concept sections; all 10 analyses marked ingested

### Notes
- Bidirectional links between jamming ↔ randomness via Bell / DI / no-signaling; CIGaRS ↔ COSMOS-Web via photo-\(z\) and large photometric samples
- `David Thesis.md` lacks full prose — paper page flagged `analysis-ingest-thin-source`
- Style: intuition-first, active voice, math-light per AGENTS.md

---

## [2026-07-31] ingest | Batch 3 — five papers (GR freeze-in, BH evaporation, SnV SUPER, weak values, WDM)

### Pre-clean
- Scanned new batch files for `![](data:image/png;base64,` images.
- Permanently stripped all such images from:
  - `raw/analyses/frozen gravity.md` (10 images; ~5.7 MB → ~0.2 MB)
  - `raw/analyses/Evaporating Charged Black Holes Avoid Singularities.md` (3 images)
- Other batch files had zero base64 images. Skipped already-ingested files for this clean pass.
- Skipped `Gemini Learnings.md` (not a paper analysis).

### Papers created
- `wiki/papers/frozen-in-gravitational-fields.md`
- `wiki/papers/evaporating-charged-black-holes.md`
- `wiki/papers/snv-super-coherent-excitation.md`
- `wiki/papers/negative-weak-valued-excitation-times.md`
- `wiki/papers/filming-plasma-birth.md`

### Concepts created
- GR/BH: `frozen-in-gravity`, `gravitational-helicity`, `weyl-curvature`, `hawking-radiation`, `null-energy-condition`, `reissner-nordstrom`, `black-hole-interiors`
- Quantum optics foundations: `weak-values`, `group-delay`, `coherent-forward-scattering`
- Solid-state networks: `color-centers`, `super-scheme`, `spin-photon-interface`
- Plasma/HED: `warm-dense-matter`, `xfel-pump-probe`, `inertial-confinement-fusion`

### Cross-links
- Frozen-in ↔ evaporating BH (GR interiors); evaporating BH ↔ quantum-jamming (horizons); weak values ↔ quantum-proper-time (different “quantum time”)

### Index
- Updated paper/concept sections and raw inbox status (15 paper analyses tracked)

---

## [2026-07-31] ingest | Batch 4 — five papers (GW DM, double-copy Hawking, ISR, HOLISMOKES, SPHEREx ice)

### Pre-clean
- Scanned new batch files for `![](data:image/png;base64,` images.
- Permanently stripped all such images from:
  - `raw/analyses/Hawking Radiation from a Charge Shel.md` (20 images)
  - `raw/analyses/High-pT Physics at the CERN ISR.md` (7 images)
- Other batch files had zero base64 images.

### Papers created
- `wiki/papers/gw-induced-fermion-freeze-in.md` — Maleknejad & Kopp PRL 2026
- `wiki/papers/hawking-radiation-charge-shell.md` — double-copy Vaidya/charge shell thermality
- `wiki/papers/high-pt-physics-cern-isr.md` — fuller ISR high-\(p_T\) narrative (links [[levinthal-high-pt-isr]])
- `wiki/papers/holismokes-sn-winny.md` — HOLISMOKES XIX & XX lensed SLSN Winny
- `wiki/papers/interstellar-glaciers-spherex.md` — SPHEREx ice maps

### Concepts created
- DM/GWs: `freeze-in`, `conformal-invariance`, `stochastic-gw-background`, `fermionic-dark-matter`
- Double copy: `double-copy`, `vaidya-spacetime`, `bogoliubov-coefficients`
- Lensing: `strong-gravitational-lensing`, `time-delay-cosmography`, `hubble-tension`, `superluminous-supernovae`
- ISM: `interstellar-ice`, `spherex`, `pahs`, `giant-molecular-clouds`

### Cross-links
- Charge-shell Hawking ↔ existing `hawking-radiation` / evaporating BH cluster
- ISR full paper ↔ thin Levinthal outline + high-pt concepts
- HOLISMOKES ↔ Type Ia SN / Hubble-tension path
- Index now tracks 20 paper analyses

---

## [2026-07-31] synthesis | Two cross-cutting pages filed

### Created
- `wiki/synthesis/quantum-time-across-platforms.md` — ion proper time / SODS / revivals + weak-valued dwell times + massive tunneling NOON Ramsey duration
- `wiki/synthesis/black-hole-evaporation-energy-conditions.md` — evaporating RN + NEC, double-copy charge-shell Hawking, frozen-in topology, jamming side door; agreements and tensions

### Bookkeeping
- Bidirectional links from core papers/concepts back to each synthesis
- `wiki/index.md` Synthesis section populated (was placeholder)

---

## [2026-08-01] ingest | Batch 5 — four analyses (3 new papers + Sorci consolidate)

### Pre-clean
- Stripped `![](data:image/…)` images from:
  - `Ion Clocks Enter the Quantum Proper-Time Regime.md` (3)
  - `Kinetic Barcoding Cracks One-Pot.md` (3)
  - `Lattice Stretch Flips the Switch.md` (6)
- `Loki - Early Accreted VMP Stars.md`: zero data images

### Papers
- **Consolidated:** Sorci et al. *Quantum Signatures of Proper Time…* PRL 136, 163602 (2026) into existing [[quantum-proper-time-ion-clocks]] (full DOI/arXiv + dual analysis sources; not a second paper page)
- **New:** [[kinetic-barcoding-cas13a]], [[siv-hydrostatic-strain-symmetry]], [[loki-early-accreted-vmp]]

### Concepts created
- Diagnostics: `cas13a`, `kinetic-barcoding`, `droplet-microfluidics`
- Diamond strain: `silicon-vacancy`, `hydrostatic-strain` (updated `color-centers`)
- Galactic archaeology: `very-metal-poor-stars`, `chemical-tagging`, `galactic-accretion`

### Cross-links
- SiV ↔ SnV / color centers; Loki ↔ COSMOS-Web assembly narrative
- Index + log updated

---

## [2026-08-01] ingest | Batch 6 — seven papers + List1 extract / List2 defer

### Pre-clean
- Stripped data:image markdown from `Magnesium Hijacks the Benzidine Rearrangement.md` (3) and `Photonic Supersolid.md` (8)
- Lists had zero base64 data images

### Papers created (7)
- Standalone: [[magnesium-benzidine-rearrangement]], [[newton-ksz-force-law]], [[photonic-supersolid]]
- From List1 only: [[plasma-relativistic-amplifier]], [[pre-bang-leftovers]], [[pulsars-satellite-masses]], [[quantum-metallurgy-cdw]]

### Concepts created (~18)
- Chem: benzidine-rearrangement, biaryl-scaffolds
- Gravity/cosmo: ksz-effect, pairwise-velocity, modified-newtonian-dynamics, bouncing-cosmology, primordial-black-holes, particle-horizon
- Photonics: supersolid, exciton-polaritons, bound-state-in-the-continuum
- Laser plasma: relativistic-oscillating-mirror, coherent-harmonic-focus
- CDW: charge-density-wave, kthny-melting, hexatic-phase
- Pulsars: millisecond-pulsars

### Notes
- `List2_Combined_Clean.md` deliberately **not** fully ingested (large remaining set: dark-matter vortices, Shor budget, chondrite dust trap, collapse models, magnon flip-flop, SMBH pairs, etc.) — next batch candidate
- Wiki paper count ~30

---

## [2026-08-01] lint | Stub fold + index rebuild

### Thin stubs
- **Deleted 44** single-paper / low-value concept stubs (content folded into parent papers as plain-language terms where links were scrubbed).
- **Kept 41** multi-paper hubs or synthesis-critical concepts (e.g. quantum-proper-time, black-hole-interiors, hubble-tension, color-centers).

### Index
- Rebuilt `wiki/index.md` by major clusters + final **Islands / Other** section.
- Removed demoted concepts from the catalog; paper count still ~30.

---

## [2026-08-01] ingest | List2 first 10 — batch 7

### Pre-clean
- Scanned all List2 sections for this batch in `raw/analyses/List2_Combined_Clean.md`
- **Zero** `![](data:image/…)` base64 images remaining (List2 already cleaned / IMAGE REMOVED markers only)

### Papers created (10)
1. `wiki/papers/alena-tensor-rotation-dm.md` — Ogonowski Alena Tensor / rotational energy as halo
2. `wiki/papers/shor-algorithm-budget.md` — neutral-atom + qLDPC Shor resource estimate
3. `wiki/papers/chondrite-pressure-bump.md` — single Jupiter dust trap → CC diversity
4. `wiki/papers/collapse-models-clock-precision.md` — Bortolotti et al. collapse noise → clock floor
5. `wiki/papers/spin-flip-flop-saf.md` — magnon mode hop in synthetic antiferromagnet
6. `wiki/papers/ancient-immigrant-lmc-star.md` — SDSS J0715−7334 extreme UMP / LMC
7. `wiki/papers/smbh-inclination-angle.md` — ~20° / ~45° SMBH pairing filter
8. `wiki/papers/aquila-booster-pevatron.md` — LHAASO PeVatron PWN efficiency crisis
9. `wiki/papers/b-meson-fcnc-anomaly.md` — LHCb `B→K*μμ` / `C9` anomaly
10. `wiki/papers/desi-evolving-dark-energy.md` — DESI BAO evolving dark energy

### Concepts created (~17)
- Gravity/DM: `alena-tensor`
- QC: `qldpc-codes`, `neutral-atom-qubits`
- Foundations: `spontaneous-collapse-models`
- Cosmology: `baryon-acoustic-oscillations`, `dark-energy-equation-of-state`
- Galactic archaeology: `ultra-metal-poor-stars`, `population-iii`
- Magnonics: `synthetic-antiferromagnets`, `magnons`
- SMBH dynamics: `dynamical-friction`, `supermassive-black-hole-binaries`
- UHE / PWN: `pevatron`, `pulsar-wind-nebulae`
- Flavor: `flavor-changing-neutral-current`, `wilson-coefficients`
- Planetary: `pressure-bumps`

### Concepts updated (bidirectional)
- `modified-newtonian-dynamics` ↔ Alena Tensor
- `hubble-tension` ↔ DESI / DE equation of state
- `quantum-proper-time` ↔ collapse-model clock floor
- `galactic-accretion` + `loki-early-accreted-vmp` ↔ Ancient Immigrant

### Index
- Rebuilt `wiki/index.md`: 40 papers · 58 concepts · 2 synthesis
- New/extended clusters: high-energy astrophysics (UHE), flavor/collider, planetary, QC resource estimates under foundations/crypto
- List2 remaining ~15 sections still deferred

### Notes
- Style kept intuition-first / math-light per AGENTS.md
- Several analyses flag reconstructed numbers; paper pages mark provisional claims where noted
- Prefer multi-paper concept hubs; single-paper concepts kept only where they are clear cross-link anchors

---

## [2026-08-01] ingest | List2 next 8 — batch 8

### Pre-clean
- Scanned List2 sections 11–18 in `raw/analyses/List2_Combined_Clean.md`
- **Zero** `data:image/` base64 images (already clean)

### Papers created (6 new)
1. `wiki/papers/3d-electron-diffraction-osc.md` — Kraus et al. 3D ED for OSC films
2. `wiki/papers/ic1262-metal-mixing.md` — galaxy group metal transport (sloshing/shock/jet)
3. `wiki/papers/eta-prime-mesic-nucleus.md` — Sekiya/Itahashi η′-mesic semi-exclusive search
4. `wiki/papers/ciss-homochirality.md` — Paltiel et al. CISS magnitude asymmetry / homochirality
5. `wiki/papers/color-superconductivity-qcd.md` — color SC / CFL / NS cores (List2 tutorial deep-dive; not a single DOI)
6. `wiki/papers/beam-driven-plasma-mirror.md` — ELI Beamlines particle-beam flying mirror pair

### Consolidated (2 List2 sections → existing pages)
- **Flavor Anomaly That Won't Die** = same LHCb PRL/arXiv as [[b-meson-fcnc-anomaly]] — dual analysis sources merged; DOI/arXiv + theory-limited plateau noted
- **Time Goes Quantum** (List2) = same program as [[time-goes-quantum]] — source note + collapse-model cross-link; no second page

### Concepts created (~14)
- Materials: `three-d-electron-diffraction`, `organic-solar-cells`
- Groups: `intragroup-medium`, `gas-sloshing`
- QCD/hadrons: `eta-prime-meson`, `mesic-nuclei`, `u1a-anomaly`, `color-superconductivity`, `color-flavor-locking`, `qcd-phase-diagram`
- Spin/bio: `chiral-induced-spin-selectivity`, `homochirality`
- Plasma: `relativistic-flying-mirror`, `plasma-wakefield`

### Cross-links
- Beam-driven mirror ↔ existing [[plasma-relativistic-amplifier]] (ROM)
- η′-mesic ↔ color SC / QCD vacuum cluster (new index section)
- CISS ↔ magnonics solid-state neighborhood
- B-meson page strengthened from second List2 analysis

### Index
- Rebuilt `wiki/index.md`: **46 papers · 72 concepts · 2 synthesis**
- New section: **QCD, dense matter & hadrons**
- List2 remaining ~6 unfiled paper analyses (+ frozen gravity already filed)

### Notes
- IC 1262 analysis flagged partial reconstruction — numbers marked provisional on paper page
- Color-superconductivity page explicitly tagged as tutorial/deep-dive, not peer-reviewed single paper

---

## [2026-08-01] lint | Post–List2 batch 8 pass (report only)

### Scope
- 46 papers · 72 concepts · 2 synthesis
- Orphans, thin pages, missing high-value bidirectional links
- No large rewrites (per lint protocol)

### Headline findings
- True orphan papers: chemistry/biotech island (boronate zero outbound wikilinks; magnesium & kinetic-barcoding only mutual/island neighbors)
- No broken `[[wikilinks]]` targets
- Quantum-time synthesis not yet aware of collapse-model clock floor
- Cosmology SN ladder pages not yet linked back to DESI evolving DE
- Many List2 concepts remain single-paper hubs (expected post-batch; demote later if still lonely)

### Suggested next actions
- 4–6 bidirectional link adds (see lint report in chat)
- Optional thin-page deepening queue for island + provisional analyses

---

## [2026-08-01] lint-followup | Implement §2 bidirectional links

Applied all six high-value link suggestions from the post–List2 lint report:

1. `quantum-time-across-platforms` — new collapse-model side thread + map rows for `collapse-models-clock-precision` / `spontaneous-collapse-models`
2. `type-ia-supernovae` + `cigars-i-supernova-cosmology` → DESI / DE EOS / BAO
3. `certified-randomness-amplification` → `shor-algorithm-budget`
4. `cosmos-web-cosmic-web` → `ic1262-metal-mixing` (+ IGrM / sloshing)
5. `spin-flip-flop-saf` → `ciss-homochirality` / CISS (also `photonic-supersolid` → SAF for prior one-way)
6. `boronate-velcro-synthetic-cells` → kinetic barcoding + magnesium biaryl (closes zero-outbound island)

No content rewrites beyond Connections / synthesis glue text.

---

## [2026-08-01] lint-followup | Honorable-mention cross-links

- `smbh-inclination-angle` <-> `pulsars-satellite-masses` (dynamical friction / satellite vs SMBH pairing)
- `photonic-supersolid` <-> `spin-flip-flop-saf` already closed in prior §2 pass
- Bonus on pulsars page: light pointers to Aquila PeVatron / PWN concepts

---

## [2026-08-01] ingest | List2 final remainder — batch 9 (List2 complete)

### Pre-clean
- Scanned remaining List2 sections (Topology … frozen gravity)
- **Zero** `data:image/` base64 images

### Papers created (6)
1. `topological-cosmological-constant.md` — Alexander et al. gravitational θ-vacua / CSK
2. `high-z-quasar-pair-merger.md` — Yue et al. J2037−4537 dual quasars at z=5.7
3. `mrk501-double-jet-smbbh.md` — Britzen et al. VLBA double jet / close binary
4. `ultramassive-bh-binary-cavity.md` — McDonald et al. A402 core-scouring cavity
5. `w-state-entangled-measurement.md` — Park et al. W-state entangled measurement
6. `bata2s5-field-induced-sc.md` — Zhao et al. BaTa2S5 field-induced SC phases

### Consolidated (1)
- List2 `frozen gravity.md` → existing [[frozen-in-gravitational-fields]] (+ topology CC cross-link)

### Concepts created (~10)
- QG/Λ: `gravitational-theta-vacua`, `ashtekar-variables`
- SMBH: `dual-agn`, `core-scouring`, `pulsar-timing-arrays`, `blazars`
- QI: `w-states`, `entangled-measurements`
- SC: `spin-triplet-superconductivity`, `ising-superconductivity`

### Hub updates
- `supermassive-black-hole-binaries`, `smbh-inclination-angle`, `desi-evolving-dark-energy` bidirectional links into new papers

### Index
- **52 papers · 82 concepts · 2 synthesis**
- List2 marked **fully ingested**

---

## [2026-08-01] stub+index | Aggressive concept stub cleanup + index rebuild

### A. Thin stubs
- **Deleted / folded: 26** single-paper low-value concept stubs
- Useful one-line definitions folded into parent paper `Key terms` / Connections
- Inbound `[[wikilinks]]` rewritten to plain language or remaining hubs

**Deleted concepts:** ising-superconductivity, spin-triplet-superconductivity, blazars, charge-density-wave, homochirality, mesic-nuclei, neutral-atom-qubits, organic-solar-cells, pevatron, entangled-measurements, plasma-wakefield, population-iii, qldpc-codes, qcd-phase-diagram, core-scouring, ashtekar-variables, w-states, synthetic-antiferromagnets, three-d-electron-diffraction, color-flavor-locking, wilson-coefficients, freeze-in, superradiance, eta-prime-meson, color-superconductivity, u1a-anomaly

- **Kept: 56** multi-paper hubs, synthesis-critical, or multi-concept anchors

### B. Index
- Full rebuild of `wiki/index.md` by major clusters + **Islands / Other**
- Catalog: **52 papers · 56 concepts · 2 synthesis**

### C. Not done (per prompt)
- No new synthesis pages
- No broad link-addition pass beyond stub fold rewrites

---

## [2026-08-01] stub+index | Residual second pass

- Folded/deleted 2 more single-paper stubs: `pressure-bumps`, `relativistic-flying-mirror`
- Cumulative this cleanup cycle: **28 deleted**, **54 kept**
- Catalog: 52 papers · 54 concepts · 2 synthesis

---

## [2026-08-01] ingest | ITO nanocrystal fieldoscopy (missing paper)

### Pre-clean
- Copied `Watching a Nanocrystal Flip a Light Switch.md` into `raw/analyses/`
- Stripped `![](data:image/…)` base64 images (3)

### Paper
- `wiki/papers/ito-nanocrystal-fieldoscopy.md` — Herbst et al. Advanced Science 2025; fieldoscopy of ITO NC switch

### Concepts
- `fieldoscopy`, `epsilon-near-zero`

### Links
- Photonic supersolid + 3D-ED OSC neighbors; ultrafast plasma cousins noted

### Catalog
- **53 papers · 56 concepts · 2 synthesis**

---

## [2026-08-01] ingest | Export batch 1/8 (5 papers) — gravastars, GW gauge, shear, entropy, Big Ring

Controlled unattended run from `claude_export/extracted-analyses/` (target 40).

### Papers
1. `gravastar-dust-collapse` — Jampolski & Rezzolla PRD 2026
2. `second-order-gw-strain-gauge` — Newton-gauge TT as free-fall strain
3. `quantum-damping-cosmological-shear` — mLQC-I shear vs no-hair critique
4. `entropy-maximization-bh-mergers` — PRL entropy peak → remnant spin
5. `big-ring-ultra-large-structure` — Mg II Big Ring ~400 Mpc

### Concepts
`gravastars`, `induced-gravitational-waves`, `gravitational-wave-memory`, `loop-quantum-cosmology`, `cosmic-no-hair`, `black-hole-thermodynamics`, `cosmological-principle`, `large-scale-structure`

### Catalog after batch 1
- Papers: 58 · Concepts: 64 · Synthesis: 2
- Progress: 5 / 40

---

## [2026-08-01] ingest | Export batch 2/8 (papers 6–10) + lint links

### Papers
6. `star-jpsi-spin-interference` — STAR UPC J/ψ spin interference
7. `noise-driven-qubit-entanglement` — Kraus–Cirac noise entanglement
8. `brown-zak-nonlinear-transport` — Brown–Zak fermions via nonlinear voltage
9. `horizon-direct-wave-gw250114` — direct wave horizon thermodynamics
10. `mond-external-field-sparc` — EFE fingerprint on SPARC

### Lint (at 10 papers)
Bidirectional / hub links added:
- `black-hole-interiors` ↔ gravastars / entropy mergers / horizon direct wave
- `stochastic-gw-background` ↔ induced GW / second-order strain / memory
- `modified-newtonian-dynamics` ↔ mond-external-field-sparc
- `newton-ksz-force-law` ↔ mond-external-field-sparc (scale tension note)
- `black-hole-thermodynamics` ↔ horizon-direct-wave

### Progress: 10 / 40

---

## [2026-08-01] ingest | Export run complete — STOPPED at 40 papers

Controlled unattended ingest from `claude_export/extracted-analyses/`.

### Run structure
- Batches of 5; lint+links at 10; stub cleanup at ~20–40 end; **hard stop at 40**

### Totals this run
- **New papers ingested: 40**
- **New concept pages created (net after stub trim): ~8–10** (gravastars, induced-gw, LQC, BH thermodynamics, cosmological principle, fieldoscopy/ENZ already present from ITO, etc.)
- Catalog now: **93 papers · 61 concepts · 2 synthesis**

### Notable clusters added
- Gravastars / horizonless mimickers + BH thermodynamics / direct-wave horizon probes
- Induced GW strain gauge + memory language
- LQC shear damping vs cosmic no-hair
- MOND EFE on SPARC vs kSZ large-scale n≈2 tension
- Noise-driven entanglement + retrocausal channel capacity (QI)
- Euclid high-z quasars, Big Ring, Gpc anisotropy claims
- Ultrafast: attosecond STM, sunlight SPDC, photon-number optical analogy

### Skipped / not ingested
- Hard wiki duplicates in `_possible_wiki_duplicates/`
- Remaining extract files beyond the 40 (still in folder)
- Soft overlaps kept as alternate analyses where useful

### Confirmation
**STOPPED at 40 new papers. No further ingest in this run.**


---

## [2026-08-02] ingest | Export wave-2 batch 1/8 (5 papers)

Continue from remaining claude_export/extracted-analyses/ after wave-1 stop at 40.

### Queue
- Built claude_export/remaining_queue_wave2.json (~42 not-yet-in-wiki candidates after map40/junk/content-dup filters)
- Prefer physics-heavy Tier A; skip hard dups and soft overlaps

### Papers created
1. beyond-iron-ultraheavy-cosmic-rays — UH nuclei as UHECRs / Amaterasu path
2. nucleus-shell-src-memory — JLab CaFe SRC orbital memory
3. black-hole-third-law-violation — vacuum 5D finite-time extremality
4. dissipative-cavity-entanglement — dark-state many-body entanglement via cavity decay
5. jwst-filament-cnd-ngc4696 — JWST filament to CND feeding NGC 4696

### Concepts
- No new single-paper stubs (policy). Updated hub: black-hole-thermodynamics (third-law note)
- Bidirectional: noise-driven-qubit-entanglement <-> dissipative cavity; gas-pedal notes soft-dup of Lorentz extract

### Soft-dup not ingested
- Lorentz-violation emergent gravity extract maps to universe-gas-pedal-leaky (same Isichei-Magueijo Otto-cycle program)

### Catalog after batch 1
- **Papers: 98 · Concepts: 61 · Synthesis: 2**
- Wave-2 progress: **5 / 40**



---

## [2026-08-02] ingest | Export wave-2 batch 2/8 (papers 6–10) + lint links

### Papers created
6. category-79-quasar-wind — J2318 UV BAL wind ~0.3c
7. peters-cycle-cosmic-rays — DAMPE multi-species rigidity softening
8. fractional-fermi-sea-1d-bosons — holonomy fractional Fermi seas
9. quantum-state-sculptor — Oxford non-Gaussian oscillator cats
10. freeze-fiber-brillouin — frozen CS2 liquid-core Brillouin gain

### Lint at 10 (high-value bidirectional links)
- beyond-iron <-> peters-cycle; aquila-booster <-> peters + beyond-iron
- jwst-filament <-> category-79-quasar-wind
- massive-tunneling-cats <-> quantum-state-sculptor
- problem-of-time-cold-atoms <-> fractional-fermi-sea-1d-bosons
- two-clocks-one-laser <-> freeze-fiber-brillouin

### Concepts
- No new stubs

### Catalog
- **Papers: 103 · Concepts: 61 · Synthesis: 2**
- Wave-2 progress: **10 / 40**



---

## [2026-08-02] ingest | Export wave-2 COMPLETE (36 papers)

Processed remaining unique extracts after wave-1 (40) + wave-2 batches 1–2 (10).

### Cadence applied
- Batches of 5 through remainder
- Lint + high-value links at 10 (batch 2), 20, 30 + final pass
- Stub policy: no new single-paper concept stubs; key terms folded into papers
- Index: counts rebuilt + Wave-2 appendix table

### Wave-2 slugs (36)
beyond-iron-ultraheavy-cosmic-rays, nucleus-shell-src-memory, black-hole-third-law-violation, dissipative-cavity-entanglement, jwst-filament-cnd-ngc4696, category-79-quasar-wind, peters-cycle-cosmic-rays, fractional-fermi-sea-1d-bosons, quantum-state-sculptor, freeze-fiber-brillouin, radio-changing-look-agn, glimpse-17775-cocoon, mot-metal-hydride, molecular-rotation-superfluid-he, droplet-rewrites-ring, nucleus-tells-on-itself, confinement-stiffening-films, metal-fall-apart-on-purpose, topo-chirality-structured-light, color-space-geometry, qg-deep-dive-1-mergers-emission, qg-deep-dive-2-info-holography, qg-deep-dive-3-holographic-codes, qg-deep-dive-4-de-sitter, cryptochrome-ascorbate-compass, ultrafast-chemical-shifts, two-lasers-one-reaction, gpu-mass-spectrometry, bond-breaking-discount, millisecond-pharma-factory, ruthenium-atom-catalysis, water-rna-polymerase, molecular-bias-point, interstellar-sulfur-ice, one-bond-inductive-effect, enzyme-resistance-tax

### Soft-dups / skips (not pages)
- Lorentz emergent gravity ≡ universe-gas-pedal-leaky
- spin-flip SAF, SnTe light symmetry, BH census alt, water-dissociation (double-life)
- why-thinner-is-tougher ≡ confinement-stiffening-films
- mass-and-instantons extract rematch → eta-prime (already in wiki); deleted bad page
- AI language-model scratchpad (non-physics)
- Hard dups folder untouched

### Catalog
- **Papers: 129 · Concepts: 61 · Synthesis: 2**
- Wave-2 progress: **36 / 36 COMPLETE — queue exhausted**



---

## [2026-08-04] synthesis | BH feedback ladder + AMO state control

### Created
- wiki/synthesis/black-hole-feedback-and-changing-look-agn.md — fuel (filament/CND), UV winds, radio changing-look, duals/inclination, cavities/recoils; tensions + open questions
- wiki/synthesis/amo-quantum-state-control.md — unitary cats/sculptor, dissipative/noise resources, 1D holonomy, photonic/Brillouin infrastructure

### Index
- Synthesis section now 4 pages; catalog synthesis count 2 → 4

### Bidirectional links
- Key AGN/SMBH paper pages → BH feedback synthesis
- Key AMO/QI paper pages → AMO state-control synthesis
- Sister notes on evaporation + quantum-time synthesis pages



---

## [2026-08-04] synthesis | Measurement problem threads 1–7

### Created
- wiki/synthesis/measurement-problem-threads.md — two-column sort (decoherence vs outcome-selection); Threads 1–7 map (problem statement, einselection, collapse, Bohm, Everett, epistemic/relational, Born bill); intersections with collapse clock floor, quantum time, problem-of-time cold atoms, Bell/DI, engineered measurement

### Index
- Synthesis count 4 → 5

### Reverse links
- Key papers, concepts (collapse, weak values, Bell/DI, proper time), and sister syntheses (quantum-time, AMO control)

### Source note
- Export study: claude_export/extracted-analyses/2026-07-28_measurement-problem-threads-1-7_19ad1981.md (not a single peer-reviewed paper page)



---

## [2026-08-04] ingest | SpaceX Wave-1 (5 NEW papers)

First ingest batch from spacex_export/TRIAGE.md NEW list only (27 eligible; 22 remain).

### Sources chosen (high-value experimental/theory papers)
1. 
ickelate-nodeless-gap-arpes <- nickelate ARPES nodeless gap + 70 meV kink
2. nyon-trions-twisted-mote2 <- Nature 2026 anyon-trions in twisted MoTe2
3. supermoire-trilayer-graphene-sc <- Nature Physics 2026 supermoire SC cascade
4. 
hic-net-proton-fluctuations <- STAR BES-II net-proton cumulants
5. mc-effect-marathon-a3 <- JLab MARATHON EMC in 3H/3He

### Concepts
- No new single-paper stubs (policy). Multi-paper hubs expanded via links only:
  - ata2s5-field-induced-sc, rown-zak-nonlinear-transport, color-superconductivity-qcd, 
ucleus-shell-src-memory, ractional-fermi-sea-1d-bosons

### Catalog
- **Papers: 134** (+5) · **Concepts: 61** · **Synthesis: 5**
- SpaceX NEW remaining: 22

### Notes
- Light lint: bidirectional links among new CM trio and nuclear pair + existing hubs.
- Soft-dups / THIN from triage not ingested.



---

## [2026-08-04] ingest | SpaceX Wave-2 (papers 6–10 of NEW)

Next 5 from remaining TRIAGE NEW list (prefer experimental / sharp theory).

### Papers
6. 
a61-isospin-kaon-asymmetry — NA61 charged-vs-neutral kaon excess (isospin breaking)
7. quantum-metric-spin-momentum-locking — Science 2025 quantum metric from Rashba locking (LAO/STO)
8. muse-quasar-filament-z3 — Nature Astronomy MUSE LyA filament at z~3.22
9. magnetar-slsn-2017egm-fermi — Fermi-LAT GeV detection of SLSN 2017egm
10. psr-j1906-binary-timing — 18 yr timing of PSR J1906+0746

### Concepts
- No new stubs. Links expanded on: rhic-net-proton, snte-light, pulsars-satellite-masses, jwst-filament-cnd, supernova-onion, nickelate-nodeless-gap

### Catalog
- **Papers: 139** · **Concepts: 61** · **Synthesis: 5**
- SpaceX NEW remaining: **17**



---

## [2026-08-04] ingest | SpaceX Wave-3 (papers 11–15 of NEW)

### Papers
11. 1d-anyons-momentum-tails — PRA 2025 universal 1D anyon momentum tails
12. magnetic-heliknoton-electric-write — Nature Materials electric heliknoton write/steer
13. positronium-diffraction-graphene — Nature Comm positronium diffraction
14. 
onabelian-photonic-braiding — PRL programmable non-Abelian photonic lattices
15. ice-core-fe60-local-cloud — PRL Antarctic 60Fe maps Local Interstellar Cloud

### Concepts
- No new stubs. Links: fractional-fermi-sea, anyon-trions, spin-flip-flop-saf, 3d-electron-diffraction, photon-number control, supernova-onion, interstellar-glaciers

### Catalog
- **Papers: 144** · **Concepts: 61** · **Synthesis: 5**
- SpaceX NEW remaining: **12**



---

## [2026-08-04] lint | SpaceX Waves 1–3 bidirectional link pass

Full lint of 15 SpaceX NEW paper pages (no new ingest).

### Work
- Reverse-link audit: ~33 missing paper→paper edges fixed (~36 links added/strengthened)
- Cross-links among CM moiré trio, nuclear trio, anyon 1D/2D, photonics topology, ISM/SN ash
- Concept hubs expanded (no new stubs): cosmic-web, magnons, pulsar-timing-arrays
- Index placement confirmed for all 15

### Notes
- Thin/verify later: RHIC (noisy source), EMC (conversational extract), NA61 (mislabeled source title), heliknoton & positronium (shorter pages)
- Report: spacex_export/LINT_REPORT.md
- Remaining TRIAGE NEW: 12 (untouched)

### Catalog
- Unchanged: **144 papers · 61 concepts · 5 synthesis**



---

## [2026-08-04] ingest | SpaceX Wave-4 (papers 16–20 of NEW)

Next 5 from remaining TRIAGE NEW list (prefer experimental / sharp theory). Final 7 NEW left untouched.

### Sources → wiki paths
| Source extract | Wiki page |
| --- | --- |
| `2025-11-08_massive-gravity-gluon-magic_a16227af.md` | [[massive-gravity-drgt]] |
| `2025-08-20_early-universe-ionization-by-supermassive-stars_fd46ef60.md` | [[early-universe-popiii-flash-ionization]] |
| `2026-05-13_trinity-test-creates-novel-ca-cu-si-clathrate_42edff4d.md` | [[trinity-ca-cu-si-clathrate]] |
| `2026-02-26_iras-21204-4913-eruptive-low-mass-fuor_48e8a69e.md` | [[iras-21204-fuor]] |
| `2026-01-14_laboratory-suppression-of-blazar-instabilities_fcdb46c3.md` | [[lab-blazar-pair-instability]] |

### Concept hubs expanded (no new stubs)
- [[dark-energy-equation-of-state]] — massive-gravity alternative
- [[hubble-tension]] — Pop III.1 τ lever
- [[cosmic-web]] — early flash ionization bubbles
- [[warm-dense-matter]] — Trinity HED + lab pair beams
- [[supermassive-black-hole-binaries]] — heavy-seed / Pop III.1 channel

### Reverse links (high-value)
- Cosmology: desi, universe-gas-pedal, muse, euclid
- Materials/plasma: metal-fall-apart, filming-plasma-birth, beam-driven-plasma-mirror
- Astro: mrk501 (blazar cascade), dr21 (YSO accretion)

### Cluster placement
| Page | Cluster |
| --- | --- |
| massive-gravity-drgt | Black holes, GR & dense gravity |
| early-universe-popiii-flash-ionization | Cosmology, galaxies & large-scale gravity |
| iras-21204-fuor | Cosmology, galaxies & large-scale gravity (star formation) |
| trinity-ca-cu-si-clathrate | Solid-state, optics & materials |
| lab-blazar-pair-instability | Islands / Plasma & high-energy-density |

### Catalog
- **Papers: 149** · **Concepts: 61** · **Synthesis: 5**
- SpaceX NEW remaining: **7**



---

## [2026-08-04] ingest | SpaceX final NEW wave (papers 21–27)

All remaining TRIAGE NEW analyses ingested. **NEW queue empty (27/27).**

### Sources → wiki paths
| Source extract | Wiki page |
| --- | --- |
| `2026-05-25_axion-quantum-signatures-erased-in-detectors_6487c8e0.md` | [[axion-detector-quantum-erasure]] |
| `2026-01-07_five-dimensional-classical-gravity-model_c344a460.md` | [[five-dimensional-classical-gravity]] |
| `2026-02-07_jwst-reveals-hydrocarbon-factory-in-ulirg_757ca7d7.md` | [[jwst-ulirg-hydrocarbons]] |
| `2026-02-25_phosphorus-radical-catalyzed-markovnikov-hydroamination_de2d756d.md` | [[phosphorus-radical-hydroamination]] |
| `2026-02-09_physically-possible-warp-drive-breakthrough_a388b090.md` | [[warp-drive-positive-energy]] |
| `2026-01-11_temporal-imbalance-theory-gravity-s-new-clock_bc2d307c.md` | [[temporal-imbalance-gravity]] |
| `2026-02-05_v3-4-3-prompt-evanescent-waves-hidden-transverse-spin-moment_2c39fa3c.md` | [[evanescent-wave-transverse-spin]] |

### Concept hubs expanded (no new stubs)
- [[null-energy-condition]] — positive-energy warp shell
- [[fieldoscopy]], [[epsilon-near-zero]] — evanescent transverse spin
- [[quantum-proper-time]] — time-first gravity contrast

### Reverse links
- DM: synchrotron-dm-detector ↔ axion
- Gravity foundations: gravity-from-entropy, problem-of-time, retrocausal, evaporating-BH
- Astrochemistry: interstellar-sulfur-ice, interstellar-glaciers ↔ ULIRG
- Chemistry: bond-breaking-discount ↔ phosphorus hydroamination
- Optics: topo-chirality ↔ evanescent spin

### Cluster placement
| Page | Cluster |
| --- | --- |
| warp-drive-positive-energy | Black holes, GR & dense gravity |
| five-dimensional-classical-gravity | Black holes, GR & dense gravity |
| temporal-imbalance-gravity | Black holes, GR & dense gravity |
| jwst-ulirg-hydrocarbons | Cosmology / galaxies |
| axion-detector-quantum-erasure | Cosmology / galaxies (DM) |
| evanescent-wave-transverse-spin | Solid-state, optics & materials |
| phosphorus-radical-hydroamination | Islands / Chemistry & biotech |

### Catalog
- **Papers: 156** · **Concepts: 61** · **Synthesis: 5**
- SpaceX TRIAGE NEW remaining: **0**



---

## [2026-08-04] cleanup | SpaceX attention list resolved

No new ingest. No new synthesis/concept stubs. Full write-up: `spacex_export/CLEANUP_REPORT.md`.

### Work
1. **rhic-net-proton-fluctuations** — retied to arXiv:2504.00817; extract chat noise discarded; clarified BES-II $C_4/C_2$ (below Poisson; min deviation ~2–5σ vs non-critical baselines @ 19.6 GeV).
2. **emc-effect-marathon-a3** — retied to arXiv:2410.12099; kinematics + slopes fixed; **no** large isovector EMC claim (K-P isoscalar OK).
3. **na61-isospin-kaon-asymmetry** — content confirmed ($R_K$, DOI); **filename mismatch** documented (extract title “nuclear magnetization” is wrong; body is NA61).
4. **magnetic-heliknoton-electric-write**, **positronium-diffraction-graphene** — +1 high-value link / clarifying sentence each.
5. **five-dimensional-classical-gravity**, **temporal-imbalance-gravity** — `status: exploratory` + top blockquote non-consensus disclaimers.
6. **Last 7 NEW pages** — all wikilinks resolve; light cross-link polish on axion + warp.

### Catalog
- Unchanged: **156 papers · 61 concepts · 5 synthesis**



---

## [2026-08-04] synthesis | Condensed-matter topology & fractionalization

New comparative synthesis across moiré FCIs, 1D anyons/holonomy, supermoiré SC, quantum metric, heliknotons, and photonic non-Abelian braiding.

### Page
- `wiki/synthesis/condensed-matter-topology-fractionalization.md`

### Structure
- Platform × mechanism map (table)
- Thread A: fractionalization (charge / statistics / occupancy)
- Thread B: band geometry, folding, mini-band SC
- Thread C: writable classical spin textures
- Thread D: photonic emulators
- Strong vs thin coverage + open questions

### Bidirectional links
- Key papers: anyon-trions, 1d-anyons, fractional-fermi-sea, supermoiré, quantum-metric, brown-zak, heliknoton, nonabelian-photonic
- Concept hub: magnons

### Catalog
- **Papers: 156** · **Concepts: 61** · **Synthesis: 6**



---

## [2026-08-04] synthesis | High-energy astrophysics, multi-messenger & early thermal history

New comparative synthesis of energetic transients, multi-messenger fossils, ISM/ULIRG chemistry, cosmic-web lighting, and Pop III.1 ionization.

### Page
- `wiki/synthesis/high-energy-astrophysics-multimessenger.md`

### Structure
- Messenger × epoch map (table)
- Thread A: energetic engines & HE photons (SLSN, PeVatron, lab blazar)
- Thread B: nucleosynthetic fossils ($^{60}$Fe ice, SN onion)
- Thread C: gas lighting, chemistry, accretion (MUSE, ULIRG, FUor, ice)
- Thread D: early ionization / thermal history (Pop III.1 flash)
- Strong vs thin coverage + open questions

### Bidirectional links
- Core papers: magnetar-slsn, ice-core-fe60, muse filament, jwst-ulirg, popiii flash, iras-fuor
- Hubs: supernova-onion, interstellar-glaciers, cosmic-web; cross-pointer from BH-feedback synthesis

### Catalog
- **Papers: 156** · **Concepts: 61** · **Synthesis: 7**



---

## [2026-08-04] synthesis | Nuclear and dense-matter precision observables

New comparative synthesis of RHIC cumulants, NA61 isospin, MARATHON EMC, SRC shell memory, hard probes, and dense-QCD theory.

### Page
- `wiki/synthesis/nuclear-dense-matter-precision.md`

### Structure
- Observable → constraint map (table)
- Thread A: hot dense (fluctuations, isospin, color SC)
- Thread B: cold nuclei (EMC, SRC)
- Thread C: hard scattering / nuclear gluons
- Thread D: finite-density rare probes (η′, color SC)
- Strong vs thin coverage + open questions

### Bidirectional links
- Core: rhic, na61, emc, nucleus-shell-src, color-sc, star-jpsi
- Concepts: high-pt-scaling, parton-jets

### Catalog
- **Papers: 156** · **Concepts: 61** · **Synthesis: 8**


---

## [2026-08-04] synthesis | Modified and speculative gravity approaches

Comparative map of dRGT, positive-energy warp shells, exploratory 5D/temporal-imbalance/GfE foundations, MOND/EFE, with energy-condition constraints from the BH evaporation synthesis. Explicit non-consensus framing.

### Page
- `wiki/synthesis/modified-speculative-gravity.md`

### Structure
- Approach × modification × constraint table
- Thread A: field-theory IR mods (massive gravity vs DE data)
- Thread B: metric engineering + NEC referee (warp, gravastar, evaporation library)
- Thread C: exploratory ontology rewrites (5D, temporal imbalance, GfE)
- Thread D: phenomenological force laws (MOND/EFE, kSZ)
- Strong vs thin + open questions

### Bidirectional links
- Core: massive-gravity-drgt, warp-drive, 5D classical, temporal-imbalance
- Hubs: null-energy-condition, dark-energy-equation-of-state; cross-pointer from black-hole-evaporation-energy-conditions

### Catalog
- **Papers: 156** · **Concepts: 61** · **Synthesis: 9**


---

## [2026-08-04] polish | Index hygiene + light link/front-matter pass

No new pages. No deepening.

### Index
- Folded 16 Wave-2-only papers into topical clusters
- Removed duplicate Wave-2 batch table (was double-listing 21 slugs)
- Inbox/provenance table updated; all 156 papers + 9 synthesis indexed once under correct clusters

### Links
- Spot-check of recent synthesis reverse links: OK
- One add: desi-evolving-dark-energy → modified-speculative-gravity

### Front-matter
- No defects found

### Report
- `spacex_export/POLISH_REPORT.md`

### Catalog
- Unchanged: **156 papers · 61 concepts · 9 synthesis**


---

## [2026-08-04] deepen | Thin pages (8 papers + 2 concept hubs)

No new papers/synthesis. Focused density pass after index polish.

### Deepened papers
- magnetic-heliknoton-electric-write, positronium-diffraction-graphene
- brown-zak-nonlinear-transport, quantum-metric-spin-momentum-locking, nonabelian-photonic-braiding
- star-jpsi-spin-interference, supernova-onion-expansion (rewrite)
- eta-prime-mesic-nucleus, lab-blazar-pair-instability, color-space-geometry

### Concept hubs
- magnons, parton-jets

### Report
- `spacex_export/DEEPEN_REPORT.md`

### Catalog
- Unchanged: **156 papers · 61 concepts · 9 synthesis**
