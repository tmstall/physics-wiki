import json
from pathlib import Path

d = json.loads(Path("spacex_export/TRIAGE.json").read_text(encoding="utf-8"))
print(d["counts"])
for b in ["NEW", "SOFT-DUP", "THIN-SKIP"]:
    print("====", b, d["counts"][b])
    for i in d["items"]:
        if i["bucket"] == b:
            wiki = ",".join(i.get("closest_wiki") or [])
            print(f"  {i['title'][:90]}")
            print(f"    -> {wiki} | {i.get('note','')[:100]}")
