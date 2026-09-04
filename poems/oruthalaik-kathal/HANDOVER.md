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

Historical source locks remain authoritative, including scan 2 `600 0017` vs scan 3 `600 017`, scan 52 `பீத்து கொண்டு`, and scan 57 `நாற்புறங்களில்` / `அலைகடலின் கொந்தளிப்பை`.

Phase 3: **IN PROGRESS**.

### Gate 1

**COMPLETE / PASS.** `PHASE3_STRUCTURE_AUDIT.md` is authoritative. Scans 2–5 reconcile to logical Roman I–IV; scans 6–100 reconcile to logical Arabic 1–95; pagination gaps/resets 0; page-text changes 0.

### Gate 2

**COMPLETE / PASS.** `PHASE3_BOUNDARY_JOIN_AUDIT.md` is authoritative.

- all **100/100** adjacent physical joins accounted;
- all ten numbered-section close/open transitions certified;
- all eleven illustration interpositions certified in physical source order;
- special continuation / quotation / glossary joins rechecked;
- missing/duplicated pages: **0 / 0**;
- unresolved join questions: **0**;
- Gate-2 page-text changes: **0**.

### Gate 3

**COMPLETE / PASS.** `PHASE3_TITLE_WITNESS_RECONCILIATION.md` is authoritative.

- scan 1 cover: `ஒருதலைக்` / `காதல்` across two lines;
- scan 2 title page: `ஒருதலைக் காதல்`;
- scan 4 publisher references: `ஒருதலைக் காதல்`;
- scan 6 main-work title: `ஒருதலைக் காதல்`;
- scan 7 self-reference and all title-running heads: `ஒருதலைக் காதல்`;
- lexical title variants: **0**;
- unresolved title questions: **0**;
- primary assembly title authority: **scan 2 title page**;
- canonical title: **`ஒருதலைக் காதல்`**;
- cover line break is layout only;
- `ஓவியக் கவிதை நாவல்` / `கவிதை நாவல்` is description, not subtitle;
- Gate-3 page-text changes: **0**.

## Phase 3 gate order

1. physical scan ↔ printed-page reconciliation — **COMPLETE / PASS**;
2. boundary / page-join audit — **COMPLETE / PASS**;
3. title-witness reconciliation — **COMPLETE / PASS**;
4. canonical Tamil assembly — **NEXT**;
5. assembly/source-completeness review;
6. Tamil final clearance.

Do not skip gates. Phase 4 remains blocked until Tamil final clearance.

## Exact next activity

**Phase 3 Gate 4 — canonical Tamil assembly.** Assemble the main work from verified scans 6–100 only, preserving verified spelling, punctuation, lineation, quotation/source blocks, separators, section boundaries and physical-scan provenance. Follow the Gate-3 title authority. Keep scans 1–5 and 101 outside poem body. Do not begin Gate 5 or later work in the same activity.
