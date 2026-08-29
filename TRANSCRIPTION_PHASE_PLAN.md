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

`poems/kaalap-pezhaiyum-kavithai-saaviyum/` is in **Phase 3 — structure, completeness, assembly and Tamil final clearance**.

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
- Phase-3 boundary / within-item page-join audit: **COMPLETE — 58/58 items certified**;
- closing boundary **299→300: PASS**, separating `(முதல் பாகம் முற்றிற்று)` from the `குறிப்புகள்` end matter;
- Phase-3 title-witness reconciliation: **COMPLETE — 14/14 discrepancy cases reconciled**;
- governing reconciliation record: `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_TITLE_WITNESS_RECONCILIATION.md`;
- canonical Tamil assembly: **UNBLOCKED — exact next activity**;
- Phase 4 translation remains blocked until assembly review and Tamil final clearance.

### Completed Phase-3 activity 1 — exact scan / printed-page mapping

The exact scan/printed-page map is recorded in `indexes/page-map.md`. Phase 3 explicitly distinguishes a **visibly printed numeral** from a **reconciled logical printed page**; suppressed page numerals are not retroactively claimed as visible source marks.

### Completed Phase-3 activity 2 — item boundaries and page joins

All **58/58** numbered items have passed opening-boundary, within-item join and closing-boundary review. No unresolved structural join remains and no dropped/duplicated source passage was detected. Detailed evidence is recorded in `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

### Completed Phase-3 activity 3 — title-witness reconciliation

The verified contents witness and item-opening title-page witness differ for items **18, 22, 25, 26, 29, 31, 32, 37, 40, 44, 46, 50, 54 and 58**.

The reconciliation rule is:

- preserve both witnesses exactly;
- use the **title-page witness** as the displayed title and title-derived filename basis in canonical item assembly;
- retain the **contents witness** as the contents/index witness and alternate source metadata;
- create no hybrid or silently normalized title;
- keep item identity/order based on the certified contents sequence **1–58**;
- item 37 remains item **37** although its title page visibly prints item number **36**; that number is preserved only as a source anomaly.

### Exact next Phase-3 activity — canonical Tamil assembly

Assemble **58 separate canonical Tamil item files** from the verified `pages/NNNN.md` records in certified page order.

Assembly must:

- preserve verified lineation, spelling, punctuation, quotations, separators, source notes and unusual printed forms;
- use the title-page witness for the assembled title where contents/title witnesses differ;
- retain the contents witness as alternate source metadata for those discrepant items;
- retain item 37's printed number `36` as a source anomaly without renumbering the sequence;
- avoid any silent source normalization.

After assembly, perform an assembly/source-completeness review. Tamil final clearance may be granted only after that review passes. Phase 4 translation remains blocked until then.