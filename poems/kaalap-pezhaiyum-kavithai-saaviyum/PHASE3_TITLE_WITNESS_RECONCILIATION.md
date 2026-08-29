# Phase 3 title-witness reconciliation — காலப் பேழையும் கவிதைச் சாவியும்

## Status

**COMPLETE — all documented contents/title-page differences reconciled as separate source witnesses.**

This record follows completion of the 58-item boundary and page-join audit. It resolves **assembly authority**, not source wording: neither witness is corrected into the other.

## Governing source rule

The controlling scan contains two legitimate title-bearing contexts:

1. the **contents witness**, preserved in `indexes/item-title-map.md`; and
2. the **item-opening title-page witness**, preserved in the verified `pages/NNNN.md` record for the item's first physical scan.

When those two witnesses differ, the repository must preserve **both exactly**.

### Assembly authority decision

For Phase-3 canonical Tamil assembly:

- the **title-page witness controls the assembled item's displayed title** because it is the title printed on the item's own opening page;
- the **title-page witness is also the textual basis for any later title-derived filename**, before purely mechanical filesystem-safe escaping/sanitization;
- the **contents witness remains unchanged** as the contents/index witness and must be retained in metadata or the title-witness record for every discrepant item;
- no hybrid or editorially “corrected” third title may be created;
- stable item identity/order remains the verified **contents sequence 1–58**, not any anomalous printed item number on a title page.

A filesystem-safe transformation may mechanically escape or replace characters that cannot be used in a filename, but such a transformation is **not textual normalization** and must not change spelling, word division, lexical form or source punctuation in the canonical title field.

## Item 37 numbering rule

Contents item **37** begins at physical scan **179**. That title page visibly prints item number **`36`**.

Reconciliation rule:

- canonical sequence identity: **item 37**;
- printed title-page number: **36 — preserved as a source anomaly**;
- do **not** renumber item 37 to 36;
- do **not** shift items 38–58;
- canonical assembled title follows the title-page wording, while the anomalous printed number is recorded separately.

## Reconciled witness register

| Item | Contents start page | Title scan | Contents witness | Title-page witness | Difference class | Phase-3 assembly handling |
|---:|---:|---:|---|---|---|---|
| 18 | 95 | 96 | `தேய்ந்ததுபோக மிச்சத்தைத் தேடுகின்றோம்!` | `தேய்ந்தது போக மிச்சத்தைத் தேடுகின்றோம்!` | word division | Use title-page witness as assembled title; retain contents witness separately. |
| 22 | 111 | 112 | `பிறகேன் வினா? என்பதே என் வினா!` | `“பிறகேன் வினா? என்பதே என் வினா!”` | enclosing quotation marks | Preserve the title-page quotation marks in assembled title; retain unquoted contents witness. |
| 25 | 123 | 124 | `கலாச்சாரத்தின்மீது கண்ணகி காட்டிய அழுத்தம்!` | `கலாச்சாரத்தின்மீது கண்ணகி காட்டிய அழுத்தம்` | final punctuation | Assembled title follows title page without final `!`; contents witness remains unchanged. |
| 26 | 127 | 128 | `விழித்தெழுக; இதோ, செம்மொழி விடியல்!` | `விழித்தெழுக; இதோ செம்மொழி விடியல்!` | comma omission | Assembled title follows title page without the comma after `இதோ`; contents witness remains unchanged. |
| 29 | 139 | 140 | `தாயே, தந்திடு எமக்கு தன்மானச் செல்வங்களை ஈன்று!` | `தாயே தந்திடு எமக்கு தன்மானச் செல்வங்களை ஈன்று!` | comma omission | Assembled title follows title page without the comma after `தாயே`; contents witness remains unchanged. |
| 31 | 147 | 148 | `மாண்பு நிறை தாயும், மாசற்ற மகனும்!` | `மாண்பு நிறை தாயும் மாசற்ற மகனும்!` | comma omission | Assembled title follows title page without the comma after `தாயும்`; contents witness remains unchanged. |
| 32 | 151 | 152 | `கோவூரார் கேள்வியும் குனிந்திடும் தலையும்!` | `கோவூரார் கேள்வியுறும் - குனிந்திடும் தலையுறும்` | substantive wording + punctuation | Treat as two distinct printed witnesses. Use the title-page wording exactly for assembled title; retain contents wording exactly as the contents witness. |
| 37 | 178 | 179 | `அன்பால் அவனை விலை கொள்ள முடியுமா?` | `அன்பால் அவனை விலைகொள்ள முடியுமோ?` | word division + lexical/interrogative form; title page also prints item `36` | Use title-page wording for assembled title. Keep sequence identity as item 37 and separately preserve printed item number `36`. |
| 40 | 194 | 195 | `காஞ்சி மண் காட்டிய கனிவும் கருணையும்!` | `காஞ்சி மண் காட்டிய கனிவும் கருணையும்` | final punctuation | Assembled title follows title page without final `!`; contents witness remains unchanged. |
| 44 | 210 | 211 | `இரும்புத் தூணும், ஈக்களின் இறகும்!` | `இரும்புத் தூணும் ஈக்களின் இறகும்!` | comma omission | Assembled title follows title page without the comma after `தூணும்`; contents witness remains unchanged. |
| 46 | 219 | 220 | `முன்மாதிரியாகத் திகழ்ந்த மும்முடிச் சோழன்` | `முன்மாதிரியாகத் திகழ்ந்த மும்முடிச் சோழன்!` | final punctuation | Assembled title preserves the title page's final `!`; contents witness remains unchanged. |
| 50 | 245 | 246 | `குருதிக் களமே! கொலு மண்டபம் ஆனது!` | `குருதிக்களமே; கொலு மண்டபம் ஆனது!` | word division + punctuation | Use title-page `குருதிக்களமே;` exactly in assembled title; retain contents `குருதிக் களமே!` exactly as its witness. |
| 54 | 270 | 271 | `தலையாலங்கானத்துச் செரு வென்றான்!` | `தலையாலங்கானத்துச் செருவென்றான்!` | word joining | Use joined title-page form `செருவென்றான்!` in assembled title; retain spaced contents witness. |
| 58 | 295 | 296 | `பகை வாள் முனை மருங்க; நாள் எல்லாம் உழைப்போம்` | `பகைவாள் முனை மருங்க; நாள் எல்லாம் உழைப்போம்!` | word joining + final punctuation | Use title-page `பகைவாள்` and final `!` in assembled title; retain contents witness unchanged. |

## Non-discrepant titles

For the other **44/58 items**, the verified contents title and title-page title do not require a witness-specific assembly decision. Canonical assembly still derives the displayed title from the verified item-opening page record, with the contents index retained independently.

## Required canonical-assembly metadata

For every discrepant item, the later assembled item should make the witness distinction durable. At minimum it must retain:

- stable item sequence number;
- title-page title used by the assembled item;
- contents title as the alternate source witness;
- physical title scan;
- printed start page / reconciled range;
- for item 37 only, `printed_item_number: 36` or an equivalent explicit source-anomaly note.

This may be represented in front matter or in a source note, but the distinction must not be lost during filename creation or canonical assembly.

## Reconciliation result

- documented discrepant items reviewed: **14/14**;
- contents witnesses preserved: **14/14**;
- title-page witnesses preserved: **14/14**;
- hybrid/normalized titles created: **none**;
- item-37 printed-number anomaly preserved: **yes**;
- title authority for canonical assembly: **title-page witness**;
- title authority for contents/index representation: **contents witness**;
- unresolved title-witness decisions: **none**.

## Phase-3 gate

The title-witness reconciliation gate is now **PASS**.

Canonical Tamil assembly is therefore **UNBLOCKED**. The next Phase-3 activity is to assemble the **58 separate canonical Tamil item files from verified page records**, preserving verified lineation, page-order joins, source separators/notes, and the title authority rules above.

Do not begin Phase 4 translation until canonical assembly, assembly/source-completeness review, and Tamil final clearance are complete.