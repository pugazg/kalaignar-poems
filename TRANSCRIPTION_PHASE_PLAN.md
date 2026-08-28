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

During Phase 1:

- new transcription records are **not** promoted to `verified` merely because they were transcribed;
- use `partial` for a substantially transcribed page that still awaits the independent verification phase, or `needs-review` where a specific unresolved reading requires attention;
- pages that were already genuinely verified before this phase remain `verified`; do not downgrade them only to make status labels uniform;
- do not perform a separate glyph-by-glyph verification pass;
- do not perform systematic page-join or continuity auditing;
- do not perform work-wide structural/completeness audit;
- do not assemble the canonical Tamil work;
- do not begin English translation;
- do not repeatedly update `README.md`, `audit.md`, or `page-map.md` after every small transcription batch unless a milestone, source anomaly, or phase-status change needs to be recorded.

Minimal structural observation needed to transcribe a page — for example a visible heading, a printed page number, a blank page, a photograph/caption, or an obvious new-item heading — may be recorded. That is not a substitute for the later structural audit.

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
- Phase 2 verified range: **scans 1–75 consecutively**;
- completed Phase-2 batches: **1–25**, **26–50**, and **51–75**;
- scan-proven corrections in batch 1: scan 3 `ஈகில் பிரஸ்`, scan 14 `உளியொன்றை`, scan 17 `மாளிகை யொன்றை`, scan 22 `வாய்ப்பை யெனக்`;
- scan-proven corrections in batch 2: scan 28 `பேர்`, scan 35 `மனிதக் கனம்`, scan 36 `கால்நடைப்`, scan 41 `இத்தினையையும்`;
- scan-proven corrections in batch 3 include scan 52 `மனத்துணிவுடைய`, scan 56 `அக்குழந்தை`, scan 61 `கருவிகளை` and the source vocatives `பூவைகாள்` / `புறவங்காள்` / `மயில்காள்` / `மணிக்கிளிகாள்` / `குயில்காள்`, scan 62 `போன்றுவீழ்வது` / `என் மகளாயின்`, scan 67 `ஆயிரம் பேர்`, scan 69 `தீராதி தீர தீன தயாபர`, scan 71 `மாண்டுவிடவில்லை`, scan 72 `மண்டூகே`, scan 73 `அண்ணலே`, and scan 74 `அழும்பில்` / `தோரணங்கற்பட்டு` / `கோட்டைகளிலுள்ள`;
- source-supported compact forms retained after independent review include scan 29 `ஏழைபாழையிடம்`, scan 31 `எனந்தப்`, scan 35 `மரத்தின் அழுத்தமான வேர்` / `மண்டூகே மனிதன்`, scan 47 `சளித்தோமா`, scan 52 `மாக்கலத்தில்`, scan 59 `பெருளான்` / `அவர் ஆராய்`, scan 65 `தொலைவடவர்` / `நேடியாட்சியாகவோ` / `ஒருசன்`, scan 66 `புனரதீர்` / `கைப்பா`, scan 71 `அறிந்திலராகிச்` / `துவேன்`, and scan 74 `பொழிவும்` / `சிலதுகள்`;
- next Phase-2 verification batch: **scans 76–100**.

Phase 2 must remain independent visual verification only. Do not begin Phase-3 structure/assembly work or Phase-4 translation until the required later phase transition.
