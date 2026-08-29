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
- Phase 2 verified range: **scans 1–275 consecutively**;
- completed Phase-2 batches: **1–25**, **26–50**, **51–75**, **76–100**, **101–125**, **126–150**, **151–175**, **176–200**, **201–225**, **226–250**, **251–275**;
- unresolved readings through scan 275: **none**;
- next Phase-2 verification batch: **scans 276–299**;
- final Phase-2 remainder after the numbered work sequence: **scans 300–306**.

### Latest completed batch — scans 251–275

Scan-proven corrections:

- scan 254: `மரபு வழிக் கலப்புப் மணவிழாவை` → `மரபு வழிக் கலப்பு மணவிழாவை`;
- scan 255: `கி.பி. 1070 சூன் திங்கள்` → `கி.பி. 1070 ஜூன் திங்கள்`;
- scan 266: compact continuation `பெயன்று` → `யென்று`;
- scan 269: `முடிவரை` → `முடிவுரை`; `மூற்கத்தனமிக்க` → `மூர்க்கத்தனமிக்க`.

Source-sensitive forms independently rechecked and retained include scan 251 `கோல்காபூர்` / `சமணத் துறவி யொருவர்`, scan 253 `கடற்கரம் நீட்டியெழுந்த` / `ஒளவைக் கிழவி`, scan 255 `விருதராச பயங்கரன்` / `பார்த்தகன்` / `அய்ம்பது`, scan 256 `‘ஆலந்து’`, scan 259 `குறிப்பிடுழுதி`, scan 261 `ஒடிந்த கரத்துக்கு உபரிக் கரமாக`, scan 262 `விழைந்த நாண்`, scan 263 `அதுகிழ்` / `அகோரப் பசிக்கு`, scan 264 `கோரசனி` / `கெல்லி`, scan 265 `வெளியிடப்போது`, scan 267 its dense proper-name/work-title sequence, scan 268 `பைசாசம்` / `கெடுதலை`, scan 269 `எழுநூற்றுக் காவத தூரம் இவற்றின் நீர்மலிவான்`, scan 272 `அருமை அண்ணன் அண்ணால் தங்கோ` / `குக்கல்களாய்க்`, scan 273 `மண்டீது`, scan 274 `கழனியோர்த்துக்`, and scan 275 its quoted battle description.

The item-54 title-page witness `தலையாலங்கானத்துச் செருவென்றான்!` remains distinct from the contents witness `தலையாலங்கானத்துச் செரு வென்றான்!`. Both are preserved for later Phase-3 reconciliation.

Phase 2 must remain independent visual verification only. Do not begin Phase-3 structure/assembly work or Phase-4 translation until scans 276–306 have also completed Phase 2 and the phase transition is explicitly recorded.
