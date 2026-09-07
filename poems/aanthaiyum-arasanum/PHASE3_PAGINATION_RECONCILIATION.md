# Phase 3 Gate 1 — physical scan ↔ printed-page reconciliation — ஆந்தையும் அரசனும்

Date: **2026-09-07**.

Controlling source: `TVA_PRL_0001631_முரசொலி_ பொங்கல் மலர்_ 1965.pdf` — **102 physical pages / 381,558,891 bytes / SHA-256 `523a038dcd391f5cbe48f564d2ecac566fd0065066e05d29fc5b738aa4964819`**.

Active work range: physical scans **18–25**.

## Gate rule

This gate distinguishes three things which must not be conflated:

1. the **physical PDF scan number**;
2. a **directly visible printed page numeral** in the source;
3. a **reconciled logical printed-page number** supported by an external/direct pagination anchor.

A physical scan number is never silently copied into `printed_page`.

## Source inspection result

All eight active scans were inspected for printed pagination after Phase 2 verification.

| Physical scan | Direct printed numeral | Reconciled logical printed page | Durable `printed_page` |
|---:|---|---|---|
| 18 | none visible | not assigned | `null` |
| 19 | none visible | not assigned | `null` |
| 20 | none visible | not assigned | `null` |
| 21 | none visible | not assigned | `null` |
| 22 | none visible | not assigned | `null` |
| 23 | none visible | not assigned | `null` |
| 24 | none visible | not assigned | `null` |
| 25 | none visible | not assigned | `null` |

No source-supported printed-page anchor was established that would justify assigning inferred logical numerals to these eight records. The existing `printed_page: null` values are therefore **confirmed**, not merely left pending.

This finding does **not** assert that the 1965 Pongal Malar as a whole is unpaginated. It records only that scans 18–25 provide no admissible printed-page numeral or anchored logical pagination for this work.

## Physical-range accounting

- scan 17: unrelated prose — neighbour evidence only;
- scans 18–25: `ஆந்தையும் அரசனும்!` — **8/8 accounted**;
- scan 26: unrelated cartoon — neighbour evidence only.

The poem's physical range remains **18–25 inclusive**, with no missing or duplicated physical scan inside the active range.

## Gate result

**PHASE 3 GATE 1 PASS — PHYSICAL RANGE 8/8 ACCOUNTED / PRINTED-PAGE WITNESSES 0/8 / `printed_page` CONFIRMED `null` ON 8/8 / NO UNSUPPORTED LOGICAL PAGINATION ASSIGNED.**

No lexical page text was changed by this gate, and all eight page records remain `verified`.

Exact next activity: **Phase 3 Gate 2 — boundary / page-join audit**. Certify the opening boundary, joins 18→19 through 24→25, separator/quotation/line continuities, and the closing boundary against the controlling source. Do not begin canonical assembly until Gate 2 and the remaining ordered Phase-3 gates pass.
