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

Only after page verification is complete:

- finish exact physical scan ↔ printed-page mapping;
- audit work/item boundaries and all page joins;
- reconcile quotation carry-over, separators and continuation lines;
- account for every physical page or explicitly document unavailable pages;
- synchronize `README.md`, `indexes/page-map.md` and `audit.md`;
- assemble the canonical Tamil text from verified page records;
- perform assembly/source-completeness review;
- mark the Tamil source layer final-cleared only when all required checks pass.

## Phase 4 — translation and release

English translation or other derivative/release work begins only after the Tamil source layer reaches the repository's required final-clearance state.

Translation/release follows the existing voice-fidelity and editorial-review rules in `POEM_PROCESSING_GUIDE.md` and the relevant work-specific documents.

## Current application — காலப் பேழையும் கவிதைச் சாவியும்

`poems/kaalap-pezhaiyum-kavithai-saaviyum/` has completed **Phase 2 — source-critical visual verification** and is ready for **Phase 3 — structure, completeness, assembly and Tamil final clearance**.

Current state:

- controlling PDF: **306 physical scans**;
- Phase 1 transcription: **306/306 physical scans represented**;
- numbered item/title pages observed: **58/58**;
- Phase 2 verified range: **scans 1–306 consecutively (306/306)**;
- completed Phase-2 batches: **1–25**, **26–50**, **51–75**, **76–100**, **101–125**, **126–150**, **151–175**, **176–200**, **201–225**, **226–250**, **251–275**, **276–299**, **300–306**;
- unresolved readings after Phase 2: **none**;
- scans 300–305 independently confirm six blank `குறிப்புகள்` notes pages carrying only that heading and horizontal rule;
- scan 306 independently confirms an image-only back cover with no independently printed textual content;
- Phase 2: **COMPLETE**;
- next activity: **begin Phase 3 with exact physical scan ↔ printed-page mapping and structure/completeness reconciliation before canonical Tamil assembly**;
- Phase 4 translation remains blocked until Tamil final clearance.

### Final Phase-2 batch — scans 300–306

All seven end-matter scans passed independent source-critical visual verification with **no textual corrections and no unresolved readings**. Page records `0300.md` through `0306.md` are now `verified`.

Phase 3 may now begin, but its structural reconciliation, page-join certification and canonical Tamil assembly must remain distinct from the completed Phase-2 textual verification record. Phase 4 must not begin until Phase 3 reaches Tamil final clearance.
