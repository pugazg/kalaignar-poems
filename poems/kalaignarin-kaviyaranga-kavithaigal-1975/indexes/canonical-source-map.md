# Canonical source map — கலைஞரின் கவியரங்கக் கவிதைகள் (1975)

Phase 3 Gate 4 canonical outputs for the user-directed new-item-only Kalaignar scope:

- `../sections/01.md` — NEW ITEM 01 — scans **46–57**;
- `../sections/02.md` — NEW ITEM 02 — scans **58–65**;
- `../sections/04.md` — NEW ITEM 04 — scans **67–68**.

The numeric filenames preserve the publication-intake IDs. `sections/03.md` is intentionally absent because intake Item 03 / scan **66** is Rajaji `சாராய சுதந்திரம்`, a non-Kalaignar contextual source unit.

## Assembly accounting

- active Kalaignar canonical items: **3/3**;
- active Kalaignar source scans represented: **22/22**;
- explicit `scan_page` provenance markers: **22/22**;
- source scan ranges: **46–57, 58–65, 67–68**;
- contextual scan excluded from canonical Kalaignar text: **66/66**;
- duplicate/already represented anthology ranges reopened: **0**;
- page-record lexical changes required by assembly: **0**;
- page-status changes required by assembly: **0**.

Canonical `printed_pages` metadata below follows the Gate-1 reconciled logical publication sequence. It does not alter the source-visible `printed_page` fields: scans **46, 58, 66, 67** remain `printed_page: null` in the page layer.

## Canonical item inventory

| Intake item | Canonical title authority | Title scan | Physical scans | Reconciled logical pages | Visible printed numerals | Canonical file |
|---:|---|---:|---:|---:|---|---|
| 01 | exact two-line scan-46 heading: `புரட்சிக் கவிஞர் பாட்டரங்கில்` / `முதல்வர் கலைஞர் தலைமைக் கவிதை` | 46 | 46–57 | 46–57 | 47–57 | `sections/01.md` |
| 02 | exact three-line scan-58 heading: `பறம்புமலைப் பாரி வள்ளல் விழாக்` / `கவியரங்கில்` / `முதல்வர் கலைஞரின் தலைமைக் கவிதை` | 58 | 58–65 | 58–65 | 59–65 | `sections/02.md` |
| 04 | exact scan-67 heading `“முதல்வர் கலைஞரின் பதில் கவிதை”` | 67 | 67–68 | 67–68 | 68 | `sections/04.md` |

## Title / context controls

Gate-3 authority is `../PHASE3_TITLE_WITNESS_RECONCILIATION.md`.

- no item-level contents page exists for these active items;
- event/date/provenance prose remains source text but is not synthesized into the canonical title;
- Item 02 retains source `கவியரங்கில்`; the earlier convenience normalization `கவியரங்கு` is not used;
- scan 66's editorial descriptor `மறுப்புக் கவிதை` is contextual provenance only;
- Item 04 canonical title remains the direct scan-67 witness `“முதல்வர் கலைஞரின் பதில் கவிதை”` with its printed quotation marks;
- no hybrid title is created.

## Boundary / separator controls

Gate-2 authority is `../PHASE3_BOUNDARY_JOIN_AUDIT.md`.

- all **19/19** internal joins are preserved in source order;
- the scan **50 → 51** open-quotation state is left untouched: no editorial quotation mark is inserted at the page boundary;
- closing horizontal rules after scans **57, 65 and 68** are represented by non-lexical `source_separator` comments;
- scan **68** retains terminal `பட்டியல் பிறகு சொல்வேன்:` exactly; no missing list or continuation is invented.

## Canonical file hashes

| File | SHA-256 |
|---|---|
| `sections/01.md` | `1020bafb32b120cd58ca043597102368e026e5f681530a0f665f4086a4916ff2` |
| `sections/02.md` | `ea1e62ec88997c45c753b4e2dc1113ec30f21a939bd198696d32860dbe0cc40b` |
| `sections/04.md` | `4b86a8d12ad3851589fbcdc28dd778f92d472945c4769b110ad9042dc9b44d31` |

Canonical three-file manifest SHA-256: `52d0c105cf8d6b14ae87bee871583d2b47d6aa32dabb3b0f2514633592d667e7`.

## Gate 5 source-completeness review

Authority: `../PHASE3_CANONICAL_SOURCE_REVIEW.md` — **COMPLETE / PASS**.

- canonical items: **3/3 PASS**;
- source scans: **22/22 exactly once**;
- canonical payload equality vs verified page layer: **22/22 PASS**;
- duplicate / omitted / unexpected active scan markers: **0 / 0 / 0**;
- scan 66 canonical occurrences: **0**;
- title/context authority: **3/3 PASS**;
- Gate-2 joins: **19/19 preserved**;
- unresolved source-completeness defects: **0**;
- canonical file changes required by Gate 5: **0**.

Canonical three-file manifest remains `52d0c105cf8d6b14ae87bee871583d2b47d6aa32dabb3b0f2514633592d667e7`.
