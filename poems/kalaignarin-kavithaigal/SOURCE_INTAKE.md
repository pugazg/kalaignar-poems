# Source intake — கலைஞரின் கவிதைகள்

## Controlling source

`TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

- physical pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`;
- title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- fourth edition, March 1995.

A renderer previously exposed only 150 pages; this is not the source boundary. Physical `scan_page` numbering is 1–465 against the exact source above.

## Intake / verification state

- Phase 1 transcription: **COMPLETE 465/465**;
- Phase 2 source coverage: **COMPLETE 465/465**;
- Phase 2 page clearance: **COMPLETE C01–C19**;
- final page statuses: **465 verified; 0 needs-review; 0 partial**;
- Phase 3 Gate 1 pagination reconciliation: **COMPLETE / PASS**;
- Phase 3 Gate 2 boundary/page-join audit: **COMPLETE / PASS — 464/464 adjacent joins**;
- Phase 3 Gate 3 title-witness reconciliation: **COMPLETE / PASS — 81 witnesses, 51 exact matches, 30 variants, 0 unresolved**;
- Phase 3 Gate 4 canonical Tamil assembly: **NEXT**.

## Printed-page behaviour established at Gate 1

- scan 1 is an unpaginated front cover;
- scans 2–17 form a sixteen-page Roman front-matter sequence, logical **I–XVI**;
- scans 18–464 form the continuous Arabic body sequence **1–447**, with `logical printed page = scan_page - 17`;
- scan 465 is an unpaginated colour back cover.

The edition intentionally suppresses the numeral on many title/opening pages. Verified page records continue to use `printed_page` only for a numeral visibly present in the source; reconciled logical pagination is structural metadata and is not silently backfilled.

## Boundary / join behaviour established at Gate 2

All physical adjacent transitions are accounted for in `PHASE3_BOUNDARY_JOIN_AUDIT.md`. No missing or duplicated physical page and no page-text discrepancy was found. Source order must be preserved even at the intentionally interposed 236→237→238→239 sequence; blank/show-through versos are not missing text.

## Title-witness behaviour established at Gate 3

`PHASE3_TITLE_WITNESS_RECONCILIATION.md` reconciles every contents/group/item title witness from scans 15–17 against the verified divider/title/opening layer.

- total witnesses: **81**;
- exact title-string matches: **51**;
- source-valid variants: **30**;
- unresolved: **0**.

For later canonical assembly, the dedicated section-divider or item title/opening witness is authoritative; contents wording remains preserved exactly as a separate source witness. No hybrid title may be created. Gate 3 also preserves the contents locator anomaly for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்`: contents page 279 versus verified opening at scan 293 / printed page 276.

## Next phase gate

**Phase 3 Gate 4 — canonical Tamil assembly only**. Gate 5 assembly/source-completeness review, Tamil final clearance and translation remain deferred.
