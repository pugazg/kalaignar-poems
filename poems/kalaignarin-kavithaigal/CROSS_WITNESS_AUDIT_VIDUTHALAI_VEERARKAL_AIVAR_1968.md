# Cross-Witness Audit — விடுதலை வீரர்கள் / விடுதலை வீரர்கள் ஐவர் (1968)

Status: **COMPLETE — PASS / SAME CANONICAL WORK, ALTERNATE SOURCE WITNESS**

Repository checkpoint reviewed before this audit: `ced98990dce8ce8ee0cc3b63ea32d66fbeeea3cd`.

This is a **post-release source-witness audit** for `கலைஞரின் கவிதைகள்`, Item 06 — `விடுதலை வீரர்கள்`. It does not replace the controlling 1995 anthology witness and does not silently reconcile one edition into another.

## 1. Existing canonical / controlling witness

Workspace: `poems/kalaignarin-kavithaigal/`.

Controlling publication:

`TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

- fourth edition: **March 1995**;
- physical PDF pages: **465**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`;
- Item 06 canonical file: `sections/06.md`;
- Item 06 canonical blob at audit start: `61aa91e7aa3ff17f556c4a42d8d04967f25d9d3f`;
- Item 06 controlling-source scans: **72–79**;
- represented printed pages: **55–62**;
- Tamil layer: **FINAL-CLEARED**;
- English layer: **RELEASE-CLEARED**.

The 1995 canonical witness remains edition-specific source text. This audit does not authorize rewriting it from an earlier edition.

## 2. Newly supplied alternate witness

Source:

`TVA_BOK_0004067_விடுதலை_வீரர்கள்_ஐவர்.pdf`

Exact supplied-file identity:

- physical PDF pages: **78**;
- bytes: **12,691,388**;
- SHA-256: `88bbbd3451752504aa58e124c52be3965187602a98c3e06e1747bb4c918bb1c3`;
- printed publication title: **விடுதலை வீரர்கள் ஐவர்**;
- edition statement: **Ed 1 MAY 1968**;
- publisher: **The South India Saiva Siddhanta Works Publishing Society, Tinnevelly, Limited / திருநெல்வேலித் தென்னிந்திய சைவசித்தாந்த நூற்பதிப்புக் கழகம்**.

The title page states that the poetry event was held at Trichy Radio under Kalaignar M. Karunanidhi's chairmanship on **13-8-67**.

### Kalaignar-bearing pages in this witness

The standalone volume contains five invited poets' long poems plus Kalaignar's chairperson verses. Only the following physical pages carry Kalaignar's own poetic chairperson text:

| Physical PDF page | Printed page | Role |
|---:|---:|---|
| 17–18 | 3–4 | `தலைமையுரை` / opening poem |
| 28 | 14 | chairperson transition after Kattabomman |
| 36 | 22 | chairperson transition to Bharathi |
| 50 | 36 | chairperson transition to V.V.S. Aiyar |
| 60 | 46 | chairperson transition to V.O.C. |
| 75–76 | 61–62 | `தலைவர் முடிவுரை` / closing poem |

The other poets' full poems remain contextual/source material and are **not** imported into Kalaignar's canonical poem body by this audit.

## 3. Identity finding

**PASS — same canonical work / alternate source witness.**

Identity is established by sustained source correspondence, not title alone:

- the same Trichy Radio freedom-fighters poetry-event context;
- the same Kalaignar chairperson role;
- the same opening sequence beginning `இமிழ்கடல் வேலித் தமிழகம் ஈன்ற`;
- the same sequence of five freedom-fighter introductions/transitions;
- the same final `தலைவர் முடிவுரை` argument about preserving hard-won freedom;
- the same closing invocation to Tamil and final `வணக்கம் / வாழ்க`.

The 1968 source is therefore an earlier standalone witness of the work represented as Item 06 in the 1995 anthology. It is **not a new canonical poem**.

## 4. Historical Tamil glyph audit policy

The user-supplied `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` was treated as mandatory method for this comparison.

Guide snapshot used during this audit:

- bytes: **12,598**;
- SHA-256: `99f2568007f4db7e150e44d8d1d38ae25709626df9a3965fe337ede22d35bce4`.

Core rule applied: **decode historical character identity first; encode that identity in modern Unicode; do not modernize source wording.**

All eight Kalaignar-bearing physical pages were inspected from enlarged source pixels. OCR/parser text was used only as a locator and was never lexical authority. On every page the minimum historical-form families were explicitly considered:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`.

### Representative historical-glyph findings

| Physical page | Source-supported reading | Family / issue | Audit result |
|---:|---|---|---|
| 17 | `புதுமைதனைப்` | historical `னை`; parser suggested `புதுமைதளைப்` | **pixels support `னை`** |
| 17 | `தலைவர் நானும்` | difficult final cluster; parser suggested `நானாம்` | **same-edition comparison with p.75 `நானும்` supports `நானும்`** |
| 18 | `கயத்தாறுத்` | `றா` | **decoded, no modernization** |
| 28 | `மணமானார்`; `நன்றாய்` | `னா`; `றா` | **decoded** |
| 36 | `களைத்தவர்க்கும்` | `ளை` | **decoded** |
| 50 | `போலன்றோ` | `றோ` | **decoded** |
| 60 | `மனைவியே` | `னை` | **decoded** |
| 75 | `தளையறுத்த`; `தளையகற்றிப்` | `ளை` | **decoded** |
| 76 | `நன்றோ`; `கற்றார்`; `சிற்றாள்` | `றோ`; `றா` | **decoded** |

This historical-glyph pass is important because several raw parser readings are wrong even where the source is legible. None of the material edition differences listed below disappears when the old typeforms are decoded correctly.

## 5. Material cross-witness differences

The following are preserved as **source-witness variants**, not silently reconciled corrections.

| Area | 1968 standalone witness | 1995 anthology Item 06 witness | Classification |
|---|---|---|---|
| event date | `13-8-67` on the 1968 title page | `15.8.67` in the 1995 Item-06 contextual heading | bibliographic/date conflict — unresolved between witnesses |
| opening wording | `விடுதலை வேண்டா எனும் உபதேசம்` | `விடுதலை வேண்டாம் எனும் வெறும் உபதேசம்` | lexical expansion/variant |
| opening close | `வந்துளர் தாங்கள், தலைவர் நானும்` | `வந்துளர் தாய்கள்: தலைவன் நானாம்!` | **substantive lexical variant** |
| Kattabomman introduction close | `அத்தலத்து வரலாற்றை / அழகு திருச் சிற்றம்பலம் / தருகின்றார், அள்ளி உண்போம்.` | `அத்தலத்து வரலாற்றைத் தருகின்றார் / அள்ளி உண்போம்.` | 1968 contains explicit `அழகு திருச் சிற்றம்பலம்` line absent from the later witness |
| Kattabomman transition | `கொடுத்து விட்டப் புலிமக்கள்`; `அம்புபோல்வேகம் காட்டி` | `கொடுத்து விட்ட புலிமக்கள்`; `அம்புபோல் வேகம் காட்டித்` | sandhi/spacing/source-form variants |
| Bharathi introduction | `முருகு சுந்தரக்`; `பழையநடை`; `கனிந்தபடி`; `சுளைத்தமிழால்`; `சுப்பிரமணிய` | `முருகுசுந்தரக்`; `பழைய நடை`; `கனிந்தபடித்`; `சுளைத் தமிழால்`; `சுப்ரமண்ய` | orthographic/spacing plus lexical-name-form variants |
| V.V.S. Aiyar transition | after `அன்றொரு நாள் மாய்ந்து விட்டார்`, the 1968 witness proceeds directly to `சுவர் எழுப்பிச்...` | later witness additionally contains `இன்றொரு கவிஞர் / அவர் எழுப்ப வந்துவிட்டார்.` | **later-witness two-line addition** |
| Abdul Rahman name form | `அப்துல் ரகுமானின்` | `அப்துர் ரகுமானின்` | name-form witness variant |
| V.O.C. transition structure | `இளஞ்செழியக் கவி நண்பர் ...` appears before the quoted `திருவும் புகழும்...` block | later witness places the Ilanchezhiyan introduction after that block | structural/order variant within the chairperson transition |
| V.O.C. quoted line | `பின்னுறப் பாதியைப் பெரிய நம் இதயத்தில்` | `பின்னுறப் பாதியை பெரிய நம் தேயத்தின்` | **substantive lexical variant** |
| final poem — rose image | `முட்கள் கீறிடப் பறித்த நல்ரோசா` | `முட்கள் கீறிடப் பறித்த நல் ரோஜா` | spelling/lexical witness variant; not normalized |
| final poem — recipient image | `குட்டம் கொண்டோன் குறுகிய கையில் / கொடுத்திடல் நலமா?` | `அதனைத் / துட்டக் குரங்கின் குறுகிய கையில் / கொடுத்திடல் நலமா?` | **substantive rewritten image** |
| final poem — policy line | `சந்தத் தமிழ் ஒலிப்போம் இன்று` | `சந்தத் தமிழில் ஒலிப்போம் இன்று.` | lexical/grammatical witness variant |
| final close | `வணக்கம்! / வாழ்க!!` | `வணக்கம்! / வாழ்க!` | punctuation witness variant |

There are also many smaller punctuation, ellipsis, spacing and line-break differences throughout the eight Kalaignar pages. Those are edition-specific source states and are not globally normalized in this audit.

## 6. Historical-glyph vs. genuine variant decision

The old-glyph review was performed **before** classifying the above differences.

Examples:

- `புதுமைதனைப்` is **not** treated as a 1968 lexical difference merely because the parser produced `புதுமைதளைப்`; the historical `னை` identity is source-supported and agrees with the later witness.
- `தளையறுத்த` / `தளையகற்றிப்` are retained with `ளை`; a modern visual resemblance is not allowed to turn them into different words.
- `நல்ரோசா` vs `நல் ரோஜா`, `குட்டம் கொண்டோன்` vs `துட்டக் குரங்கின்`, `இதயத்தில்` vs `தேயத்தின்`, and `தாங்கள், தலைவர் நானும்` vs `தாய்கள்: தலைவன் நானாம்` remain genuine cross-witness differences after glyph decoding; they are **not** historical-glyph look-alike artifacts.

## 7. Canonical / release decision

**NO REOPEN. NO CANONICAL TEXT CHANGE.**

Reason:

The repository's canonical Item 06 is explicitly the verified/final-cleared witness of the controlling **1995 fourth edition**. An earlier 1968 witness can establish an alternate reading, but it does not by itself prove that the 1995 scan was transcribed incorrectly. Replacing 1995 wording with 1968 wording would violate source-witness separation.

Therefore this audit changes:

- verified 1995 page records: **0**;
- `sections/06.md`: **0**;
- any other Tamil canonical item: **0**;
- English translation files: **0**;
- release report / release-cleared text: **0**.

The 1995 Tamil and English layers remain **FINAL-CLEARED / RELEASE-CLEARED for their controlling source**.

## 8. Durable witness relationship

Record the relationship as:

**`விடுதலை வீரர்கள்` (1995 anthology Item 06) ← same canonical work / alternate earlier witness → `விடுதலை வீரர்கள் ஐவர்` (1968 standalone volume, Kalaignar chairperson portions).**

The 1968 source should be preserved as a distinct source witness if it is later onboarded in full. A future critical-edition or parallel-witness activity may transcribe its eight Kalaignar pages into a dedicated witness layer, but must not overwrite the current 1995 canonical source layer.

## Audit result

**PASS — alternate witness identified, material variants documented, historical Tamil glyph pass completed, and no source-layer contamination introduced.**
