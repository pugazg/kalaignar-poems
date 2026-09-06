# Phase 3 Canonical Tamil Assembly — Gate 4

Work: **அண்ணா கவியரங்கம்**  
Controlling source: `TVA_PRL_0001502_முரசொலி_பொங்கல் மலர்_1968.pdf`

- physical PDF pages: **136**;
- file size: **58,026,496 bytes**;
- SHA-256: `5f9cc505038ae1c3f91cbd0b50c0b6692b54baeee40fffef1fcdc8d213a146ce`;
- scoped work range: physical scans **119–124**;
- Gate 1: `PHASE3_STRUCTURE_AUDIT.md` — **COMPLETE / PASS**;
- Gate 2: `PHASE3_BOUNDARY_JOIN_AUDIT.md` — **COMPLETE / PASS**;
- Gate 3: `PHASE3_TITLE_WITNESS_RECONCILIATION.md` — **COMPLETE / PASS**.

## Gate 4 scope

This record performs **Phase 3 Gate 4 only: canonical Tamil assembly**. It creates the canonical Tamil file from the verified page layer after applying the already-certified pagination, reading-order/join and title-witness decisions. It does not perform the Gate-5 assembly/source-completeness review, grant Tamil final clearance or begin translation.

## Canonical output

`sections/anna-kaviyarangam.md`

Assembly inputs are exactly the verified page records:

- `pages/0119.md`
- `pages/0120.md`
- `pages/0121.md`
- `pages/0122.md`
- `pages/0123.md`
- `pages/0124.md`

Physical scan provenance is retained with hidden `scan_page` comments. Scan 119 carries its directly certified printed page **19**; scans 120–124 retain `printed_page: null` provenance and no inferred numerals are introduced.

## Assembly decisions applied

1. **Top-level title:** `அண்ணா கவியரங்கம்`, from the decorated scan-119 title authority certified in Gate 3.
2. **Opening context panel:** retained separately and verbatim from verified scan 119, including the contextual inflection `‘அண்ணா கவியரங்கத்திற்கு’`.
3. **Reading order:** scans 120–124 follow the Gate-2 left-column → right-column order before continuing to the next physical scan.
4. **Physical joins:** the five Gate-2-certified scan joins are represented sequentially without invented bridge text, repeated text or normalization.
5. **Internal handoff headings:** all eight source-visible headings remain verbatim at their verified positions.
6. **`மு. க.` markers:** retained as separate source markers where printed; never merged into headings.
7. **Body/title variants:** source-supported differences remain distinct, including `தலைவராம் அண்ணா` vs `‘தலைவர் அண்ணா’`, and `அன்னையாம் அண்ணா` / `‘அண்ணா அன்னை’` / `அன்னை அண்ணா`.
8. **No modernization:** verified spelling, spacing, punctuation, lineation, historical-glyph resolutions and user manual lexical controls are copied without editorial normalization.

## Provenance / coverage result

- verified source pages consumed: **6/6**;
- canonical scan markers: **6/6 — 119, 120, 121, 122, 123, 124**;
- scan 118 text imported: **0**;
- scan 125 text imported: **0**;
- source-context panel preserved: **1/1**;
- top-level title witnesses used for canonical title: **1/1**;
- internal handoff headings preserved: **8/8**;
- page-record Tamil changes during assembly: **0**;
- hybrid/normalized titles introduced: **0**;
- inferred printed numerals introduced: **0**;
- unresolved assembly decisions: **0**.

**Phase 3 Gate 4 is COMPLETE / PASS.**

The canonical file is an **assembled output awaiting Gate-5 review**. Gate 4 completion is not Tamil final clearance.

## Exact next gate

Proceed with **Phase 3 Gate 5 — assembly/source-completeness review only**. Compare the canonical output against all six verified page records and Gates 1–3, certify that every required source block occurs exactly once with correct provenance/exclusions and no silent normalization, and document any discrepancy before further progression. Do not grant Tamil final clearance or begin translation in the same activity.
