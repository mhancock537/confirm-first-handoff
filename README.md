# Confirm First (Team 4B)

> Built at the Claude Impact Lab, Birmingham, August 28, 2026. This README follows the
> event's team README template. See SUBMISSIONS.md and JUDGING.md in the
> [event repository](https://github.com/Birmingham-AI/claude-impact-lab).

## Team

- **Team name:** Confirm First
- **Team ID:** 4B, confirmed at kickoff on August 28, 2026.
- **Team members (optional):** Three members. Names get added here only if all three opt in
  at submission.

## Challenge and primary user

- **Challenge:** 4, Improve the Handoff to Homelessness Services.
- **Primary user:** The family, not the person experiencing homelessness or the frontline
  responder the brief names by default. The team reframed the primary user on lab day. The
  family member is who makes the calls, and the moment that matters most happens before
  homelessness starts. The person they love is who every handoff ultimately serves.

## Problem and repeated workflow

Most people do not fall into homelessness in one step. For people with co-occurring mental
health and substance use needs, there are catchable moments first: an ER discharge with
nowhere to go, a walk-out from detox, a night the family cannot safely get through, an
eviction notice, another loop through jail and the ER. In each of those moments a family
faces four separate systems, crisis care, treatment, housing, and benefits, with no map, no
order of operations, and no way to know what is actually open. The repeated friction: who
do we call first, what must we confirm before anyone drives anywhere, and who owns the next
step. Families burn out guessing, and the person lands in the system this tool exists to
keep them out of.

## What the project does

A confirm-first family navigator. The family picks the moment they are in, from six
synthetic scenarios, and the card returns the calls to make first in order, the one thing
to confirm by phone before anyone travels, the safe next step, who owns it now, the point
where a trained person takes over, and when to check back. Scenarios split into two paths:
prevent entry into homelessness when a catchable moment exists, and navigate the systems in
the right order when entry cannot be avoided. The handoff summary stays locked until the
family marks the phone confirmation done. A human confirms. Then the card hands off. Below
the card, one page maps all four systems with real, verified front doors.

## Data and evidence sources

- `data/family-scenarios.csv`: 6 family scenarios, **all synthetic**, written by the team
  on August 28, 2026. Every row carries `is_synthetic=true` and every screen repeats the
  label. No real names, no PII, no client records, and the page has no way to enter any.
- `data/resources.csv`: 11 **real** organizations across crisis, treatment, housing,
  family support, and benefits. Each site was verified live on August 28, 2026, and the
  verification date shows in the page. Hours, beds, and openings were not verified and are
  labeled not live everywhere.
- `data/homelessness-handoff-scenarios.csv`: the event's synthetic dataset, kept as
  provenance. It powered version 1, a responder-facing card, before the team pivoted to
  the family on lab day.
- [One Roof](https://www.oneroofonline.org/): Coordinated Entry lead for the Birmingham
  area, the workflow boundary. Verified live August 28, 2026.
- [impact-birmingham.com](https://impact-birmingham.com): the team's evidence base on why
  referral navigation fails without funded humans. Key figure: North Carolina's NCCARE360
  platform resolved 88 percent of referrals with funded navigators and 30 percent without,
  on the same software. The detailed fact base sits behind a login on that site.

## Architecture or approach

A single `index.html`. No framework, no build step, no server, no dependencies, no forms,
no storage. Scenarios and resources are embedded as JavaScript constants so the page opens
from a file, and `tests/check-data.py` guards against drift between the CSVs and the page,
mutation-tested to prove it can fail. Claude built the repo, the app, the tests, and these
documents during the lab under the rules in `CLAUDE.md`, including the mid-day pivot from
responder card to family navigator. Claude does not appear in the artifact at run time. The
tool is deliberately deterministic: no model generates text about anyone's situation.

The design boundary does the safety work. The tool never scores, ranks, or predicts
anything about a person, never claims live capacity, never files a referral, never goes
around Coordinated Entry, and never records or transmits anything. Diagnosis words never
appear in a handoff summary. Its one mechanism is a gate: the summary unlocks only after a
human marks the phone confirmation done.

## Working artifact

[`index.html`](index.html) in this repository. Open it in a browser. Exact demo steps are
in [`DEMO.md`](DEMO.md). Also live for anyone with the link, no login, at
[mhh205.cloud/lab](https://mhh205.cloud/lab/).

## What works today

- All 6 synthetic family scenarios render the full six-step card with both path types.
- The call-first list resolves to real resources with verified sites and dates shown.
- The confirm gate works: NOT YET CONFIRMED and a locked copy button until the checkbox is
  ticked, then CONFIRMED and unlocked.
- The four-systems reference grid renders all 11 verified resources.
- The drift guard passes and was mutation-tested red and green on lab day.
- The demo path was walked in a real browser before every commit that touched it.

## Known limitations and simulated elements

The full living list is [`LIMITATIONS.md`](LIMITATIONS.md). The short version: every family
is fictional, the resources are real but nothing about them is live, the phone call is the
family's to make and the checkbox only records their say-so for the page visit, two
candidate resources were dropped as unverifiable on lab day, and the tool gives no medical
or legal advice.

## Next step toward a pilot

Put the navigator in front of a NAMI Alabama family support group and One Roof's
Coordinated Entry staff for a 30-minute review each: do the six moments match what families
actually face, and does the routing respect the real front doors. Owner: Mike Hancock
(mhancock537 on GitHub) sends both requests within one week of the lab. A pilot would need
each listed organization to confirm its own entry in the resource table, and funded humans
to own the confirmations, since the evidence says the humans are the active ingredient.

## Demo video (if needed)

Not needed. The artifact runs from a public repo in any browser with no setup.
