# Audit — காலப் பேழையும் கவிதைச் சாவியும்

## Current phase

**Phase 1 — TRANSCRIPTION ONLY.**

The user explicitly directed that the current phase should build the transcription layer first. Source-critical verification, systematic continuity/page-join review, structural/completeness audit, canonical Tamil assembly and translation are deferred to later phases.

Governing plan: repository root `TRANSCRIPTION_PHASE_PLAN.md`.

## State at the phase switch

- physical scans in controlling PDF: **306**
- scans inspected for identity/opening structure: **10**
- genuinely verified page records completed before phase switch: **9**
- verified range: **scans 1–9 consecutively**
- next Phase-1 transcription page: **scan 10**

The nine already verified records remain verified. New scan-10+ pages should normally remain `partial`, or `needs-review` for a specific unresolved reading, until Phase 2.

## Phase-1 rules

During the current phase:

1. transcribe each physical scan directly from the controlling source;
2. preserve source spelling, punctuation, headings, lineation, quotation marks and unusual forms;
3. record visible printed page numbers only;
4. exclude later stamps/handwriting/show-through from edition text;
5. record genuine uncertainty rather than guessing;
6. create the sequential page record;
7. do **not** run a separate glyph-by-glyph verification pass;
8. do **not** conduct systematic page-join/continuity or item-boundary audits;
9. do **not** conduct work-wide completeness review;
10. do **not** assemble canonical Tamil or begin translation.

Control documents are updated at milestones/anomalies/phase changes rather than after every small transcription batch.

## Source controls already established

- SHA-256 recorded: **PASS**
- file size recorded: **PASS**
- source PDF excluded from repository: **PASS**
- title/author verified from scan: **PASS**
- publication details recorded from visible preliminaries: **PASS**

## Work completed before Phase 1 was declared

### Scans 1–4

Direct visual verification was completed for:

1. scan 1 — colour front cover;
2. scan 2 — title page, excluding later library stamp/handwriting from edition text;
3. scan 3 — publication details / price / printer line;
4. scan 4 — introductory note signed `மு. க.`.

The scan-4 source form `நிலைபோட்டி` is preserved exactly as printed and has not been silently normalized.

### Scans 5–7 — contents

All three contents pages were transcribed and verified before the phase switch:

- scan 5 — items **1–19**;
- scan 6 — items **20–43**, visible printed page `5`;
- scan 7 — items **44–58**, visible printed page `6`.

Result:

- contents items accounted for: **58/58**;
- listed starting-page numbers captured: **58/58**;
- contents page records: **3/3 verified**;
- no OCR wording imported.

The preliminary scan-5 printed-page inference `4` was removed because no printed number is visibly present on that scan.

### Scan 8

Verified as an unnumbered work/display page containing the title and author line, with no poem/body text.

### Scan 9

Resolved and verified as a blank verso dominated by reverse-side/show-through, with no independently printed edition text and no visibly printed page number.

## Deferred audits

### Phase 2 — source-critical visual verification

Deferred until Phase 1 transcription is complete. This will independently check scan-10+ transcriptions for glyphs, word endings, punctuation, lineation, old-typeface failure classes and lexical-control corrections.

### Phase 3 — structure/completeness/assembly

Deferred until Phase 2 is complete. This will cover exact mapping reconciliation, item/work boundaries, all page joins, completeness, canonical Tamil assembly and final clearance.

### Phase 4 — translation/release

Blocked until Tamil final clearance.

## Assembly readiness

**DEFERRED / NOT READY.** Assembly is a Phase-3 activity and must not begin during the current transcription-only phase.

## Translation readiness

**BLOCKED.** Translation is a Phase-4 activity and Tamil final clearance has not been reached.

## Exact next activity

Transcribe **scan 10** into `pages/0010.md` from the controlling scan, using Phase-1 status rules, then continue sequentially through subsequent scans. Do not perform the deferred verification, continuity, structural audit or assembly as part of this phase.
