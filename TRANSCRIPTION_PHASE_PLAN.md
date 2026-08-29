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

`poems/kaalap-pezhaiyum-kavithai-saaviyum/` is in **Phase 3 — canonical Tamil assembly**.

Current live work state:

- controlling PDF: **306 physical scans**;
- Phase 1 transcription: **306/306 physical scans represented — COMPLETE**;
- numbered item/title pages observed: **58/58**;
- Phase 2 source-critical verification: **306/306 scans verified — COMPLETE**;
- unresolved readings after Phase 2: **none**;
- Phase-3 scan ↔ printed-page reconciliation: **COMPLETE**;
- numbered pagination block: scans **5–299** ↔ printed pages **4–298**, continuously, with no unexplained gap or duplicate;
- all **306 scans** structurally accounted for;
- all **58** contents start pages align with title scans by `title scan = contents start page + 1`;
- Phase-3 boundary / within-item page-join audit: **COMPLETE — 58/58 items certified**;
- closing boundary **299→300: PASS**, separating `(முதல் பாகம் முற்றிற்று)` from the `குறிப்புகள்` end matter;
- Phase-3 title-witness reconciliation: **COMPLETE — 14/14 discrepancy cases reconciled**;
- canonical Tamil assembly: **IN PROGRESS — 11/58 item files assembled**;
- completed canonical files: `sections/01.md` through `sections/11.md`;
- latest assembly iteration: **physical scans 35–59 — COMPLETE**;
- next assembly iteration: **physical scans 60–84**, completing carried item 12 from scans **58–63**;
- assembly/source-completeness review: **BLOCKED until 58/58 canonical item files exist**;
- Tamil final clearance: **PENDING assembly/source-completeness review**;
- Phase 4 translation: **BLOCKED until Tamil final clearance**.

### Completed Phase-3 gate 1 — exact scan / printed-page mapping

The exact scan/printed-page map is recorded in `indexes/page-map.md`. Phase 3 explicitly distinguishes a **visibly printed numeral** from a **reconciled logical printed page**; suppressed page numerals are not retroactively claimed as visible source marks.

### Completed Phase-3 gate 2 — item boundaries and page joins

All **58/58** numbered items have passed opening-boundary, within-item join and closing-boundary review. No unresolved structural join remains and no dropped/duplicated source passage was detected. Detailed evidence is recorded in `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

The numbered sequence closes on scan **299 / printed page 298** with `(முதல் பாகம் முற்றிற்று)`. Scan 300 begins the separate `குறிப்புகள்` end matter.

### Completed Phase-3 gate 3 — title-witness reconciliation

The verified contents witness and item-opening title-page witness differ for items **18, 22, 25, 26, 29, 31, 32, 37, 40, 44, 46, 50, 54 and 58**.

The reconciliation rule is:

- preserve both witnesses exactly;
- use the **title-page witness** as the displayed title in canonical item assembly;
- retain the **contents witness** as the contents/index witness and alternate source metadata;
- create no hybrid or silently normalized title;
- keep item identity/order based on the certified contents sequence **1–58**;
- item 37 remains item **37** although its title page visibly prints item number **36**; that number is preserved only as a source anomaly.

The governing decision record is `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_TITLE_WITNESS_RECONCILIATION.md`.

### Active Phase-3 gate 4 — canonical Tamil assembly

Canonical assembly uses the verified `pages/NNNN.md` records as its text layer.

Rules:

- create stable numeric files `sections/01.md` … `sections/58.md`;
- preserve verified lineation, spelling, punctuation, quotations, separators, source notes and unusual printed forms;
- preserve physical-page provenance with `<!-- scan_page: N -->` markers;
- use the title-page witness for the displayed title where contents/title witnesses differ;
- retain the contents witness separately in front matter;
- retain item 37's printed number `36` as a source anomaly without renumbering the stable sequence;
- do not normalize source-level abrupt transitions already certified in the boundary/join audit;
- if an assembly batch ends inside an item, do **not** create an incomplete canonical file; carry that item into the following iteration;
- if assembly exposes a real source/page-record discrepancy, reopen and correct the verified source layer with audit history before continuing assembly.

### Completed canonical-assembly iteration 1 — scans 10–34

Created and recorded:

- `sections/01.md` — scans 10–11;
- `sections/02.md` — scans 12–15;
- `sections/03.md` — scans 16–19;
- `sections/04.md` — scans 20–24;
- `sections/05.md` — scans 25–28;
- `sections/06.md` — scans 29–34.

No verified page record was modified and no partial canonical file was created.

### Completed canonical-assembly iteration 2 — scans 35–59

Created and recorded:

- `sections/07.md` — scans 35–39;
- `sections/08.md` — scans 40–43;
- `sections/09.md` — scans 44–49;
- `sections/10.md` — scans 50–53;
- `sections/11.md` — scans 54–57.

Item 12 spans scans **58–63**. Scans **58–59** were carried forward, and no partial `sections/12.md` was created. No verified page record was modified.

## Exact next activity

Process the next **25 physical scans: 60–84** as canonical assembly iteration 3, completing carried item 12 from its full certified range **58–63**.

The complete item files available at that boundary are:

- item 12 — scans **58–63** → create `sections/12.md`;
- item 13 — scans **64–67** → create `sections/13.md`;
- item 14 — scans **68–77** → create `sections/14.md`;
- item 15 — scans **78–81** → create `sections/15.md`.

Item 16 begins at scan **82** but runs through scan **87**. Because this iteration stops at scan 84, **do not create `sections/16.md` yet**. Carry item 16 forward until the following iteration includes its complete certified range.

After this iteration, update `PHASE3_CANONICAL_ASSEMBLY.md` and the work `README.md` with the durable progress boundary. Do **not** begin assembly/source-completeness review until all **58/58** canonical files exist. Do **not** begin Phase 4 translation before Tamil final clearance.

For every continuation, live GitHub `main` supersedes any older checkpoint SHA or copied prompt.
