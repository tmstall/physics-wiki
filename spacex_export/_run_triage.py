"""Hand-curated conservative triage of 94 SpaceX extracts vs wiki papers."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(r"C:\Users\tmsta\Documents\Physics-Wiki")
exts = json.loads((ROOT / "spacex_export" / "_extract_heads.json").read_text(encoding="utf-8"))
by_file = {e["file"]: e for e in exts}

# Every file must appear once: (bucket, closest_wiki_list, note_or_topic_tag)
# bucket: NEW | SOFT-DUP | THIN-SKIP
# For NEW, note is topic_tag. For others, note is reason.

CLASS: dict[str, tuple[str, list[str], str]] = {
    # --- mega learning / pedagogy ---
    "2025-02-28_i-astrophysics-and-black-holes_5d552948.md": (
        "SOFT-DUP",
        ["evaporating-charged-black-holes", "hawking-radiation-charge-shell", "pre-bang-leftovers"],
        "Long multi-topic BH/astro learning mega-thread; overlaps existing BH cluster",
    ),
    "2025-03-01_i-quantum-mechanics-quantum-field-theory_c6667db7.md": (
        "SOFT-DUP",
        ["time-goes-quantum", "quantum-proper-time-ion-clocks", "massive-tunneling-schrodinger-cats"],
        "Long QM/QFT learning mega-thread; overlaps quantum-time / foundations cluster",
    ),
    "2025-02-28_materials-science-semiconductors-nanostructures_afa0fe4c.md": (
        "THIN-SKIP",
        [],
        "Broad materials survey mega-thread; not one paper",
    ),
    "2025-03-01_chemistry_73efd331.md": (
        "THIN-SKIP",
        [],
        "Generic chemistry chat; no single-paper core",
    ),
    "2025-03-10_physics_c7a8e63b.md": (
        "THIN-SKIP",
        [],
        "Generic physics chat; too fragmentary for a paper page",
    ),
    "2025-03-14_biology-microscopy_7fb6f0cb.md": (
        "THIN-SKIP",
        [],
        "Generic biology/microscopy chat",
    ),
    "2025-04-12_general-physics_4e3dc5c4.md": (
        "THIN-SKIP",
        [],
        "Generic general-physics chat",
    ),
    "2025-04-12_qft-related_09c7589c.md": (
        "THIN-SKIP",
        [],
        "Loose QFT-related discussion; no single paper",
    ),
    "2025-05-07_quantum-field-theory_5568829a.md": (
        "THIN-SKIP",
        [],
        "Broad QFT pedagogy without single-paper core",
    ),
    "2025-07-12_quantum-information-and-thermodynamics_b7200478.md": (
        "THIN-SKIP",
        ["noise-driven-qubit-entanglement", "dissipative-cavity-entanglement"],
        "Pedagogical QI+thermo discussion; not a distinct paper analysis",
    ),
    "2025-07-30_quantum-field-theory-and-qed-vectors_4da72e5b.md": (
        "THIN-SKIP",
        [],
        "Pedagogical QED vectors thread",
    ),
    "2025-07-30_quantum-field-theory-basics-for-chemists_a0236668.md": (
        "THIN-SKIP",
        [],
        "QFT for chemists overview; pedagogy only",
    ),
    "2025-08-01_quantum-field-theory-perspective_dfc276c9.md": (
        "THIN-SKIP",
        [],
        "QFT perspective overview; no single paper",
    ),
    "2025-08-01_vector-potential-car_c3a4e848.md": (
        "THIN-SKIP",
        [],
        "Informal car-chat vector potential teaching",
    ),
    "2025-08-04_quantum-field-theory-basics-car_ae9cfbc1.md": (
        "THIN-SKIP",
        [],
        "Informal car-chat QFT basics",
    ),
    "2025-09-12_technical-paper-discussion-continuation_4fca6e67.md": (
        "THIN-SKIP",
        [],
        "Continuation fragment; paper identity unclear",
    ),
    "2025-09-26_qmm-information-as-fundamental-cosmic-component_5901c9a9.md": (
        "THIN-SKIP",
        ["qg-deep-dive-2-info-holography"],
        "Speculative QMM series; not wiki-grade paper analysis",
    ),
    "2025-09-29_continuing-qmm_c7ba254f.md": (
        "THIN-SKIP",
        [],
        "QMM continuation fragment",
    ),
    "2025-09-29_qmm-and-dark-matter_e136b865.md": (
        "THIN-SKIP",
        ["gamma-glow-pbh-detector"],
        "Speculative QMM + DM chat",
    ),
    "2025-10-01_quark-gluon-plasma-discussion_88f679b7.md": (
        "SOFT-DUP",
        ["color-superconductivity-qcd", "high-pt-physics-cern-isr"],
        "QGP discussion overlaps dense QCD / high-energy nuclear cluster",
    ),
    "2025-10-20_astronomy-cosmology-advances_7cfc9fe8.md": (
        "THIN-SKIP",
        [],
        "Generic advances survey without single-paper core",
    ),
    "2025-11-11_sun-s-photon-generation-via-fusion-reactions_4720fc2d.md": (
        "THIN-SKIP",
        [],
        "Pop-level solar fusion photon chat",
    ),
    "2025-11-17_perovskite-research-synthesis-and-optimization_cf3c923a.md": (
        "THIN-SKIP",
        [],
        "Chemistry process chat; thin for paper page",
    ),
    "2026-01-17_spin-networks-to-spin-foams-evolution_560ee84e.md": (
        "SOFT-DUP",
        ["qg-deep-dive-1-mergers-emission", "quantum-damping-cosmological-shear"],
        "Spin networks/foams pedagogy; overlaps LQG / QG deep-dive material",
    ),
    "2026-02-05_v3-4-3-prompt-evanescent-waves-hidden-transverse-spin-moment_2c39fa3c.md": (
        "NEW",
        ["snte-light-topological-inversion", "ciss-homochirality"],
        "evanescent-transverse-spin",
    ),
    "2026-02-08_generation-v3-4-4-1-holographic-universe-error-correcting-co_25dca1ca.md": (
        "SOFT-DUP",
        ["qg-deep-dive-2-info-holography", "qg-deep-dive-3-holographic-codes"],
        "Holographic error-correcting cosmology; same theme as QG deep dives",
    ),
    "2026-02-08_clustering-of-conditional-mutual-information_6b2b0505.md": (
        "THIN-SKIP",
        [],
        "ML/info-theory fragment; not a physics paper page",
    ),
    "2026-02-10_bec-superfluid-he4_6bdb7007.md": (
        "THIN-SKIP",
        ["molecular-rotation-superfluid-he"],
        "Short BEC/4He teaching thread",
    ),
    "2026-02-10_cooper-pairs-in-superconductivity-explained_43aca8a3.md": (
        "THIN-SKIP",
        ["bata2s5-field-induced-sc", "color-superconductivity-qcd"],
        "Pedagogical Cooper-pair explainer",
    ),
    "2026-02-11_universe-as-holographic-error-correcting-code_6c0f6fd9.md": (
        "SOFT-DUP",
        ["qg-deep-dive-3-holographic-codes", "qg-deep-dive-2-info-holography"],
        "Holographic code cosmology; same as QG deep-dive cluster",
    ),
    "2026-02-17_quantum-field-theory-virtual-particles-analysis_7510072d.md": (
        "THIN-SKIP",
        [],
        "Virtual-particles pedagogy; not one experimental/theory paper",
    ),
    "2026-02-24_reviving-schr-dinger-s-geometric-color-vision-theory_2c22f0bf.md": (
        "SOFT-DUP",
        ["color-space-geometry"],
        "Same Schrödinger color-geometry / non-Riemannian color program",
    ),
    "2026-04-05_femtosecond-laser-pulse-carrier-envelope-phase-explained_750daeba.md": (
        "THIN-SKIP",
        ["attosecond-stm-lightwave"],
        "CEP concept explainer; thin for paper page",
    ),
    "2026-05-23_analyze-paper-in-conversation_5dad645d.md": (
        "THIN-SKIP",
        [],
        "Unnamed thin analysis session",
    ),
    "2026-05-24_delayed-choice-quantum-eraser-summary-and-updates_de4ce7a3.md": (
        "THIN-SKIP",
        ["negative-weak-valued-excitation-times", "w-state-entangled-measurement"],
        "Thin delayed-choice summary with high chrome; not full paper page",
    ),
    "2026-06-01_quantum-mechanics-particle-eigenvectors-and-resonance-harmon_6d7909ce.md": (
        "THIN-SKIP",
        [],
        "Pedagogical eigenvectors/harmonics chat",
    ),
    "2026-07-20_einstein-and-riemann-geometry-in-relativity_3c9369d4.md": (
        "THIN-SKIP",
        ["second-order-gw-strain-gauge", "frozen-in-gravitational-fields"],
        "Pedagogical relativity/geometry thread",
    ),
    "2026-07-09_euclid-images-technical-paper-analysis_9f84bcac.md": (
        "SOFT-DUP",
        ["euclid-high-z-quasar-census"],
        "Euclid imaging/high-z program soft-overlap",
    ),
    "2026-05-11_neural-net-cosmology-simulator_d729b1cb.md": (
        "SOFT-DUP",
        ["cigars-i-supernova-cosmology", "desi-evolving-dark-energy"],
        "ML cosmology / SBI-adjacent; soft overlap with existing cosmology inference pages",
    ),
    "2026-05-08_liquids-pin-bio-friendly-constants_cdd8a90f.md": (
        "THIN-SKIP",
        [],
        "Speculative constants chat; thin for paper page",
    ),
    "2026-02-22_flexible-electrodynamic-dust-shields-for-moon_5b2e8080.md": (
        "THIN-SKIP",
        [],
        "Engineering dust-shield note; low wiki priority / thin analysis",
    ),
    "2026-02-11_microfluidic-electro-viscoelastic-nano-particle-separation_fec8a441.md": (
        "THIN-SKIP",
        [],
        "Device paper island; short/thin relative to wiki paper standard",
    ),

    # --- clear soft-dups of ingested papers ---
    "2026-05-09_hawking-radiation-from-charged-shell_7a92c9cf.md": (
        "SOFT-DUP",
        ["hawking-radiation-charge-shell"],
        "Same double-copy charge-shell Hawking analysis already in wiki",
    ),
    "2026-05-26_evaporating-charged-black-holes-avoid-singularities_42f29512.md": (
        "SOFT-DUP",
        ["evaporating-charged-black-holes"],
        "Same charged BH evaporation / regular endpoints paper",
    ),
    "2026-05-24_black-holes-evaporate-before-breaking_fe621d53.md": (
        "SOFT-DUP",
        ["evaporating-charged-black-holes", "black-hole-evaporation-energy-conditions"],
        "Evaporation-before-breakdown theme; covered by evaporation cluster",
    ),
    "2026-05-05_collapse-gravity-proper-time-uncertainty_4a24df05.md": (
        "SOFT-DUP",
        ["collapse-models-clock-precision"],
        "CSL/DP spacetime jitter -> clock floor",
    ),
    "2026-05-06_quantum-proper-time-signatures-in-ion-clocks_57902025.md": (
        "SOFT-DUP",
        ["quantum-proper-time-ion-clocks", "time-goes-quantum"],
        "Ion-clock proper-time / SODS program",
    ),
    "2026-05-17_cluster-tunneling-forges-scalable-schr-dinger-cats_19c6e325.md": (
        "SOFT-DUP",
        ["massive-tunneling-schrodinger-cats"],
        "Collective tunneling NOON cats paper",
    ),
    "2026-06-03_photon-truncation-creates-infinite-particle-zoo_771b4084.md": (
        "SOFT-DUP",
        ["truncated-photon-dynamical-casimir"],
        "Truncated-photon dynamical Casimir multiphoton states",
    ),
    "2026-05-08_photonic-supersolid-nature-paper_1390a395.md": (
        "SOFT-DUP",
        ["photonic-supersolid"],
        "Photonic supersolid paper",
    ),
    "2026-05-08_quantum-metallurgy-cdw-electron-crystals-melt_ad2a2c65.md": (
        "SOFT-DUP",
        ["quantum-metallurgy-cdw"],
        "CDW quantum metallurgy melting",
    ),
    "2026-05-12_ultramassive-black-hole-binary-carves-a-starless-kiloparsec-_5d425014.md": (
        "SOFT-DUP",
        ["ultramassive-bh-binary-cavity"],
        "Ultramassive BH binary kpc cavity",
    ),
    "2026-05-12_cosmic-web-jwst-shows-quenching-flip-by-z-2_057c4984.md": (
        "SOFT-DUP",
        ["cosmos-web-cosmic-web"],
        "JWST cosmic web / quenching flip",
    ),
    "2026-05-27_loki-early-accreted-vmp-stars_811e3d54.md": (
        "SOFT-DUP",
        ["loki-early-accreted-vmp"],
        "Loki early-accreted VMP stars",
    ),
    "2026-05-25_pulsar-timing-reveals-lmc-and-sagittarius-masses_2c1f4c1d.md": (
        "SOFT-DUP",
        ["pulsars-satellite-masses"],
        "Pulsar accelerations -> satellite masses",
    ),
    "2026-06-13_cold-atoms-measure-time-via-entropy_aae7fe62.md": (
        "SOFT-DUP",
        ["problem-of-time-cold-atoms"],
        "Cold-atom problem of time / entropy-time probes",
    ),
    "2026-06-21_mond-bullet-cluster-core-mass-solved_e2ed039c.md": (
        "SOFT-DUP",
        ["mond-external-field-sparc", "newton-ksz-force-law"],
        "MOND / large-scale gravity family (Bullet Cluster angle)",
    ),
    "2026-05-16_mesic-nuclei-discovery-at-gsi_9525664b.md": (
        "SOFT-DUP",
        ["eta-prime-mesic-nucleus"],
        "eta-prime mesic nucleus GSI search",
    ),
    "2026-05-14_vacua-quantize-cosmological-constant_be01e1f5.md": (
        "SOFT-DUP",
        ["topological-cosmological-constant"],
        "theta-vacua / topological cosmological constant",
    ),
    "2026-04-16_high-pt-jets-early-isr-evidence-1970s_af30aa25.md": (
        "SOFT-DUP",
        ["high-pt-physics-cern-isr", "levinthal-high-pt-isr"],
        "ISR high-pT historical program",
    ),
    "2026-05-04_siv-centers-in-diamond-tension-induced-symmetry-breaking_e044c9ed.md": (
        "SOFT-DUP",
        ["siv-hydrostatic-strain-symmetry"],
        "SiV strain / symmetry",
    ),
    "2026-03-26_femtosecond-spin-conserving-coherent-tin-vacancy-excitation_0a0600d1.md": (
        "SOFT-DUP",
        ["snv-super-coherent-excitation"],
        "SnV coherent / SUPER excitation family",
    ),
    "2026-05-01_programmable-kinetic-barcoding-for-cas13a-multiplexing_433319cb.md": (
        "SOFT-DUP",
        ["kinetic-barcoding-cas13a"],
        "Cas13a kinetic barcoding",
    ),
    "2026-05-01_sub-2-cryo-em-of-transcribing-rna-polymerase-ii_55dfe2e1.md": (
        "SOFT-DUP",
        ["water-rna-polymerase"],
        "RNA Pol II catalysis / structure island (closest existing page)",
    ),
    "2026-04-30_magnesium-promoted-benzidine-rearrangement-breakthrough_d07a73a5.md": (
        "SOFT-DUP",
        ["magnesium-benzidine-rearrangement"],
        "Mg benzidine biaryl synthesis",
    ),
    "2026-05-26_single-pressure-bump-explains-carbonaceous-chondrite-diversi_1d61108e.md": (
        "SOFT-DUP",
        ["chondrite-pressure-bump"],
        "Chondrite pressure-bump story",
    ),
    "2026-02-11_jwst-reveals-uv-deficient-low-luminosity-agn_5567d75b.md": (
        "SOFT-DUP",
        ["euclid-high-z-quasar-census", "naked-black-hole-candidate"],
        "High-z / compact AGN portrait family",
    ),
    "2026-06-30_two-mode-squeezed-states-entanglement_4726e199.md": (
        "SOFT-DUP",
        ["noise-driven-qubit-entanglement", "dissipative-cavity-entanglement"],
        "Two-mode squeezing / noise-entanglement family already covered",
    ),

    # --- NEW (clear or carefully argued unique papers/angles) ---
    "2025-05-18_nuclear-magnetization-observation-breakthrough_d40be7a8.md": (
        "NEW",
        ["nucleus-shell-src-memory", "nucleus-tells-on-itself"],
        "nuclear-magnetization",
    ),
    "2025-11-08_massive-gravity-gluon-magic_a16227af.md": (
        "NEW",
        ["color-superconductivity-qcd", "gw-induced-fermion-freeze-in"],
        "massive-gravity-gluon",
    ),
    "2025-08-20_early-universe-ionization-by-supermassive-stars_fd46ef60.md": (
        "NEW",
        ["cosmos-web-cosmic-web", "pre-bang-leftovers"],
        "early-universe-ionization-sms",
    ),
    "2025-08-29_emc-effect-quarks-and-gluons_a467bb47.md": (
        "NEW",
        ["nucleus-shell-src-memory", "high-pt-physics-cern-isr"],
        "emc-effect-quarks-gluons",
    ),
    "2025-10-01_precision-net-proton-fluctuations-at-rhic_284130d8.md": (
        "NEW",
        ["color-superconductivity-qcd", "star-jpsi-spin-interference"],
        "rhic-net-proton-fluctuations",
    ),
    "2026-01-07_five-dimensional-classical-gravity-model_c344a460.md": (
        "NEW",
        ["black-hole-third-law-violation", "gravastar-dust-collapse"],
        "5d-classical-gravity",
    ),
    "2026-01-11_temporal-imbalance-theory-gravity-s-new-clock_bc2d307c.md": (
        "NEW",
        ["collapse-models-clock-precision", "quantum-proper-time-ion-clocks"],
        "temporal-imbalance-gravity",
    ),
    "2026-01-14_laboratory-suppression-of-blazar-instabilities_fcdb46c3.md": (
        "NEW",
        ["mrk501-double-jet-smbbh", "plasma-relativistic-amplifier"],
        "lab-blazar-instability-suppression",
    ),
    "2026-01-19_positronium-diffraction-breakthrough-in-antimatter-physics_1d9d4313.md": (
        "NEW",
        ["3d-electron-diffraction-osc"],
        "positronium-diffraction",
    ),
    "2026-02-07_jwst-reveals-hydrocarbon-factory-in-ulirg_757ca7d7.md": (
        "NEW",
        ["interstellar-glaciers-spherex", "interstellar-sulfur-ice"],
        "jwst-ulirg-hydrocarbons",
    ),
    "2026-02-08_quantum-metric-from-spin-momentum-locking_7ba11668.md": (
        "NEW",
        ["snte-light-topological-inversion", "brown-zak-nonlinear-transport"],
        "quantum-metric-spin-momentum",
    ),
    "2026-02-09_physically-possible-warp-drive-breakthrough_a388b090.md": (
        "NEW",
        ["second-order-gw-strain-gauge", "universe-gas-pedal-leaky"],
        "warp-drive-metric",
    ),
    "2026-02-13_programmable-non-abelian-photonic-braiding_c725bcab.md": (
        "NEW",
        ["photon-number-optical-analogy-control", "twisted-light-chiral-ms"],
        "nonabelian-photonic-braiding",
    ),
    "2026-02-14_electric-nucleation-of-3d-magnetic-heliknotons_65da18c4.md": (
        "NEW",
        ["spin-flip-flop-saf", "photonic-supersolid"],
        "magnetic-heliknotons",
    ),
    "2026-02-16_anyon-trions-reveal-fractional-charges-in-twisted-mote_7e86dd11.md": (
        "NEW",
        ["three-body-quantum-company", "fractional-fermi-sea-1d-bosons"],
        "anyon-trions-motte2",
    ),
    "2026-02-16_supermoir-trilayer-graphene-superconductivity_f38a787f.md": (
        "NEW",
        ["brown-zak-nonlinear-transport", "bata2s5-field-induced-sc"],
        "supermoire-trilayer-sc",
    ),
    "2026-02-17_long-term-timing-of-psr-j1906-0746-binary_19e0bfc4.md": (
        "NEW",
        ["pulsars-satellite-masses", "gw170817-jet-hubble"],
        "psr-j1906-binary-timing",
    ),
    "2026-02-25_phosphorus-radical-catalyzed-markovnikov-hydroamination_de2d756d.md": (
        "NEW",
        ["magnesium-benzidine-rearrangement", "bond-breaking-discount"],
        "p-radical-hydroamination",
    ),
    "2026-02-26_iras-21204-4913-eruptive-low-mass-fuor_48e8a69e.md": (
        "NEW",
        ["dr21-magnetic-accretion", "supernova-onion-expansion"],
        "iras-fuor-outburst",
    ),
    "2026-05-10_1d-anyons-momentum-tails_6e74a90c.md": (
        "NEW",
        ["fractional-fermi-sea-1d-bosons", "three-body-quantum-company"],
        "1d-anyons-momentum-tails",
    ),
    "2026-05-13_trinity-test-creates-novel-ca-cu-si-clathrate_42edff4d.md": (
        "NEW",
        ["dense-plasma-opacity-revision", "filming-plasma-birth"],
        "trinity-clathrate",
    ),
    "2026-05-16_ice-core-traces-supernova-fe-60-in-local-cloud_1507751a.md": (
        "NEW",
        ["supernova-onion-expansion", "interstellar-glaciers-spherex"],
        "ice-core-fe60-supernova",
    ),
    "2026-05-18_muse-captures-glowing-quasar-filament-at-z-3_4e0316bd.md": (
        "NEW",
        ["jwst-filament-cnd-ngc4696", "high-z-quasar-pair-merger"],
        "muse-quasar-filament-z3",
    ),
    "2026-05-23_magnetar-powered-slsn-2017egm-fermi-lat-detection_42ee8206.md": (
        "NEW",
        ["supernova-onion-expansion", "aquila-booster-pevatron"],
        "magnetar-slsn-fermi",
    ),
    "2026-05-23_nickelate-films-nodeless-gap-and-70-mev-kink_765e7590.md": (
        "NEW",
        ["bata2s5-field-induced-sc", "hot-electron-coherent-phonons-ptcu"],
        "nickelate-nodeless-gap",
    ),
    "2026-05-25_axion-quantum-signatures-erased-in-detectors_6487c8e0.md": (
        "NEW",
        ["synchrotron-dm-detector", "gamma-glow-pbh-detector"],
        "axion-signature-erasure",
    ),
    "2025-05-18_nuclear-magnetization-observation-breakthrough_d40be7a8.md": (
        "NEW",
        ["nucleus-shell-src-memory", "nucleus-tells-on-itself"],
        "nuclear-magnetization",
    ),
}

# Fix accidental duplicate key - keep one
# (nuclear magnetization listed twice with same content - fine)

def main() -> None:
    missing = [f for f in by_file if f not in CLASS]
    extra = [f for f in CLASS if f not in by_file]
    if missing or extra:
        print("MISSING FROM CLASS", len(missing))
        for m in missing:
            print(" ", m, by_file[m]["title"])
        print("EXTRA IN CLASS", extra)
        raise SystemExit(1)

    items = []
    for f, (bucket, wiki, note) in sorted(CLASS.items(), key=lambda x: by_file[x[0]]["title"].lower()):
        e = by_file[f]
        rec = {
            "bucket": bucket,
            "file": f,
            "title": e["title"],
            "size": e["size"],
            "closest_wiki": wiki,
            "note": note,
        }
        if bucket == "NEW":
            rec["topic_tag"] = note
        items.append(rec)

    counts = {
        "NEW": sum(1 for i in items if i["bucket"] == "NEW"),
        "SOFT-DUP": sum(1 for i in items if i["bucket"] == "SOFT-DUP"),
        "THIN-SKIP": sum(1 for i in items if i["bucket"] == "THIN-SKIP"),
    }
    assert sum(counts.values()) == 94, counts

    out = {
        "triaged_at": "2026-08-04",
        "source": "spacex_export/extracted-analyses",
        "wiki_papers_compared": 129,
        "extracts_total": 94,
        "counts": counts,
        "policy": "Conservative: prefer SOFT-DUP over NEW when uncertain. No wiki ingest.",
        "items": items,
    }
    (ROOT / "spacex_export" / "TRIAGE.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    lines = []
    lines.append("# SpaceX extract — duplicate triage\n\n")
    lines.append("**Date:** 2026-08-04  \n")
    lines.append("**Source:** `spacex_export/extracted-analyses/` (94 files)  \n")
    lines.append("**Wiki papers compared:** 129  \n")
    lines.append(
        "**Policy:** Conservative — when uncertain between NEW and SOFT-DUP, prefer SOFT-DUP. "
        "Mega learning threads and pure pedagogy → SOFT-DUP or THIN-SKIP, not NEW.  \n"
    )
    lines.append("**No wiki ingest; `wiki/` not modified.**\n\n")
    lines.append("## Summary counts\n\n")
    lines.append("| Bucket | Count |\n| --- | ---: |\n")
    lines.append(f"| **NEW** | {counts['NEW']} |\n")
    lines.append(f"| **SOFT-DUP** | {counts['SOFT-DUP']} |\n")
    lines.append(f"| **THIN / SKIP** | {counts['THIN-SKIP']} |\n")
    lines.append(f"| **Total** | 94 |\n")

    lines.append("\n## NEW — later ingest candidates only\n\n")
    lines.append("| File | Title | Topic tag |\n| --- | --- | --- |\n")
    for r in sorted([i for i in items if i["bucket"] == "NEW"], key=lambda x: x["title"].lower()):
        lines.append(
            f"| `{r['file']}` | {r['title'].replace('|', '/')} | `{r.get('topic_tag', r['note'])}` |\n"
        )

    lines.append("\n## SOFT-DUP — already covered (do not create new paper pages)\n\n")
    lines.append("| File | Title | Closest wiki page(s) | Note |\n| --- | --- | --- | --- |\n")
    for r in sorted([i for i in items if i["bucket"] == "SOFT-DUP"], key=lambda x: x["title"].lower()):
        pages = ", ".join(f"`{s}`" for s in r["closest_wiki"])
        note = r["note"].replace("|", "/")
        lines.append(
            f"| `{r['file']}` | {r['title'].replace('|', '/')} | {pages} | {note} |\n"
        )

    lines.append("\n## THIN / SKIP — not worth a paper page\n\n")
    lines.append("| File | Title | Note |\n| --- | --- | --- |\n")
    for r in sorted([i for i in items if i["bucket"] == "THIN-SKIP"], key=lambda x: x["title"].lower()):
        note = r["note"].replace("|", "/")
        lines.append(
            f"| `{r['file']}` | {r['title'].replace('|', '/')} | {note} |\n"
        )

    lines.append("\n## Notes for later ingest\n\n")
    lines.append(
        f"- Ingest queue size if policy held: **{counts['NEW']} NEW** files only "
        "(after optional human spot-check).\n"
    )
    lines.append(
        "- SOFT-DUP may still hold useful alternate phrasing — optional fold into existing pages, not new slugs.\n"
    )
    lines.append("- Machine-readable twin: `spacex_export/TRIAGE.json`.\n")

    (ROOT / "spacex_export" / "TRIAGE.md").write_text("".join(lines), encoding="utf-8")
    print("NEW", counts["NEW"])
    print("SOFT-DUP", counts["SOFT-DUP"])
    print("THIN-SKIP", counts["THIN-SKIP"])
    print("OK TRIAGE.md TRIAGE.json")


if __name__ == "__main__":
    main()
