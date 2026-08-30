# Transcription-first phase plan

This repository may process long or difficult source works in explicit phases so that transcription and verification do not become mixed into one activity.

The controlling scan remains the textual authority in every phase. Phase separation changes **when review happens**, not the source-fidelity requirement.

## Phase 1 — transcription only

Goal: create a complete page-record transcription layer as efficiently and faithfully as possible.

For each physical scan:

- read the controlling scan directly;
- transcribe visible edition text without silent normalization;
- preserve spelling, punctuation, headings, quotation marks, lineation and unusual printed forms as seen;
- record the physical scan number and any **visibly printed** page number;
- exclude later stamps, handwriting, bleed-through/show-through and unrelated marks from edition text while noting them when necessary;
- if a glyph or word is genuinely unreadable, record the uncertainty explicitly rather than guessing;
- create the corresponding `pages/NNNN.md` record.

New Phase-1 records are not promoted to `verified` merely because they were transcribed. Systematic glyph review, page-join auditing, work-wide completeness review, canonical Tamil assembly and translation belong to later phases.

## Phase 2 — source-critical visual verification

After Phase 1 transcription is complete:

- independently reread each page against the controlling scan;
- check every word ending and compact/old Tamil glyph;
- check punctuation, lineation, quotation marks, separators, English/Latin material and unusual forms;
- use enlarged crops or non-destructive image variants where needed;
- reconcile documented user lexical controls and corrections;
- correct source-backed discrepancies;
- promote a page to `verified` only after this review actually passes.

Phase 2 is where the repository's old-typeface failure classes receive systematic attention. Phase 1 transcription must not be treated as final clearance.

## Phase 3 — structure, completeness, assembly and Tamil final clearance

Only after page verification is complete, proceed through these gates in order:

1. **scan ↔ printed-page reconciliation**;
2. **item/work boundary and page-join audit**;
3. **title-witness reconciliation** where contents/title-page witnesses differ;
4. **canonical Tamil assembly** from verified page records;
5. **assembly/source-completeness review**;
6. **Tamil final clearance**.

Do not skip a gate or begin a later gate because its inputs appear obvious.

## Phase 4 — translation and release

English translation or other derivative/release work begins only after the Tamil source layer reaches the repository's required final-clearance state.

Translation/release follows the existing voice-fidelity and editorial-review rules in `POEM_PROCESSING_GUIDE.md` and the relevant work-specific documents.

## Current application — காலப் பேழையும் கவிதைச் சாவியும்

`poems/kaalap-pezhaiyum-kavithai-saaviyum/` has completed the full phase-separated workflow.

Final status:

- controlling PDF: **306 physical scans**;
- Phase 1 transcription: **306/306 — COMPLETE**;
- Phase 2 source-critical verification: **306/306 — COMPLETE**;
- unresolved Tamil readings: **0**;
- Phase 3 scan/page reconciliation: **COMPLETE**;
- Phase 3 boundary/page-join audit: **58/58 — PASS**;
- Phase 3 title-witness reconciliation: **14/14 — PASS**;
- canonical Tamil assembly: **58/58 — COMPLETE**;
- assembly/source-completeness review: **PASS**;
- Tamil final clearance: **PASS — FINAL-CLEARED**;
- Phase 4 translation batches: **21/21 reviewed PASS**;
- English items: **58/58**;
- English numbered-item scan coverage: **290/290**, scans **10–299**;
- complete English collection assembly: **COMPLETE**;
- standalone English item files: **58/58**;
- editorial/terminology/Kalaignar-voice review: **PASS**;
- final source-coverage/release review: **PASS — RELEASE-CLEARED**;
- unresolved release issues: **0**;
- Tamil `sections/` or `pages/` files changed during Phase 4: **0**.

Durable records:

- `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_CANONICAL_SOURCE_REVIEW.md`;
- `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_TAMIL_FINAL_CLEARANCE.md`;
- `poems/kaalap-pezhaiyum-kavithai-saaviyum/translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`;
- `poems/kaalap-pezhaiyum-kavithai-saaviyum/translations/en/RELEASE_REPORT.md`.

The numbered first-part range closes on scan **299**; scan **300** begins separate end matter.

**No further routine phase activity remains for this work.** A later change requires explicit user scope or a documented source-backed reopen.

For every continuation, live GitHub `main` supersedes older checkpoint SHAs or copied prompts.
