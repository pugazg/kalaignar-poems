# Audit — கலைஞரின் கவிதைகள்

## Current state

**PHASE 1 COMPLETE — 465/465 records. PHASE 2 SOURCE-COVERAGE PASS COMPLETE — ALL 465 PHYSICAL SCANS HAVE BEEN REREAD. PAGE CLEARANCE REMAINS IN PROGRESS. C01–C15 COMPLETE. C16 PARTIAL.**

- controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`;
- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: **`19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`**;
- cumulative page status: **0 `partial`, 67 `needs-review`, 398 `verified`**;
- verified pages: **0001–0396, 0447, 0465**;
- unresolved backlog: **67 `needs-review` pages**;
- durable contiguous verified boundary: **scans 1–396**;
- Phase 3 / canonical assembly / English translation: **blocked**.

## Durable alignment rule — user instruction

Page-number labels inside supplied Markdown must **not** be used to position that text. Alignment is determined from **starting body word/paragraph and ending body word/paragraph**. Supplied lexical control is applied only inside the confirmed interval; the scan always controls physical placement, punctuation, quotation structure, headings, lineation and non-body separation.

## Clearance C16 — PARTIAL

Target physical window: **376–400**.

### Content-anchor integrity check

Uploaded `kavi9.md` was matched to `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_016_pages_376-400.pdf`:

- first substantive anchor `கலைத்தாயின் தலைச் செல்வன்!` = derivative page 1 / scan **376**;
- final substantive supplied anchor `அடைகாக்கும் கோழி போல` = derivative page 21 / scan **396**.

The exact-source derivative page 22 / scan **397** continues the same poem. `kavi9.md` has already ended, so the filename's nominal 376–400 range is **not** lexical-span evidence. `kavi10.md` begins with `சுயமரியாதை இயக்கத்தின் பெயரால்; பெரியார்...`, matching part_017 page 1 / physical scan **401**. There is therefore a genuine supplied-control gap for **397–400**.

### Source structure fixed in the current pass

- **376–378** — `கலைத்தாயின் தலைச் செல்வன்!`;
- **379–381** — `உன் நிழலாக அசைகின்றோம்!`;
- **382–383** — `வாழ்க ஜீவா`;
- **384–389** — `மறைந்த மாவீரன்`;
- **390–391** — `என் இனிய நண்பா! ஏன் பிரிந்தாய்?`;
- **392** — `மலர்த் தோட்டம்` divider;
- **393** — divider verso;
- **394–395** — `இன்றைக்கு உன்றன் பிறந்த நாள்`;
- **396–397** — `அவன் பிறந்தநாள் என ஒன்றில்லை!`;
- **398–399** — `அருமருந்தே! அன்புறவு உடன்பிறப்பே!`;
- **400** — `பகுத்தறிவுப் பாண்டியனார்!`, continuing to 401.

### Lexical-control handling

Supplied words were retained through scan 396 rather than silently normalized. Running headers, printed page numerals, ornaments and obvious extraction-only artifacts were excluded from body text. Where line-wrap fragments were visibly one source word, structural joining was recorded without substituting a different lexical reading.

No supplied text was invented for scans 397–400 and `kavi10.md` was not borrowed backward. Scan 397's section title was synchronized to the source-visible title `அவன் பிறந்தநாள் என ஒன்றில்லை!`, while unresolved compact body lines remain explicit.

### C16 result so far

- physical scans **376–396: 21/21 verified**;
- pre-existing verified scans **392, 393** preserved/reconciled;
- newly promoted pages: **19**;
- scans **397–400: 4 needs-review**;
- cumulative moved from **0 / 86 / 379** to **0 / 67 / 398**;
- durable contiguous verified boundary advanced from **1–375** to **1–396**.

## Verification safeguards

- live GitHub `main` is authoritative for durable project state;
- exact source identity remains 465 physical pages;
- supplied Markdown position is determined by text anchors, never page-number claims alone;
- missing supplied text is not invented;
- direct controlling scan is authoritative outside a confirmed lexical-control interval;
- Phase 3 remains blocked while Phase 2 clearance is incomplete.

## Exact next activity

Finish **C16 — physical scans 397–400** by direct controlling-scan lexical verification. Do not begin C17, Phase 3, canonical assembly or translation until these four pages are cleared.
