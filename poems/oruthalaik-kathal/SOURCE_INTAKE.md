# Source intake — ஒருதலைக் காதல்

## Controlling source

`TVA_BOK_0065554_ஒருதலைக்_காதல்.pdf`

Exact-byte identity:

- physical PDF pages: **101**;
- file size: **200,800,237 bytes**;
- SHA-256: `a9b0ff45820155a4775074f630e791a8304073a90e5e36ab793bdf702ec33184`.

Printed source facts:

- title: **ஒருதலைக் காதல்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **திருமகள் நிலையம்**;
- first edition: **டிசம்பர் 1998**;
- source page-count statement: **95 + IV**;
- price shown: **ரூ.24.00**.

The publisher's `பதிப்புரை` describes the work as an **ஓவியக் கவிதை நாவல்**.

## Intake result

**PASS — source identity and physical structure established.**

- all physical scans accounted: **101/101**;
- page records: **101/101**;
- source PDF committed to repository: **no**.

## Physical / pagination map

Phase 3 Gate 1 reconciles the complete physical source as:

- scan 1: front cover, unpaginated;
- scans 2–5: four front-matter pages, logical Roman **I–IV** (`scan_page - 1`);
- scans 6–100: main sequence, logical Arabic **1–95** (`scan_page - 5`);
- scan 101: back cover, unpaginated.

The source-visible `பக்கங்கள் : 95 + IV` statement on scan 3 supports the four-page Roman front-matter sequence. No individual Roman numeral is visibly printed on scans 2–5, so their page records retain `printed_page: null`.

## Numbered-section boundaries

| Section | Physical scans | Logical pages |
|---:|---:|---:|
| 1 | 6–13 | 1–8 |
| 2 | 14–20 | 9–15 |
| 3 | 21–30 | 16–25 |
| 4 | 31–38 | 26–33 |
| 5 | 39–45 | 34–40 |
| 6 | 46–55 | 41–50 |
| 7 | 56–63 | 51–58 |
| 8 | 64–73 | 59–68 |
| 9 | 74–82 | 69–77 |
| 10 | 83–92 | 78–87 |
| 11 | 93–100 | 88–95 |

## Full-page illustrations

**8, 16, 22, 32, 40, 48, 58, 66, 76, 84, 94**.

Section-opening scans plus illustration scans account for the **22** suppressed Arabic numerals in the main-work sequence. The other **73** main-work pages visibly print their Arabic numeral.

## Closing / back-cover boundary

Scan **100** / logical page **95** closes the work with `(முற்றும்)`. Scan **101** is a pale-yellow back cover with a colour portrait, red horizontal rule, publisher emblem and the source-visible two-line text `திருமகள் / நிலையம்`.

## Phase progression

- Phase 1: **COMPLETE — 101/101 first-pass captured**;
- Phase 2: **COMPLETE / PASS — 101/101 independently verified**;
- statuses: **101 verified / 0 partial / 0 not-started / 0 needs-review**;
- Phase 3 Gate 1: **COMPLETE / PASS**;
- Gate-1 unexplained pagination gaps/resets: **0**;
- Gate-1 page-text changes: **0**;
- Phase 3 Gates 2–6: not started;
- Phase 4: blocked until Tamil final clearance.

Gate-1 details are recorded in `PHASE3_STRUCTURE_AUDIT.md`; the reconciled map is in `indexes/page-map.md`.

## Next activity

**Phase 3 Gate 2 — boundary / page-join audit.**
