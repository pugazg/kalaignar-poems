# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems` — branch `main`

## Authority rule

**Live GitHub `main` is authoritative.** The controlling scan is source authority for physical/source structure. An explicitly user-designated exact-source word-for-word transcription controls lexical words only where that supplied text is actually present for the stated page range.

## Mandatory startup

Before continuing `கலைஞரின் கவிதைகள்`:

1. fetch live `main`;
2. read `POEM_PROCESSING_GUIDE.md`, `TRANSCRIPTION_PHASE_PLAN.md`, root `README.md`, `NEXT_CHAT_PROMPT.md`;
3. read `poems/kalaignarin-kavithaigal/README.md`, `SOURCE_INTAKE.md`, `metadata/source.md`, `indexes/page-map.md`, `audit.md`;
4. preserve source-established page/order/lineation structure and the user-designated lexical words;
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

## Durable state

- Phase 1: **465/465 COMPLETE**;
- Phase 2 source coverage: **465/465 COMPLETE**;
- Clearance **C01–C11 COMPLETE**;
- C12: **PARTIAL**;
- cumulative: **0 partial / 169 needs-review / 296 verified**;
- verified: **0001–0275, 0285, 0292–0300, 0310, 0317, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**;
- durable contiguous verified boundary: **1–275**;
- Phase 3 / canonical assembly / translation: **blocked**.

## Completed lexical-control ranges

- C04 76–100 — supplied Gemini transcription;
- C05 101–125 — `part_005_pages_101-125`;
- C06 126–150 — `part_006_pages_126-150`;
- C07 151–175 — `part_007_pages_151-175`;
- C08 176–200 — `kavi1.md` / `part_008_pages_176-200`;
- C09 201–225 — `kavi2.md` / `part_009_pages_201-225`;
- C10 226–250 — `kavi3.md` / `part_010_pages_226-250`;
- C11 251–275 — `kavi4.md` / `part_011_pages_251-275`.

Standing rule:

- retain supplied lexical words;
- source-established scan structure controls physical placement, order, punctuation, quotations, headings, speaker/performance-note boundaries, lineation and spacing;
- exclude running headers/page numbers, library marks, handwriting-derived material and OCR/extraction garbage;
- never silently substitute scan-derived lexical wording where the user supplied a lexical control.

## C12 — PARTIAL / SUPPLIED-FILE GAP

Intended physical window: **276–300**. Uploaded `kavi5.md` says it was extracted from `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_012_pages_276-300.pdf`.

Actual attached Markdown content is incomplete for that declared range:

- its first body page is printed page **276**, corresponding to physical scan **293** in the established page map;
- its last body page is printed page **283**, corresponding to physical scan **300**;
- it contains no lexical transcription for physical scans **276–292** / printed pages **259–275**.

Work completed safely:

- **293–300** reconciled to the supplied `kavi5.md` words and marked `verified`;
- **296** remained verified while being reconciled;
- new promotions from this partial C12 activity: **293, 294, 295, 297, 298, 299, 300** = **7**;
- pre-existing verified scans **285** and **292** were preserved and not altered by absent lexical text;
- scans **276–284 and 286–291** remain `needs-review` under C12 because the intended supplied lexical text is missing;
- cumulative moved from **0/176/289** to **0/169/296**;
- contiguous verified boundary remains **1–275**.

Notable retained supplied forms in scans 293–300 include `உடன் பிறப்பே`, `சோதரிகள்`, `குறளையும்`, `உதடசைக்கு`, `எழுபத்தி`, `உலைக்களத்துக்`, `கை நிறைய`, `காலனியாய்`, `நாடாகக்`, `இந்தி வெறியர்களின்`, `கறுப்பு`, `சூளூரை`, `அணுப் பொழுதுமின்றி`, `நாடதிர`, `எங்குதித்த`, `கங்குகரை`, `கனல் கிளம்ப`, `கலிங்கத்துப்`, `பழம்பாட்டே`, `சூளுரை`, `வைதீகபுரியை`, `செல்லுபடியானதில்லை`, `சினந்து`, `புதுமைக் காளைகள்`, `இந்நாட்டான்`, `கொழித்து விட்ட உமிகள்`, `உதித்துவிட்ட`, `உயர்ஜாதிக்காரர்`, `கடவுளரின்`, `நடத்துகின்றீர்`, `ஆனகதி`, and `சிவனாரும்`.

Extraction garbage such as `mimage A`, non-Tamil script, running `கலைஞரின்` / `கவிதைகள்` headers and page numerals was excluded.

## Remaining uploaded sequence

- `kavi5.md` → intended 276–300, but current payload only supplies 293–300 — **C12 PARTIAL**;
- `kavi6.md` → 301–325;
- `kavi7.md` → 326–350;
- `kavi8.md` → 351–375;
- `kavi9.md` → 376–400;
- `kavi10.md` → 401–425;
- `kavi11.md` begins with internal label `part_018_pages_426-450`; inspect internal transitions before final-range use.

## EXACT NEXT ACTIVITY

Recover or re-attach the missing word-for-word transcription for **physical scans 276–292 / printed pages 259–275** from the intended `part_012_pages_276-300` source range, then finish C12. Preserve already verified scans **285** and **292**. Do **not** begin C13, Phase 3, canonical assembly or translation until C12 is complete.
