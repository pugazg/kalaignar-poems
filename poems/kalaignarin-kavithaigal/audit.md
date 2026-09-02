# Audit — கலைஞரின் கவிதைகள்

## Current state

**PHASE 1 COMPLETE — 465/465 records. PHASE 2 SOURCE-COVERAGE PASS COMPLETE — ALL 465 PHYSICAL SCANS HAVE BEEN REREAD. PAGE CLEARANCE REMAINS IN PROGRESS. C01–C13 COMPLETE. C14 NEXT.**

- controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`;
- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: **`19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`**;
- cumulative page status: **0 `partial`, 131 `needs-review`, 334 `verified`**;
- verified pages: **0001–0325, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**;
- unresolved backlog: **131 `needs-review` pages**;
- durable contiguous verified boundary: **scans 1–325**;
- Phase 3 / canonical assembly / English translation: **blocked**.

## Completed clearance history

- C01–C03: scans **1–75**;
- C04: **76–100** supplied Gemini lexical control;
- C05: **101–125** supplied lexical control;
- C06: **126–150** supplied lexical control;
- C07: **151–175** supplied lexical control;
- C08: **176–200** `kavi1.md`;
- C09: **201–225** `kavi2.md`;
- C10: **226–250** `kavi3.md`;
- C11: **251–275** `kavi4.md`;
- C12: **276–300**, mixed direct-source + content-anchored `kavi5.md`;
- C13: **301–325**, content-anchored `kavi6.md` + attached exact-source derivative.

## Durable alignment rule — user instruction

Page-number labels inside supplied Markdown must **not** be used to place that text. Alignment is determined from **starting body word/paragraph and ending body word/paragraph**.

Operationally:

1. match the first substantive supplied body anchor to the exact source;
2. match the final substantive supplied body anchor;
3. apply supplied lexical control only to that confirmed source interval;
4. ignore internal/claimed Markdown page numbers as positional authority;
5. outside the supplied interval, the controlling scan itself remains lexical authority;
6. source scan always controls physical placement, punctuation, quotation structure, headings, speaker/performance-note boundaries, lineation and non-body separation.

## Clearance C13 — COMPLETE

Target physical window: **301–325**.

### Content-anchor integrity check

`kavi6.md` is matched to attached exact-source `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_013_pages_301-325.pdf` by body text:

- first substantive anchor `அது கண்ட பார்வதி கொதித் தெழுந்து...` = derivative page 1 / physical scan **301**;
- final anchor `மாறப்போகும் மனிதன் எடுக்கப் போகும் - ஜென்மம்தானே?..` = derivative page 25 / physical scan **325**.

Therefore the supplied lexical-control interval is the complete **301–325** C13 window.

### Source structure

- **301–310** — `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை`; scan 310 closes with a printed ornament;
- **311–317** — `மாறி வரும் ஊரினிலே`; scan 311 opens with title/context/star and scan 317 closes with a decorative lower-page illustration;
- **318–325** — `சமுதாயப் பார்வைகள்...!`; scan 318 opens with title/context/star and scan 325 remains mid-item.

### Supplied lexical control / structure reconciliation

All supplied lexical words were retained within the anchored interval. Representative precedence examples include:

- 301 `ஆனையொன்று`, `செய்யுமளவுக்கு`, `வித்திட்டு`, `சுருட்டும்`;
- 304 `சண்டமாருதங்களையும்`, `கறுப்புப் பணக்காரன்`, `திட்டம் சொன்னார்`, `எதிரிகட்கு`;
- 307 `பூஜைக்கு`, `ஓதிய மிலார்`, `மூக்கணாங் கயிறில்லா`, `எப்படி டைக்கலாம்`;
- 308 `கனற்பிழம்பாய்`;
- 313 `சா வுரலில்`, `உலக்கை`, `ஏணைகளில்`;
- 315 `உழைத்தலுத்த`;
- 316 `ஈர விறகுக் கட்டை`, `நளபாகத்தை`;
- 319 `ஐம்பதாமே`, `வம்புக்குத்`, `நடைபழகி`;
- 321 `கொஞ்சேமா`, `பாலசுப்ரமணியன்`, `இவள்`, `பெற்றவள்`;
- 322 `பயிண்டு`, `அட்டையெனும்`;
- 323 `பாபம்`, `அனாதைப்`, `அராஜகக்`;
- 325 `தான்றியது`.

Source structure corrected extraction placement without changing supplied lexical words where needed. On scan 321, for example, `பெற்றவள்!` and separator placement were restored to the positions visible in the scan. Running headers and printed page numerals were excluded from body text.

### C13 result

- physical scans **301–325: 25/25 verified**;
- pre-existing verified scans **310** and **317** were preserved/reconciled;
- newly promoted pages: **23**;
- cumulative moved from **0 / 154 / 311** to **0 / 131 / 334**;
- durable contiguous verified boundary advanced from **1–300** to **1–325**.

## Verification safeguards

- live GitHub `main` is authoritative for durable project state;
- exact source identity remains 465 physical pages;
- supplied Markdown position is determined by text anchors, never page-number claims alone;
- missing supplied text is not invented;
- direct controlling scan is authoritative outside a confirmed lexical-control interval;
- Phase 3 remains blocked while Phase 2 clearance is incomplete.

## Exact next activity

Execute **C14 — physical scans 326–350**. First align uploaded `kavi7.md` to attached `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_014_pages_326-350.pdf` by first and last substantive body anchors, not Markdown page labels. Preserve/reconcile already verified scans **328** and **332**. Do not begin C15, Phase 3, canonical assembly or translation in the same activity.
