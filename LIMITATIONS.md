# Limitations

The living list. Every faked, mocked, hardcoded, or synthetic thing gets a line here the
moment it enters the repo. Do not trust this tool for anything a line below rules out.

## Synthetic

- The entire dataset is synthetic. All 6 scenarios in
  `data/homelessness-handoff-scenarios.csv` are fictional, marked `is_synthetic=true` in
  the file. No scenario describes a real person or a real case. Added 2026-08-28 when the
  dataset entered `data/`.
- Every resource the scenarios name is fictional. "Fictional Coordinated Entry access
  point," "Fictional youth-specific transitional housing program," and the rest are labels
  from the synthetic dataset, not real Birmingham programs. The card never resolves them to
  a real address or phone number. Added 2026-08-28.

## Not live

- Capacity is never live. The tool holds no connection to any shelter, cooling center, or
  bed inventory. `capacity_is_not_live` is `true` on every row, and every screen that
  touches capacity repeats the label. The one thing to confirm by phone exists exactly
  because this tool cannot confirm it. Added 2026-08-28.

## Hardcoded and mocked

- The 6 scenarios are embedded in `index.html` as a JavaScript constant, copied by hand
  from the CSV so the page opens from a file with no server and no fetch call. The CSV in
  `data/` is the source of record. If the two ever drift, the CSV wins. Added 2026-08-28.
- The phone-confirmation step is described, not performed. No call is placed, no number is
  dialed, no availability is checked. A person makes the call. Added 2026-08-28.
- The handoff summary's copy button copies text to the clipboard and nothing else. Nothing
  is sent, filed, or referred anywhere. Added 2026-08-28.

## What this tool must not be trusted for

- Whether any facility is open, has a bed, or accepts anyone today. Confirm by phone.
- Eligibility decisions. The card flags what to confirm. A trained person decides.
- Anything about a real person. There are no real people in this system.

## Unverified

- Team ID is unverified. The event lists teams 4A, 4B, and 4C for this challenge without
  member names. The README marks the ID as to-be-confirmed at kickoff.
