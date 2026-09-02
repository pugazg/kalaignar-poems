# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems` — branch `main`

## Authority rule

**Live GitHub `main` is authoritative.** The controlling scan is source authority for physical/source structure and, outside a confirmed supplied lexical-control interval, for lexical text as well.

An explicitly user-designated exact-source word-for-word transcription controls lexical words only where its body text is actually matched to the source.

### Mandatory content-anchor rule

The user explicitly instructed: **do not position supplied Markdown using page numbers written inside the Markdown. Use the starting word/paragraph and ending word/paragraph.**

Accordingly:

- match first substantive supplied body text to the exact source;
- match final substantive supplied body text;
- the matched interval is the actual lexical-control span;
- embedded/claimed Markdown page numbers are not positional authority;
- outside the matched supplied interval, use the controlling scan directly;
- source-established page/order/lineation structure always remains authoritative.

## Mandatory startup

Before continuing `கலைஞரின் கவிதைகள்`:

1. fetch live `main`;
2. read `POEM_PROCESSING_GUIDE.md`, `TRANSCRIPTION_PHASE_PLAN.md`, root `README.md`, `NEXT_CHAT_PROMPT.md`;
3. read `poems/kalaignarin-kavithaigal/README.md`, `SOURCE_INTAKE.md`, `metadata/source.md`, `indexes/page-map.md`, `audit.md`;
4. inspect the active exact-source derivative and supplied Markdown by first/last body anchors before applying lexical control;
5. synchronize all status-bearing files after the active batch.

# CURRENT ACTIVE WORK — கலைஞரின் கவிதைகள்

Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

- physical pages: **465**;
- bytes: **486,369,088**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`;
- title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

## Durable state after C12

- Phase 1: **465/465 COMPLETE**;
- Phase 2 source coverage: **465/465 COMPLETE**;
- Clearance **C01–C12 COMPLETE**;
- C13: **NEXT**;
- cumulative: **0 partial / 154 needs-review / 311 verified**;
- verified: **0001–0300, 0310, 0317, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**;
- durable contiguous verified boundary: **1–300**;
- Phase 3 / canonical assembly / translation: **blocked**.

## Completed supplied lexical-control ranges

Previous C04–C11 ranges are documented in the audit and phase plan.

C12 required mixed authority after the new content-anchor rule was applied:

- **293–300** — `kavi5.md` lexical control, positioned by body text anchors;
- **276–292** — direct controlling-scan lexical verification from newly attached exact-source `part_012` derivative because `kavi5.md` has no body text covering those scans.

Standing supplied-control rule:

- retain supplied lexical words inside the confirmed anchor span;
- source-established scan structure controls physical placement, order, punctuation, quotations, headings, speaker/performance-note boundaries, lineation and spacing;
- exclude running headers/page numbers, library marks, handwriting-derived material and OCR/extraction garbage;
- never silently substitute scan-derived lexical wording inside a confirmed supplied span;
- never invent a supplied span merely from a Markdown page-number claim.

## C12 — COMPLETE

Physical window: **276–300**.

### Anchor determination

`kavi5.md` opening body text:

`நடந்திடுவேன் நமது அய்யா, / அண்ணா வழியில்!`

This matches attached `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_012_pages_276-300.pdf` page 18 = physical scan **293**.

Its ending body text:

`அழுக்குருவின் சிரத்தை அறுத்தெறிந்தார்`

matches attached derivative page 25 = physical scan **300**.

Therefore `kavi5.md` lexical control is **293–300 only**.

### Direct-source closure for 276–292

The exact source derivative was attached, allowing a complete direct visual pass for scans **276–292**. Source-backed repairs included:

- scan 280 `சேறு`;
- scan 284 `குழந்தைகட்கு` ×2;
- scan 286 `சூளுரை`;
- scan 287 `மேடைப் பேச்சரங்கில்`, `அழித்தாராம்`;
- scan 288 `வாக்குக்குச்`.

Already verified **285** and **292** were preserved. Scans **276–284 and 286–291** were newly promoted = **15**.

### C12 totals

- scans **276–300 = 25/25 verified**;
- earlier partial C12 new promotions = **7**;
- closure new promotions = **15**;
- pre-C12 verified in window = **285, 292, 296**;
- cumulative now **0 / 154 / 311**;
- contiguous boundary **1–300**.

## Remaining uploaded sequence / content-anchor preflight

- `kavi6.md` + `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_013_pages_301-325.pdf` → **C13 NEXT**. Anchor check already passes across the full derivative:
  - start `அது கண்ட பார்வதி கொதித் தெழுந்து...` = scan **301**;
  - end `மாறப்போகும் மனிதன் எடுக்கப் போகும் - ஜென்மம்தானே?..` = scan **325**.
- later `kavi7.md` … `kavi11.md` must each be aligned by first/last body text before use; do not trust their internal page labels alone.

## EXACT NEXT ACTIVITY

Execute **C13 — physical scans 301–325** using attached `part_013_pages_301-325.pdf` plus content-anchored `kavi6.md`. Preserve/reconcile already verified scans **310** and **317**. Promote only complete passes, synchronize all status-bearing files, and **do not begin C14, Phase 3, canonical assembly or translation in the same activity**.
