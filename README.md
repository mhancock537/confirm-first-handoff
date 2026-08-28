# Confirm First (Team 4B)

> Built at the Claude Impact Lab, Birmingham, August 28, 2026. This README follows the
> event's team README template. See SUBMISSIONS.md and JUDGING.md in the
> [event repository](https://github.com/Birmingham-AI/claude-impact-lab).

**This is a learning lab demonstration. No part of this website or repository should be
used in a crisis situation. In an emergency call 911. For a mental health crisis call or
text 988.** Full terms in [Disclaimers](#disclaimers).

## Team

- **Team name:** Confirm First
- **Team ID:** 4B, confirmed at kickoff on August 28, 2026.
- **Team members (optional):** Mike Hancock, Alex Romi, Darby Westfall, Bobbie.

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
to confirm by phone before anyone travels, the safe next step, the benefit and housing
applications to start now so the person is set up to succeed after the crisis, who owns it
now, the point where a trained person takes over, and when to check back. Scenarios split into two paths:
prevent entry into homelessness when a catchable moment exists, and navigate the systems in
the right order when entry cannot be avoided. The handoff summary stays locked until the
family marks the phone confirmation done. A human confirms. Then the card hands off. Below
the card, one page maps all four systems with real, verified front doors. Every card also
carries a button that opens a printable application checklist PDF: every resource in the
guide, how to apply, and what to have ready, each entry sourced to the organization's own
site and dated, so the family leaves with paper in hand.

## Data and evidence sources

- `data/family-scenarios.csv`: 6 family scenarios, **all synthetic**, written by the team
  on August 28, 2026. Every row carries `is_synthetic=true` and every screen repeats the
  label. No real names, no PII, no client records, and the page has no way to enter any.
- `data/resources.csv`: 13 **real** organizations across crisis, treatment, housing,
  family support, and benefits. Each site was verified live on August 28, 2026, and the
  verification date shows in the page. Hours, beds, and openings were not verified and are
  labeled not live everywhere.
- `data/apply-checklist.csv`: what each of the 13 resources needs from an applicant, taken
  only from each organization's own public site on August 28, 2026, source URL cited per
  row. Where a site publishes no checklist, the row says to ask. Feeds the printable
  takeaway (`takeaway.html`, `takeaway.pdf`) through `gen_takeaway.py`, guarded by the
  same drift test as the page.
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

- All 6 synthetic family scenarios render the full seven-step card with both path types,
  including the set-up-to-succeed step with timing matched to each scenario's moment.
- The call-first list resolves to real resources with verified sites and dates shown.
- The confirm gate works: NOT YET CONFIRMED and a locked copy button until the checkbox is
  ticked, then CONFIRMED and unlocked.
- The four-systems reference grid renders all 13 verified resources.
- Every card links the printable application checklist PDF, generated from the resource
  data, five pages, sourced and dated per entry.
- The drift guard passes and was mutation-tested red and green on lab day, including the
  checklist data.
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

## Plan to put the tool in front of families

This is a proposed plan. Nothing below has been printed or placed anywhere yet.

A tool nobody finds does not help anyone. The pilot review above tests whether the routing
is right. This plan gets the link in front of a family at the moment they need it, before
they start guessing.

**Where:** the same catchable moments the six scenarios describe. A card and a one-page
handout at hospital ER discharge desks, at the Jefferson County Jail release area, at
Crisis Center Birmingham and other 988 intake points, at One Roof's Coordinated Entry front
door, and at NAMI Alabama family support meetings.

**What gets placed:** a small card with a QR code to mhh205.cloud/lab, and a handout with
the same code plus the 988 and 211 numbers printed large. Both state plainly that the tool
is a synthetic-scenario demo, not a live directory, until a pilot says otherwise.

**Who approves it:** each site's own staff. No card or handout goes on a wall, a discharge
folder, or a jail release packet without that site agreeing first.

**Owner and timing:** Mike Hancock raises the placement idea in the same NAMI Alabama and
One Roof conversations named in the pilot review, then extends it to a hospital and the
jail once one of the first two says yes.

**What proves it worked:** a site agrees to a physical placement, or a family who saw a
card reaches a step 2 call.

## Disclaimers

1. **Learning lab project.** This project was built in a single day at the Claude Impact
   Lab, Birmingham, Alabama, on August 28, 2026, for educational and demonstration
   purposes only. It is a prototype, not a service, and no organization operates it.
2. **Not for crisis use.** No part of this website or repository should be used in a
   crisis situation. If anyone is in danger, call 911. For a mental health or substance
   use crisis, call or text 988. For referrals to food, housing, and health care, dial
   2-1-1.
3. **Not professional advice.** Nothing here is medical, clinical, legal, or financial
   advice, and nothing here substitutes for the judgment of a trained professional. The
   tool deliberately routes every consequential decision to a person.
4. **No affiliation or endorsement.** The organizations named in this project are real,
   but none of them are affiliated with this project, and none of them have reviewed,
   approved, or endorsed it. Their inclusion means only that their public site was
   reachable on August 28, 2026.
5. **Information is point in time.** Every fact was verified only as described, on
   August 28, 2026, from public sources. Phone numbers, requirements, programs, and
   organizations change. Nothing here updates itself.
6. **Nothing is live.** This project makes no claim about hours, bed availability,
   capacity, eligibility, wait lists, or acceptance, anywhere, at any time.
7. **All scenarios are fictional.** Every family and situation shown is synthetic,
   labeled as such, and describes no real person or case.
8. **No data collection.** The site has no forms, no accounts, no analytics, and no
   storage of visitor information. It records nothing and sends nothing.
9. **No warranty.** This project is provided as is, without warranty of any kind,
   express or implied. Use of any part of it is at the user's own risk.

## Demo video (if needed)

Not needed. The artifact runs from a public repo in any browser with no setup.
