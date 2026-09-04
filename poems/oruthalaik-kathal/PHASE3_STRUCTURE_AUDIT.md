# Phase 3 Structure Audit — Gate 1

Work: **ஒருதலைக் காதல்**  
Controlling source: `TVA_BOK_0065554_ஒருதலைக்_காதல்.pdf`

- physical PDF pages: **101**;
- file size: **200,800,237 bytes**;
- SHA-256: `a9b0ff45820155a4775074f630e791a8304073a90e5e36ab793bdf702ec33184`;
- source pagination statement: **95 + IV**.

## Gate 1 scope

This record performs **Phase 3 Gate 1 only: physical scan ↔ printed-page reconciliation**. It does not alter verified lexical text.

## Result

**PASS — all 101 physical scans are accounted for with one continuous front-matter/main-work pagination model and no unexplained reset, insertion or omission.**

## Complete physical-scan accounting

| Physical scan(s) | Source role | Reconciled logical pagination | Rule |
|---:|---|---|---|
| 1 | front cover | none | unpaginated cover |
| 2–5 | front matter | Roman **I–IV** | logical Roman page = `scan_page - 1` |
| 6–100 | main work | Arabic **1–95** | logical main-work page = `scan_page - 5` |
| 101 | back cover | none | unpaginated back cover |

These four rows partition **1–101** completely, with no overlap and no gap.

## Front-matter reconciliation — scans 2–5

Scan 3 visibly prints the bibliographic page-count statement **`95 + IV`**. The four physical front-matter scans between the covers are reconciled structurally as Roman logical pages **I–IV**:

- scan 2 → logical **I** — title page;
- scan 3 → logical **II** — publication / edition details;
- scan 4 → logical **III** — `பதிப்புரை`;
- scan 5 → logical **IV** — photograph / publisher tribute.

No individual Roman page numeral is visibly printed on scans 2–5. Their page-record `printed_page` fields therefore remain `null`.

## Main-work reconciliation — scans 6–100

The main-work sequence begins logically at **page 1 on physical scan 6** and ends at **page 95 on physical scan 100**. The invariant is:

`logical main-work page = physical scan - 5`

Representative verified anchors include scan 7→2, 13→8, 15→10, 30→25, 50→45, 55→50, 65→60, 75→70, 82→77, 85→80, 92→87, 95→90 and 100→95.

No source-visible anchor contradicts the invariant.

## Suppressed main-work numerals

The source deliberately suppresses the Arabic numeral on **22** main-work scans:

- numbered-section openings: **6, 14, 21, 31, 39, 46, 56, 64, 74, 83, 93**;
- full-page illustrations: **8, 16, 22, 32, 40, 48, 58, 66, 76, 84, 94**.

The remaining **73 / 95** main-work pages visibly print their Arabic page numeral.

## `printed_page` field policy

The verified page records remain authoritative for **visible source witnesses**. Reconciled logical pagination is structural metadata and must not be backfilled as source-visible text.

## Closing boundary / back cover

Physical scan **100** is logical main-work page **95**, visibly prints **95**, and closes the work with `(முற்றும்)` plus the verified three-diamond ornament. Physical scan **101** is the verified unpaginated back cover.

## Gate 1 closure

- physical scans accounted: **101/101**;
- verified page records preserved: **101/101**;
- Roman logical sequence: **I–IV** on scans 2–5;
- Arabic logical sequence: **1–95** on scans 6–100;
- visibly numbered Arabic pages: **73/95**;
- deliberately suppressed Arabic numerals: **22/95**;
- unexplained pagination gaps/resets: **none**;
- page-text changes in this gate: **none**.

**Phase 3 Gate 1 is COMPLETE / PASS.**

## Gate progression

Gate 2 is COMPLETE / PASS in `PHASE3_BOUNDARY_JOIN_AUDIT.md`. Gate 3 is COMPLETE / PASS in `PHASE3_TITLE_WITNESS_RECONCILIATION.md`.

## Exact next gate

Proceed to **Phase 3 Gate 4 — canonical Tamil assembly** only. Use this pagination model together with the Gate-2 join decisions and Gate-3 title authority. Do not begin Gate 5, Tamil final clearance or translation in the same activity.
