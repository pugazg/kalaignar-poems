# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Authority rule

**Treat live GitHub `main` as authoritative.** The controlling source scan remains the highest textual authority for Tamil wording unless a documented user instruction establishes another lexical/editorial control.

## Mandatory startup

Before continuing `கலைஞரின் கவிதைகள்`:

1. fetch live `main` and note current HEAD;
2. read `POEM_PROCESSING_GUIDE.md`, `TRANSCRIPTION_PHASE_PLAN.md`, root `README.md`, `NEXT_CHAT_PROMPT.md`;
3. read `poems/kalaignarin-kavithaigal/README.md`, `SOURCE_INTAKE.md`, `metadata/source.md`, `indexes/page-map.md`, and `audit.md`;
4. inspect the exact unresolved target pages recorded below before changing anything;
5. use the controlling scan directly; never substitute unrelated OCR, memory, another edition, or a separate source witness;
6. exact page-range derivatives of the same controlling PDF and user-supplied word-for-word extraction may be used as rendering/lexical aids only and must be reconciled against the scan for structure/punctuation/lineation;
7. synchronize status-bearing files after each clearance pass.

# CURRENT ACTIVE WORK — கலைஞரின் கவிதைகள்

Work directory: `poems/kalaignarin-kavithaigal/`  
Author: **கலைஞர் மு. கருணாநிதி**  
Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

## Exact controlling-source identity

- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`;
- printed title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

## Durable phase state

**Phase 1 COMPLETE — 465/465 page records. Phase 2 source coverage COMPLETE — all 465 physical scans independently reread. Phase 2 page clearance remains IN PROGRESS. Clearance C01–C02 is COMPLETE. C03 source-layout review is COMPLETE; C03 lexical clearance remains OPEN.**

Current cumulative page status:

- `partial`: **0**;
- `needs-review`: **384**;
- `verified`: **81**;
- total: **465**;
- unresolved backlog: **384**.

Verified pages: **0001–0050, 0061, 0070, 0071, 0154, 0174, 0184, 0196, 0204, 0215, 0217, 0226, 0238, 0244, 0253, 0260, 0266, 0272, 0285, 0292, 0296, 0310, 0317, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**.

## Phase-2 Clearance Batches C01–C02 — COMPLETE

C01 cleared all unresolved records inside physical scans **1–25**. C02 then cleared unresolved scans **26–31 and 34–50**, preserving already verified scans **32 and 33**.

Durable contiguous verified boundary: **every physical scan 1–50 is `verified`**.

### C02 control / learnings

For C02, the user supplied word-for-word transcription produced from exact page-range derivatives of the same controlling PDF. It was used as the lexical base. The controlling scan remained authoritative for punctuation, lineation, quotation boundaries, page carry-over, running headers/page numbers, illustrations, ornaments and other structural/non-text details.

Important page-level controls:

- scans **26–31** complete `இதயத்தைத் தந்திடு அண்ணா`; scan 31 has a centered closing ornament;
- scan **34** opens `தென்னவன் காதை`; scan 42 closes it with a centered ornament;
- scan **37 → 38** preserves a quotation crossing the physical boundary;
- scan **38** contains a lower line illustration;
- scan **41** preserves the standing user-directed single-token exclusion applicable to `தென்னவன் காதை` while retaining all surrounding source text;
- scan **43** opens `இந்திரஜித்`;
- scan **45 → 46** preserves a speech beginning at the bottom of scan 45;
- scan **47** contains a large reclining-figure illustration splitting a long speech that continues onto scan 48;
- scan **49** contains a mounted-warrior illustration; `000 000 000 8` in the flattened extraction was confirmed as non-text OCR/layout noise and excluded;
- scan **49 → 50** preserves the `காவிற்கு அழகில்லை...` cross-page quotation;
- scan **50** is fully verified as a physical page but `இந்திரஜித்` remains open beyond it.

## Phase-2 Clearance Batch C03 — SOURCE-LAYOUT REVIEW COMPLETE; LEXICAL CLEARANCE OPEN

Physical window: **51–75**.

- previously verified: **70, 71**;
- C03 complete-pass lexical promotion so far: **61**;
- unresolved targets now: **51–60, 62–69 and 72–75** (**22 pages**);
- cumulative totals: **0 partial / 384 needs-review / 81 verified**.

The full C03 window has been directly inspected for physical structure. Durable source-established controls:

- **51–54** — `இந்திரஜித்` continuation; scan **54 / printed 37** ends the item with a centered floral ornament;
- **55–61** — `இரணியன்`; scan **55 / printed 38** opens the titled item; scan **61 / printed 44** closes it with a centered floral ornament and is now complete-pass `verified`;
- **62–69** — `வாளி மன்னன்`; scan **62 / printed 45** opens the titled item; scan **69 / printed 52** closes it with a centered floral ornament;
- **70–71** — already verified divider/title leaves, not reopened;
- **72–75** — `விடுதலை வீரர்கள்`; scan **72 / printed 55** opens with the printed two-line title, `15.8.67` Tiruchi radio-event note and centered star separator; scan **74 / printed 57** visibly separates parenthetical performance notes, `தலைவர் கலைஞர்:` speaker labels and verse; scan **75 / printed 58** contains a large mounted-warrior illustration; the item continues to scan 76.

### Latest C03 lexical pass — scan 61

Scan **61 / printed 44** was reread directly at glyph/word-ending level. The complete pass restores source-backed readings including `ஆடற்று ஆரியம் திருக்கூத்திது!-`, `தெய்வந்தான் ... கொண்டதெனத்`, `அவனறியான்`, and `ஆடுதற்கு ஆவலுடன் நிற்கிட்டான் அரியணையில்!`; printed page/header, punctuation, lineation and the centered floral closing ornament also pass. Status: `verified`.

The current Markdown for the remaining 22 targets still contains provisional first-pass lexical readings. A complete `verified` promotion requires direct glyph/word-ending reconciliation plus punctuation, quotation and lineation checks.

## Phase-2 rule

Independently reread the source itself. Correct only what the controlling scan supports. Preserve old Tamil forms and source anomalies. Resolve `⟦…⟧` / `[மங்கலான ...]` only from direct source evidence. Promote a page to `verified` only when every word/glyph, punctuation mark, line break, quotation, separator and non-Tamil element passes.

## Cross-witness safeguard

Do not copy separate source-witness transcriptions into this anthology. Exact page derivatives from the same controlling PDF are source-access aids only. Other witnesses may not determine anthology wording. The existing user-directed exclusion applicable to `தென்னவன் காதை` remains in force.

## EXACT NEXT ACTIVITY

Continue **Phase 2 Clearance Batch C03 — exact lexical/glyph verification of scans 51–60, 62–69 and 72–75**.

- source-layout boundaries are already fixed as recorded above;
- do not reopen scans 61, 70 or 71 merely for uniformity;
- if a user-supplied word-for-word extraction from the exact controlling-PDF pages is available, retain those words as the lexical base and independently check punctuation, quotation continuity, lineation, illustrations/ornaments and page boundaries;
- otherwise resolve only what the controlling scan itself supports without guessing;
- promote only complete passes to `verified`;
- keep C03 open until all **22** residual pages are cleared;
- **do not advance to C04, Phase 3, canonical assembly or translation**.
