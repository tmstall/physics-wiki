"""Extract first ~12k body chars of batch-2 sources for ingest."""
import re
from pathlib import Path

root = Path(__file__).resolve().parent
src = root / "extracted-analyses"
out = root / "_batch2_extracts"
out.mkdir(exist_ok=True)

files = {
    "category-79-quasar-wind": "2026-06-06_category-79-hurricane-in-space_098f3cd6.md",
    "peters-cycle-cosmic-rays": "2026-05-02_peters-cycle-confirmed-charge-dependent-cosmic-ray-spectral_a9c50c9b.md",
    "1d-bose-exotic-critical": "2026-06-19_the-sea-that-forgot-half-its-water-bosons_27a5c392.md",
    "quantum-state-sculptor": "2026-06-10_the-quantum-state-sculpto_35bae5fb.md",
    "freeze-fiber-brillouin": "2026-07-22_freeze-the-fiber-not-the-budget_e1d211de.md",
}

for slug, fn in files.items():
    t = (src / fn).read_text(encoding="utf-8", errors="replace")
    body = re.sub(r"^---.*?---\s*", "", t, count=1, flags=re.S)
    (out / f"{slug}.txt").write_text(body[:14000], encoding="utf-8")
    print(slug, "ok", len(body))
