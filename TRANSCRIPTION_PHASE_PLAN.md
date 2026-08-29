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
- Phase 2 verified range: **scans 1–250 consecutively**;
- completed Phase-2 batches: **1–25**, **26–50**, **51–75**, **76–100**, **101–125**, **126–150**, **151–175**, **176–200**, **201–225**, and **226–250**;
- scan-proven corrections in batch 1: scan 3 `ஈகில் பிரஸ்`, scan 14 `உளியொன்றை`, scan 17 `மாளிகை யொன்றை`, scan 22 `வாய்ப்பை யெனக்`;
- scan-proven corrections in batch 2: scan 28 `பேர்`, scan 35 `மனிதக் கனம்`, scan 36 `கால்நடைப்`, scan 41 `இத்தினையையும்`;
- scan-proven corrections in batch 3 include scan 52 `மனத்துணிவுடைய`, scan 56 `அக்குழந்தை`, scan 61 `கருவிகளை` and the source vocatives `பூவைகாள்` / `புறவங்காள்` / `மயில்காள்` / `மணிக்கிளிகாள்` / `குயில்காள்`, scan 62 `போன்றுவீழ்வது` / `என் மகளாயின்`, scan 67 `ஆயிரம் பேர்`, scan 69 `தீராதி தீர தீன தயாபர`, scan 71 `மாண்டுவிடவில்லை`, scan 72 `மண்டூகே`, scan 73 `அண்ணலே`, and scan 74 `அழும்பில்` / `தோரணங்கற்பட்டு` / `கோட்டைகளிலுள்ள`;
- scan-proven corrections in batch 4 include scan 77 `மணிக் குலத்தைக்`, scan 78 `தூற்றிச் சிலர்`, scan 79 `குரலுக்கோர்` / `மிடுக்குடன்` / `வைர வைடூர்ய`, scan 80 `எலும்பெடுத்து`, scan 82 `தகுதியெல்லாம்`, scan 83 `என்றல்ல` / `வெளிவந்த` / `பூரிப்போடு` / `அங்ஙனமாயின்`, scan 84 `அறந்தங்கும்`, scan 95 `சுற்றி மாற்றிக்`, scan 97 `சமர்` / `எவர்தான்`, and scan 98 `இராமச்சந்திர தீட்சிதர்`;
- scan-proven corrections in batch 5 include scan 109 `அனல் வீழ்` with source-visible five-dot ellipsis, scan 113/114 numeric `எண்பது`, scan 121 `பொன்னை அனைத்தையும்`, and scan 122 `கொண்டாந்து` / `கச்சிதமாக`;
- scan-proven corrections in batch 6 include scan 126 `வாணியது` / `தூமப்பணிகளாக`, scan 128 `எலும்புகளைப்`, scan 130 `அன்னையொருத்தி` / `பாட்டுமார்`, and scan 147 `எடுத்தனன்` / `முரசமொன்று` / `தணித்துக் கொள்வோம்`;
- scan-proven corrections in batch 7 include scan 161 `முற்பட்ட சோழர்களின்`, scan 162 `அமுதூட்டி`, scan 166 `சோர்வுற்றதற்கும்`, scan 168 `அவருக்கும் பேரக் / குழந்தைகட்டும்!`, scan 171 `வெள்ளமெனக் கருதாமல்`, and scan 174 `செல்லூர்க் குணா அது`;
- scan-proven corrections in batch 8 include scan 176 `பழுத்த கிழம்`, scan 177 `அந்தகாராய்` / `அறியாய்க்காரர்களை`, scan 179 `காவற்பெண்டு`, scan 181 `நாத்தழும்பேறி`, scan 183 `சண்டமாருதச் சுழற்சிபோல்`, scan 186 `வருகின்றார் வரலாற்றில்!`, scan 188 `பக்கமெலாம்`, scan 189 `சிறுகுடி யெனும்`, scan 193 `பல தூண்களை` / `சில தூண்கள்`, and scan 194 `எண் ணிலகவர்ந்தே`, together with source-visible punctuation/spacing restorations on scans 181, 182, 184 and 195;
- scan-proven corrections in batch 9 include scan 201 `தர்மராசர் மண்டபமும்`, scan 205 `கட்வல் ; சோர, கேந்தூர்`, scan 206 `கந்தலாடை யொன்றினால்`, scan 210 `திறமனைத்தும்`, scan 212 `குறிப்பிடத்தக்கோர்`, scan 214 `இற்றுப் போகும் ?`, scan 219 `கி.பி. 985 ஜூன் திங்கள்`, scan 224 `கிடைத்த பேறு` / `ஈட்டி யொன்றை அவள் கையால்`, and scan 225 `பேச்சிருக்காது` / `முன்மாதிரியாகத்`;
- scan-proven corrections in batch 10 include scan 228 `குமுறியது` / `வைத்தே திரும்புவேன்`, scan 229 `குலுங்கச் சிரித்து` / `தவித்ததாலே`, scan 230 `இத்திருமணம் தெரிவித்தது!`, scan 233 `கங்க பாடியுந்` / `சிங்கள ஈழ` / `இரட்டபாடி யேழரை` / `நெழில்வள ருழியு ளெல்லா` / `சத்தியாசிரியன்`, scan 234 `இலாடப் பேரரையன்`, scan 240 `கடைப்பிடித்து தமிழ் மக்கள்`, and source-visible punctuation spacing on scan 250 `கூவிடக் கூவிட;`;
- source-supported compact forms retained after independent review include scan 29 `ஏழைபாழையிடம்`, scan 31 `எனந்தப்`, scan 35 `மரத்தின் அழுத்தமான வேர்` / `மண்டூகே மனிதன்`, scan 47 `சளித்தோமா`, scan 52 `மாக்கலத்தில்`, scan 59 `பெருளான்` / `அவர் ஆராய்`, scan 65 `தொலைவடவர்` / `நேடியாட்சியாகவோ` / `ஒருசன்`, scan 66 `புனரதீர்` / `கைப்பா`, scan 71 `அறிந்திலராகிச்` / `துவேன்`, scan 74 `பொழிவும்` / `சிலதுகள்`, scan 80 `காபியோ`, scan 82 `முறையாகத்தானிருக்கும்!`, scan 85 `பாராட்டும் பெற்றன`, scan 91 `காற்றுக் கொப்புளங்களைச்`, scan 93 `அமைக்கப்பட்ட முடியாதல்லவா?`, scan 97 `சுமோர்` / `நிக்கிதோ சிந்தோ`, scan 104 `வடித்தகள்`, scan 107 `கொண்ட கொண்டலாம் சோழன்`, scan 109 `துரத்தியம்` / `அவனாகக்`, scan 115 `உவைத்து`, scan 116 `கார்முற்றும்`, scan 118 `குன்றிரண்டை` / `கனதனங்கள்`, scan 120 `குவிந்துவரை`, scan 129 `தமிழ்ச்சியர்`, scan 130 `பத்தரை மாற்றுப் பொன்னெனத்`, scan 132 `அஷ்டமாசித்தி`, scan 134 `கலாம் விளைக்கும்`, scan 136 `சாகிரப்`, scan 137 `குருக்கர்` / `ஆரப்பா` / `மொகஞ்சதாரோ` / `அசுரா`, scan 138 `காந்திரதோவ்` / `ஒனசு` / `எரிது`, scan 145 `அய்வரும்` / `அழுந்தார்`, scan 146 `வணங்கி பேற்றிட`, scan 149 `வாணிக்க` / `இதயமா`, scan 150 `தாதரவென`, scan 151 `தந்திருக்கு`, scan 154 `கன்னலாம் தமிழர்க் கென்றும்`, scan 155 `திருமலியும்`, scan 160 `ஆனந்தப் பள்ளுப்பாடி!`, scan 161 `முடியிறந்து` / `நிலமைக்கு` / `அய்ந்து`, scan 162 `பாவுராயத்` / `திருமலியும்` / `காரணத்தியவர்`, scan 164 `இஃதோர்` / `வண்ணனை`, scan 167 `கற்பனையுற்றாய்` / `மார்பகமுற்றி` / `அயிரை`, scan 169 `கவலைவென`, scan 170 `திரும்புவானார்`, scan 172 `நண்பாது`, scan 175 `கன்னலடா` / `வஞ்சிதனைக்` / `பயற்றும்` / `மேய்ச்ச லென்றால்`, scan 176 `தலைவில் நின்றவள்`, scan 177 `சூளுரை பொன்றும்`, scan 178 `வீழ்ந்திறந்தார்`, scan 180 `ஆவுக்கு விழுதெனவே` / `கரணையெனக்` / `நற்கிள்ளியனித்த`, scan 184 `கையுசி`, scan 186 `சோணையும்` / `அய்நூறு`, scan 187 `பூழு`, scan 189 `விட்டான்செருக்களத்தில்`, scan 194 `புயங்கொள்ளியை`, scan 197 `தோணியொன்றில்-இந்து` / `இன்மில்லாவிடினும்` / `அகம் வினவு`, scan 198 `எஃகினைய உளம்`, scan 199 `அவர்க்கட்டு`, scan 202 `மாதகர் காஞ்சியின்` / `கருமுகில் தவழுமாடக் கச்சி யேகம் பன்றே` / `வியர்த்தமான வேலை`, scan 203 `நரசிங்கப் போத்தரையன்`, scan 207 `‘மாட்சி’(?)களும்` / `வீர்பால்`, scan 209 `அன்றந்தக் காலம்` / `அகமிக` / `முடிவிழந்த`, scan 210 `“இராஜதந்திரம்” ஆகாது (?)`, scan 211 `அவ்வர் மகன்கள்`, scan 213 `இறும்பூதெய்தினாள்`, scan 217 `ஏற்றுவரே!`, scan 221 `பழங் குலங்கும் பஞ்சசோலைப் பூ மலராத பழங்காலத்தே`, scan 223 `நெரியாத` / `அய்ந்தும் ஆறும்` / `பெண்ணொருத்தி ஒன்று கேட்கும்`, scan 226 `நாற்பத்தி ஆறு` / `தெலுங்கு குல பாலன்`, scan 231 `தளகர்த்தர்களும்` / `வேளக்காரர் படை`, scan 232 `மகேசன் தொண்டு`, scan 233 `நெழில்வள ருழியு ளெல்லா` / `பிருதிகண்ட வர்மன்`, scan 234 `பணி தொடர்பவனாய்` / `புயற் காற்று`, scan 236 `சம்பந்தப்பட்டதிப்`, scan 237 `ஒடுக்கலாகிவிட்டவைகள்`, scan 238 `உலகளவித்த திருவடிகள் சாத்தன்`, scan 239 `அரசோச்சிய` / `கலிங்கு வாரியம்`, scan 242 `கூளி முறிப்பது` / `‘மண்ணைக் கடக்க’மெனும்`, scan 243 `இடுப்பொடித்துப்`, scan 244 `நாமணைக் கோணமும்` / `இரணசூரன்` / `தெக்கண லாட`, scan 247 `ஆசிர்வாதம்` / `அய்ந்து குடுமி` / `அரவாணி`, scan 248 `துவரபாலகர்` / `அயிராவ தேசுவர்`, scan 249 `சமர்களத்தில்`, and scan 250 `படைத்தனை`;
- unresolved readings through scan 250: **none**;
- next Phase-2 verification batch: **scans 251–275**.

Phase 2 must remain independent visual verification only. Do not begin Phase-3 structure/assembly work or Phase-4 translation until the required later phase transition.
