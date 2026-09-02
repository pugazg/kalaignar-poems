# Page map — கலைஞரின் கவிதைகள்

Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf` — **465 physical scans**.

## Page-layer status

- Phase 1: **465/465 COMPLETE**;
- Phase 2 source coverage: **465/465 COMPLETE**;
- Phase 2 clearance: **C01–C19 COMPLETE**;
- verified pages: **0001–0465**;
- needs-review: **none**;
- partial: **none**;
- contiguous verified boundary: **1–465**.

## Phase 3 Gate 1 — pagination reconciliation COMPLETE

Gate 1 distinguishes source-visible page numerals from reconciled logical pagination. Verified page records are not rewritten to invent suppressed numerals.

| Physical scan(s) | Reconciled logical page(s) | Source role |
|---:|---|---|
| 1 | — | front cover |
| 2–17 | Roman I–XVI | front matter; logical Roman page = scan − 1 |
| 18–464 | Arabic 1–447 | book body; logical printed page = scan − 17 |
| 465 | — | full-colour back cover |

Source-visible anchors prove the continuous body offset: scan 21 = 4, scan 117 = 100, scan 217 = 200, scan 317 = 300, scan 416 = 399, scan 419 = 402, scan 452 = 435, scan 464 = 447.

The source intentionally suppresses numerals on title/opening pages. In those page records `printed_page` remains `null`; the logical number is supplied only by the Gate-1 reconciliation rule above. Full rationale and front-matter witness details are in `PHASE3_STRUCTURE_AUDIT.md`.

## Phase status

- Phase 3 Gate 1: **COMPLETE**;
- Gate 2 boundary/page-join audit: **NEXT**;
- Gate 3 title-witness reconciliation: **NOT STARTED**;
- canonical Tamil assembly: **NOT STARTED**;
- Tamil final clearance / translation: **NOT STARTED**.
