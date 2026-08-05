"""Build remaining unique extract queue after wave-2 papers 1-10."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
extracts = root / "claude_export" / "extracted-analyses"
wiki = {p.stem for p in (root / "wiki" / "papers").glob("*.md")}
w2 = json.loads((root / "claude_export" / "new_papers_wave2.json").read_text(encoding="utf-8"))
done_w2 = {x["slug"] for x in w2}
done40 = {x["slug"] for x in json.loads((root / "claude_export" / "new_papers_40.json").read_text(encoding="utf-8"))}

# Extract files already used as sources for wiki pages
used_sources = set()
for p in (root / "wiki" / "papers").glob("*.md"):
    t = p.read_text(encoding="utf-8", errors="replace")[:2000]
    for m in re.finditer(r"extracted-analyses/([^\s\"']+\.md)", t):
        used_sources.add(m.group(1))

# Explicit map of extract filename -> already handled
done_files = {
    "2026-06-14_beyond-iron-the-universe-s-most-violent-events-may-be-firing_344a8eb5.md",
    "2026-06-05_the-nucleus-has-a-memory_9f350308.md",
    "2026-06-05_the-third-law-is-dead_911cf359.md",
    "2026-06-06_dissipation-as-a-feature-not-a-bug_e3b36343.md",
    "2026-07-19_watching-a-black-hole-set-the-table-a-filament-caught-feedin_2745e811.md",
    "2026-06-06_category-79-hurricane-in-space_098f3cd6.md",
    "2026-05-02_peters-cycle-confirmed-charge-dependent-cosmic-ray-spectral_a9c50c9b.md",
    "2026-06-19_the-sea-that-forgot-half-its-water-bosons_27a5c392.md",
    "2026-06-10_the-quantum-state-sculpto_35bae5fb.md",
    "2026-07-22_freeze-the-fiber-not-the-budget_e1d211de.md",
    # wave1 map + soft dups already in wiki
    "2026-06-25_lorentz-violation-in-emergent-gravity-and-cosmological-accel_1a6d0e13.md",
}

junk_re = re.compile(
    r"(framework|paper-analysis_|paper-analysis-details|reviewing-prior-session|"
    r"finding-a-matching-paper|finding-and-analyzing|finding-detailed-nasa|"
    r"patent-analysis|mit-paper-analysis|comparative-analysis-of-two|untitled_|"
    r"measurement-problem-threads|create-v3-9-framework|here-s-a-reference-from-a-post|"
    r"technical-paper-analysis-framework|EXTRACT_REPORT)",
    re.I,
)

# Soft content dups of existing wiki (patterns checked on head)
content_dups = [
    (r"Brown.?Zak|Brown–Zak", "brown-zak"),
    (r"gravastar", "gravastar"),
    (r"Th-229|229Th|thorium.?229", "thorium"),
    (r"problem of time|Barontini", "problem-of-time"),
    (r"GW250114", "horizon-wave"),
    (r"noise.?driven.*entangl|two-mode correlated microwave", "noise-driven"),
    (r"Big Ring", "big-ring"),
    (r"Euclid.*quasar|31 new quasars", "euclid"),
    (r"Terzan 5", "terzan"),
    (r"\bSnTe\b", "snte"),
    (r"truncated photon|dynamical Casimir", "truncated"),
    (r"mLQC|Bianchi.I", "mlqc"),
    (r"attosecond.*STM|lightwave.?driven STM", "attostm"),
    (r"spin.?flip.?flop|synthetic antiferromagnet", "saf"),
    (r"\bCISS\b|chiral.?induced spin selectivity", "ciss"),
    (r"SUPER protocol|\bSnV\b|tin.?vacancy", "snv"),
    (r"quantum jamming", "jamming"),
    (r"evaporating charged black", "evap"),
    (r"frozen.?in gravitational|frozen.?in gravity", "frozen"),
    (r"DESI.*dark energy|evolving dark energy", "desi"),
    (r"\bkSZ\b|kinetic Sunyaev", "ksz"),
    (r"photonic supersolid", "supersolid"),
    (r"B.?meson|flavor anomaly", "bmeson"),
    (r"Aquila.*PeV|PeVatron", "aquila"),
    (r"dual quasars|high.?z quasar pair", "dualq"),
    (r"Mrk\s*501", "mrk"),
    (r"\bITO\b|fieldoscop", "ito"),
    (r"collapse models.*clock|\bCSL\b", "csl"),
    (r"W.?state.*entangled", "wstate"),
    (r"Shor algorithm|qLDPC", "shor"),
    (r"certified randomness", "rand"),
    (r"relativistic amplifier|flying mirror", "plasma"),
    (r"beam.?driven plasma", "beam"),
    (r"plasma birth|filming plasma", "film"),
    (r"color superconduct", "csc"),
    (r"charge density wave|quantum metallurgy", "cdw"),
    (r"BaTa2S5", "bata"),
    (r"\bSiV\b", "siv"),
    (r"Hawking.*charge shell|double.?copy.*Hawking", "shell"),
    (r"Alena tensor", "alena"),
    (r"eta.?prime|η.?prime", "eta"),
    (r"topological cosmological constant", "lambda"),
    (r"COSMOS.?Web", "cosmos"),
    (r"CIGaRS", "cigars"),
    (r"HOLISMOKES|SN Winny", "holi"),
    (r"SPHEREx|interstellar glaciers", "spherex"),
    (r"pulsars.*satellite|satellite masses.*pulsar", "pulsar"),
    (r"SMBH inclination", "inc"),
    (r"ultramassive", "ultra"),
    (r"pre.?bang|bounce relics", "prebang"),
    (r"fermion freeze.?in", "freezein"),
    (r"3D electron diffraction", "3ded"),
    (r"Cas13a|kinetic barcoding", "cas"),
    (r"boronate|synthetic cells|coacervat", "boro"),
    (r"benzidine rearrangement", "benz"),
    (r"chondrite|pressure bump", "chond"),
    (r"\bLoki\b|LMC star|ancient immigrant", "loki"),
    (r"IC\s*1262", "ic"),
    (r"high.?p_?T|\bISR\b|Levinthal", "isr"),
    (r"time goes quantum", "tgq"),
    (r"\bSorci\b|second.?order Doppler", "sods"),
    (r"608.?Dalton|massive tunneling", "cats"),
    (r"superradiant", "superrad"),
    (r"weak.?valued excitation|negative weak", "weak"),
    (r"retrocausal|closed timelike", "retro"),
    (r"second.?order.*gravitational.?wave strain", "2ndgw"),
    (r"sunlight.*SPDC|ghost imaging.*sunlight", "sun"),
    (r"G292", "sn"),
    (r"entropy maximization", "entmax"),
    (r"GW170817", "gw17"),
    (r"primordial black hole|\bPBH\b", "pbh"),
    (r"\bDR21\b", "dr21"),
    (r"warm dense|dense plasma.*opacity", "dense"),
    (r"synchrotron.*dark matter", "sync"),
    (r"gigaparsec", "gpc"),
    (r"leaky engine|gas pedal", "gas"),
    (r"three.?flavor|three.?s company", "3body"),
    (r"naked black hole", "naked"),
    (r"twisted light.*chiral|chiral.*mass spectrometry", "twisted"),
    (r"water.*double life|nanoconfinement", "water"),
    (r"macroscopic.*crystal.*entangl|neutron.*entangl", "macro"),
    (r"number state|photon.?number.*optical", "pnum"),
    (r"two clocks.?one laser", "2clk"),
    (r"differential signaling", "diff"),
    (r"light is a brake|optical friction|friction brake", "brake"),
    (r"electrons as piston|hot electron|\bPtCu\b", "hote"),
    (r"gravity as a compression|gravity from entropy|compression error", "gfe"),
    (r"black hole recoil|recoiling black", "recoil"),
    (r"\bMOND\b|external field effect|\bSPARC\b", "mond"),
    (r"STAR Collaboration|ultra.?peripheral|J/psi|photoproduction", "star"),
    (r"Peters cycle|DAMPE.*softening|15 TV", "peters"),
    (r"J2318|Category 79|77,?000 km", "cat79"),
    (r"fractional Fermi|super.?Tonks|Lieb.?Liniger.*holonomy", "fermi1d"),
    (r"trisqueez|quadsqueez|state sculpt", "sculpt"),
    (r"liquid.?core|Brillouin.*freez|CS2|CS.?2", "freeze"),
    (r"third law.*black hole|surface gravity.*finite time|Myers.?Perry.*extremal", "3rdlaw"),
    (r"short.?range correlat|CaFe|\^\{?40\}?Ca.*\^\{?48\}?Ca", "src"),
    (r"Amaterasu|ultraheavy|beyond iron", "uh"),
    (r"dissipation as a feature|AKLT|dark.?state.*cavity", "dissip"),
    (r"filament.*feeding|NGC 4696|circumnuclear disk", "filament"),
    (r"Isichei|Magueijo|Otto cycle.*emergent", "otto"),
]

# Prefer order: solid unique physics first
priority = [
    "2026-07-05_the-black-hole-that-flipped-its-radio-switch-and-left-it-on_9b801f92.md",
    "2026-06-10_glimpse-17775-inside-the-cocoon_73204815.md",
    "2026-07-09_south-pole-telescope-analysis_cad1e155.md",
    "2026-06-26_magneto-optical-trapping-of-metal-hydride-molecules_a175fb0e.md",
    "2026-07-04_molecular-rotation-control-in-superfluid-helium_bb64afb7.md",
    "2026-06-26_the-droplet-that-rewrites-the-ring_69f8581e.md",
    "2026-07-26_the-nucleus-tells-on-itself_edc2587e.md",
    "2026-06-16_confinement-stiffening-in-nanoscale-ballistic-films_6b9b99ac.md",
    "2026-06-16_why-thinner-is-tougher_de07cf13.md",
    "2026-07-09_letting-a-metal-fall-apart-on-purpose_6609c393.md",
    "2026-04-30_topological-control-of-chirality-and-spin-with-structured-li_c172b505.md",
    "2026-06-09_color-space-has-potholes_0a5c3ef4.md",
    "2026-06-25_quantum-gravity-deep-dive-1-from-black-hole-mergers-to-spont_0b25cbf8.md",
    "2026-06-27_quantum-gravity-deep-dive-2-outside-project-from-information_5c0fdae0.md",
    "2026-06-28_quantum-gravity-deep-dive-3-holographic-codes-and-bulk-recon_447ad3f1.md",
    "2026-06-29_quantum-gravity-deep-dive-4-de-sitter-holography-and-quantum_cea522d1.md",
    "2026-04-08_mass-and-instatons-zero-modes_7b9a60cf.md",
    "2026-07-11_the-tension-was-partly-in-the-ruler_7fd96459.md",
    "2026-06-21_the-bullet-that-didn-t-need-dark-matter_12fa6547.md",
    "2026-07-26_todd-intended-the-spin-quiet-partner-that-almost-never-shows_de8ad8dd.md",
    "2026-03-12_ultrafast-chemical-shifts-analysis_653e2cb3.md",
    "2026-07-03_two-lasers-one-reaction_942df2d8.md",
    "2026-06-06_the-gpu-moment-for-mass-spectrometry_d44aa7e3.md",
    "2026-07-09_the-bond-breaking-discount_30ce2966.md",
    "2026-06-03_millisecond-pharma-factory-drug-scaffold-rings-built-in-mida_20cc3e4b.md",
    "2026-07-04_a-single-ruthenium-atom-that-both-lights-the-match-and-bends_9beb4c8d.md",
    "2026-05-01_water-molecules-in-rna-polymerase-ii-catalysis_90d5cce7.md",
    "2026-06-17_paper-analysis-on-sulfur-chemistry-in-interstellar-ice_d08f1727.md",
    "2026-07-22_finding-the-bias-point-where-a-molecule-stops-listening_1bb5fc5d.md",
    "2026-07-26_todd-actual-the-resistance-tax-how-breaking-the-one-enzyme-t_93719d40.md",
    "2026-07-12_one-bond-and-done_b51aa206.md",
    "2026-07-07_the-model-keeps-a-small-readable-scratchpad-and-that-s-where_c964decd.md",
    "2026-06-18_schrodinger-s-cat-but-weirder_acd4b7cd.md",
    "2026-07-21_polarizable-vacuum-framework-analysis_c3317248.md",
]

candidates = []
skipped = []

for p in sorted(extracts.glob("*.md")):
    name = p.name
    if name == "EXTRACT_REPORT.md":
        continue
    if name in done_files or name in used_sources:
        skipped.append((name, "already-used"))
        continue
    if junk_re.search(name):
        skipped.append((name, "junk"))
        continue
    size = p.stat().st_size
    if size < 1500:
        skipped.append((name, "thin"))
        continue
    head = p.read_text(encoding="utf-8", errors="replace")[:5000]
    hit = None
    for pat, lab in content_dups:
        if re.search(pat, head, re.I):
            hit = lab
            break
    if hit:
        skipped.append((name, f"content-dup:{hit}"))
        continue
    m = re.search(r"(?m)^#\s+(.+)$", head)
    title = m.group(1).strip() if m else name
    # classify
    chem = bool(re.search(
        r"pharma|drug|mechanochemical|RNA polymerase|ruthenium|bond.?breaking|"
        r"organic|enzyme|resistance tax|one bond|mass spectrometry|diarylacety",
        name + title + head[:600], re.I))
    ai = bool(re.search(r"scratchpad|language model|Jacobian lens|Anthropic", name + title + head[:400], re.I))
    tier = "ai" if ai else ("chem" if chem else "physics")
    # slug guess
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}_", "", name)
    slug = re.sub(r"_[a-f0-9]{8}\.md$", "", slug)
    slug = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")[:60]
    candidates.append({
        "file": name,
        "title": title[:120],
        "size": size,
        "tier": tier,
        "slug_guess": slug,
    })

# Sort by priority list then size
prio_idx = {f: i for i, f in enumerate(priority)}
candidates.sort(key=lambda c: (prio_idx.get(c["file"], 999), 0 if c["tier"] == "physics" else 1, -c["size"]))

out = {
    "wiki_papers": len(wiki),
    "wave2_done": sorted(done_w2),
    "candidates": candidates,
    "skipped_count": len(skipped),
    "skipped_sample": skipped[:40],
}
(root / "claude_export" / "remaining_after_10.json").write_text(
    json.dumps(out, indent=2), encoding="utf-8"
)
print(f"wiki={len(wiki)} candidates={len(candidates)} skipped={len(skipped)}")
for i, c in enumerate(candidates, 1):
    print(f"{i:2}. [{c['tier']:6}] {c['size']:6}  {c['file'][:65]}")
    print(f"    slug~ {c['slug_guess']}")
    print(f"    {c['title'][:90]}")
