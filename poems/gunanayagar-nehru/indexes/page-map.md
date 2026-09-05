# Page map — குணநாயகர் நேரு

Controlling source: `TVA_BOK_0065713_குணநாயகர்_நேரு.pdf`  
Physical scans: **10**.

Phase 3 Gates 1–2 are **PASS**. `Visible printed page` records only a numeral actually printed on the scan. `Reconciled logical page` is structural metadata and is never backfilled into page-record `printed_page` fields when the numeral is absent.

| Scan | Visible printed page | Reconciled logical page | Page type | Canonical Tamil scope | Status |
|---:|---:|---:|---|---|---|
| 1 | — | — | cover | excluded | verified |
| 2 | — | 1 | preface / `பதிப்புரை` | excluded | verified |
| 3 | 2 | 2 | poem opening | **included** | verified |
| 4 | 3 | 3 | poem continuation | **included** | verified |
| 5 | 4 | 4 | poem continuation | **included** | verified |
| 6 | 5 | 5 | poem continuation | **included** | verified |
| 7 | 6 | 6 | poem conclusion + performance note | **verse included; performance note excluded** | verified |
| 8 | — | 7 | source translation | excluded | verified |
| 9 | — | 8 | source translation + translator credit + `அரசு அச்சகம்.` | excluded | verified |
| 10 | — | — | photograph/back matter | excluded | verified |

## Gate 1 — pagination

- physical scans: **10/10**;
- numbered interior: **logical pages 1–8 = scans 2–9**;
- visibly printed numerals: **2–6 on scans 3–7**;
- inferred/suppressed values: scan 2 → **1**, scan 8 → **7**, scan 9 → **8**;
- unresolved pagination issues: **0**.

Authority: [`../PHASE3_PAGE_RECONCILIATION.md`](../PHASE3_PAGE_RECONCILIATION.md).

## Gate 2 — canonical-body boundary / joins

- canonical Tamil poem-body source scans: **3–7 = 5/5**;
- joins **3→4, 4→5, 5→6, 6→7**: **PASS 4/4**;
- scan-7 verse close / performance-note separation: **PASS**;
- excluded from canonical Tamil verse: scans **1–2, 8–9, 10**, plus the performance note on scan 7;
- unresolved boundary/join issues: **0**.

Authority: [`../PHASE3_BOUNDARY_JOIN_AUDIT.md`](../PHASE3_BOUNDARY_JOIN_AUDIT.md).

## Next gate

**Phase 3 Gate 3 — title / attribution witness reconciliation only.** Canonical assembly remains deferred.