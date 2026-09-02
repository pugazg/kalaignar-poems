# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems` — branch `main`.

**Live `main` is authoritative. Fetch it first in every fresh chat and preserve any newer durable state.**

## Active work — கலைஞரின் கவிதைகள்

Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

- physical PDF pages: **465**;
- bytes: **486,369,088**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`;
- title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

The old renderer `total_pages: 150` is only a tooling window and must never override the exact 465-page source identity.

## Durable state after Phase 3 Gate 2

- Phase 1: **465/465 COMPLETE**;
- Phase 2 source coverage and clearance: **465/465 COMPLETE — C01–C19**;
- page status: **0 partial / 0 needs-review / 465 verified**;
- durable contiguous verified boundary: **1–465**;
- Phase 3 Gate 1 — physical scan ↔ printed-page reconciliation: **COMPLETE**;
- Phase 3 Gate 2 — boundary / page-join audit: **COMPLETE**;
- Phase 3 Gate 3 — title-witness reconciliation: **NOT STARTED — NEXT**;
- canonical Tamil assembly: **NOT STARTED**;
- Tamil final clearance: **NOT STARTED**;
- translation: **NOT STARTED**.

## Gate 1 durable result

`poems/kalaignarin-kavithaigal/PHASE3_STRUCTURE_AUDIT.md` records the complete pagination model:

- scan 1 front cover, unpaginated;
- scans 2–17 logical Roman I–XVI;
- scans 18–464 logical Arabic 1–447, `logical printed page = scan_page - 17`;
- scan 465 back cover, unpaginated.

`printed_page` in page records remains a source-visible witness only; suppressed numerals are not backfilled.

## Gate 2 durable result

`poems/kalaignarin-kavithaigal/PHASE3_BOUNDARY_JOIN_AUDIT.md` certifies **464/464 physical adjacent joins** without changing verified page text.

Key locked source-order facts include:

- 236→237→238→239 is intentionally interposed: `அண்ணன் ஒரு கவியரங்கம்` participant list, then `தமிழ் வளர வழிநடைப் பயணம்` title leaf, then return to close the prior item, then resume the new item. **Do not reorder.**
- 370→371→372→373→374 is a real close / blank verso / `கண்ணீர்த் துளிகள்` divider / divider verso / `பன்னீர்ச்செல்வமே!` opening sequence. Show-through is not edition text.
- 397 closes `அவன் பிறந்தநாள் என ஒன்றில்லை!`; 398–399 is `அருமருந்தே! அன்பழக உடன்பிறப்பே!`; 400 opens `பகுத்தறிவுப் பாண்டியனார்!`.
- 425 opens `ஒரு சொட்டுத் தேன்!` and continues to 426.
- 450–452 is `பகலவனாய்க் கிழக்கில் உதித்திடுவோம்!`; 453 opens `திசை திருப்பல் நியாயம்தானா?`.
- 464 closes `உன் காலணியை வாழ்த்துகிறாய்`; 465 is the back cover.

Batch boundaries from transcription/clearance are never item boundaries by themselves.

## Supplied-transcription rule

Do not position supplied Markdown by page numbers written inside it. Match first and last substantive body anchors to the exact source. Supplied text controls lexical words only inside the confirmed interval; the scan controls physical placement, headings, punctuation, quotation structure, lineation, ornaments and non-body separation. Running headers, printed page numerals and extraction/OCR garbage are not body text.

## Mandatory startup

Before changing anything, read completely:

1. `POEM_PROCESSING_GUIDE.md`;
2. `TRANSCRIPTION_PHASE_PLAN.md`;
3. root `README.md`;
4. this `HANDOVER.md`;
5. `NEXT_CHAT_PROMPT.md`;
6. active-work `README.md`;
7. `SOURCE_INTAKE.md`;
8. `metadata/source.md`;
9. `indexes/page-map.md`;
10. `audit.md`;
11. `PHASE3_STRUCTURE_AUDIT.md`;
12. `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

## EXACT NEXT ACTIVITY

Execute **Phase 3 Gate 3 — title-witness reconciliation only**.

Compare contents-page titles, section-divider/title-page witnesses, and other source title witnesses. Preserve every source form exactly. Where witnesses differ, record the variants and an explicit authority decision for later canonical assembly. **Never normalize or create a hybrid title.**

Do **not** begin canonical Tamil assembly, Tamil final clearance, translation, or release work in the same activity.
