# Audit — இதயத்தைத் தந்திடு அண்ணா

## Source

- Source file: `TVA_BOK_0064132_இதயத்தைத்_தந்திடு_அண்ணா.pdf`
- SHA-256: `152cfb251a2049662102a2296487220f6f227f243657c9456df34105520676fe`
- Total scan pages: **28**
- Poem-body range currently mapped: **13–26** (**14 scans**)
- Source PDF committed: **No**

## Current physical-page status

| Status | Count |
|---|---:|
| verified | 12 |
| partial | 0 |
| needs-review | 0 |
| blocked | 0 |
| not-started | 16 |
| **total** | **28** |

Verified page records:

- scans 1–4 — cover / advertisement / photograph / portrait front matter
- scans 5–10 — complete `என்னுரை` by குறிஞ்சி சுப்பிரமணியன், printed pages 3–8
- scan 11 — rotated captioned photograph, dated 8.11.1960 in the printed caption
- scan 12 — rotated captioned photograph, dated 15.8.1975 in the printed caption

Front matter **scans 1–12 is closed at page-record level**.

## Current poem-body status

| Status | Count |
|---|---:|
| verified | 0 |
| partial | 0 |
| needs-review | 0 |
| blocked | 0 |
| not-started | 14 |
| **total poem scans** | **14** |

Poem transcription has **not yet begun**. The first poem scan is scan **13** / printed page **11**.

## Source-faithful observations from scans 5–12

### Scan 5 → scan 6 quotation

The final paragraph on scan 5 opens the quotation beginning `“சாகித்திய அகாதமி விருது...`; the quotation continues across the physical page boundary and closes on scan 6 with `...தீ வைத்துக் கொளுத்த வேண்டும்”`. Page records keep that source boundary rather than reconstructing a synthetic single page.

### Scan 6 → scan 7 name continuation

Scan 6 ends with the printed fragment `ஆலடி`; scan 7 begins `அருணா...`. The two page records preserve the physical split while documenting that the sentence continues across pages.

### Scan 8 source forms

Forms such as `அய்ஏஎஸ்` and `அப்துல்ரகுமான்` are retained as visibly printed rather than normalized.

### Scan 9 boxed passage

A large bordered passage about Mao, the crowds at Anna's funeral, and the Guinness record appears inside the foreword. It is retained as a distinct printed-text block in `pages/0009.md`; it is not poem text.

### Scan 10 title / sandhi variants

Direct visual review confirms two source forms that must not be silently standardized:

- the prose prints `மொழிபெயர்ப்பு செய்யப்பட்டு`, not an editorialized `மொழிபெயர்ப்புச் செய்யப்பட்டு`;
- the later title occurrence is printed as `“இதயத்தை தந்திடு அண்ணா”`, without the `த்` visible in other occurrences such as `“இதயத்தைத் தந்திடு அண்ணா”`.

Both variants are preserved in the page record.

### Scans 11–12 photograph policy

Both pages were rotated for reading. Only identities/relations explicitly supplied by the printed captions are transcribed; no identity is inferred from facial appearance.

## Corrections / reopened readings

### Scan 3 source description correction

During direct rotation-and-visual inspection of scan 3, the caption was confirmed as referring to **ரூபாய் 3 இலட்சம் பங்குத் தொகையாக** வழங்கியபோது for the **“பெரியார்” திரைப்படக் காவியம்**, dated **22.9.2006**.

An earlier working summary incorrectly described this as presentation of three lakh books. That working description was corrected in `metadata/source.md` before archival closure of scan 3. The page-level transcription reflects the scan.

### Scan 7 verification correction

During the scan-5–12 review pass, the phrase `என் கல்லூரித் தோழர்` was rechecked against the source and the page record was corrected to retain the printed `த்`.

### Scan 10 verification correction

The source was re-opened at high resolution before closure. An initially inserted editorial sandhi in `மொழிபெயர்ப்புச் செய்யப்பட்டு` was removed; the verified page now preserves the source-supported `மொழிபெயர்ப்பு செய்யப்பட்டு`.

## Source-boundary notes

- scans 1–12: front matter / photographs / foreword — **verified**
- scans 13–26: poem body; scan 26 also includes printer imprint — **not started**
- scans 27–28: back matter / back cover — **not started**

No English translation should begin until the Tamil source layer is complete and the assembled poem has passed source comparison.

## Next audit checkpoint

Begin the poem at **scan 13 / printed page 11**. For the poem batch:

1. re-open every scan directly before assigning `verified`;
2. preserve exact poetic lineation, indentation, stanza spacing, quotation marks, dashes and ellipses;
3. do not use OCR or remembered versions as authority;
4. keep the parenthetical contextual note on scan 13 distinct from the poem lines;
5. update poem-body counts after the batch.
