# Phase 3 Gate 1 — Physical scan ↔ printed-page reconciliation — தலைகேட்டான் தம்பி

Date: **2026-09-08**

## Scope

Controlling source: `TVA_PRL_0001662_முரசொலி_பொங்கல் மலர்_1966.pdf` — **75 physical scans / 30,952,719 bytes / SHA-256 pending exact-byte hash**.

Active poem range: physical scans **18–23 = 6 scans**.

Phase-2 prerequisite: **PASS — 6/6 VERIFIED / 0 unresolved**.

## Method

The complete physical scans 18–23 were inspected directly from the same attached 75-page controlling PDF. Printed-page numerals were treated separately from physical PDF scan numbers. A physical scan number was not substituted for a printed page number. Neighbour scans 17 and 24 were also checked only as boundary/context evidence; they do not provide a reliable printed-pagination anchor for the active range.

The exact SHA-256 remains an independent source-identity hold because the available checksum execution facility did not return a hash. No checksum is inferred or invented in this record.

## Reconciliation

| Physical scan | Directly visible printed numeral | Source-supported logical printed page | Durable `printed_page` |
|---:|---|---|---|
| 18 | none | none established | `null` |
| 19 | none | none established | `null` |
| 20 | none | none established | `null` |
| 21 | none | none established | `null` |
| 22 | none | none established | `null` |
| 23 | none | none established | `null` |

No reliable surrounding numeral or other source evidence supports assigning logical printed-page values to this six-scan sequence. Therefore all six existing `printed_page: null` values are **confirmed**, not merely pending placeholders.

## Gate result

**PHASE 3 GATE 1 — PASS.**

- active physical scans accounted for: **6/6**;
- directly visible printed numerals: **0/6**;
- source-supported logical printed-page assignments: **0/6**;
- confirmed `printed_page: null`: **6/6**;
- missing active scans: **0**;
- duplicate active scans: **0**;
- pagination-affecting page-text changes required: **0**;
- unresolved pagination issues: **0**.

## Subsequent structural correction and Gate 2

After Gate 1, scan 18 received a structural-role correction documented in `POST_PHASE2_STRUCTURAL_CORRECTION.md`: trailing `தம்பி` / `கருணாநிதி` was removed from poem body because those source-visible elements are title and author material. This does **not** affect any Gate-1 pagination conclusion.

Phase 3 Gate 2 has subsequently passed under `PHASE3_BOUNDARY_JOIN_AUDIT.md`: opening **1/1 PASS**, internal joins **5/5 PASS**, closing **1/1 PASS**, unresolved boundary issues **0**.

## Remaining provenance hold / current next activity

The exact source **SHA-256 is still pending**. No hash is inferred or invented. Establish and durably record it, then proceed to **Phase 3 Gate 3 — title-witness reconciliation**. Canonical Tamil assembly remains blocked until the ordered title gate passes.
