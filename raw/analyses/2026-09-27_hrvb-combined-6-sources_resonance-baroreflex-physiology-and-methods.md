Analyzing | Framework v3.11 | six-source combined synthesis

**v3.11**

> **Access Status**
>
> | # | Source | What was retrieved | How |
> |---|---|---|---|
> | S1 | Vaschillo, Lehrer, Rishe & Konstantinov 2002 | Full text: methods, Table I, results, discussion, figure captions, limitations. Per-frequency figure values were **not** available as numbers, only as plots | academia.edu copy, two verbatim-extraction passes; abstract also from Springer |
> | S2 | Vaschillo, Vaschillo & Lehrer 2006 | Full text | hartfocus.nl re-hosted PDF, summary pass plus verbatim-quote pass |
> | S3 | Lehrer, Vaschillo, Lu, Eckberg, Vaschillo, Scardella & Habib 2006 (*Chest*) | Full text data: Table 1, Table 2 excerpts, author list | academia.edu copy, structured data-extraction pass |
> | S4 | Lehrer & Gevirtz 2014 | Abstract and mechanism sections, as close verbatim quotes | Frontiers PDF |
> | S5 | Bates et al. 2022 | Full text, verbatim | Europe PMC full-text XML |
> | S6 | Lalanza et al. 2023 | Full text | PMC HTML, plus verbatim cross-check against DNB PDF and Springer |
>
> **Not retrieved:**
> - **Lehrer et al. 2003** (*Psychosom Med* 65:796–805, the main baroreflex-gain training paper): Ovid returned 402, the Rutgers portal 404, and the Semantic Scholar API 429 (not retried). It is cited here only through S3/S4.
> - **Europe PMC search API:** 429 earlier; not retried.
> - **PMC and PubMed pages:** reCAPTCHA.
> - **Springer landing-page summary of S5:** it contradicted the verbatim text, so it was discarded.
>
> **Analysis basis:** full text for S1, S2, S5 and S6; tabulated data for S3; mechanism sections for S4.

**Scope.** One full nine-section analysis combining six sources on the physiology and practice of heart-rate-variability resonance breathing, built on the primary data. S1 is the only source that measured blood pressure; S3 reports age effects on baroreflex gain. Every number below is quoted from a source unless it is explicitly labelled as analyst-computed.

**Sources**

| # | Citation | Type | N | What it contributes |
|---|---|---|---|---|
| S1 | Vaschillo E, Lehrer P, Rishe N, Konstantinov M. *Appl Psychophysiol Biofeedback* 27(1):1–27 (2002). DOI 10.1023/A:1014587304314 | Primary experiment | 5 (all male, 24–27 y), 20 one-hour sessions each | **The only direct HR + BP transfer-function data.** Seven drive frequencies from 0.01 to 0.143 Hz; 180° and 0° HR–BP phase points; delay, inertia and rate-sensitivity estimates; two-loop model |
| S2 | Vaschillo EG, Vaschillo B, Lehrer PM. *Appl Psychophysiol Biofeedback* 31(2):129–142 (2006). DOI 10.1007/s10484-006-9009-3 | Primary experiment | 56 (24 healthy, 32 asthma), 10 weekly sessions | Individual resonance frequencies, stability, height/sex/age/weight effects, hyperventilation, and the phase rule used to steer the biofeedback. **No BP recorded** |
| S3 | Lehrer P, Vaschillo E, Lu SE, Eckberg D, Vaschillo B, Scardella A, Habib R. "Heart rate variability biofeedback: effects of age on heart rate variability, baroreflex gain, and asthma." *Chest* 129(2):278–284 (2006). PMID 16478842 | Secondary analysis of an RCT | 45 with asthma, split by age <40 / ≥40 | How much low-frequency HRV and baroreflex gain rise during biofeedback, by age; changes in asthma medication |
| S4 | Lehrer PM, Gevirtz R. *Frontiers in Psychology* 5:756 (2014). DOI 10.3389/fpsyg.2014.00756 | Mechanism review | — | Synthesis of the phase relationships, stimulus-agnostic resonance, gas-exchange, plasticity and afferent hypotheses |
| S5 | Bates ME, Price JL, Leganes-Fonteneau M, Muzumdar N, Piersol K, Frazier I, Buckman JF. *Appl Psychophysiol Biofeedback* 47(4):327–340 (2022). DOI 10.1007/s10484-022-09544-4 | Letter/tribute | — | The three-branch baroreflex; 0.1 Hz picture-cue resonance with unchanged respiration; the null result from paced sighing for a second resonance |
| S6 | Lalanza JF, Lorente S, Bullich R, García C, Losilla JM, Capdevila L. *Appl Psychophysiol Biofeedback* 48(3):275–297 (2023). DOI 10.1007/s10484-023-09582-6 | Systematic review | 143 studies | How the field actually applies and reports HRV biofeedback; the protocol taxonomy; the reporting audit |

---

## 1. Punchy Title & One-Sentence Hook

**Six breaths a minute exploits a 4.5–9-second blind spot in your blood-pressure controller, and most of the field never checked whether people actually breathed at that rate**

In five men wired with beat-to-beat blood-pressure sensors, heart rate swung 4–10 times harder than at rest once it was driven near 0.1 Hz. That was exactly where heart rate and blood pressure moved in perfect opposition. Yet two decades later, only 19 of the 88 studies in the review that recorded breathing checked whether participants were really breathing at the target rate.

---

## 2. Big-Picture Context

**Paper Type & Stakes:** a combined analysis of three primary experiments (S1, S2, S3), one mechanism review (S4), one historical letter (S5) and one systematic review of methods (S6). Together they span the causal chain from **reflex physiology → measurement protocol → dose-response by age → field-wide practice**. The stakes: whether "resonance-frequency breathing" is a real, measurable property of the cardiovascular control loop that justifies personalized protocols, or a label for a generic slow-breathing effect. And whether the published literature is precise enough to tell the difference.

**The physiology problem.** Heart rate fluctuates on a scale of seconds for two reasons. Breathing moves it directly: respiratory sinus arrhythmia (RSA) speeds the heart on the in-breath and slows it on the out-breath. And the **baroreflex**, a blood-pressure regulator, adjusts heart rate to counter pressure changes sensed by stretch receptors in the carotid arteries and aortic arch. Around 0.1 Hz (one cycle every 10 s, 6 per minute) the combined heart-rate oscillation becomes very large. Engineers had long modeled the baroreflex as a feedback loop, and De Boer et al. (1987) explained the spontaneous ~10 s blood-pressure rhythm (the Mayer wave) as that loop's resonance. Vaschillo, an electrical engineer, took a different route: he drove the loop with a controlled sinusoid and measured its frequency response directly (S1). Then he scaled the idea into a clinical protocol (S2, S3).

**The practice problem.** Protocols spread faster than the physiology was pinned down. S6 counted what 143 studies actually did between 2000 and 2021. It found three incompatible protocol families under one name:

- **Optimal RF, n = 37:** detect each person's resonance frequency first, then train at it.
- **Individual, n = 48:** a device sets the breathing rate in real time.
- **Preset-pace, n = 51:** everyone breathes at a fixed rate, usually 6 per minute.

About two-thirds of the studies are under-reported to the point where they could not be replicated. The physiology says precision matters: S2 found the effect can halve with a 0.5/min error. The practice mostly doesn't measure it.

**Prior Belief Check:** the core physiology *aligns with* mainstream cardiovascular control theory. A delayed baroreflex loop resonating near 0.1 Hz is the standard explanation of Mayer waves. What is less established is how large and how person-specific the *driven* resonance is, and every clinical claim built on it. S1 is the load-bearing experiment and it is small: five young men. The height dependence (S2) and age-attenuated response (S3) are plausible physical consequences but rest on one research lineage. S6's reporting audit is *confirmatory* of a general replication-crisis pattern, and unsurprising. The genuinely interesting tension across the set is internal: the physiology papers say the exact rate matters, while the practice review says most studies neither measure nor report it.

**Replication & Convergence Note:** S1–S5 all come from the Vaschillo/Lehrer network (S5's authors are Vaschillo's Rutgers laboratory). The existence of large 0.1 Hz heart-rate oscillations under paced breathing is widely reproduced outside that network. The specific quantitative claims are not independently confirmed. Those are the 180° HR–BP phase coinciding with the HR amplitude peak (S1, N = 5), the delay range, the height correlation (S2), and the age attenuation (S3). Independent confirmation would mean a group outside the network running S1's design on a larger, mixed-sex, mixed-age sample: drive at ≥7 frequencies, record continuous blood pressure, and test in each person whether the 180° crossing coincides with the heart-rate amplitude peak. S6 is an independent group (Barcelona) and is the only non-lineage source here, but it evaluates reporting, not physiology.

---

## 3. Necessary Background Crash-Course

### 3.1 The baroreflex: sensor, controller, actuators

**Plain version.** Stretch receptors in the carotid sinus and aortic arch report arterial pressure to the brainstem. The brainstem responds through two outputs:

- **Vagal (parasympathetic):** it slows the heart's pacemaker within roughly one beat.
- **Sympathetic:** it changes heart rate, the force of each beat and vessel diameter over several seconds.

S5 records Vaschillo's three-branch framing: an **HR baroreflex** ("HR is adjusted to stabilize BP"), a **stroke-volume baroreflex** (the strength of contraction) and a **vascular-tone (VT) baroreflex** ("vessel diameter is adjusted to stabilize BP"). S1 formalizes two of these as a "two closed loop system … one loop involves HR and BP control systems, and the other VT and BP control systems."

**Analogy:** a data-center cooling controller with a fast actuator (fan speed) and a slow one (chilled-water valve), both steered by one temperature sensor.

**Breaks when:** you ask what the sensor measures. The cooling sensor reads temperature itself. S1 states that "baroreceptors respond only to relatively fast BP changes and do not sense a constant BP values or very slow BP changes." The baroreflex sensor is closer to a **rate-of-change detector**, and §3.3 shows why that matters.

### 3.2 Respiratory sinus arrhythmia (RSA)

**Plain version.** Breathing drives heart rate directly. On the in-breath the brainstem's respiratory circuitry gates off vagal output, so heart rate rises. Breathing also changes chest pressure and venous return, which swings blood pressure within each breath; the baroreflex reacts to those swings. S2's definition: "inhaling with HR increases and exhaling with HR decreases."

**Analogy:** breathing is a periodic workload applied to a server; RSA is the immediate clock-boost response to each burst.

**Breaks when:** the "workload" and the controller aren't separate. Breathing both drives heart rate directly and creates the pressure swings the controller corrects. The analogy has no slot for an input that partly flows through the loop it is driving.

### 3.3 The baroreflex as a band-limited delayed loop — *central concept*

**Concept:** S1 measured the loop's frequency response and identified three properties, each in its own words.

1. **Delay.** "The gradual decrease in the phase transfer function W(BP–HR) as frequency increases shows that a delay between HR and BP changes occurs." A delay turns negative feedback into positive feedback at the frequency where the delay equals half the period. S1 and S2 both give the rule: resonance frequency = 1/(2 × delay).
2. **Inertia.** "The decrease in the amplitude transfer function W(BP–HR) as frequency increases shows inertia … Inertia limits the working frequency range of the baroreflex system at the upper end." Proposed contributors: "the inertia of blood mass, the effects of blood vessel plasticity, and the relatively slow process of acetylcholine hydrolization in the parasympathetic nervous system."
3. **Speed sensitivity.** "The decrease in amplitude … as frequency decreases in the very low frequency range and the positive value of the phase transfer function shows that the baroreflex system contains a speed sensitivity link … [it] limits the working frequency range … at the lower end."

Together these make a loop that works only in a band, from about 0.02 to 0.14 Hz. Within the band, the delay creates one dominant resonance. The **total** phase lag of the loop, not a pure transport time, is what hits half a cycle at resonance. That lag comes from inertia plus delay.

**Vehicle:** a CPU thermal governor with three flaws.

- **(a)** It reacts to the *rate of change* of temperature, not temperature itself, so it ignores slow drifts.
- **(b)** Its reading is stale by a few seconds.
- **(c)** The die has thermal mass, so fast clock changes barely move temperature.

Feed it bursty work. Very slow bursts: it doesn't react, because the rate is too low. Very fast bursts: nothing happens, because the thermal mass smooths them out. At one intermediate burst period, its stale correction lands exactly as the next burst begins, and the governor deepens the swing it was built to damp.

**Analogy:**

| Vehicle | Concept |
|---|---|
| Rate-of-change trigger ignores slow drift | Baroreceptor speed sensitivity (low-frequency cutoff, phase lead at 0.01 Hz) |
| Stale reading | Loop delay |
| Thermal mass smoothing fast changes | Inertia: blood mass, vessel elasticity, acetylcholine clearance (high-frequency cutoff) |
| Burst period where the correction lands in step with the next burst | Resonance near 0.1 Hz, where HR and BP sit 180° apart |
| Direct boost at each burst start | RSA |

**Breaks when:** you ask what sets the band edges in the body. The governor's flaws are fixed engineering constants. The baroreflex's "thermal mass" includes blood volume, which scales with body size (S2's height effect), and its gain drops with age (S3). A single fixed vehicle has no representation for a plant whose timing constants vary person to person and decade to decade. Those variations are exactly what the S2 and S3 data measure.

### 3.4 Hypocapnia: why beginners can't find their resonance (foundational chemistry)

S2 monitored end-tidal CO₂ and warned whenever it fell below 3.5%, roughly 25 mmHg against a normal ~38–40 mmHg. Slow but deep breathing raises minute ventilation, blows off CO₂, and drives the bicarbonate equilibrium (CO₂ + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻) to the left, producing respiratory alkalosis. S2: this "could have decreased HRV amplitude by depressing parasympathetic activity." Chemistry you know cold explains a measurement artifact in the physiology.

**Central analogy for this paper:** a rate-triggered, stale-sensor governor that hunts in one band.

---

## 4. Core Technical Explanation

### 4.1 The direct measurement (S1, 2002): driving the loop at seven frequencies

**Design.** Five healthy men aged 24–27 each completed 20 one-hour sessions. A screen drew a target sine wave with a period of "100, 47, 34, 18, 13, 9, or 7 s (i.e., frequencies … 0.010, 0.021, 0.029, 0.055, 0.077, 0.111, or 0.143 Hz)." Participants had to make their **heart rate trace follow it**, by any means they could, for 5 minutes at each frequency. Blood pressure was recorded continuously from the finger using the Penaz (Finapres-type) principle, along with respiration. Transfer functions (the amplitude ratio and phase shift between input and output at each frequency) were computed between target → HR, target → BP, HR → BP and target → respiration.

**How well the drive locked in (Table I, verbatim values):**

| Target frequency (Hz) | Period (s) | Breaths/min equivalent | % of HR spectral power at target frequency (mean ± SD) |
|---|---|---|---|
| 0.010 | 100 | 0.6 | 81.1 ± 4.3 |
| 0.021 | 47 | 1.3 | 85.4 ± 3.8 |
| 0.029 | 34 | 1.8 | 73.8 ± 5.7 |
| 0.055 | 18 | 3.3 | 71.6 ± 6.1 |
| 0.077 | 13 | 4.6 | 88.6 ± 3.8 |
| **0.111** | **9** | **6.7** | **91.5 ± 2.9** |
| 0.143 | 7 | 8.6 | 64.2 ± 3.1 |

The heart-rate spectrum was cleanest (91.5% at one frequency) at 0.111 Hz, and least clean at 0.143 Hz, just past the band edge.

**Amplitude (S1, verbatim):**

- "HR oscillation amplitudes at target frequencies were 4–10 times greater than HR oscillation amplitudes at baseline."
- "The highest amplitudes of HR oscillations occurred in the frequency band of 0.055–0.11 Hz. The lowest amplitudes of HR oscillations occurred in the frequency band of 0.02–0.055 Hz. For BP the highest amplitudes of oscillations occurred in the frequency band of 0.02–0.055 Hz."
- "Where HR oscillation amplitudes were high, BP oscillation amplitudes were low, and vice versa."

**Phase: the decisive result (S1, verbatim):**

- "For each participant, we found a frequency at which W(BP–HR) had a phase angle of 180°, that is, HR and BP were oscillating in perfectly opposite directions. This frequency was always within the low-frequency range [near 0.1 Hz]. At this frequency, the W(HR-target) amplitude was invariably at its maximum level."
- "We also found a frequency at which W(BP–HR) had a phase angle of 0° … At this frequency (which invariably was within the very low frequency range) the W(HR-target) was always at its minimum level."

**Why this is the key datum.** Two independent measurements coincide in every participant:

1. the *phase* of blood pressure relative to heart rate, and
2. the *amplitude* of heart rate relative to the drive.

At 180° the baroreflex's correction (pressure up → heart down) reinforces the drive, so heart rate peaks. At 0° heart rate and blood pressure rise together; the reflex (pressure up → heart down) now opposes the drive, so heart rate bottoms out. This is the resonance-plus-antiresonance signature a feedback loop predicts, observed directly, not inferred.

**Is it just breathing?** No. The task was heart-rate tracing, not paced breathing. S1: "Although the respiratory patterns in HR-tracing biofeedback tasks differ from the pattern at baseline, they do not usually include frequencies of the target stimulus sinusoid, particularly at very low frequencies." The abstract adds: "Changes in HR oscillations could not be completely explained by changes in breathing." Respiration amplitude at the target frequency "was always lower than resting respiration amplitude." S5 reports the same logic from the later picture-cue studies: 0.1 Hz heart-rate resonance with "respiration spectra [that] did not vary across neutral and emotional cue conditions."

**The delay, as S1 actually derives it.** "The length of the delay can be calculated from the frequency at which the input and output variables are completely out of phase (180°) … equal to one half of the oscillation period of this frequency. The specific length of the delay varied between 4.5 and 9 s in all participants." S1 attributes it to "the effects of sympathetic influence on vascular tone and vascular tissue plasticity."

> **Worked equation — resonance from delay, and the circularity to watch**
>
> $$f_{res} = \frac{1}{2D}$$
>
> **Symbol definitions:**
> $f_{res}$ : resonance frequency (Hz)
> $D$ : effective loop delay (s), defined in S1 as half the period at the 180° HR–BP crossing
>
> **Hand-checkable values (analyst-computed from S1's grid):**
> - 180° at 0.111 Hz → D = 1/(2 × 0.111) = **4.5 s** → 6.7/min
> - 180° at 0.077 Hz → D = **6.5 s** → 4.6/min
> - 180° at 0.055 Hz → D = **9.1 s** → 3.3/min
>
> S1's "4.5–9 s" is exactly the half-periods of its three highest grid frequencies below 0.143 Hz.
>
> **What this actually means — and the catch:** in S1, D is not measured independently. It is *computed from* the 180° frequency. So "resonance frequency = 1/(2 × delay)" is definitional in this dataset, not a tested prediction. The tested prediction is the *coincidence* of the 180° crossing with the heart-rate amplitude maximum, and the 0° crossing with the minimum. That held in all five participants. So the delay range can't serve as an independent check on the resonance frequencies; they are the same measurement.

**A discrepancy between S1 and S2.** S2 describes the same assessment ("a delay of approximately 5 s … in the range of 4–6.5 s for all subjects"), yet S1's own text says 4.5–9 s. With S1's coarse grid (0.055, 0.077, 0.111 Hz), the upper end of 9 s requires at least one participant whose 180° crossing sat at 0.055 Hz (3.3/min). That is well below S2's observed 4.5–6.5/min range. Either S2 summarizes a different or re-analyzed dataset, or one of the two ranges is misstated. The texts don't resolve it.

### 4.2 Analyst model: does a band-limited loop reproduce S1 and S2? (illustrative, parameters chosen by me)

A pure-delay model would predict an equal resonance at 0.3 Hz (18/min), which the body doesn't show. S1's inertia and speed-sensitivity findings fix that. I added a rate-sensitive low-frequency rolloff (corner 0.02 Hz) and an inertial high-frequency rolloff (corner 0.1 Hz). I then chose the delay so the total loop lag hits half a cycle at 0.1 Hz, and set loop gain to 0.7 there.

> **Worked example — band-limited loop, heart-rate swing relative to the drive alone**
>
> | Breaths/min | Hz | Loop gain (magnitude) | HR amplitude (×) | HR phase vs drive |
> |---|---|---|---|---|
> | 1.2 | 0.02 | 0.70 | 0.59 | −2° |
> | 3.0 | 0.05 | 0.84 | 0.70 | +35° |
> | 4.5 | 0.075 | 0.78 | 1.32 | +51° |
> | 5.5 | 0.092 | 0.73 | 2.79 | +33° |
> | **6.0** | **0.100** | **0.70** | **3.33** | **0°** |
> | 6.5 | 0.108 | 0.67 | 2.54 | −27° |
> | 7.0 | 0.117 | 0.65 | 1.82 | −37° |
> | 12 | 0.20 | 0.45 | 0.69 | −3° |
> | 18 | 0.30 | 0.32 | 1.33 | +13° |
>
> **Symbol definitions (in words):** loop gain = the fraction of a disturbance the reflex feeds back; HR amplitude = the swing with the reflex in the loop divided by the swing without it; phase > 0 means HR leads the drive.
>
> **Required pure transport delay: 4.06 s, not 5 s.** The inertial rolloff alone supplies 34° of lag at 0.1 Hz, so a shorter true delay reaches the half-cycle. The "delay" read off a 180° crossing is a **total effective lag**, a mix of travel time and inertial smoothing.
>
> **What it reproduces, against measured data:**
> - A sharp peak at 6/min falling to ~1.3–1.8× at ±1–1.5/min. S2 measured >2× power change for 0.5/min, consistent with this.
> - HR leading the drive below resonance and lagging above it: S2's steering rule, verbatim.
> - Suppression (<1×) in the 0.02–0.05 Hz band: S1's measured HR amplitude minimum in 0.02–0.055 Hz.
> - The 0.3 Hz echo is now 1.33× instead of 3.33×, i.e., no second resonance at normal breathing rates.
>
> **What this actually means:** once you add the two S1-measured band limits, a single loop explains the peak, the phase rule and the low-frequency dip. The corners are my choices, not fitted to data. The model shows the pieces are *sufficient*, not that these are the true values.

### 4.3 Individual resonance in 56 people (S2, 2006)

**Design.** 56 adults aged 18–65: 24 healthy (16 female) and 32 with asthma (21 female). Each had 10 weekly sessions. Recordings: ECG (512 Hz), respiration strain gauge, end-tidal CO₂. **No blood pressure.**

- **Session 1:** 2 minutes at each of 6.5, 6, 5.5, 5 and 4.5 breaths/min. Resonance frequency = "the respiratory frequency that produced the highest respiratory component in the RRI spectra."
- **Sessions 2–3:** pacer adjusted ±0.5/min using the phase rule.
- **Sessions 4–10:** pacer off after 5 minutes; participants breathed at whatever rate maximized the heart-rate swing on screen with 0° phase to breathing.

**Data:**

| Measure | Value |
|---|---|
| Mean resonance frequency, all 56 | **5.56 ± 0.41 breaths/min (0.0926 ± 0.007 Hz)**; range 4.5–6.5 |
| Correctly identified in session 1 | 20/56 (35.7%) |
| End-tidal CO₂ | "frequently fell below 3.5%" in sessions 1–3; hyperventilation "disappeared by the fourth session" |
| Stability over 10 sessions | "almost never varied by more than 0.5 breaths/min"; F(9,486) = 1.32, n.s. |
| Sensitivity | respiratory-component power "could change by a factor of more than 2, for respiratory rate changes of only 0.5 times/min" |
| Height | r = −0.55, p < 0.0001 (taller → lower frequency) |
| Sex | F 5.66/min (0.0943 Hz) vs M 5.21/min (0.0868 Hz), t = 4.07, p < 0.0001; the difference vanishes after height adjustment |
| Weight | r = 0.02, n.s. |
| Age | r = 0.01, n.s.; ≤40 y: 5.54 vs >40 y: 5.52/min |
| Asthma vs healthy | 5.55 vs 5.50/min, t = 0.35, p = 0.73 |

**Height–resonance correlation by session (S2, Table IV):**

| Session | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| r | −0.26 | −0.24 | −0.30 | −0.61 | −0.63 | −0.57 | −0.50 | −0.61 | −0.48 | −0.59 |
| p | n.s. | n.s. | n.s. | <.0005 | <.0001 | <.001 | <.005 | <.0005 | <.006 | <.0005 |

**Reading the table:** the correlation jumps from about −0.27 to about −0.57 between sessions 3 and 4. That is exactly when hyperventilation disappears and participants start self-selecting their rate. The body-size signal only appears once measurement noise from overbreathing is gone.

**Phase rule (S2, verbatim):** "HR oscillation precedes respiration (a positive phase) if the individual breathes more slowly than resonant frequency, and HR oscillation lags behind respiration (a negative phase) if the individual breathes more frequently."

**Implied loop lag by group (analyst-computed, D = 1/(2f)):** all 56: 5.40 s; women: 5.30 s; men: 5.76 s. S2's explanation: "greater volume of vasculature and mass of circulated blood in taller individuals … inertia in the CVS is greater, so the delay … is longer." This fits S1's attribution of the delay to inertia and vascular plasticity.

### 4.4 Dose-response by age (S3, *Chest* 2006)

**Design.** 45 adults with asthma, randomized to a full protocol (HRV biofeedback + pursed-lips abdominal breathing) or HRV biofeedback alone, and analyzed by age (<40 vs ≥40). Outcomes: low-frequency (LF) HRV and baroreflex gain ("α LF"), measured during biofeedback versus rest, plus asthma controller medication over 10 sessions.

**Baseline (S3 Table 1, verbatim):**

| | Full protocol <40 (n = 8) | Full protocol ≥40 (n = 11) | Biofeedback only <40 (n = 10) | Biofeedback only ≥40 (n = 7) |
|---|---|---|---|---|
| Age (y) | 27.55 ± 6.30 | 47.50 ± 6.55 | 28.07 ± 5.62 | 50.44 ± 3.23 |
| log LF + HF HRV | 6.95 ± 1.12 | 6.33 ± 0.81 | 7.80 ± 1.56 | 6.79 ± 0.77 |
| log LF HRV | 5.64 ± 0.84 | 5.60 ± 0.87 | 6.75 ± 1.72 | 5.93 ± 1.32 |
| log baroreflex gain | 1.86 ± 0.40 | 1.65 ± 0.79 | 2.35 ± 0.45 | 1.56 ± 0.61 |

**Acute effect of biofeedback vs rest (S3 Table 2 excerpts, verbatim log changes; fold-change analyst-computed):**

| Group | Δ log LF HRV | ≈ fold | Δ log baroreflex gain | ≈ fold |
|---|---|---|---|---|
| Full protocol <40 | +3.114 (SE 0.375), p < 0.0001 | ×22.5 | +0.604 (SE 0.121), p < 0.0001 | ×1.83 |
| Full protocol ≥40 | +2.761 (SE 0.319), p < 0.0001 | ×15.8 | +0.219 (SE 0.101), p = 0.030 | ×1.24 |
| Biofeedback only <40 | +3.489 (SE 0.332), p < 0.0001 | ×32.8 | +0.590 (SE 0.107), p < 0.0001 | ×1.80 |
| Biofeedback only ≥40 | +2.220 (SE 0.397), p < 0.0001 | ×9.2 | +0.371 (SE 0.126), p = 0.003 | ×1.45 |

Age difference in the LF increase: 0.879 (SE 0.376, t = 2.340, p = 0.020), i.e., the younger group's fold-increase was ~2.4× larger. Age difference in the baroreflex-gain increase for biofeedback only: 0.218 (SE 0.165, p = 0.186, n.s.). Asthma medication fell in every group over 10 sessions (−1.6 to −3.1 steps on a 13-step scale, all p ≤ 0.008), "from … moderate asthma to … mild persistent asthma." The age difference was not significant: "Decreases in need for controller medication were independent of age."

> **Worked check — which logarithm? (analyst reasoning)**
>
> The paper's log base isn't stated in what I retrieved. Natural log gives plausible physiology; base 10 does not.
> - Baseline log baroreflex gain of 1.86 → e^1.86 = **6.4 ms/mmHg**, inside the normal resting range of a few to ~20 ms/mmHg. Base 10 would give 72 ms/mmHg, implausible.
> - Baseline log LF of 5.64 → e^5.64 ≈ **280 ms²**, a typical resting LF power.
>
> So the fold-changes above use e^Δ.
>
> **What this actually means:** resonance breathing multiplied LF heart-rate power roughly 9–33-fold during the session, and roughly doubled the moment-to-moment baroreflex gain in under-40s. Over-40s got a smaller boost, about 1.2–1.5×.

**Cross-paper synthesis (S2 × S3):** age does **not** move the resonance *frequency* (S2: 5.54 vs 5.52/min), but it **does** shrink the resonance *amplitude* and the baroreflex-gain boost (S3). In the loop picture, the timing constants survive aging while the loop gain falls. Arterial stiffening and reduced vagal responsiveness are the textbook reasons, and S2 invokes both for the frequency puzzle. A lower loop gain means a lower, broader peak at the same place. Using the §4.2 model: dropping gain from 0.7 to 0.5 lowers the peak from 3.33× to 2.0× without moving it.

### 4.5 Mechanism claims beyond the loop (S4) and the missing second resonance (S5)

**S4's four moves:**

1. The 0° HR–respiration and 180° HR–BP phases at ~0.1 Hz, plus baroreflex sensitivity peaking there ("a specific frequency where heart rate changes per unit change in blood pressure were greatest…approximately 0.1 Hz"). This is S1's result restated.
2. Resonance is stimulus-agnostic: "rhythmic muscle tension" and "rhythmical presentation of emotion-inducing pictures" produce it too.
3. Gas exchange is "most efficient when heart rate starts increasing at the beginning of inhalation … a 0° phase relationship" (citing Hayano et al.). This is the proposed asthma rationale, and consistent with S3's medication reductions.
4. Baroreflex gain rises during biofeedback and at rest after training ("neuroplasticity in the baroreflex"). The regular baroreceptor output travels via vagal afferents to regions "involved in affect regulation and mood." S3 supplies the acute half with numbers (×1.2–1.8). The resting-gain increase is from Lehrer et al. 2003, which was not retrieved.

**S5 on the vascular branch.** S1's data already showed a *BP* amplitude maximum at 0.02–0.055 Hz. S1 hypothesized this "results from the VT baroreflex … which was not studied in this experiment." Vaschillo later predicted a VT resonance at ~0.03 Hz ("a hypothetical 15 s delay (or 30 s period)"). Because no one can breathe that slowly, he used paced sighing at 0.02, 0.03 and 0.06 Hz. Result: "strong and immediate responses that rippled across the cardiovascular system with no signs of habituation" (including skin conductance) "but evidence of resonance was not readily observable. It remains unknown whether there is a second resonance frequency."

**Cross-paper synthesis (S1 × S5):** S1's BP peak in the very-low-frequency band was measured while *heart rate* was the driven variable. S5's null came from sighing, an impulsive, mostly respiratory-mechanical drive. These are different inputs to different branches. The null doesn't contradict S1's BP peak. It shows the VT branch is either heavily damped or poorly driven by brief sighs.

### 4.6 What the field actually does with this (S6, 2023)

S6's audit measures the practice against the physiology in S1–S3:

| Physiology says (S1–S3) | Practice in 143 studies (S6) |
|---|---|
| Resonance frequency varies 4.5–6.5/min between people (S2) | 51 of 145 interventions used a fixed preset pace; 37 detected an individual resonance frequency |
| 0.5/min error can halve the effect (S2) | Only 20 of 85 Optimal RF + Individual studies (24%) reported the sample's mean resonance frequency |
| Beginners overbreathe; resonance frequency can't be measured in session 1 (S2) | Most studies detected resonance frequency once, at baseline; only 6 rechecked it every session |
| Achieved breathing rate is the manipulation (S1, S2) | Only 19 of 88 studies (22%) monitored achieved breathing rate; one that did saw ~8.5 → 6.3/min over training |
| Timing within the breath shapes the effect (S4, 0° phase) | Only 27 studies (~19%) reported the inhale:exhale ratio; two comparisons disagree (Lin 2014 equal vs van Diest 2014 longer exhale) |
| Age shrinks the response (S3) | ~60% of samples were aged 18–39; <10% were over 65 |
| Signal quality matters for beat timing | ECG beats PPG during paced breathing (Jan et al. 2019, cited in S6) |

**S2 through S6's lens (analyst reading of what I retrieved):** S2 would score well on S6's breathing-protocol items. It gives the detection procedure, per-session adjustment, the mean resonance frequency (it is one of the ~20 that did), and breathing monitoring by strain gauge plus capnometry. I did not see inhale:exhale ratio, body position or room conditions in the retrieved text. So even the reference physiology paper may miss parts of S6's checklist.

### Assumption Audit

> **Watch:** Reader likely assumes the ~5 s "delay" is independently measured and then used to predict 6/min. **S1 actually** computes the delay *from* the 180° frequency (half its period). The formula is definitional there. The real test is that the 180° point coincides with the heart-rate amplitude maximum, and the 0° point with the minimum, in all five participants.

> **Watch:** Reader likely assumes the resonance lives in the breathing system. **S1 actually** drove heart rate by visual tracking, with respiration mostly *not* at the target frequency, and still found the resonance. S5 reports it with picture cues while respiration spectra didn't change. It is a cardiovascular-loop property; breathing is the most convenient drive.

> **Watch:** Reader likely assumes age-invariant resonance frequency (S2) means an age-invariant effect. **S3 actually** shows over-40s get a markedly smaller LF-power boost (×9–16 vs ×22–33; age difference p = 0.020) and a smaller baroreflex-gain boost (×1.2–1.5 vs ×1.8). Timing survives aging; gain doesn't.

> **Watch:** Reader likely assumes the key HR–BP phase numbers come from the 56-person study. **Only S1 (N = 5 young men) measured blood pressure.** S2's "4–6.5 s for all subjects" sentence also conflicts with S1's own "4.5 and 9 s."

---

## 5. What's Genuinely New or Clever

1. **Frequency-response testing of a human reflex (S1).** Vaschillo applied a standard engineering move to physiology: inject a clean sine at a grid of frequencies and read amplitude and phase at each. The result: a resonance (180°, maximum) and an antiresonance (0°, minimum) located directly, plus three identifiable loop properties (delay, inertia, rate sensitivity) read from the curve shapes. New to the field in 2002. The spontaneous Mayer-wave literature could only infer resonance.
2. **A phase-sign steering rule (S2).** Whether heart rate leads or lags breathing tells the person which way their resonance lies. That turns a sweep-and-compare search into a feedback loop the person can close in real time. It is a nontrivial, confirmed prediction of the loop model.
3. **Body size and age as loop parameters (S2 × S3).** Height moves the *timing* (frequency, r = −0.55); age moves the *gain* (amplitude and baroreflex boost) but not the timing. Together they decompose individual differences into two physically distinct knobs. That is a synthesis across the set; neither paper states it alone.
4. **Separating the loop from breathing (S1 + S5).** Heart-rate tracing and picture cues at 0.1 Hz produce the resonance without the breathing drive. It is the control a skeptic of the "just RSA" account would demand.
5. **A physiology-to-practice audit (S6 as the counterweight).** Lining up S6's numbers against S1–S3 shows the field mostly doesn't measure the variables the physiology says control the effect.

**Predictive Content Check**

1. **Falsifiable handle — strong on physiology, with one prediction that failed:**
   - **Phase–amplitude coincidence (S1):** the 180° HR–BP crossing must sit at the heart-rate maximum and 0° at the minimum. It was tested in five of five participants, and could have failed. This is the load-bearing prediction; "resonance frequency = 1/(2D)" is not, since D is derived from the crossing.
   - **Lead/lag sign rule (S2):** HR must lead breathing below resonance and lag above. Confirmed and used operationally.
   - **Body size → frequency, age → gain (S2, S3):** height confirmed (r = −0.55); age leaves frequency unchanged (r = 0.01) but cuts gain (p = 0.020 for LF). This is a split prediction, partly unexplained.
   - **Stimulus-agnostic (S1, S4, S5):** confirmed with visual tracking, muscle tension and picture cues.
   - **Second resonance at ~0.03 Hz (S5):** **not found** with paced sighing. A partial disconfirmation of the model's generality.
   - **S6:** audits and prescribes rather than predicts. Its implied testable claim, that protocol type and breathing compliance moderate effect size, remains unrun.
2. **Formalism load:** not triggered. The transfer-function analysis in S1 generates every phase and amplitude claim; no decorative math.

---

## 6. Limitations & Open Questions

1. **The load-bearing physiology rests on five young men.** S1 is the only source that measured blood pressure: N = 5, all male, aged 24–27. S1 itself calls for "confirming our findings on a larger sample." **(A) Consensus** — stated by the authors and plain from the design. **(S1, Discussion)**

2. **The delay range is internally inconsistent across S1 and S2.** S1 says 4.5–9 s; S2, describing the same assessment, says 4–6.5 s "for all subjects." S1's 9 s end implies a 180° crossing at 0.055 Hz (3.3/min), outside S2's observed 4.5–6.5/min. **(C) Speculative** — the discrepancy is a fact; which figure is right, or whether S2 refers to different data, is my inference. **(analyst inference)**

3. **"Resonance = 1/(2 × delay)" is circular in these data.** The delay is computed from the 180° frequency; no transport delay was measured independently (e.g., pulse transit time, or the time to the vagal and sympathetic response). The §4.2 model shows that inertia alone contributes ~34° of the half-cycle, so "delay" is an effective lag, not a physical travel time. **(C) Speculative** — the circularity follows from S1's stated method; the inertia-share estimate is from my illustrative model. **(analyst inference)**

4. **How much of the breathing-driven peak is RSA growing at slow rates vs. baroreflex resonance is not quantified.** S1 and S5 show the loop resonates without the breathing drive. But in breathing-driven HRVB (S2, S3), the two contributions add, and no source splits them. The broader literature (e.g., Hirsch & Bishop 1981) shows RSA alone grows as breathing slows. **(B) Contested** — baroreflex involvement is well supported, but its fractional share in breathing protocols is debated. **(broader literature)**

5. **Where the loop lag physically lives is unresolved.** S1 attributes the delay to "sympathetic influence on vascular tone and vascular tissue plasticity." S5 calls the 0.1 Hz resonance specific to the HR branch. The vagal limb acts within about a beat, and De Boer's model places the Mayer-wave lag in the sympathetic vascular limb. S1's own inertia list (blood mass, vessel plasticity, acetylcholine clearance) mixes mechanical and neural sources. **(B) Contested** — an open question in cardiovascular modelling. **(broader literature + S1)**

6. **The height mechanism is inferred, not measured.** Blood volume was not measured in S2; weight and age don't fit a blood-mass story; arterial path length is an alternative with the same sign. **(C) Speculative** — the path-length alternative is my inference. **(analyst inference)**

7. **S3's effects are within-session and from one asthma sample.** The large LF and baroreflex-gain increases are *during* biofeedback versus rest, largely the resonance itself. They don't by themselves show lasting plasticity; that claim rests on Lehrer et al. 2003 (not retrieved). The log base is my inference from plausibility. Group sizes are 7–11. **(B) Contested** — acute amplification is uncontroversial, while durable baroreflex remodeling is debated. **(S3 + broader literature)**

8. **Resonance-frequency stability is contested.** S2 reports stability within 0.5/min over 10 sessions, but its 0.5/min grid is about the width of the peak. S6 cites Lin et al. 2012 finding a 6 → 5/min shift across sessions. **(B) Contested** — the primary studies disagree. **(S6, broader literature)**

9. **The second (vascular) resonance is predicted but not found.** Paced sighing produced strong responses without a resonance signature. **(A) Consensus** — reported as a null by the proposing lab. **(S5)**

10. **Clinical necessity of exact resonance frequency is unproven.** S2's authors: "it has not yet been proven whether precise measurement of resonant frequency is essential." S6 found no efficacy comparison across the three protocol families. S3's medication reductions came from individualized protocols, with no fixed-pace comparison arm. **(A) Consensus** — stated by S2 and still open per S6. **(S2, S6)**

11. **Downstream mechanisms (S4) are hypotheses.** Vagal-afferent effects on frontal and limbic areas, and anti-inflammatory action, rest on small studies largely from the same network. **(B) Contested** — the vagal anti-inflammatory pathway is established physiology; its engagement by HRVB is debated. **(S4 + broader literature)**

12. **Single lineage for the physiology; reporting gaps even in the core papers.** S1–S5 share the Vaschillo/Lehrer network. Judged against S6's checklist, even S2's retrieved text doesn't show the inhale:exhale ratio or body position. **(A) Consensus** — authorship is a matter of record; the checklist gaps are from what I retrieved. **(S6 + analyst inference)**

13. **S6's screening numbers don't reconcile.** 262 − 19 + 20 = 263, not the stated 282 full-text assessments. **(C) Speculative** — the arithmetic is fact; its significance (typo vs. accounting gap) is my judgment. **(analyst inference)**

---

## 7. Detailed Summary & Explanation

**Summary.** Heart rate and blood pressure are tied together by a feedback loop, the baroreflex. When pressure rises the brainstem slows the heart; when it falls the heart speeds up. In 2002, Vaschillo's group tested that loop the way an engineer tests an amplifier. Five young men learned to make their heart rate follow a sine wave on a screen at seven different speeds, from one cycle every 100 seconds to one every 7 seconds, while blood pressure was recorded beat by beat.

The results were unambiguous for all five:

- Near one cycle every 9–13 seconds, heart rate swung 4–10 times harder than at rest.
- At exactly the speed where heart rate peaked, blood pressure was moving in perfect opposition to it. The reflex's correction was landing in step with the push instead of against it.
- At the very slow speed where heart rate and blood pressure moved together, the heart-rate swing was at its smallest.
- The loop only works in a band. Very slow changes don't register, because the sensors respond to rates of change. Very fast changes are smoothed out by the inertia of blood and vessels.
- Breathing mostly wasn't at the target frequency, so this is a property of the heart-and-vessel loop, not the lungs.

Scaled up to 56 adults (2006), breathing drove the same resonance. Each person's best rate fell between 4.5 and 6.5 breaths per minute, averaging 5.6. Being off by half a breath per minute could halve the effect. Taller people resonated slower (r = −0.55), which explained the difference between men and women entirely. Age made no difference to the *rate*. Beginners overbreathed and blew off CO₂, which suppressed the oscillation, so the body-size signal only appeared from the fourth session on.

A 45-person asthma study (2006) showed what age *does* change: during biofeedback, low-frequency heart-rate power rose about 22–33-fold in under-40s but only 9–16-fold in over-40s, and baroreflex gain rose about 1.8-fold versus 1.2–1.5-fold. Asthma medication needs fell in every group regardless of age.

The later review (2014) and tribute letter (2022) add that the resonance also appears with rhythmic muscle tension or rhythmically shown pictures. They add the hypotheses that it helps via better gas exchange, baroreflex plasticity and vagal signalling to emotion-regulating brain areas. They also report that a predicted second, slower resonance in vessel tone was not found.

The 2023 systematic review shows how far practice lags this physiology. Across 143 studies, a third used one fixed pace for everyone. Only about a fifth checked the breathing rate actually achieved, fewer reported the inhale:exhale timing, and only 6 rechecked the resonance frequency each session.

**Explanation.** I organized the synthesis around **one loop with two kinds of individual difference**: timing, set by body size, and gain, reduced by age. That framing is what lets the six sources speak to each other. S1 establishes the loop and its band limits with direct blood-pressure data. S2 maps the timing across people. S3 maps the gain across age. S4 and S5 extend and test the model. S6 shows whether practice respects it.

I made two interpretive choices that go beyond any single paper, and flagged both:

- **Circularity.** In S1's method the 1/(2 × delay) formula is circular. The genuine test is the phase–amplitude coincidence.
- **Timing vs. gain.** The S2 × S3 split (age moves gain, not timing) is my synthesis, not a stated result of either paper.

The band-limited model in §4.2 is explicitly illustrative. Its corners are my choices. It demonstrates that S1's three measured loop properties are sufficient to reproduce S1's and S2's observations, including why there is no second resonance at normal breathing rates.

**Structure adaptation note:** six sources synthesized per the multi-paper pattern: one Big-Picture Context, one Background, and a Core Technical Explanation ordered by the causal chain (direct measurement → model → individuals → age → mechanisms → practice) rather than by paper.

**Where I'm least confident in this analysis:**

- **S1's per-frequency amplitudes and phases.** S1's quantitative transfer-function values exist only as figures (Figs. 3–7), which I could not read as numbers. The amplitude claims here are S1's own verbal summaries ("4–10 times," the frequency bands), not values I extracted.
- **S3's logarithm base.** Natural log is inferred from physiological plausibility, not stated in the retrieved text. If wrong, the fold-changes would be misstated, though the direction and significance would not change.
- **The S1–S2 delay discrepancy** (4.5–9 s vs 4–6.5 s) I can flag but not resolve.

---

## 8. Three Crystallized Takeaways

1. **Your blood-pressure reflex is a delayed feedback loop that works only in a band, and near one cycle every 10 seconds its correction lands on the beat instead of against it.** In the direct measurement, heart rate swung 4–10× harder than at rest exactly where heart rate and blood pressure moved in perfect opposition.
2. **Body size sets the rhythm; age sets the volume.** Taller people resonate slower (4.5–6.5 breaths/min across 56 people), but age doesn't change the rate. It shrinks the boost: over-40s got roughly 30–70% of the heart-rate amplification of under-40s.
3. **The physiology says precision matters; the literature mostly doesn't measure it.** Half a breath per minute off can halve the effect, yet only about one study in five checked what rate people actually breathed at.

---

## 9. Shorter Summary

Why does breathing near six breaths per minute make heart rate swing so much? These six papers answer it with direct measurements. Heart rate and blood pressure form a feedback loop: when pressure rises the brain slows the heart, and when it falls the heart speeds up. That loop responds several seconds late, and it only reacts in a middle band of speeds. Very slow drifts go unnoticed, and very fast changes are smoothed out by the inertia of blood and vessels.

In a 2002 experiment, five men made their heart rate follow a wave on a screen at seven different speeds while blood pressure was recorded beat by beat. Near one cycle every ten seconds, heart rate swung four to ten times harder than at rest. At that same speed, blood pressure moved exactly opposite to heart rate, so the reflex's correction reinforced the swing instead of damping it. Breathing mostly wasn't at that speed, so this is a property of the heart-and-vessel loop, not the lungs.

In 56 adults, each person's best breathing rate fell between 4.5 and 6.5 breaths per minute. Taller people resonated slower, and half a breath per minute off could halve the effect. Beginners overbreathed at first, which suppressed the oscillation. Age didn't change the rate, but a 45-person asthma study found it shrank the payoff: people under 40 gained far more heart-rate variability and reflex sensitivity than people over 40. Asthma medication needs dropped regardless of age.

Reviews propose benefits through better oxygen uptake, a strengthened reflex and calming signals to the brain; these remain hypotheses. A predicted second, slower resonance in blood-vessel tone wasn't found.

A 2023 review of 143 studies found practice lagging behind: a third used one fixed pace for everyone, and only about one in five checked the breathing rate people actually achieved. The core physiology rests on a small sample and one research network, and needs independent replication.

---

## Appendix — Deep-Dive Discussion Log (2026-09-27)

Follow-up questions after the analysis, recorded in the order they were asked. Each unpacks existing content rather than correcting it. The parts about the reader's own data and device are at the end.

### A. The three loop properties S1 identifies, and where each shows up

**What W(BP–HR) is.** Heart rate is driven as a sine wave at one frequency at a time; blood pressure answers with a sine wave at the same frequency. Each frequency gives two numbers:

- **Amplitude ratio:** mmHg of pressure swing per bpm of heart-rate swing.
- **Phase:** how far the pressure peak sits from the heart-rate peak, in degrees of one cycle.

To convert degrees to seconds: time shift = (phase ÷ 360°) × period. −180° at a 10 s period means the pressure peak comes 5 s after the heart-rate peak.

**1. Delay: phase keeps falling while amplitude stays the same.** A fixed lag of D seconds adds −360° × f × D of phase, so the same lag counts for more degrees as frequency rises. With D = 4 s: −14° at 0.01 Hz, −72° at 0.05 Hz, −144° at 0.1 Hz, −180° at 0.125 Hz. The baroreflex's built-in inversion (pressure up → heart down) is worth 180°. Add another 180° of lag and the correction lands in step with the push.

**2. Inertia: the upper limit.** The arterial tree is an elastic reservoir holding a large mass of blood. On top of that, acetylcholine clearance smears out fast vagal commands. Brief heart-rate changes therefore barely move pressure. Signature: amplitude falls as frequency rises, and the response lags by up to 90°. Analogy: the Linux load average, an exponentially weighted moving average that ignores a 5 s spike and always trails the true load. With the smoothing corner at 0.1 Hz, the fraction of the swing that gets through and the added lag are:

| Frequency | Fraction passed | Added lag |
|---|---|---|
| 0.05 Hz | 0.89 | −27° |
| 0.1 Hz | 0.71 | −45° |
| 0.2 Hz | 0.45 | −63° |
| 0.3 Hz | 0.32 | −72° |

This is why there is no second resonance at normal breathing rates. It also matches S1's Table I, where the drive held worst at 0.143 Hz (64.2% of heart-rate power at the target frequency).

**3. Speed sensitivity: the lower limit.** Baroreceptors fire mainly on the *rate* of stretch and adapt to steady pressure. For a ±5 mmHg swing, the peak rate of change is:

| Period | Peak rate of change |
|---|---|
| 100 s | 0.31 mmHg/s |
| 18 s | 1.75 mmHg/s |
| 10 s | 3.14 mmHg/s |

So amplitude falls as frequency falls. A sine wave's rate of change peaks a quarter cycle before its value does, which gives the positive phase S1 saw near 0.01 Hz. Analogy: a disk alert keyed to percent-per-minute, which ignores slow creep and fires before the disk is full.

**Combined (illustrative model: rate-sensing corner 0.02 Hz, smoothing corner 0.1 Hz, pure delay 4.06 s):**

| Frequency | Rate lead | Smoothing lag | Delay lag | Total phase | Amplitude passed |
|---|---|---|---|---|---|
| 0.01 Hz | +63° | −6° | −15° | +43° | 0.44 |
| 0.021 Hz | +44° | −12° | −31° | **≈ 0°** | 0.71 |
| 0.055 Hz | +20° | −29° | −81° | −89° | 0.82 |
| 0.077 Hz | +15° | −38° | −113° | −136° | 0.77 |
| 0.1 Hz | +11° | −45° | −146° | **−180°** | 0.69 |
| 0.143 Hz | +8° | −55° | −209° | −256° | 0.57 |

The curve crosses 0° near 0.02 Hz, where S1 found the heart-rate amplitude at its minimum, and −180° at 0.1 Hz, where it found the maximum. So the three properties are the pieces that shape one phase curve, not three separate facts.

**Two flags on the quoted wording:**

- **"Delay equals half the period" really means *total* lag.** In this model the pure transport delay is 4.06 s, not the 5 s half-period, because smoothing supplies part of the lag. The corner frequencies are my choices, so the exact split is uncertain.
- **Speed sensitivity appears in the HR → BP measurement only indirectly.** The rate-sensing receptors sit in the return path (BP → brain). They can shape W(BP–HR) through S1's second, vascular-tone loop, and local autoregulation also cancels slow pressure drifts. S1 did not measure vascular tone, so it cannot separate those contributions.

### B. The same mechanism without degrees

**The shower with a long pipe.** You react correctly but late, so you swing between too hot and too cold. The swing's period is twice the pipe delay. The mapping:

| Shower | Body |
|---|---|
| Knob | Heart rate |
| Water temperature | Blood pressure |
| You | The brainstem reflex |
| Pipe | The few seconds for a heart-rate change to become a pressure change |
| Someone pushing the knob on a schedule | Breathing |

**Second by second, breathing once every 10 s, with pressure lagging heart rate by 5 s:**

| Time | Breath | Heart rate | Pressure | Reflex | Effect |
|---|---|---|---|---|---|
| 0 s | in-breath starts | low | high | "slow down" | deepens the low |
| 2.5 s | mid in-breath | rising | falling | switching to "speed up" | pushes the rise |
| 5 s | in-breath ends | high | low | "speed up" | deepens the high |
| 7.5 s | mid out-breath | falling | rising | switching to "slow down" | pushes the fall |

**Breathing once every 5 s (a normal rate), the lag equals a whole breath.** Pressure peaks together with heart rate, so the reflex trims every peak and fills every dip.

**The rule:** a reflex lag of half a breath helps; a lag of a whole breath fights. A 5 s lag means a 10 s breath, which is 6 per minute.

**Where the band edges come from:** the tank smooths out fast wiggles (inertia), and the change-detecting sensors miss slow drifts (speed sensitivity). One rate inside the band makes the lag line up.

**Where the analogy breaks:** the body's "wait" is part travel time and part tank-filling, blended together. A real shower has only a pipe.

### C. A consumer device: the Ohm Resonance Lamp (Ohm Health)

- **Hardware:** a lamp plus a handheld sensing stone containing an optical pulse sensor (PPG) and a 9-axis accelerometer/magnetometer.
- **Stated measurements:** "heart rate and breathing patterns." Pacing is by light, sound and vibration, with cadence "adjusted" in real time.
- **Stated logistics:** sessions of 3–5 min rising to 10–15; $350 list ($249 introductory); shipping mid-Oct to Nov 2026.
- **Not disclosed:** the pace-selection algorithm, the definition of its score, beat-interval export, and any validation study.

How it maps onto the analysis:

1. **It is an "Individual"-type protocol** in S6's taxonomy, with a proprietary algorithm (limitation 12's concern).
2. **It can see the S2 phase-rule signal**, since it has both pulse timing and breathing timing.
3. **It cannot measure blood pressure.** Marketing that mentions blood pressure describes the physiology, not a measurement.
4. **Palm pulse timing includes pulse-arrival delay (analyst inference).** That delay varies with blood pressure on each breath, adding a small error in phase with the trained rhythm. This is one reason S6 notes ECG outperforms PPG during paced breathing.

### D. Reader's own resonance data (chest-strap ECG, Polar + Elite HRV)

- **Resonance:** 8.7 s per breath (6.9/min, 0.115 Hz), with 3.2 s in and 5.5 s out. Found by a rate sweep and confirmed with the chest strap. Used off and on for about 3 years.
- **Implied effective loop lag:** about 4.35 s. That is faster than every one of S2's 56 participants (4.5–6.5/min), but within S1's heart-rate peak band, which reached 0.111 Hz (6.7/min).
- **Peak sharpness:** ±0.5 s (8.2 s or 9.2 s per breath) gave a definite drop in the swing. In a pure-delay model at a 4.35 s lag, power relative to peak at 8.2 s and 9.2 s is 93/95% for gain 0.5, 78/82% for 0.7, 58/63% for 0.8, and 23/28% for 0.9. A clearly noticeable drop implies loop gain of roughly ≥ 0.8, consistent with S2's ">2× per 0.5/min." This is illustrative, not a fit.
- **Subjective timeline:** clearly parasympathetic by ~10 min, sleepy by 15–20 min. That fits a strong parasympathetic shift. It is worth keeping separate from hypocapnia (tingling, lightheadedness), and the reader reports avoiding overbreathing.
- **Inhale/exhale caveat:** the resonance was found at a 37:63 inhale/exhale split. The ratio literature is split (equal ratio vs longer exhale), so re-test if the ratio changes.

### E. Planned device-validation test: Ohm vs Polar

1. Record simultaneously: Polar chest strap into Elite HRV, and the Ohm stone in the palm, for 10 min.
2. **Session A (lamp-paced):** note where the lamp's pace settles (≈ 8.7 s, or pulled toward 10 s?) and the size of the heart-rate swing.
3. **Session B:** pace manually at 8.7 s.
4. Compare:
   - swing amplitude on each device;
   - beat-by-beat timing, if Ohm exports intervals (a few ms of disagreement is good, tens of ms is poor; check whether errors cluster at one point in the breath cycle);
   - phase (heart rate should peak at the end of the in-breath).
5. **Verdict:** if Ohm agrees with Polar and settles near 8.7 s, use the lamp alone. Otherwise set the pace manually and keep the Polar as the reference.

*Practical companion guide (the reader's own numbers, practice rules, lamp checklist, session log):* `my-resonance-breathing-guide.md` in the Physics-Wiki root and on Google Drive.
