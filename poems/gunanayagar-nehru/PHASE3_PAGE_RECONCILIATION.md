# Phase 3 Gate 1 — Physical scan ↔ printed/logical page reconciliation

Work: **குணநாயகர் நேரு**  
Controlling source: `TVA_BOK_0065713_குணநாயகர்_நேரு.pdf` — **10 physical scans**, **27,006,676 bytes**, SHA-256 `efc8efb14d45e8cb7cbf2dc232732b7a54e778c1fd1957ad64e198072829e07c`.

## Gate decision

**PASS — all 10 physical scans are accounted and the interior logical sequence is reconciled without rewriting any source-visible `printed_page` value.**

`Visible printed page` means a numeral actually printed on the scan. `Reconciled logical page` is structural metadata established from the continuous physical sequence and must not be copied into page-record `printed_page` fields where the numeral is absent.

| Scan | Visible printed page | Reconciled logical page | Role | Gate-1 basis |
|---:|---:|---:|---|---|
| 1 | — | — | front cover | outside interior pagination |
| 2 | — | 1 | `பதிப்புரை` | immediately precedes visibly printed page 2; numeral is suppressed/not visible |
| 3 | 2 | 2 | Tamil poem opening | visible numeral controls |
| 4 | 3 | 3 | Tamil poem continuation | visible numeral controls |
| 5 | 4 | 4 | Tamil poem continuation | visible numeral controls |
| 6 | 5 | 5 | Tamil poem continuation | visible numeral controls |
| 7 | 6 | 6 | Tamil poem conclusion + performance note | visible numeral controls |
| 8 | — | 7 | printed source English translation, part 1 | continuous interior sequence after page 6; numeral not visible |
| 9 | — | 8 | printed source English translation, part 2 + imprint | continuous interior sequence; numeral not visible |
| 10 | — | — | final photograph / back matter | outside reconciled interior pagination |

## Reconciled publication sequence

- physical scans: **1–10 = 10/10 accounted**;
- interior logical pagination: **1–8 = scans 2–9**;
- source-visible printed numerals: **2–6 only, on scans 3–7**;
- inferred/suppressed logical numerals: **1, 7, 8** on scans **2, 8, 9** respectively;
- covers/back matter outside the reconciled numbered interior: **scans 1 and 10**.

No page-record YAML `printed_page` value is changed by this reconciliation. In particular, scans 2, 8 and 9 retain `printed_page: null` because no numeral is visibly printed there.

## Boundary implication for later gates

Gate 1 concerns pagination only. It does **not** yet certify canonical Tamil body boundaries. The verified working roles remain available for Gate 2:

- scans 1–2: cover/front matter;
- scans 3–7: Tamil poem candidate body;
- scans 8–9: source-printed English translation, outside the Tamil poem body;
- scan 10: photograph/back matter.

Gate 2 must independently certify the poem opening/closing boundary, all Tamil page joins, and the exclusion of front matter, source translation and final back matter before any canonical assembly.

## Gate result

**PHASE 3 GATE 1 — PASS.**  
Unresolved pagination issues: **0**.  
Exact next activity: **Phase 3 Gate 2 — boundary / page-join audit only**.
