# Phase 3 Canonical Tamil Assembly — Gate 4

Work: **ஒருதலைக் காதல்**  
Controlling source: `TVA_BOK_0065554_ஒருதலைக்_காதல்.pdf`

- physical PDF pages: **101**;
- file size: **200,800,237 bytes**;
- SHA-256: `a9b0ff45820155a4775074f630e791a8304073a90e5e36ab793bdf702ec33184`.

## Gate 4 scope

This record performs **Phase 3 Gate 4 only: canonical Tamil assembly**. The verified page layer and Gates 1–3 remain authoritative. The canonical layer is a provenance-preserving merge of verified main-work page records, not a fresh transcription or normalization pass.

Gate 4 does **not** perform the Gate-5 assembly/source-completeness review, Tamil final clearance, translation, release work or Digital Library integration.

## Result

**PASS — the complete main work has been assembled from verified page records into eleven canonical numbered-section files with explicit physical-scan provenance.**

- canonical title: **`ஒருதலைக் காதல்`**;
- primary title authority: **scan 2 title page**, per Gate 3;
- canonical section files: **11/11**;
- main-work physical scans represented: **95/95 — scans 6–100 exactly once**;
- text-bearing main-work scans: **84**;
- full-page illustration scans represented by provenance-only markers: **11**;
- front matter excluded from poem body: **scans 1–5**;
- back cover excluded from poem body: **scan 101**;
- page-layer changes in Gate 4: **0**;
- unresolved assembly discrepancies: **0**.

## Canonical file map

| Canonical file | Source section | Physical scans | Logical pages | Illustration scan |
|---|---:|---:|---:|---:|
| `sections/01.md` | 1 | 6–13 | 1–8 | 8 |
| `sections/02.md` | 2 | 14–20 | 9–15 | 16 |
| `sections/03.md` | 3 | 21–30 | 16–25 | 22 |
| `sections/04.md` | 4 | 31–38 | 26–33 | 32 |
| `sections/05.md` | 5 | 39–45 | 34–40 | 40 |
| `sections/06.md` | 6 | 46–55 | 41–50 | 48 |
| `sections/07.md` | 7 | 56–63 | 51–58 | 58 |
| `sections/08.md` | 8 | 64–73 | 59–68 | 66 |
| `sections/09.md` | 9 | 74–82 | 69–77 | 76 |
| `sections/10.md` | 10 | 83–92 | 78–87 | 84 |
| `sections/11.md` | 11 | 93–100 | 88–95 | 94 |

These eleven ranges partition scans **6–100** completely with no overlap and no gap.

## Assembly method

1. Every lexical body segment is copied from the corresponding `verified` record under `pages/`.
2. Each physical source page is anchored with `<!-- scan_page: N -->`.
3. The eleven full-page illustrations remain members of the physical source sequence and are represented only by provenance markers plus `<!-- full-page illustration; no lexical body text -->`; no wording is inferred from the artwork.
4. Running heads, page-record audit prose, Phase-2 notes and visible page-number metadata are not duplicated into canonical poem body.
5. Gate-2 cross-page continuations are preserved across scan markers. Page boundaries are not smoothed away and source punctuation is not repaired.
6. Source quotations, attributions, `பொருள் விளக்கம்` blocks, diamond separators and `(முற்றும்)` remain in their verified source positions.
7. Gate-3 title authority is followed: the canonical work title is `ஒருதலைக் காதல்`; the cover line break is not imposed as a lexical variant and no subtitle is invented from publisher descriptive prose.

## Locked source forms carried into assembly

The canonical files preserve the verified lexical decisions rather than silently normalizing them. Representative locks include scan 38 `பரிதாபத்திற்` / `குரியவர்`, scan 52 `பீத்து கொண்டு`, scan 57 `நாற்புறங்களில்` / `அலைகடலின் கொந்தளிப்பை`, scan 77 `கங்கநாட்டுக்` / `உயிரினுஞ்`, scan 78 `நாளவையில்`, scan 85 `தமிழ் எழுதிப்பிழைக்க` / `நினைவூட்டுகின்றேன்`, scan 88 `ஓடிவந்தீர்`, scan 92 `ஊழித்தீயெனப்`, scan 93 `அனிச்சமலர் தேகத்தை` / `காளைகளைச்`, scan 97 `உனைக் கொல்வதுபோல்`, scan 98 `கூர்கொண்ட` / `என் அறியாமை`, and scan 99 `கரும்பாய் முத்தம்`.

## Closing witness

`sections/11.md` preserves scan **100 / logical page 95** through its final attribution and glossary, followed by:

`(முற்றும்)`

and the source-visible three-diamond closure.

Scan 101 remains outside canonical poem body as the verified back cover.

## Gate 4 closure

**Phase 3 Gate 4 is COMPLETE / PASS.**

The verified page layer remains **101/101 verified** and unchanged. Gates 1–3 remain PASS. The canonical Tamil layer is now assembled but is **not yet Tamil-final-cleared**; Gate 5 must independently review assembly/source completeness before Gate 6 can be considered.

## Exact next gate

Proceed to **Phase 3 Gate 5 — assembly/source-completeness review** only. Verify that every required main-work scan occurs exactly once in the canonical files, every lexical block matches its verified page record, illustration/front-matter/back-cover exclusions are correct, provenance markers and Gate-2 joins are intact, and no source text was silently normalized. Do not grant Tamil final clearance, begin translation, release work or Digital Library integration in the same activity.
