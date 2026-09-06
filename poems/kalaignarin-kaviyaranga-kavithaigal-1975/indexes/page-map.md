# Physical page map — கலைஞரின் கவியரங்கக் கவிதைகள் (1975)

Physical `scan_page` is 1-indexed against the exact 84-scan supplied PDF. Printed-page values are recorded only when visibly printed. Reconciled logical pagination is structural metadata and is kept separate from `printed_page`.

## Publication classification

| Physical scans | Classification | Production policy |
|---:|---|---|
| 1–8 | publication preliminaries | retained intake records; **no contents page** |
| 9–20 | existing Anna witness | **ALREADY IN REPOSITORY — SKIP** |
| 21–32 | existing Nehru witness | **ALREADY IN REPOSITORY — SKIP** |
| 33–45 | existing `வாழ்வெனும் பாதையில்` witness | **ALREADY IN REPOSITORY — SKIP** |
| 46–57 | **NEW ITEM 01** | **Phase 2 COMPLETE / Gates 1–3 PASS** |
| 58–65 | **NEW ITEM 02** | **Phase 2 COMPLETE / Gates 1–3 PASS** |
| 66 | Rajaji `சாராய சுதந்திரம்` | **NON-KALAIGNAR — source/context only; structural/separation context certified** |
| 67–68 | **NEW ITEM 04 — `“முதல்வர் கலைஞரின் பதில் கவிதை”`** | **Phase 2 COMPLETE / Gates 1–3 PASS** |
| 69–70 | Bharathidasan insert | **NON-KALAIGNAR** |
| 71–77 | existing `விடுதலை வீரர்கள்` witness | **ALREADY IN REPOSITORY — SKIP** |
| 78–84 | existing `தந்தை பெரியார்` witness | **ALREADY IN REPOSITORY — SKIP** |

Inventory: **84/84 scans accounted for**.

## Phase 3 Gate 1 — active interval reconciliation

Gate-1 authority: `../PHASE3_STRUCTURE_AUDIT.md`.

The complete structural interval **46–68** reconciles continuously as publication pages **46–68**:

| Scan(s) | Item/context | Verified production status | Reconciled logical page(s) | Visibly printed numeral(s) |
|---:|---|---|---:|---|
| 46 | Item 01 opening | `verified` | **46** | none visible |
| 47–57 | Item 01 | 11 `verified` | **47–57** | **47–57** |
| 58 | Item 02 opening | `verified` | **58** | none visible |
| 59–65 | Item 02 | 7 `verified` | **59–65** | **59–65** |
| 66 | Rajaji context insert | non-Kalaignar source/context | **66** | none visible |
| 67 | Item 04 opening | `verified` | **67** | none visible |
| 68 | Item 04 conclusion | `verified` | **68** | **68** |

Structural invariant for this interval:

`reconciled logical publication page = physical scan_page`

- Gate-1 interval accounted: **23/23 scans**;
- active Kalaignar scans accounted: **22/22**;
- visibly numbered interval pages: **19/23**;
- suppressed numerals: **46, 58, 66, 67**;
- unexplained gaps/resets: **none**.

`printed_page` stays `null` on scans 46, 58, 66 and 67; logical values are not backfilled as if they were printed witnesses.

## Phase 3 Gate 2 — boundary / page-join audit

Gate-2 authority: `../PHASE3_BOUNDARY_JOIN_AUDIT.md`.

- Item 01 opening / joins / closing: **PASS — 1 opening, 11/11 joins, 1 closing**;
- Item 02 opening / joins / closing: **PASS — 1 opening, 7/7 joins, 1 closing**;
- Item 04 opening / joins / closing: **PASS — 1 opening, 1/1 join, 1 closing**;
- total internal joins: **19/19 certified**;
- scan 66: **contextual separation certified only; non-Kalaignar status unchanged**;
- scan 50 → 51 open-quotation carry-over: **source state certified / no editorial repair**;
- scan 68 colon before horizontal closing rule: **source state certified / no invented continuation**;
- unresolved boundary/join issues: **0**;
- page-text/status changes in Gate 2: **none**.

## Phase 3 Gate 3 — title-witness reconciliation

Gate-3 authority: `../PHASE3_TITLE_WITNESS_RECONCILIATION.md`.

| Item | Physical scans | Canonical title authority for later assembly |
|---:|---:|---|
| 01 | 46–57 | exact scan-46 two-line heading `புரட்சிக் கவிஞர் பாட்டரங்கில்` / `முதல்வர் கலைஞர் தலைமைக் கவிதை` |
| 02 | 58–65 | exact scan-58 three-line heading `பறம்புமலைப் பாரி வள்ளல் விழாக்` / `கவியரங்கில்` / `முதல்வர் கலைஞரின் தலைமைக் கவிதை` |
| 04 | 67–68 | exact scan-67 heading `“முதல்வர் கலைஞரின் பதில் கவிதை”` |

- publication item-level contents witness: **none**;
- scan 66 `மறுப்புக் கவிதை`: **contextual descriptor only**, not Item-04 title authority;
- unresolved title-witness conflicts: **0**;
- Gate-3 verified page-text/status changes: **none**.

## Phase status

**Phase 1: 22/22 COMPLETE. Phase 2: 22/22 VERIFIED — COMPLETE. Phase 3 Gates 1–3: COMPLETE / PASS. Gate 4 NEXT.**

## Exact next activity

Perform **Phase 3 Gate 4 — canonical Tamil assembly only** for Items 01, 02 and 04. Do not begin Gate 5, final clearance or translation in the same activity.
