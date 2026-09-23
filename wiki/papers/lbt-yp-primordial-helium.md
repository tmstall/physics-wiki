---
tags: [papers, cosmology, bbn, helium, neutrinos, lbt]
last_updated: 2026-09-20
status: analysis-ingest
related_papers: [cosmology-expansion-history-and-structure, early-universe-popiii-flash-ionization]
source_analysis: "raw/analyses/2026-09-14_lbt-yp_part1of2_methodology-and-data.md; raw/analyses/2026-09-14_lbt-yp_part2of2_result-and-implications.md"
---

# LBT Yp Project — Primordial Helium and Neutrino Counting

**One-line summary:** Five-paper ApJ series: build ruler (He I λ10830 breaks T–n degeneracy; quality-over-quantity sample) then average near-pristine galaxies instead of extrapolating → tighter Yp → Nν≈2.925±0.082 (SM=3); tightened null, not discovery. Papers I–V ApJ 1008; DOI 10.3847/1538-4357/ae879b (IV).

## Key claims and results

- Papers I–III: quality-first sample of extremely metal-poor HII regions; three-year LBT/MODS flux calibration (~0.5–0.6%); super-Gaussian line fits; new $T_e$[SIII]–$T_e$[OIII] scaling; He I λ10830 / Pγ density diagnostic on 48 LUCI targets with a hard unphysical-ratio quality floor none of their objects fail.
- Paper IV: $\chi^2$ gate + conservative flagging → 41 clean targets; 15 at O/H ≤ $4\times10^{-5}$ support a weighted average (not a Y–O extrapolation) → $Y_p = 0.2458\pm0.0013$ (0.5% relative) — tightest $^4$He to date.
- Robustness: doubled metallicity cut, S/H instead of O/H, and two regression methods all land near the same central value; regressions cannot constrain the slope — averaging was the right call.
- Paper V: BBN + Planck + updated D/H → $N_\nu = 2.925\pm0.082$, $\Delta N_\nu < 0.125$ (95% CL one-sided); ~2× tighter than the same team’s 2022 result, almost entirely from the better $Y_p$.
- Result is a tightened null near SM $N_\nu=3$, not a beyond-SM discovery; rules out a fully thermalized extra light scalar ($\Delta N_\nu\approx0.57$).

## Physical intuition

You cannot observe BBN helium directly. You measure near-pristine local galaxies and push as close to zero metallicity as the sky allows. Optical He lines alone tangle temperature and density; He I λ10830 is the independent densitometer that breaks the tie. Once enough galaxies sit near “idle,” skip drawing a trend line through contaminated points — just average the near-pristine cluster. Better $Y_p$ is the lever that tightens the early-universe neutrino count when fused with deuterium and the CMB.

## Limitations and assumptions

- $Y_p$ is a local-universe proxy (extrapolation/average), not a direct look at $t\sim1$ s; $N_\nu$ adds BBN Monte Carlo + Planck likelihood layers on top.
- Assumed-linear ΔY/ΔO remains a structural caveat; the project minimizes it by low metallicity rather than solving it.
- LINMIX finds intrinsic scatter on the full 41-object sample; whether that contaminates the preferred 15-object average is not separately demonstrated.
- Density stratification (high-ionization zones ~10–15× denser) exists; three-zone model is an approximation (O/H impact shown small).
- Single-team dataset; Table 6 field comparison shows broad ~0.24–0.26 agreement, not an independent re-observation of this sample.

## Connections

- Synthesis: [[cosmology-expansion-history-and-structure]]
- Early ionization / Pop III cousin: [[early-universe-popiii-flash-ionization]]

## Source

- `raw/analyses/2026-09-14_lbt-yp_part1of2_methodology-and-data.md`
- `raw/analyses/2026-09-14_lbt-yp_part2of2_result-and-implications.md`
