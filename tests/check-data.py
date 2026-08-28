#!/usr/bin/env python3
"""Drift guard: every field value in the CSVs must appear verbatim in index.html."""
import csv, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text()
missing = []

def check(csv_name, id_col, skip_cols, synthetic_col=None):
    with open(root / "data" / csv_name) as f:
        for row in csv.DictReader(f):
            if synthetic_col and row[synthetic_col] != "true":
                missing.append(f'{csv_name} {row[id_col]}: {synthetic_col} is not true')
            for key, val in row.items():
                if key in skip_cols:
                    continue
                if val not in html:
                    missing.append(f'{csv_name} {row[id_col]}.{key}: "{val}" not found in index.html')

check("family-scenarios.csv", "scenario_id",
      {"capacity_is_not_live", "is_synthetic", "path"}, synthetic_col="is_synthetic")
check("resources.csv", "resource_id", {"is_real"})

# The event dataset no longer feeds the page but stays as provenance, intact.
with open(root / "data" / "homelessness-handoff-scenarios.csv") as f:
    rows = list(csv.DictReader(f))
    if len(rows) != 6 or any(r["is_synthetic"] != "true" for r in rows):
        missing.append("event dataset homelessness-handoff-scenarios.csv altered")

for label in ("Synthetic", "not live", "NOT LIVE", "no diagnosis", "verified live"):
    if label not in html:
        missing.append(f'required label missing from index.html: "{label}"')

# The takeaway page is generated from the CSVs. Rebuild it and compare bytes, so a CSV
# edit without a regenerate, or a hand edit to takeaway.html, fails here.
sys.path.insert(0, str(root))
import gen_takeaway
try:
    expected = gen_takeaway.build()
    if expected != (root / "takeaway.html").read_text():
        missing.append("takeaway.html is stale: rerun python3 gen_takeaway.py and re-render takeaway.pdf")
except SystemExit as e:
    missing.append(f"apply-checklist.csv inconsistent: {e}")

if "takeaway.pdf" not in html:
    missing.append("index.html no longer links takeaway.pdf")
pdf = root / "takeaway.pdf"
if not pdf.exists() or pdf.stat().st_size < 20000:
    missing.append("takeaway.pdf missing or implausibly small: re-render it from takeaway.html")

if missing:
    print("DRIFT FOUND:")
    print("\n".join(missing))
    sys.exit(1)
print("OK: CSVs and index.html agree, synthetic, not-live, and no-diagnosis labels present.")
