# Transcription-first phase plan

The controlling scan remains the textual authority in every phase. Phase separation changes **when review happens**, not the source-fidelity requirement.

## Phase 1 — transcription only

For each physical scan:

- read the controlling scan directly;
- transcribe visible edition text without silent normalization;
- preserve spelling, punctuation, headings, quotation marks, lineation and unusual printed forms as seen;
- record the physical scan number and any **visibly printed** page number;
- distinguish later marks/show-through from edition text;
- if a glyph or word is unreadable, record uncertainty explicitly rather than guessing;
- create `pages/NNNN.md`.

Phase-1 records are not `verified` merely because they exist.

## Phase 2 — source-critical visual verification

After Phase 1 is complete across the source:

- independently reread each page against the scan;
- check every word/glyph, punctuation, lineation, quotation, separator and non-Tamil material;
- use enlarged source inspection when needed;
- correct only source-backed discrepancies;
- promote a page to `verified` only after the independent visual review passes.

## Phase 3 — structure, completeness, assembly and Tamil final clearance

Proceed only after page verification:

1. scan ↔ printed-page reconciliation;
2. item/work boundary and page-join audit;
3. title-witness reconciliation;
4. canonical Tamil assembly;
5. assembly/source-completeness review;
6. Tamil final clearance.

## Phase 4 — translation and release

Derivative/English work begins only after Tamil final clearance and follows the repository's voice-fidelity/release rules.

## Current application — கலைஞரின் கவிதைகள்

Active work: `poems/kalaignarin-kavithaigal/`

Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

### Exact source identity

- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: **`19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`**;
- source title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher visible: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

The previous 150-page assumption was a renderer-window error and is withdrawn. Direct full-source access confirms 465 physical pages.

### Phase-1 state

- page records created: **150/465** — `pages/0001.md` through `pages/0150.md`;
- cumulative status: **10 `partial`, 140 `needs-review`, 0 `verified`**;
- completed batches: **01 scans 1–25; 02 scans 26–50; 03 scans 51–75; 04 scans 76–100; 05 scans 101–125; 06 scans 126–150**;
- current item: `நீர்க் குடும்பம்`, opened scan 144 and continuing beyond scan 150;
- scan 151 has been source-access checked and visibly prints page 134;
- Phase 2: **not started**;
- Phase 3: **not started**;
- Phase 4: **blocked**.

### Blur rule

- use explicit `⟦…⟧` markers for unresolved Phase-1 spans;
- do not reconstruct from OCR, memory, metre, grammar, historical expectation or another edition;
- do not copy existing separate source witnesses into this anthology;
- preserve source-visible speaker/performance structure where legible;
- record only visibly printed page numerals.

### Exact next activity

Execute **Phase 1 Batch 07 — physical scans 151–175**.

Create `pages/0151.md` through `pages/0175.md`, continuing directly from `நீர்க் குடும்பம்`.

Do not begin Phase 2 in the same activity.

## Completed prior application — காலப் பேழையும் கவிதைச் சாவியும்

This work completed the full phase-separated workflow and is **Tamil FINAL-CLEARED / English RELEASE-CLEARED**.

For every continuation, live GitHub `main` supersedes older checkpoint SHAs or copied prompts.