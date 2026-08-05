from pathlib import Path
import json

root = Path(__file__).resolve().parent.parent
log = root / "wiki" / "log.md"
entry = """

---

## [2026-08-02] ingest | Export wave-2 batch 2/8 (papers 6–10) + lint links

### Papers created
6. category-79-quasar-wind — J2318 UV BAL wind ~0.3c
7. peters-cycle-cosmic-rays — DAMPE multi-species rigidity softening
8. fractional-fermi-sea-1d-bosons — holonomy fractional Fermi seas
9. quantum-state-sculptor — Oxford non-Gaussian oscillator cats
10. freeze-fiber-brillouin — frozen CS2 liquid-core Brillouin gain

### Lint at 10 (high-value bidirectional links)
- beyond-iron <-> peters-cycle; aquila-booster <-> peters + beyond-iron
- jwst-filament <-> category-79-quasar-wind
- massive-tunneling-cats <-> quantum-state-sculptor
- problem-of-time-cold-atoms <-> fractional-fermi-sea-1d-bosons
- two-clocks-one-laser <-> freeze-fiber-brillouin

### Concepts
- No new stubs

### Catalog
- **Papers: 103 · Concepts: 61 · Synthesis: 2**
- Wave-2 progress: **10 / 40**

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)

slugs = [
    "beyond-iron-ultraheavy-cosmic-rays",
    "nucleus-shell-src-memory",
    "black-hole-third-law-violation",
    "dissipative-cavity-entanglement",
    "jwst-filament-cnd-ngc4696",
    "category-79-quasar-wind",
    "peters-cycle-cosmic-rays",
    "fractional-fermi-sea-1d-bosons",
    "quantum-state-sculptor",
    "freeze-fiber-brillouin",
]
prog = {
    "wave": 2,
    "completed": 10,
    "target": 40,
    "batches_done": 2,
    "stopped": False,
    "papers_total": 103,
    "concepts_total": 61,
    "synthesis_total": 2,
    "new_slugs": slugs,
    "note": "Wave-2 batch 2 complete; lint links at 10 done; continue batches of 5; stub+index at 20; stop at 40",
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
print("disk papers", n, "concepts", c, "wave2", len(slugs))
