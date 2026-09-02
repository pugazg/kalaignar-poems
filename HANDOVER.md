# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems` — branch `main`.

**Live `main` is authoritative.**

## Active work — கலைஞரின் கவிதைகள்

Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

- physical PDF pages: **465**;
- bytes: **486,369,088**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`;
- title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

The old renderer `total_pages: 150` is only a tooling window and must never override the exact 465-page identity.

## Durable state after Phase 3 Gate 1

- Phase 1: **465/465 COMPLETE**;
- Phase 2 source coverage: **465/465 COMPLETE**;
- Phase 2 clearance: **C01–C19 COMPLETE**;
- page status: **0 partial / 0 needs-review / 465 verified**;
- durable contiguous verified boundary: **1–465**;
- Phase 3 Gate 1 — physical scan ↔ printed-page reconciliation: **COMPLETE / PASS**;
- Phase 3 Gate 2 — boundary/page-join audit: **NEXT**;
- title-witness reconciliation: **NOT STARTED**;
- canonical Tamil assembly: **NOT STARTED**;
- Tamil final clearance: **NOT STARTED**;
- translation: **NOT STARTED**.

## Gate 1 pagination model

The complete physical source is partitioned as follows:

- scan **1** — unpaginated front cover;
- scans **2–17** — logical Roman front matter **I–XVI**, with some numerals intentionally suppressed in print;
- scans **18–464** — logical Arabic pages **1–447**, invariant `logical printed page = scan_page - 17`;
- scan **465** — unpaginated full-colour back cover.

The verified page record field `printed_page` remains a **source-visible numeral witness only**. Gate 1 does not backfill suppressed numerals. Logical pagination is recorded in `poems/kalaignarin-kavithaigal/PHASE3_STRUCTURE_AUDIT.md` and `indexes/page-map.md`.

Representative body witnesses: scan 21 = 4; scan 117 = 100; scan 217 = 200; scan 317 = 300; scan 416 = 399; scan 419 = 402; scan 452 = 435; scan 464 = 447. No reset or unexplained pagination gap was found.

## Supplied-transcription rule remains in force

Do not position supplied Markdown by page numbers written inside it. Match first and last substantive body anchors to the exact source. Supplied text controls lexical words only inside the confirmed interval; the scan controls physical placement, headings, punctuation, quotation structure, lineation, ornaments and non-body separation.

## EXACT NEXT ACTIVITY

Execute **Phase 3 Gate 2 — boundary / page-join audit** only. Read `PHASE3_STRUCTURE_AUDIT.md` first. Certify every item opening, every internal page join, quotation carry-over, separator, continuation line and closing boundary from the verified page layer against the controlling source. Preserve verified page text. Do **not** begin Gate 3, canonical Tamil assembly, Tamil final clearance or translation in the same activity.
