# Audit — ஒருதலைக் காதல்

## Current status

**SOURCE INTAKE COMPLETE / PHASE 1 COMPLETE / PHASE 2 COMPLETE / PASS / PHASE 3 IN PROGRESS — GATES 1–3 COMPLETE / PASS**

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
- scans **2–5**: logical Roman **I–IV**, while source-visible `printed_page: null` is preserved;
- scans **6–100**: logical Arabic **1–95**, invariant `logical_page = scan_page - 5`;
- section-opening scans and illustration scans account for **22/95** suppressed Arabic numerals;
- visibly numbered Arabic pages: **73/95**;
- scan 100 = logical/printed page **95** and closes with `(முற்றும்)` plus three diamonds;
- scan 101: unpaginated verified back cover;
- unexplained pagination gaps/resets: **0**;
- verified page-text changes in Gate 1: **0**.

## Phase 3 Gate 2 — boundary / page-join audit

**COMPLETE / PASS.** Full findings are recorded in `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

- physical adjacent joins: **100/100 accounted**;
- missing physical pages: **0**;
- duplicated physical pages: **0**;
- source-order reordering: **0**;
- unresolved join/boundary questions: **0**;
- verified page-text changes in Gate 2: **0**;
- all ten numbered-section close/open transitions certified;
- all eleven illustration interpositions certified;
- special continuation / quotation / glossary joins certified, including 6→7, 43→44, 51→52, 54→55, 61→62→63, 68→69, 70→71, 81→82, 87→88, 91→92 and 98→99→100;
- internal diamond separators are not promoted into synthetic section boundaries;
- 100→101 main-work/back-cover boundary certified.

## Phase 3 Gate 3 — title-witness reconciliation

**COMPLETE / PASS.** Full findings are recorded in `PHASE3_TITLE_WITNESS_RECONCILIATION.md`.

### Witnesses

- scan 1 front cover: `ஒருதலைக்` / `காதல்` across two stylized lines;
- scan 2 title page: `ஒருதலைக் காதல்`;
- scan 4 publisher `பதிப்புரை`: repeated `ஒருதலைக் காதல்` references;
- scan 6 section-1 title: `ஒருதலைக் காதல்`;
- scan 7 self-reference: `‘ஒருதலைக் காதல்’`;
- all title-bearing running heads: `ஒருதலைக் காதல்`.

### Decision

- lexical title variants: **0**;
- unresolved title questions: **0**;
- scan-1 line break is layout only and remains preserved in the cover record;
- primary canonical assembly title authority: **scan 2 title page**;
- canonical work title: **`ஒருதலைக் காதல்`**;
- `ஓவியக் கவிதை நாவல்` / `கவிதை நாவல்` is publisher description, not a subtitle;
- no hybrid title or synthetic subtitle is permitted;
- verified page-text changes in Gate 3: **0**.

## Phase 3 remaining gates

- Gate 1 physical scan ↔ printed-page reconciliation: **COMPLETE / PASS**;
- Gate 2 boundary / page-join audit: **COMPLETE / PASS**;
- Gate 3 title-witness reconciliation: **COMPLETE / PASS**;
- Gate 4 canonical Tamil assembly: **NEXT**;
- Gate 5 assembly/source-completeness review: not started;
- Gate 6 Tamil final clearance: not started;
- English translation and release: blocked until Tamil final clearance.

## Exact next activity

**Phase 3 Gate 4 — canonical Tamil assembly.** Assemble only from verified page records under the Gate-1 pagination model, Gate-2 join decisions and Gate-3 title authority. Preserve physical-scan provenance and source forms; keep front matter and back cover outside poem body. Do not begin Gate 5 or later work in the same activity.
