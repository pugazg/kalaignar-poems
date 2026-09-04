# HANDOVER — ஒருதலைக் காதல்

Repository: `pugazg/kalaignar-poems`  
Branch: `main`  
Workspace: `poems/oruthalaik-kathal/`

## Controlling source

`TVA_BOK_0065554_ஒருதலைக்_காதல்.pdf`

- 101 physical scans;
- 200,800,237 bytes;
- SHA-256 `a9b0ff45820155a4775074f630e791a8304073a90e5e36ab793bdf702ec33184`;
- first edition, December 1998;
- publisher `திருமகள் நிலையம்`;
- source pagination statement `95 + IV`.

## Durable checkpoint

Source intake: **COMPLETE**.

Phase 1: **COMPLETE — 101/101 first-pass captured**.

Phase 2: **COMPLETE / PASS — 101/101 independently verified**.

- `verified`: **101**;
- `partial`: **0**;
- `not-started`: **0**;
- `needs-review`: **0**;
- unresolved Phase-2 readings: **0**.

Phase 3: **IN PROGRESS**.

### Gate 1 — physical scan ↔ printed-page reconciliation

**COMPLETE / PASS.** See `PHASE3_STRUCTURE_AUDIT.md`.

- scans **1–101** form one complete physical partition with no gap/overlap;
- scan 1 = unpaginated front cover;
- scans **2–5 = logical Roman I–IV**; no individual Roman numeral is source-visible, so page-record `printed_page` remains `null`;
- scans **6–100 = logical Arabic 1–95**, invariant `logical_page = scan_page - 5`;
- section starts **6, 14, 21, 31, 39, 46, 56, 64, 74, 83, 93** and illustrations **8, 16, 22, 32, 40, 48, 58, 66, 76, 84, 94** account for **22** deliberately suppressed Arabic numerals;
- remaining **73/95** main-work pages visibly print their numeral;
- scan 101 = unpaginated verified back cover;
- unexplained pagination gaps/resets: **0**;
- page-text changes in Gate 1: **0**.

The reconciled Roman/Arabic mapping is durable in `indexes/page-map.md`.

Historical Phase-2 lexical/source locks remain authoritative; Gate 1 did not reopen them.

## Phase 3 gate order

1. physical scan ↔ printed-page reconciliation — **COMPLETE / PASS**;
2. boundary / page-join audit — **NEXT**;
3. title-witness reconciliation;
4. canonical Tamil assembly;
5. assembly/source-completeness review;
6. Tamil final clearance.

Do not skip gates. Phase 4 remains blocked until Tamil final clearance.

## Exact next activity

**Phase 3 Gate 2 — boundary / page-join audit.** Certify every section opening, internal page join, quotation/glossary carry-over, illustration boundary, continuation line, separator and closing boundary against the verified page layer and controlling source. Do not begin Gate 3 or later work in the same activity.
