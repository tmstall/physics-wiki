---
tags: [papers, modified-gravity, quantised-inertia, failed-derivation]
last_updated: 2026-10-31
status: derivation-fails
related_papers: [modified-speculative-gravity, mond-external-field-sparc, phantom-halo-verlinde-surface-density]
source_analysis: raw/analyses/2026-10-10_arxiv-1610.06787_quantised-inertia-relativity-uncertainty-principle.md
---

# Derivation fails: quantised inertia is not recovered from the uncertainty principle

**One-line summary:** McCulloch’s 2016 EPL derivation (arXiv:1610.06787) does **not** recover the quantised-inertia formula. The cosmic and Rindler horizons do produce the formula’s bracket shape; the prefactor, the signs, and the identification of a mass change with a total mass do not.

## Key claims and results

The paper claims that conserving rest energy plus Heisenberg “energy uncertainty,” then shrinking the position uncertainty from the cosmic horizon to the Rindler horizon, derives quantised inertia. Recomputation of the printed equations does not support that claim. Five reads:

1. **Sign flip as printed; author’s intended convention unclear.** Eq. 13 rearranges to a *lower* inertial mass when the position spread shrinks. Eq. 14 prints the opposite sign. The algebra of that mismatch is unambiguous. What is unclear is only whether the author meant the conservation law written the other way round. Even if he did, the next four findings still stand.
2. **Gravity sign.** Eq. 6 adds a term that grows as two bodies approach, so the force is repulsive. Integrating that law from rest sends the bodies apart. The paper claims attraction. The later claim that energy is released as the bodies move together contradicts Eq. 6. This is not a claim that Eq. 8’s algebra “dropped a sign.”
3. **$\hbar$ versus $h$.** The printed mass formulas use the reduced Planck constant. The quoted masses match those formulas with the full Planck constant, a factor of about six. As printed, the electron is about six times too light and the proton about eight times too light. The electron and Planck-mass rows reverse the definitions of the Compton wavelength and the Planck length. They are not independent predictions.
4. **The ~59-order gap.** The horizon step leaves a prefactor ~59 orders of magnitude too small for a 1 kg object at Earth gravity. The numerical match appears only after an extra substitution that sets one Unruh-peak photon’s energy equal to the object’s rest energy. That step is not justified by the uncertainty argument.
5. **Change versus total.** Eq. 20 is a *change* in mass (about 1.26 times the mass times the discount bracket). Eq. 1 is the *total* inertial mass. The paper calls them the same. They are not, so the quantised-inertia formula is not recovered. Taken at face value, Eq. 20 more than doubles the mass of every accelerating object at any acceleration.

Footnote: the text calls the gravity unit “the reduced Planck mass,” but the value later quoted is essentially the ordinary Planck mass. With the reduced unit the gravity derivation would be ~25 times too strong.

Renda (arXiv:1908.01589) criticizes earlier derivations. This analysis saw that abstract only, so that critique stays contested and is not this recomputation.

Galaxy rotation curves, a cosmic-acceleration threshold, and “no dark matter” are claims from the author’s other papers. They are not results of this derivation.

## Physical intuition

A 1/length rule with two horizons (cosmic size, then the acceleration horizon) is enough to sketch the *shape* “inertia fades when acceleration drops below a cosmic scale.” Shape is not a derivation. The size of the effect is set by $\hbar a/c^3$, a fixed tiny mass change, the same for a feather and a planet. Turning that into the object’s whole inertial mass requires equating one photon’s energy with $mc^2$.

## Limitations and assumptions

- The journal typeset version (EPL 115, 69001, DOI 10.1209/0295-5075/115/69001) was not compared line by line with arXiv:1610.06787v1. Small editorial differences are possible.
- Finding 1’s *intent* is unclear. Findings 2–5 are reads of what is printed.
- No concept page is warranted: quantised inertia is not established here as a working law.

## Connections

- Synthesis: [[modified-speculative-gravity]] — 2016 derivation **fails on recomputation**; do not cite this paper as “quantised inertia derived from the uncertainty principle.”
- Neighbors that also modify inertia or gravity without being this claim: [[mond-external-field-sparc]], [[phantom-halo-verlinde-surface-density]].

## Open questions

- Is there a derivation of the quantised-inertia prefactor that does not equate unrelated energies?
- Does a later paper correct Eq. 14’s sign relative to Eq. 13 without the $E=mc^2$ substitution?

## Source

- `raw/analyses/2026-10-10_arxiv-1610.06787_quantised-inertia-relativity-uncertainty-principle.md`
- Ingest card: `incoming/INGEST_DIRECTIVES.md` § quantised-inertia-2016
