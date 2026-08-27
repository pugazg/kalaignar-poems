# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Mandatory startup for every continuation

1. Read `POEM_PROCESSING_GUIDE.md` completely.
2. Read `TRANSCRIPTION_PHASE_PLAN.md` completely.
3. Read root `README.md`.
4. Read `NEXT_CHAT_PROMPT.md`.
5. For an existing work, read its `README.md`, `metadata/source.md`, `indexes/page-map.md`, `audit.md`, `ASSEMBLY_REVIEW.md`, and `SOURCE_COMPLETENESS_REVIEW.md` when present.
6. For English translation work, also read `translations/en/README.md`, `translations/en/TRANSLATION_PLAN.md`, `translations/en/SOURCE_MAP.md`, completed batch files, the complete English assembly, `EDITORIAL_CONSISTENCY_REVIEW.md`, and `RELEASE_REPORT.md` when present.
7. Inspect existing files before creating anything; continue existing work and do not duplicate records.
8. The supplied scan remains controlling for Tamil source wording. Do not silently normalize Tamil or poem lineation.
9. Do not commit source PDFs.
10. Determine the declared current phase before doing any work and do not perform activities belonging to a later phase.

## CURRENT ACTIVE WORK — காலப் பேழையும் கவிதைச் சாவியும்

Slug: `poems/kaalap-pezhaiyum-kavithai-saaviyum/`  
Tamil title: **காலப் பேழையும் கவிதைச் சாவியும்**  
Author: **கலைஞர் மு. கருணாநிதி**  
Controlling source: `TVA_BOK_0063593_காலப்_பேழையும்_கவிதைச்_சாவியும்.pdf`  
Physical scans in directly opened PDF: **306**.

### Current phase — Phase 1: TRANSCRIPTION ONLY

The user explicitly changed the workflow for this book-length source: **finish transcription first; defer verification and all other archival activities to later phases**.

Governing phase reference: `TRANSCRIPTION_PHASE_PLAN.md`.

Current Phase-1 rules:

- continue sequentially from the controlling scan;
- transcribe visible edition text faithfully into `pages/NNNN.md`;
- preserve spelling, punctuation, headings, lineation, quotation marks and unusual forms exactly as seen;
- record visible printed page numbers but do not infer invisible numbers;
- exclude later stamps/handwriting/show-through from edition text;
- explicitly record genuine uncertainty rather than guessing;
- new pages transcribed from scan 10 onward should normally be `partial`, or `needs-review` when a specific unresolved reading exists;
- do **not** call a new page `verified` merely because it has been transcribed once;
- do not perform a separate glyph-by-glyph verification pass;
- do not perform systematic continuity/page-join audit;
- do not perform work-wide structural/completeness audit;
- do not assemble canonical Tamil;
- do not start English translation;
- avoid routine control-document updates after every small transcription batch; update them at milestones, anomalies, or phase changes.

Existing work completed before this phase switch remains valid:

- scans **1–9** already have genuinely verified page records and remain `verified`;
- front matter through scan 9 is already recorded;
- contents entries **58/58** are already represented;
- scan 5 correctly has no visibly printed page number;
- scan 9 is already resolved as a blank verso with show-through only.

### Exact next activity

Begin Phase-1 transcription at **scan 10** and continue sequentially. The immediate task is to create the transcription record for scan 10, then continue to subsequent scans without pausing for the deferred Phase-2 verification or Phase-3 structural/assembly work.

Phase 1 remains active until the user explicitly advances this work to Phase 2.

---

## Other ongoing work — தென்னவன் காதை

Slug: `poems/thennan-kathai/`  
Tamil title: **தென்னவன் காதை**  
Author: **கலைஞர் மு. கருணாநிதி**  
Publication: **முரசொலி-பொங்கல் மலர்**  
Year: **1956**  
Correct physical poem range: **scans 145–152**.

Source holdings:

- scans 145–150: `TVA_PRL_0007090_முரசொலி.pdf`;
- scans 151–152: separately supplied one-page PDFs.

The earlier Kalaignar Karuvoolam description/range inference is **superseded as incorrect**.

### Tamil archival status

- physical source images: **8/8 available**;
- page records: **8/8 present**;
- verified/reconciled: **8/8**;
- user lexical-control reconciliation: **scans 147–152 complete**;
- final continuity audit: **7/7 joins PASS**;
- visible `★` separators across work: **8**;
- canonical Tamil assembly: `poems/thennan-kathai/sections/thennan-kathai.md`;
- assembly review: **PASS**;
- Tamil layer: **FINAL-CLEARED**.

Important recovery history:

- scan 146 required a third source-critical re-audit after eleven user-detected old-glyph/suffix errors;
- scans 147–152 were reconciled to user-supplied lexical controls after repeated old-Tamil-typeface misreadings, especially `-ஆன்` / `-உன்` confusion and whole-word substitution;
- scan 151 contains **one explicit user-directed omission of a caste-based slur without replacement**. The excluded term must not be restored, reconstructed, quoted, transliterated, paraphrased or replaced in later assembly/translation work unless the user explicitly changes this instruction;
- during English EN-01 Gate A review, a final scan-145 source punctuation discrepancy was caught: `பூசுரர்கள் கூட்டம்....` → `பூசுரர்கள் கூட்டம்...` (three dots). The page record, canonical assembly and EN-01 were synchronized; continuity/assembly PASS remained valid after revalidation.

### English translation status

Workspace: `poems/thennan-kathai/translations/en/`

- `TRANSLATION_PLAN.md`: **REVIEWED / PASS**;
- `SOURCE_MAP.md`: **REVIEWED / PASS**;
- `PLAN_REVIEW.md`: **PASS**;
- EN-01 scans 145–146: `batches/EN-01-scans-145-146.md` — **REVIEWED / PASS**;
- Gate A: `GATE_A_REVIEW.md` — **PASS**;
- EN-02 scans 147–148: `batches/EN-02-scans-147-148.md` — **REVIEWED / PASS**;
- Gate B: `GATE_B_REVIEW.md` — **PASS**;
- EN-03 scans 149–151: **NOT STARTED — next permitted batch when this work is resumed**;
- EN-04 scan 152: **BLOCKED pending Gate C**;
- final assembled English poem: **NOT STARTED**.

Gate A baseline includes:

- preserve the poem's openly partisan narrator and rhetorical force;
- `ஆரியர்` → `Aryan / Aryans`;
- `பூசுரர்கள்` → `earth-god priests` in its scan-145 context;
- `இருடிகள்` → `rishis`;
- `தமிழரசி` → `Tamil queen`;
- `யாழ்ப்பாணத் திருநாட்டான்` → `a man of sacred Yalpanam`, not the over-strong draft `lord`;
- `கரும்பனைய` → `like a stalk of sugarcane`, without an unsupported colour inference;
- `காவலுக்குக் கைக்காரி` → `an accomplice standing guard`, preserving the narrator's accusatory agency.

Gate B adds:

- preserve scan 147's unusual quotation punctuation rather than silently balancing it;
- `தென்னவன்` → `the Southerner` in the reviewed local passage;
- `ஐந்தாம்படை` → `fifth-column force`;
- keep compressed images such as honour put aboard a ship, palmyra fruit and darbha-grass stratagems visible rather than explaining them inside the poem;
- preserve the scan-147→148 ship/boarding narrative as continuous across the provenance boundary;
- user-confirmed scan-148 lexical forms control the English; no superseded `நின்றுள்` / `என்றுன்`-class reading may return.

### Next activity when தென்னவன் காதை is explicitly resumed

Begin **EN-03 — scans 149–151 only** from the canonical Tamil assembly and the final user-controlled page records.

Mandatory EN-03 constraints:

1. keep the direct speech opened on scan 149 continuous through scan 150 and close it only where the canonical scan-151 text closes it;
2. preserve the page-151 user-directed omission exactly as omission — do not restore, reconstruct, quote, transliterate, paraphrase, replace or indirectly supply the excluded term;
3. use the Gate A terminology baseline and Gate B consistency decisions;
4. do not reintroduce superseded Tamil readings from earlier scan interpretations.

After the EN-03 draft, perform **Gate C omission/speech review before starting EN-04**. Do not begin EN-04 in the same activity.

---

## First completed work

Slug: `poems/idhayathai-thanthidu-anna/`  
Tamil title: **இதயத்தைத் தந்திடு அண்ணா**  
English title: **Lend Me Your Heart, Anna**  
Source file: `TVA_BOK_0064132_இதயத்தைத்_தந்திடு_அண்ணா.pdf`  
SHA-256: `152cfb251a2049662102a2296487220f6f227f243657c9456df34105520676fe`  
Scan pages: **28**

Scan 13 states that on **9.2.1969**, on **சென்னை வானொலி**, **கலைஞர் மு. கருணாநிதி** offered the poem as a **கண்ணீர்க் கவிதாஞ்சலி** to **பேரறிஞர் அண்ணா**. Do not replace this source wording with an inferred event description.

## Tamil archival/source layer — COMPLETE

- physical scans verified: **28 / 28**
- poem scans verified: **14 / 14**
- `needs-review`: **0**
- `blocked`: **0**
- Tamil assembly: **PASS; 14/14 page blocks; 0 discrepancies**
- physical completeness: **PASS; 28/28**

Locked boundaries:

- scan 13 context note outside verse;
- scan 26 printer imprint outside verse;
- scans 27–28 back matter outside verse;
- no source wording normalized during assembly.

Important difficult source forms remain exactly as verified in the Tamil archive, including `களப்பரணி..`, `அய்ம்பத்திரண்டுதனில்`, repeated `முன்றெழுத்து`, `எடெல்லாம் வீடெல்லாம் தமிழ்`, `மாண்பே! .`, `பிரிவாய்மாறி`, `கீரியென்றால்`, `சழக்கரால்`, `மாறிற்றுத் தமிழர் மனம்`, `கடிதோச்சி`, `போதாகி மலர்கின்ற`, `கால்டுவெல் போப்புக்கும் சிலை`, `பற்றுதனை உலகறிய ; அந்த`, and `இதயத்தை தந்திடண்ணா..`.

## English translation — RELEASE-COMPLETE

Governing instruction:

> **Retain Kalaignar's language while translating.**

This remains a hard editorial requirement for future translations: preserve direct address, public cadence, repetition, slogans, rhetorical questions, political specificity, literary/classical references, source imagery and emotional escalation. Do not genericize Kalaignar, neutralize politics, paraphrase away repetition, invent corrected Tamil, or use fake archaism.

Translation priority: **voice fidelity before elegance**.

### Batch status

| Batch | Scans | Printed pages | Status |
|---|---:|---:|---|
| 01 | 13–15 | 11–13 | **reviewed — PASS** |
| 02 | 16–19 | 14–17 | **reviewed — PASS** |
| 03 | 20–21 | 18–19 | **reviewed — PASS** |
| 04 | 22–23 | 20–21 | **reviewed — PASS** |
| 05 | 24–26 | 22–23 + unnumbered | **reviewed — PASS** |

Across all batches:

- source poem scans represented: **14/14**
- omissions / duplications: **0/0**
- source/continuity reviews: **PASS**
- Kalaignar voice reviews: **PASS**

### Complete English assembly

Files:

- `translations/en/idhayathai-thanthidu-anna-en.md`
- `translations/en/EDITORIAL_CONSISTENCY_REVIEW.md`
- `translations/en/RELEASE_REPORT.md`

Assembly/review result:

- assembly status: **`reviewed-assembly`**
- reviewed batches present: **5/5 once each**
- Tamil poem scans represented: **14/14**
- missing batch bodies: **0**
- duplicate batch bodies: **0**
- non-verse exclusions: **PASS**
- Batch 01 → 02 continuity: **PASS**
- Batch 02 → 03 paired-question continuity: **PASS**
- Batch 03 → 04 social-critique continuity: **PASS**
- Batch 04 → 05 `pathigam → purappāṭṭu` continuity: **PASS**
- names/titles/political vocabulary consistency: **PASS**
- literary-term / selective transliteration policy: **PASS**
- repetition and rhetorical architecture: **PASS**
- image/motif continuity: **PASS**
- full-poem Kalaignar-language/voice review: **PASS**

Release report result: **PASS — English translation RELEASE-COMPLETE.**

Full-poem review confirms retention of:

- `A flood! / A flood! / A mighty flood!`;
- repeated `three letters` architecture;
- compact Anna slogans/quotations;
- `Anna`, `Ayya`, `Kazhagam`, `Dravidar Kazhagam`, `Munnetra Kazhagam`, `Muttamil`, `Parani`, `Tirukkural/Kural`, `Navalar`, `pathigam`, `purappāṭṭu`;
- Mother Tamil/Valluvar dramatic dialogue;
- public cultural/statue catalogue;
- abrupt transition into grief;
- repeated direct questions;
- `You will not come; you will not come;`;
- final borrowing/return logic: `lend me your heart, Anna..`;
- final `foot-flowers` echo of the opening flower/body imagery.

The English title **Lend Me Your Heart, Anna** is a translation-layer decision reflecting the closing `இரவலாக` borrowing logic. The Tamil title remains exactly **இதயத்தைத் தந்திடு அண்ணா**.

No change to the verified Tamil source layer was required during English release closure.

## Current release state

**இதயத்தைத் தந்திடு அண்ணா is CLOSED:** Tamil archival/source layer complete; English translation release-complete.

Do not retranscribe, normalize, retranslate or modify this released work unless a genuine source-level discrepancy is found and documented, or the user explicitly requests a separately tracked editorial revision.

## General next-repository rule

For any new Kalaignar poem supplied by the user:

1. inspect the actual source scan before metadata;
2. confirm the work has not already been started;
3. create source identity/checksum/page map;
4. determine whether the work will use the normal integrated workflow or an explicit phased workflow;
5. when phased mode is declared, follow `TRANSCRIPTION_PHASE_PLAN.md` and do not cross phase boundaries without user authorization;
6. transcribe page-by-page under `POEM_PROCESSING_GUIDE.md`;
7. complete source-critical verification and Tamil source/assembly review before English translation;
8. when translating, preserve the same **Kalaignar-language/voice fidelity** standard established here.
