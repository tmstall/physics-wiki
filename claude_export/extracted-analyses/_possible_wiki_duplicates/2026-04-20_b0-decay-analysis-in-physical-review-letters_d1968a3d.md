---
source: claude_export
conversation_uuid: d1968a3d-49a0-447f-9781-6e7cc56fc1a4
title: "-> B0 decay analysis in Physical Review Letters"
created_at: 2026-04-20T22:12:36.660777Z
updated_at: 2026-05-10T23:56:12.615931Z
tier: A
score: 223
n_messages: 2
---

# -> B0 decay analysis in Physical Review Letters

## Human

Detailed analysis of this paper Publication details
A comprehensive analysis of the B0 -> K*0μ+μ- decay, Physical Review Letters (2026). DOI: 10.1103/24g9-yn9d. On arXiv: DOI: 10.48550/arxiv.2512.18053

Journal information: Physical Review Letters  , arXiv

## Assistant

Fetching

**Analysis v3.4.9**

---

## The Flavor Anomaly That Won't Die: LHCb's Definitive B→K*μμ Report Still Can't Explain Its Own Deviations

*The most complete angular snapshot yet of B⁰ → K*⁰ μ⁺μ⁻ uses LHCb's full Run 1+2 dataset — and the stubborn tensions with the Standard Model are still there, still statistically short of discovery, and still theoretically ambiguous enough to keep everyone arguing.*

---

### 1. Big-Picture Context

B-meson decays into a kaon, a pion, and two muons are particle physics gold. The B⁰ meson itself is a bound state of a bottom antiquark and a down quark. When it decays as B⁰ → K*⁰ μ⁺μ⁻, the underlying quark-level event is a bottom quark flipping into a strange quark while emitting a muon-antimuon pair — the so-called b → s μ⁺μ⁻ transition. The Standard Model (SM) forbids this at tree level: no single diagram connects b → s + leptons directly. Instead, it can only happen via quantum loops — virtual top quarks and W/Z bosons flickering into existence for a brief moment.

That's exactly what makes the decay so powerful as a new-physics probe. Because the SM amplitude is loop-suppressed (it only happens "by detour"), any new heavy particle that also mediates the same transition can compete on nearly equal footing, potentially showing up as a measurable deviation in how the decay products fly apart. Think of it like testing the background noise floor of a circuit: the weaker the nominal signal, the easier it is for extraneous pickup to appear.

LHCb analyzed the decay B⁰ → K*⁰(→ K⁺π⁻) μ⁺μ⁻ using 8.4 fb⁻¹ of proton-proton collision data, representing the full Run 1 and Run 2 dataset. This is the definitive "close-out" angular analysis before the experiment's Upgrade I data dominates. The paper presents the full set of CP-averaged and CP-asymmetric angular observables in bins of the invariant mass squared of the dimuon system, along with the branching fraction relative to the B⁰ → J/ψ(→μ⁺μ⁻)K⁺π⁻ decay.

The B → K*ℓ⁺ℓ⁻ anomaly story stretches back to 2013. Each successive LHCb dataset has sharpened the picture without resolving it: the tensions show up in the same angular observable (called P₅′) in the same q² bins, keep hovering around 2–3σ, and refuse to either go away or grow into a discovery. This paper is the most complete version of that story yet.

---

### 2. Background Crash-Course

**The decay geometry and three angles.** When the B⁰ decays, you reconstruct three decay angles: θₗ (angle of the μ⁺ relative to the B in the dimuon rest frame), θ_K (angle of the K⁺ in the K*⁰ rest frame), and φ (the azimuthal angle between the two decay planes). Plot the full 3D distribution of events in these angles versus q² (the dimuon invariant mass squared, in units of GeV²/c⁴), and you get a rich set of "angular observables" — essentially the Fourier-like coefficients of this 3D distribution. Think of it like measuring the radiation pattern of an antenna: the exact shape tells you about the polarization state and interference structure of the underlying physics.

**The P-basis and why it matters.** The theoretically cleanest observables are the "P_i′" basis (prime observables), specifically designed so that hadronic form-factor uncertainties largely cancel out. P₅′ is the star: it's sensitive to interference between left-handed and right-handed muon currents. If only SM amplitudes contribute, it predicts a specific curve vs. q². New physics shifts that curve.

**Wilson coefficients as the control knobs.** The SM weak interaction at low energies can be written as an effective field theory (EFT). The "Wilson coefficients" C₉ and C₁₀ are the strength knobs for the vector and axial vector couplings of the b → sμ⁺μ⁻ operator. Like amplifier gain settings — SM predicts specific values; any BSM physics shifts the gain. The angular observables directly constrain these knobs.

**CP symmetry and asymmetries.** CP stands for charge conjugation × parity. If CP is a good symmetry of the decay, then B⁰ and B̄⁰ decay identically (mirrored). The CP-averaged observables are the mean; CP-asymmetric ones are the difference. Non-zero CP asymmetries could signal direct CP violation in these rare decays.

**The S-wave background.** The K*⁰ resonance isn't the only way K⁺π⁻ can be produced. A non-resonant (S-wave) K⁺π⁻ pair can also contribute — it's orbital-angular-momentum zero rather than one, so it has its own distinct angular distribution. Including it properly is bookkeeping work, but the S-wave amplitudes carry their own physical observables.

---

### 3. Core Technical Explanation

**Data and sample.** LHCb uses 8.4 fb⁻¹ of proton-proton collision data collected at Run 1 and Run 2 center-of-mass energies. The B⁰ candidate is reconstructed from two identified muon tracks and two hadron tracks (K⁺ and π⁻) fit to a common displaced vertex. The K*⁰ mass window is constrained to suppress backgrounds. Two control modes — B⁰ → J/ψK*⁰ and B⁺ → J/ψK⁺ — provide the efficiency corrections, and differences between them are used to assess systematic uncertainties.

**Background suppression.** A Boosted Decision Tree (BDT) classifier handles the nastiest background: B⁺ → K⁺μ⁺μ⁻ events where one muon is combined with a stray pion. A dedicated BDT trained on simulation suppresses this to a negligible level. Semileptonic cascade backgrounds (B → D(→Kμ⁻X)μ⁺X) are also eliminated.

**The angular fit itself.** The analysis performs an unbinned maximum likelihood fit across the three decay angles and the K⁺π⁻ invariant mass simultaneously, in bins of q². The fit simultaneously extracts all CP-averaged Si and CP-asymmetric Ai angular observables. Critically, the P-wave K*⁰ decay and the S-wave K⁺π⁻ contribution are handled together — the angular distribution of the S-wave component has a different functional form (isotropic in θ_K instead of cos²θ_K for P-wave), so the fit disentangles them.

**Two firsts in this paper.** For the first time, the full set of observables pertaining to the K⁺π⁻ S-wave contribution to the final state are presented. Consideration is also given for the first time to effects arising from the mass of the muons. In most previous analyses, muons were treated as massless. At low q² — where the dimuon invariant mass is not much bigger than twice the muon mass (roughly 0.21 GeV) — this approximation breaks down. Including finite muon mass adds additional angular structures (terms proportional to m²_μ/q²) that were previously ignored.

**Results: the tensions.** The measurements of the CP-averaged observables and the branching fractions continue to exhibit the pattern of tensions with Standard Model predictions seen in previous analyses using part of the dataset. In particular, P₅′ deviations in the 4 < q² < 8 GeV²/c⁴ region persist. A prior LHCb amplitude analysis of this same 8.4 fb⁻¹ dataset found that the Wilson coefficient C₉ responsible for vector dimuon currents shows a 2.1σ deviation from the Standard Model expectation. The binned angular analysis in this PRL paper tells a consistent story.

**CP asymmetries: nothing there.** The extracted CP-asymmetry observables show no significant deviations from zero. This rules out scenarios of large direct CP violation in these decays, though most BSM models predicting modified C₉ don't require it.

---

### 4. What's Genuinely New or Clever

**First complete S-wave observable set.** Previous analyses included S-wave as a nuisance — they fit the S-wave contribution to remove its contamination but didn't report S-wave observables as physics outputs. This paper for the first time extracts and publishes the full set of S-wave angular observables. These are new data points that constrain theories of the non-resonant K⁺π⁻ system in the presence of electroweak loops, and they may prove crucial for distinguishing hadronic from new-physics explanations of the overall tension.

**Muon mass effects.** The muon mass correction is subtle but matters at low q². The muon is 207 times heavier than the electron, so near threshold (q² ~ 4m²_μ ≈ 0.044 GeV²) helicity-flipping terms proportional to m²_μ/q² are not negligible. Including these adds new angular terms to the fit and potentially small but systematic shifts in the observables. At high luminosity, ignoring this would become a bias — so this paper closes that theoretical gap.

---

### 5. Limitations & Open Questions (brutally honest)

**The hadronic pollution problem hasn't gone away.** The dominant uncertainty in interpreting these tensions is not the experiment — it's theory. Charm-quark loop contributions ("charm rescattering") can fake shifts in C₉ at roughly the right size to explain the anomaly without any new physics. The significance of the tensions in angular observables is still dependent on theoretical estimates of hadronic contributions to the decays, and the community has not converged on whether the most favored explanation is new physics or underestimated hadronic effects.

**Significance plateau.** The anomaly has hovered near 3σ for a decade now across multiple dataset generations (3 fb⁻¹ → 4.7 fb⁻¹ → 8.4 fb⁻¹), persistently short of the 5σ discovery threshold. Each new dataset sharpens the measurement precision but doesn't dramatically change the picture because the tension is no longer statistics-limited — it's theory-limited. Without better hadronic calculations, more data won't decisively resolve the question.

**Lepton universality picture has partially softened.** The RK and RK* ratios — once the clearest signs of lepton non-universality — were reanalyzed by LHCb in 2022 and found to be consistent with the SM after correcting for a background misidentification. That major pillar of the "BSM flavor anomalies" story fell. The angular anomalies in B→K*μμ remain, but their interpretation has become more cautious.

**S-wave theory lags experiment.** Now that S-wave observables are measured for the first time, there are essentially no rigorous SM predictions to compare against. The experimental measurement has leapfrogged the theory.

**No CP violation means no new CP-odd phases.** Most attractive BSM models (leptoquarks, Z′ bosons) that explain the C₉ shift don't predict large CP asymmetries, so this null result is consistent but uninformative.

---

### 6. Three Crystallized Takeaways

1. **The B→K*μμ angular anomaly is real, persistent, and stubbornly sub-discovery** — the most complete LHCb analysis yet confirms the same pattern of deviations, but the 5σ finish line remains out of reach because hadronic theory, not statistics, is the bottleneck.

2. **Two genuine firsts here:** the S-wave angular observables and finite muon-mass corrections are both published for the first time — new physical inputs that refine the theory landscape but for which theoretical predictions largely don't yet exist.

3. **No CP asymmetry is itself informative** — it rules out a class of models with new CP-violating phases in b→s transitions, and confirms the deviation lives in CP-averaged amplitude interference, pointing toward a real-part shift in C₉.

---

### 7. Detailed Summary & Explanation

**What the decay is and why it's special.** The B⁰ meson (a bottom quark bound with a down antiquark) decays into a K*⁰ (kaon-star, which further decays to K⁺π⁻) and a muon-antimuon pair. At the quark level, the bottom quark changes flavor to a strange quark while emitting the muon pair. In the Standard Model, this is a "flavour-changing neutral current" (FCNC) — completely forbidden at leading order. It only happens via quantum loop diagrams involving virtual top quarks and electroweak gauge bosons. Because the amplitude is loop-suppressed, the branching fraction is tiny (about one in a million B decays). But this rarity is also the decay's superpower: any new-physics particle that couples to b→s transitions can contribute at comparable loop order, potentially leaving measurable fingerprints.

**Angular analysis as a tomography tool.** The decay has a rich kinematic structure — four final-state particles (K⁺, π⁻, μ⁺, μ⁻) give three meaningful angles and the dimuon invariant mass squared q². The full angular distribution, parameterized in bins of q², is essentially a decomposition into helicity amplitudes — the partial waves of the decay. Each term in the distribution has a coefficient (an "angular observable" labeled S_i or A_i) that isolates different combinations of those helicity amplitudes. Some of these, the P_i′ basis, are designed so that hadronic form-factor uncertainties largely cancel in ratios of amplitudes, making them theoretically clean tests of the electroweak sector. Think of it like using a polarimetry measurement on light: the Stokes parameters tell you about the polarization state without needing to know the source's total brightness.

**What the new analysis adds.** The dataset (8.4 fb⁻¹) is the full Run 1+2 LHCb sample — seven years of data combined. The 2025 PRL paper is the binned angular analysis using this full sample: it extracts all CP-averaged and CP-asymmetric observables vs. q², and does two things no previous version did. First, it fully characterizes the S-wave component — the non-resonant K⁺π⁻ contribution that contaminates the K*⁰ signal. The S-wave has its own angular observables (it's a distinct partial wave, angularly uniform in the kaon direction), and for the first time these are extracted and published as first-class measurements rather than nuisance parameters. Second, it includes effects from the finite muon mass. Near the dimuon production threshold (where q² is only slightly above four times the muon mass squared), helicity-suppressed terms proportional to the square of the muon mass divided by q² become non-negligible and affect the angular distribution in measurable ways.

**Where the tensions are.** The CP-averaged observable P₅′ — the most famous of the flavor anomaly signals — continues to show deviations from SM predictions in the 4–8 GeV²/c⁴ q² range. The branching fraction is also below SM predictions across multiple q² bins. The Wilson coefficient C₉ (the strength of the vector current b→sμμ coupling) deviates from its SM value at roughly 2σ when extracted from the angular fit. The CP-asymmetric observables are all consistent with zero — no evidence of new CP violation.

**Why it's not a discovery.** The key issue is that charm quarks circulate in the same loop diagrams and can produce hadronic "non-local" contributions — essentially long-distance QCD effects from virtual charmonium states (J/ψ, ψ(2S), and higher resonances) interfering with the signal. These effects are difficult to calculate from first principles and could mimic a shift in C₉ without any BSM physics. LHCb has dedicated separate analyses trying to isolate these (the "comprehensive amplitude" analyses from 2023–2024), finding the hadronic effects are larger than naively expected but not large enough to explain the full tension. The debate continues.

**Physical meaning of the S-wave observables.** The S-wave contribution arises from K⁺π⁻ pairs produced with zero relative orbital angular momentum (as opposed to the K*⁰ which is a p-wave, L=1, resonance). At the quark level, the same b→sμμ transition can produce a K⁺π⁻ pair without going through the K*⁰ pole — think of it as the continuum background under a resonance peak. The S-wave amplitudes interfere with the P-wave amplitudes, and that interference shows up in distinctive angular terms. Measuring the S-wave observables for the first time gives experimenters (and theorists) new constraints on QCD dynamics in this kinematic region.

**What muon mass effects do.** Muons are about 207 times heavier than electrons, so their mass is not negligible compared to the dimuon invariant mass at low q². When you include muon masses properly in the decay rate calculation, you get additional angular terms proportional to the ratio of the muon mass squared to q². These terms couple to different helicity amplitude combinations than the massless limit does, effectively mixing some of the observables and adding small but systematic corrections to the fit. Ignoring these would bias the extracted angular observables at low q², especially once the statistical uncertainties are small enough to reveal the effect.

---

### 8. Shorter Summary

LHCb used its full 8.4 fb⁻¹ Run 1+2 dataset to perform the definitive binned angular analysis of B⁰ → K*⁰ μ⁺μ⁻ decays. They extracted all CP-averaged and CP-asymmetric angular observables versus dimuon invariant mass, plus the decay branching fraction. Two features appear here for the first time in this mode: a complete set of S-wave (non-resonant K⁺π⁻) angular observables, and corrections for the finite muon mass at low dimuon masses. The main finding: the well-known pattern of tensions between measured angular observables and Standard Model predictions persists — specifically in the CP-averaged observables and branching fractions — at roughly the same significance level as before. The CP asymmetries are all consistent with zero. The experiment is now statistics-saturated; the remaining debate is about whether hadronic QCD effects (charm loops, non-local contributions) are large enough to explain the deviations, or whether new physics — most likely a shift in the vector electroweak coupling strength connecting bottom quarks to strange quarks and muon pairs — is required. That question requires better theory, not more data.
