---
tags: [papers, perception, geometry, foundations]
last_updated: 2026-08-04
status: analysis-ingest
related_papers: [weak-values]
source_analysis: "claude_export/extracted-analyses/2026-06-09_color-space-has-potholes_0a5c3ef4.md"
---

# Non-Riemannian Color Geometry (Bujack et al.)

**One-line summary:** Los Alamos work rebuilds Schrödinger’s hue/saturation/lightness on a non-Riemannian perceptual metric — fixing Bezold–Brücke-type hue paths, lightness ambiguity, and a rigorous gray-axis definition after proving color space violates Riemannian triangle inequality.

## Key claims and results

- Prior result (2022 PNAS lineage): perceptual color differences show diminishing returns → non-Riemannian geometry.
- This paper: redefines hue, saturation, lightness with correct non-Riemannian geodesics.
- Neutral (gray) axis defined intrinsically as locus of colors closest to black on equal-brightness surfaces.
- Experimental validation that the patched geometry matches human judgments better than Schrödinger’s original ruler.

## Physical intuition

Color difference is a measurement problem, not a paint recipe. Schrödinger gave an elegant 1920s geometry, but he assumed a ruler that adds small steps into large ones. Human vision does not: ten small ΔE steps do not equal one big step. Once the metric is allowed to be non-Riemannian, the three classical color coordinates can be rebuilt without cracks — including a gray spine that was previously assumed rather than proved.

## Why “non-Riemannian” is the load-bearing word

In Riemannian geometry, small distances integrate cleanly into large ones along geodesics. Perceptual metrics fail that test: equal-step paths and straight-line large steps disagree (diminishing returns). Fixing hue paths (Bezold–Brücke shifts) and defining gray without an ad-hoc axis are consequences of **dropping** the Riemannian assumption, not of better color charts alone. The engineering lag is real: industrial ΔE formulas still smuggle near-Euclidean shortcuts even when the geometry paper is right.

## Limitations and assumptions

- Still a model of average human observers; individual / cultural variation remains.
- Analysis-based ingest; confirm experimental protocols on the CGF/primary paper.
- Engineering ΔE standards will lag pure geometry papers.
- Conceptual cousin to conditional measurement language in quantum optics ([[weak-values]]) only at the level of “geometry of observation,” not shared formalism.

## Connections

- Measurement / post-selection cousins in quantum optics: [[weak-values]] (conceptual only — different domain)
- Foundations / measurement culture: [[measurement-problem-threads]] (loose — perceptual metric ≠ quantum measurement problem)

## Source

- `claude_export/extracted-analyses/2026-06-09_color-space-has-potholes_0a5c3ef4.md`
