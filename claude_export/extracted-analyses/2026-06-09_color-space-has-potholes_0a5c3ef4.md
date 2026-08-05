---
source: claude_export
conversation_uuid: 0a5c3ef4-fe19-4dd1-b19a-ea3a44724e23
title: "Color Space Has Potholes"
created_at: 2026-06-09T18:09:14.340521Z
updated_at: 2026-06-11T15:42:18.300647Z
tier: A
score: 227
n_messages: 12
---

# Color Space Has Potholes

## Human

Detailed analysis of this paper

## Assistant

Good. I have solid material from the open-access paper text, the Wikimedia-hosted PDF cache, and the Newswise/phys.org/SciTechDaily coverage. Now writing the full analysis.

---

# **v3.4.9**

---

## 1. Punchy Title & One-Sentence Hook

**Color Space Has Potholes: Why Your Brain's Distance Meter Isn't a Ruler**

Schrödinger sketched a beautiful geometry of color perception a century ago but left three fatal holes in the foundation — this Los Alamos team patches all three by replacing his flat-ish Riemannian ruler with a genuinely warped, non-Riemannian one, and proves experimentally the fix works.

---

## 2. Big-Picture Context

Color perception is fundamentally a measurement problem: given two colors, how *different* do they look to a human observer? Since the 19th century, scientists have treated that question geometrically — imagine all possible colors living in a 3D space, and the perceived difference between two colors is the "distance" between their positions. Riemann (1854) gave mathematicians the framework for curved distance metrics, Helmholtz applied it to color in the 1890s, and Schrödinger formalized hue, saturation, and lightness from that metric in the 1920s. This lineage is so well-established it's baked into the international color standard ΔE used everywhere from display calibration to paint matching.

The problem is that Schrödinger's Riemannian framework assumes distances add up cleanly — ten small color steps equal one large color step. But human perception doesn't work that way. Large color differences look *smaller* than the accumulated sum of small steps, a well-documented phenomenon called **diminishing returns**. Bujack's group proved in a landmark 2022 PNAS paper that perceptual color space is fundamentally non-Riemannian for exactly this reason — the triangle inequality is violated. Think of it as the color equivalent of discovering that spacetime isn't flat after decades of treating it as Euclidean.

This 2025 CGF paper is the follow-up: now that we know the geometry is non-Riemannian, how do we rebuild Schrödinger's beautiful definitions of hue, saturation, and lightness in that warped space? Three specific flaws in his approach had to be fixed. The paper fixes all three, validates the fixes experimentally, and in doing so closes a century-old loop: hue, saturation, and lightness don't emerge from cultural or learned experiences but reflect intrinsic properties of the color metric itself.

This matters well beyond color science. Scientific visualization — the field of turning data into images that communicate meaning — depends critically on accurate perceptual color models. A bad color map that assigns similar-looking colors to very different data values actively misleads scientists reading their own results. The Los Alamos team works in exactly this applied domain; they came to this problem because their visualization algorithms were producing artifacts from Schrödinger's flawed geometry.

---

## 3. Necessary Background Crash-Course

**Color space as a manifold.** Your three cone types (L, M, S — roughly red, green, blue tuned) each report a scalar activation. Together they produce a 3D coordinate. Color space is just the set of all such coordinates. Saying it's a "Riemannian manifold" means you can define a smoothly varying local distance metric at every point — like a rubber sheet that might be more or less stretched in different directions, but is always locally ruler-flat. *Analogy: a curved CPU floorplan where each tile has its own local clock frequency — cache latency within a tile is clean; cross-tile latency depends on the local warp.*

**The Riemannian line element.** Helmholtz and Schrödinger wrote down a formula that assigns a tiny "perceptual distance" to any infinitesimally small step in color space. Integrate that along a path, and you get total perceptual distance. The key constraint in a Riemannian space is that this integration is additive — no matter how many segments you break a path into, the total length is the same. *Analogy: measuring a signal path in a PCB with a calibrated impedance tester — every segment contributes independently.*

**Why non-Riemannian?** Diminishing returns means: the perceived size of a large color jump is *less* than what you'd get summing up small perceptual steps along that path. This violates a core Riemannian axiom (specifically, metric spaces require triangle inequality equality for collinear points). A non-Riemannian metric — technically a **Finsler metric** — allows the "ruler" itself to change depending on how fast you're moving through color space, not just where you are. *Analogy: a SerDes link where jitter accumulation is sub-linear with cable length — each segment adds less than the previous one.*

**Geodesic.** The shortest path between two points in a curved space. In flat Euclidean space, geodesics are straight lines. In a curved Riemannian space (like the surface of a sphere), they're great circles. In a non-Riemannian Finsler space, they can be even more exotic — shortest path and "straightest path" can diverge. *Analogy: optimal routing in a network with asymmetric link costs.*

**Hue, saturation, lightness (HSL) — Schrödinger's definitions.** Lightness = total geodesic distance from black. Saturation = how far you are from the "neutral axis" (the gray axis from black to white) within your equal-lightness surface. Hue = which direction around the neutral axis you sit. Clean and geometric — in principle. In practice, Schrödinger left three things undefined or broken.

**The Bezold-Brücke effect.** When you increase the brightness of a colored light, its *apparent hue shifts* — a yellow-green becomes more yellow, a blue becomes more cyan. This means equal-hue surfaces in color space are *not* straight lines pointing at black; they curve. Schrödinger's straight-line hue definition misses this entirely.

---

## 4. Core Technical Explanation

**The three problems and their fixes:**

**Problem 1 — Hue definition breaks under Bezold-Brücke.**
Schrödinger defines hue as the "stimulus quality" that doesn't change as you scale intensity — essentially, the direction from black to your color is your hue label. But that direction is a straight line, and experimental data clearly show equal-hue surfaces curve away from straight lines as you move through the space. Bujack's team replaces the straight-line path from black with the **geodesic** from black to the color under the non-Riemannian metric. They embed previous experimental equal-hue surface measurements into the CIERGB color space and show the geodesic paths follow the curvature of those surfaces. The image below shows this directly:

[![CIERGB equal-hue surfaces showing geodesic curvature](https://scitechdaily.com/images/CIERGB-Color-Spaces-777x548.jpg)](https://scitechdaily.com/images/CIERGB-Color-Spaces.jpg)
*Equal-hue surfaces in CIERGB space. Schrödinger's straight-line hue paths (what you'd expect if hue were a simple ray from black) don't match the experimental data. The geodesic paths in the non-Riemannian metric do. Each surface represents colors that look the same hue — note how they fan and curve rather than pointing like spokes at the black apex.*

**Problem 2 — Non-Riemannian metrics introduce a lightness ambiguity.**
In a Riemannian space, the length of a path from A to B equals the length from B to A (symmetry). In a Finsler/non-Riemannian space, this can break — going uphill and going downhill can have different "costs." That means "distance from black" — Schrödinger's lightness — could give two different answers depending on whether you measure starting from the color or starting from black. The team frames this as two candidate lightness definitions. They then run a psychophysical experiment: show observers a color and ask them to pick the gray patch that appears equally light. If the ambiguity mattered perceptually, the two definitions would predict different matching grays. Their experiment shows the two definitions give the same result within experimental noise, so the ambiguity is real mathematically but inconsequential for actual human perception. *Analogy: two different routing algorithms that produce different path lengths in simulation but land on the same hardware execution time due to pipeline saturation masking the difference.*

[![Color perception experiment results](https://scitechdaily.com/images/Color-Perception-Experiment.jpg)](https://scitechdaily.com/images/Color-Perception-Experiment.jpg)
*The experimental validation. Each row is a reference color; columns 2 and 4 show the gray matches predicted by the two competing lightness definitions. Subjects chose grays from column 3. If columns 2 and 4 match visually, both definitions agree — and they do, row after row. The ambiguity collapses in practice.*

**Problem 3 — The neutral axis was never defined.**
This is the most fundamental gap. Schrödinger's definitions of saturation and hue both reference the neutral axis (the black-to-white gray spine of color space), but he never gave a geometric definition of it. He simply assumed you'd know where "gray" was. This is like building a coordinate system without defining the origin. In a non-Riemannian setting, you can't even borrow Euclidean intuitions to patch it.

Bujack's team defines the neutral axis geometrically: within any equal-lightness surface (a level set at constant perceived brightness), the neutral point is the color that sits **closest to black** under the non-Riemannian metric — i.e., the color reachable from black via the shortest geodesic that also lies within that lightness surface. String those neutral points together across all lightness levels and you get the neutral axis. Saturation then decreases as one moves closer to this neutral axis — exactly as Schrödinger intended, but now on rigorous geometric footing.

The team also identifies a subtle secondary issue: two plausible ways to generalize Schrödinger's saturation definition to non-Riemannian space don't automatically agree. The first uses the raw non-Riemannian path length directly. The second computes an "induced Riemannian metric" from those path lengths and uses that. These can give different numbers, and the paper flags this openly as an unresolved subtlety that probably doesn't matter perceptually but deserves future attention.

**The experimental backbone:**
Throughout, they validate by embedding historical color-matching data (multiple independent studies) into the CIERGB color space and checking whether the geodesic predictions align with the experimental equal-hue and equal-saturation boundaries. They also run their own lightness-matching experiment with 289 human responses per reference color. The match between theory and experiment is the whole claim — this isn't a pure theory paper; it's theory-plus-experiment.

---

## 5. What's Genuinely New or Clever

**The geodesic replacement for stimulus quality.** The conceptual move of swapping Schrödinger's straight-line "hue ray" for a geodesic in the non-Riemannian metric is clean, minimal, and automatically handles the Bezold-Brücke effect without adding free parameters. It's the kind of fix that looks obvious in retrospect but required recognizing that the whole Riemannian scaffolding was wrong first.

**Defining the neutral axis via geometric minimization.** Nobody before had formally defined gray as "the shortest-geodesic point on each equal-lightness surface." This closes a foundational gap that has existed since Schrödinger wrote down his definitions — a hole so basic it's almost embarrassing in retrospect. It also makes the definition intrinsic: you can find the neutral axis from the metric alone, without any external cultural or physiological assumptions about what "gray" means. The work establishes color perception attributes as intrinsic properties of the color metric itself, not constructs imported from outside the geometry.

---

## 6. Limitations & Open Questions

**The Finsler metric isn't uniquely pinned down.** The 2022 PNAS paper established that perceptual color space is non-Riemannian, but the specific Finsler metric they use carries uncertainty. The paper acknowledges that the saturation definition has two non-equivalent formulations in non-Riemannian space, and doesn't resolve which is perceptually "correct" — just notes they likely agree in practice. That's an honest admission but a real gap.

**The neutral axis experiment is indirect.** Demonstrating that two definitions of lightness agree is necessary but not sufficient to prove the neutral axis definition is the *right* one. A fully discriminating experiment would need to directly test whether the geometric neutral axis predicts human gray-matching across a wide gamut, including saturated colors far from the axis — the paper doesn't fully do this.

**Scope is limited to color-normal trichromats under standard illumination.** Anomalous trichromacy, tetrachromacy, and chromatic adaptation (the brain's white-balance correction) are all untouched. The neutral axis definition in particular will shift under different illuminants — von Kries adaptation will warp the metric, and the "geometric gray" will move.

**Geodesic computation is still expensive.** The team's 2023 TVCG paper on efficient geodesic computation in color space is a prerequisite for making this usable in real visualization pipelines. The math is clean but production deployment at real-time rendering speeds remains non-trivial.

**The ΔE standard remains uncorrected.** The international ΔE color-difference standard used in industry is still based on Riemannian assumptions. This paper provides theoretical grounding for an overhaul, but calibrating an industry standard requires broad experimental datasets and committee processes that are years away.

---

## 7. Three Crystallized Takeaways

1. **Schrödinger was 90% right but built on a cracked foundation** — his hue, saturation, and lightness definitions are geometrically elegant but required a Riemannian assumption that is demonstrably wrong; swapping in the correct non-Riemannian geodesics fixes all three outstanding problems at once.

2. **The neutral axis — the gray spine of color space — finally has a rigorous definition** after a century of being assumed without proof: it's the locus of colors closest to black on each equal-brightness surface, derived purely from the perceptual distance metric with no external reference.

3. **Color qualities are geometry, not culture** — hue, saturation, and lightness are intrinsic properties of the warped perceptual distance metric, which means any sufficiently accurate model of how far apart colors look will automatically recover these perceptual attributes without any additional assumptions about vision biology or human experience.

---

## 8. Detailed Summary & Explanation

**What the paper does and why it matters:**

For over 150 years, color scientists have tried to build a mathematical "map" of human color perception — a 3D space where the distance between any two points tells you exactly how different those two colors look to a human eye. Riemann's geometry of curved spaces provided the tools, Helmholtz applied them to color, and Schrödinger in the 1920s used that framework to give formal geometric definitions for the three core color attributes: hue (the "color-ness" — red vs. blue vs. green), saturation (how vivid vs. gray), and lightness (how bright vs. dark).

Schrödinger's definitions were elegant: lightness is how far you are from pure black along the shortest perceptual path; the neutral axis is the gray spine of the space (black-to-white); saturation is how far you are from that gray spine within a constant-lightness layer; and hue is which direction around the spine you sit. Beautiful in concept.

Three problems undermined it in practice.

**First problem:** Schrödinger defined hue by drawing a straight line from black through your color. But experimental evidence — the Bezold-Brücke effect — shows that equal-hue surfaces (all the reds, say, at every brightness) don't form straight rays from black; they curve. The Bujack team replaces the straight line with a **geodesic** — the truly shortest path in the warped perceptual space. When they plot this against historical experimental data on equal-hue surfaces, the geodesic paths match the measured curves. Fix achieved.

**Second problem:** Schrödinger assumed perceptual color space obeys Riemannian geometry, where distances add up like ordinary ruler measurements. The team's 2022 PNAS paper proved this is wrong: human perception shows **diminishing returns** — a large color difference looks smaller than the sum of many small color differences along the same path, violating a core property of Riemannian spaces. The correct framework is non-Riemannian (technically a Finsler geometry), which is more general: the local "cost" of moving through color space can depend on the direction and speed of travel, not just the location. In this more general geometry, measuring the distance from point A to point B can give a different answer than measuring from B to A (the "asymmetry" of the metric). This creates an ambiguity: Schrödinger's lightness definition — distance from black — could mean "distance measured starting from black" or "distance measured starting from the color," and in a non-Riemannian space those can differ. The team ran a human experiment: they showed people colored patches and asked them to pick the gray that appeared equally bright. If the asymmetry mattered, the two definitions would predict different grays. Their experiment with 289 responses per reference color found the two predictions were indistinguishable. The mathematical ambiguity is real but perceptually harmless.

**Third problem (the deepest one):** Schrödinger's whole framework — saturation, hue, the neutral axis — is built relative to the gray spine of color space, but he never actually defined that spine mathematically. He assumed people would know intuitively where "gray" lived. In any rigorous geometric treatment, especially in a non-Riemannian space that doesn't inherit Euclidean intuitions, this is a foundational hole. The team's solution: within any equal-lightness layer (a surface of constant perceived brightness), define the neutral point as the color that sits **geometrically closest to black** under the perceptual metric. The collection of all such neutral points, one per lightness layer, forms the neutral axis. This definition requires nothing external — no assumptions about cone physiology, no cultural expectations about gray — just the metric itself. They validate it by checking that the experimentally chosen neutral-point grays align with the geodesic-based prediction.

The result is a complete, rigorous reformulation of Schrödinger's color attribute theory that works in the correctly non-Riemannian color space. The core conclusion is that hue, saturation, and lightness are intrinsic geometric properties of the color perception metric — they emerge from the structure of perceptual distance itself, not from biology or culture imposed from outside the geometry.

**Why it matters beyond color theory:** This work directly feeds scientific visualization — the craft of turning numbers into images that communicate. Colormap design (choosing which colors represent which data values) is only as good as the underlying perceptual model. Bad colormaps misrepresent data. The Los Alamos team works in exactly this space — their original motivation was fixing artifacts in their own visualization pipelines. A non-Riemannian-aware color model means future colormaps can be perceptually uniform in a much stronger sense than current industry-standard maps.

---

## 9. Shorter Summary

Erwin Schrödinger, better known for quantum mechanics, also built the most mathematically complete model of color perception in the 1920s. He defined hue, saturation, and lightness as geometric properties of a curved "color space" — a three-dimensional map where distance encodes how different two colors look to a human eye. His framework was influential but had three long-standing problems: his definition of hue used straight-line paths that don't match experimental data (the Bezold-Brücke effect, where perceived hue shifts with brightness); his lightness definition runs into an ambiguity when the underlying geometry is more general than he assumed; and he never formally defined the gray axis that his whole framework depends on.

A Los Alamos team led by Roxana Bujack fixes all three. The key move: replace Schrödinger's straight-line geometry with geodesics — truly shortest paths — computed in the correct non-Riemannian (Finsler) color space that their 2022 work established. The hue fix naturally captures the Bezold-Brücke curvature. The lightness ambiguity turns out to be mathematically real but perceptually irrelevant, confirmed by a human experiment. And the neutral gray axis gets its first rigorous definition: within any equal-brightness layer of color space, gray is the color sitting geometrically closest to black under the perceptual distance metric — no external assumptions needed. The payoff is that hue, saturation, and lightness are now proven to be intrinsic geometric properties of how far apart colors look, not cultural constructs — closing a century-old loop in the mathematics of perception.

## Human

More details on Schrödinger's definitions. Lightness = total geodesic distance from black. Saturation = how far you are from the "neutral axis" (the gray axis from black to white) within your equal-lightness surface. Hue = which direction around the neutral axis you sit. Clean and geometric — in principle. In practice, Schrödinger left three things undefined or broken.

## Assistant

**Elaborating**

Great — let's pull apart each of Schrödinger's three definitions at the technical seams, show exactly where they work, where they crack, and why the cracks matter.

---

## Schrödinger's Color Geometry: A Full Dissection

### The Setup: What Schrödinger Was Actually Doing

First, appreciate the audacity of the project. Schrödinger wasn't trying to describe color physics (wavelengths, photons) — he was trying to describe **color perception as pure geometry**, with zero neuroscience. His thesis: everything you need to know about how a human experiences a color — its brightness, its vividness, its "color-ness" — can be derived solely from one object: the **perceptual metric**, the function that tells you how different any two nearby colors look.

This is a profound claim. It says the metric *contains* all perceptual information. Hue isn't a biological fact about cone cells — it's a geometric fact about the shape of the metric. This is the same philosophical move that general relativity makes: gravity isn't a force, it's the geometry of spacetime. Schrödinger was doing general relativity for the inside of your skull.

The metric he used is a **Riemannian metric** — specifically a line element that assigns an infinitesimally small perceptual distance to any infinitesimally small step in color space. Integrate along a path, get total perceptual cost. Minimize over all paths, get the geodesic distance between two colors.

With that infrastructure in place, here are his three definitions, cracked open.

---

### Definition 1: Lightness

**The idea:** Lightness is the total geodesic distance from pure black (the origin of color space) to your color, measured along the shortest perceptual path.

**Why this is elegant:** It's coordinate-free and metric-intrinsic. You don't need to know which direction is "up" in color space, or pick a preferred axis. You just ask: what's the shortest route from nothing to this color, in perceptual distance units? A bright white is far from black; a deep shadow is close. Naturally, the definition also handles colored lights — a vivid red and a dim red at the same geodesic distance from black have the same lightness, even though they look very different in other ways.

**Where it works:** For small color differences near black, and for comparing grays to each other, this definition tracks human judgments well. The psychophysics bear it out in the low-contrast regime.

**Where it starts to strain:** The moment you go to large color differences, the Riemannian assumption starts failing. In a Riemannian space, the geodesic distance from black to a color is path-additive — you can compute it by integrating small steps. But as Bujack's 2022 PNAS work showed, human perception is **subadditive** for large differences. Ten barely-noticeable color steps don't add up to one ten-times-as-noticeable jump — the large jump feels smaller than the sum. So the "ruler" you're integrating with is systematically wrong for large geodesic distances, which is exactly what lightness is measuring. The geodesic distance from black to a bright color is a *large* distance — precisely the regime where Riemannian geometry lies.

**The non-Riemannian complication (the asymmetry problem):** In Schrödinger's Riemannian world, distance from A to B equals distance from B to A — symmetry is automatic. In a Finsler/non-Riemannian space, this breaks. "Distance from black to this color" and "distance from this color to black" can be different numbers. So when you say "lightness equals geodesic distance from black," you immediately face: which direction are you measuring? Schrödinger never had to ask this question because his geometry was symmetric by construction. Bujack's team asks it, derives two candidate lightness functions, and then shows experimentally that human subjects can't tell the difference between the two — the perceptual asymmetry is too small to matter. But the conceptual crack is real.

**The deeper issue:** Lightness in practice is also influenced by **surround context** — the same gray patch looks lighter against black than against white (simultaneous contrast). Schrödinger's purely intrinsic metric definition explicitly ignores this. It's a model of isolated color appearance, not contextual appearance. This is a known scope limitation, not a flaw in the internal logic, but it means the definition doesn't fully capture what humans call "lightness" in complex scenes.

---

### Definition 2: The Neutral Axis (The Hidden Gap)

Before you can define saturation, you need the neutral axis — the spine of gray from black to white that everything else is measured relative to. This is so foundational that without it, both saturation and hue collapse.

**What Schrödinger assumed:** He assumed the neutral axis is simply the set of all "achromatic" stimuli — lights that produce no net chromaticity signal, activating the three cone types in the same ratio as the "white" adaptation reference. In colorimetry terms, it's the set of points in color space that plot along the equal-energy white point as intensity varies.

**Why this seems fine:** In a Euclidean or mildly curved Riemannian space, the neutral axis is visually obvious — it's the straight line (or gently curved spine) that runs through all the grays. You can define it extrinsically by specifying the cone-activation ratios that correspond to achromatic appearance.

**Why it's actually a problem:** Schrödinger's *geometric* framework promises that all perceptual attributes emerge purely from the metric — no external biological facts needed. But his neutral axis definition secretly imports an external fact: you need to know which cone-activation ratio counts as "achromatic." This is a biological fact about the visual system, not a geometric fact about the metric. The neutral axis is thus a **hybrid** — partly geometric (it's a curve in color space), partly physiological (which curve it is depends on adaptation state and cone spectral sensitivities).

In a non-Riemannian space, the problem becomes acute. You can no longer assume the neutral axis is "the straight line" because straight lines don't have preferred status in curved geometry. And the metric itself might curve away from the physiological achromatic locus. The two definitions — physiological achromatic locus versus geometric minimizer of distance to black — might not coincide.

**Bujack's fix:** Define the neutral axis purely geometrically. Within any equal-lightness surface (a level set of the lightness function defined above), the neutral point is the color that minimizes geodesic distance to black. No cone physiology required. String these minimizing points together and you have a neutral axis defined entirely by the shape of the metric. This closes the foundational gap.

**A subtle remaining issue:** The minimizer might not be unique — in a sufficiently warped metric, there could be multiple points in a given lightness surface that are equidistant-minimum from black. The paper doesn't deeply address this degeneracy case, presumably because in practice the metric is well-behaved enough that a unique minimizer exists. But in principle it's a gap.

---

### Definition 3: Saturation

**The idea:** Once you have the neutral axis, saturation is the geodesic distance from a color to the nearest point on the neutral axis, measured *within* the equal-lightness surface that contains the color.

Unpack that constraint: you hold lightness constant (you stay on your equal-lightness surface — think of it as a 2D sheet at a fixed perceived brightness), and within that sheet you measure how far your color sits from the gray point on that sheet. High saturation = far from gray. Zero saturation = you're on the neutral axis itself (you are the gray).

**Why this is elegant:** Again, intrinsic and coordinate-free. You don't need to know what "red" is or where it lives in RGB space. You just ask: within my brightness layer, how far am I from the neutral reference? A vivid red and a vivid blue at the same lightness will have the same saturation if they're equidistant from the neutral axis in their common equal-lightness surface.

**Where it works:** For moderate saturations near the neutral axis, and in regimes where the Riemannian metric is a decent approximation, this tracks human saturation judgments reasonably well. It also naturally handles the fact that saturation and lightness are perceptually somewhat independent — changing lightness moves you between surfaces, not within them.

**The first crack — the Bezold-Brücke contamination:** Schrödinger's saturation definition depends on the neutral axis, which he defined as the physiological achromatic locus. But the equal-lightness surfaces themselves are defined by geodesic distance from black — and the direction of "toward black" inside those surfaces is determined by the geodesics, which curve due to the Bezold-Brücke effect. So if hue definition is contaminated by the straight-line error, and saturation is defined within the same equal-lightness surfaces, saturation inherits some of that error. When Bujack's team fixes the geodesics, the equal-lightness surfaces are recomputed, and saturation automatically becomes more accurate.

**The second crack — two non-equivalent generalizations in non-Riemannian space:** This is subtle and the paper flags it explicitly. In a Riemannian space, there's only one natural way to define "distance from a color to the neutral axis within the equal-lightness surface." In a non-Riemannian space, two natural generalizations appear:

The first uses the raw non-Riemannian path length directly — you just ask for the shortest path within the equal-lightness surface under the Finsler metric.

The second computes what's called an **induced Riemannian metric** from the Finsler metric — you take the Finsler metric, extract a symmetric Riemannian approximation from it, and use that symmetric version to measure the distance to the neutral axis.

These two methods are mathematically distinct. They agree at infinitesimal scales but can diverge for paths of finite length — exactly what saturation measures. The paper notes this ambiguity exists, presents both, and essentially punts on resolving it, stating the perceptual difference is likely negligible but offering no experimental test specific to this question. This is the most honest unresolved technical crack in the paper.

---

### Definition 4: Hue

**The idea:** Hue is the direction around the neutral axis you sit, within your equal-lightness surface. Once you know your saturation (how far from the axis you are), hue is the angular coordinate — north vs. south vs. east vs. west, in the 2D sheet of that equal-lightness surface, centered on the neutral axis point.

**Why this is elegant:** It's polar coordinates in the equal-lightness surface, with the neutral point as origin and geodesic distance as radius. Hue is the angle. Every distinct hue corresponds to a distinct "ray" emanating from the neutral axis, within the equal-lightness surface.

**The Bezold-Brücke crack — what Schrödinger actually broke here:** His definition says "hue is constant along the path from black to your color" — i.e., scaling the intensity of a light without changing its spectral composition traces a path of constant hue. The path he used is the **straight line** from black to the color in color space.

But the Bezold-Brücke effect is precisely the experimental observation that this is wrong. When you increase the intensity of a spectral yellow light (without changing its wavelength), the hue you perceive shifts — the light appears more greenish-yellow at low intensity and more pure yellow at high intensity. That means equal-hue surfaces (all the stimuli that look "the same hue" across different brightnesses) do **not** form straight lines from black. They curve.

Schrödinger's straight-line definition therefore incorrectly assigns different hues to stimuli that observers judge as the same hue, and the same hue to stimuli that observers judge as different hues. The error grows with distance from black — i.e., for bright, saturated colors.

**Bujack's geodesic fix:** Replace "straight line from black to color" with "geodesic from black to color" under the non-Riemannian metric. The geodesic naturally curves in the same direction the equal-hue surfaces curve, because the metric that defines equal-hue (in Helmholtz's and Schrödinger's original vision) is the same metric that defines the geodesics. When they embed the historical equal-hue experimental data into CIERGB color space and plot the geodesics, the paths follow the experimental surfaces. The fix is geometrically minimal — you're not adding parameters, you're just using the correct notion of "straight" for your space.

**The residual crack:** Equal-hue surfaces are measured psychophysically under specific adaptation conditions, and those conditions affect the metric. The geodesic fix is only as good as the non-Riemannian metric it's computed in — and that metric is still being refined. Additionally, hue perception has both a chromatic-adaptation component (your "white point" shifts with illumination) and a higher-level cognitive component (category labels like "red" are language-dependent). Schrödinger's geometric hue captures neither of these, and the geodesic fix doesn't change that.

---

### The Meta-Crack: Internal Consistency

There's a structural issue that cuts across all three definitions. Schrödinger builds them in a specific dependency order:

Metric → Lightness (geodesic distance from black) → Equal-lightness surfaces (level sets of lightness) → Neutral axis (the gray spine) → Saturation (distance to neutral axis within equal-lightness surface) → Hue (angle in equal-lightness surface)

Each definition depends on all the ones before it. An error anywhere in the chain propagates forward. Schrödinger's Riemannian metric is wrong (Bujack 2022), so lightness is slightly miscalibrated for bright colors, so equal-lightness surfaces are slightly wrong, so the neutral axis derivation starts from imperfect surfaces, so saturation and hue inherit accumulated error.

Bujack's 2025 paper fixes the metric and the neutral axis definition, which in principle repairs the whole chain simultaneously. But it does so in a framework (non-Riemannian) that itself has unresolved degrees of freedom — the specific Finsler metric isn't uniquely determined from existing data. So the chain is now formally correct in structure but still approximately calibrated at the metric level. The geometry is right; the numbers are still being tuned.

---

### Quick Summary Table

| Definition | Schrödinger's Version | Specific Crack | Bujack's Fix |
|---|---|---|---|
| **Lightness** | Geodesic distance from black | Riemannian = wrong geometry; asymmetry in non-Riemannian case | Non-Riemannian geodesic; asymmetry shown to be perceptually negligible |
| **Neutral axis** | Physiological achromatic locus | Imported external biology; not metric-intrinsic | Geometric minimizer of distance-to-black on each equal-lightness surface |
| **Saturation** | Distance to neutral axis within equal-lightness surface | Inherits all upstream errors; two non-equivalent non-Riemannian generalizations exist | Geodesic-distance version in Finsler space; ambiguity noted but not resolved |
| **Hue** | Direction of straight line from black to color | Bezold-Brücke effect: straight lines don't follow equal-hue surfaces | Replace straight line with geodesic; matches experimental equal-hue data |

The deepest unresolved issue is the **saturation ambiguity** — the two Finsler generalizations that haven't been experimentally discriminated. Everything else is closed or shown to be perceptually negligible.

## Human

Don't really understand Within any equal-lightness surface (a level set of the lightness function defined above), the neutral point is the color that minimizes geodesic distance to black.

## Assistant

**Clarifying**

Good catch — that sentence is doing too much work too fast. Let me rebuild it from scratch, one layer at a time.

---

## What Is an Equal-Lightness Surface?

Start with the full 3D color space. Every possible color is a point in that space. Three coordinates — roughly, how much red, green, and blue signal your cones are sending.

Now imagine Schrödinger's lightness function already exists and works correctly. You can ask: what is the lightness value of every color in that space? Some colors are bright, some are dark, most are somewhere in between. The lightness function assigns a single number to every point.

Now ask: **which colors all share the same lightness value?**

Those colors form a surface — a 2D sheet floating inside the 3D color space. Every point on that sheet has identical perceived brightness. You can have a vivid red, a muted green, a grayish blue, and a saturated purple — all wildly different in hue and saturation — but if they're all on the same sheet, they all look equally bright to you.

That sheet is the **equal-lightness surface**. It's the color-space equivalent of a contour line on a topographic map — every point on the line is at the same elevation, even though the points are geographically spread out in different directions.

There are infinitely many such surfaces — one for every possible lightness value. They stack inside the 3D color space like layers in a cake, from a very dark surface near the black point all the way up to a very bright surface near white.

*CPU analogy: think of performance bins in a chip fab. Every die on a wafer gets tested and assigned a speed grade. The "equal-lightness surface" is the set of all dies that binned at exactly 3.2 GHz — they came from different parts of the wafer, have different leakage characteristics, look different under a microscope, but they all hit the same clock target. The speed grade is the single number that defines the surface.*

---

## What Lives on One of These Surfaces?

Pick one equal-lightness surface — say, the one corresponding to medium brightness, call it lightness = 50.

On that surface you have:
- A medium gray (low saturation, no particular hue)
- A medium red
- A medium green
- A medium blue
- Hundreds of other colors at medium brightness

They're all on the same 2D sheet. Within that sheet, colors vary in two ways: **which hue** they are, and **how saturated** they are. Lightness is held constant by construction — you're already on the surface.

The neutral axis — the gray spine — passes through this surface at exactly one point. That point is the medium gray that lives on this particular brightness level. Call it the **neutral point** of this surface.

---

## What Does "Minimize Geodesic Distance to Black" Mean?

Here's the question Bujack's team is answering: **How do you find that neutral point geometrically, without importing any biology?**

Schrödinger's answer was essentially: "It's the gray one — the achromatic one — you'll know it when you see it." That's importing cone physiology. Bujack wants a definition that falls out of the metric alone.

Their answer: the neutral point on this surface is the color that is **closest to black**, measured in perceptual distance, but with one constraint — you can only consider colors that actually live on this surface.

Walk through it step by step.

**Step 1:** You're standing on the equal-lightness surface for lightness = 50. You have access to many colors — the medium red, the medium green, the medium gray, all of them.

**Step 2:** For each color on this surface, ask: what is the geodesic distance from black to this color? Geodesic distance = shortest path through the full 3D color space, measured in perceptual cost units.

**Step 3:** Black is not on this surface — black has lightness = 0, this surface has lightness = 50. So you're measuring distances from a point *outside* the surface to points *on* the surface. That's fine — geodesic distance in the full 3D space doesn't care about surfaces.

**Step 4:** Find the color on this surface that has the **smallest** geodesic distance to black. That color is the neutral point.

---

## Why Does That Pick Out Gray?

Intuitively: gray is the "most direct" path from black toward brightness. To get from black to a vivid red at medium lightness, you have to travel both "upward" in brightness and "sideways" in color — you're taking a detour through color territory. To get from black to a medium gray at the same lightness, you travel almost straight up in brightness, with no sideways detour.

The geodesic distance to black is shortest for the color that requires the least detour — and that's the gray, because gray sits on the most direct route from black through the lightness levels.

*Analogy: imagine a highway from a city center (black) outward. The equal-lightness surface is a ring road at a fixed distance from the center. The neutral point is where the highway intersects the ring road — the spot on the ring that required the least total travel from the city center. Every other point on the ring road is reachable, but only by also driving sideways off the main highway.*

---

## Why Is This Better Than Schrödinger's Approach?

Schrödinger said: the neutral axis is where the achromatic stimuli live — the lights that activate your cones in the "white" ratio. To use his definition you need to know:

- What your adaptation state is (what your visual system currently calls "white")
- The spectral sensitivities of the three cone types
- The spectral power distribution of the reference illuminant

That's a lot of external biology and physics. None of it comes from the metric.

Bujack's definition needs only one thing: the perceptual metric — the function that tells you how different any two colors look. Everything else is derived. No cone biology. No illuminant. No adaptation state baked in.

This is the geometric equivalent of defining "north" by the shape of the gravitational field rather than by consulting a magnetic compass — intrinsic rather than extrinsic.

---

## The Full Picture in One Sequence

1. The perceptual metric exists — it assigns a tiny perceptual cost to every tiny step in color space.
2. Integrating that metric along a path gives the perceptual length of that path.
3. Minimizing over all paths from black to a color gives the **geodesic distance** from black to that color.
4. That geodesic distance is defined to be **lightness**.
5. Colors sharing the same lightness value form an **equal-lightness surface** — a 2D sheet in color space.
6. On any one of those sheets, the color with the **shortest geodesic distance to black** is the **neutral point** for that sheet.
7. Connect all the neutral points across all the equal-lightness surfaces and you get the **neutral axis** — the gray spine.
8. Saturation is then how far you are from that neutral axis, within your surface.
9. Hue is which direction around that neutral axis you sit.

Every step derives from the metric and nothing else. That's the whole program.

## Human

In terms of hue is giving in radians is giving in polar coordinates so it's a vector and an angle. What is the vector would have to be a color? What is that vector that is measured from to get the ang

## Assistant

**Clarifying**

Exactly the right question to ask — and the answer exposes something that Schrödinger's framework handles somewhat awkwardly.

---

## The Setup: Polar Coordinates on the Equal-Lightness Surface

You're on a 2D equal-lightness surface. You've found the neutral point — call it **N** — the gray dot at the center of that surface (closest to black, as established). That neutral point is your **origin**.

From any other color **C** on that surface, you can define:

- **Saturation** = the geodesic distance from N to C (the radial coordinate — how far out you are)
- **Hue** = the angle that describes which direction from N you had to travel to reach C

In standard polar coordinates that's exactly **(r, θ)** where r is saturation and θ is hue. So yes — hue is an angle in radians, measured in the 2D equal-lightness surface, centered on the neutral point.

---

## Your Question: What Is the Vector? What Is the Reference Direction?

In ordinary polar coordinates on a flat 2D plane, you measure the angle θ relative to a reference direction — conventionally the positive x-axis. The angle is between that reference ray and the ray from the origin to your point.

On the equal-lightness surface you have the same structure, but you immediately hit a problem:

**The equal-lightness surface has no natural x-axis.**

The neutral point N is geometrically well-defined — Bujack's framework gives it to you unambiguously. But there is no geometric object in the metric that says "this direction is zero degrees." The metric tells you distances. It does not come with a compass.

So to actually assign a numerical hue angle, you need to **pick a reference direction arbitrarily** — choose one color on the surface and declare it to be θ = 0. Every other hue is then measured as an angle relative to that anchor.

*Analogy: you've established the center of a clock face (the neutral point) but the metric gives you no "12 o'clock" position. You have to nail one down by convention.*

---

## What Gets Chosen in Practice?

In actual color systems, the reference direction is chosen by convention, not derived from the metric. In most standard color spaces it ends up being something like:

- The direction toward **red** (in CIELAB, the positive a* axis — the red direction — is the conventional zero)
- Or the direction toward **yellow**

This choice is entirely external to Schrödinger's geometric program. It's the one place where the "everything from the metric alone" promise quietly breaks down — you need one external anchor to turn a directionless angle into a numbered angle.

---

## But Here's the Deeper Point About the "Vector"

You asked: *what is the vector?* Meaning — in polar coordinates (r, θ), r is a scalar distance, but θ requires a reference vector to measure against. What is that reference vector made of?

The answer is: **it's a color.**

Specifically, the reference direction is defined by picking a specific color on the equal-lightness surface and declaring it the zero-angle anchor. The "vector" from N to that anchor color is your reference ray. Every other color's hue angle is measured relative to that ray.

So the full polar coordinate description of any color C on the surface is:

- **Origin**: the neutral point N (a color — the gray on this surface)
- **Reference ray**: from N toward the anchor color (conventionally red or some other agreed-upon hue)
- **r**: geodesic distance from N to C → this is saturation
- **θ**: angle between the reference ray and the ray from N to C → this is hue

Both the origin and the reference direction are colors. The coordinate system lives entirely inside color space — it's just that one of its defining elements (the reference ray direction) has to be fixed by convention.

---

## Why the Equal-Lightness Surface Has No Intrinsic Zero Direction

This is worth sitting with, because it's a genuine geometric fact, not a gap in the theory.

The equal-lightness surface is a 2D Riemannian (or Finsler) manifold. Its metric tells you distances between points. But a metric alone — even a perfectly specified one — does not define a preferred direction. Distance is isotropic in the sense that the metric doesn't "point" anywhere. It's like knowing all the road distances between cities but having no compass — you can reconstruct the map up to a rotation, but not the absolute orientation.

To get a fully numerical hue angle out of geometry alone, you'd need an additional geometric structure — something like a **preferred vector field** on the surface, or a **parallel transport** frame anchored somewhere. Neither exists in Schrödinger's framework or in Bujack's extension of it.

So hue-as-angle is always defined **up to a global rotation** by pure geometry. The actual number you call "red = 0°" or "red = 25°" is a calibration convention, not a geometric truth.

What *is* geometrically meaningful — and fully metric-intrinsic — is the **angular difference between two hues**: the angle between the ray to color C1 and the ray to color C2, both emanating from N. That relative angle doesn't depend on where you put your zero. Two colors separated by 90° of hue are geometrically 90° apart regardless of convention.

---

## Summary

| Element | What It Is | How It's Defined |
|---|---|---|
| **Origin N** | The neutral point (gray) on the surface | Geometric — minimizes geodesic distance to black |
| **Radial distance r** | Saturation | Geometric — geodesic distance from N to C within the surface |
| **Reference ray** | The zero-angle anchor direction | **Conventional** — must be chosen externally; typically "toward red" |
| **Angle θ** | Hue | Geometric relative to the reference ray — but the ray itself is a convention |
| **Angular differences** | Hue separation between two colors | Fully geometric — convention-independent |

The honest answer to your question is: the reference vector is a color, it points from the neutral gray toward an arbitrarily chosen anchor hue, and its absolute direction is the one element of Schrödinger's entire geometric program that cannot be derived from the metric alone.

## Human

That's what I thought it had to be. I just didn't know how that color was picked. Seems like it's picked to be red as convention. So how do you tell which is truly red and which is a little bit of r in it? Or I mean a little bit of g in it. A little bit of r in it. Is it just r256 g0b0?

## Assistant

**Clarifying**

Great question — and it cuts right to the heart of a subtle but important distinction. The short answer is: no, it's not R=255 G=0 B=0. That would be a hardware number, not a perceptual fact. Here's why that matters and how "red" is actually anchored.

---

## The Problem With R=255 G=0 B=0

RGB values are **device-dependent**. R=255 G=0 B=0 on your monitor means "drive the red phosphor/LED at full power and the others at zero." But:

- Your monitor's red LED peaks at roughly 630nm
- A different monitor's red LED peaks at 615nm
- A laser at 700nm is also "red" but has no RGB representation that's universal
- A paint called "cadmium red" reflects a broad spectrum centered around 620nm

None of these are the same physical stimulus. They all look red. So "redness" can't be anchored to a device value.

*Analogy: saying red = R255 G0 B0 is like saying "north = the direction my compass points" — works locally, fails globally, and silently depends on your specific hardware.*

---

## How Red Is Actually Anchored: The CIE System

The international standard anchors colors to **physical wavelengths of light and human cone responses**, not device values. The framework is called the **CIE color matching functions**, established in 1931.

Here's how it works:

**Step 1 — Measure real human observers.**
CIE ran experiments where observers looked at a monochromatic (single wavelength) light and adjusted mixtures of three reference primaries until the mixture looked identical to the test light. This was done across the full visible spectrum. The result is three functions — called x̄, ȳ, z̄ — that describe how an average human visual system responds to each wavelength.

**Step 2 — Define a device-independent color space.**
Every physical light source has a spectrum — a distribution of power across wavelengths. You integrate that spectrum against the three color matching functions and get three numbers (X, Y, Z). These are the **CIE XYZ tristimulus values** — they describe the color as the human visual system experiences it, completely independent of any display device.

**Step 3 — Anchor hue zero to a specific XYZ location.**
In CIELAB (the standard perceptual color space), the coordinate system is built around a reference white point. The a* axis (positive = red direction, negative = green direction) and b* axis (positive = yellow, negative = blue) define the hue plane. Red is defined as the positive a* direction — which corresponds to the spectral region around **~620–700nm dominant wavelength**, derived from the cone responses, not from any display.

---

## So What Counts as "Pure Red"?

In the perceptual geometry, the "pure red" anchor — the conventional zero of the hue angle — corresponds to colors whose XYZ coordinates place them on the positive a* axis in CIELAB with b* = 0. 

In terms of physical light, that's approximately a dominant wavelength of around **700nm** — the long-wavelength end of the visible spectrum where the L cone (red-sensitive) is firing strongly and the M cone (green-sensitive) response has dropped off.

But here's the key nuance: **no real surface or light is perfectly on that axis.** Every physical red has some b* component (some yellow or blue mixed in). "Pure red" in the hue-angle sense is a mathematical direction in the color space — a limiting case that real objects approximate but never perfectly achieve.

---

## Your Real Question: How Do You Tell Pure Red From "A Little G In It"?

In the perceptual geometry framework, you tell them apart by their **hue angle** — but also by how far they deviate from the reference axis:

- Perfect red: hue angle θ = 0°, any saturation r, b* = 0
- Red with a little green: hue angle θ slightly positive (toward yellow), because adding green pulls you toward the yellow quadrant (positive b*)
- Red with a little blue: hue angle θ slightly negative (toward magenta)

So "a little G in it" doesn't mean G=10 in RGB. It means your color's position in the equal-lightness surface has rotated slightly away from the zero-angle reference ray, toward the yellow direction.

The hue angle tells you the mixture. The saturation tells you how vivid it is. Lightness tells you how bright. Together they fully specify the color — and the hue angle is doing the work of distinguishing "pure red" from "red-orange" from "red with a green tint."

---

## The Hierarchy of "Redness"

| What It Is | How Red Is Defined | Problem |
|---|---|---|
| R=255 G=0 B=0 | Device RGB | Device-dependent — different on every screen |
| sRGB (255,0,0) | Standardized RGB with a defined white point and primaries | Better — but still a display standard, not perceptual |
| CIE XYZ | Tristimulus values from cone responses | Device-independent, physically grounded |
| CIELAB a*>0, b*=0 | Perceptual red axis, referenced to a white point | Perceptually uniform, metric-intrinsic |
| Dominant wavelength ~700nm | Pure spectral red | Physical ground truth — but not what most "reds" are |

The perceptual geometry Schrödinger and Bujack work in operates at the CIELAB / CIE XYZ level — where "red" means a specific direction in a space defined by human cone responses, not by display hardware. R=255 G=0 B=0 in sRGB is a reasonable practical approximation of that direction on a calibrated display, but it's downstream of the real definition, not the source of it.

## Human

Explain more about a star and b Star

## Assistant

**Elaborating**

Good — a* and b* are worth a full explanation because they're doing something genuinely clever that most people never unpack.

---

## Where a* and b* Come From: The Opponent Color Model

First, why two axes and not three? Because the visual system doesn't send raw cone signals to the brain. It computes **differences** between cone signals before anything reaches conscious perception. This is called **opponent processing**, and it's wired in at the retinal ganglion cell level.

The three opponent channels are:

**Luminance channel:** L cone + M cone (roughly red + green = brightness). This becomes lightness L* in CIELAB.

**Red-green channel:** L cone minus M cone. When L fires more than M, you see red. When M fires more than L, you see green. You literally cannot perceive red and green simultaneously in the same location — they oppose each other.

**Blue-yellow channel:** S cone minus (L+M). When S dominates, you see blue. When L+M dominates over S, you see yellow. Again, mutually exclusive — you cannot see bluish-yellow.

This is why there's no such thing as a "reddish-green" or a "bluish-yellow" — those combinations cancel at the neural hardware level before you're even aware of them. The color wheel isn't arbitrary; it's the topology of opponent processing.

*Analogy: it's a push-pull differential amplifier. The cone signals are the single-ended inputs. The opponent channels are the differential outputs. You're throwing away common-mode (absolute level) and keeping only the difference signal — exactly what a diff pair does in a SerDes front end.*

---

## The CIELAB Construction

CIELAB takes the raw CIE XYZ tristimulus values and transforms them into a space that's approximately **perceptually uniform** — equal distances in the space correspond to approximately equal perceived color differences.

The three coordinates are:

**L\*** — perceptual lightness. Runs from 0 (black) to 100 (reference white). Nonlinear — roughly cube-root of luminance Y, because human brightness perception is compressive (diminishing returns — the same issue Bujack is fixing at a deeper level).

**a\*** — the red-green opponent axis. Positive a* = red direction. Negative a* = green direction. Zero a* = neither red nor green — you're on the neutral axis in the red-green dimension.

**b\*** — the blue-yellow opponent axis. Positive b* = yellow direction. Negative b* = blue direction. Zero b* = neither blue nor yellow.

Both a* and b* are zero at the neutral axis — the gray spine. That's the definition of gray in this framework: no red-green signal and no blue-yellow signal. Pure luminance, nothing else.

---

## What the a*b* Plane Looks Like

At any fixed L* value, you have a 2D plane with a* on one axis and b* on the other. This is exactly the equal-lightness surface discussed earlier. The neutral point is at (a*=0, b*=0). Colors radiate outward from that center:

- Due east (positive a*, zero b*): pure red direction
- Due west (negative a*, zero b*): pure green direction  
- Due north (zero a*, positive b*): pure yellow direction
- Due south (zero a*, negative b*): pure blue direction
- Northeast: orange (red + yellow)
- Northwest: yellow-green (green + yellow)
- Southeast: magenta (red + blue)
- Southwest: cyan (green + blue)

The hue angle θ is literally the arctangent of b* divided by a* — standard polar angle from the positive a* axis. The saturation (called chroma C* in CIELAB) is the straight-line distance from the origin — the square root of (a*² + b*²).

So when you asked earlier about the reference vector — it's the positive a* axis. The "vector" pointing from the neutral gray origin toward pure red. That's the θ=0 anchor.

---

## Why the Axes Are Scaled the Way They Are

A critical feature: **a* and b* are not symmetric in scale.** The yellow-blue axis (b*) spans a wider range than the red-green axis (a*) for typical real-world colors. This is because:

- The S cone (blue-sensitive) has far fewer cells than L and M cones — roughly 5-10% of the total
- The yellow-blue opponent channel has lower sensitivity and coarser spatial resolution than red-green
- Real surfaces and lights tend to have more variation in the yellow-blue direction than the red-green direction at equivalent saturation levels

The result is that the a*b* plane is not a circle for real-world colors — it's more of an irregular shape, wider in the b* direction for high-chroma yellows, and the available gamut is asymmetric. A maximally saturated yellow sits much further from the neutral axis than a maximally saturated blue at the same lightness level.

*Analogy: two noise channels in a measurement system with different noise floors. The channel with lower sensitivity (S cone / b* axis) needs larger signals to register the same SNR. The dynamic range is different on each axis.*

---

## The Nonlinearity and Why It Matters

Both a* and b* are computed from XYZ via a cube-root compression (the same compression applied to get L*). Specifically:

$$a^* = 500\left[\left(\frac{X}{X_n}\right)^{1/3} - \left(\frac{Y}{Y_n}\right)^{1/3}\right]$$

**Symbol definitions:**
- $a^*$ : red-green opponent coordinate
- $X, Y$ : tristimulus values of the color being described
- $X_n, Y_n$ : tristimulus values of the reference white (your white point)
- $(\cdot)^{1/3}$ : cube root compression — models the compressive nonlinearity of cone response

**What this actually means:** You're taking the cube root of how much X you have relative to white, and how much Y you have relative to white, and differencing them. The cube root is there because cone responses compress — doubling the physical light intensity does not double the perceived difference. This is the same diminishing returns that Bujack's non-Riemannian metric is trying to handle more rigorously. CIELAB bakes in a fixed cube-root approximation; Bujack's framework says the true compression is more complex and spatially varying.

Similarly for b*:

$$b^* = 200\left[\left(\frac{Y}{Y_n}\right)^{1/3} - \left(\frac{Z}{Z_n}\right)^{1/3}\right]$$

**Symbol definitions:**
- $b^*$ : blue-yellow opponent coordinate
- $Z, Z_n$ : Z tristimulus value of the color and reference white respectively
- The 200 scaling factor (vs 500 for a*) reflects the lower sensitivity of the blue-yellow channel

---

## The White Point Dependency — a Hidden Variable

Both a* and b* are computed relative to a **reference white** (X_n, Y_n, Z_n). This is the color your visual system is adapted to — what it currently calls "white." Change the illuminant and the whole coordinate system shifts.

This is chromatic adaptation — the same mechanism that makes a white piece of paper look white under both noon sunlight (bluish) and incandescent light (yellowish). Your visual system recalibrates its white point, and the opponent channels recenter around the new reference.

In CIELAB, you pick a standard white point (D65 for daylight, D50 for print industry) and fix it. The a* and b* values are then defined relative to that fixed white.

This is the external biological fact that Bujack's geometric neutral axis definition elegantly sidesteps — because her definition derives the neutral axis from the metric shape alone, without requiring you to specify a white point. The metric already encodes how the visual system is adapted, implicitly. The white point is baked into the metric rather than specified separately.

---

## Summary

| Coordinate | Opponent channel | Zero means | Positive means | Negative means |
|---|---|---|---|---|
| **L\*** | Luminance (L+M cones) | Black | Bright white | — (L* has no negative) |
| **a\*** | Red-green (L minus M) | No red/green signal | Red | Green |
| **b\*** | Blue-yellow (S minus L+M) | No blue/yellow signal | Yellow | Blue |

The a*b* plane at any fixed L* is the equal-lightness surface. The origin (0,0) is the neutral point — geometrically gray. Hue is the angle from the positive a* axis. Chroma/saturation is the distance from the origin. Schrödinger's entire geometric program — lightness, neutral axis, saturation, hue — maps directly onto L*, the origin, C*, and θ respectively. The a* and b* axes are the opponent-channel hardware that makes the geometry physically meaningful.
