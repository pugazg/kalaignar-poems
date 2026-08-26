# Audit — காலப் பேழையும் கவிதைச் சாவியும்

## Current totals

- physical scans in controlling PDF: **306**
- scans inspected for identity/opening structure: **10**
- verified page records: **9**
- needs-review page records: **0**
- blocked page records: **0**
- physical scans without verified page records: **297**

Verified records now cover scans **1–9 consecutively**.

## Source controls

- SHA-256 recorded: **PASS**
- file size recorded: **PASS**
- source PDF excluded from repository: **PASS**
- title/author verified from scan: **PASS**
- publication details recorded from visible preliminaries: **PASS**

## Opening-page verification

### Scans 1–4

Direct visual verification was completed for:

1. scan 1 — colour front cover;
2. scan 2 — title page, excluding later library stamp/handwriting from edition text;
3. scan 3 — publication details / price / printer line;
4. scan 4 — introductory note signed `மு. க.`.

The scan-4 source form `நிலைபோட்டி` is preserved exactly as printed and has not been silently normalized by semantic expectation.

### Scans 5–7 — contents review

All three contents pages have now been transcribed and verified directly from the controlling scan:

- scan 5 — items **1–19**;
- scan 6 — items **20–43**, visible printed page `5`;
- scan 7 — items **44–58**, visible printed page `6`.

Result:

- contents items accounted for: **58/58**;
- listed starting-page numbers captured: **58/58**;
- contents page records: **3/3 verified**;
- no OCR wording imported;
- long entries that physically wrap are represented as single logical contents entries without changing wording or punctuation;
- dot leaders are documented as navigation/layout marks, not silently treated as title punctuation.

### Scan-5 printed-page correction

The preliminary page map previously recorded scan 5 as printed page `4` by sequence. Full verification found **no visible printed page number on scan 5**. That inference has been removed and `printed_page` is now unset for scan 5. This correction follows the repository rule that inferred numbering must not be recorded as visibly printed evidence.

### Scan 8 — work display

Scan 8 is now verified as an unnumbered work/display page containing:

- `காலப் பேழையும்,`
- `கவிதைச் சாவியும்`
- author line `- கலைஞர் மு. கருணாநிதி`;
- decorative border motifs above and below the title block;
- no poem/body text.

### Scan 9 anomaly resolution

The earlier unresolved scan-9 role remains **resolved**:

- no independently printed edition text is visible on that side;
- the visible material is faint reverse-side/show-through;
- no printed page number is visibly present;
- scan 9 is recorded as a **blank verso**, with no inferred printed-page number.

## Remaining cautions

1. Later library marks occur in the front matter and must remain excluded from edition text.
2. Contents pagination is navigation evidence and is not a substitute for physical scan mapping.
3. The controlling file is image-only for inspected pages; no OCR output is authoritative.
4. The directly opened controlling PDF contains 306 physical scans. A smaller count reported by an external preview layer is treated as a preview limitation, not as source evidence.
5. Poem/body pages beginning at scan 10 require line-by-line transcription with lineation, punctuation and page joins checked independently of contents wording.

## Assembly readiness

**NOT READY.** Only 9/306 physical scans currently have verified page records.

## Translation readiness

**BLOCKED.** Tamil source layer has not reached final clearance.

## Exact next activity

Complete the first poem/body item, **`பொது உலகம்`**, beginning at scan **10**. Transcribe and verify scan 10 and its continuation on scan 11 line by line, and inspect scan 12 only as the boundary witness needed to confirm that item 1 has ended before item 2 begins. Do not transcribe item 2 in the same activity.