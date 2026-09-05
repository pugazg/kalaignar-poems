# Phase 3 Structure Audit — Gate 1

Work: **கலைஞரின் கவியரங்கக் கவிதைகள் (1975) — new-item-only Kalaignar intake**  
Controlling source: `TVA_BOK_0064169_கலைஞரின்_கவியரங்கக்_கவிதைகள்.pdf`

- physical PDF scans: **84**;
- file size: **93,307,011 bytes**;
- SHA-256: `d9b70fd65f913c2c4377c25675e115555987bb9d9a4c22681b13ebae98afd168`.

## Gate 1 scope

This record performs **Phase 3 Gate 1 only: physical scan ↔ printed/logical page reconciliation** for the user-directed new-item production interval.

The structural interval examined here is physical scans **46–68**:

- scans **46–57** — NEW ITEM 01 / Kalaignar;
- scans **58–65** — NEW ITEM 02 / Kalaignar;
- scan **66** — Rajaji `சாராய சுதந்திரம்`, retained only as non-Kalaignar source/context;
- scans **67–68** — NEW ITEM 04 / Kalaignar response poem.

Already represented Kalaignar ranges elsewhere in the anthology remain outside this new-item-only gate and are not reopened.

This gate does **not** alter verified lexical text, perform boundary/page-join certification, choose canonical titles, assemble canonical Tamil, or begin translation.

## Result

**PASS — the complete scans 46–68 interval reconciles to one continuous publication-page sequence 46–68 with no gap, reset or insertion.**

Within this interval the structural invariant is:

`reconciled logical publication page = physical scan_page`

The invariant is supported by the visible numbered runs on scans **47–57**, **59–65**, and **68**. The unnumbered scans sit exactly at the missing positions in the same continuous sequence.

## Complete Gate-1 accounting

| Physical scan(s) | Source role | Reconciled logical publication page(s) | Visible printed numeral policy |
|---:|---|---:|---|
| 46 | NEW ITEM 01 opening | **46** | numeral suppressed / not visibly printed |
| 47–57 | NEW ITEM 01 continuation/conclusion | **47–57** | numerals **47–57** visibly printed |
| 58 | NEW ITEM 02 opening | **58** | numeral suppressed / not visibly printed |
| 59–65 | NEW ITEM 02 continuation/conclusion | **59–65** | numerals **59–65** visibly printed |
| 66 | Rajaji source/context insert | **66** | numeral suppressed / not visibly printed |
| 67 | NEW ITEM 04 opening | **67** | numeral suppressed / not visibly printed |
| 68 | NEW ITEM 04 conclusion | **68** | numeral **68** visibly printed |

These rows partition physical scans **46–68** completely, with no overlap and no gap.

## New-Kalaignar item reconciliation

### NEW ITEM 01 — scans 46–57

- reconciled logical publication pages: **46–57**;
- scan 46 is the item opening and has no visible numeral;
- scans 47–57 visibly print **47–57**;
- no pagination break occurs inside the item.

### NEW ITEM 02 — scans 58–65

- reconciled logical publication pages: **58–65**;
- scan 58 is the item opening and has no visible numeral;
- scans 59–65 visibly print **59–65**;
- no pagination break occurs inside the item.

### Scan 66 — non-Kalaignar context

Scan 66 is structurally reconciled as logical publication page **66** because it lies between visibly numbered page 65 and the scan-67/68 response block, with scan 68 visibly numbered 68. Its `printed_page` remains `null` because no numeral is visibly printed.

This structural reconciliation does **not** change its attribution, lexical status or canonical exclusion: scan 66 remains a Rajaji source/context insert and is not Kalaignar canonical material.

### NEW ITEM 04 — scans 67–68

- reconciled logical publication pages: **67–68**;
- scan 67 is the response-poem opening and has no visible numeral;
- scan 68 visibly prints **68**;
- the pair forms one continuous two-page publication sequence.

## `printed_page` field policy

The page records preserve only **source-visible numerals**:

- `printed_page: null` remains correct on scans **46, 58, 66, 67**;
- visible numerical values remain on scans **47–57, 59–65, 68**.

Reconciled logical pagination is structural metadata and must **not** be backfilled into `printed_page` where the source suppresses the numeral.

## Gate 1 closure

- physical scans in Gate-1 interval accounted: **23/23** (46–68);
- active new-Kalaignar scans accounted: **22/22**;
- non-Kalaignar contextual scan accounted: **1/1** (scan 66);
- reconciled logical sequence: **46–68**;
- visibly numbered pages in the interval: **19/23**;
- suppressed/unprinted numerals in the interval: **4/23** — scans **46, 58, 66, 67**;
- visibly numbered active Kalaignar pages: **19/22**;
- suppressed active Kalaignar numerals: **3/22** — scans **46, 58, 67**;
- unexplained pagination gaps/resets: **none**;
- page-text changes in this gate: **none**;
- existing release-cleared poem-tree changes: **none**.

**Phase 3 Gate 1 is COMPLETE / PASS.**

## Exact next gate

Proceed to **Phase 3 Gate 2 — boundary / page-join audit only** for NEW ITEM 01 (46–57), NEW ITEM 02 (58–65), and NEW ITEM 04 (67–68), using scan 66 only as contextual separation evidence between Items 02 and 04.

Do not begin title-witness reconciliation, canonical assembly, final clearance or translation in the same activity.