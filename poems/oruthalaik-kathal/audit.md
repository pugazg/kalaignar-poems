# Audit — ஒருதலைக் காதல்

## Current status

**SOURCE INTAKE COMPLETE / PHASE 1 COMPLETE / PHASE 2 COMPLETE / PASS / PHASE 3 COMPLETE / PASS — TAMIL FINAL-CLEARED**

- physical scans: **101/101 accounted**;
- page records: **101/101 verified**;
- partial / not-started / needs-review / blocked: **0 / 0 / 0 / 0**;
- unresolved Tamil/source issues: **0**.

## Phase 2 closure

**PASS — 101/101 independently verified.** Historical source locks remain authoritative, including scan 2 `600 0017` vs scan 3 `600 017`, scan 52 `பீத்து கொண்டு`, scan 57 `நாற்புறங்களில்` / `அலைகடலின் கொந்தளிப்பை`, and all eleven visual-only illustration records.

## Phase 3 Gate summary

- Gate 1 physical scan ↔ printed-page reconciliation: **COMPLETE / PASS**;
- Gate 2 boundary / page-join audit: **COMPLETE / PASS**;
- Gate 3 title-witness reconciliation: **COMPLETE / PASS**;
- Gate 4 canonical Tamil assembly: **COMPLETE / PASS**;
- Gate 5 assembly/source-completeness review: **COMPLETE / PASS**;
- Gate 6 Tamil final clearance: **COMPLETE / PASS**.

### Gate 4 canonical coverage

- canonical files: **11/11**;
- scans **6–100 = 95/95** represented exactly once;
- text-bearing scans: **84**;
- illustration provenance-only scans: **11**;
- scans **1–5** and **101** excluded from poem body.

### Gate 5 source-backed correction

Fresh review found one inconsistency between source/boundary evidence and the verified/canonical layer:

- scan **82 / printed page 77** visibly closes section 9 with `♦     ♦     ♦`;
- Gate 2 had correctly certified that close and the 82→83 boundary;
- `pages/0082.md` had omitted the ornament;
- Gate 4 therefore propagated the omission into `sections/09.md`.

Direct source recheck restored the ornament in both files.

Correction/revalidation result:

- lexical changes: **0**;
- punctuation/lineation changes: **0**;
- structural non-lexical correction: **1**;
- affected page: **82**;
- affected canonical file: `sections/09.md`;
- 82→83 boundary: **PASS**;
- Gate-4 section-9 assembly after correction: **PASS**;
- unresolved Gate-5 discrepancies: **0**.

### Gate 6 final clearance

Gate 6 reconfirmed Gates 1–5 PASS and explicitly reconfirmed the scan-82 correction in both `pages/0082.md` and `sections/09.md`.

Final judgement:

- verified page records: **101/101**;
- canonical section files: **11/11**;
- main-work scan coverage: **95/95 exactly once**;
- missing/duplicate canonical scan markers: **0 / 0**;
- unresolved Tamil/source issues: **0**;
- Tamil source/canonical layer: **FINAL-CLEARED**.

Governing final-clearance record: `PHASE3_TAMIL_FINAL_CLEARANCE.md`.

## Phase 4

**UNBLOCKED / READY — not started.** Gate 6 created no English translation and made no further Tamil text changes.

## Exact next activity

**Phase 4 T0 — English translation setup and source mapping.** Create `translations/en/README.md`, `TRANSLATION_PLAN.md` and `SOURCE_MAP.md`; define source-order translation batch boundaries from the eleven final-cleared canonical sections and lock the translation-source hierarchy. Do not modify final-cleared Tamil `pages/` or `sections/` files.
