#!/usr/bin/env python3
"""Generate takeaway.html from data/resources.csv and data/apply-checklist.csv.

The committed takeaway.html is a build product of the two CSVs. tests/check-data.py
regenerates it and fails on any byte difference, so the CSVs stay the source of record.
Rerun after any CSV change:  python3 gen_takeaway.py
Then re-render the PDF (see DEMO.md deploy notes):
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
    --print-to-pdf=takeaway.pdf --no-pdf-header-footer takeaway.html
"""
import csv
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent


def esc(s):
    return html.escape(s, quote=True)


def load(name):
    with open(ROOT / "data" / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def entry(r, a):
    ready = "".join(
        f'<li>{esc(part.strip())}</li>' for part in a["have_ready"].split("|")
    )
    src = a["source_url"]
    dx = ""
    if a.get("diagnosis_note", "").strip():
        dx = f'\n  <p class="dx"><strong>Medical diagnosis:</strong> {esc(a["diagnosis_note"])}</p>'
    return f"""<section class="entry">
  <h3>{esc(r["name"])}</h3>
  <p class="what">{esc(r["what_it_is"])}.</p>
  <p><strong>How to apply or reach them:</strong> {esc(a["how_to_apply"])}</p>
  <p class="ready-label"><strong>Have ready:</strong></p>
  <ul class="ready">{ready}</ul>{dx}
  <p class="src">Source: <a href="{esc(src)}">{esc(src.replace("https://", ""))}</a> &middot; verified {esc(a["verified"])}</p>
</section>"""


def build():
    resources = {r["resource_id"]: r for r in load("resources.csv")}
    checklist = load("apply-checklist.csv")
    apply_ids = [a["resource_id"] for a in checklist if a["application_needed"] == "true"]
    call_ids = [a["resource_id"] for a in checklist if a["application_needed"] != "true"]
    by_id = {a["resource_id"]: a for a in checklist}

    missing = set(resources) ^ set(by_id)
    if missing:
        raise SystemExit(f"apply-checklist.csv and resources.csv disagree on ids: {sorted(missing)}")

    applies = "\n".join(entry(resources[i], by_id[i]) for i in apply_ids)
    calls = "\n".join(entry(resources[i], by_id[i]) for i in call_ids)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Application checklist &middot; Help the Homeless</title>
<style>
  :root {{ --ink: #1c1a17; --muted: #5c564e; --line: #d8d2c8; --amber: #9a6a1e; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: #fff;
         margin: 0 auto; max-width: 46rem; padding: 1.5rem 1.25rem 2.5rem; line-height: 1.45; }}
  h1 {{ font-size: 1.6rem; margin: 0 0 0.25rem; }}
  h2 {{ font-size: 1.15rem; border-bottom: 2px solid var(--ink); padding-bottom: 0.2rem;
        margin: 1.6rem 0 0.6rem; }}
  h3 {{ font-size: 1.02rem; margin: 0 0 0.2rem; }}
  p {{ margin: 0.25rem 0; }}
  .lede {{ color: var(--muted); margin-bottom: 0.75rem; }}
  .notice {{ border: 1.5px solid var(--ink); padding: 0.6rem 0.75rem; font-size: 0.9rem;
             margin: 0.75rem 0 0.25rem; }}
  .notice strong {{ text-transform: uppercase; letter-spacing: 0.04em; font-size: 0.82rem; }}
  .entry {{ border-top: 1px solid var(--line); padding: 0.65rem 0 0.5rem;
            break-inside: avoid; page-break-inside: avoid; }}
  .what {{ color: var(--muted); font-style: italic; }}
  ul.ready {{ margin: 0.15rem 0 0.35rem; padding-left: 0; list-style: none; }}
  ul.ready li {{ padding-left: 1.5rem; position: relative; margin: 0.18rem 0; }}
  ul.ready li::before {{ content: "\\2610"; position: absolute; left: 0.2rem; }}
  .ready-label {{ margin-bottom: 0; }}
  .src {{ font-size: 0.82rem; color: var(--muted); }}
  .src a {{ color: var(--muted); }}
  .dx {{ border-left: 3px solid var(--amber); padding: 0.3rem 0.6rem; margin: 0.4rem 0;
         font-size: 0.92rem; background: #faf5ec; break-inside: avoid; }}
  .hotlines {{ margin-top: 1.5rem; border: 2px solid var(--ink); padding: 0.7rem 0.8rem;
               font-size: 1.05rem; break-inside: avoid; page-break-inside: avoid; }}
  .footer {{ margin-top: 1rem; font-size: 0.82rem; color: var(--muted); }}
  @page {{ size: Letter; margin: 0.6in; }}
  @media print {{ body {{ max-width: none; padding: 0; }} a {{ text-decoration: none; }} }}
</style>
</head>
<body>
<h1>Application checklist</h1>
<p class="lede">What to have ready for every resource in the Help the Homeless guide.
Built at the Claude Impact Lab, Birmingham, August 28, 2026.</p>
<div class="notice">
  <strong>Read this first.</strong> Every item below comes from each organization's own
  public site, verified on 2026-08-28, and nothing more. Requirements change and vary by
  program, so confirm with each agency before you gather documents. Where a site publishes
  no checklist, this page says so instead of guessing. This is a printable takeaway from a
  demo tool, not legal, medical, or benefits advice, and nothing in it is a live feed.
  No door in the call-first list requires you to arrive with a medical diagnosis. Where a
  program's eligibility runs on one, its entry says so and names who makes that decision.
</div>

<h2>Applications to start</h2>
<p class="lede">These take time. Starting them early is part of setting the person up to succeed.</p>
{applies}

<h2>Call first, no application needed</h2>
<p class="lede">These doors open with a phone call or a visit to the site.</p>
{calls}

<div class="hotlines">
  <strong>In a crisis right now:</strong> call or text <strong>988</strong>.
  For referrals to food, housing, and health care: dial <strong>2-1-1</strong>
  or text your ZIP to <strong>898-211</strong>. If anyone is in danger, call <strong>911</strong>.
</div>
<p class="footer">Help the Homeless &middot; Team 4B &middot; github.com/mhancock537/confirm-first-handoff
&middot; This page collects nothing and sends nothing. No name or personal detail appears on it.</p>
</body>
</html>
"""
    return page


def main():
    page = build()
    (ROOT / "takeaway.html").write_text(page, encoding="utf-8")
    print(f"wrote takeaway.html ({len(page)} bytes)")


if __name__ == "__main__":
    main()
