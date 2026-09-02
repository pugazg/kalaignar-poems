# Source metadata — கலைஞரின் கவிதைகள்

## Identity

- source filename: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`;
- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`;
- printed title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

## Renderer warning

An older page renderer exposed only pages 1–150 and reported `total_pages: 150`. Exact-byte inspection establishes **465 physical pages**; the renderer count is not source-file length.

## Current archival state

- Phase 1: **465/465 COMPLETE**;
- Phase 2 source coverage: **465/465 COMPLETE**;
- Phase 2 clearance: **C01–C19 COMPLETE**;
- final statuses: **465 verified / 0 needs-review / 0 partial**;
- Phase 3 Gate 1 pagination reconciliation: **COMPLETE / PASS**;
- Gate 2 boundary/page-join audit: **NEXT**.

## Printed-page numbering behaviour

Gate 1 establishes one continuous pagination model:

1. physical scan **1** — front cover, no logical page number;
2. scans **2–17** — front matter, logical Roman **I–XVI** (`scan_page - 1`); some title/opening scans suppress the printed Roman numeral;
3. scans **18–464** — book body, logical Arabic **1–447** (`scan_page - 17`); poem/title opening pages may suppress the printed numeral without interrupting the sequence;
4. scan **465** — back cover, no logical page number.

Visible-source anchor checks include scan 5 = IV, scan 17 = XVI, scan 21 = 4, scan 117 = 100, scan 217 = 200, scan 317 = 300, scan 416 = 399, scan 419 = 402, scan 452 = 435 and scan 464 = 447.

The `printed_page` field in page records remains strictly source-visible. A logically reconciled but suppressed number must not be inserted into that field or into body text. Logical pagination is recorded in `PHASE3_STRUCTURE_AUDIT.md` and `indexes/page-map.md`.
