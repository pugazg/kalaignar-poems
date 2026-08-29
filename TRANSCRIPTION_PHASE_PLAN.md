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

`poems/kaalap-pezhaiyum-kavithai-saaviyum/` is now in **Phase 3 — structure, completeness, assembly and Tamil final clearance**.

Current state:

- controlling PDF: **306 physical scans**;
- Phase 1 transcription: **306/306 physical scans represented — COMPLETE**;
- numbered item/title pages observed: **58/58**;
- Phase 2 source-critical verification: **306/306 scans verified — COMPLETE**;
- unresolved readings after Phase 2: **none**;
- Phase-3 physical scan ↔ printed-page reconciliation: **COMPLETE**;
- numbered pagination block: scans **5–299** ↔ printed pages **4–298**, continuously, with no unexplained gap or duplicate;
- all **306 scans** structurally accounted for;
- all **58** contents start pages align with title scans by `title scan = contents start page + 1`;
- Phase-3 structural audit file: `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_STRUCTURE_AUDIT.md`;
- exact next activity: **58-item boundary and within-item page-join continuity audit**;
- canonical Tamil assembly remains blocked until that structural audit passes;
- Phase 4 translation remains blocked until Tamil final clearance.

### Completed Phase-3 activity 1

The exact scan/printed-page map is now recorded in `indexes/page-map.md`. Phase 3 explicitly distinguishes a **visibly printed numeral** from a **reconciled logical printed page**; suppressed page numerals are not retroactively claimed as visible source marks.

The next Phase-3 pass must certify every item boundary and every adjacent within-item page join, including quotation carry-over, continuation punctuation, separators and dropped/duplicated lines. Only after that pass succeeds may canonical Tamil assembly begin.