**Access Status** — Full paper: uploaded directly as PDF with complete text extracted (main text, methods, extended data legends, references) · Abstract: present in full · Supplementary material: referenced but not uploaded; analysis based on main text and extended data legends · Analysis basis: full text

## 1. Google DeepMind Cracks the Hurricane Forecasting Bottleneck — With Coarser Data Than the Models It Beats

A single AI system, trained end-to-end on both global weather data and a curated cyclone database, simultaneously outperforms the world's best global model on track *and* the best regional model on intensity — breaking a decades-old trade-off the field assumed was fundamental.

## 2. Big-Picture Context

Tropical cyclone forecasting has been stuck on a scaling dilemma for decades. Predicting *where* a cyclone goes (track) requires capturing large-scale atmospheric steering currents, which global models like ECMWF's ENS do well at ~28 km resolution. Predicting *how strong* it gets (intensity) requires resolving the fine-scale thermodynamic processes in and around the eyewall, which demands resolutions of a few kilometres — the domain of specialised regional models like NOAA's HAFS. Running a regional model at high resolution over a large domain is computationally prohibitive, so forecasters have lived with a painful trade-off: use the global model for track, the regional model for intensity, and hope the two stories don't contradict each other too badly. No single system has excelled at both simultaneously.

The first generation of AI weather models (GraphCast, Pangu-Weather, GenCast) demonstrated that machine learning could match or beat traditional numerical weather prediction (NWP) on global atmospheric variables. They inherited excellent track forecasting from the global analysis data they trained on, but they also inherited the analysis data's inability to resolve cyclone peak winds — a 0.25° grid simply cannot represent a 30 km eyewall. Intensity forecasts from these models were systematically low-biased, and this was widely noted as a fundamental limitation of the approach.

This paper introduces WeatherNext Cyclones (WN-C), which breaks this impasse by doing something conceptually simple but technically non-trivial: it trains a single model to jointly predict both the coarse global atmospheric state *and* a separate set of cyclone-specific variables (position, intensity, wind radii) drawn from the IBTrACS best-track database. The cyclone variables are "griddified" — mapped onto the same 0.25° grid as auxiliary output channels — so the model can learn to infer fine-scale storm properties from the large-scale atmospheric context, even though the input resolution can't directly see them. The claim is that the coarse atmospheric data contains far more intensity signal than anyone previously recognised, and that the right learning architecture can extract it.

**Paper Type & Stakes:** This is a large-scale systems/engineering paper demonstrating an operational AI weather model that achieves state-of-the-art performance across multiple tropical cyclone forecasting tasks simultaneously. The stakes are high both scientifically (it challenges the assumption that high resolution is prerequisite for intensity skill) and practically (the system has already been adopted operationally by the U.S. National Hurricane Center and other WMO forecast centres).

**Prior Belief Check**

This result substantially complicates the prior consensus. The field broadly accepted that intensity forecasting required high-resolution simulation of inner-core processes, and that AI models trained on coarse analysis data were fundamentally limited in intensity skill. WN-C's demonstration that a global model on a ~28 km grid can beat HAFS (which runs at ~2 km resolution) on intensity is genuinely surprising to experts — not because better intensity was unexpected eventually, but because the resolution gap was considered a hard barrier, not a soft one. The track improvements are less surprising (AI models were already competitive), but the *magnitude* — over a day of additional lead time versus ENS — exceeds the incremental improvements the field has seen from NWP over the past decade. The consensus-ensemble results (18–38% track improvement, 5–14% intensity improvement when WN-C is added to TVCN/IVCN) are arguably the most operationally significant, since forecasters ultimately rely on consensus products.

**Replication & Convergence Note**

This is a single-group result from Google DeepMind, with co-authors from NOAA/NHC, CIRA, and UK Met Office contributing to validation and operational evaluation. The 2025 NHC hurricane season evaluation provides something close to independent operational validation, but the model development and core evaluation are from one team. Independent confirmation would require another group reproducing comparable track+intensity skill using a different architecture or training approach — particularly the intensity result, which is the most novel claim. The code and weights have been released, which lowers the barrier to replication.

## 3. Necessary Background Crash-Course

**The scale dilemma as a cache-hierarchy problem.** Think of cyclone forecasting like trying to predict both the throughput of an entire data center network (track) and the hotspot temperature of a single die (intensity). The network throughput depends on large-scale routing patterns you can capture with coarse monitoring. The die temperature depends on micro-architectural details that require fine-grained sensors. Traditional NWP solves this by running two separate systems at different granularities — a global model for the "network" and a regional model for the "die." WN-C's trick is to discover that the coarse network-level monitoring actually contains enough correlated signal to infer die temperatures, if you know what patterns to look for.

**Breaks when:** the analogy implies the coarse data *contains* the fine-scale information in a lossless sense. It doesn't — the 0.25° grid genuinely cannot resolve an eyewall. What WN-C learns is a *statistical mapping* from large-scale context to intensity, not a physical reconstruction of inner-core dynamics. This means it should fail on storms whose intensity is determined by processes truly uncorrelated with the large-scale environment (though the results suggest this happens less often than assumed).

**Ensemble forecasting as Monte Carlo sampling.** Weather is chaotic — small differences in initial conditions lead to diverging futures. An ensemble forecast runs the model many times with slightly different starting conditions or internal perturbations, producing a distribution of possible outcomes rather than a single prediction. You can think of it like running a benchmark suite with randomised cache-line alignments: each run is individually valid, but the *distribution* of results tells you about the system's sensitivity to things you can't control. A well-calibrated ensemble has spread (the scatter among members) that matches skill (the typical error of the mean) — the spread/skill ratio should be close to 1.0.

**Breaks when:** you push the analogy to assume ensemble members are independent samples from a well-defined distribution. They're not — they share the same model architecture and training data, so systematic biases appear in every member. The ensemble captures *forecast uncertainty*, not *model uncertainty* in general.

**CRPS: the proper scoring rule for probabilistic forecasts.** The Continuous Ranked Probability Score measures how well a predicted probability distribution matches reality. Think of it like a loss function that penalises you not just for getting the mean wrong, but for getting the *shape of your uncertainty* wrong. A forecast that says "50 ± 5 knots" when reality is 80 knots gets penalised more than one that says "50 ± 30 knots" — the second was wrong on the mean but honest about its uncertainty. CRPS is "strictly proper," meaning the only way to minimise it is to report your true belief — you can't game it by hedging.

**Breaks when:** you assume CRPS constrains the full *joint* distribution. It doesn't — it's a marginal loss, evaluated independently at each location and variable. Two forecasts can have identical CRPS but completely different spatial correlation structures. This matters for cyclones, where position, intensity, and wind radii are physically coupled.

**Central analogy for this paper:** coarse monitoring that learns to infer fine-scale hotspots

## 4. Core Technical Explanation

### The dual-modality formulation

WN-C's fundamental insight is to treat cyclone forecasting as a *joint prediction* problem over two data types. The first is the dense global atmospheric state *X* — six variables at 13 pressure levels plus six surface variables, on a 0.25° latitude-longitude grid (the same inputs used by GraphCast and GenCast). The second is a sparse, tabular set of cyclone trajectories *C*, drawn from IBTrACS — position (latitude, longitude), maximum sustained wind speed, minimum sea level pressure, radius of maximum wind, and quadrant wind radii at three thresholds (34, 50, 64 kt).

The system models this as a second-order Markov process with 6-hour timesteps: given the atmospheric state at times *t*−1 and *t*, predict the joint state at time *t*+1. Applied autoregressively, this produces 15-day ensemble forecasts.

### The griddification trick

The core engineering challenge is bridging the representation gap between the dense gridded atmospheric data (~20 TB of training data) and the sparse tabular cyclone data (~10 MB from IBTrACS). The authors solve this with a "griddification" mapping that converts each cyclone's tabular properties into two gridded channels on the same 0.25° grid:

The **existence probability field** *E* places a Gaussian kernel (width ℓ = 120 km) at each cyclone centre — this creates a smooth, differentiable target that the model can learn to predict, inspired by the CornerNet approach from object detection in computer vision. The **conditional scalar fields** *S* broadcast each cyclone's scalar properties (intensity, radii, etc.) within 120 km discs around the true centre, masked to NaN elsewhere — so the model only receives training signal for cyclone properties at locations where a cyclone actually exists.

Think of this like the difference between maintaining a sparse hash table of active objects and rasterising them onto a dense framebuffer. The model operates on the framebuffer during training and prediction, but a heuristic tracker "de-rasterises" at inference time to recover tabular trajectories.

### Functional Generative Networks (FGNs)

This is the paper's primary methodological contribution over GenCast. GenCast uses a diffusion model, which requires ~40 neural network forward passes per timestep to denoise a sample. WN-C replaces this with what the authors call a *functional generative network*: a single forward pass with stochastic parameters.

The idea: instead of injecting noise into the input or output and iteratively denoising (diffusion), inject noise into the *model's own parameters* and run it once. Specifically, a 32-dimensional Gaussian noise vector is passed through all of the network's conditional layer-norm layers, so that different noise draws produce different ensemble members. The parameters are decomposed as θ = θ\* + Δ · ε, where θ\* is the deterministic mean, Δ is a learned matrix controlling the covariance, and ε is standard Gaussian noise.

This has two critical properties. First, the noise is *low-dimensional* (32 components) and *globally shared* across all spatial locations — which forces the model to produce spatially coherent perturbations rather than pixel-level noise. This is analogous to the difference between perturbing a single global configuration register that affects all cores uniformly (producing coherent system-wide behaviour changes) versus independently flipping random bits at each memory address (producing incoherent noise). Second, it requires only one forward pass per ensemble member per timestep, making it 8× faster than GenCast at inference.

The model is trained using the fair CRPS loss with just two ensemble members per training step (the minimum for an unbiased CRPS estimate). Epistemic uncertainty is captured via deep ensembles — four independently trained model seeds whose predictions are combined at inference time.

### The co-training pipeline

Training proceeds in six stages of increasing complexity:

Stages 1–3 are pure atmospheric pre-training, progressively increasing from 1° / 12-hour resolution to 0.25° / 6-hour resolution. Stage 4 introduces the cyclone targets (the griddified IBTrACS channels) but only trains the final output layer for those channels, keeping the atmospheric backbone frozen. Stage 5 unfreezes everything and trains end-to-end on both atmospheric and cyclone targets. Stage 6 adds autoregressive unrolling, backpropagating gradients through up to 8 sequential 6-hour steps (48 hours) to improve long-range stability.

This staged approach is elegant: the atmospheric pre-training builds a robust weather foundation, the frozen-backbone cyclone stage initialises the cyclone output heads without disrupting weather skill, and the end-to-end fine-tuning lets the two tasks mutually benefit. The ablation studies show that co-training improves *both* atmospheric forecasting and cyclone prediction — the ~20 TB atmospheric dataset provides generalisation capacity that benefits the ~10 MB cyclone dataset, and cyclone supervision provides gradient signal that improves the model's representation of physically important processes.

### The tracking algorithm

At inference time, the model predicts griddified cyclone fields, which a heuristic "direct tracker" converts back to tabular trajectories. The tracker uses momentum-based extrapolation for an initial position guess, then refines using a "mode-then-mean" strategy on the existence probability field (find the peak, then compute a probability-weighted centroid around it). Tracks are dissipated when the mean existence probability within 500 km falls below 10⁻⁵, and a pruning step prevents track merging. New cyclone genesis is detected by scanning for high-probability regions in the existence field that aren't associated with existing tracks.

### Assumption Audit

**Watch:** Reader likely assumes the intensity improvement comes from *higher effective resolution* learned by the model. The paper actually says the improvement comes from *co-training on IBTrACS* — the model learns a statistical mapping from large-scale atmospheric context to cyclone intensity, not a super-resolution reconstruction of inner-core dynamics. The input resolution is the same 0.25° as GenCast.

**Watch:** Reader likely assumes the 8× speed advantage of FGN over GenCast comes from model compression or simplification. The paper actually says WN-C is a *larger* model (~180M parameters vs GenCast's ~57M) — the speed gain is purely architectural, from eliminating the iterative denoising loop. The model can afford to be bigger precisely because it only needs one forward pass.

**Watch:** Reader likely assumes the ensemble spread is generated by perturbing initial conditions. The paper actually says WN-C uses *no initial condition perturbations* — all aleatoric uncertainty comes from the learned parameter perturbations in the FGN, and epistemic uncertainty from the four-seed deep ensemble. This is a fundamentally different uncertainty model from traditional NWP ensembles, which primarily perturb initial conditions and model physics.

## 5. What's Genuinely New or Clever

**The co-training insight is the headline.** The field assumed high resolution was prerequisite for intensity skill. WN-C shows that a 0.25° model, given direct supervision from IBTrACS best-track data, can beat a 2 km regional model at its own game. This isn't just "AI is better" — it's a scientific claim that the large-scale atmospheric state contains more intensity-relevant information than the community recognised, because no one had previously tried to learn a direct mapping from it. The fact that co-training also improves atmospheric forecasting (~6 hours of track gain at long lead times from the cyclone supervision alone) suggests that cyclone dynamics encode information about large-scale flow that the atmospheric-only training misses.

**FGNs as a replacement for diffusion.** Injecting stochasticity through parameter perturbations rather than input/output noise is not itself new (it has roots in NWP stochastic physics and RL exploration), but applying it to high-dimensional weather prediction with a strictly proper scoring rule loss is. The key insight is that conditional normalisation layers — originally designed for diffusion models to condition on noise level — can be repurposed as the injection point for ensemble-generating noise, and that keeping the noise low-dimensional and spatially shared forces global coherence. This is a genuine architectural contribution that could apply broadly beyond weather.

**The griddification/de-griddification pipeline** is a clean engineering solution to the representation mismatch between sparse object-level data and dense field-level prediction. By separating differentiable training (on the grid) from non-differentiable tracking (at inference), they get the best of both worlds.

**Predictive Content Check**

**Falsifiable handle:** The paper makes several specific, falsifiable predictions. The most concrete: WN-C's 5-day track error of 230 km should hold (or improve) on future hurricane seasons, and its intensity MAE should remain below HAFS across all basins. The rapid intensification CSI improvement from ~0.3 to ~0.5 is also directly testable on the next RI event. The 2025 NHC basin evaluation (Extended Data Fig. 1) already provides partial out-of-sample validation. The broader scientific claim — that coarse atmospheric data contains underexploited intensity signal — predicts that other groups using different architectures but similar co-training strategies should achieve comparable intensity gains. If the intensity skill turns out to be architecture-specific rather than data-access-specific, the scientific interpretation weakens even if the engineering result stands.

## 6. Limitations & Open Questions

**The model has no intensity physics — it has intensity statistics.** WN-C does not simulate the thermodynamic processes that drive intensification; it learns correlations between large-scale atmospheric patterns and observed intensity outcomes. This works on average but may fail on physically unusual storms — cases where intensity is determined by unresolved processes genuinely uncorrelated with the large-scale environment (e.g., eyewall replacement cycles, mesovortex-driven intensification, rapid ocean cooling). The paper does not analyse performance conditioned on physical mechanism. **(B) Contested** — some researchers argue statistical approaches can learn these relationships implicitly; others maintain that explicit physics is necessary for reliable extreme-event prediction, especially under climate change. **(analyst inference)**

**Evaluation is retrospective, not prospective, for most results.** The 2023–2024 evaluations are reforecasts (hindcasts run after the fact with frozen model design), and while the 2025 NHC evaluation is closer to operational, the model design was still frozen before that season. True operational skill assessment requires multiple seasons of live, real-time forecasting with no model updates during the evaluation period. **(A) Consensus** — this limitation is explicitly acknowledged in standard forecast verification practice and applies to all new models. **(broader literature)**

**IBTrACS is not ground truth — it's expert-curated best estimates.** Best-track intensity estimates, particularly in basins without aircraft reconnaissance, carry substantial uncertainty (±10–15 kt for wind speed). The model is trained and evaluated against these estimates, so the reported skill improvements are relative to a noisy target. In basins with weaker observational coverage, the model may be learning the biases of the best-track analysts rather than true atmospheric physics. **(A) Consensus** — this is a well-known limitation of the best-track paradigm, acknowledged explicitly by the operational community. **(broader literature)**

**No precipitation, storm surge, or wind gust prediction.** The paper acknowledges this directly (§9). For end-users, the downstream impacts of a cyclone (flooding, wind damage, storm surge) matter more than track and peak wind speed. WN-C in its current form provides guidance inputs, not impact outputs. **(A) Consensus** — the authors state this as future work. **(paper §9)**

**Intensity calibration, while much better than baselines, still shows underspread.** The intensity spread/skill ratio is ~0.8, meaning the ensemble is slightly overconfident about intensity predictions. For the tail events that matter most (rapid intensification of major hurricanes), this underspread could lead to insufficient warning. **(B) Contested** — the degree to which this matters operationally depends on how forecasters use the ensemble guidance, and WN-C's calibration is substantially better than all baselines. **(paper §6, Fig. 3d)**

**The consensus ensemble weights were optimised on a small validation set.** The TVCN+WN-C and IVCN+WN-C weights were tuned on 2022 cyclones in two basins, then held fixed across all lead times and basins for testing. With such limited optimisation data, the weights may not generalise to unusual seasons or underrepresented basins. The paper acknowledges the potential for slight overfitting. **(B) Contested** — the improvements are statistically significant and consistent enough to suggest robustness, but the optimisation sample is genuinely small. **(paper §15)**

**Dependence on ECMWF analysis as input.** WN-C requires ECMWF's operational analysis (HRES-fc0) as initial conditions, creating a dependency on another institution's infrastructure and data quality. If the analysis system degrades, changes, or becomes unavailable, WN-C's skill degrades correspondingly. The paper acknowledges this and flags direct observation assimilation as a necessary future direction. **(A) Consensus** — this applies to all analysis-dependent AI weather models. **(paper §9)**

## 7. Detailed Summary & Explanation

WeatherNext Cyclones (WN-C) is an AI-based operational weather model from Google DeepMind that produces ensemble forecasts of tropical cyclone track, intensity, and wind structure globally, extending to 15 days. The central innovation is *co-training*: a single probabilistic model is trained jointly on decades of global atmospheric analysis data from ECMWF (capturing large-scale weather dynamics) and the IBTrACS best-track database of ~5,000 historical tropical cyclones (providing direct supervision for cyclone-specific properties that the coarse atmospheric grid cannot resolve). This co-training allows the model to learn statistical relationships between the large-scale atmospheric environment and fine-scale storm properties — particularly intensity — that traditional approaches assumed required explicit high-resolution simulation.

The model's probabilistic architecture, called functional generative networks (FGNs), generates ensemble diversity by perturbing the neural network's own parameters through learned conditional normalisation layers, rather than through the iterative denoising process used by diffusion models like GenCast. This yields an 8× inference speedup while maintaining or improving ensemble calibration, and enables practical generation of ensembles with up to 1,000 members — far beyond the 50-member limit of conventional NWP ensembles.

Evaluated on tropical cyclones from 2023–2025, WN-C achieves state-of-the-art performance across all major forecasting metrics. Its track forecasts provide over a day of additional lead time compared to ECMWF's ENS (the best global system) and roughly 24 hours over GenCast (the previous best AI model). Its intensity forecasts outperform NOAA's HAFS — a specialised high-resolution regional model specifically designed for intensity prediction — by 3.75 kt at 3 days, matching a decade of NWP progress. Its wind radii forecasts and rapid intensification predictions also surpass all baselines. When added to the NHC's operational consensus ensembles (TVCN for track, IVCN for intensity), WN-C improves track accuracy by 18–38% and intensity accuracy by 5–14%.

The analysis is framed this way because the paper makes two separable claims, and it's important to distinguish them. The *engineering* claim — that WN-C is the best cyclone forecasting system currently available — is strongly supported by comprehensive benchmarking across multiple metrics, basins, and years, with rigorous statistical testing. The *scientific* claim — that high resolution is not a prerequisite for intensity forecasting, and that coarse atmospheric data contains underexploited intensity signal — is more provocative and less definitively established. It could be that WN-C succeeds not because the large-scale atmosphere carries intensity information in general, but because a massive neural network trained on historical outcomes is very good at learning empirical correlations that happen to work on the evaluation set. Distinguishing "the physics is there but we weren't looking for it" from "the statistics happen to work right now" requires independent replication, robustness under climate change, and mechanistic analysis of what the model has learned — none of which the paper provides.

The key interpretive takeaway: WN-C represents a genuine paradigm shift in tropical cyclone forecasting, with immediate operational value already being realised at NHC and other forecast centres. But the deeper scientific question — *why* it works at coarse resolution — remains open, and the answer matters for how much we should trust it on the unprecedented storms that climate change will deliver.

**Where I'm least confident in this analysis:** The FGN contribution. I've described the mechanism (low-dimensional noise through conditional normalisation) and the key property (spatially coherent ensemble diversity from a marginals-only loss), but the theoretical argument for *why* this works — why marginal CRPS training with functional perturbations yields good joint distributions in very high-dimensional spaces — is left somewhat implicit in the paper and relies on empirical demonstration rather than theory. My explanation of this mechanism may miss subtleties about the interaction between the low-dimensional noise, the parameter-sharing across spatial dimensions, and the multi-scale structure of the icosahedral mesh that collectively make this work.

## 8. Three Crystallized Takeaways

1.  **A single AI model now beats the world's best global system on cyclone track AND the world's best regional system on intensity — breaking a trade-off the field treated as fundamental.** The trick: train on both weather data and a curated cyclone database simultaneously, letting the model discover that coarse atmospheric data carries far more intensity signal than anyone thought.
2.  **Speed matters as much as accuracy.** By replacing diffusion with single-pass parameter perturbations, WN-C generates 1,000-member ensembles in minutes rather than hours — enabling reliable estimation of rare, high-consequence events like rapid intensification that 50-member ensembles systematically miss.
3.  **The model is already operational.** NHC began using WN-C during the 2025 Atlantic hurricane season, and adding it to the standard consensus ensemble improved track forecasts by 28% and intensity forecasts by 6% on average — the kind of immediate, measurable impact that usually takes a decade of NWP development to achieve.

## 9. Shorter Summary

WeatherNext Cyclones (WN-C) is an AI weather model from Google DeepMind that forecasts tropical cyclone track, intensity, and wind structure globally for up to 15 days. It solves a long-standing problem in hurricane forecasting: global models predict where storms go well but not how strong they get, while specialised regional models do the reverse. No single system has excelled at both — until now.

The key innovation is co-training. WN-C jointly learns from two data sources: decades of global atmospheric analysis (capturing large-scale weather patterns) and a curated database of approximately 5,000 historical tropical cyclones (providing direct supervision for storm-specific properties). This teaches the model to infer fine-scale intensity from coarse-resolution inputs, without requiring the expensive high-resolution simulations traditionally considered essential.

The model uses a novel probabilistic architecture called functional generative networks, which generates ensemble diversity through learned perturbations of the neural network's own parameters rather than through iterative denoising. This makes it roughly eight times faster than previous AI approaches and enables practical generation of very large ensembles — up to 1,000 members — that better capture rare, dangerous events like rapid intensification.

Evaluated on storms from 2023 to 2025, WN-C provides over a day of additional lead time on track versus the best global model and outperforms the best regional intensity model by a margin matching a decade of conventional progress. Its forecasts are already being used operationally at the U.S. National Hurricane Center, where adding WN-C to the standard consensus ensemble improved track accuracy by roughly 28 percent and intensity accuracy by 6 percent on average. The model's code and weights are publicly released.

The deeper scientific question — whether the intensity skill reflects genuinely underexploited physical signal in the large-scale atmosphere, or learned statistical correlations that may not generalise to unprecedented future storms — remains open and consequential.

The idea: instead of injecting noise into the input or output and iteratively denoising (diffusion), inject noise into the model's own parameters and run it once. Specifically, a 32-dimensional Gaussian noise vector is passed through all of the network's conditional layer-norm layers, so that different noise draws produce different ensemble members. The parameters are decomposed as θ = θ\* + Δ · ε, where θ\* is the deterministic mean, Δ is a learned matrix controlling the covariance, and ε is standard Gaussian noise.

Thought for 8s

Responding

Good — that paragraph compressed a lot of machinery into a small space. Let me unpack the mechanism layer by layer.

### What conditional layer-norm actually is

Start with regular layer normalization, which you can think of as a per-sample standardization step inside the network. At each layer, the activations (the intermediate feature vectors flowing through the network) get their mean subtracted and are divided by their standard deviation, then rescaled by two learned parameters: a scale γ and a shift β. Every layer has its own γ and β, but they're *fixed* after training — the same values apply regardless of input.

*Conditional* layer-norm makes γ and β *functions of some external conditioning signal* rather than fixed constants. In GenCast, that conditioning signal is the diffusion noise level σ — the network needs to know how noisy its current input is so it can denoise appropriately. The conditional parameters are typically computed by a small learned linear mapping: given the conditioning input *z*, you get γ(*z*) and β(*z*).

The key architectural fact: these γ and β parameters modulate the *gain and bias* of every activation in the layer. They're applied *after* the normalization and *before* the nonlinearity. So they control the effective operating point of the entire layer — which features are amplified, which are suppressed, and what the baseline activation level is.

**Breaks when:** you think of this as changing the network's "weights" in the usual sense. The actual weight matrices (the ones that do the heavy linear transformations) are unchanged. What changes is the *normalization statistics* — closer to adjusting the voltage rails on a circuit than rewiring the circuit itself. But because normalisation sits between every major computation, small changes here propagate pervasively.

### The repurposing move

In GenCast, the conditioning signal is the diffusion noise level — a single scalar σ that tells the network "how much denoising to do on this step." WN-C has no diffusion steps, so that conditioning input is now free. The authors repurpose it: instead of conditioning on σ, they condition on a random vector *z* ~ N(0,1)³², drawn fresh for each ensemble member and each timestep.

This is the core of the trick. The network architecture is essentially unchanged from GenCast's denoiser — same graph-transformer on an icosahedral mesh, same encoder/decoder structure. But instead of the conditional normalisation layers asking "what noise level am I denoising from?", they ask "which version of reality am I sampling?"

### Why 32 dimensions — the bottleneck argument

This is where the spatial coherence comes from, and it's worth thinking about carefully.

The model's output lives in an enormously high-dimensional space: 6 atmospheric variables × 13 pressure levels × ~1 million grid points, plus the cyclone channels. That's roughly 80+ million output dimensions. If you injected independent noise into each output dimension, you'd get spatially incoherent garbage — neighbouring grid points would fluctuate independently, producing forecasts with physically meaningless salt-and-pepper noise.

The 32-dimensional noise vector acts as an *information bottleneck*. Think of it like this: you have a building with 80 million light switches (the output dimensions), but only 32 control dials in the basement (the noise vector). Each dial, through the learned Δ mapping and the conditional normalisation layers, affects a *specific coordinated pattern* of switches throughout the building. Dial 1 might correspond to "shift the jet stream north and weaken the cyclone" — a physically coherent perturbation that affects millions of grid points in a correlated way. Dial 2 might correspond to "intensify the storm but keep the track fixed." The 32 dials can produce 32 independent *modes* of variability, and any ensemble member is a linear combination of those modes.

Too few dimensions (say, 1–2) and the model can only express a handful of distinct weather scenarios — the ensemble would be underdispersive (overconfident). Too many dimensions (say, 10,000) and the bottleneck loosens enough that the model could learn spatially incoherent perturbations — which is exactly what happens with per-pixel noise approaches that the paper mentions needing convolutional filters to fix.

32 is empirically chosen, but the order of magnitude makes sense: it's comparable to the number of *physically meaningful degrees of freedom* that distinguish plausible weather scenarios at the synoptic scale. You don't need a separate noise dimension for every grid point; you need one for each independent mode of large-scale atmospheric variability.

### The decomposition θ = θ\* + Δ · ε, concretely

Here's a worked micro-example. Suppose one conditional layer-norm layer has just 4 parameters: γ₁, γ₂ (scales) and β₁, β₂ (shifts). With a noise vector of dimension 2 (shrunk for illustration):

θ\* = \[γ₁\*, γ₂\*, β₁\*, β₂\*\] is the *deterministic* parameter vector — what the model would predict if there were no uncertainty. This is a point in 4-dimensional parameter space.

Δ is a 4 × 2 matrix — it maps from 2-dimensional noise space to 4-dimensional parameter space:

*Δ = \| 0.3 0.1 \|*

*\| -0.2 0.4 \|*

*\| 0.5 -0.1 \|*

*\| 0.0 0.3 \|*

ε is drawn as a 2-dimensional standard Gaussian: say ε = \[1.2, −0.7\] for one ensemble member.

Then the perturbed parameters are:

θ = θ\* + Δ · ε = θ\* + \[0.3×1.2 + 0.1×(−0.7), −0.2×1.2 + 0.4×(−0.7), ...\] = θ\* + \[0.29, −0.52, 0.67, −0.21\]

A different ensemble member draws ε = \[−0.5, 1.8\] and gets a completely different perturbation. But both perturbations are *constrained to the 2-dimensional subspace* spanned by Δ's columns. Column 1 of Δ is the "direction" in parameter space that noise component 1 moves you along; column 2 is the direction for noise component 2.

The matrix Δ is *learned during training* alongside θ\*. CRPS training encourages the model to find the Δ that produces ensemble spread matching the true forecast uncertainty — if Δ is too small, the ensemble is overconfident and CRPS penalises it; if too large, the ensemble is overdispersive and CRPS penalises that too.

### Why parameter-sharing makes this spatially coherent

Here's the architectural detail that ties it together. In the graph-transformer processor, the same conditional layer-norm parameters are applied at *every mesh node*. The icosahedral mesh has ~40,000 nodes (for the 6-times-refined mesh), but the γ(*z*) and β(*z*) values computed from the noise vector *z* are *shared* identically across all 40,000 nodes.

This is the parameter-sharing argument from the paper: because the same perturbation is applied everywhere simultaneously, the effect on the output is necessarily spatially coherent. If the perturbation amplifies a particular feature channel, it amplifies it *globally*, which manifests as a coherent large-scale weather pattern shift — not as independent pixel-level noise.

The combination of low-dimensional noise (32D) and spatial parameter sharing is what lets CRPS — a marginals-only loss — produce good *joint* distributions. The model literally cannot produce spatially incoherent samples, because the noise injection mechanism doesn't have enough degrees of freedom to vary independently at each location. The joint structure is baked in by architectural constraint, not learned from a joint loss.

### How this differs from diffusion, mechanically

In GenCast's diffusion approach: you start with pure noise in output space (random weather maps), then iteratively denoise over ~40 steps, each step removing a fraction of the noise. Each step requires a full forward pass through the network. The stochasticity comes from the initial noise and from the stochastic sampling during denoising. The 40-pass requirement is the cost of producing high-quality samples from a learned distribution.

In WN-C's FGN approach: you draw one noise vector *z*, compute the perturbed normalisation parameters once, and run a single forward pass. The stochasticity is in the *function itself* (which function from the family you're evaluating), not in the input or the sampling process. One pass, one sample — hence 8× faster (actually the model is ~3× larger, so the raw speedup per FLOP is more like 24×, partially offset by the larger model).

The trade-off: diffusion has a richer expressivity for the output distribution (it can, in principle, model arbitrary distributions through iterative refinement), while FGNs are constrained to distributions that can be expressed through low-dimensional parameter perturbations of a single forward pass. The paper's results suggest that for weather forecasting, this constrained family is expressive enough — and the constraints actually *help* by forcing spatial coherence.
