---
tags: [papers, black-holes, quasinormal-modes, gauss-bonnet, higher-dimensions]
last_updated: 2026-10-05
status: analysis-ingest
related_papers: [looking-inside-a-quantum-black-hole, horizon-direct-wave-gw250114, massive-gravity-drgt, black-hole-interiors, entanglement-islands-page-curves-kerr-ads]
source_analysis: "raw/analyses/2026-10-04_arxiv-2608.06083_gauss-bonnet-black-hole-quasinormal-modes-spectral.md"
---

# Gauss–Bonnet Quasinormal-Mode Atlas

**One-line summary:** A 300-digit Chebyshev survey catalogues ringdown tones of Gauss–Bonnet black holes from 5 to 26 dimensions; the anchor numbers and a six-dimensional instability check out, and the claims that WKB grabbed the wrong tone and that a space detector could hear string dimensions do not. Phys. Rev. D 114, 044015 (2026), DOI 10.1103/91q6-r3jd.

## Key claims and results

- **Paper:** Batic & Dutykh, arXiv:2608.06083, Phys. Rev. D 114, 044015 (2026). Static, non-rotating, asymptotically flat holes. Three wave equations: a test scalar, and the vector-type and tensor-type parts of gravitational perturbations. Gravity’s scalar-type channel, which carries the known five-dimensional Gauss–Bonnet instability, is not computed. “No instability in the scalar sector” therefore does not mean five-dimensional Gauss–Bonnet holes are gravitationally stable.
- Method: Chebyshev spectral expansion at 300 digits. Eigenvalues are kept when they stay fixed as the matrix size changes. The survey runs from weak coupling up to the edge of horizon existence, in dimensions 5 through 26, with public Maple/Matlab code (not re-run in the analysis). An independent double-precision Chebyshev solver reproduced the five-dimensional scalar fundamentals at zero, moderate, and near-maximal coupling to the quoted digits, and the zero-coupling value matches the Tangherlini limit after rescaling.
- At moderate coupling the method returns ladders of purely imaginary (“overdamped”) eigenvalues with nearly constant spacing. WKB cannot see non-oscillating tones. These towers sit next to a branch-cut-like column on the same axis. Convergence across three matrix sizes is the only test. An independent double-precision solver did not recover the fixed ladders. Treat the towers as a candidate until a continued-fraction or time-domain calculation confirms them.
- At strong coupling the spectrum contains more than one family: a low-pitch, more strongly damped family beside the one WKB sees. The paper reads this as WKB misidentifying the fundamental. By the usual definition the fundamental is the longest-lived tone. In six dimensions at the couplings checked, the WKB tone is the least damped, and the paper’s own tables show that ordering. The extra family is real as a numerical finding. The criticism of WKB is backwards. The paper’s “fundamental” label in the strong-coupling tables is a family index, not “longest ringing.”
- At zero coupling the scalar monopole and the gravitational vector dipole are isospectral. The paper explains this by a supersymmetric factorization: the two potentials are $W^2 \pm dW/du$ with the same superpotential, so they share nonzero eigenvalues. That identity checks out. Two caveats: the algebra is not special to five or more dimensions, and the vector partner is the one-unit-of-angular-momentum mode, which in Einstein gravity is the non-dynamical “add a little rotation” deformation rather than a radiating wave. Separately, the paper says the tensor sector has no such pairing, while its own tables show tensor and scalar tones identical at zero coupling for angular number two and up, as the Kodama–Ishibashi equations predict.
- Six-dimensional tensor modes grow once a rescaled coupling exceeds ~5.4 for the lowest angular mode. That onset and the growth rates reproduce. It is not the first numerical sighting: time-domain work (Konoplya & Zhidenko 2008) and analytic critical masses (Beroiz, Dotti & Gleiser 2007) already exist. Higher angular modes go unstable at weaker coupling (mode 4 already at ~4.4), so the quoted mass bound — unstable below ~158 times the coupling to the three-halves, for the lowest mode — is not the true threshold. The coefficient also moves by a factor of a few depending on how mass is normalized. Nothing similar appears in seven or more dimensions in this survey.
- A bound-state counting integral (Cohn–Calogero) is offered as a rigorous stability guarantee. At a coupling where the paper itself reports a growing tone, the integral is still below one. It tracks the threshold. It does not prove stability of the vector sector.
- The observational claim does not survive. Tones in 26 dimensions look “amplified” in the paper’s dimensionless units, which change meaning with dimension. The conversion to hertz raises a quantity with units of inverse time to a fractional power, so the same formula in milliseconds does not give the same number of hertz. Physical tones scale as one over size. A horizon tens of kilometres across rings at kilohertz per dimensionless unit, and a black hole much larger than compact extra dimensions is not higher-dimensional. The DECIGO pathway is not a prediction.

## Physical intuition

A ringdown is a bell tone that leaks. The pitch and the decay depend on the hole, not on what struck it. Gauss–Bonnet gravity adds the simplest curvature-squared correction that string theory suggests. In four dimensions that term does not change the equations. In five or more it does, so these holes are a clean numerical laboratory for “how do short-distance corrections move the tones and the stability line?”

The useful product is the table: one method, three sectors, many dimensions, compared with older WKB and time-domain numbers. The less useful product is a layer of names for the shapes of the eigenvalue cloud (glassware metaphors). The names organize pictures. They do not predict a different observable.

## Limitations and assumptions

- Overdamped towers may be branch-cut artefacts. That is the most novel claim and the least checked.
- WKB comparison at strong coupling in six dimensions is inverted if “fundamental” means least damped.
- Hertz / DECIGO claim is dimensionally inconsistent, and astrophysical holes with compact extra dimensions would not ring as higher-dimensional objects.
- Instability mass bound uses the least unstable angular mode and a chosen mass normalization.
- Test scalar is not gravitational scalar-type perturbation.
- Only static, non-rotating, flat asymptotics. No spin, no AdS. The authors list those as next steps.
- Code on GitHub was not inspected. Anchor checks used an independent solver, not the authors’ 300-digit run. The overdamped towers specifically need that precision, so a failed double-precision replay is not a disproof.

## Connections

- Ringdown overtones used to profile a quantum black-hole center (different hole, different question): [[looking-inside-a-quantum-black-hole]]
- A measured ringdown read as a horizon quantity: [[horizon-direct-wave-gw250114]]
- A different modified-gravity field theory (massive graviton, four dimensions): [[massive-gravity-drgt]]
- Interiors and islands, not this classical spectrum: [[black-hole-interiors]], [[entanglement-islands-page-curves-kerr-ads]]
- Synthesis: [[modified-speculative-gravity]] (higher-D curvature correction; not a detection channel), [[black-hole-evaporation-energy-conditions]] only as a neighbor — this page is classical ringdown, not evaporation

## Open questions

- Do the purely imaginary towers survive a continued-fraction or time-domain evolution?
- What is the large-angular-number instability threshold in the same method, and how does it compare with the 2007 critical masses?
- Does the extra strongly damped family show up as a second decaying piece in a time-domain waveform?

## Source

- `raw/analyses/2026-10-04_arxiv-2608.06083_gauss-bonnet-black-hole-quasinormal-modes-spectral.md`
