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
- Clearance C01–C04: **COMPLETE**;
- C05: **NEXT**;
- cumulative status: **0 partial / 337 needs-review / 128 verified**;
- verified pages: **0001–0100, 0154, 0174, 0184, 0196, 0204, 0215, 0217, 0226, 0238, 0244, 0253, 0260, 0266, 0272, 0285, 0292, 0296, 0310, 0317, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**;
- durable contiguous verified boundary: **scans 1–100**;
- Phase 3 / translation: **blocked**.

## C04 — COMPLETE

Physical window: **76–100**.

Source structure:

- **76–79** — `விடுதலை வீரர்கள்`; 79 closes with `வணக்கம்!`, `வாழ்க!`, floral ornament;
- **80–89** — `ஐம்புலன்`; 80 has title + `24.3.68` event note + star; 89 closes with `வணக்கம்.` + floral ornament;
- **90–100** — `பிலவங்க ஆண்டு`; 90 has title + `13.4.68` event note + star; 100 closes with `வணக்கம்.` + floral ornament;
- `தலைவர் கலைஞர்:` / `தலைவர் கலைஞரின் முடிவுரைக் கவிதை:` passages and parenthetical poet-performance notes remain separate.

C04 received repeated direct source-critical iterations **A–L**. At the end of iteration L, exactly **22 pages** remained `needs-review` because lexical spans could not be safely inferred from the scan.

### User-designated Gemini lexical control for scans 76–100

The user then supplied a Gemini **word-for-word transcription for the full scans 76–100 range** and explicitly directed:

- **keep the supplied words**;
- **do not silently correct lexical words from the scan**;
- correct only source-supported **page placement, paragraph order, punctuation, quotation structure, headings, speaker labels, performance-note boundaries, poetry lineation and spacing**;
- remove non-body/non-source extraction material such as misplaced running headers/page numbers, library stamps, handwriting-derived text and OCR garbage.

This instruction supersedes earlier scan-derived lexical substitutions inside scans 76–100. Examples include previously settled source readings on scans 79, 81, 86, 89, 90, 94, 96, 97 and 100: the page records now retain the user-designated Gemini words while the scan controls structure.

All **25 C04 page records** were reconciled against the controlling scan under that exact rule. Result:

- scans **76–100: 25/25 `verified`**;
- the 22 former residuals were promoted;
- contiguous verified boundary advanced to **1–100**;
- cumulative status is now **0 partial / 337 needs-review / 128 verified**.

This lexical-control decision is **strictly range-specific to scans 76–100**. Do not carry Gemini/OCR wording into other ranges unless the user explicitly designates it there.

## Source-critical rule for future ranges

Outside an explicitly designated lexical-control range, correct only what the controlling source supports. Preserve old Tamil forms, punctuation, lineation, quotation boundaries, separators, speaker/performance labels and layout. Never fill blur from grammar, metre, memory, historical context or another edition.

## EXACT NEXT ACTIVITY

Begin **Phase 2 Clearance Batch C05 — physical scans 101–125**.

- inspect/reconfirm the source structure for scans 101–125;
- perform source-critical page clearance against the controlling PDF;
- promote only complete passes under the applicable source rule;
- synchronize tracking files after the activity;
- do **not** begin C06, Phase 3, canonical assembly or translation in the same activity.
