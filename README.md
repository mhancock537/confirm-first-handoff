# Confirm First (Team 4X)

> Built at the Claude Impact Lab, Birmingham, August 28, 2026. This README follows the
> event's team README template. See SUBMISSIONS.md and JUDGING.md in the
> [event repository](https://github.com/Birmingham-AI/claude-impact-lab).

## Team

- **Team name:** Confirm First
- **Team ID:** Unverified. One of 4A, 4B, or 4C. The event's assignment table lists team
  IDs without member names, so the ID gets confirmed with organizers at kickoff and
  corrected here before submission.
- **Team members (optional):** Three members. Names get added here only if all three opt in
  at submission.

## Challenge and primary user

- **Challenge:** 4, Improve the Handoff to Homelessness Services.
- **Primary user:** The frontline responder standing with a person who needs the next safe
  step. The person experiencing homelessness is who the handoff serves.

## Problem and repeated workflow

A responder meets someone who needs shelter, cooling, respite, or daytime services. The
repeated moment of friction: fragmented information, capacity that changes hour to hour,
and no clear answer to three questions. What is the safe next step? What must be confirmed
before anyone travels? Who owns the follow-up? People get sent across town to closed doors,
and they retell their story at every stop.

## What the project does

One confirm-first handoff card. The responder picks a situation and the card returns five
things: the situation stated with dignity, the safe next step, the one thing to confirm by
phone before anyone travels, the named handoff owner, and the follow-up window. The handoff
summary stays locked until the responder marks the phone confirmation done. A human
confirms. Then the card hands off. The summary contains no sensitive personal data and
names the point where a trained person takes over.

## Data and evidence sources

- `data/homelessness-handoff-scenarios.csv`: 6 scenarios, **all synthetic**, from the
  event's resource pack. Every row carries `is_synthetic=true`, and every screen and every
  output of the app repeats the synthetic label. No real names, no PII, no client records.
- [One Roof](https://www.oneroofonline.org/): the Coordinated Entry lead for the Birmingham
  area, cited as the workflow boundary. Verified live on August 28, 2026.
- [impact-birmingham.com](https://impact-birmingham.com): the team's evidence base on why
  referral navigation fails without funded humans. Key figure: North Carolina's NCCARE360
  platform resolved 88 percent of referrals with funded navigators and 30 percent without,
  on the same software. The detailed fact base sits behind a login on that site.

## Architecture or approach

A single `index.html`. No framework, no build step, no server, no dependencies. The 6
synthetic scenarios are embedded as a JavaScript constant so the page opens from a file.
`tests/check-data.py` guards against drift between the CSV and the embedded copy, and it
checks the synthetic and not-live labels are present. Claude built the repo, the app, the
tests, and these documents during the lab, working under the rules in `CLAUDE.md`. Claude
does not appear in the artifact at run time. The tool is deliberately deterministic: no
model generates text about a person's situation.

The design boundary does the safety work. The tool never scores or ranks anyone, never
claims live capacity, never files a referral, and never goes around Coordinated Entry. Its
one mechanism is a gate: the handoff summary unlocks only after a human marks the phone
confirmation done.

## Working artifact

[`index.html`](index.html) in this repository. Open it in a browser. Exact demo steps are
in [`DEMO.md`](DEMO.md).

## What works today

- All 6 synthetic scenarios render a full five-step card.
- The confirm gate works: the summary reads NOT YET CONFIRMED and the copy button stays
  locked until the checkbox is ticked, then the summary flips to CONFIRMED and unlocks.
- Copy summary puts the plain-text handoff on the clipboard.
- The drift guard test passes, and it was mutation-tested to prove it can fail.
- The demo path was walked in a real browser before every commit that touched it.

## Known limitations and simulated elements

The full living list is [`LIMITATIONS.md`](LIMITATIONS.md). The short version: every
scenario and every resource is fictional, capacity is never live anywhere, the phone call
is described but not performed, and the checkbox records nothing and sends nothing.

## Next step toward a pilot

Put the card in front of One Roof's Coordinated Entry staff for a 30-minute review of the
five-step structure against their real intake flow. Owner: Mike Hancock
(mhancock537 on GitHub) sends the request within one week of the lab. A pilot would need
One Roof to supply real resource lists and phone numbers, and funded staff to own the
confirmations, since the evidence says the humans are the active ingredient.

## Demo video (if needed)

Not needed. The artifact runs from a public repo in any browser with no setup.
