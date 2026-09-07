# HANDOVER — பூமுடி

Repository: `pugazg/kalaignar-poems`, branch `main`. **Live main is authoritative.**

Active workspace: `poems/poomudi/`.

## Controlling source

`TVA_PRL_0001656_முரசொலி_அண்ணா மலர்_1965.pdf`

- physical PDF pages: **65**;
- file size: **247,645,717 bytes**;
- SHA-256: **`7312d5f8686f7968d62bbac9318c2452ca32873a0ae889f10a7151e5de81ab5a`**;
- user-scoped poem range: physical scan **4 only**;
- source PDF must not be committed.

## Work identity

- title: **பூமுடி** — direct source title;
- source-visible signature: **மு.கருணாநிதி**;
- user-supplied publication/year: **முரசொலி-அண்ணா மலர் / 1965**;
- user context: `முரசொலி அண்ணா மலருக்காக அண்ணனுக்கு வாழ்த்துச் சொல்லி தம்பி கலைஞர் எழுதிய கவிதை`.

## Current durable state

**PHASE 1 COMPLETE — 1/1 / PHASE 2 COMPLETE — 1/1 VERIFIED / PASS AFTER SOURCE-BACKED REVERIFICATION / PHASE 3 NOT STARTED.**

- verified page: `pages/0004.md`;
- Phase-2 authority: `PHASE2_SOURCE_VERIFICATION.md`;
- post-verification correction authority: `PHASE2_REVERIFICATION_2026-09-07.md`;
- visible printed page numeral: **none**; `printed_page: null`;
- source-backed corrected readings after user recheck: **4**;
- compact/historical glyph pass: **PASS**;
- unresolved Tamil readings: **0**;
- Phase 3: **NOT STARTED**;
- Phase 4: **NOT STARTED**;
- canonical Tamil: **none**;
- English derivative: **none**.

Neighbouring scans 3 and 5 remain boundary evidence only.

## Source-backed correction / no-regression control

The user flagged exactly four readings as wrong and stated that the rest of the transcription was correct. Direct enlarged-scan reinspection confirmed these corrections:

- `கமழ்கின்ற` → `கமழுகின்ற`;
- `தலையது` → `தலையிது`;
- `பொன்னைவைத்தால்` → `பொன்னை வைத்தால்`;
- `உனக்காக` → `உனைக் காக்க`.

The affected verified lines are now:

- `அறிவுமணங் கமழுகின்ற அண்ணன் தலையிது`;
- `பொன்னை வைத்தால் நோகுமென்று`;
- `உனைக் காக்க எனைத் துறப்பேன்.`

All other poem wording, punctuation and lineation remain unchanged.

## Parallel textual reuse

The shared core passage appears later in:

- `poems/anna-kaviyarangam/sections/anna-kaviyarangam.md` (1968);
- `poems/idhayathai-thanthidu-anna/sections/idhayathai-thanthidu-anna.md` (1969).

The 1965 page is not to be normalized to either later reuse. The corrected 1965 close agrees with the 1968 `உனைக் காக்க எனைத் துறப்பேன்.`; the 1969 witness has `உனக்காக எனைத் துறப்பேன்; என் -`.

## Exact next activity

Perform **Phase 3 Gate 1 — physical scan ↔ printed-page reconciliation only**.

- fetch live `main` first;
- reread the controlling scan and page-map state;
- formally certify the one-page physical scope;
- confirm whether any source-visible printed page numeral exists;
- retain `printed_page: null` only if the scan supports it;
- create/update the Gate-1 structural authority and synchronized status docs;
- do **not** begin Gate 2, canonical assembly, or translation in the same activity.

All release-cleared work remains closed unless formally reopened by source-backed evidence.