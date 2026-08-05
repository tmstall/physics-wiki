---
tags: [synthesis, condensed-matter, topology, fractionalization, moire, quantum-geometry]
last_updated: 2026-08-04
status: synthesis
related_papers: [anyon-trions-twisted-mote2, 1d-anyons-momentum-tails, fractional-fermi-sea-1d-bosons, supermoire-trilayer-graphene-sc, quantum-metric-spin-momentum-locking, brown-zak-nonlinear-transport, magnetic-heliknoton-electric-write, nonabelian-photonic-braiding, nickelate-nodeless-gap-arpes, three-body-quantum-company, snte-light-topological-inversion, photonic-supersolid, spin-flip-flop-saf, bata2s5-field-induced-sc, quantum-metallurgy-cdw]
---

# Condensed-Matter Topology and Fractionalization

**One-line summary:** Across moiré Chern bands, 1D cold gases, oxide interfaces, chiral magnets, and photonic lattices, this wiki’s pages ask the same engineering question — **how do you create, fingerprint, and reconfigure fractional or topological order** — and answer it with different knobs: flat-band geometry, statistics angles, quantum metric, spin knots, and programmable braids.

## Why pull these together

Fractional charges, anyonic exchange, mini-band superconductivity, quantum geometry, and Hopf spin textures look like separate subfields. In this wiki they form one comparative map:

> Which **platform** carries the topological object, which **knob** writes it, and which **readout** proves it is fractional or non-Abelian rather than ordinary order?

No single paper wins. Stack them and four mechanisms appear: (1) **fractionalization** of charge or occupancy, (2) **band geometry** as a resource (metric, Brown–Zak, supermoiré folding), (3) **classical topological textures** you can write with current, (4) **photonic / soft-matter emulators** of non-Abelian structure. The tensions live where “anyon” means a real quasiparticle versus a programmable phase or a classical knot.

This synthesis is **condensed-matter / AMO topology**. Quantum-time metrology lives on [[quantum-time-across-platforms]]; general AMO state engineering lives on [[amo-quantum-state-control]]. They share cold-atom pages; they answer different questions.

---

## Comparative map (platforms × mechanisms)

| Platform | Topological / fractional object | How you write it | How you read it | Wiki anchors |
| --- | --- | --- | --- | --- |
| Twisted TMD moiré (MoTe₂) | Fractional Chern insulator anyons ($e/3$, $e/5$) | Twist + displacement field; zero large $B$ | Anyon–trion PL binding ~ charge² | [[anyon-trions-twisted-mote2]] |
| 1D Bose / anyon gas | Fractional exclusion / statistical angle $\alpha$ | Holonomy in $g_{\rm 1D}$; zero-range $a_+=a_-$ | Momentum tails, Friedel / correlation structure | [[fractional-fermi-sea-1d-bosons]], [[1d-anyons-momentum-tails]] |
| Asymmetric trilayer graphene | Mini-flat bands → SC domes + isospin insulators | Supermoiré from unequal twists | Transport, Brown–Zak / Hofstadter fans | [[supermoire-trilayer-graphene-sc]], [[brown-zak-nonlinear-transport]] |
| Oxide 2DEG (LAO/STO) | Quantum metric from Rashba locking | Gate density → SOC strength | $B$-odd nonlinear magnetoresistance | [[quantum-metric-spin-momentum-locking]] |
| Chiral magnet FeGe | 3D heliknoton (Hopf texture) | ns current pulses (STT), $B=0$ | Electron holography + micromagnetic fit | [[magnetic-heliknoton-electric-write]] |
| Photonic lattice | Non-Abelian mode braiding | Programmable pseudospin rotations | Adiabatic path-order observables | [[nonabelian-photonic-braiding]] |

**Intuition:** Fractionalization is not one effect. Sometimes charge itself splits (FCI anyons). Sometimes occupancy dilutes over a stretched sea (1D holonomy). Sometimes bands fracture into drawers that host SC and insulators (supermoiré). Sometimes geometry, not topology, is the headline (quantum metric). Sometimes the “topology” is classical and writable (heliknotons). Sometimes light only *emulates* non-Abelian structure (photonics). Keep the labels honest.

**Concepts nearby:** [[magnons]] (textures and spin waves), [[amo-quantum-state-control]] (1D holonomy as state engineering)

---

## Thread A — Fractionalization: charge, statistics, occupancy

**Papers:** [[anyon-trions-twisted-mote2]], [[1d-anyons-momentum-tails]], [[fractional-fermi-sea-1d-bosons]], [[three-body-quantum-company]]

### A1 — Optical anyons in a zero-field FCI

[[anyon-trions-twisted-mote2]]: twisted bilayer MoTe₂ hosts fractional Chern insulators at fillings such as $\nu=-2/3$ and $-3/5$ without monster magnets. Natural traps localize trions; PL finds red-shifted anyon–trion peaks whose binding scales roughly as fractional charge squared ($e/3$ vs $e/5$).

**Intuition:** Moiré flat bands fake Landau levels with lattice geometry. Light, not an interferometer, fingerprints the fraction: the trion snags a partial-charge packet and the energy ratio reads the charge.

**Limits:** Trap disorder; not every filling shows clear peaks; braiding not measured; fans reintroduce $B$ for Chern checks.

### A2 — 1D statistics in momentum tails

[[1d-anyons-momentum-tails]]: continuum 1D anyons split into bosonic and fermionic families. When even- and odd-parity contact lengths match, high-$|k|$ tails of $n(k)$ carry Tan contacts weighted by $\sin$/$\cos$ of the statistical angle $\alpha$. The $k^{-3}$ term is a statistical smoking gun for generic bosonic anyons.

**Intuition:** In 1D, exchange *is* a collision. Put a tunable phase on the handshake; Fourier-transform the sharp coincidence edges into power-law tails. Contacts measure interaction; trigonometric weights measure statistics.

**Limits:** Strictly zero-range theory; large-$|k|$ anyon TOF not yet experimental on this page’s stack.

### A3 — Fractional Fermi seas via interaction holonomy

[[fractional-fermi-sea-1d-bosons]]: cyclic holonomy through Lieb–Liniger $g_{\rm 1D}$ (repulsive ↔ attractive via Feshbach / CIR) clicks a 1D Bose gas into fractional Fermi seas with occupancy $1/\ell$ over stretched momentum support — claimed beyond ordinary two-parameter TLL.

**Intuition:** Same cars, wider stalls, half full. Each interaction loop is a quantum gear shift that redistributes occupancy without changing particle number.

**Limits:** Integrability-protected protocol; “beyond TLL” is a strong claim under community scrutiny; attractive-side losses and temperature degrade the ladder.

**A-thread tension:** 2D FCI anyons are **charged quasiparticles** with optical binding fingerprints. 1D anyons and fractional seas are **statistical / exclusion** objects. Same word “fractional,” different ontology. Do not collapse them.

---

## Thread B — Band geometry, folding, and correlated mini-bands

**Papers:** [[supermoire-trilayer-graphene-sc]], [[brown-zak-nonlinear-transport]], [[quantum-metric-spin-momentum-locking]], [[snte-light-topological-inversion]], [[nickelate-nodeless-gap-arpes]], [[quantum-metallurgy-cdw]]

### B1 — Supermoiré as hierarchical cache

[[supermoire-trilayer-graphene-sc]]: unequal twists in trilayer graphene break mirror symmetry and build a ~31 nm supermoiré that dices flat bands into mini-bands. Isospin-broken insulators and a cascade of superconducting domes fragment around half-filling gaps (BKT $T_c\sim0.5$ K).

**Intuition:** One moiré is L1 cache (flat bands). Supermoiré is L2 misaligned on top — smaller drawers, stronger interaction win rate, SC only in leftover pockets.

### B2 — Nonlinear transport as geometry stethoscope

[[brown-zak-nonlinear-transport]]: Brown–Zak fermions at rational flux appear in nonlinear voltage response at lower $B$ than linear magnetoresistance needs, because the channel tracks quantum-geometric ballistic takeover.

[[quantum-metric-spin-momentum-locking]]: Rashba spin-momentum locking forces a finite **quantum metric** even without magnetism or nontrivial Chern number; gate-tunable $B$-odd nonlinear MR in 111-LAO/STO reads it.

**Intuition:** Berry curvature is band “magnetic field”; quantum metric is band **distance**. Nonlinear transport hears which geometry is in charge. Spin-momentum locking is a rifled bullet that bends Bloch states so hard the metric cannot stay zero.

### B3 — Neighboring correlated platforms (weaker topology claim)

[[nickelate-nodeless-gap-arpes]], [[bata2s5-field-induced-sc]], [[quantum-metallurgy-cdw]], [[snte-light-topological-inversion]]: pairing, field-driven SC, CDW melting, light-induced band inversion — related engineering of flat / soft bands, not fractionalization per se. Keep them as **context**, not anyon evidence.

**B-thread tension:** Metric and Brown–Zak are about **geometry of Bloch states**. Supermoiré SC is about **interaction-dominated mini-bands**. Geometry can enable correlations; it is not the same as fractional charge.

---

## Thread C — Writable topological textures (classical spin)

**Papers:** [[magnetic-heliknoton-electric-write]], [[spin-flip-flop-saf]] · concept [[magnons]]

[[magnetic-heliknoton-electric-write]]: ns current pulses nucleate and steer 3D magnetic heliknotons in FeGe at zero external field. Holography + micromagnetics show a distorted skyrmion–antiskyrmion core; opposite Hall pushes cancel so the package slides straight.

**Intuition:** 2D skyrmions are surface whirlpools. Heliknotons are **volume knots** (Hopf index). Current is the stylus; STT writes the knot over a barrier. Magnon physics ([[magnons]], [[spin-flip-flop-saf]]) supplies the underlying spin-wave language.

**Limits:** Cryogenic FeGe window; nucleation yield; classical LLG — not a quantum anyon.

**C vs A tension:** A heliknoton is a **classical topological soliton**. An FCI anyon is a **quantum fractional excitation**. Both are “topology you can point to”; only one fractionalizes charge.

---

## Thread D — Photonic and soft-matter emulators

**Papers:** [[nonabelian-photonic-braiding]], [[photonic-supersolid]], [[twisted-light-chiral-ms]] (structured light neighbor)

[[nonabelian-photonic-braiding]]: reconfigurable photonic lattices implement full SU(2) pseudospin rotations; adiabatic loops braid light modes with path-order memory. Two Abelian bulks with mismatched spin bases can host a non-Abelian interface.

**Intuition:** Sequence is memory — rotate $x$ then $y$ versus $y$ then $x$. Light’s internal labels are programmed couplers; braiding is classical room-temperature practice for ideas usually reserved for fragile non-Abelian anyons.

**Limits:** Loss, fabrication detuning; classical simulation, not a topological qubit.

**D vs A tension:** Photonic non-Abelian braiding **emulates** non-commutative structure. TMD anyon–trions claim **material** fractional charge. Use D as a design lab; do not treat it as condensed-matter anyon discovery.

---

## Coverage: strong vs thin

### Strong in this wiki

- **Moiré experimental stack:** FCI optical fingerprints ([[anyon-trions-twisted-mote2]]), supermoiré SC cascade ([[supermoire-trilayer-graphene-sc]]), Brown–Zak nonlinear probe ([[brown-zak-nonlinear-transport]]).
- **1D fractionalization theory + holonomy experiment narrative:** [[1d-anyons-momentum-tails]], [[fractional-fermi-sea-1d-bosons]].
- **Quantum metric as measurable geometry:** [[quantum-metric-spin-momentum-locking]] tied to nonlinear transport culture.
- **Writable spin topology + magnon hub:** [[magnetic-heliknoton-electric-write]], [[magnons]], [[spin-flip-flop-saf]].
- **Photonic non-Abelian control:** [[nonabelian-photonic-braiding]] as emulator anchor.

### Still thin (honest gaps)

- **True anyon braiding / interferometry** in electronic or cold-atom platforms — not on disk as a primary paper page.
- **Fractional quantum Hall continuum** (GaAs, graphene FQH at high $B$) — wiki leans moiré / zero-field FCI, not classic FQH depth.
- **Non-Abelian condensed-matter anyons** (Majorana, Fibonacci, Moore–Read) — photonic emulator only; no solid-state non-Abelian anyon experiment page.
- **Dedicated quantum-geometry concept hub** — metric appears on paper pages; no multi-paper concept stub yet (policy: expand only multi-paper hubs when ready).
- **Spectroscopic confirmation of supermoiré mini-Dirac satellites** — transport-heavy; ARPES-class depth thin.
- **Cross-platform theory** that unifies FCI anyons, 1D exclusion, and metric nonlinearities under one formalism — synthesis map only, not a single theory page.

---

## Open questions the wiki is positioned to answer

1. **Same word, same object?** When do optical anyon–trion binding energies and 1D Tan-tail statistics constrain a shared fractionalization language, and when must the wiki keep them strictly separate?
2. **Geometry → pairing?** Does the quantum-metric / Brown–Zak toolkit on oxide and graphene pages predict which supermoiré mini-bands should host SC domes versus isospin insulators?
3. **Write vs fractionalize:** Can electrically written Hopf textures ([[magnetic-heliknoton-electric-write]]) ever couple to electronic fractionalization, or do they remain a classical spintronics island next to the moiré stack?
4. **Emulator transfer:** Which non-Abelian photonic braiding protocols ([[nonabelian-photonic-braiding]]) have a realistic map onto electronic or cold-atom anyon paths already referenced in Thread A?
5. **What to ingest next:** Classic FQH interferometry, solid-state Majorana claims, or a second quantum-metric material — which gap most improves this map without bloating single-paper stubs?

---

## How to use this page

- Start here for **platform comparison**, then open the paper pages for claims, limits, and sources.
- For cold-atom holonomy as *control engineering*, also see [[amo-quantum-state-control]].
- For time-as-quantum-object (NOON duration, clocks), see [[quantum-time-across-platforms]] — different axis.

**Catalog role:** Sixth synthesis page. Complements the two BH syntheses (evaporation vs AGN feedback), the two quantum foundations/AMO syntheses (time, state control, measurement), and leaves cosmology / QFT clusters without a topology-fractionalization synthesis of their own.
