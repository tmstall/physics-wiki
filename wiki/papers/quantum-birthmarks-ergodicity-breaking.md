---
tags: [papers, quantum-chaos, scarring, ergodicity]
last_updated: 2026-10-31
status: analysis-ingest
related_papers: [measurement-problem-threads]
source_analysis: "raw/analyses/2026-10-12_arxiv-2412.02982_quantum-birthmarks-ergodicity-breaking-beyond-scarring.md"
---

# Quantum Birthmarks — Memory Beyond Scarring

**One-line summary:** arXiv:2412.02982. In a chaotic quantum box, infinite-time return is at least 2× any comparable state (3× if time-reversal and a real state). Scars are one case of that memory; early partial returns deepen a "birthmark." The factor of two is standard random-matrix lore; the framing is the contribution. One table in the paper needs a recount.

## Key claims and results

- Phys. Rev. X 16, 031063 (2026). DOI 10.1103/dhzb-28rb. arXiv:2412.02982 v4 (10 Sep 2026). Graf, Atwood, Xiao, Ketzmerick, Heller, and Keski-Rahkonen.
- Question shift: not "which standing waves are scarred?" but "how often does a moving packet come home, forever, compared with a fair control state that has the same energy profile?"
- Random-matrix statistics set a floor. Chaotic eigenstates behave like random vectors, so a packet's weights are spiky. Self-return squares those spikes. Transfer multiplies two unrelated sets. The ratio is two for complex amplitudes, or when time-reversal symmetry is broken. It is three when time-reversal symmetry holds and the initial state is real. The floor is fixed at launch and does not involve Planck's constant, so it survives the semiclassical limit even as the fraction of scarred eigenstates goes to zero.
- Extra return from early partial revivals, a scar orbit or a lucky focusing bounce, deepens the mark. The paper calls the sum a quantum birthmark and treats every kind of scarring as one case of it.
- Stadium-billiard simulations (one particle, two dimensions): four launches, three on scar-forming paths and one generic. Infinite-time density stays bright at the launch point and along early paths, with dark regions elsewhere, even when any late snapshot looks like a random wave. Stronger early return means a deeper mark. At higher energy the spatial pattern gets finer and paler. The state-level ratio stays put.
- The analysis recomputed the effective number of levels behind Table I from the paper's own formula and Appendix B inputs and got about 10,700, not the 8,916 the table uses, about 20% apart. The quoted ratios therefore carry an unstated normalization uncertainty of that size, and the one case that appears to sit below the floor of two is the likely casualty of a too-small baseline. Existence of the mark does not depend on that recount. The headline numbers do.

## Physical intuition

Classical chaos in a stadium billiard forgets the start. The ball eventually spends equal time everywhere. A quantum packet cannot, because its recipe of energy eigenstates is a spiky barcode, and the barcode lines up with itself perfectly and only imperfectly with a stranger's. That self-match is worth a factor of two, or three if the waves are real and the box does not distinguish past from future. Scars are not a separate exception for a few standing waves. They are extra early laps that stamp the same permanent return a little harder. "Ergodicity breaking" here means "never down to the flat classical baseline." A specialist can just as well call the factor of two the correct quantum-ergodic value. The pictures and the split into universal floor plus early bonus are the new framing. The arithmetic is old.

## Limitations and assumptions

- The factor of two or three is Porter–Thomas / random-matrix lore (close cousins: Heller's exploration-rate work, elastic enhancement, coherent backscattering). Removing the new vocabulary changes no number, only how the numbers are grouped.
- Whether that floor counts as ergodicity breaking depends on the baseline. One over the number of levels is a value almost no quantum state can hit for its own return.
- The revival factor is an estimator, exact only in limiting cases, with a cutoff chosen by rule of thumb. The paper does not test "universal times revival" quantitatively against each simulated launch. Table I ratios come from the simulations, not from that estimator.
- All demonstrations are a single particle in a two-dimensional billiard. Many-body scars, quantum dots, molecular spectra, and coherent forward scattering are analogies, not new calculations.
- The real-space mark fades under coarse resolution at higher energy. A large or warm experiment needs fine resolution or a state-resolved measurement.
- Scope overlaps Pizzi's "quantum trails" (arXiv:2412.04310). The paper says that work only covers narrow packets on classical paths. The analysis read Pizzi's abstract, not the paper, so the dispute is reported, not judged.
- No experiment has measured a birthmark directly. A simulator that can switch time-reversal symmetry and watch two become three is the clean test. Publisher animations cited in the paper were not in the arXiv package.

## Connections

- Synthesis: [[measurement-problem-threads]]

## Source

- `raw/analyses/2026-10-12_arxiv-2412.02982_quantum-birthmarks-ergodicity-breaking-beyond-scarring.md`
