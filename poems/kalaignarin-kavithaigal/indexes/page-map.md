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

## Phase 3 Gate 1 — pagination reconciliation COMPLETE / PASS

| Physical scan(s) | Reconciled logical page(s) | Source role |
|---:|---|---|
| 1 | — | front cover |
| 2–17 | Roman I–XVI | front matter; logical Roman page = scan − 1 |
| 18–464 | Arabic 1–447 | book body; logical printed page = scan − 17 |
| 465 | — | back cover |

`printed_page` remains source-visible only; source-suppressed numerals are not backfilled. Full evidence: `PHASE3_STRUCTURE_AUDIT.md`.

## Phase 3 Gate 2 — boundary / page-join audit COMPLETE / PASS

`PHASE3_BOUNDARY_JOIN_AUDIT.md` certifies **464/464** physical adjacent transitions. Preserve exact physical order, including 236→237→238→239 and 370→371→372→373→374.

## Phase 3 Gate 3 — title-witness reconciliation COMPLETE / PASS

`PHASE3_TITLE_WITNESS_RECONCILIATION.md` accounts for **81** title/group witnesses: **51 exact**, **30 source-valid variants**, **0 unresolved**. Dedicated divider/title/opening witnesses control canonical titles; contents variants remain separate provenance witnesses. The contents page-279 locator for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்` remains as printed; canonical mapping starts at scan 293 / printed page 276.

## Phase 3 Gate 4 — canonical Tamil assembly COMPLETE / PASS

Canonical outputs: `../sections/01.md` through `../sections/77.md`.

Canonical provenance map: `canonical-source-map.md`.

Gate-4 evidence: `../PHASE3_CANONICAL_ASSEMBLY.md`.

- indexed poem/items: **77/77**;
- verified body interval accounted: **18–464 = 447/447**;
- canonical item scan coverage: **439/439**;
- pure anthology group-divider/verso scans outside item files: **8/8**;
- explicit item-file `scan_page` markers: **439/439**;
- physical source section runs: **83**;
- Gate-3 title variants retained in provenance: **30/30**;
- canonical item-manifest SHA-256: `69635ca2edc7c5dc0f0ada58881d05e33ba462c7891b095ad3638c4dbf22d310`.

The earlier monolithic canonical file was removed after Gate 4 was reopened for anthology structure. The corrected assembly uses 77 stable numeric item files. The intentional `230–236, 238` / `237, 239–244` interposition is represented without reordering. No verified poem wording or page record changed.

## Phase status

- Phase 3 Gate 1: **COMPLETE / PASS**;
- Gate 2 boundary/page-join audit: **COMPLETE / PASS**;
- Gate 3 title-witness reconciliation: **COMPLETE / PASS**;
- Gate 4 canonical Tamil assembly: **COMPLETE / PASS**;
- Gate 5 assembly/source-completeness review: **NEXT / NOT STARTED**;
- Tamil final clearance / translation: **NOT STARTED**.
