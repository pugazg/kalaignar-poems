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

## Current application — கலைஞரின் கவிதைகள்

Active work: `poems/kalaignarin-kavithaigal/`.

Controlling source currently supplied:

`TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

### Source intake state

- available physical scans: **150**;
- file size: **486,369,088 bytes**;
- SHA-256: **pending exact-byte computation; never guess**;
- source title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher visible: **பாரதி பதிப்பகம்**;
- edition visible in English imprint: **fourth edition, March 1995**;
- Phase 1 page records: **0/150**;
- Phase 2: **not started**;
- Phase 3: **not started**;
- Phase 4: **blocked**.

### Critical partial-source boundary

The supplied PDF is not the complete printed edition.

Source-supported evidence:

- physical scans **15–17** are contents pages;
- those contents list entries beginning through at least printed page **444**;
- physical scan **150** visibly carries printed page **133** and ends with continuing body text.

Accordingly, the phase framework applies in two distinct senses:

1. the **available 150-scan source tranche** can complete Phase 1 and later source-critical verification for the pages actually supplied;
2. the **printed book as a whole** cannot reach source-completeness review, Tamil final clearance or release until continuation source is supplied and reconciled.

No status document may collapse `150/150 available scans` into a whole-book completion claim.

### Cross-witness rule

This anthology contains works also represented by other controlling sources in the repository, including at least `இதயத்தைத் தந்திடு அண்ணா!` and `தென்னவன் காதை`.

Those existing texts are not transcription authority for this edition. Every page of the 1995 anthology must be read independently from its own controlling scan. Differences in spelling, punctuation, lineation, wording or paratext must be preserved rather than harmonized.

### Exact next activity

Execute **Phase 1 batch 01 — physical scans 1–25**.

Create `pages/0001.md` through `pages/0025.md` from direct visual inspection. This batch includes cover/title/imprint/introduction, all contents scans, the divider/verso, and the opening pages of `இதயத்தைத் தந்திடு அண்ணா!`.

First-pass page records should normally be `partial`. Record only visibly printed page numbers. Do not begin Phase 2, Phase 3 or translation during this activity.

At batch completion update `audit.md` and `indexes/page-map.md` with the durable boundary and exact next Phase-1 batch.

## Completed prior application — காலப் பேழையும் கவிதைச் சாவியும்

`poems/kaalap-pezhaiyum-kavithai-saaviyum/` completed the full phase-separated workflow and is **Tamil FINAL-CLEARED / English RELEASE-CLEARED**. Do not reopen its completed gates merely because another source has become active.

For every continuation, live GitHub `main` supersedes older checkpoint SHAs or copied prompts.
