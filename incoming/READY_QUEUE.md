# READY_QUEUE

staged_at: 2026-10-01
notes: Staged by Cowork `copy`. Wave 2026-09-05: 12 ingested + 1 skipped_duplicate (ErTe₃); 0 pending. Wave 2026-09-12: 4 copied to raw/analyses/ + verified (byte-size match), 0 pending (ingested 2026-09-12) — but the archive-move step could NOT run this pass (device_bash unreachable on this session due to the Windows-mount issue tracked since 2026-09-08); all 4 inbox originals remain in incoming/md/ root, not yet moved to incoming/md/archive/. Safe to re-run `copy` once device_bash is back — raw/analyses/ already has verified copies, so a re-run will correctly skip_exists on these 4 and just complete the archive move. Wave 2026-09-20: 7 copied to raw/analyses/ + verified (byte-size match) and archived to incoming/md/archive/ (rapid-orbital-decay-erassu-j060839, unconventional-materials-light-dark-matter-detection, entanglement-islands-page-curves-kerr-ads, lbt-yp part1of2, lbt-yp part2of2, zz-boson-pair-entanglement-higgs-decays, topology-of-the-universe); 0 pending (ingested 2026-09-20). The 4 files noted as stranded since 2026-09-12 (ultraheavy-dark-matter-levitated-magnet-polonaise, baryon-semileptonic-decays-polarization-entanglement, eccentric-massive-protobinary-core-merger, ch3oh-hcn-3i-atlas-outgassing) were skipped_exists again this run, per COPY.md's literal default (a skip leaves the inbox original in place, unarchived) — contrary to the prior note's expectation that a re-run would complete the archive move; COPY.md as written never archives on the skip_exists path. These 4 remain in incoming/md/ root, already byte-verified in raw/analyses/, awaiting either manual archiving or a `copy --force` re-run if that's the path wanted. Follow-up same session: hash-verified (sha256) all 4 stranded 2026-09-12-wave inbox originals (ultraheavy-dark-matter-levitated-magnet-polonaise, baryon-semileptonic-decays-polarization-entanglement, eccentric-massive-protobinary-core-merger, ch3oh-hcn-3i-atlas-outgassing) against their raw/analyses/ copies — all 4 matched byte-for-byte — then archived them to incoming/md/archive/ by hand at the user's request. incoming/md/ root is now fully empty. No status/row changes needed (all 4 were already `done`). Wave 2026-10-01: 20 copied to raw/analyses/ + verified (byte-size + sha256 match) and archived to incoming/md/archive/; 0 skipped_exists, 0 failed; 0 pending (ingested 2026-10-01).

| status | filename | staged_at | notes |
| --- | --- | --- | --- |
| done | 2026-08-18_doi-10.1038-s41550-026-02932-4_bottom-heavy-imf-hidden-mass-early-galaxies.md | 2026-08-22 | [[bottom-heavy-imf-early-galaxies]] |
| done | 2026-08-19_doi-10.1038-s41567-026-03382-5_time-domain-competing-cdw-ErTe3.md | 2026-08-22 | [[erte3-competing-cdw-time-domain]] |
| done | 2026-08-19_doi-10.1103-5pr6-5fmd_quantum-droplets-bose-fermi-mixture.md | 2026-08-22 | [[quantum-droplets-bose-fermi]] |
| done | 2026-08-19_eso2612a_s301-star-sensitive-to-spin-sgrA-star.md | 2026-08-22 | [[s301-sgra-spin-sensitive-star]] |
| done | 2026-08-20_arxiv-2607.20366_x2370-lightest-pseudoscalar-glueball.md | 2026-08-22 | [[x2370-pseudoscalar-glueball]] |
| done | 2026-08-20_doi-10.1038-s41467-026-76747-2_mmwave-comb-optical-microcomb.md | 2026-08-22 | [[mmwave-optical-microcomb]] |
| done | 2026-08-20_doi-10.1038-s41586-026-10904-x_cft-spectra-quantum-simulator.md | 2026-08-22 | [[cft-spectra-rydberg-simulator]] |
| done | 2026-08-20_doi-10.1103-gymp-vp87_nuclear-geometry-anisotropic-flow-oo-nene.md | 2026-08-22 | [[alice-oo-nene-nuclear-geometry-flow]] |
| done | 2026-08-20_doi-10.1103-lmq8-nsty_quantum-relative-entropy-semiclassical-einstein-equations.md | 2026-08-22 | [[quantum-relative-entropy-einstein-equations]] |
| done | 2026-08-22_doi-10.3847-1538-4357-ae8f31_stellar-spin-repeating-partial-tidal-disruption.md | 2026-08-22 | [[stellar-spin-repeating-partial-tde]] |
| done | 2026-08-23_doi-10.1126-science.ads5962_tracking-baryon-number-nuclear-collisions.md | 2026-08-29 | [[tracking-baryon-number-nuclear-collisions]] |
| done | 2026-08-24_arxiv-2601.11446_coupling-free-electrons-trapped-ion-quantum-computer.md | 2026-08-29 | [[coupling-free-electrons-trapped-ion]] |
| done | 2026-08-24_doi-10.1038-s41566-026-01976-2_correlated-electrons-xray-hhg-beyond-single-electron-limit.md | 2026-08-29 | [[correlated-electrons-xray-hhg]] |
| done | 2026-08-24_doi-10.1103-g6v2-grnl_particle-view-many-body-electronic-structure-nn-wavefunction.md | 2026-08-29 | [[particle-view-nn-wavefunction]] |
| done | 2026-08-26_doi-10.1103-lq5r-sjp7_43gev-gamma-ray-line-galaxy-clusters.md | 2026-08-29 | [[43gev-gamma-ray-line-clusters]] |
| done | 2026-08-26_doi-10.1126-sciadv.adu9368_emergent-social-conventions-collective-bias-llm-populations.md | 2026-08-29 | [[emergent-social-conventions-llm-populations]] |
| done | 2026-08-26_doi-10.3847-1538-3881-ae8bae_streamer-misalignment-gw-ori-circumtriple-disk.md | 2026-08-29 | [[gw-ori-streamer-misalignment]] |
| done | 2026-08-27_arxiv-2411.11581_oasis-million-agent-social-simulator.md | 2026-08-29 | [[oasis-million-agent-social-simulator]] |
| done | 2026-08-27_doi-10.1038-s41586-026-10914-9_atomic-scale-double-slit-interferometry-si.md | 2026-08-29 | [[atomic-scale-double-slit-si]] |
| done | 2026-08-28_arxiv-2604.05307_equilibrated-fraction-qcd-oo-collisions.md | 2026-08-29 | [[equilibrated-fraction-oo-qcd]] |
| done | 2026-08-28_doi-10.3847-1538-4357-ae3c08_astrid-simulation-z0-black-holes-large-scale-structure.md | 2026-08-29 | [[astrid-z0-mbh-lss]] |
| done | 2026-08-29_arxiv-2608.20311_imaging-vacuum-fluctuations-quantum-field.md | 2026-09-03 | [[imaging-vacuum-fluctuations-qft]] |
| done | 2026-08-29_doi-10.1038-s44284-026-00443-x_urban-congestion-relief-routing-app-interventions.md | 2026-09-03 | [[urban-congestion-routing-app]] (multi-agent section; moved from Islands 2026-08-31) |
| done | 2026-08-30_doi-10.1038-s41586-026-10579-4_direct-black-hole-mass-little-red-dot-high-redshift.md | 2026-09-03 | [[direct-bh-mass-lrd-abell2744]] |
| done | 2026-08-31_arxiv-2109.03752_discrete-gravity-planck-scale-cells.md | 2026-09-03 | [[discrete-gravity-planck-cells]] |
| done | 2026-08-31_doi-10.1126-sciadv.aeh1011_feynman-path-integral-postulates-single-photons.md | 2026-09-03 | [[feynman-path-integral-single-photons]] |
| done | 2026-09-02_lz-preprint-260901_dark-matter-eft-nuclear-recoil-higher-energies.md | 2026-09-03 | [[lz-dm-eft-high-energy-recoil]] |
| done | 2026-09-04_apj-998-318_missing-watts-tarantula.md | 2026-09-05 | [[missing-watts-tarantula]] |
| done | 2026-09-04_arxiv-2512.11659_bh-thermo-far-from-equilibrium.md | 2026-09-05 | [[bh-thermo-far-from-equilibrium]] |
| done | 2026-09-04_arxiv-2604.10477_vacuum-birefringence-magnetar-xrays.md | 2026-09-05 | [[vacuum-birefringence-magnetar-xrays]] |
| done | 2026-09-04_arxiv-2608.09867_extracting-reasoning-traces-proprietary-llms.md | 2026-09-05 | [[extracting-reasoning-traces-proprietary-llms]] |
| done | 2026-09-04_doi-10.1038-s41467-026-76488-2_mirror-that-lies-diffractive-concealment.md | 2026-09-05 | [[mirror-that-lies-diffractive-concealment]] |
| done | 2026-09-04_doi-10.1038-s41567-026-03360-x_electron-hole-migrate-molecule.md | 2026-09-05 | [[electron-hole-migrate-molecule]] |
| done | 2026-09-04_doi-10.3847-2041-8213-ae808f_hi-intensity-mapping-meerkat-autopower-detection.md | 2026-09-05 | [[hi-intensity-mapping-meerkat]] |
| done | 2026-09-04_nodoi_25gpps-diffractive-microscope.md | 2026-09-05 | [[25gpps-diffractive-microscope]] |
| done | 2026-09-04_nodoi_deepmind-hurricane-forecasting.md | 2026-09-05 | [[deepmind-hurricane-forecasting]] |
| done | 2026-09-04_nodoi_desktop-ct-electron-clouds-3d-pot.md | 2026-09-05 | [[desktop-ct-electron-clouds]] |
| skipped_duplicate | 2026-09-04_nodoi_phase-transition-hides-fingerprints.md | 2026-09-05 | skipped_duplicate of [[erte3-competing-cdw-time-domain]] |
| done | 2026-09-04_nodoi_recycling-idler-quantum-superresolution.md | 2026-09-05 | [[recycling-idler-quantum-superresolution]] |
| done | 2026-09-04_nodoi_woven-ferroelectric-domains-optical.md | 2026-09-05 | [[woven-ferroelectric-domains-optical]] |
| done | 2026-09-08_arxiv-2608.20464_ultraheavy-dark-matter-levitated-magnet-polonaise.md | 2026-09-12 | [[ultraheavy-dm-levitated-magnet-polonaise]] |
| done | 2026-09-08_doi-10.1038-s41586-026-10818-8_baryon-semileptonic-decays-polarization-entanglement.md | 2026-09-12 | [[baryon-semileptonic-polarization-entanglement]] |
| done | 2026-09-10_doi-10.1038-s41550-026-02953-z_eccentric-massive-protobinary-core-merger.md | 2026-09-12 | [[eccentric-massive-protobinary-core-merger]] |
| done | 2026-09-10_doi-10.3847-2041-8213-ae433b_ch3oh-hcn-3i-atlas-outgassing.md | 2026-09-12 | [[ch3oh-hcn-3i-atlas-outgassing]] |
| done | 2026-09-12_doi-10.3847-2041-8213-ae8cf7_rapid-orbital-decay-erassu-j060839-double-degenerate-binary.md | 2026-09-20 | [[rapid-orbital-decay-erassu-j060839]] |
| done | 2026-09-13_doi-10.1103-jdw6-3556_unconventional-materials-light-dark-matter-detection.md | 2026-09-20 | [[unconventional-materials-light-dm]] |
| done | 2026-09-13_doi-10.1140-epjc-s10052-026-15820-y_entanglement-islands-page-curves-kerr-ads.md | 2026-09-20 | [[entanglement-islands-page-curves-kerr-ads]] |
| done | 2026-09-14_lbt-yp_part1of2_methodology-and-data.md | 2026-09-20 | [[lbt-yp-primordial-helium]] (part 1/2) |
| done | 2026-09-14_lbt-yp_part2of2_result-and-implications.md | 2026-09-20 | [[lbt-yp-primordial-helium]] (part 2/2) |
| done | 2026-09-15_doi-10.1103-y1nh-1b82_zz-boson-pair-entanglement-higgs-decays.md | 2026-09-20 | [[zz-entanglement-higgs-decays]] |
| done | 2026-09-18_doi-10.1038-s41550-026-02930-6_topology-of-the-universe.md | 2026-09-20 | [[topology-of-the-universe]] |
| done | 2026-09-20_doi-10.1038-s41467-026-77922-1_dynamics-informed-imputation-missing-systems-dynamics.md | 2026-10-01 | [[dynamics-informed-imputation]] |
| done | 2026-09-20_doi-10.1038-s41586-026-10894-w_s301-star-sensitive-to-spin-of-sgr-a-star.md | 2026-10-01 | updated [[s301-sgra-spin-sensitive-star]] (no new page) |
| done | 2026-09-20_doi-10.1088-1681-7575-ae570f_redetermination-gravitational-constant-bipm-torsion-balance-nist.md | 2026-10-01 | [[big-g-bipm-torsion-balance-nist]] |
| done | 2026-09-21_doi-10.1038-s41467-026-76604-2_orbformer-ab-initio-foundation-model-wavefunctions-bond-breaking.md | 2026-10-01 | [[orbformer-wavefunction-foundation-model]] |
| done | 2026-09-21_doi-10.1038-s42005-026-02791-5_narrowband-tunable-euv-soft-xray-harmonics.md | 2026-10-01 | [[narrowband-tunable-euv-soft-xray-harmonics]] |
| done | 2026-09-21_doi-10.1126-science.adz0521_extreme-loss-suppression-dipolar-molecular-gas.md | 2026-10-01 | [[extreme-loss-suppression-dipolar-molecules]] |
| done | 2026-09-21_doi-10.1126-science.aeh7535_quantum-jumps-of-sound.md | 2026-10-01 | [[quantum-jumps-of-sound]] |
| done | 2026-09-23_doi-10.3847-1538-4365-ae95f6_tempos-treasury-extremely-metal-poor-o-stars.md | 2026-10-01 | [[tempos-metal-poor-o-stars]] |
| done | 2026-09-24_arxiv-2512.14204_cosmic-lockdown-decoherence-vacuum-tunneling.md | 2026-10-01 | [[cosmic-lockdown-vacuum-tunneling]] |
| done | 2026-09-24_doi-10.1103-2xsn-rgx3_nonmonotonicity-transverse-momentum-correlations-star.md | 2026-10-01 | [[star-pt-correlations-qcd-critical]] |
| done | 2026-09-24_ssrn-7180683_phantom-halo-surface-density-scale-verlinde-gravity.md | 2026-10-01 | [[phantom-halo-verlinde-surface-density]] |
| done | 2026-09-25_doi-10.3847-2041-8213-ae9a9e_fdm-wave-simulation-lensing-hs0810.md | 2026-10-01 | [[fdm-wave-lensing-hs0810]] |
| done | 2026-09-26_doi-10.1016-j.dark.2026.102364_negative-mass-objects-in-the-sky.md | 2026-10-01 | [[negative-mass-objects-in-the-sky]] |
| done | 2026-09-26_doi-10.31526-PHEP.2026.21_cms-black-holes-sphalerons-phase-space-svm.md | 2026-10-01 | [[cms-black-holes-sphalerons-svm]] |
| done | 2026-09-26_doi-10.3847-2041-8213-ae9cbd_jet-aligned-halpha-cgm-radio-galaxies.md | 2026-10-01 | [[jet-aligned-halpha-cgm]] |
| done | 2026-09-27_doi-10.1007-s10484-023-09582-6_hrv-biofeedback-methods-systematic-review.md | 2026-10-01 | [[hrv-biofeedback-methods-review]] |
| done | 2026-09-27_hrvb-combined-6-sources_resonance-baroreflex-physiology-and-methods.md | 2026-10-01 | [[hrv-resonance-baroreflex]] |
| done | 2026-09-28_arxiv-2609.20788_looking-inside-a-quantum-black-hole.md | 2026-10-01 | [[looking-inside-a-quantum-black-hole]] |
| done | 2026-09-28_arxiv-2609.21471_geodesic-tessellation-schwarzschild-holography.md | 2026-10-01 | [[geodesic-tessellation-schwarzschild-holography]] (with v2) |
| done | 2026-09-29_arxiv-2609.21471_geodesic-tessellation-schwarzschild-holography-v2-foundations.md | 2026-10-01 | [[geodesic-tessellation-schwarzschild-holography]] (foundations) |
