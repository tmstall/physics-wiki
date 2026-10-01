---
tags: [papers, dynamical-systems, imputation, machine-learning]
last_updated: 2026-10-01
status: analysis-ingest
related_papers: [deepmind-hurricane-forecasting]
source_analysis: "raw/analyses/2026-09-20_doi-10.1038-s41467-026-77922-1_dynamics-informed-imputation-missing-systems-dynamics.md"
---

# Dynamics-Informed Imputation of Missing Time Series (FPRM)

**One-line summary:** *Nature Communications* (DOI [10.1038/s41467-026-77922-1](https://doi.org/10.1038/s41467-026-77922-1), accepted manuscript) fills catastrophic gaps by mapping delay-embedded windows between sensors: Takens geometry makes those windows exactly translatable, a Gaussian process only approximates the map, and the method still needs one fully observed anchor channel.

## Key claims and results

- Full–partial reconstruction mapping (FPRM) delay-embeds a complete series and a gappy series, then learns one global map from the full attractor reconstruction onto the partial one. Gaussian-process regression is the default approximator, not the idea.
- Takens’ theorem supplies the load-bearing claim: for smooth deterministic dynamics, two observables reconstruct diffeomorphic copies of the same attractor, so a one-to-one map exists in the noise-free case. The fit approximates that map; it does not invent a correlation and hope it holds in the gap.
- The stress test keeps one anchor complete and deletes 90% of every other channel. Across a 3-species ecology model, the Lorenz system, 120-dimensional coupled Lorenz and Rössler systems, road occupancy (500 series), 64-channel EEG, and 52 exchange rates, Pearson $\rho$ typically lands near 0.8–0.95 and normalized RMSE near 0.4–0.7. On the 120D Lorenz case the analysis quotes average $\rho \approx 0.84$–$0.87$.
- FPRM beats ten baselines that span classical imputation, ordinary machine learning, and local empirical-dynamic-modeling fits (S-map / MVCM). Swapping the Gaussian process for a support-vector machine or a neural net still works, so the embedding-to-embedding architecture does the real work.
- Not every anchor is equal. Some complete channels impute nearly every other variable; others cover only a subset. The paper reports that split and does not give a rule that picks the good anchor in advance.
- Code and data: Figshare DOI 10.6084/m9.figshare.30446765 (MATLAB R2024b). Single-group result (accepted 9 September 2026; Article in Press 19 September 2026). No independent replication yet.

## Physical intuition

A dynamical system does not sprinkle its missing samples at random in state space. The trajectory has to stay on the attractor, so a gap in one sensor is still a point on that shape. Stack each sensor into a short sliding window of its own past and the two clouds are the same shape drawn in different coordinates — an exact translation, not a loose correlation. The Gaussian process is only the lookup table for that translation, trained on the times both windows were intact. You still need one sensor that never drops out, because that complete window is the coordinate chart everything else is translated from.

## Limitations and assumptions

- The core recipe requires at least one fully observed anchor. The sketched “lag FPRM” extension for the all-missing case still fails on long gaps that hit every channel at once. The authors state this limit.
- The guarantee is for low-dimensional deterministic dynamics. Strongly stochastic series, and abrupt regime switches, should break the embedding. The paper flags tipping points as unresolved.
- Anchor quality varies with no a priori selector. The paper’s explanation (“noise and complexity”) is thin.
- The paper reports no wall-clock time or memory. It trains one Gaussian process per incomplete channel — hundreds of models on the traffic set — and says nothing about scaling past that.
- Tested missingness is continuous blocks, threshold cuts, and periodic dropouts, not a full missing-not-at-random taxonomy.
- This ingest reads the accepted manuscript (captions and Table 1, not the rendered figures) and did not pull the supplementary climate runs. Treat numbers as provisional against the Version of Record.

## Connections

- Complex-systems / machine-learning cousin, different job (forecast a cyclone, do not impute a gappy attractor): [[deepmind-hurricane-forecasting]]

## Source

- `raw/analyses/2026-09-20_doi-10.1038-s41467-026-77922-1_dynamics-informed-imputation-missing-systems-dynamics.md`
