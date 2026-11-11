# Ingest directives

Binding notes for specific analyses. `incoming/prompts/INGEST.md` requires a check of this file **before** each wiki paper page is written or updated.

Match a card if the analysis filename or body contains the arXiv id, the DOI, or the filename stem. A card overrides the paper’s abstract. Do not paraphrase the abstract into the wiki title, one-line summary, index row, or synthesis blurb.

Framework confidence tags such as **(C) Speculative** mean “analyst recomputation, not an independent published confirmation.” They do **not** mean the algebra is doubtful. When a card says a finding is a recomputed failure, write it that way.

Add a new card when a future ingest must not repeat a claim the analysis has already refuted.

---

## quantised-inertia-2016

**Match:** `1610.06787` · `10.1209/0295-5075/115/69001` · `quantised-inertia-relativity-uncertainty-principle`

**Source:** `2026-10-10_arxiv-1610.06787_quantised-inertia-relativity-uncertainty-principle.md` (McCulloch, EPL 2016 / arXiv:1610.06787). Keep the page. It is a checked failed derivation, not evidence for the model.

**This card overrides the analysis file.** The file remains the provenance record, including its **(C) Speculative** tags. Those tags mean “analyst recomputation, not an independent published confirmation.” They do not mean the algebra is doubtful. On the wiki page, write the five findings below as reads of the printed equations. Do not copy “(C) Speculative” onto them.

**Wiki page**

- Slug: `quantised-inertia-failed-derivation` (or equally explicit). Do not use a slug that reads as an established result.
- `status: derivation-fails`
- Title, one-line summary, index row, and any hub sentence must **lead with the verdict**: the derivation does not recover the quantised-inertia formula.
- State these five findings as equation reads:
  1. **Sign of the inertia ledger.** Sign flip as printed; author’s intended convention unclear. Eq. 13 rearranges unambiguously to the opposite sign of what Eq. 14 prints: shrinking the position spread lowers the inertial mass. Do not call this finding soft, and do not drop or hedge the printed mismatch. What is unclear is only whether the author meant to write the conservation law the other way round. Even if that was the intent, findings 2–5 still stand.
  2. **Gravity sign.** The two-body energy law (Eq. 6) adds a term that grows as the bodies approach, so the force is repulsive. A short integration of that law, started at rest, sends the bodies apart. The paper claims the force is attractive. Do **not** say “Eq. 8 has its sign dropped” or that Eq. 8’s algebra is wrong. Say the paper’s later claim that energy is released as the bodies move together contradicts Eq. 6.
  3. **$\hbar$ versus $h$.** The printed mass formulas use the reduced Planck constant. The masses the paper quotes match the same formulas with the full Planck constant, a factor of about six. With the formulas as printed, the electron is about six times too light and the proton about eight times too light. The electron and Planck-mass rows reverse definitions (Compton wavelength, Planck length). They are not independent predictions.
  4. **The ~59-order gap.** Steps that produce the quantised-inertia *bracket* leave a prefactor ~59 orders of magnitude too small for a 1 kg object at Earth gravity. The numerical match appears only after an extra substitution: one Unruh-peak photon’s energy is set equal to the object’s rest energy ($E=mc^{2}$). That step is not justified by the uncertainty argument.
  5. **Change versus total.** Even after that substitution, Eq. 20 is a *change* in mass (about 1.26 times the mass times the discount bracket). Eq. 1 is the *total* inertial mass. Setting them equal does not recover the quantised-inertia formula. Taken at face value, Eq. 20 more than doubles the mass of every accelerating object, at any acceleration.
- Footnote only, not a headline: the text calls the gravity unit “the reduced Planck mass,” but the value later quoted is essentially the ordinary Planck mass. With the reduced unit the gravity derivation would be ~25 times too strong.
- Renda (arXiv:1908.01589) may stay **contested**: the analysis saw the abstract only, and it criticizes earlier derivations, not this recomputation.
- Galaxy rotation, cosmic acceleration, and “no dark matter” are claims from the author’s other papers. This page must not cite them as results of this derivation.
- The one structural remark worth keeping: cosmic and Rindler horizons as the two lengths of a 1/length rule reproduce the bracket’s shape. That is bookkeeping, not a derivation of the prefactor.

**Do not**

- Create a concept page that states quantised inertia as a working law.
- Let [[modified-speculative-gravity]] (or any hub) summarize this paper as “quantised inertia derived from the uncertainty principle.” If the hub mentions it, the sentence must say the 2016 derivation fails on recomputation.

**Pass test (required before the queue row is marked done).** The ingest session runs this check itself; a batch note that says “directive applied” does not count. Open the new paper page, search `wiki/` for `quantised inertia` / `quantised-inertia` / `1610.06787`, and pass only if all of these are true: the page shows `status: derivation-fails`; the title leads with the failure; all five reads appear; and no sentence on that page or any hub states the abstract’s claims as fact. There is no concept page for quantised inertia. Report pass or fail in the batch summary from that read, not from memory. The same check is a one-minute grep if you want to re-run it later.
