# Audit — கலைஞரின் கவிதைகள்

## Current state

**PHASE 1 COMPLETE — 465/465 records. PHASE 2 SOURCE-COVERAGE PASS COMPLETE — ALL 465 PHYSICAL SCANS HAVE BEEN REREAD. PAGE CLEARANCE REMAINS IN PROGRESS. C01–C12 COMPLETE. C13 NEXT.**

- controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`;
- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: **`19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`**;
- cumulative page status: **0 `partial`, 154 `needs-review`, 311 `verified`**;
- verified pages: **0001–0300, 0310, 0317, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**;
- unresolved backlog: **154 `needs-review` pages**;
- durable contiguous verified boundary: **scans 1–300**;
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
- C12: **276–300**, mixed direct-source + content-anchored `kavi5.md` control as documented below.

## Durable alignment rule — user instruction

The user clarified that page-number labels inside supplied Markdown must **not** be used to place that text. Alignment is determined from **starting body word/paragraph and ending body word/paragraph**.

Operationally:

1. match the first substantive supplied body anchor to the exact source;
2. match the final substantive supplied body anchor;
3. apply supplied lexical control only to that confirmed source interval;
4. ignore internal/claimed Markdown page numbers when they conflict with text anchors;
5. outside the supplied interval, the controlling scan itself remains lexical authority;
6. source scan always controls physical placement, punctuation, quotation structure, headings, speaker/performance-note boundaries, lineation and non-body separation.

## Clearance C12 — COMPLETE

Target physical window: **276–300**.

### Content-anchor integrity check

`kavi5.md` claims `part_012_pages_276-300`, but its body text anchors show its real coverage:

- first substantive body anchor `நடந்திடுவேன் நமது அய்யா, / அண்ணா வழியில்!` matches attached exact-source `part_012` page 18 = physical scan **293**;
- final anchor `அழுக்குருவின் சிரத்தை அறுத்தெறிந்தார்` matches `part_012` page 25 = physical scan **300**.

Therefore the supplied Markdown lexical-control span is **293–300**, not 276–300.

### Scans 276–292 — direct-source closure

The user supplied the exact derivative `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_012_pages_276-300.pdf`, so scans **276–292** were independently reread directly from those page images rather than blocked on absent Markdown text.

Direct-source corrections made during the closure pass:

- scan **280**: first-pass `சேரு` → source-visible `சேறு`;
- scan **284**: both first-pass `குழந்தைகட்டு` → `குழந்தைகட்கு`;
- scan **286**: `குளுரை` → `சூளுரை`;
- scan **287**: `ஆடப் பேச்சரங்கில்` → `மேடைப் பேச்சரங்கில்`; `அழித்தாரம்` → `அழித்தாராம்`;
- scan **288**: `வார்க்குக்குச்` → `வாக்குக்குச்`.

Pre-existing verified scans **285** and **292** remained verified.

### Scans 293–300 — anchored supplied lexical control

These retain the already applied `kavi5.md` supplied wording and source-established structure. Scan **296** remained verified. The previously promoted scans **293, 294, 295, 297, 298, 299, 300** remain verified.

### C12 final result

- physical scans **276–300: 25/25 verified**;
- new promotions in this closure activity: **15** (`276–284`, `286–291`);
- earlier partial C12 promotions: **7**;
- total C12 pages newly promoted across both activities: **22**, with pre-existing verified **285, 292, 296** preserved;
- cumulative moved from the partial state **0 / 169 / 296** to **0 / 154 / 311**;
- durable contiguous verified boundary advanced from **1–275** to **1–300**.

## C13 anchor preflight

Uploaded `kavi6.md` has already been checked by content against attached `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_013_pages_301-325.pdf`:

- opening `அது கண்ட பார்வதி கொதித் தெழுந்து...` = derivative page 1 / scan **301**;
- ending `மாறப்போகும் மனிதன் எடுக்கப் போகும் - ஜென்மம்தானே?..` = derivative page 25 / scan **325**.

Therefore `kavi6.md` has full C13 lexical coverage by text anchors. Pre-verified scans **310** and **317** must be preserved/reconciled.

## Verification safeguards

- live GitHub `main` is authoritative for durable project state;
- exact source identity remains 465 physical pages;
- supplied Markdown position is determined by text anchors, never page-number claims alone;
- missing supplied text is not invented;
- direct controlling scan is authoritative outside a confirmed lexical-control interval;
- Phase 3 remains blocked while Phase 2 clearance is incomplete.

## Exact next activity

Execute **C13 — physical scans 301–325** using attached `part_013_pages_301-325.pdf` and content-anchored `kavi6.md`. Preserve/reconcile verified scans **310** and **317**. Do not begin C14, Phase 3, canonical assembly or translation in the same activity.
