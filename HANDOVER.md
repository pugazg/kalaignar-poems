# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Authority rule

**Treat live GitHub `main` as authoritative.** The controlling source scan is the highest source authority unless a documented user instruction explicitly designates an exact-source word-for-word transcription as lexical control for a stated page range.

## Mandatory startup

Before continuing `கலைஞரின் கவிதைகள்`:

1. fetch live `main` and note current HEAD;
2. read `POEM_PROCESSING_GUIDE.md`, `TRANSCRIPTION_PHASE_PLAN.md`, root `README.md`, `NEXT_CHAT_PROMPT.md`;
3. read `poems/kalaignarin-kavithaigal/README.md`, `SOURCE_INTAKE.md`, `metadata/source.md`, `indexes/page-map.md`, and `audit.md`;
4. inspect the exact target scans against the controlling PDF before writes;
5. synchronize all status-bearing files after the activity.

# CURRENT ACTIVE WORK — கலைஞரின் கவிதைகள்

Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

- physical pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`;
- printed title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

## Durable state

- Phase 1: **465/465 COMPLETE**;
- Phase 2 source coverage: **465/465 COMPLETE**;
- Clearance C01–C05: **COMPLETE**;
- C06: **NEXT**;
- cumulative status: **0 partial / 312 needs-review / 153 verified**;
- verified pages: **0001–0125, 0154, 0174, 0184, 0196, 0204, 0215, 0217, 0226, 0238, 0244, 0253, 0260, 0266, 0272, 0285, 0292, 0296, 0310, 0317, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**;
- durable contiguous verified boundary: **scans 1–125**;
- Phase 3 / translation: **blocked**.

## C04 — COMPLETE

Physical window: **76–100**. The user-designated Gemini word-for-word transcription for this range controls lexical words; the scan controls source structure. All 25 pages are `verified`.

## C05 — COMPLETE

Physical window: **101–125**.

The user supplied a word-for-word transcription explicitly identified as extracted from `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_005_pages_101-125.pdf`. Under the standing instruction to **keep supplied words and not silently correct lexical words**, that transcription is lexical control for scans **101–125**.

For this exact range:

- retain the supplied lexical words;
- use the controlling scan for **physical page placement, paragraph order, punctuation, quotation structure, headings, speaker labels, performance-note boundaries, poetry lineation and spacing**;
- exclude non-body/non-source extraction material such as misplaced running headers/page numbers, library marks, handwriting-derived text and OCR garbage;
- do not substitute scan-derived lexical readings for the supplied words.

All 25 target scans were independently inspected against the controlling PDF and all page records `0101.md`–`0125.md` were reconciled under this rule.

### C05 fixed source structure

- **101–115** — `காதலா - வீரமா?`;
- scan **101** opens with title + `4-8-68` Salem debate context;
- scan **115 / printed 98** closes with `வணக்கம்.` and a centered floral ornament;
- **116–125** — `அருமறையில் அறுவர்`;
- scan **116** opens with title + `10.8.68` Tamil Vattam/Chennai context + centered star;
- scan **117 / printed 100** contains a large printed line illustration below the short verse continuation, with no body-text caption;
- scan **125 / printed 108** remains inside `அருமறையில் அறுவர்`; the item continues beyond the C05 boundary.

### C05 result

- scans **101–125: 25/25 `verified`**;
- promotions: **25**;
- cumulative status advanced from **0 partial / 337 needs-review / 128 verified** to **0 partial / 312 needs-review / 153 verified**;
- contiguous verified boundary advanced from **1–100** to **1–125**.

## Source-critical rule for future ranges

Outside an explicitly designated lexical-control range, correct only what the controlling source supports. Preserve old Tamil forms, punctuation, lineation, quotation boundaries, separators, speaker/performance labels and layout. Never fill blur from grammar, metre, memory, historical context or another edition.

## EXACT NEXT ACTIVITY

Begin **Phase 2 Clearance Batch C06 — physical scans 126–150**.

- inspect/reconfirm source structure for scans 126–150;
- perform page clearance under the applicable source/lexical-control rule;
- promote only complete passes;
- synchronize tracking files after the activity;
- do **not** begin C07, Phase 3, canonical assembly or translation in the same activity.
