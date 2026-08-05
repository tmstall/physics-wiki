from pathlib import Path
import json

root = Path(__file__).resolve().parent.parent
log = root / "wiki" / "log.md"
entry = """

---

## [2026-08-02] ingest | Export wave-2 batch 1/8 (5 papers)

Continue from remaining claude_export/extracted-analyses/ after wave-1 stop at 40.

### Queue
- Built claude_export/remaining_queue_wave2.json (~42 not-yet-in-wiki candidates after map40/junk/content-dup filters)
- Prefer physics-heavy Tier A; skip hard dups and soft overlaps

### Papers created
1. beyond-iron-ultraheavy-cosmic-rays — UH nuclei as UHECRs / Amaterasu path
2. nucleus-shell-src-memory — JLab CaFe SRC orbital memory
3. black-hole-third-law-violation — vacuum 5D finite-time extremality
4. dissipative-cavity-entanglement — dark-state many-body entanglement via cavity decay
5. jwst-filament-cnd-ngc4696 — JWST filament to CND feeding NGC 4696

### Concepts
- No new single-paper stubs (policy). Updated hub: black-hole-thermodynamics (third-law note)
- Bidirectional: noise-driven-qubit-entanglement <-> dissipative cavity; gas-pedal notes soft-dup of Lorentz extract

### Soft-dup not ingested
- Lorentz-violation emergent gravity extract maps to universe-gas-pedal-leaky (same Isichei-Magueijo Otto-cycle program)

### Catalog after batch 1
- **Papers: 98 · Concepts: 61 · Synthesis: 2**
- Wave-2 progress: **5 / 40**

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)

slugs = [
    "beyond-iron-ultraheavy-cosmic-rays",
    "nucleus-shell-src-memory",
    "black-hole-third-law-violation",
    "dissipative-cavity-entanglement",
    "jwst-filament-cnd-ngc4696",
]
prog = {
    "wave": 2,
    "completed": 5,
    "target": 40,
    "batches_done": 1,
    "stopped": False,
    "papers_total": 98,
    "concepts_total": 61,
    "synthesis_total": 2,
    "new_slugs": slugs,
    "note": "Wave-2 batch 1 complete; continue batches of 5; lint at 10; stub+index at 20; stop at 40",
    "soft_dups_skipped": [
        {
            "file": "2026-06-25_lorentz-violation-in-emergent-gravity-and-cosmological-accel_1a6d0e13.md",
            "maps_to": "universe-gas-pedal-leaky",
        }
    ],
}
(root / "claude_export" / "INGEST_PROGRESS_WAVE2.json").write_text(
    json.dumps(prog, indent=2), encoding="utf-8"
)
(root / "claude_export" / "new_papers_wave2.json").write_text(
    json.dumps([{"slug": s} for s in slugs], indent=2), encoding="utf-8"
)
n = len(list((root / "wiki" / "papers").glob("*.md")))
c = len(list((root / "wiki" / "concepts").glob("*.md")))
print("progress written; disk papers", n, "concepts", c)
