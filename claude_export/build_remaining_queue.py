"""Build not-yet-in-wiki queue from extracted-analyses."""
import json
import re
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent.parent
extracts = root / "claude_export" / "extracted-analyses"
wiki_papers = root / "wiki" / "papers"

wiki_slugs = sorted(p.stem for p in wiki_papers.glob("*.md"))
print(f"wiki papers: {len(wiki_slugs)}")

with open(root / "claude_export" / "new_papers_40.json", encoding="utf-8") as f:
    np40 = json.load(f)
slugs40 = {x["slug"] for x in np40}
print(f"slugs40: {len(slugs40)}")

# Known extract filename -> slug for first 40
map40 = {
    "2026-06-13_dynamical-formation-of-gravastars-from-dust-collapse_3e59a7b3.md": "gravastar-dust-collapse",
    "2026-06-14_thorium-229-nuclear-clock-analysis_c4c4cae5.md": "thorium-229-nuclear-clock",
    "2026-06-15_testing-the-problem-of-time-with-cold-atoms_3bdca1d2.md": "problem-of-time-cold-atoms",
    "2026-06-16_light-is-a-brake_74b6ff14.md": "light-as-friction-brake",
    "2026-06-17_entanglement-detected-in-macroscopic-crystal-via-neutron-sca_11579b57.md": "macroscopic-crystal-entanglement-neutrons",
    "2026-06-17_sunlight-doesn-t-need-a-laser-s-permission_f460aa4e.md": "sunlight-spdc-ghost-imaging",
    "2026-06-18_differential-signaling-for-the-quantum-vacuum_416551a8.md": "differential-signaling-quantum-vacuum",
    "2026-06-19_second-order-gravitational-wave-strain-analysis_9cdb1c0c.md": "second-order-gw-strain-gauge",
    "2026-06-20_a-globular-cluster-that-isn-t_d5678701.md": "not-a-globular-cluster",
    "2026-06-23_the-magnetic-compass-of-a-stellar-nursery_81e2ab23.md": "dr21-magnetic-accretion",
    "2026-06-23_the-universe-s-gamma-ray-glow-as-a-primordial-black-hole-det_7f776ce5.md": "gamma-glow-pbh-detector",
    "2026-06-24_the-standard-rulebook-for-reading-dense-plasmas-is-wrong_94785e1d.md": "dense-plasma-opacity-revision",
    "2026-06-24_the-synchrotron-s-new-dark-matter-detector_1ad48d4d.md": "synchrotron-dm-detector",
    "2026-06-25_the-horizon-speaks_8707aeb2.md": "horizon-direct-wave-gw250114",
    "2026-06-25_the-universe-s-gas-pedal-is-a-leaky-engine_e23e36e1.md": "universe-gas-pedal-leaky",
    "2026-06-25_three-s-company_50eacd55.md": "three-body-quantum-company",
    "2026-06-26_anisotropic-cosmic-structures-at-gigaparsec-scale_e511d1e3.md": "gigaparsec-anisotropic-structures",
    "2026-06-26_water-dissociation-in-confined-nanopores_3c1038a4.md": "water-double-life-nanoconfinement",
    "2026-06-28_water-s-secret-double-life_4318f0b4.md": "water-double-life-nanoconfinement",
    "2026-06-29_the-naked-black-hole_4cff7056.md": "naked-black-hole-candidate",
    "2026-07-04_the-black-hole-recoils_22da14b0.md": "black-hole-recoil-agn",
    "2026-07-05_discovery-of-a-big-ring-ultra-large-scale-structure_2f60382c.md": "big-ring-ultra-large-structure",
    "2026-07-05_the-oscilloscope-that-outran-the-electron_7a3d1b76.md": "attosecond-stm-lightwave",
    "2026-07-06_retrocausal-capacity-of-noisy-quantum-channels_666dfff1.md": "retrocausal-noisy-channel-capacity",
    "2026-07-06_the-quasar-census-begins_15c38246.md": "euclid-high-z-quasar-census",
    "2026-07-10_entropy-maximization-in-black-hole-mergers_57963c1b.md": "entropy-maximization-bh-mergers",
    "2026-07-10_two-clocks-one-laser-zero-excess-noise_af4e5b7a.md": "two-clocks-one-laser",
    "2026-07-11_beam-me-up-a-number-state_239be18f.md": "photon-number-optical-analogy-control",
    "2026-07-11_reading-a-supernova-s-onion-by-watching-it-grow_f7f83901.md": "supernova-onion-expansion",
    "2026-07-12_two-ways-to-read-a-black-hole-census_557975a4.md": "bh-recoils-agn-survey",
    "2026-07-14_black-hole-recoils-in-active-galactic-nuclei_77b287ab.md": "bh-recoils-agn-survey",
    "2026-07-15_gw170817-jet-geometry-and-hubble-constant-from-visibility-pl_d836bdf8.md": "gw170817-jet-hubble",
    "2026-07-15_quantum-damping-of-cosmological-shear_062a278d.md": "quantum-damping-cosmological-shear",
    "2026-07-16_the-qubits-that-entangled-themselves_694c81b2.md": "noise-driven-qubit-entanglement",
    "2026-07-19_gravity-as-a-compression-error_7db43741.md": "gravity-from-entropy",
    "2026-07-27_chiral-molecules-from-twisted-light-and-mass-spectrometry_439a3921.md": "twisted-light-chiral-ms",
    "2026-07-27_light-induced-topological-band-inversion-in-snte_000b415d.md": "snte-light-topological-inversion",
    "2026-06-03_the-photon-that-multiplied-when-you-tried-to-cut-it_b2eb34ef.md": "truncated-photon-dynamical-casimir",
    "2026-06-21_electrons-as-piston-not-furnace_e58c866e.md": "hot-electron-coherent-phonons-ptcu",
    "2026-04-27_mond-s-cosmic-fingerprint_898c8c43.md": "mond-external-field-sparc",
}

junk_re = re.compile(
    r"(framework|paper-analysis_|paper-analysis-details|reviewing-prior-session|"
    r"finding-a-matching-paper|finding-and-analyzing|finding-detailed-nasa|"
    r"patent-analysis|mit-paper-analysis|comparative-analysis-of-two|untitled_|"
    r"measurement-problem-threads|create-v3-9-framework|here-s-a-reference-from-a-post|"
    r"technical-paper-analysis-framework)",
    re.I,
)

# Content patterns matching papers already in wiki (pre-export + wave1)
content_dups = [
    (r"Brown.?Zak|Brown–Zak", "brown-zak"),
    (r"gravastar", "gravastar"),
    (r"Th-229|229Th|thorium.?229", "thorium-229"),
    (r"problem of time|Barontini", "problem-of-time"),
    (r"GW250114", "horizon-direct-wave"),
    (r"noise.?driven.*entangl|two-mode correlated microwave", "noise-driven"),
    (r"Big Ring", "big-ring"),
    (r"Euclid.*quasar|31 new quasars", "euclid"),
    (r"Terzan 5", "not-a-globular"),
    (r"\bSnTe\b", "snte"),
    (r"truncated photon|dynamical Casimir", "truncated-photon"),
    (r"mLQC|Bianchi.I", "quantum-damping"),
    (r"attosecond.*STM|lightwave.?driven STM", "attosecond-stm"),
    (r"spin.?flip.?flop|synthetic antiferromagnet", "saf"),
    (r"\bCISS\b|chiral.?induced spin selectivity", "ciss"),
    (r"SUPER protocol|tin.?vacancy|\bSnV\b", "snv"),
    (r"quantum jamming", "jamming"),
    (r"evaporating charged black", "evap-charged"),
    (r"frozen.?in gravitational|frozen.?in gravity", "frozen-in"),
    (r"DESI.*dark energy|evolving dark energy", "desi"),
    (r"\bkSZ\b|kinetic Sunyaev", "ksz"),
    (r"photonic supersolid", "photonic-supersolid"),
    (r"B.?meson|flavor anomaly", "b-meson"),
    (r"Aquila.*PeV|PeVatron", "aquila"),
    (r"dual quasars|high.?z quasar pair", "high-z-pair"),
    (r"Mrk\s*501", "mrk501"),
    (r"\bITO\b|fieldoscop", "ito"),
    (r"collapse models.*clock|\bCSL\b", "collapse-clock"),
    (r"W.?state.*entangled", "w-state"),
    (r"Shor algorithm|qLDPC", "shor"),
    (r"certified randomness", "certified-rand"),
    (r"relativistic amplifier|flying mirror", "plasma-amp"),
    (r"beam.?driven plasma", "beam-mirror"),
    (r"plasma birth|filming plasma", "filming-plasma"),
    (r"color superconduct", "color-sc"),
    (r"charge density wave|quantum metallurgy", "cdw"),
    (r"BaTa2S5", "bata2s5"),
    (r"\bSiV\b", "siv"),
    (r"Hawking.*charge shell|double.?copy.*Hawking", "hawking-shell"),
    (r"Alena tensor", "alena"),
    (r"eta.?prime|η.?prime", "eta-prime"),
    (r"topological cosmological constant", "topo-lambda"),
    (r"COSMOS.?Web", "cosmos-web"),
    (r"CIGaRS", "cigars"),
    (r"HOLISMOKES|SN Winny", "holismokes"),
    (r"SPHEREx|interstellar glaciers", "spherex"),
    (r"pulsars.*satellite|satellite masses.*pulsar", "pulsars"),
    (r"SMBH inclination", "smbh-inc"),
    (r"ultramassive", "ultramassive"),
    (r"pre.?bang|bounce relics", "pre-bang"),
    (r"fermion freeze.?in", "gw-freeze"),
    (r"3D electron diffraction", "3d-ed"),
    (r"Cas13a|kinetic barcoding", "cas13a"),
    (r"boronate|synthetic cells|coacervat", "boronate"),
    (r"benzidine rearrangement", "mg-benz"),
    (r"chondrite|pressure bump", "chondrite"),
    (r"\bLoki\b|LMC star|ancient immigrant", "loki"),
    (r"IC\s*1262", "ic1262"),
    (r"high.?p_?T|\bISR\b|Levinthal", "isr"),
    (r"time goes quantum", "time-goes-q"),
    (r"\bSorci\b|second.?order Doppler", "sods"),
    (r"608.?Dalton|massive tunneling", "massive-cats"),
    (r"superradiant", "superradiant"),
    (r"weak.?valued excitation|negative weak", "weak-val"),
    (r"retrocausal|closed timelike", "retrocausal"),
    (r"second.?order.*gravitational.?wave strain|GW strain gauge", "2nd-gw"),
    (r"sunlight.*SPDC|ghost imaging.*sunlight|sunlight.*ghost", "sunlight"),
    (r"G292", "sn-onion"),
    (r"entropy maximization", "entropy-max"),
    (r"GW170817", "gw170817"),
    (r"primordial black hole|\bPBH\b", "pbh"),
    (r"\bDR21\b", "dr21"),
    (r"warm dense|dense plasma.*opacity|opacity revision", "dense-plasma"),
    (r"synchrotron.*dark matter", "sync-dm"),
    (r"gigaparsec", "gpc"),
    (r"leaky engine|gas pedal", "gas-pedal"),
    (r"three.?flavor|three.?s company|three.?body quantum", "three-body"),
    (r"naked black hole", "naked"),
    (r"twisted light.*chiral|chiral.*mass spectrometry", "twisted-ms"),
    (r"water.*double life|nanoconfinement", "water"),
    (r"macroscopic.*crystal.*entangl|neutron.*entangl", "macro-xtal"),
    (r"number state|photon.?number.*optical", "photon-num"),
    (r"two clocks.?one laser", "two-clocks"),
    (r"differential signaling", "diff-sig"),
    (r"light is a brake|optical friction|friction brake", "light-brake"),
    (r"electrons as piston|hot electron|\bPtCu\b", "hot-e"),
    (r"gravity as a compression|gravity from entropy|compression error", "grav-entropy"),
    (r"black hole recoil|recoiling black", "bh-recoil"),
    (r"\bMOND\b|external field effect|\bSPARC\b", "mond"),
    (r"STAR Collaboration|ultra.?peripheral|J/psi|photoproduction", "star-jpsi"),
    (r"proper time.*ion clock|ion clock.*proper time", "proper-time"),
    (r"quantum proper time", "qpt"),
    (r"\bNOON\b", "noon"),
    (r"randomness amplification", "rand-amp"),
]

candidates = []
skipped = []

for p in sorted(extracts.glob("*.md")):
    if p.name == "EXTRACT_REPORT.md":
        continue
    name = p.name
    size = p.stat().st_size
    head = p.read_text(encoding="utf-8", errors="replace")[:5000]
    m = re.search(r"(?m)^#\s+(.+)$", head)
    title = m.group(1).strip() if m else ""

    if name in map40:
        skipped.append((name, "map40", map40[name], size))
        continue
    jm = junk_re.search(name)
    if jm:
        skipped.append((name, "junk", jm.group(0), size))
        continue
    if size < 800:
        skipped.append((name, "thin", f"{size}B", size))
        continue

    hit = None
    for pat, lab in content_dups:
        if re.search(pat, head, re.I):
            hit = lab
            break
    if hit:
        skipped.append((name, "content-dup", hit, size))
        continue

    blob = name + " " + title + " " + head[:800]
    chem = bool(
        re.search(
            r"pharma|drug scaffold|mechanochemical|RNA polymerase|diarylacety|"
            r"lithium.?mediated|mass spectrometry|ruthenium|bond.?breaking|"
            r"quantum chemistry|observables versus|organic synthesis",
            blob,
            re.I,
        )
    )
    physics = bool(
        re.search(
            r"quantum|gravit|black hole|cosmo|plasma|photon|spin|nuclear|clock|"
            r"entangl|holograph|Lorentz|shear|filament|Hubble|vacuum|neutron|"
            r"crystal|confinement|dark matter|gamma|dissipation|third law|"
            r"color space|magneto|helium|molecular rotation|Peters|cosmic ray|"
            r"instanton|particle physics|ultrafast|Schrodinger|Schr.dinger|"
            r"boson|dark matter|South Pole|spin quiet|nucleus|fiber|"
            r"watching a black|scratchpad|hurricane|glimpse|sculpto|static|"
            r"droplet|two lasers|one bond|metal fall|stiffen|thinner|"
            r"ballistic film|Lorentz violation|emergent gravity|"
            r"quantum gravity|holographic|de Sitter|information paradox|"
            r"polarizable vacuum|tension was partly|Hubble tension",
            blob,
            re.I,
        )
    )
    if physics:
        tier = "physics"
    elif chem:
        tier = "chem"
    else:
        tier = "other"

    candidates.append(
        {
            "file": name,
            "size": size,
            "title": title[:120],
            "tier": tier,
            "preview": re.sub(r"\s+", " ", head[150:500])[:220],
        }
    )

print(f"\nSKIPPED: {len(skipped)}")
print(dict(Counter(s[1] for s in skipped)))
print(f"\nCANDIDATES: {len(candidates)}")

# Prefer physics, then larger files
candidates.sort(key=lambda x: (0 if x["tier"] == "physics" else 1 if x["tier"] == "chem" else 2, -x["size"], x["file"]))

for i, c in enumerate(candidates, 1):
    print(f"{i:2}. [{c['tier']:7}] {c['size']:7}  {c['file']}")
    print(f"    title: {c['title']}")

# Also list soft content-dups that might be alternate analyses worth a glance
print("\n--- content-dup skips (first 40) ---")
for s in skipped:
    if s[1] == "content-dup":
        print(f"  {s[0][:70]:70} -> {s[2]}")

outp = root / "claude_export" / "remaining_queue_wave2.json"
payload = {
    "built": "2026-08-02",
    "wiki_papers": len(wiki_slugs),
    "slugs40_count": len(slugs40),
    "candidates": candidates,
    "skipped": [{"file": s[0], "reason": s[1], "detail": s[2], "size": s[3]} for s in skipped],
    "batch1": [c["file"] for c in candidates if c["tier"] == "physics"][:5],
}
with open(outp, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2)
print(f"\nWrote {outp}")
print(f"Batch1 suggestion: {payload['batch1']}")
