# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems` — branch `main`.

**Live `main` is authoritative. Fetch it first and preserve newer durable state.**

## Active work — ஒருதலைக் காதல்

Workspace: `poems/oruthalaik-kathal/`

Controlling source: `TVA_BOK_0065554_ஒருதலைக்_காதல்.pdf`

- physical PDF pages: **101**;
- bytes: **200,800,237**;
- SHA-256: `a9b0ff45820155a4775074f630e791a8304073a90e5e36ab793bdf702ec33184`;
- title: **ஒருதலைக் காதல்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **திருமகள் நிலையம்**;
- first edition: **December 1998**;
- source pagination statement: **95 + IV**.

The scan is controlling source; do not silently modernize or reconstruct wording.

## Durable state

Source intake: **COMPLETE — 101/101**.  
Phase 1: **COMPLETE — 101/101**.  
Phase 2: **COMPLETE / PASS — 101/101 independently verified**, unresolved readings **0**.

Phase 3: **COMPLETE / PASS — TAMIL FINAL-CLEARED**.

1. Gate 1 physical scan ↔ printed-page reconciliation — **PASS**;
2. Gate 2 boundary / page-join audit — **PASS**;
3. Gate 3 title-witness reconciliation — **PASS**;
4. Gate 4 canonical Tamil assembly — **PASS**;
5. Gate 5 assembly/source-completeness review — **PASS**;
6. Gate 6 Tamil final clearance — **PASS**.

`poems/oruthalaik-kathal/PHASE3_TAMIL_FINAL_CLEARANCE.md` is the final Phase-3 authority.

### Gate-5 correction retained by final clearance

Physical scan **82 / printed page 77** visibly ends section 9 with `♦     ♦     ♦`. Gate 5 found that the ornament had been omitted from `pages/0082.md` and therefore from `sections/09.md`. Direct controlling-scan recheck restored it in both files.

- lexical wording changes: **0**;
- non-lexical structural correction: **1**;
- 82→83 boundary: revalidated **PASS**;
- Gate-4 section-9 assembly: revalidated **PASS**;
- unresolved assembly/source-completeness discrepancies: **0**.

Final-cleared Tamil state:

- canonical title: **`ஒருதலைக் காதல்`**, scan 2 title-page authority;
- verified page records: **101/101**;
- canonical section files: **11/11**;
- main-work scans **6–100 = 95/95** represented exactly once;
- text-bearing scans: **84**;
- illustration scans: **11**, provenance-only;
- scans **1–5** and **101** excluded from poem body;
- unresolved Tamil/source issues: **0**.

Historical source locks remain authoritative, including scan 2 `600 0017` vs scan 3 `600 017`, scan 52 `பீத்து கொண்டு`, and scan 57 `நாற்புறங்களில்` / `அலைகடலின் கொந்தளிப்பை`.

Phase 4 is now **UNBLOCKED / READY — not started**. The Gate-6 activity created no English translation and did not modify final-cleared Tamil text.

## Preserved completed work — கலைஞரின் கவிதைகள்

`poems/kalaignarin-kavithaigal/` remains **RELEASE-CLEARED** and must not be modified merely because `ஒருதலைக் காதல்` is active.

## EXACT NEXT ACTIVITY

**Phase 4 T0 — English translation setup and source mapping.** Create `poems/oruthalaik-kathal/translations/en/README.md`, `TRANSLATION_PLAN.md` and `SOURCE_MAP.md`; use only the Tamil final-cleared `sections/01.md` … `sections/11.md` as the normal translation source; define complete source-order translation batch boundaries and document the source hierarchy. Do not modify the final-cleared Tamil `pages/` or `sections/` layer.
