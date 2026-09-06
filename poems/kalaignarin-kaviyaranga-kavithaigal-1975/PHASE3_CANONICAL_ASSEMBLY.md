# Phase 3 Canonical Tamil Assembly — Gate 4

Work: **கலைஞரின் கவியரங்கக் கவிதைகள் (1975) — new-item-only Kalaignar intake**  
Controlling source: `TVA_BOK_0064169_கலைஞரின்_கவியரங்கக்_கவிதைகள்.pdf`

- physical PDF scans: **84**;
- file size: **93,307,011 bytes**;
- SHA-256: `d9b70fd65f913c2c4377c25675e115555987bb9d9a4c22681b13ebae98afd168`.

Prerequisites:

- `PHASE3_STRUCTURE_AUDIT.md` — **Gate 1 COMPLETE / PASS**;
- `PHASE3_BOUNDARY_JOIN_AUDIT.md` — **Gate 2 COMPLETE / PASS**;
- `PHASE3_TITLE_WITNESS_RECONCILIATION.md` — **Gate 3 COMPLETE / PASS**.

## Gate 4 scope

This record performs **Phase 3 Gate 4 only: canonical Tamil assembly** for the three genuinely new Kalaignar items:

- NEW ITEM 01 — scans **46–57**;
- NEW ITEM 02 — scans **58–65**;
- NEW ITEM 04 — scans **67–68**.

Assembly is a provenance-preserving merge of the already `verified` page records. It does not retranscribe, normalize or repair source text. Gate 5 source/completeness review, Tamil final clearance and translation are not performed here.

## Result

**PASS — 3/3 canonical Kalaignar item files assembled from the 22/22 verified active pages.**

Canonical outputs:

- `sections/01.md` — Item 01 — scans **46–57**;
- `sections/02.md` — Item 02 — scans **58–65**;
- `sections/04.md` — Item 04 — scans **67–68**.

`sections/03.md` is intentionally absent. Intake Item 03 / scan **66** is the non-Kalaignar Rajaji source/context unit `சாராய சுதந்திரம்`; it is excluded from canonical Kalaignar text while remaining preserved in the page layer and Gate-2/Gate-3 provenance records.

## Assembly controls applied

### Verified-page authority

- active Kalaignar page records consumed: **22/22 `verified`**;
- explicit canonical `scan_page` provenance markers: **22/22**;
- physical source order preserved;
- lexical/page-record corrections during Gate 4: **0**;
- page-status changes during Gate 4: **0**.

### Gate-3 title authority

- Item 01 uses the exact scan-46 two-line heading block `புரட்சிக் கவிஞர் பாட்டரங்கில்` / `முதல்வர் கலைஞர் தலைமைக் கவிதை`;
- Item 02 uses the exact scan-58 three-line heading block `பறம்புமலைப் பாரி வள்ளல் விழாக்` / `கவியரங்கில்` / `முதல்வர் கலைஞரின் தலைமைக் கவிதை`;
- Item 04 uses the exact scan-67 direct heading `“முதல்வர் கலைஞரின் பதில் கவிதை”` including its printed quotation marks;
- no item-level contents witness exists for these items;
- event/provenance prose is preserved in source order but not merged into synthetic titles;
- scan 66's contextual `மறுப்புக் கவிதை` descriptor is not substituted for Item 04's direct title.

For Items 01 and 02, the canonical YAML `title` is a block scalar so the source line structure of the controlling heading itself is retained rather than collapsed into a synthetic one-line title.

### Gate-2 joins and separators

- all **19/19** certified internal joins are carried into the canonical files in physical source order;
- scan **50 → 51** remains a source-open quotation across the page boundary; the provenance marker does not insert any editorial quotation punctuation;
- scans **57, 65 and 68** close with source horizontal rules; these non-lexical separators are represented as `<!-- source_separator: horizontal-rule -->` comments after the verified text;
- scan **68** still ends `பட்டியல் பிறகு சொல்வேன்:` before its closing rule; no continuation/list is invented.

## Canonical source map

`indexes/canonical-source-map.md` records the complete Gate-4 mapping, including:

- 3/3 canonical item files;
- 22/22 active Kalaignar scans;
- 22/22 provenance markers;
- intentional absence of Item 03 canonical output;
- title/context controls;
- canonical file hashes.

Canonical three-file manifest SHA-256: `52d0c105cf8d6b14ae87bee871583d2b47d6aa32dabb3b0f2514633592d667e7`.

## Gate 4 closure ledger

- canonical Kalaignar items assembled: **3/3**;
- verified active source pages represented: **22/22**;
- explicit scan provenance markers: **22/22**;
- canonical scan overlap: **0**;
- canonical active-scan omission: **0**;
- non-Kalaignar contextual scan included in canonical output: **0**;
- verified page-text changes: **0**;
- page-status changes: **0**;
- existing release-cleared poem-tree changes: **0**;
- unresolved assembly defects at Gate 4: **0**.

**Phase 3 Gate 4 is COMPLETE / PASS.**

## Subsequent Gate 5 outcome

Phase 3 Gate 5 subsequently completed **PASS**. Durable evidence: `PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical item inventory: **3/3 PASS**;
- active source scan accounting: **22/22 PASS**;
- canonical payload equality against the verified page layer: **22/22 PASS**;
- Gate-3 title/context authority: **3/3 PASS**;
- Gate-2 internal joins preserved: **19/19 PASS**;
- scan 66 canonical inclusion: **0**;
- unresolved source-completeness defects: **0**;
- verified page-record changes during Gate 5: **0**;
- canonical item changes during Gate 5: **0**.

## Exact next gate

Proceed to **Phase 3 Gate 6 — Tamil final clearance only**. Do not begin English translation in the same activity.
