# Phase 3 Structure Audit — Gate 1

Work: **கலைஞரின் கவிதைகள்**  
Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`.

## Gate 1 scope

This record performs **Phase 3 Gate 1 only: physical scan ↔ printed-page reconciliation**. It does not alter verified lexical text, does not perform page-join certification, and does not begin canonical assembly or translation.

## Result

**PASS — all 465 physical scans are accounted for with one continuous pagination model and no unexplained reset, insertion, or omission.**

## Complete physical-scan accounting

| Physical scan(s) | Source role | Reconciled logical pagination | Rule |
|---:|---|---|---|
| 1 | front cover | none | unpaginated cover |
| 2–17 | front matter | Roman **I–XVI** | logical Roman page = `scan_page - 1` |
| 18–464 | paginated book body | Arabic **1–447** | logical printed page = `scan_page - 17` |
| 465 | back cover | none | unpaginated colour back cover |

These four rows partition **1–465** completely, with no overlap and no gap.

## Front-matter reconciliation — scans 2–17

The front matter occupies sixteen logical Roman pages, **I–XVI**. The source suppresses a printed Roman numeral on some title/opening pages; the logical sequence nevertheless continues without a break.

Direct visual witnesses include **IV** on scan 5, **VI–IX** on scans 7–10, **XI–XII** on scans 12–13, and **XV–XVI** on scans 16–17. Scans **2, 3, 4, 6, 11, 14 and 15** are source pages in the same Roman sequence whose numeral is not visibly printed.

Gate 1 therefore distinguishes:

- **source-visible numeral witness** — what is actually printed on that scan;
- **reconciled logical pagination** — the inferred continuous Roman position I–XVI.

The reconciled Roman number is structural metadata only. It must not be backfilled into a page record as though the numeral were visibly printed.

## Main-body reconciliation — scans 18–464

The Arabic sequence begins logically at **page 1 on physical scan 18** and ends at **page 447 on physical scan 464**. The invariant is:

`logical printed page = physical scan - 17`

Source-visible anchors across the book confirm the invariant, including:

- scan 21 → printed **4**;
- scan 35 → printed **18**;
- scan 117 → printed **100**;
- scan 217 → printed **200**;
- scan 317 → printed **300**;
- scan 416 → printed **399**;
- scan 419 → printed **402**;
- scan 452 → printed **435**;
- scan 464 → printed **447**.

The exact source suppresses the Arabic numeral on many poem/title opening pages and on some other designed pages. Those suppressed numerals are **not source-visible text**. Gate 1 reconciles their logical position from the continuous sequence but does not rewrite the verified page layer to pretend that a number was printed.

Examples at the beginning make the distinction explicit:

- scan 18 = logical page **1**, numeral suppressed;
- scan 19 = logical page **2**, numeral suppressed;
- scan 20 = logical page **3**, numeral suppressed;
- scan 21 = logical page **4**, numeral visibly printed.

The same rule remains continuous through scan 464.

## `printed_page` field policy

The verified page records remain authoritative for **visible source witnesses**. Their existing `printed_page` value means only: a numeral is visibly printed and verified on that scan. A `null` value must remain `null` when the source suppresses the numeral, even when Gate 1 can reconcile the logical page number.

Accordingly:

1. no verified poem wording is changed in Gate 1;
2. no suppressed page number is silently inserted into body text or front matter;
3. logical pagination belongs in this structural audit/page-map layer;
4. future assembly may use the logical mapping for ordering/provenance, but must preserve the visible-vs-reconciled distinction.

## Back cover

Physical scan **465** is the verified full-colour back cover carrying the printed two-line title `கலைஞர் / கவிதைகள்`. It is outside both the Roman and Arabic logical pagination sequences.

## Gate 1 closure

- physical scans accounted: **465/465**;
- verified page records preserved: **465/465**;
- Roman logical sequence: **I–XVI** on scans 2–17;
- Arabic logical sequence: **1–447** on scans 18–464;
- unexplained pagination gaps/resets: **none**;
- page-text changes in this gate: **none**.

**Phase 3 Gate 1 is COMPLETE.**

## Exact next gate

Proceed to **Phase 3 Gate 2 — boundary / page-join audit**. Certify every item opening, internal page join, quotation carry-over, separator, continuation line and closing boundary against the verified page layer and controlling source. Do **not** begin title-witness reconciliation, canonical Tamil assembly, Tamil final clearance or translation in the same activity.
