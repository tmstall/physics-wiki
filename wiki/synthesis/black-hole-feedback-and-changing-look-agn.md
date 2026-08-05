---
tags: [synthesis, black-holes, agn, feedback, galaxy-evolution]
last_updated: 2026-08-04
status: synthesis
related_papers: [jwst-filament-cnd-ngc4696, category-79-quasar-wind, radio-changing-look-agn, glimpse-17775-cocoon, smbh-inclination-angle, mrk501-double-jet-smbbh, ultramassive-bh-binary-cavity, high-z-quasar-pair-merger, bh-recoils-agn-survey, black-hole-recoil-agn, euclid-high-z-quasar-census, naked-black-hole-candidate]
---

# Black Hole Feedback and Changing-Look AGN

**One-line summary:** This wiki’s AGN and SMBH pages form an observational ladder — fuel in, radiation and jets out, pairs merge and kick, cores get scoured — that closes the feedback loop only if cold gas can shed angular momentum, winds actually couple, and “changing-look” switches are physical, not classification noise.

## Why pull these together

A supermassive black hole is a small engine with galaxy-scale consequences. The wiki already holds separate stories that all answer pieces of one systems question:

> How does a black hole **get** gas, **push** gas, **pair**, **merge**, and **leave fingerprints** we can actually measure?

No single paper owns the whole loop. Stack them and a ladder appears: kiloparsec filaments → circumnuclear disks → accretion states → winds and jets → dual nuclei and binaries → recoils and cavities. The tensions live at the handoffs between rungs.

This synthesis is **astrophysical** (fuel and feedback). Interior evaporation and energy conditions live on [[black-hole-evaporation-energy-conditions]]; do not collapse the two. High-energy messengers, ISM chemistry, and early ionization history live on [[high-energy-astrophysics-multimessenger]] — shared filament/quasar pages, different question.

---

## The loop in one picture

Think of a power plant with a fuel pipe, a furnace, an exhaust stack, and occasional twin turbines that slam together and kick the foundation.

| Stage | What happens | Wiki anchors |
| --- | --- | --- |
| **Fuel delivery** | Cooling multiphase gas must lose angular momentum or it circularizes far out | [[jwst-filament-cnd-ngc4696]], [[dr21-magnetic-accretion]] (magnetic guidance at star-forming scales) |
| **Staging buffer** | Circumnuclear disk (CND) holds rotating gas near the sphere of influence | [[jwst-filament-cnd-ngc4696]] |
| **Furnace mode** | Accretion lights a quasar / AGN; soft vs hard continua, WLQ vs strong-lined | [[category-79-quasar-wind]], [[glimpse-17775-cocoon]], [[euclid-high-z-quasar-census]] |
| **Exhaust (radiative)** | UV / X-ray winds carry mass and kinetic power | [[category-79-quasar-wind]] |
| **Exhaust (mechanical)** | Jets and radio lobes reheat atmospheres; radio loudness can flip | [[radio-changing-look-agn]], [[mrk501-double-jet-smbbh]] |
| **Pairing** | Two holes in one host; inclination filters merger vs stall | [[smbh-inclination-angle]], [[high-z-quasar-pair-merger]], [[mrk501-double-jet-smbbh]] |
| **Hardening / scouring** | Binary slingshots stars and gas; kpc cavities | [[ultramassive-bh-binary-cavity]] |
| **Kick** | GW recoil flings the remnant through the nucleus | [[bh-recoils-agn-survey]], [[black-hole-recoil-agn]] |

**Intuition:** Feedback is a control loop, not a one-way blast. Without fuel, no wind. Without wind or jets, cooling dumps too hard. Without pairing physics, you cannot budget the nanohertz GW sky or explain dual quasars. The wiki’s value is that each rung has at least one concrete observational paper.

**Concepts nearby:** [[supermassive-black-hole-binaries]], [[dual-agn]], [[dynamical-friction]], [[pulsar-timing-arrays]]

---

## Rung 1 — Fuel: filaments into disks

**Paper:** [[jwst-filament-cnd-ngc4696]]

JWST/NIRSpec resolves, at ~10 pc in the Centaurus BCG NGC 4696, the kinematic handoff where a cooling filament dumps ionized gas into a rotating CND. That is the missing conveyor belt from kiloparsec cooling flows to sub-100 pc fueling.

**Intuition:** Precipitation says cold clouds rain inward; angular momentum says they should park. Magnetic tethers (Maxwell stress) act like regenerative brakes on the tangential motion so gas can fall almost radially and settle into a spinning buffer disk. Turbulence peaks at the junction — the plumbing joint is noisy, as expected.

**Honest limits:** Inflow is inferred (geometry ⊥ jet, PV linkage, NGC 1275 analogy), not a 3D velocity vector. Sims are system-tuned consistency checks. Multiphase thermal structure still disagrees with some cold-sim CNDs. $M_{\rm BH}$ often still from scaling relations.

**Why it matters for feedback:** Cold-mode accretion wins observational ground here against pure hot Bondi straws — at least in this nearby, resolvable laboratory.

---

## Rung 2 — Exhaust: UV winds that matter for the galaxy

**Paper:** [[category-79-quasar-wind]] (J2318)

Record UV BAL wind at ~0.26–0.3$c$ (C IV / Si IV), evolving over rest-frame years, with conservative $L_{\rm kin}/L_{\rm bol}\gtrsim0.75\%$ — right at the usual galaxy-impact threshold, and possibly much higher under less conservative geometry.

**Intuition:** Radiation pressure is a firehose; absorption troughs are the radar gun. UV ions that *survive* at 0.3$c$ are the puzzle: the same radiation field that accelerates gas should strip those ions. Weak-lined / soft continua may be why the wind is visible at all.

**Limits:** Covering fraction and launch radius model-dependent; single object; comparison to PDS 456 is analogy, not a matched campaign.

**Ladder note:** Winds answer “does the engine push?” Filaments answer “does the engine eat?” Both are required for a closed loop; the wiki now has a clean observational example of each.

---

## Rung 3 — Mode switches: changing-look, especially radio

**Paper:** [[radio-changing-look-agn]] (SDSS J1105+1452)

An NLS1 jumped from radio-quiet (~1.4 mJy) to radio-loud (~39 mJy) and *stayed* there for years with almost no multiwavelength twin outburst — coining a long-duration **radio changing-look** class.

**Intuition:** Optical and X-ray changing-look already dismantle neat type bins. Radio loudness was supposed to be the stable bit (jet on vs off). J1105 flipped the jet switch and left it latched while the rest of the chip barely twitched.

**Limits:** Single object; sparse historical sampling; jet power and beaming still model-dependent.

**Tension with Rung 2:** Radiative BAL winds and mechanical radio jets are different exhaust channels. A galaxy can be wind-dominated, jet-dominated, or both over different epochs. Changing-look phenomenology means **mode is not a permanent property of the black hole’s passport**.

**High-$z$ cousin:** [[glimpse-17775-cocoon]] — a Little Red Dot where a dense cocoon rewrites the spectrum and inflates inferred mass; super-Eddington on a *smaller* hole can hide inside fog. Early growth modes (NLS1-like fast accretors) connect local radio switches to JWST’s compact red monsters without forcing every LRD to be an overmassive galaxy.

---

## Rung 4 — Pairing: inclination, duals, and imaged jets

**Papers:** [[smbh-inclination-angle]], [[high-z-quasar-pair-merger]], [[mrk501-double-jet-smbbh]]

- **Inclination filter:** Post-merger disk galaxies — secondary SMBH orbital tilt $\lesssim 20^\circ$ favors merger in a few Gyr; $\gtrsim 45^\circ$ risks everlasting high-inclination stall ([[smbh-inclination-angle]]).
- **High-$z$ dual:** Confirmed quasar pair in a $z=5.7$ merger with a tidal gas bridge — dual engines in the early universe ([[high-z-quasar-pair-merger]]).
- **Local imaging:** Mrk 501’s second jet loops around the primary — binary deep in the final-parsec regime ([[mrk501-double-jet-smbbh]]).

**Intuition:** Two black holes in one galaxy are not guaranteed to merge. Geometry is a gate: flat coplanar orbits sink; polar orbits can hang. Dual quasars and double jets are the times when *both* furnaces light up before the final plunge.

**Concepts:** [[supermassive-black-hole-binaries]], [[dual-agn]], [[dynamical-friction]]

**Open tension:** Final-parsec problem lore vs observed duals and PTA-relevant candidates — the wiki’s objects sit at different separations and do not yet form a continuous evolutionary sequence for one system.

---

## Rung 5 — Hardening footprints and recoils

**Papers:** [[ultramassive-bh-binary-cavity]], [[bh-recoils-agn-survey]], [[black-hole-recoil-agn]]

- Ultramassive binary candidate scours a ~1 kpc starless cavity ([[ultramassive-bh-binary-cavity]]) — three-body slingshots as a bulldozer, not a gentle inspiral cartoon.
- Recoil surveys hunt GW kicks that offset AGNs from photometric centers ([[bh-recoils-agn-survey]], [[black-hole-recoil-agn]]).

**Intuition:** Mergers leave scars. Cavities are the construction site; recoils are the aftermath when the foundation jumps. Both are rare, selection-biased, and easy to fake with projection — which is why multiwavelength vetoes matter.

**PTA link:** Hardening binaries and high-$z$ pair fractions feed the nanohertz GW budget ([[pulsar-timing-arrays]] language on the dual-quasar page). This synthesis does not compute that budget; it flags which observational rungs enter it.

---

## Census rungs — population context

**Papers:** [[euclid-high-z-quasar-census]], [[naked-black-hole-candidate]], [[glimpse-17775-cocoon]]

Euclid multiplies the high-$z$ quasar sample; extreme JWST portraits (naked / horizonless candidates, LRD cocoons) stress how incomplete “standard AGN SED” assumptions are. Feedback models trained on local quasars must not pretend every $z\sim6$–8 object is a scaled-up SDSS template.

---

## Where the rungs agree

| Agreement | Notes |
| --- | --- |
| Feedback is multiphase and multi-channel | Cold filaments + UV winds + radio jets are not competitors for a single prize |
| Mode can change on human or rest-frame-year timescales | Changing-look (incl. radio) breaks static labels |
| Angular momentum is the bottleneck | Filament→CND and binary inclination both are geometry problems |
| Nearby laboratories teach high-$z$ physics | NGC 4696, NLS1s, Mrk 501 as resolvable analogs |
| Selection and projection dominate “rare object” claims | Duals, recoils, cavities need independent confirmation paths |

---

## Where they tension or talk past each other

| Tension | Detail |
| --- | --- |
| **Hot vs cold accretion** | Filament work favors cold precipitation; Bondi still may dominate elsewhere |
| **Wind vs jet coupling** | Kinetic thresholds (~0.5–1% of $L_{\rm bol}$) are order-of-magnitude; geometry can hide true power |
| **Stable radio-loudness myth** | Radio changing-look vs textbook radio-loud / quiet permanence |
| **Pair fraction vs merger rate** | Seeing two active nuclei ≠ knowing they will merge in a Hubble time (inclination stall) |
| **Cavity / recoil impostors** | Star formation holes, dust lanes, dual AGN without kicks can mimic signatures |
| **LRD mass crisis** | Cocoon reprocessing vs truly ultramassive early holes — same photometry, different physics |

Do not force one “SMBH feedback theory.” Prefer a **stack of constraints**:

1. Fuel must reach the sphere of influence (filaments / CNDs).
2. Exhaust must couple enough energy (winds / jets).
3. Pairs must clear angular-momentum and inclination gates (duals / binaries).
4. Remnants leave spatial scars (cavities / recoils).
5. Labels must allow time dependence (changing-look).

---

## Open questions this synthesis highlights

1. How common is the filament→CND handoff across BCGs once JWST IFU samples grow?
2. What fraction of UV ultrafast outflows are WLQ-enabled visibility effects vs truly extreme coupling?
3. Can radio changing-look events be caught in the act with simultaneous X-ray / optical / VLBI?
4. Does the inclination filter survive in gas-rich, high-$z$ mergers like J2037−4537?
5. Which recoiling-AGN candidates survive next-generation astrometric and spectroscopic vetoes?
6. How do LRD cocoons change the high-$z$ black-hole mass function used in feedback and reionization models?

---

## Map of pages

| Role | Pages |
| --- | --- |
| Fuel / CND | [[jwst-filament-cnd-ngc4696]] |
| Radiative exhaust | [[category-79-quasar-wind]] |
| Mechanical / radio mode | [[radio-changing-look-agn]], [[mrk501-double-jet-smbbh]] |
| Early / extreme AGN | [[glimpse-17775-cocoon]], [[euclid-high-z-quasar-census]], [[naked-black-hole-candidate]] |
| Pairing | [[smbh-inclination-angle]], [[high-z-quasar-pair-merger]], [[mrk501-double-jet-smbbh]] |
| Scars | [[ultramassive-bh-binary-cavity]], [[bh-recoils-agn-survey]], [[black-hole-recoil-agn]] |
| Concepts | [[supermassive-black-hole-binaries]], [[dual-agn]], [[dynamical-friction]], [[pulsar-timing-arrays]] |
| Sister synthesis (interiors) | [[black-hole-evaporation-energy-conditions]] |
