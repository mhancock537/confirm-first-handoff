#!/usr/bin/env python3
"""Drift guard: every field value in the CSV must appear verbatim in index.html."""
import csv, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text()
missing = []
with open(root / "data" / "homelessness-handoff-scenarios.csv") as f:
    for row in csv.DictReader(f):
        if row["is_synthetic"] != "true":
            missing.append(f'{row["scenario_id"]}: is_synthetic is not true')
        for key, val in row.items():
            if key in ("capacity_is_not_live", "is_synthetic"):
                continue
            if val not in html:
                missing.append(f'{row["scenario_id"]}.{key}: "{val}" not found in index.html')
for label in ("Synthetic", "not live", "NOT LIVE"):
    if label not in html:
        missing.append(f'required label missing from index.html: "{label}"')
if missing:
    print("DRIFT FOUND:")
    print("\n".join(missing))
    sys.exit(1)
print("OK: CSV and index.html agree, synthetic and not-live labels present.")
