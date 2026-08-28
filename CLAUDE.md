# confirm-first-handoff

Team project for the Claude Impact Lab, Birmingham, 2026-08-28. Challenge 4: Improve the
Handoff to Homelessness Services. This repo is public. Every session that works here loads
these rules first.

## What this is

A confirm-first family navigator for co-occurring mental health and substance use needs.
The family of the person picks the bounded moment they are in and gets the calls to make
first, the one thing to confirm by phone before anyone travels, the safe next step, the
owner, the point where a trained person takes over, and the follow-up window. Two paths:
prevent entry into homelessness at a catchable moment, or navigate the four systems in
order when entry cannot be avoided. Scenarios are synthetic. Resources are real, verified
live on 2026-08-28, and never live-capacity. One Roof's Coordinated Entry is the workflow
boundary. The tool feeds people toward it, never around it. Version 1 was a responder-
facing card over the event dataset, replaced by the family pivot at midday on lab day.

## Working rules

1. Maintain `LIMITATIONS.md`. Append every faked, mocked, hardcoded, or synthetic thing the
   moment it enters the code, never at the end.
2. Keep the demo path working after every change. The demo is walking one scenario to a
   safe handoff in the browser.
3. Commit after every working step with a clear message.
4. Never add real data. No real names, no PII, no client records. The dataset is synthetic
   and every screen and output says so.
5. Never write to any live system. Read the web only. Submit no tickets or referrals.
6. When uncertain about a fact, mark it unverified in the artifact instead of guessing.
7. Never score, rank, or assign vulnerability or risk to any person.
8. Never claim live bed or shelter capacity from any source.
9. Every consequential decision in the workflow names the point where a person reviews or
   takes over.
10. Never replace or bypass Coordinated Entry.
11. Tone is dignity first. The person is the user, never the problem.
12. Prefer the simplest stack that demos in a browser. No build step a reviewer has to fight.

## Layout

- `data/` holds the synthetic scenarios (`is_synthetic` intact), the verified real
  resource list, and the event's original dataset as provenance.
- `index.html` is the app. Single file, no dependencies.
- `DEMO.md` holds the exact demo steps.
- `README.md` follows the event's team README template.
- `LIMITATIONS.md` is the living list of everything synthetic, mocked, or hardcoded.
