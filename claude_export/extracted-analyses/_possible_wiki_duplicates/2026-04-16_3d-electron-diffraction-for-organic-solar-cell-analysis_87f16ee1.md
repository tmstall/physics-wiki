---
source: claude_export
conversation_uuid: 87f16ee1-31a2-42ce-b404-6d6815809620
title: "-> 3D electron diffraction for organic solar cell analysis"
created_at: 2026-04-16T15:46:49.421985Z
updated_at: 2026-05-10T23:52:22.977056Z
tier: A
score: 255
n_messages: 2
---

# -> 3D electron diffraction for organic solar cell analysis

## Human

Analyze this paperIrene Kraus et al, 3D electron diffraction—the missing slice completing nanoscale analysis of organic solar cells in TEM, Nature Communications (2026). DOI: 10.1038/s41467-026-70690-y

Journal information: Nature Communications

## Assistant

**Fetching**

**Analysis** v3.4.9

---

# The Electron Microscope Finally Gets a Full Map — Now It Can See *and* Measure the Soul of an Organic Solar Cell

**One sentence:** By adding elastically-filtered 3D electron diffraction to the TEM toolbox, a single instrument can now simultaneously image the nanoscale morphology of an organic solar cell *and* extract the same bulk crystal-structure data that used to require a separate synchrotron beamline.

---

## 1. Big-Picture Context

Organic solar cells (OSCs) are built around a conceptually simple idea: blend a donor and an acceptor molecule into a thin film so intimately that excitons (bound electron-hole pairs created by light) are never far from a junction where they can split. The catch is that the *precise nanoscale arrangement* of those molecules — how they pack, which face they present to the substrate, how large the crystalline grains are — controls every efficiency-determining process: light absorption, exciton dissociation, charge separation, and carrier collection. Engineering that arrangement is more alchemy than science if you can't measure it.

OSC power conversion efficiencies now exceed 20%, largely from molecular design advances, but further gains increasingly require knowing *where* the ordered crystallites are and *how* they're oriented at the 10–100 nm scale — simultaneously with the nanomorphology. The field has been stuck in an awkward situation: X-ray techniques give you the crystal structure but spatially average over millions of domains; electron microscopy gives you nanoscale images but had never been able to extract the equivalent crystal-structure statistics. You needed both experiments, on separate instruments, hoping nothing changed between them.

Researchers at FAU Erlangen-Nürnberg, with partners from Forschungszentrum Jülich and DESY in Hamburg, now show that electrons alone can achieve both — the spatially averaged structural picture *and* the local real-space image — within a single TEM session. The "missing slice" of the paper's title is a literal reference to a gap in 3D reciprocal-space coverage that the new technique closes, but it's also a metaphor for the information gap that has plagued OSC characterization for two decades.

The performance of OSC devices is inherently linked to structural organization and nanomorphology: large domains facilitate charge collection but limit exciton dissociation, a contradiction alleviated by highly anisotropic domains showing efficient exciton dissociation and charge collection simultaneously. That specific physics — anisotropy at the domain scale — is exactly what the new technique finally lets you measure locally.

---

## 2. Necessary Background Crash Course

**Bulk heterojunction (BHJ) morphology.** The active layer of an OSC is a bicontinuous interpenetrating network of donor-rich and acceptor-rich domains, each 10–100 nm wide. The molecules within those domains partially crystallize. The orientation of those crystals matters enormously: a molecule presenting its flat aromatic face toward a neighboring molecule (face-on) supports vertical charge transport; edge-on orientation supports lateral transport. Analogy: it's the difference between stacking poker chips (face-on, good for current flowing perpendicular to the film — what you want in a solar cell) vs. standing them on edge.

**GIWAXS — the incumbent.** Grazing-Incidence Wide-Angle X-ray Scattering fires a pencil of X-rays at the film at a nearly-flat angle (~0.1°), and the diffracted intensity pattern on a 2D detector is converted to a map in reciprocal space (momentum transfer **q**). From the position of diffraction rings/spots you extract lattice spacings; from their width (Scherrer analysis) you get crystallite size; from their azimuthal spread you get degree of alignment (mosaicity). GIWAXS effectively captures ensemble-averaged structural information but does not provide real-space images of nanomorphology or local structural heterogeneities. It also has a "missing wedge" along the out-of-plane axis due to the finite grazing incidence angle — some crystallite orientations are geometrically inaccessible. Analogy: GIWAXS is like measuring the average tile size in a mosaic by looking at it from 100 meters away — you get statistics, not the individual tiles.

**3D Electron Diffraction (3D ED).** Rather than a fixed X-ray beam, you tilt your TEM sample through a range of angles (typically ±75°) while collecting a diffraction pattern at every tilt step. The stack of 2D diffraction slices is computationally assembled into a 3D reciprocal-space volume. Originally developed for structural analysis of submicron-sized crystals too small for conventional single-crystal X-ray diffraction, 3D ED has revolutionized crystallography, with automated data acquisition and ab initio structure determination routines enabling high-throughput workflows for beam-sensitive materials such as metal-organic frameworks and pharmaceuticals. Applying it to *polycrystalline, partially ordered* films — what OSCs are — is the new move here. Analogy: instead of X-ray tomography (GIWAXS), you're doing electron-beam CT — tilt the patient, collect projections, reconstruct the 3D volume.

**The elastic filtering requirement.** Organic materials scatter electrons both elastically (Bragg diffraction, the signal you want) and inelastically (energy loss, noise). An energy filter (a spectrometer in the electron column) selects only the zero-loss electrons, dramatically improving signal-to-noise. Without it, the diffraction rings from organic films are too smeared to be quantitative. This is why prior attempts at 3D ED on OSCs failed.

**Reciprocal space and the missing wedge.** Imagine a 3D sphere of radius proportional to a spatial frequency. Every crystal plane maps to a point in that sphere. GIWAXS has a missing wedge near the film-normal axis because the grazing geometry can't physically access those angles. 3D ED has a different-shaped missing wedge due to limited tilt range, while GIWAXS has a missing wedge from Ewald sphere curvature — the two methods' blind spots are geometrically complementary. This is the "missing slice" headline: 3D ED can access the in-plane directions that GIWAXS cannot.

---

## 3. Core Technical Explanation

**The model system.** They work primarily on DRCN5T:PC₇₁BM — a small-molecule donor blended with a fullerene acceptor, solvent-vapor annealed to develop crystallinity. This system is well-characterized by prior GIWAXS at both lab and synchrotron sources, giving the team a ground truth to validate against. They also demonstrate the technique on P3HT:PC₇₁BM, the classic polymer:fullerene workhorse system, to show generality.

**The experimental workflow.** They prepare plan-view TEM samples (thin film lifted off its substrate onto a TEM grid — no FIB damage, large sample area). They acquire a tilt series in the TEM with an energy filter selecting zero-loss electrons at every tilt angle. The key technical step: *stitching* multiple overlapping 3D ED datasets together, because a single tilt series only covers a small sample area. Combining many datasets gives the large-area statistical sampling GIWAXS enjoys, while preserving local spatial registration.

**Reciprocal-space reconstruction.** Each diffraction pattern at tilt angle α is a 2D slice through 3D reciprocal space. They create a new orthogonal data volume expressed in cylindrical coordinates and fill aligned raw data into it, then transform back via polar transformation to obtain a full 3D reciprocal space volume, normalizing by a unit data volume to account for the increased sampling density near the tilt axis. The result is a **qrz map** — a 2D projection of 3D reciprocal space comparable directly to GIWAXS output.

**Validation against GIWAXS.** Comparing qrz maps from 3D ED and GIWAXS reveals matching diffraction rings and reflections; the good agreement confirms that 3D ED yields structural information comparable to GIWAXS. The amorphous halo near qr ≈ 2 nm⁻¹ originates from PC₇₁BM, while sharp rings with azimuthal segments stem from DRCN5T crystallites. Quantitative peak positions, coherence lengths (grain sizes via Scherrer analysis), and mosaicity values match between the two methods to within measurement uncertainty.

**The correlative payoff.** Here's where 3D ED goes beyond GIWAXS. Because the same sample area that gave you the diffraction data is sitting in the TEM, you can immediately follow up with:
- **HAADF-STEM imaging** — dark-field image showing domain morphology at ~5–20 nm resolution
- **4D-SCED (scanning confocal electron diffraction)** — maps local crystallite orientation pixel-by-pixel across the film
- **EELS/EDX** — chemical mapping (which domain is donor, which is acceptor)

By combining 3D ED with complementary analytical and diffraction-imaging methods, they directly reveal how nanomorphology and molecular orientation coincide in the BHJ film — an insight that pure GIWAXS, lacking real-space information, cannot provide. Each DRCN5T "leaf" domain (~80 nm long) contains multiple smaller crystallites (~20 nm per Scherrer analysis), indicating a mosaic structure within domains, with grain boundaries that relate to trap states and charge carrier recombination.

That last sentence is the key physics result: the "leaf-shaped" domains you see in TEM images are not single crystals — they're internally mosaic, containing several 20 nm crystallites with slightly misoriented stacking. Those grain boundaries are carrier traps. You couldn't see this with GIWAXS alone.

**True in-plane access.** 3D ED is more radiation dose-efficient and provides access to the degree of crystallite alignment — particularly out-of-plane — capturing inclined crystallites that deviate from strict edge-on or face-on orientation. Because the electron beam probes in transmission rather than at grazing incidence, the in-plane axis is fully accessible, eliminating the GIWAXS blind spot for edge-on crystallites.

---

## 4. What's Genuinely New or Clever

**Trick 1: Elastic filtering applied to polycrystalline organic films.** This sounds incremental but it isn't. The energy filter had previously been required for single-crystal structure determination. Applying it systematically to a *statistical* ensemble of crystallites in a disordered polymer/small-molecule blend film — and showing you still get quantitative GIWAXS-equivalent data — is a methodological bridge nobody had crossed. The beam damage management (controlled dose, stitching many small acquisitions across the sample rather than hammering one spot) is the engineering breakthrough underneath the physics.

**Trick 2: Correlative multimodal registration in a single instrument.** Electron microscopy now uniquely combines averaged structural information with local imaging, diffraction imaging, and chemical analysis in a single instrument — what they call multimodal microscopy, allowing direct linking of molecular texture to local order and composition within one experiment. In the signal-integrity world, you'd call this having a logic analyzer, oscilloscope, and TDR on the same probe simultaneously. You can actually correlate what you measure in each domain to the same domain's crystal structure, grain size, and chemical composition — without ever unloading the sample.

---

## 5. Limitations & Open Questions

**The missing wedge problem isn't gone, just different.** Both 3D ED and GIWAXS have missing wedges in reciprocal space — they're just in complementary regions. The paper honestly acknowledges this and shows overlay plots where both blind spots are visible. The full solution would require combining both methods, which is now tractable given that the data formats are directly comparable.

**Beam damage is still the elephant in the room.** Organic films are exquisitely sensitive to electrons. The team mitigates this carefully, but quantitative thresholds for "safe" total dose on arbitrary OSC materials haven't been established. Different molecular systems (non-fullerene acceptors like Y6, for instance) may require entirely different dose protocols. The >20% efficiency OSCs use non-fullerene acceptors, and those haven't been demonstrated here.

**The lab-scale energy filter requirement.** The strong inelastic scattering in OSCs necessitates elastic filtering, which is not always available. Energy filters are expensive add-ons; not every OSC characterization lab has one. This limits immediate adoption.

**Sample area statistics.** GIWAXS with a synchrotron beam samples millimeters² of film in seconds, achieving excellent powder-averaging statistics. 3D ED stitches many small-area datasets, but the sampling is still inherently local — and the stitching is computationally non-trivial. For highly heterogeneous films, GIWAXS will remain more statistically robust.

**P3HT:PC₇₁BM is the "easy" validation system.** P3HT has been studied for 20 years. Demonstrating 3D ED on a cutting-edge non-fullerene system with a complex multi-ring acceptor (PM6:Y6 type) would be a more demanding and relevant test for state-of-the-art device work.

---

## 6. Three Crystallized Takeaways

1. **Electrons can now do what used to need X-rays.** Elastically-filtered 3D ED extracts the same crystal structure statistics (lattice spacings, grain sizes, texture) from organic solar cell films that GIWAXS requires a synchrotron for — but inside the TEM that was already imaging the film.

2. **The "leaf-shaped domains" aren't single crystals — they're mosaics with internal grain boundaries that trap charge carriers.** This microscopic insight was invisible to GIWAXS and is directly relevant to understanding efficiency losses in real devices.

3. **The TEM is now a complete characterization station for OSCs.** Morphology, crystal structure, chemical composition, and local orientation — all from one sample, one session, one instrument, without cross-contamination between the measurements.

---

## 7. Detailed Summary & Explanation

**What problem is being solved?**
Organic solar cell performance is tightly coupled to molecular packing at the 10–100 nanometer scale. The dominant structural characterization tool has been GIWAXS (Grazing Incidence Wide-Angle X-ray Scattering), which gives excellent crystal-structure statistics by diffracting X-rays off the film and analyzing the ring/spot pattern in reciprocal space — the Fourier-transform domain where spatial frequencies map to momentum transfer. The problem is that GIWAXS spatially averages over millions of domains and cannot tell you *where* a given crystal orientation occurs in the film, or whether a visually distinct domain (seen in electron microscopy) has a different structure from its neighbor.

Electron microscopy could image the nanomorphology beautifully, but conventional electron diffraction in TEM only samples one 2D slice of reciprocal space — the slice perpendicular to the beam. To get full 3D reciprocal space coverage (equivalent to GIWAXS), you need to tilt the sample and record diffraction at every angle. That's 3D ED. The technique was mature for *single crystals* of inorganic materials, but organic films posed two extra challenges: (a) they're radiation-sensitive, requiring ultra-low electron doses, and (b) they're polycrystalline with a distribution of crystal orientations, so statistical sampling was always the concern.

**What the team actually did:**
They grew DRCN5T:PC₇₁BM blend films (the donor DRCN5T is a small organic molecule, the acceptor PC₇₁BM is a buckminsterfullerene derivative) via solvent vapor annealing — a well-controlled process that produces a reproducible crystalline texture. They prepared plan-view TEM samples by lifting the film off its substrate, avoiding the cross-sectional FIB preparation that introduces ion beam damage and limits sample area.

In the TEM equipped with an in-column energy filter (zero-loss elastic filtering), they recorded tilt series: acquire a diffraction pattern, tilt by one degree, repeat, across roughly ±75°. Multiple overlapping tilt series were acquired across the sample to build up statistics. These were computationally assembled — via a cylindrical-coordinate reconstruction followed by polar transformation — into a full 3D reciprocal-space volume.

The qrz map (a 2D projection of 3D reciprocal space in radial and out-of-plane coordinates, directly comparable to a GIWAXS detector image) from 3D ED matched the synchrotron GIWAXS data quantitatively: the same peak positions (lattice spacings), peak widths (coherence lengths, i.e., grain sizes), and azimuthal spread (mosaicity, i.e., how well-aligned the crystallites are). The key quantitative metrics were all within a few percent of each other.

**What the new capability revealed:**
Then they used the same sample area for HAADF-STEM imaging and 4D-SCED (scanning confocal electron diffraction), which maps the local crystallite orientation pixel-by-pixel. Overlaying all three datasets: the leaf-shaped DRCN5T domains visible in STEM images each contain multiple (~20 nm) crystallites with slightly different orientations — a mosaic structure. The mosaic grain boundaries inside what looked like single uniform domains are exactly where charge carriers get trapped and recombine before reaching the electrodes. GIWAXS would have reported the averaged grain size of ~20 nm and the domain size of ~80 nm, but couldn't link those two length scales to the same physical region, nor confirm whether they coexisted in the same leaf or came from different sample regions.

They validated generality on P3HT:PC₇₁BM — the polymer:fullerene system that defined the field for 15 years — showing the same agreement with GIWAXS and the same capacity for correlative imaging.

**Why the "missing slice" title?**
GIWAXS has a geometric blind spot (missing wedge) in reciprocal space near the film normal, because the grazing incidence geometry can't physically reach those scattering angles. Plan-view TEM electron diffraction (single beam direction) has the opposite problem — it only sees the in-plane slice. 3D ED fills in the entire sphere, and its missing wedge (from finite tilt range) happens to complement GIWAXS's — the two together would cover all of reciprocal space. More poetically, 3D ED was "the missing slice" completing the TEM characterization toolkit, which already had imaging, chemical mapping, and local diffraction, but lacked the globally-averaged crystal structure information.

---

## 8. Shorter Summary

Organic solar cells work better when their nanoscale crystal structure is optimized — but measuring that structure used to require a synchrotron X-ray experiment that couldn't tell you *where* specific crystals were in the film. This paper shows that elastically-filtered 3D electron diffraction — tilting a film sample in a transmission electron microscope while collecting diffraction patterns at every angle — extracts exactly the same crystal structure data (lattice spacings, grain sizes, alignment statistics) as grazing-incidence X-ray scattering, with quantitative agreement validated against both lab and synchrotron X-ray sources. The payoff is that the same TEM session that delivers crystal structure data can immediately deliver nanoscale images, local chemical maps, and spatially-resolved crystal orientation maps of the *same sample area*. Using this combined toolkit, they discover that the visually distinct "leaf-shaped" domains in their model OSC film are internally mosaic — composed of multiple misaligned sub-crystallites with grain boundaries that act as charge carrier traps. The technique closes the last gap in all-electron TEM characterization of organic solar cells, eliminating the need for a separate X-ray experiment.
