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

Source intake: **COMPLETE**.  
Phase 1: **COMPLETE — 101/101**.  
Phase 2: **COMPLETE / PASS — 101/101 independently verified**, unresolved readings **0**.

Phase 3: **IN PROGRESS**.

- Gate 1 — physical scan ↔ printed-page reconciliation: **COMPLETE / PASS**;
- Gate 2 — boundary / page-join audit: **COMPLETE / PASS**;
- Gate 3 — title-witness reconciliation: **COMPLETE / PASS**;
- Gate 4 — canonical Tamil assembly: **COMPLETE / PASS**.

### Gate 4 durable assembly

`PHASE3_CANONICAL_ASSEMBLY.md` is authoritative for the assembly milestone.

- canonical title: **`ஒருதலைக் காதல்`**, primary authority scan 2 title page;
- canonical files: `poems/oruthalaik-kathal/sections/01.md` … `11.md`;
- main-work scans **6–100 = 95/95** represented exactly once with `<!-- scan_page: N -->` provenance;
- text-bearing main-work scans: **84**;
- illustration scans: **11**, provenance-only with no invented lexical text;
- scans **1–5** front matter and scan **101** back cover excluded from poem body;
- verified page-layer changes in Gate 4: **0**;
- unresolved Gate-4 assembly discrepancies: **0**.

Historical source locks remain authoritative, including scan 2 `600 0017` vs scan 3 `600 017`, scan 52 `பீத்து கொண்டு`, and scan 57 `நாற்புறங்களில்` / `அலைகடலின் கொந்தளிப்பை`.

Phase 4 remains blocked until Tamil final clearance.

## Preserved completed work — கலைஞரின் கவிதைகள்

`poems/kalaignarin-kavithaigal/` remains **RELEASE-CLEARED** and must not be modified merely because `ஒருதலைக் காதல்` is active.

## Mandatory continuation startup

Read `POEM_PROCESSING_GUIDE.md`, `TRANSCRIPTION_PHASE_PLAN.md`, root `README.md`, this `HANDOVER.md`, root `NEXT_CHAT_PROMPT.md`, then the active work's `README.md`, `SOURCE_INTAKE.md`, `metadata/source.md`, `indexes/page-map.md`, `audit.md`, all four Phase-3 gate records, work `HANDOVER.md`, work `NEXT_CHAT_PROMPT.md`, canonical `sections/` files and verified page records relevant to the review.

## EXACT NEXT ACTIVITY

**Phase 3 Gate 5 — assembly/source-completeness review.** Independently verify the canonical section files against the verified page records, Gate-1 pagination, Gate-2 joins and Gate-3 title authority. Confirm every required main-work scan occurs exactly once, all lexical content matches, illustration/front-matter/back-cover exclusions are correct, and no silent normalization occurred. Do not grant Tamil final clearance or begin translation/release/Digital Library work in the same activity.
