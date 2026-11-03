---
tags: [papers, white-dwarfs, magnetic-fields, chandrasekhar]
last_updated: 2026-10-31
status: analysis-ingest
related_papers: [high-energy-astrophysics-multimessenger, rapid-orbital-decay-erassu-j060839, type-ia-supernovae]
source_analysis: "raw/analyses/2026-10-23_doi-10.3847-2041-8213-aea97e_super-chandrasekhar-magnetized-white-dwarfs.md"
---

# Super-Chandrasekhar Magnetized White Dwarfs

**One-line summary:** ApJL DOI 10.3847/2041-8213/aea97e. With an imposed internal magnetic field the code moves the white-dwarf maximum from 1.4 to as much as 2.4 solar masses. The field is an input formula, not computed; interior fields ~$10^{5}$ times any measured surface field are assumed. The paper's own magnetic-energy accounting looks too small for the mass it supports and needs rechecking.

## Key claims and results

- Zuraiq, Mukhopadhyay, Kumar, Sarkar, Hackett, Banerjee & Tout, *ApJL* **1010**, L8 (10 Oct 2026), DOI 10.3847/2041-8213/aea97e. Cambridge STARS code with a magnetic-pressure term. arXiv companion 2609.22437 was located but not read.
- The field is never solved. At each point it is looked up from density, $B(\rho) = B_{\rm s} + B_0[1 - e^{-\eta(\rho/\rho_0)^{\gamma}}]$, with a ceiling $B_0 = 10^{14}$ G. Inner 90% is treated as toroidal (magnetic pressure added); outer 10% as poloidal (magnetic pressure subtracted). Shape knobs $\eta$ and $\gamma$ are chosen so the run finishes; steeper profiles crash.
- Stars of 3, 5, and 8 solar masses are evolved through the giants to white dwarfs of 0.45, 0.82, and 1.02 solar masses. Young white dwarfs have central fields around $10^{12}$ G and surface fields of order $10^{5}$ G, inside the observed magnetic-white-dwarf range, and they sit on the ordinary mass–radius curve. The field is "dormant" until accretion compresses the core.
- Steady spherical accretion at $10^{-9}\,M_\odot$/yr onto the 1.02-solar-mass carbon–oxygen white dwarf. No field: the run stops near 1.38 solar masses when carbon ignites. With the field the maximum is about 1.8, 2.2, or 2.4 solar masses as the climb rate goes from 0.7 to 1.3. The 2.4-solar-mass model reaches a central field of about $8\times 10^{13}$ G.
- A helium-rich hybrid (about a tenth of a solar mass of helium left) ignites helium and is destabilized below the magnetic maximum, with or without the field. Switching nuclear energy off lets both compositions reach the top of the curve. Only helium-poor white dwarfs can climb all the way.
- At ordinary masses the field adds a few percent to the radius on top of temperature. For SDSS J123204.19+522548.2 the magnetized curve misses the measured radius by under 1%, versus about 7% for temperature alone. One object, extra parameters; a systematic study is deferred.
- The paper reports magnetic energy below about a tenth of gravitational energy, ellipticity below $10^{-5}$, and a decay time of about 5 Gyr. A toy recomputation with the paper's own formula matches the "below one tenth" energy ratio (about 4–7%) and the quoted central field. A virial estimate for a star supported by relativistic electrons says lifting the limit from 1.44 to 2.4 solar masses needs magnetic energy near 29% of gravitational energy (about 24% for 2.2). A one-tenth budget would reach only about 1.7 solar masses. The stated sphericity matches the quoted number only if magnetic pressure is converted to a mass density by dividing by $c^{2}$; the force-based distortion, scaling with the energy ratio, is a few percent to about ten percent — roughly a thousand times larger.

## Physical intuition

The Chandrasekhar limit is a limit on electron support, not a law that no white dwarf can be heavier. A second support beam — magnetic pressure — can hold more weight, the way a column with a guy-wire carries more load than the column alone. This code does not compute that beam. It reads field strength from density the way a fan curve reads a temperature sensor and looks up a speed. Turn the climb-rate knob and the maximum mass follows: 1.8, 2.2, or 2.4 solar masses. The energy ledger is the check that the knob cannot fake. If magnetic energy is only about a tenth of gravitational energy, it is not obvious that the books can pay for a jump from 1.4 to 2.4. Interior fields near $10^{14}$ G are about $10^{5}$ times any measured surface field, and only the surface is observable.

## Limitations and assumptions

- The interior field is an input, motivated by flux freezing, not an outcome of the magnetic equations. The headline maxima are what the code returns for the chosen profiles. The claim "the limit can exceed 1.4" survives for any profile that actually reaches $10^{14}$ G in the core; it fails if interior fields stay near the $10^{12}$ G the young white dwarfs start with.
- Isotropic magnetic pressure omits the inward hoop tension. Self-consistent two-dimensional calculations that solve for the geometry have argued that deformation and electron capture cap the extra mass. This paper does not re-run those cases.
- The energy-budget and ellipticity flags are order-of-magnitude checks on an idealized star, not a re-run of STARS. A non-ideal structure could move the numbers. A factor-of-three gap is unlikely to close quietly, but it is not a proof the code is wrong.
- Strong-field stability is assumed from Braithwaite's energy-ratio window, not tested at $10^{14}$ G. If the true ratio must be ~0.3 to hold 2.4 solar masses, the model moves toward the unstable range.
- Accretion is spherical, steady, and nova-free. The authors note that fields above about $10^{6}$ G would funnel gas onto the poles, and that real low-rate accretion flashes. The quoted accretion time to 2.4 solar masses is ~1.4 Gyr, longer than the paper's "at most about 1 Gyr"; decay at ~5 Gyr still outlasts it.
- No rotation and no magnetic back-reaction on convection. Over-luminous Type Ia events have other explanations (asymmetry, circumstellar interaction, mergers). Super-Chandrasekhar white dwarfs remain one candidate, not a required progenitor. None of the cited candidates is established as one of these stars.

## Connections

- Synthesis (high-energy astrophysics): [[high-energy-astrophysics-multimessenger]]
- Ultracompact double white dwarf: [[rapid-orbital-decay-erassu-j060839]]
- Type Ia context: [[type-ia-supernovae]]

## Source

- `raw/analyses/2026-10-23_doi-10.3847-2041-8213-aea97e_super-chandrasekhar-magnetized-white-dwarfs.md`
