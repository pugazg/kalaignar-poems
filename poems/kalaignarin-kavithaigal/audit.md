# Audit — கலைஞரின் கவிதைகள்

## Source identity

`TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf` — 465 physical pages, 486,369,088 bytes, SHA-256 `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`.

## Page-layer status

- Phase 1: **COMPLETE — 465/465**;
- Phase 2 source coverage: **COMPLETE — 465/465**;
- Phase 2 clearance: **COMPLETE — C01–C19**;
- final page status: **0 partial / 0 needs-review / 465 verified**;
- contiguous verified boundary: **1–465**.

## Phase 3 Gate 1 audit — COMPLETE / PASS

Scope: **physical scan ↔ printed-page reconciliation only**. Scan 1 is the cover; scans 2–17 are logical Roman I–XVI; scans 18–464 are logical Arabic 1–447 (`scan_page - 17`); scan 465 is the back cover. `printed_page` remains a source-visible witness only. Evidence: `PHASE3_STRUCTURE_AUDIT.md`.

## Phase 3 Gate 2 audit — COMPLETE / PASS

Scope: **boundary / page-join certification only**.

- physical scans covered: **465/465**;
- adjacent transitions covered: **464/464**;
- missing/duplicated physical pages: **none**;
- source-order normalization/reordering: **none**.

High-risk joins include 236→237→238→239, 370→371→372→373→374, 397→398→399→400, 424→425→426, 450→451→452→453 and 464→465. Evidence: `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

## Phase 3 Gate 3 audit — COMPLETE / PASS

Scope: **title-witness reconciliation only**.

- contents/group/item title witnesses: **81**;
- exact title-string matches: **51**;
- source-valid variants: **30**;
- unresolved title witnesses: **0**;
- hybrid/normalized title constructions: **none**.

Dedicated divider/title/opening witnesses control canonical titles; contents witnesses remain preserved separately. The contents page-279 locator for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்` remains untouched while the verified opening is scan 293 / printed page 276. Evidence: `PHASE3_TITLE_WITNESS_RECONCILIATION.md`.

## Phase 3 Gate 4 audit — COMPLETE / PASS

Scope: **canonical Tamil assembly only**.

### Final accounting

- eligible page records checked: **465/465 `verified`**;
- canonical poem-body interval: **scans 18–464 = 447 scans**;
- explicit `scan_page` provenance markers: **447/447**;
- marker-only/non-edition-text body scans retained: **6**;
- physical section runs: **83**;
- Gate-3 source-valid variants retained separately in provenance: **30/30**;
- canonical output: `sections/kalaignarin-kavithaigal.md`;
- source map: `indexes/canonical-source-map.md`;
- Gate-4 evidence: `PHASE3_CANONICAL_ASSEMBLY.md`;
- canonical SHA-256: `ee021de215f2dcca176afe31959f07fdd6ed2b1b2926ff6d3cf91c43d986f57d`.

### Conflict handling during Gate 4

The first assembly exposed stale title metadata in six verified records. The affected records were reopened before final regeneration:

- 0406: title authority corrected to `கேட்டுண்டோ?`; source poem line `பாரத வீரா! நீ கேட்டதுண்டோ?` unchanged;
- 0409: title authority corrected to `இன்றுமா கூச்சல்?`; source poem line `இளித்த வாயரே இன்னுமா கூச்சல்?` unchanged;
- 0457–0460: section/title metadata synchronized to `சில நாடுகள் இருக்கின்றன!`; source-facing opening already had the terminal `!`.

Affected joins 405→406→407, 408→409→410 and 456→457→458→459→460→461 were rechecked and remain valid item boundaries/continuations. **Poem-body lexical changes: 0.** All six reopened records remain `verified`.

### Locked Gate-4 invariants

- exact physical order preserved, including 236→237→238→239;
- 370→371→372→373→374 preserved with blank/divider versos;
- Gate-3 divider/opening title authority used;
- contents variants preserved separately in provenance/source-map metadata;
- page-293 canonical start retained for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்!`;
- no partial canonical item emitted;
- no Gate-5 review, Tamil final clearance, translation or release work performed.

### Gate result

**Gate 4 PASS.**

## Next audit gate

**Phase 3 Gate 5 — assembly/source-completeness review only.** Review Gate-4 output/source map against the verified page layer for one-time coverage, exclusions, title authority, physical source-order fidelity, source-note preservation and silent-normalization risk. Tamil final clearance and translation remain blocked until later ordered gates.
