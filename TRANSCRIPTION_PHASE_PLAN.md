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
- Phase 2 verified range: **scans 1–175 consecutively**;
- completed Phase-2 batches: **1–25**, **26–50**, **51–75**, **76–100**, **101–125**, **126–150**, and **151–175**;
- scan-proven corrections in batch 1: scan 3 `ஈகில் பிரஸ்`, scan 14 `உளியொன்றை`, scan 17 `மாளிகை யொன்றை`, scan 22 `வாய்ப்பை யெனக்`;
- scan-proven corrections in batch 2: scan 28 `பேர்`, scan 35 `மனிதக் கனம்`, scan 36 `கால்நடைப்`, scan 41 `இத்தினையையும்`;
- scan-proven corrections in batch 3 include scan 52 `மனத்துணிவுடைய`, scan 56 `அக்குழந்தை`, scan 61 `கருவிகளை` and the source vocatives `பூவைகாள்` / `புறவங்காள்` / `மயில்காள்` / `மணிக்கிளிகாள்` / `குயில்காள்`, scan 62 `போன்றுவீழ்வது` / `என் மகளாயின்`, scan 67 `ஆயிரம் பேர்`, scan 69 `தீராதி தீர தீன தயாபர`, scan 71 `மாண்டுவிடவில்லை`, scan 72 `மண்டூகே`, scan 73 `அண்ணலே`, and scan 74 `அழும்பில்` / `தோரணங்கற்பட்டு` / `கோட்டைகளிலுள்ள`;
- scan-proven corrections in batch 4 include scan 77 `மணிக் குலத்தைக்`, scan 78 `தூற்றிச் சிலர்`, scan 79 `குரலுக்கோர்` / `மிடுக்குடன்` / `வைர வைடூர்ய`, scan 80 `எலும்பெடுத்து`, scan 82 `தகுதியெல்லாம்`, scan 83 `என்றல்ல` / `வெளிவந்த` / `பூரிப்போடு` / `அங்ஙனமாயின்`, scan 84 `அறந்தங்கும்`, scan 95 `சுற்றி மாற்றிக்`, scan 97 `சமர்` / `எவர்தான்`, and scan 98 `இராமச்சந்திர தீட்சிதர்`;
- scan-proven corrections in batch 5 include scan 109 `அனல் வீழ்` with source-visible five-dot ellipsis, scan 113/114 numeric `எண்பது`, scan 121 `பொன்னை அனைத்தையும்`, and scan 122 `கொண்டாந்து` / `கச்சிதமாக`;
- scan-proven corrections in batch 6 include scan 126 `வாணியது` / `தூமப்பணிகளாக`, scan 128 `எலும்புகளைப்`, scan 130 `அன்னையொருத்தி` / `பாட்டுமார்`, and scan 147 `எடுத்தனன்` / `முரசமொன்று` / `தணித்துக் கொள்வோம்`;
- scan-proven corrections in batch 7 include scan 161 `முற்பட்ட சோழர்களின்`, scan 162 `அமுதூட்டி`, scan 166 `சோர்வுற்றதற்கும்`, scan 168 `அவருக்கும் பேரக் / குழந்தைகட்டும்!`, scan 171 `வெள்ளமெனக் கருதாமல்`, and scan 174 `செல்லூர்க் குணா அது`;
- source-supported compact forms retained after independent review include scan 29 `ஏழைபாழையிடம்`, scan 31 `எனந்தப்`, scan 35 `மரத்தின் அழுத்தமான வேர்` / `மண்டூகே மனிதன்`, scan 47 `சளித்தோமா`, scan 52 `மாக்கலத்தில்`, scan 59 `பெருளான்` / `அவர் ஆராய்`, scan 65 `தொலைவடவர்` / `நேடியாட்சியாகவோ` / `ஒருசன்`, scan 66 `புனரதீர்` / `கைப்பா`, scan 71 `அறிந்திலராகிச்` / `துவேன்`, scan 74 `பொழிவும்` / `சிலதுகள்`, scan 80 `காபியோ`, scan 82 `முறையாகத்தானிருக்கும்!`, scan 85 `பாராட்டும் பெற்றன`, scan 91 `காற்றுக் கொப்புளங்களைச்`, scan 93 `அமைக்கப்பட்ட முடியாதல்லவா?`, scan 97 `சுமோர்` / `நிக்கிதோ சிந்தோ`, scan 104 `வடித்தகள்`, scan 107 `கொண்ட கொண்டலாம் சோழன்`, scan 109 `துரத்தியம்` / `அவனாகக்`, scan 115 `உவைத்து`, scan 116 `கார்முற்றும்`, scan 118 `குன்றிரண்டை` / `கனதனங்கள்`, scan 120 `குவிந்துவரை`, scan 129 `தமிழ்ச்சியர்`, scan 130 `பத்தரை மாற்றுப் பொன்னெனத்`, scan 132 `அஷ்டமாசித்தி`, scan 134 `கலாம் விளைக்கும்`, scan 136 `சாகிரப்`, scan 137 `குருக்கர்` / `ஆரப்பா` / `மொகஞ்சதாரோ` / `அசுரா`, scan 138 `காந்திரதோவ்` / `ஒனசு` / `எரிது`, scan 145 `அய்வரும்` / `அழுந்தார்`, scan 146 `வணங்கி பேற்றிட`, scan 149 `வாணிக்க` / `இதயமா`, scan 150 `தாதரவென`, scan 151 `தந்திருக்கு`, scan 154 `கன்னலாம் தமிழர்க் கென்றும்`, scan 155 `திருமலியும்`, scan 160 `ஆனந்தப் பள்ளுப்பாடி!`, scan 161 `முடியிறந்து` / `நிலமைக்கு` / `அய்ந்து`, scan 162 `பாவுராயத்` / `திருமலியும்` / `காரணத்தியவர்`, scan 164 `இஃதோர்` / `வண்ணனை`, scan 167 `கற்பனையுற்றாய்` / `மார்பகமுற்றி` / `அயிரை`, scan 169 `கவலைவென`, scan 170 `திரும்புவானார்`, scan 172 `நண்பாது`, and scan 175 `கன்னலடா` / `வஞ்சிதனைக்` / `பயற்றும்` / `மேய்ச்ச லென்றால்`;
- unresolved readings through scan 175: **none**;
- next Phase-2 verification batch: **scans 176–200**.

Phase 2 must remain independent visual verification only. Do not begin Phase-3 structure/assembly work or Phase-4 translation until the required later phase transition.
