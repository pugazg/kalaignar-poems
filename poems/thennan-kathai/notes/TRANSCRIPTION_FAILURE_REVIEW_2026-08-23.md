# தென்னவன் காதை — transcription verification failure review

Date: **2026-08-23**

## Why this review exists

The earlier workflow marked scans 145–150 `verified` and later recorded a full-range audit as `PASS`. A user spot-check of scan 145 demonstrated that this confidence was not justified: multiple ordinary-looking Tamil words, grammatical suffixes and punctuation marks had been misread even after enlarged review.

This note records **where the transcription process failed**, separates the earlier repository readings from later assistant re-readings, and fixes the verification policy before work continues.

The controlling authority remains the **source pixels**. The user-provided corrections below were rechecked against enlarged scan-145 pixels and are adopted as source-backed corrections. They are not semantic normalization.

## Scan 145 — demonstrated misses

| Earlier repository reading | Later assistant re-reading | Source-backed correction | What was missed |
|---|---|---|---|
| `தாடிப்பட்டாள` | `தாடியுடனே` | `தாடியுடனே` | The original word had been segmented into a completely different, plausible-looking form instead of being read glyph by glyph. |
| `பூசாரிகள்` | `புசாரிகள்` | `பூசுரர்கள்` | The `சுரர்கள்` cluster was not resolved. A familiar lexical form (`பூசாரிகள்`) then anchored the first transcription, and the later pass still failed to read the repeated `ர` glyphs. |
| `மாடுகள், ஆடுகள்` | `மாடுகளே, ஆடுகளே` | `மாடுகளை, ஆடுகளை` | The accusative `-ளை` endings were missed twice: first dropped, then misread as emphatic `-ளே`. |
| `மனிதர்கள்` | `மனிதர்களே` | `மனிதர்களை` | The final accusative `-ை` was not read; semantic/grammatical expectation was allowed to substitute for the printed ending. |
| `மேடுகள் வேள்விகளென` | `மேடுகளே வேள்விக்கென` | `மேடுகளை வேள்விக்கென` | The same `-ளை` failure recurred in `மேடுகளை`; the first transcription also mis-segmented `வேள்விக்கென`. |
| `நின்றன` | `நின்றான்` | `நின்றான்` | The word-final `-ஆன்` sequence was not resolved on the first pass. |
| `கோமான` | `கோமான்` | `கோமான்` | Final `ன்` / long-vowel ending was lost in the first transcription. |
| `பற்றுதல்` | `பற்றுதலை` | `பற்றுதலை` | The terminal `லை` was dropped. |
| `முல்லைத்` | `மலைத்` | `மலைத்` | Internal vowel/consonant shapes were over-read as the familiar word `முல்லை`; source pixels show `மலைத்`. |
| `தோற்றுத்` | `தோற்றுப்` | `தோற்ப` | The compact `ற்ப` cluster was repeatedly mis-segmented as `ற்றுத்/ற்றுப்`. The source line reads `தோற்ப தெல்லாம்...`. |
| `பலிதரும் வேளை` | `பலிதேடும் வேளை` | `பலிதேடும் வேலை` | First pass misread the verb cluster (`தரும்` for `தேடும்`); the second pass corrected that but still substituted `வேளை` for source `வேலை`, a `ல/ள` failure reinforced by semantic plausibility. |

## Additional scan-145 misses found during the failure review

Direct enlarged reinspection also found items not in the user's initial word list:

- `போதை ஏறிக்` → source-visible **`போதையேறிக்`**;
- `உருவில் சிங்கம். உள்ளம் தங்கம்!` → source-visible **`உருவில் சிங்கம், உள்ளம் தங்கம்!`**;
- the earlier inserted em dash in `மாடுகள், ஆடுகள்—மனிதர்கள்` is not source-backed; the source line reads **`மாடுகளை, ஆடுகளை மனிதர்களை வெட்டிப் பிண`**.

These corrections reinforce that punctuation and spacing must be checked from ink, not carried over from an earlier transcription.

## Root-cause analysis

The failure was **procedural**, not limited to one difficult glyph.

1. **Confirmation bias from the existing transcription** — later passes repeatedly compared the scan against already typed text instead of starting from a blank line-by-line reading.
2. **Semantic substitution** — familiar or grammatically plausible Tamil was accepted when the printed glyphs supported a different form.
3. **Weak suffix verification** — word-final suffixes and final consonants were not independently checked at character level.
4. **Cluster segmentation failure** — compact old-print clusters were sometimes treated as whole-word shapes rather than decomposed glyph by glyph.
5. **Audit scope drift** — the earlier “full-range audit” concentrated on previously suspicious readings, page joins and selected enlarged crops; it was **not a truly blind, fresh transcription of every line**.
6. **Punctuation was normalized by eye** rather than consistently verified from source ink.

## Verification consequence

The earlier `verified`/`PASS` claims for scans 145–150 are **withdrawn**. They cannot be used as evidence that those old verification results were accurate.

Required recovery policy:

- each affected scan must be reopened and redone independently;
- scans **151–152**, now supplied by the user, remain `not-started` until separately transcribed;
- first-transcription work must be a **blind source-first transcription from a blank working buffer**, one full line at a time;
- every line must receive a second glyph-level comparison before it can return to `verified`;
- suffixes, compact clusters, punctuation, separators and line-end continuations must each be checked explicitly;
- earlier repository text may be used only as a diff target, never as authority over source pixels.

## Recovery progress — scan 145

Scan **145** has completed the replacement recovery protocol and is again **VERIFIED**.

The page was freshly rendered at high resolution and retranscribed source-first before comparison with the repository record. A second enlarged pass checked every visible line, punctuation mark, suffix, separator and the continuation into scan 146.

The recovery pass independently confirmed all source-backed corrections listed above and found one additional discrepancy that had survived the reopening stage:

- `கண்ணுக்குள் பாவைபோல் இலங்கைத் தீவு.` → **`கண்ணுக்குள் பாவை போல் இலங்கைத் தீவு.`**

## Recovery progress — scan 146

Scan **146** has also completed the replacement recovery protocol and is **VERIFIED**.

A fresh **600-dpi** render was read from a blank working buffer before opening the provisional repository transcription. A second enlarged pass checked both columns, punctuation, the single `★`, the circular stamp/library-mark overlap, and both page joins.

The recovery diff exposed two additional source-backed errors that had survived the former verification cycle:

- `மண்பாளும்` → **`மணையாளும்`**;
- `காவலுக்குக் கைகாரி சீதாதேவி!` → **`காவலுக்குக் கைக்காரி சீதாதேவி!`**.

The pass also independently rechecked the existing source-backed readings `உருவினை கொடுவாள்`, `காடெல்லாம்`, `வழிந்திடுதே`, `விட்டதாலே`, `முடிசூட முனைந்து`, and `தூங்குகின்றுள்` rather than inheriting them from the earlier audit.

## Recovery progress — scan 147

Scan **147** has completed the same blank-buffer recovery protocol and is **VERIFIED**.

A fresh **600-dpi** render was transcribed before the provisional repository text was consulted. A second enlarged review covered both columns, the single `★`, quotation marks, compact clusters, the later circular stamp/library-mark overlap, and the 146→147 / 147→148 joins.

The recovery diff exposed eight source-backed errors that had survived the former verification cycle:

- `கற்புக்கு விலையாக` → **`கற்புக்கு விலையாகக்`**;
- first `முத்துகை` → **`முத்துநகை`**;
- `குத்திரியாச்` → **`சுத்திரியாச்`**;
- `குர்ப்பனகை` → **`சூர்ப்பனகை`**;
- second `முத்துகை` → **`முத்துநகை`**;
- `மாடொன்று` → **`மானொன்று`**;
- `முத்தவனும்` → **`மூத்தவனும்`**;
- `என்ன உனக்குத்` → **`என்னை உனக்குத்`**.

The pass independently reconfirmed the previously corrected readings `பாங்கமுள்ள`, `அண்ணிக்கு விலை / விசம் நினைப்போ`, and `தேர்போல`.

## Recovery progress — scan 148

Scan **148** has completed the same blank-buffer recovery protocol and is **VERIFIED**.

A fresh **600-dpi** render and the native embedded page image were read before the provisional repository transcription was consulted. A second enlarged review covered both columns, punctuation, quotation marks, compact clusters, the single `★`, the circular stamp/library-mark overlap, and the 147→148 / 148→149 joins.

The recovery diff exposed six source-backed errors that had survived the former verification cycle:

- `பாடுபட்டாமல்` → **`பாடுபடாமல்`**;
- `பதினுபிரம்` → **`பதினாயிரம்`**;
- `போனுள்தானென்ன` → **`போனால்தானென்ன`**;
- `விட்டணன்......` → **`விட்டணன்.....`** — the source has five following dots;
- `இலங்கையமா` → **`இலங்கைமா`**;
- `சூழ்ச்சியிலே` → **`சூழ்ச்சியினில்`**.

The pass independently reconfirmed `மரபினிலே`, `விறகொடித்து`, `காத்தி- / ருப்போன்`, `யொன்றின்`, and `தாப்பைகளின்` rather than inheriting them from the earlier audit.

## Recovery progress — scan 149

Scan **149** has completed the same blank-buffer recovery protocol and is **VERIFIED**.

A fresh **600-dpi** render and the native embedded page image were read before the provisional repository transcription was consulted. A second enlarged review covered both columns, punctuation, quotation marks, compact clusters, all three `★` separators, the circular stamp/library-mark overlap, and the 148→149 / 149→150 joins.

The recovery diff exposed five source-backed errors that had survived the former verification cycle:

- `விபீஷண!` → **`விபீஷணு!`**;
- `உடை வாளைப் போலப்` → **`உடை வாளிப் போலப்`**;
- `கடைக் குட்டி தம்பியவன் எதிர்வந்து நின்றான்,` → **`கடைக் குட்டி தம்பியவன் எதிர்வந்து நின்றுன்,`**;
- `படை திரட்டிப் பயனில்லை—பாழாகும் என்றுன்!` → **`படை திரட்டிப் பயனில்லை-பாழாகும் என்றுன்!`**;
- `நடைகட்டு என்றே` → **`நடை கட்டு என்றே`**.

The pass independently reconfirmed unusual source-visible readings already present in the provisional record, including `என்றுன்!`, `நின்றுன்—`, `சென்றுன்,`, `ஜடை கட்டி`, `அறுத் தெறியாமல்`, `பிடியே!.....`, and `இன்றிகத்`.

## Recovery progress — scan 150

Scan **150** has now completed a fresh high-resolution source recovery and is **VERIFIED**.

A fresh **600-dpi** render and the native embedded page image were used to reread every visible line directly. The current page record had been loaded to establish repository state, but provisional wording was not accepted unless the source pixels directly confirmed it. A second enlarged pass covered both columns, punctuation, unusual word forms, the circular stamp/library-mark overlap, and the 149→150 / 150→151 joins.

The recovery comparison exposed two source-backed errors that had survived the former verification cycle:

- `அவரை நத்திக் கிடப்போர்;` → **`அவரை நத்திக் கிடப்போர்,`**;
- `ஆரணயம் ஓடிவந்த இராமன்,` → **`ஆரண்யம் ஓடிவந்த இராமன்,`**.

The pass independently reconfirmed unusual source-visible readings already present in the provisional record, including `எதிர்க்கின்றூர்`, `பென்றால்`, `போடுகின்றூர்`, `தீப்பந்தனைய`, `பூப்பந்தனைய`, `யாப்புணையும்`, `கோப் பெருந்தேவியவள்`, and `தந்தோன் !`. Scan 150 contains no visible `★`; its final visible line is `கட்டி!`, and the user-supplied scan 151 continues the poem on the following page.

The recovered verification status therefore currently applies to scans **145–150**. Scans **151–152** remain `not-started` and must be transcribed independently from their supplied source images.

## Source-range correction

The earlier source-completeness reasoning relied on an incorrect Kalaignar Karuvoolam description/page-range note. The user has explicitly corrected the work range to **145–152** and supplied the two missing terminal page images.

Therefore the Karuvoolam description must not be used to determine this poem's boundaries. See `../SOURCE_COMPLETENESS_REVIEW.md` for the corrected completeness record.

## Exact next activity

Transcribe **scan 151 from scratch** from the user-supplied one-page source. Use a blank source-first transcription and a second independent glyph-level comparison before assigning any verification status.

Do not begin scan 152 until scan 151 is independently complete.