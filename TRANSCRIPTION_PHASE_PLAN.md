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

`poems/kaalap-pezhaiyum-kavithai-saaviyum/` is currently in **Phase 2 — source-critical visual verification**.

Current state:

- controlling PDF: **306 physical scans**;
- Phase 1 transcription: **306/306 physical scans represented**;
- numbered item/title pages observed: **58/58**;
- Phase 2 verified range: **scans 1–299 consecutively**;
- completed Phase-2 batches: **1–25**, **26–50**, **51–75**, **76–100**, **101–125**, **126–150**, **151–175**, **176–200**, **201–225**, **226–250**, **251–275**, **276–299**;
- all **58 numbered items** have now completed Phase-2 source-critical verification;
- unresolved readings through scan 299: **none**;
- next and final Phase-2 verification batch: **scans 300–306**.

### Latest completed batch — scans 276–299

Scan-proven corrections:

- scan 278: `தடந்தோள் பழுதியிடத்` → `தடந்தோள் பழுதிபடத்`;
- scan 281: `புள்ளியமில்` → `புள்ளிமயில்`;
- scan 284: `பேராசி` → `பேரரசி`; `அருமையமிகு` → `அருமைமிகு`;
- scan 287: `கையான்ட` → `கையாண்ட`;
- scan 293: `பாண்டியருக்கு` → `பாண்டியர்க்கு`; `கூண்டவிட்ட` → `கூண்டிலிட்ட`; `இன்றுமுத்துப்` → `இன்றுமுற்றுப்`;
- scan 294: `காலை மறட்டும்` → `காலை மலரட்டும்`;
- scan 296: `நீர்வாகத்` → `நிர்வாகத்`.

Source-sensitive forms independently rechecked and retained include scan 279 `சேரமான் யானைக்கட்சேய் இரும்பொறை`, scan 280 `விண்மிரட்டல்`, scan 281 `பூசின்றோ ?`, scan 282 `அணையுடைத்துப் பெருகிற்று`, scan 283 `கூதிர்காலத்தில்` / `இடக்கோளில்`, scan 286 `அகவு மேதும்`, scan 288 `தமிழ்ப் புவி`, scan 290 `சேரமான் மாரிவெண்கோவும்`, scan 292 `வண்ணனையே`, scan 297 `தீக்கு இரையாகக்கித்`, and scan 298 `சிற்றெறும்பு அரசுகளாயின்`.

The item-58 title-page witness `பகைவாள் முனை மருங்க; நாள் எல்லாம் உழைப்போம்!` remains distinct from the contents witness `பகை வாள் முனை மருங்க; நாள் எல்லாம் உழைப்போம்`. Both remain preserved for later Phase-3 reconciliation. Scan 299's printed `(முதல் பாகம் முற்றிற்று)` was independently confirmed.

Phase 2 must remain independent visual verification only. Do not begin Phase-3 structure/assembly work or Phase-4 translation until scans 300–306 have completed Phase 2 and the phase transition is explicitly recorded.
