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
2. **Semantic substitution** — familiar or grammatically plausible Tamil (`பூசாரிகள்`, `வேளை`, `முல்லை`) was accepted when the printed glyphs supported a different form.
3. **Weak suffix verification** — word-final `-ளை`, `-ை`, `-லை`, `-ஆன்` and final consonants were not independently checked at character level.
4. **Cluster segmentation failure** — compact old-print clusters such as `சுரர்கள்` and `ற்ப` were treated as whole-word shapes rather than decomposed glyph by glyph.
5. **Audit scope drift** — the earlier “full-range audit” concentrated on previously suspicious readings, page joins and selected enlarged crops; it was **not a truly blind, fresh transcription of every line**.
6. **Punctuation was normalized by eye** — punctuation such as the comma after `சிங்கம்` and the absence of a dash after `ஆடுகளை` was not always verified against source ink.

## Verification consequence

The earlier `verified`/`PASS` claims for scans 145–150 are **withdrawn**. They cannot be used as evidence that those old verification results were accurate.

Required recovery policy:

- each affected scan must be reopened and redone independently;
- scans **151–152**, now supplied by the user, remain `not-started` until separately transcribed;
- the recovery pass must be a **blind source-first transcription from a blank working buffer**, one full line at a time;
- every line must receive a second glyph-level comparison before it can return to `verified`;
- suffixes, compact clusters, punctuation, separators and line-end continuations must each be checked explicitly;
- earlier repository text may be used only **after** a blind reading, as a diff target—not as a reading aid.

## Recovery progress — scan 145

Scan **145** has now completed the replacement recovery protocol and is again **VERIFIED**.

The page was freshly rendered at high resolution and retranscribed source-first before comparison with the repository record. A second enlarged pass checked every visible line, punctuation mark, suffix, separator and the continuation into scan 146.

The recovery pass independently confirmed all source-backed corrections listed above and found one additional discrepancy that had survived the reopening stage:

- `கண்ணுக்குள் பாவைபோல் இலங்கைத் தீவு.` → **`கண்ணுக்குள் பாவை போல் இலங்கைத் தீவு.`**

The page record now explicitly documents:

- comma in `உருவில் சிங்கம், உள்ளம் தங்கம்!`;
- absence of an inserted dash in `மாடுகளை, ஆடுகளை மனிதர்களை`;
- semicolon in `காப்பதற்கு;`;
- exclamation mark in `அவனுக்கு அவள்!`;
- one visible `★` separator;
- closing continuation `கடவுளுக்குப் பலிதேடும் வேலை, ஆகாது`.

This recovered verification applies **only to scan 145**. Scans 146–150 remain reopened until they undergo the same blank-buffer procedure.

## Source-range correction

The earlier source-completeness reasoning relied on an incorrect Kalaignar Karuvoolam description/page-range note. The user has explicitly corrected the work range to **145–152** and supplied the two missing terminal page images.

Therefore the Karuvoolam description must not be used to determine this poem's boundaries. See `../SOURCE_COMPLETENESS_REVIEW.md` for the corrected completeness record.

## Exact next activity

Redo **scan 146 from scratch**, ignoring the current transcription while reading. Only after the fresh transcription is independently compared with every visible glyph may scan 146 be marked `verified` again. Then repeat the same process sequentially for 147–152.