---
tags: [papers, microscopy, diffractive, compressive-sensing, optics]
last_updated: 2026-09-05
status: analysis-ingest
related_papers: [ultrafast-optics-and-solid-state-emitters, recycling-idler-quantum-superresolution]
source_analysis: "raw/analyses/2026-09-04_nodoi_25gpps-diffractive-microscope.md"
---

# 25 Gigapixel-per-Second Diffractive Microscope

**One-line summary:** Shared-objective multi-sensor array + engineered multi-copy PSF + compressive recon → 25.2 Gpx/s wide-field throughput; needs sparse samples; FOV expands beyond physical fill factor. Nature Photonics (nodoi in analysis).

## Key claims and results

- 6×8 array of 48 sensors shares one objective / tube lens; active silicon covers only ~22% of the image-plane hull — gaps are treated as designed erasures, not defects.
- Custom DOE in the Fourier plane engineers a 15-spot PSF so every sample point deposits light on multiple locations; triple-correlation design criterion accounts for the gapped sensor mask.
- Compressive reconstruction (TV + L1, shift-variant forward model with lens distortion) recovers the full field, including gap regions; effective FOV gain ≳5.4× beyond physical sensor coverage.
- Dark-field mode: ~3 μm resolution over ≳5.2 cm² at up to 120 fps with 4×4 binning → **25.2 GP/s** (~5× prior 3D-RAPID record); fluorescence mode lower throughput but functional (GCaMP pharyngeal pumping in many worms).
- Code and raw data released; demonstrations use sparse samples (*C. elegans* on dark backgrounds).

## Physical intuition

A conventional multi-camera microscope gives each sensor its own lens and stitches non-overlapping tiles. Here the array is one "super sensor" with known dead drives: the DOE is the erasure code, copying each object point into 15 placements so at least one copy hits live silicon. Reconstruction demixes the overlapping copies and fills holes by assuming the scene is sparse — mostly dark, signal in a small pixel fraction — the imaging analog of recovering a file that is 90% zeros from undersampled reads.

## Limitations and assumptions

- Sparsity is load-bearing: dense tissue, biofilms, or mostly filled scenes break compressive recovery.
- Headline 25.2 GP/s uses 4×4 binning; full-resolution throughput falls to ~6 GP/s under the same data-bus cap.
- Reconstruction is offline (~5 s/frame on RTX 3090), not closed-loop real-time.
- Peripheral aberrations / vignetting degrade corners; no 3D / optical-sectioning capability yet.
- 8-bit sensors may limit weak-signal fluorescence SNR.

## Connections

- Ultrafast / computational optics peers: [[ultrafast-optics-and-solid-state-emitters]]
- Peer imaging / superresolution thread: [[recycling-idler-quantum-superresolution]]

## Source

- `raw/analyses/2026-09-04_nodoi_25gpps-diffractive-microscope.md`
