# கலைஞரின் கவிதைகள்

Source-first archival workspace for `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`.

## Exact source identity

- physical PDF pages: **465**;
- bytes: **486,369,088**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`;
- printed title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

The older `total_pages: 150` display is a renderer limit, not source length.

## Current state

- Phase 1: **465/465 COMPLETE**;
- Phase 2 source coverage: **465/465 COMPLETE**;
- Phase 2 clearance: **C01–C19 COMPLETE**;
- status totals: **0 partial / 0 needs-review / 465 verified**;
- verified range: **0001–0465**;
- Phase 3 Gate 1: **COMPLETE / PASS**;
- Phase 3 Gate 2: **COMPLETE / PASS — 464/464 physical adjacent joins**;
- Phase 3 Gate 3: **COMPLETE / PASS — 81 title/group witnesses (51 exact / 30 variants / 0 unresolved)**;
- Phase 3 Gate 4 canonical Tamil assembly: **COMPLETE / PASS**;
- Phase 3 Gate 5 assembly/source-completeness review: **COMPLETE / PASS**;
- Phase 3 Gate 6 Tamil final clearance: **COMPLETE / PASS**;
- Tamil source/canonical layer: **FINAL-CLEARED**;
- Phase 4 English translation/release: **IN PROGRESS — Batches 01–09 reviewed PASS; 35/77 items; 311/439 item scans; Batch 10 NEXT**.

## Gate 1 — physical scan ↔ printed-page reconciliation

`PHASE3_STRUCTURE_AUDIT.md` records scan 1 cover; scans 2–17 logical Roman I–XVI; scans 18–464 logical Arabic 1–447 using `scan_page - 17`; scan 465 back cover. `printed_page` remains source-visible only.

## Gate 2 — boundary / page-join audit

`PHASE3_BOUNDARY_JOIN_AUDIT.md` certifies all **464/464** physical adjacent joins. Preserve the source's deliberately surprising order, especially 236→237→238→239 and 370→371→372→373→374.

## Gate 3 — title-witness reconciliation

`PHASE3_TITLE_WITNESS_RECONCILIATION.md` locks canonical-title authority to the dedicated divider/title/opening witness. Contents variants remain preserved separately; no hybrid title is allowed. The contents page-279 locator for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்` remains as printed; canonical provenance begins at scan 293 / printed page 276.

## Gate 4 — canonical Tamil assembly

**COMPLETE / PASS — corrected anthology item model.**

- indexed poem/items: **77/77**;
- canonical outputs: `sections/01.md` through `sections/77.md`;
- source map: `indexes/canonical-source-map.md`;
- audit: `PHASE3_CANONICAL_ASSEMBLY.md`;
- verified body interval accounted: **18–464 = 447/447 scans**;
- canonical item scan coverage: **439/439**;
- pure anthology group-divider/verso scans outside poem files: **8/8**, separately accounted;
- explicit item-file scan provenance: **439/439**;
- physical source section runs retained: **83**;
- Gate-3 variants preserved separately: **30/30**;
- canonical item-manifest SHA-256: `74f7bbd84edb1d13dec6d775f854a793929ef530b0c78897cc205004ba78972f`.

The earlier single whole-volume file was a structural assembly error for an anthology and has been removed. Gate 4 now follows the repository's multi-item convention: one stable numeric file per indexed poem/item. The intentional `அண்ணன் ஒரு கவியரங்கம்` / `தமிழ் வளர வழிநடைப் பயணம்` interposition is represented as non-contiguous scan ranges rather than reordered source pages.

The earlier Gate-4 source-backed title corrections at scans **406, 409, 457–460** remain valid. This structural correction changed **0** verified poem words and modified **0** page records.

## Gate 5 — assembly/source-completeness review

**COMPLETE / PASS.** Evidence: `PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical item inventory: **77/77 PASS**;
- verified body scan accounting: **447/447 PASS**;
- item-assigned source scans: **439/439 PASS**;
- structural group scans: **8/8 PASS**;
- canonical payload equality against the verified page layer: **77/77 PASS**;
- item title witnesses: **48 exact / 29 authorized variants**;
- pure group title witnesses: **3 exact / 1 authorized variant**;
- unresolved source-completeness defects: **0**;
- verified page records modified during Gate 5: **0**;
- canonical item files modified during Gate 5: **0**.

## Gate 6 — Tamil final clearance

**COMPLETE / PASS — Tamil source/canonical layer FINAL-CLEARED.** Evidence: `PHASE3_TAMIL_FINAL_CLEARANCE.md`.

No page record, canonical item or English translation was changed during Gate 6. Phase 4 is now unblocked.

## Phase 4 — English translation

**IN PROGRESS — Batches 01–08 reviewed PASS.**

- translation root: `translations/en/`;
- reviewed batches: **8**;
- reviewed items: **30/77**;
- reviewed item-assigned scans: **271/439**;
- Batch 04: items 6–10 across scans **72–127**, **56/56 PASS**;
- title decisions in Batch 04: **4 exact / 1 authorised variant**;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` / `sections/` changes: **0**.

## Next activity

**Phase 4 Batch 09 — items 31–35**, scans **293–332 = 40/40**. Preserve the title-witness variants for items 31–33 and review all five complete final-cleared items before advancing.
