---
source: claude_export
conversation_uuid: 3e59a7b3-29a8-44ec-947b-72ed44f90c0f
title: "Dynamical formation of gravastars from dust collapse"
created_at: 2026-06-13T03:12:08.157491Z
updated_at: 2026-06-13T03:15:35.480118Z
tier: A
score: 31
n_messages: 2
---

# Dynamical formation of gravastars from dust collapse

## Human

Analyze this paper

arXiv:2509.15302
Formation of gravastars
Daniel Jampolski, Luciano Rezzolla
Regular black holes and horizonless black hole mimickers offer mathematically consistent alternatives to address the challenges posed by standard black holes. However, the formation mechanism of these alternative objects is still largely unclear and constitutes a significant open problem since understanding their dynamical formation represents a first step to assess their existence. We here investigate, for the first time and without invoking higher-curvature corrections, the dynamical formation of a well-known horizonless black hole mimicker, namely, a gravastar. More specifically, starting from the collapse of a uniform dust sphere as in the case of the Oppenheimer-Snyder collapse, we demonstrate that, under fine-tuned conditions, a gravastar can form from the nucleation and expansion of a de Sitter region with initial zero size at the center of the collapsing sphere. Furthermore, the de Sitter expansion naturally slows down near the Schwarzschild radius, where it meets the collapsing dust surface and gives rise to a static equilibrium. Interestingly, we also find a maximum initial compactness of the collapsing star of , above which the collapse to a black hole is inevitable.
(or arXiv:2509.15302v2 [gr-qc] for this version)

https://doi.org/10.48550/arXiv.2509.15302
Journal reference:	Phys. Rev. D 113, L121502 (2026)
Related DOI:
https://doi.org/10.1103/c6lw-nx7k

## Assistant

v3.6.1

## 1. Punchy Title & One-Sentence Hook

**A Baby Universe Inside a Dying Star: The First Dynamical Birth of a Gravastar**

A collapsing star doesn't have to become a black hole — under fine-tuned but physically plausible conditions, a tiny patch of dark-energy-driven spacetime can nucleate at the star's center, expand outward, and slam on the brakes just at the Schwarzschild radius, leaving behind a stable horizonless object that looks almost exactly like a black hole from the outside.

---

## 2. Big-Picture Context

Black holes are the textbook endpoint of gravitational collapse, but they carry two deeply uncomfortable features: a singularity where general relativity breaks down and loses predictive power, and an event horizon whose semiclassical quantum behavior leads to the information paradox. For decades, theorists have proposed alternatives — either "regular black holes" (singularity removed, horizon kept) or "black-hole mimickers" (neither singularity nor horizon). Both approaches now have a growing literature, and several formation mechanisms for regular black holes have been worked out using deviations from GR, such as higher-curvature terms, asymptotic-safety corrections, or loop-quantum corrections.

The gravastar — short for *gravitational vacuum condensate star* — is the most elegant and physically motivated mimicker. Proposed in 2001 by Mazur and Mottola, it consists of a dark-energy interior described by a de Sitter metric (the same geometry that drives cosmic inflation and describes our accelerating universe at large scales), surrounded by a thin shell of ordinary matter, and matched to a Schwarzschild exterior. The de Sitter interior has negative pressure (dark energy pushes outward), and the shell's tangential pressure acts like a belt preventing expansion. A static equilibrium results: no horizon, no singularity, compactness almost indistinguishable from a black hole.

The critical unsolved problem was always *formation*: how does a gravastar actually come into being from real collapsing matter, starting from ordinary initial conditions? You can write down the static solution easily, but without a dynamical birth story, the gravastar is a mathematical curiosity — a stable state that the universe apparently never bothers to reach. Previous attempts at formation models either invoked non-GR physics (higher-curvature corrections, quantum gravity effects built into the action) or relied on exotic equations of state. Jampolski and Rezzolla take a different and strikingly clean approach: pure GR, starting from the simplest possible collapse scenario.

What they show is that a de Sitter region can nucleate at zero size at the center of a collapsing dust ball, expand outward against the infall, and naturally brake near the Schwarzschild radius — without any modification to Einstein's equations. The paper is compact (8 pages), analytically tractable, and published in *Physical Review D* as a Letter, signaling the editors' view that this is a significant, self-contained result.

**Prior Belief Check:** This result is genuinely notable within the community but not earth-shattering in terms of overturning anything. Experts largely expected that gravastar formation *should* be possible in principle; the open question was whether anyone could write down a consistent dynamical scenario within classical GR. This paper provides the first such scenario. It does require fine-tuned initial conditions — the parameter space for gravastar formation is a knife-edge between collapsing to a black hole and producing a non-equilibrium configuration — which is a real limitation and will likely remain a focal point of criticism. The result is also idealized (uniform dust, spherical symmetry, pressureless matter). So: experts will view this as an important proof-of-concept opening a new line of investigation, not as evidence that astrophysical black holes are routinely gravastars.

---

## 3. Necessary Background Crash-Course

**Oppenheimer-Snyder (OS) collapse.** In 1939, Oppenheimer and Snyder solved GR's equations for the simplest possible gravitational collapse: a perfectly uniform ball of pressure-free dust (pressureless matter) starting at rest. The interior evolves as a closed Friedmann universe — the same type of geometry that describes the cosmological Big Crunch — and is matched at the ball's surface to a Schwarzschild exterior. The dust surface falls inward on a predictable cycloid trajectory and hits the Schwarzschild radius in finite proper time. This is the GR textbook collapse.

*Analogy:* Think of OS collapse as a CPU thermal runaway with no feedback loop. Heat builds, no throttle engages, and the processor reaches a hard stop. The Schwarzschild radius is the wall the processor hits.

*Breaks when:* In a real CPU there are multiple feedback mechanisms (throttling, thermal sensors); they just fail. In OS collapse, there truly are *no* internal pressure gradients — the dust has zero pressure by definition. Real stellar collapse involves shocks, radiation pressure, and electron degeneracy. The OS model deliberately strips all of that out.

**de Sitter spacetime.** This is the geometry of a region dominated by a cosmological constant (or vacuum energy / dark energy) with equation of state pressure equals negative energy density. It's the spacetime inside the gravastar's core, and it's identical in structure to early-universe inflation: it expands exponentially with time. De Sitter space has positive curvature in a spatial sense and repulsive gravity — the geometry pushes outward.

*Analogy:* De Sitter space is a perfectly uniform spring under constant compression. Inject it into an otherwise collapsing system, and it pushes back. In the inflationary cosmology you know, it's what drove the exponential expansion of the early universe — the same math here drives the gravastar's interior.

*Breaks when:* The spring analogy makes it sound like the repulsion can always win. It can't — if the surrounding gravitational well is deep enough (initial compactness above 3/8, as the paper shows), the spring is overwhelmed and collapse wins.

**FLRW metric and scale factors.** Friedmann-Lemaître-Robertson-Walker (FLRW) is the metric of any homogeneous, isotropic universe — flat, open, or closed. It's described by a single time-dependent scale factor *a(t)* that encodes how distances grow or shrink. Both the dust ball's interior and the de Sitter region are described by FLRW metrics, just with different equations of state (zero pressure for dust, negative pressure for de Sitter). They each have their own scale factor and spatial curvature constant.

*Analogy:* Think of the scale factor as the clock speed of a processor, and the curvature constant as an initial overclocking setting. Two co-running processes (de Sitter bubble and dust ball) each have their own clock, and the junction condition is the synchronization protocol that makes sure both processes see the same physical boundary.

*Breaks when:* FLRW assumes homogeneity throughout the region it describes. The dust ball in real collapse develops density perturbations; the de Sitter interior by definition is perfectly homogeneous. Patching them together via Israel junction conditions is valid at the interface but ignores what happens when the dust develops real structure.

**Junction conditions (Israel thin shells).** When you glue two different spacetimes together along a hypersurface (a boundary), you need rules ensuring that observers on either side agree on the geometry of the interface. Israel's formalism says the induced metric (intrinsic geometry) must be continuous, but the extrinsic curvature (how the surface curves as embedded in each surrounding spacetime) can jump — that jump is physically a thin shell of matter with surface energy density and surface tension. In this paper, the dust-Schwarzschild boundary is a clean Israel junction (no shell); the de Sitter-dust boundary requires a shell with a surface tension.

*Analogy:* Junction conditions are like impedance matching in your SerDes links. If the characteristic impedance on each side of a transmission-line splice differs, you get a reflection — a physical signal artifact at the boundary. The surface tension of the gravastar shell is exactly that reflection layer: it carries the stress that makes the two spacetime patches fit together without pathological discontinuities.

*Breaks when:* The thin-shell approximation assumes the physical transition layer has negligible thickness. Real matter has finite extent; a shell of zero thickness is a mathematical idealization. Whether that matters quantitatively for gravastar stability is an open question.

**Compactness.** The compactness of a star is the ratio of its mass to its radius (in relativistic units where the Schwarzschild radius is 2M). A neutron star sits around 0.1–0.2. The Buchdahl limit — the most compact you can make any perfect fluid star in GR — is 4/9 ≈ 0.44. A black hole has compactness exactly 0.5 (Schwarzschild radius = 2M). The paper derives a new bound: gravastar formation is impossible above compactness 3/8 = 0.375, slightly below the Buchdahl limit.

---

## 4. Core Technical Explanation

**The three-region spacetime.** The key architectural move is to split the evolving spacetime into three nested regions at every moment:

- **Region I** (innermost): an expanding de Sitter FLRW spacetime — the nascent gravastar interior — described by its own scale factor and a negative spatial curvature constant (it starts at zero size and expands).
- **Region II** (shell): the collapsing dust FLRW spacetime — the infalling matter — described by its own scale factor and a positive spatial curvature constant (a closed Friedmann universe collapsing from rest).
- **Region III** (exterior): ordinary Schwarzschild vacuum, outside all the matter.

Each region has its own metric, its own time coordinate, and its own scale factor. The boundaries between them are two spherical hypersurfaces: one separating the de Sitter bubble from the dust (call it surface 1), and one separating the dust from the Schwarzschild exterior (surface 2). The proper circumferential radii of these surfaces — the measurable physical circumferences divided by 2π — are what the junction conditions track.

**The master differential equation.** They apply Israel junction conditions at both surfaces. The dust-Schwarzschild junction is standard OS collapse and fixes the dust evolution exactly. The de Sitter-dust junction is new. When they impose continuity of the induced metric across surface 1, they get a relationship between the rate of change of the de Sitter scale factor and the rate of change of the dust scale factor — a single coupled ODE for the position of the de Sitter boundary as seen from within the dust region.

This ODE has a critical feature: a divergence. The rate at which proper time in the de Sitter region maps to proper time in the dust region blows up when the de Sitter bubble surface reaches a specific "critical radius." At that critical radius, the expansion of the de Sitter boundary halts as seen by a dust observer. That halt is gravastar formation.

**Backward integration trick.** Rather than hunting forward through parameter space for initial conditions that produce a gravastar, they use a clever reversal: start from the known final state (a gravastar just formed, with the inner surface at the Schwarzschild radius and the outer dust surface just outside it), and integrate the equations backward in time. This turns the forward problem (find needle in haystack) into a backward problem (trace from the known endpoint), making the parameter-space exploration tractable.

The two free parameters are the de Sitter region's energy density and its spatial curvature constant. Different combinations of these two numbers produce three families of solutions:

1. Both surfaces collapse to zero → black hole forms.
2. The de Sitter expansion exactly meets the collapsing dust surface at the Schwarzschild radius → gravastar forms.
3. The de Sitter expansion outruns the collapse → a non-equilibrium configuration results (potentially a diffuse non-compact object, or an unstable transient).

**The compactness limit.** The causal constraint is elegant. For a de Sitter bubble to stop the collapse at the Schwarzschild radius, information about the bubble's existence must travel outward from the center and reach the collapsing dust surface before that surface crosses the Schwarzschild radius. A photon emitted at the center at the moment the bubble nucleates travels outward; the dust surface falls inward. If the dust ball starts too compact, the photon doesn't make it — the surface reaches 2M before the causal signal does. This sets a maximum initial compactness of exactly 3/8, derivable from the geometry of the cycloid collapse trajectory and the light travel time across the dust sphere.

The elegant thing is that 3/8 = 0.375 is only slightly below the Buchdahl limit of 4/9 ≈ 0.444. Stars above 3/8 compactness that collapse *must* form black holes; stars below this threshold could, in principle, form gravastars.

**Surface tension and energy density.** The de Sitter-dust interface carries a surface stress-energy tensor — essentially a thin shell of material with a surface energy density and a surface tension. They compute these explicitly. The surface energy density can be tuned to vanish at the moment of gravastar formation (by choosing the de Sitter energy density appropriately), which is the physically cleanest solution: the final gravastar has zero surface mass, just a pure surface tension. The surface tension itself diverges in the limit of zero-thickness shell — consistent with the known static gravastar solution where the shell provides the tangential pressure that maintains equilibrium.

**Three scenarios in spacetime diagrams.** Their Figures 1, 2, and 3 are spacetime diagrams showing the worldlines of the two boundaries. In the gravastar case (case 2), the blue curve (de Sitter boundary) and the red curve (dust surface) converge and meet exactly at the Schwarzschild radius from below and above respectively. In the black hole case (case 1), the red curve falls all the way to zero before the blue curve reaches it. In the non-equilibrium case (case 3), the de Sitter expansion overshoots, and the blue curve reaches the Schwarzschild radius while the red curve is still outside it.

**Assumption Audit:**

*Watch:* A reader familiar with inflation might assume that the de Sitter bubble, once nucleated, expands unstoppably — it is, after all, driven by a cosmological constant that doesn't dilute. The paper actually shows that the expansion *does* halt, but only because of the junction condition: the de Sitter bubble is not in free de Sitter space. It is expanding against collapsing dust, and the junction condition transfers information (in the form of the critical radius divergence) that effectively applies a brake. The de Sitter geometry intrinsically keeps expanding; the brake is entirely a boundary effect.

*Watch:* A reader might assume that "fine-tuned conditions" means a single special point in parameter space — a set-measure-zero accident. The paper actually shows that gravastar formation occurs along a one-dimensional curve in the two-dimensional (energy density, curvature constant) parameter space — infinitely many initial conditions lead to the same static gravastar, each with different dynamics on the way there. Fine-tuned in the sense that gravastar-forming parameters are a knife-edge between two families, but not uniquely fine-tuned.

---

The diagram above shows the three collapse outcomes in proper-time spacetime. In all three panels, the red curve is the dust surface worldline (starts at some initial radius, falls toward 2M), and the blue curve is the de Sitter bubble boundary worldline (starts at zero size, expands outward). Only in the middle case do they meet exactly at the Schwarzschild radius — that meeting point is the gravastar.

---

## 5. What's Genuinely New or Clever

**The backward-integration inversion.** Previous work struggled with the forward problem: pick initial conditions, integrate forward, and see whether you land on a gravastar. The parameter space is large and the gravastar condition is a knife-edge. Jampolski and Rezzolla invert this: define the end state you want (both surfaces meeting at 2M), then integrate backwards. This is mathematically clean and computationally efficient — it turns a search problem into a boundary-value problem. It's the kind of trick that makes you wonder why no one did it before.

**De Sitter nucleation within pure GR.** The genuinely novel physical result is that a gravastar can form from classical GR alone — no higher-curvature terms, no quantum corrections to the action, no exotic matter equations of state. The paper allows for quantum nucleation of the de Sitter bubble as one *motivation* for the bubble to appear, but the dynamics once it appears are entirely classical GR. This is the first such result. Prior papers on black hole alternatives forming dynamically all smuggled in deviations from GR somewhere. Here, standard GR + a cosmological constant in the interior region is sufficient.

The deep reason this works is subtle: the de Sitter metric is itself an exact vacuum solution of Einstein's equations with a cosmological constant. The paper isn't adding new physics — it's selecting a different vacuum to nucleate inside the collapsing matter. The junction conditions (Israel formalism) handle the interface self-consistently within GR.

---

## 6. Limitations & Open Questions

**Dust equation of state is unphysical.** The paper uses pressureless dust throughout. Real collapsing matter has pressure, stiffness, shock fronts, and radiation fields. Pressure gradients in real matter will resist collapse differently than dust, and the dynamics of the de Sitter-matter interface will change qualitatively. Whether the gravastar-forming parameter window survives in a realistic fluid is completely unknown. **(A) Consensus — explicitly acknowledged in the paper and a standard limitation of all OS-based studies.**

**Fine-tuning severity is unquantified.** The paper shows that gravastar-forming initial conditions form a one-dimensional curve in a two-dimensional parameter space. That's measure-zero in the strict mathematical sense: if you pick random initial conditions, you almost surely don't form a gravastar. The paper doesn't quantify *how sharp* the knife-edge is or whether astrophysical processes could plausibly populate that curve. **(A) Consensus — noted in the paper, and will be a central question for follow-up work.**

**Spherical symmetry is required.** The calculation is fully spherically symmetric. Real stellar collapse is not. Angular momentum, magnetic fields, and perturbations all break spherical symmetry. Whether the gravastar equilibrium survives even small asymmetric perturbations — let alone realistic rotation — is unknown. **(A) Consensus — acknowledged in the conclusion.**

**No quantum nucleation mechanism specified.** The paper demonstrates that *if* a de Sitter bubble nucleates at zero size, the subsequent dynamics can produce a gravastar. But *why* that bubble nucleates — whether it's a quantum tunneling event, a conformal anomaly effect (as Mottola's group has argued separately), or an instability in anti-de Sitter fluctuations — is left open. Without a concrete nucleation mechanism, the scenario's physical relevance is uncertain. **(B) Contested — Mottola and collaborators have argued for specific quantum nucleation mechanisms from conformal anomalies, but this is not mainstream consensus.**

**Gravastar vs black hole probability is uninvestigated.** Even granting that a de Sitter bubble nucleates, whether it's more likely to produce a black hole (case 1) or a gravastar (case 2) from realistic astrophysical initial data requires surveying the measure of each region in the full parameter space. **(C) Speculative — the paper explicitly defers this question to future work; I'm restating it as a limitation rather than adding new content.**

**Surface tension divergence and physical viability.** The surface tension at the de Sitter-dust boundary diverges in the zero-thickness limit — exactly what's expected for a static gravastar. But a diverging tension in a physical system raises questions about whether any realistic matter model can sustain it. **(B) Contested — gravastar proponents argue this is a legitimate mathematical idealization; critics argue it signals unphysical behavior.**

---

## 7. Three Crystallized Takeaways

1. **A gravastar can be born from pure GR:** No new physics is needed — just a de Sitter vacuum region that nucleates at a star's center during collapse, expands outward, and naturally brakes at the Schwarzschild radius due to the junction conditions with infalling matter.

2. **Compactness 3/8 is the hard wall:** Any star that collapses with initial compactness above 0.375 cannot produce a gravastar — the causal speed limit prevents the de Sitter bubble from stopping the collapse. Below that limit, gravastar formation is possible, but requires fine-tuned initial conditions.

3. **Proving it's possible is not the same as proving it happens:** This paper opens the door — it shows the scenario is dynamically self-consistent within GR — but astrophysical relevance requires realistic matter, rotation, and a concrete nucleation mechanism, none of which are addressed here.

---

## 8. Detailed Summary & Explanation

The paper by Jampolski and Rezzolla, published in *Physical Review D* in June 2026, addresses a foundational gap in the gravastar literature: while static gravastar solutions have been known since 2001, no one had shown how such an object could actually form from a collapsing star. The authors construct the first explicit dynamical formation model using only classical general relativity.

Their setup builds directly on the Oppenheimer-Snyder collapse, the simplest solvable model of gravitational collapse in GR — a uniform ball of pressureless dust starting at rest, collapsing to a black hole. Into this standard framework they embed a de Sitter region (a patch of spacetime dominated by dark energy) that starts at zero size at the dust ball's center and expands outward. The result is a three-region spacetime: a de Sitter interior, a dust-filled ring, and an exterior Schwarzschild vacuum, all glued together by Israel thin-shell junction conditions that guarantee a consistent, singularity-free patching of the Einstein equations.

The junction conditions reduce the full dynamical problem to a single coupled ordinary differential equation for the position of the de Sitter-dust boundary. This ODE has a notable mathematical feature: a divergence in the rate at which proper time in the de Sitter region maps to proper time in the dust region. When the de Sitter boundary reaches a critical radius (set by the dust's collapse geometry), that divergence means the de Sitter expansion *freezes* as seen by a dust observer. If this freeze happens just as the collapsing dust surface reaches the Schwarzschild radius from outside, the two surfaces meet at the Schwarzschild radius and a gravastar is born — an object with a de Sitter interior at exactly the Schwarzschild radius, a thin matter shell providing equilibrating tangential pressure, and a Schwarzschild exterior, but no horizon and no singularity.

Rather than searching forward through parameter space, they work backward: start from the known end state (both surfaces at the Schwarzschild radius) and integrate the equation backward in time, revealing what initial conditions lead to that outcome. This maps the full parameter space of de Sitter energy density and spatial curvature, revealing three families of outcomes: black hole formation, gravastar formation (along a one-dimensional curve in parameter space), and a non-equilibrium configuration. They also show that gravastar formation is possible for any initial dust radius above about 2.67 times the Schwarzschild mass, as long as the initial compactness of the collapsing star doesn't exceed the critical value of three-eighths.

That compactness bound has a beautiful causal argument: a de Sitter bubble nucleated at the center must be able to causally communicate its existence to the collapsing dust surface before the surface crosses the Schwarzschild radius. Since nothing travels faster than light, there's a maximum compactness above which the dust surface falls too fast, and the bubble's influence can't reach it in time. The resulting bound, compactness at most three-eighths, sits just below the Buchdahl limit (about four-ninths), which is the most compact any ordinary matter sphere can be in GR.

The surface tension at the de Sitter-dust boundary is computed explicitly. It diverges in the zero-thickness limit — consistent with the known static gravastar solution. The surface energy density can be tuned to vanish at gravastar formation by matching the de Sitter energy density to the dust energy density at that moment, giving a physically minimal solution with no exotic mass on the shell.

**Why the summary is framed this way:** The key interpretive choice is to foreground the formation mechanism as the real contribution — not the gravastar itself (which is twenty years old) but the first dynamical birth story. The backward-integration trick deserves explicit mention because it's the methodological innovation that made the calculation tractable. The compactness bound deserves emphasis because it's the paper's sharpest quantitative result and will be cited independently of the rest.

**Where I'm least confident in this analysis:** The physics of the surface tension divergence and its implications for physical realizability. The paper presents it as consistent with known static gravastar solutions, which is correct, but whether a real matter model can sustain a diverging tangential pressure during dynamic formation — as opposed to in a static equilibrium — involves subtleties of Israel thin-shell dynamics under time evolution that I may be underrepresenting. A specialist in relativistic thin-shell collapse would be the right person to interrogate this aspect.

---

## 9. Shorter Summary

Gravastars are hypothetical objects that look almost exactly like black holes from the outside but contain no singularity and no event horizon. Instead of collapsing to a point, the core transforms into a region of dark energy — the same type of spacetime that drives cosmic acceleration — surrounded by a thin shell of matter that holds everything in equilibrium. The idea has been around since 2001, but no one had shown how such a thing could actually form from a real collapsing star.

Jampolski and Rezzolla fill that gap using only standard general relativity. They start with the simplest possible collapse — a pressureless dust ball collapsing in the manner that Oppenheimer and Snyder worked out in 1939 — and insert a small region of dark-energy-dominated spacetime at the center. This dark-energy bubble starts at zero size and expands outward, while the dust continues to collapse inward. The crucial question is whether the outward-expanding bubble can catch up with the inward-falling dust surface before either crosses the point of no return.

Under the right initial conditions, it can. The dark-energy expansion naturally brakes near the Schwarzschild radius — not because of any added mechanism, but because of how the geometry of the two regions fits together at their shared boundary. When both the bubble's outer edge and the dust's inner edge arrive at the Schwarzschild radius simultaneously, a static gravastar locks in: dark-energy interior, matter shell, Schwarzschild exterior, no singularity, no horizon.

The paper also derives a hard limit: if the collapsing star starts with a compactness — mass divided by radius — above three-eighths, this scenario cannot work. The dust falls too fast for any signal from the bubble to reach the surface in time. This causal speed limit produces a clean numerical bound just below the Buchdahl limit, which is the most compact any ordinary star in general relativity can be. Stars more compact than this must form black holes; less compact stars have at least a theoretical path to gravastar formation.

The result is a proof-of-concept rather than a demonstration that astrophysical black holes are routinely gravastars. The calculation uses an idealized dust model with spherical symmetry, requires fine-tuned initial conditions, and doesn't specify what physical process nucleates the dark-energy bubble in the first place. But it clears the most important theoretical hurdle: gravastar formation is dynamically consistent with classical general relativity, without any modification to Einstein's equations.
