# Audit — ஒருதலைக் காதல்

## Current status

**SOURCE INTAKE COMPLETE / PHASE 1 COMPLETE / PHASE 2 COMPLETE / PASS / PHASE 3 IN PROGRESS — GATES 1–2 COMPLETE / PASS**

- physical scans: **101/101 accounted**;
- page-record files: **101/101**;
- verified: **101**;
- partial: **0**;
- not-started: **0**;
- needs-review: **0**;
- blocked: **0**.

## Phase 2 closure

**PASS — 101/101 physical scans independently verified; 0 unresolved readings; 0 partial pages.**

Source-backed Phase-2 corrections and locked readings remain authoritative, including:

- scan 2 title-page postcode `600 0017` while scan 3 prints `600 017`;
- scan 52 high-resolution lock `பீத்து கொண்டு`;
- scan 57 high-resolution locks `நாற்புறங்களில்` and `அலைகடலின் கொந்தளிப்பை`;
- all eleven illustration scans remain verified visual-only records;
- scan 100 verifies `(முற்றும்)` and the three-diamond close;
- scan 101 verifies the back-cover role and `திருமகள் / நிலையம்`.

The detailed Batch-01 through Batch-04 source-backed corrections remain in the verified page records and prior repository history; Phase 3 does not reopen them without contradictory source evidence.

## Phase 3 Gate 1 — physical scan ↔ printed-page reconciliation

**COMPLETE / PASS.** Full findings are recorded in `PHASE3_STRUCTURE_AUDIT.md` and `indexes/page-map.md`.

- physical scans **1–101** completely partitioned with no overlap/gap;
- scan 1: unpaginated front cover;
- scans **2–5**: logical Roman **I–IV**, supported by source-visible `95 + IV`; individual Roman numerals are not printed, so `printed_page: null` is preserved;
- scans **6–100**: logical Arabic **1–95**, invariant `logical_page = scan_page - 5`;
- section-opening scans **6, 14, 21, 31, 39, 46, 56, 64, 74, 83, 93** suppress the numeral;
- illustration scans **8, 16, 22, 32, 40, 48, 58, 66, 76, 84, 94** suppress the numeral;
- deliberately suppressed Arabic numerals: **22/95**;
- visibly numbered Arabic pages: **73/95**;
- scan 100 = logical/printed page **95** and closes with `(முற்றும்)` plus the three-diamond ornament;
- scan 101: unpaginated verified back cover;
- unexplained pagination gaps/resets: **0**;
- verified page-text changes in Gate 1: **0**.

## Phase 3 Gate 2 — boundary / page-join audit

**COMPLETE / PASS.** Full findings are recorded in `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

### Coverage

- physical adjacent joins: **100/100 accounted**;
- missing physical pages: **0**;
- duplicated physical pages: **0**;
- source-order reordering: **0**;
- unresolved join/boundary questions: **0**;
- verified page-text changes in Gate 2: **0**.

### Numbered-section boundaries

Sections 1–10 close before the next numbered opening at transitions **13→14, 20→21, 30→31, 38→39, 45→46, 55→56, 63→64, 73→74, 82→83, 92→93**. Their closing three-diamond ornaments are preserved. Scan 100 closes section 11 and the whole main work with `(முற்றும்)` and three diamonds before back-cover scan 101.

### Illustration interpositions

All eleven illustration sequences are certified in physical source order with no invented lexical text:

**7→8→9, 15→16→17, 21→22→23, 31→32→33, 39→40→41, 47→48→49, 57→58→59, 65→66→67, 75→76→77, 83→84→85, 93→94→95**.

### Special continuation / quotation / glossary joins

Direct source rechecks certify:

- **6→7** introductory-frame continuation (`சற்று` → `ஆழமாய்ச் சென்று…`);
- **43→44** starred quotation carry-over;
- **51→52** numbered quotation carry-over;
- **54→55** Purananuru quotation → attribution / `பொருள் விளக்கம்`;
- **61→62→63** Natrinai quotation → attribution / glossary / section close;
- **68→69** numbered source-sequence carry-over;
- **70→71** numbered item carry-over;
- **81→82** quoted-source item carry-over → later items / `பொருள் விளக்கம்`;
- **87→88** passage continuing across an internal section-10 diamond separator;
- scan **90** three diamonds remain an internal separator, not a section close;
- **91→92** direct sentence continuation (`இந்த` → following page);
- **98→99→100** two cross-page quoted-source continuities leading to final attribution/glossary, `(முற்றும்)` and close.

### Separator rule

The three-diamond groups on scans **13, 20, 30, 38, 45, 55, 63, 73, 82, 92** close sections 1–10. The final group on scan **100** closes the main work. Diamond ornaments occurring inside a numbered section remain internal structural separators unless the numbered-section evidence marks a close.

## Phase 3 remaining gates

- Gate 1 physical scan ↔ printed-page reconciliation: **COMPLETE / PASS**;
- Gate 2 boundary / page-join audit: **COMPLETE / PASS**;
- Gate 3 title-witness reconciliation: **NEXT**;
- Gate 4 canonical Tamil assembly: not started;
- Gate 5 assembly/source-completeness review: not started;
- Gate 6 Tamil final clearance: not started;
- English translation and release: blocked until Tamil final clearance.

## Exact next activity

**Phase 3 Gate 3 — title-witness reconciliation.** Compare all relevant title witnesses, preserve each exactly, and record an assembly-authority decision if variants exist. Never create a hybrid title. Do not begin Gate 4 or later work in the same activity.
