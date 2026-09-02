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

## Phase 3 Gate 2 — boundary / page-join audit COMPLETE

`PHASE3_BOUNDARY_JOIN_AUDIT.md` certifies **464/464** physical adjacent transitions. No missing or duplicated physical page and no verified page-text discrepancy was found. The physical sequence remains authoritative even where item order is intentionally interposed; batch boundaries are not item boundaries.

## Phase 3 Gate 3 — title-witness reconciliation COMPLETE

`PHASE3_TITLE_WITNESS_RECONCILIATION.md` reconciles every contents/group/item title witness on scans 15–17 against verified divider/title/opening witnesses.

- total title/group witnesses: **81**;
- exact title-string matches: **51**;
- source-valid variants: **30**;
- unresolved: **none**;
- verified page-text changes: **none**.

Assembly authority is locked to the dedicated section-divider or item title/opening witness. Contents variants remain separately preserved; no hybrid title is allowed. Contents scan 16's page-279 locator for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்` is preserved as printed, while the verified item opening is scan 293 / printed page 276.

## Phase status

- Phase 3 Gate 1: **COMPLETE / PASS**;
- Gate 2 boundary/page-join audit: **COMPLETE / PASS**;
- Gate 3 title-witness reconciliation: **COMPLETE / PASS**;
- Gate 4 canonical Tamil assembly: **NEXT**;
- Gate 5 assembly/source-completeness review: **NOT STARTED**;
- Tamil final clearance / translation: **NOT STARTED**.
