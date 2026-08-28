# Limitations

The living list. Every faked, mocked, hardcoded, or synthetic thing gets a line here the
moment it enters the repo. Do not trust this tool for anything a line below rules out.

## Synthetic

- Every scenario is synthetic. The 6 family scenarios in `data/family-scenarios.csv` are
  fictional, marked `is_synthetic=true`, and were written by the team on 2026-08-28 for
  the dual-diagnosis pivot. No scenario describes a real family or a real case.
- The event's original dataset, `data/homelessness-handoff-scenarios.csv`, also fully
  synthetic, stays in the repo as provenance. It powered version 1 (a responder-facing
  card) and no longer feeds the page. Added 2026-08-28.

## Real but not live

- The 13 resources in `data/resources.csv` are real organizations. Each site was verified
  live on 2026-08-28 by loading it that day. That is the entire claim. Hours, beds,
  openings, intake rules, and eligibility were not verified and are never live in this
  tool. Every screen repeats the not-live label. Added 2026-08-28 with the pivot.
- The only phone numbers shown are 988 (call or text) and 211 (dial 2-1-1, text ZIP to
  898-211), both taken from the services' own official pages on 2026-08-28. Every other
  resource says "contact page on their site" because we did not verify any other number.
- Two candidate resources were dropped because their sites could not be verified from our
  tools on 2026-08-28: Fellowship House (site blocked automated access) and Aletheia House
  (site unreachable). Their absence is a verification gap, not a judgment.

## Hardcoded and mocked

- Scenarios and resources are embedded in `index.html` as JavaScript constants, copied by
  hand from the CSVs so the page opens from a file with no server. The CSVs are the source
  of record. `tests/check-data.py` fails on any drift. Added 2026-08-28.
- The phone-confirmation step is described, not performed. No call is placed. In the family
  design the caller is the family member, and the checkbox only records their say-so for
  the length of the page visit. It records nothing and sends nothing. Added 2026-08-28.
- The copy button copies text to the clipboard and nothing else. Nothing is sent, filed,
  or referred anywhere. Added 2026-08-28.

## Not yet built

- No SEO and no AI findability. The page ships with no meta description, no Open Graph or
  structured data markup, no sitemap, and no llms.txt. A family searching the open web, or
  asking an AI assistant, will not find this tool today. Developing full SEO for search
  and AI findability is named future work, and it matters because the family in crisis
  starts at a search box. Added 2026-08-28.
- No signage or handout exists. The README names a plan to place a QR card and a handout
  at ER discharge desks, the Jefferson County Jail release area, Crisis Center Birmingham,
  One Roof, and NAMI Alabama meetings. No site has agreed, nothing has been printed, and
  nothing has been placed anywhere. Added 2026-08-28.

## What this tool must not be trusted for

- Whether any facility is open, has a bed, or will accept anyone today. Confirm by phone.
- Eligibility, clinical, or legal decisions. The card flags what to confirm and who owns
  the decision. Trained people decide.
- Medical or legal advice. The card points at real front doors and stops there. The
  scenario about a person who refuses help points to NAMI and 988 and deliberately does
  not explain involuntary commitment, which is a legal process a lawyer or the probate
  court explains.
- Anything about a real person. There are no real people in this system and no way to
  enter one.

## Unverified

- The claim that JBS Mental Health Authority runs a Jefferson County Probate Court program
  and serves Jefferson, Blount, and St. Clair counties comes from its own homepage on
  2026-08-28 and was not verified with the agency.
- Nothing else open. The team ID was unverified at first commit and got confirmed as 4B at
  kickoff on August 28, 2026.
