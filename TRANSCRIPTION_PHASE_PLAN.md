# Transcription-first phase plan

The controlling scan remains the textual authority in every phase. Phase separation changes **when review happens**, not the source-fidelity requirement.

## Phase 1 — transcription only

For each physical scan:

- read the controlling scan directly;
- transcribe visible edition text without silent normalization;
- preserve spelling, punctuation, headings, quotation marks, lineation and unusual printed forms as seen;
- record the physical scan number and any **visibly printed** page number;
- distinguish later marks/show-through from edition text;
- if a glyph or word is unreadable, record uncertainty explicitly with `⟦…⟧` rather than guessing;
- create `pages/NNNN.md`.

Phase-1 records are not `verified` merely because they exist.

## Phase 2 — source-critical visual verification

After Phase 1 is complete across the source, independently reread every page against the controlling scan, checking every word/glyph, punctuation mark, line break, quotation, separator and non-Tamil element. Promote a page to `verified` only after that independent visual review passes.

## Phase 3 — structure, completeness, assembly and Tamil final clearance

Proceed only after page verification: scan↔printed-page reconciliation; item/work boundary and page-join audit; title-witness reconciliation; canonical Tamil assembly; assembly/source-completeness review; Tamil final clearance.

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
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

The previous 150-page assumption was a renderer-window error and is withdrawn. Direct full-source access confirms 465 physical pages.

### Phase-1 state

- page records created: **300/465** — `pages/0001.md` through `pages/0300.md`;
- cumulative status: **10 `partial`, 290 `needs-review`, 0 `verified`**;
- completed batches: **01 scans 1–25; 02 scans 26–50; 03 scans 51–75; 04 scans 76–100; 05 scans 101–125; 06 scans 126–150; 07 scans 151–175; 08 scans 176–200; 09 scans 201–225; 10 scans 226–250; 11 scans 251–275; 12 scans 276–300**;
- `சிலப்பதிகார விருந்து` closes scan **285 / printed page 268**;
- `அண்ணா வழியில்` spans scans **286–292**, closes printed page **275**;
- `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்!` spans scans **293–296**, closes printed page **279**;
- current item `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை` opens scan **297 / printed page 280** and remains open after scan **300 / printed page 283**;
- Phase 2: **not started**;
- Phase 3: **not started**;
- Phase 4: **blocked**.

### Blur and witness rules

- use explicit `⟦…⟧` markers for unresolved Phase-1 spans;
- do not reconstruct from OCR, memory, metre, grammar, historical expectation or another edition;
- do not copy existing separate source witnesses into this anthology;
- preserve source-visible speaker/performance structure where legible;
- record only visibly printed page numerals;
- preserve the existing user-directed exclusion applicable to `தென்னவன் காதை`.

### Exact next activity

Execute **Phase 1 Batch 13 — physical scans 301–325**.

Create `pages/0301.md` through `pages/0325.md`, continuing directly from the unfinished `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை` at scan 300. Do not begin Phase 2, Phase 3, canonical assembly, or translation in the same activity.

## Completed prior application — காலப் பேழையும் கவிதைச் சாவியும்

This work completed the full phase-separated workflow and is **Tamil FINAL-CLEARED / English RELEASE-CLEARED**.

For every continuation, live GitHub `main` supersedes older checkpoint SHAs or copied prompts.