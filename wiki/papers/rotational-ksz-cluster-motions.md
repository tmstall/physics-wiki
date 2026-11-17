---
tags: [papers, ksz, cmb, galaxy-clusters, planck]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [newton-ksz-force-law, ksz-effect, mond-external-field-sparc]
source_analysis: "raw/analyses/2026-10-29_doi-10.1103-lz37-crg1_rotational-ksz-cluster-rotation.md"
---

# Rotational kSZ Dipole in Nearby Clusters

**One-line summary:** Stacking 25 X-ray clusters aligned by their galaxy redshift split shows a CMB warm/cool dipole at about 3.6σ; the signal is too large for gentle co-rotation, and the published title now includes mergers and other intrahalo motions. Goldstein & Hill, *Phys. Rev. Lett.* (2026).

## Key claims and results

- **Paper:** Samuel Goldstein and J. Colin Hill. *Phys. Rev. Lett.* **137**, 161001 (2026). DOI [10.1103/lz37-crg1](https://doi.org/10.1103/lz37-crg1). Analysis basis is arXiv:2512.10951v1. The journal title adds “and intrahalo gas motions.” The published PDF was not read.
- Method: orient each cluster by the sine-like galaxy redshift pattern, stack Planck, and look for a dipole from the kinematic Sunyaev–Zel’dovich effect. Sample is 25 nearby massive X-ray clusters. Equal weights give about 1.5σ. Mass weighting gives about **3.6σ** (about 25 millionths of a degree). A radial-profile fit is about 3.3σ. Dropping Coma leaves about 2.9σ. About a dozen clusters carry the weight.
- New step: subtract the part of the temperature map predicted from E-mode polarization. With Planck that removes only 10–20% of the primary CMB. The same trick should do more once ACT, SPT, or the Simons Observatory supply cleaner polarization.
- The dipole cannot separate spin from sloshing or mergers. The authors’ own template needs gas faster than circular speed, roughly four times the galaxy split. The simulation comparison uses clusters 10–100 times more massive. Yang et al. (arXiv:2603.14494) report a similar dipole at about 2.3σ on a larger optical sample that shares Planck and some of the same sky.

## Physical intuition

Bulk motion of cluster gas Doppler-shifts the CMB: toward you is warm, away is cool. One cluster is invisible under the primary ripples. Line the dipoles up with the galaxy swirl and the average can show a two-sided pattern. That pattern is a radar return for *organized* gas motion. It is not yet a tachometer for rotation. Hidden motion matters because cluster masses used in cosmology assume the gas is held up by pressure alone.

## Limitations and assumptions

- v1 preprint versus a retitled journal version. Review edits beyond the title were not checked. Figures were read as captions plus embedded arXiv images.
- Significance sits in a roughly 3–3.6σ band once the authors’ own robustness cuts are included.
- The orientation cut prefers a clean two-sided velocity split, which mergers also produce.
- Cluster-correlated noise is not in the randoms. Galaxy–gas misalignment can cut the signal.

## Connections

- Pairwise bulk-flow kSZ, a different observable: [[newton-ksz-force-law]], [[ksz-effect]]
- Synthesis: [[cosmology-expansion-history-and-structure]]

## Open questions

- Does the dipole survive in ACT or SPT, and does it vanish in relaxed clusters if mergers dominate?

## Source

- `raw/analyses/2026-10-29_doi-10.1103-lz37-crg1_rotational-ksz-cluster-rotation.md`
