# Phase 3 canonical Tamil assembly — காலப் பேழையும் கவிதைச் சாவியும்

## Status

**IN PROGRESS — 11/58 canonical item files assembled.**

Canonical assembly began only after:

- Phase-3 physical scan ↔ printed-page reconciliation passed;
- the boundary / within-item page-join audit passed for **58/58** items;
- title-witness reconciliation passed for all **14/14** documented discrepancy cases.

The verified `pages/NNNN.md` records are the assembly text layer. No OCR, outside text or semantic normalization is introduced during assembly.

## Assembly rules

1. Assemble items in the certified contents sequence **1–58**.
2. Derive body text only from the verified physical-page records assigned to that item.
3. Preserve verified spelling, punctuation, lineation, quotation structure, separators, notes and unusual source forms.
4. Preserve physical-page provenance with `<!-- scan_page: N -->` markers.
5. Use the item-opening **title-page witness** as the assembled displayed title.
6. For discrepant titles, retain the contents witness separately in front matter; do not create a hybrid title.
7. Preserve item 37's printed title-page number `36` as a source anomaly while keeping stable sequence identity **37**.
8. Canonical item filenames use stable numeric sequence names (`01.md` … `58.md`) so filesystem naming does not alter or normalize title text.
9. Work proceeds in **25-physical-scan iterations**. If an iteration stops inside an item, do not publish an incomplete canonical item file; carry that item forward until its certified range is complete.
10. Assembly/source-completeness review remains a later gate. Phase 4 translation remains blocked until Tamil final clearance.

## Iteration 1 — physical scans 10–34

**Status: COMPLETE — 25 physical scans.**

This range aligns exactly with complete items **1–6**, so no partial item is carried forward.

| Item | Canonical title | Physical scans | Printed pages | Canonical file | Result |
|---:|---|---:|---:|---|---|
| 1 | `பொது உலகம்` | 10–11 | 9–10 | `sections/01.md` | ASSEMBLED |
| 2 | `படிமுறை வளர்ச்சி` | 12–15 | 11–14 | `sections/02.md` | ASSEMBLED |
| 3 | `‘காந்தக்கல்’ கதையொன்று!` | 16–19 | 15–18 | `sections/03.md` | ASSEMBLED |
| 4 | `அன்றிருந்த கற்காலம் - இனி அமையாவிடின் நற்காலம்!` | 20–24 | 19–23 | `sections/04.md` | ASSEMBLED |
| 5 | `தங்க மனம் வேண்டும்; அது தந்திடும் அன்பு வேண்டும்!` | 25–28 | 24–27 | `sections/05.md` | ASSEMBLED |
| 6 | `கத்தி பகைவுடையது; இரத்தம் நாம் தருவது!` | 29–34 | 28–33 | `sections/06.md` | ASSEMBLED |

### Iteration-1 result

- physical scans processed for assembly: **25/25 — scans 10–34**;
- canonical item files created: **6**;
- cumulative canonical files: **6/58**;
- title-witness discrepancy cases encountered: **none**;
- Tamil source text normalized or rewritten: **none**;
- verified page records modified: **none**;
- partial canonical item files created: **none**;
- unresolved assembly issue: **none**.

Source-sensitive forms remain exactly as verified, including `பத்தரை`, `உளியொன்றை`, `மாளிகை யொன்றை`, `என்னோ டென்றேன்.`, `அணியாத தேன் ?`, `வாய்ப்பை யெனக்`, `பேத்தி, பேர் காலத்திலும்`, `ஏழைபாழையிடம்` and `எனந்தப்`. The source-level abrupt transition between scans **31→32** in item 6 is preserved without an editorial bridge.

## Iteration 2 — physical scans 35–59

**Status: COMPLETE — 25 physical scans.**

Complete certified items **7–11** were assembled. Item 12 begins at scan **58** and continues through scan **63**, so scans **58–59** were carried forward and no partial `sections/12.md` was created.

| Item | Canonical title | Physical scans | Printed pages | Canonical file | Result |
|---:|---|---:|---:|---|---|
| 7 | `வரலாற்றுக் காலத்தின் கோலம்!` | 35–39 | 34–38 | `sections/07.md` | ASSEMBLED |
| 8 | `நெற்றி வியர்வை உதிர; நெஞ்செலும்பு ஒடிய!` | 40–43 | 39–42 | `sections/08.md` | ASSEMBLED |
| 9 | `உரையாடல் உணர்த்திடும் உண்மை என்ன?` | 44–49 | 43–48 | `sections/09.md` | ASSEMBLED |
| 10 | `பழந்தமிழர் பன்னாட்டுத் தொடர்பு!` | 50–53 | 49–52 | `sections/10.md` | ASSEMBLED |
| 11 | `ஆங்காங்கு அடையாள முத்திரைகள்!` | 54–57 | 53–56 | `sections/11.md` | ASSEMBLED |
| 12 | `வரலாற்றுப் பூங்காவில் வள்ளித் திருமணம்!` | 58–63 | 57–62 | — | CARRIED FORWARD; scans 58–59 fall in this iteration but the item is incomplete at scan 59 |

### Iteration-2 result

- physical scans processed for assembly iteration: **25/25 — scans 35–59**;
- canonical item files newly created: **5** (`sections/07.md` through `sections/11.md`);
- cumulative canonical files: **11/58**;
- item carried forward: **12 — scans 58–63**;
- title-witness discrepancy cases encountered among completed items: **none**;
- Tamil source text normalized or rewritten: **none**;
- verified page records modified: **none**;
- partial canonical item files created: **none**;
- unresolved assembly issue: **none**.

Source-sensitive verified forms in this iteration were preserved exactly, including `மனிதக் கனம்`, `கால்நடைப்`, `இத்தினையையும்`, `சளித்தோமா`, `மாக்கலத்தில்`, `மனத்துணிவுடைய`, `அக்குழந்தை`, the classical quotation in scan 54, and the scan-57 line break `பன` / `நுங்கு`.

## Exact next activity

Process the next **25 physical scans: 60–84** as canonical-assembly iteration 3, while completing the carried item 12 from its full certified range **58–63**.

Create only the complete certified item files available at that boundary:

- item 12 — scans **58–63** → `sections/12.md`;
- item 13 — scans **64–67** → `sections/13.md`;
- item 14 — scans **68–77** → `sections/14.md`;
- item 15 — scans **78–81** → `sections/15.md`.

Item 16 begins at scan **82** and continues through scan **87**. Because iteration 3 ends at scan 84, **do not create a partial `sections/16.md`**. Carry item 16 forward until its complete certified range is available in the following iteration.

Do not begin assembly/source-completeness review until all **58/58** canonical item files exist. Do not begin Phase 4 translation before Tamil final clearance.
