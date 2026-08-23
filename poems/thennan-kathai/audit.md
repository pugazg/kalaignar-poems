# தென்னவன் காதை — Audit

## Source identity

- title: **தென்னவன் காதை**
- author: **கலைஞர் மு. கருணாநிதி**
- publication: **முரசொலி-பொங்கல் மலர்**
- edition/year: **1956**
- correct work range: **145–152**

User-supplied contextual description:

`தென்னிலங்கை வேந்தன் இராவணனைத் தமிழ்ப் பண்பாட்டுக் காவலனாகக் காட்டும் கலைஞர் அவர்களின் கவிதை நடைச் சித்திரம்.`

This is contextual metadata only and is not imported into the poem body.

## Source set

### Pages 145–150

- file: `TVA_PRL_0007090_முரசொலி.pdf`
- SHA-256: `a9252bcb0931366c61497d55a354964b1450a8254d2ca3f119c5f6b1c680a643`
- file size: **246,184,679 bytes**
- source form: image scan; no usable text layer

### Page 151

- user-supplied one-page PDF: `af978d0a2b6ae807620bd0167c453d1e83c95130.pdf`
- SHA-256: `9020615bed68a8467dbe4adc8dca05f1e04f123c1ad038201a864bcb1bc0379d`
- supplied: **2026-08-23**

### Page 152

- user-supplied one-page PDF: `f34bc565cd5cbae27e96a92ef704cb8f21fd1270.pdf`
- SHA-256: `1d1b52abd203ddaf690e659874ba58fa4344539648f1b6bfa7c66ac408c2206a`
- supplied: **2026-08-23**

The user confirms pages **145–152** as the poem. The two terminal page images visibly continue the illustrated poem beyond page 150.

The earlier Kalaignar Karuvoolam description/page-range inference is **superseded as incorrect** and is not used for this work's boundaries.

## Verification reset — prior PASS invalidated

The earlier repository state marked scans 145–150 `verified` and later recorded a full available-range audit as `PASS`.

That conclusion remains **withdrawn for the old verification cycle**. Pages are restored to `verified` only after the replacement blank-buffer recovery protocol.

A user spot-check of scan 145 exposed multiple transcription errors that had survived both earlier page verification and the later audit. The error density on one page proved that the prior method was not sufficiently independent or glyph-first.

## Current recovery status

| Status | Count |
|---|---:|
| verified | 2 |
| needs-review | 4 |
| not-started | 2 |

- pages **145–146**: `verified` under the replacement recovery protocol;
- pages **147–150**: `needs-review`;
- pages **151–152**: `not-started`;
- physical page-image availability: **8/8 complete**;
- Tamil assembly: **BLOCKED**;
- English translation: **BLOCKED**.

## Scan 145 — failure corrections established during reopening

The following errors were documented before the fresh recovery pass:

| Earlier repository reading | Later assistant re-reading | Correct source reading |
|---|---|---|
| `தாடிப்பட்டாள` | `தாடியுடனே` | `தாடியுடனே` |
| `பூசாரிகள்` | `புசாரிகள்` | `பூசுரர்கள்` |
| `மாடுகள், ஆடுகள்` | `மாடுகளே, ஆடுகளே` | `மாடுகளை, ஆடுகளை` |
| `மனிதர்கள்` | `மனிதர்களே` | `மனிதர்களை` |
| `மேடுகள் வேள்விகளென` | `மேடுகளே வேள்விக்கென` | `மேடுகளை வேள்விக்கென` |
| `நின்றன` | `நின்றான்` | `நின்றான்` |
| `கோமான` | `கோமான்` | `கோமான்` |
| `பற்றுதல்` | `பற்றுதலை` | `பற்றுதலை` |
| `முல்லைத்` | `மலைத்` | `மலைத்` |
| `தோற்றுத்` | `தோற்றுப்` | `தோற்ப` |
| `பலிதரும் வேளை` | `பலிதேடும் வேளை` | `பலிதேடும் வேலை` |

Additional source-backed corrections found during the failure review:

- `போதை ஏறிக்` → `போதையேறிக்`;
- `உருவில் சிங்கம்.` → `உருவில் சிங்கம்,`;
- the inserted dash in `மாடுகள், ஆடுகள்—மனிதர்கள்` was removed; source reads `மாடுகளை, ஆடுகளை மனிதர்களை வெட்டிப் பிண`.

See `notes/TRANSCRIPTION_FAILURE_REVIEW_2026-08-23.md` for the detailed root-cause analysis.

## Scan 145 — fresh blank-buffer recovery audit — PASS

Scan 145 was redone from a fresh high-resolution render under the replacement protocol. A blank-buffer reading and second enlarged pass confirmed the corrected source readings and exposed one additional spacing discrepancy:

- `கண்ணுக்குள் பாவைபோல் இலங்கைத் தீவு.` → `கண்ணுக்குள் பாவை போல் இலங்கைத் தீவு.`

Explicit checks included the title, one `★`, punctuation in `உருவில் சிங்கம், உள்ளம் தங்கம்!`, absence of an inserted dash in `மாடுகளை, ஆடுகளை மனிதர்களை`, semicolon in `காப்பதற்கு;`, exclamation in `அவனுக்கு அவள்!`, and the continuation `கடவுளுக்குப் பலிதேடும் வேலை, ஆகாது`.

Result: **scan 145 VERIFIED under the recovery protocol.**

## Scan 146 — fresh blank-buffer recovery audit — PASS

Scan 146 was independently rendered at **600 dpi** and reread from a blank working buffer before the provisional repository text was consulted.

A second enlarged source-pixel pass checked:

- every visible line in both columns;
- word-final suffixes and compact clusters;
- punctuation and line breaks;
- the single visible `★` separator;
- the page-145 → page-146 continuation;
- the later circular stamp/library-mark overlap in the lower text;
- the open ending into scan 147.

The recovery diff found two source-backed errors that had survived the former verification cycle:

| Provisional repository reading | Source-backed recovery reading |
|---|---|
| `மண்பாளும்` | `மணையாளும்` |
| `காவலுக்குக் கைகாரி சீதாதேவி!` | `காவலுக்குக் கைக்காரி சீதாதேவி!` |

The recovery pass independently rechecked earlier source-backed readings already present in the provisional record, including `உருவினை கொடுவாள்`, `காடெல்லாம்`, `வழிந்திடுதே`, `விட்டதாலே`, `முடிசூட முனைந்து`, and `தூங்குகின்றுள்`; they were retained.

Explicit punctuation/structure checks:

- opening continuation from page 145: `...பலிதேடும் வேலை, ஆகாது` → `கொடுமையென உருவினை கொடுவாள்!` — PASS;
- `அட, தொடுவேனோ ஆரியத்தேன் என` — PASS;
- `அந்தக் காளை!....` — exclamation plus four following dots retained;
- one visible `★` separator — PASS;
- left-column then right-column reading order — PASS;
- final visible line `கற்புக்கனல் காக்கக் கொதித்தெழுந்தாள்....` — PASS and remains open into scan 147.

Result: **scan 146 VERIFIED under the recovery protocol.**

## Where the previous process failed

The failure pattern remains documented as procedural:

1. later checks were anchored to the existing transcription instead of starting blind from source pixels;
2. familiar Tamil words were accepted because they were semantically plausible;
3. suffixes and final consonants were not always independently verified;
4. compact old-print clusters were not always decomposed character by character;
5. punctuation and spacing were sometimes normalized instead of read from ink;
6. the previous “full-range audit” was not a true blank-slate retranscription of every line.

## Source-first safeguards now in force

- source pixels control every glyph, suffix, punctuation mark, separator and line break;
- existing repository text is **not** a reading aid during the fresh pass;
- each line must first be transcribed blind from the scan;
- only after a blind reading may the old repository line be opened as a diff target;
- a second glyph-level pass is mandatory before `verified`;
- plausible semantics never override uncertain glyphs;
- uncertain readings remain explicitly unresolved rather than being completed from context.

## Source completeness

Physical source availability is **COMPLETE for 145–152** because pages 151 and 152 have been supplied directly by the user.

This supersedes the earlier `SOURCE_COMPLETENESS_REVIEW.md` conclusion that depended on the incorrect Kalaignar Karuvoolam description.

## Readiness

- physical page images: **COMPLETE — 8/8**
- verified transcription: **2/8**
- pages needing re-audit: **147–150**
- pages awaiting first transcription: **151–152**
- Tamil assembly: **BLOCKED**
- English translation: **BLOCKED**

## Exact next activity

Redo **scan 147 from scratch** with a blank source-first transcription and a second independent glyph-level comparison.

Do not reuse the current page text as a reading guide. Only after scan 147 is independently clean may it be restored to `verified`, then continue sequentially through **148–152**.