# Audit — கலைஞரின் கவிதைகள்

## Current state

**PHASE 1 TRANSCRIPTION IN PROGRESS — batch 01 scans 1–25 recorded.**

- controlling source currently supplied: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`;
- available physical scans: **150**;
- file size: **486,369,088 bytes**;
- SHA-256: **pending exact-byte computation**;
- Phase 1 page records: **25/150**;
- Phase 1 status among scans 1–25: **6 `partial`, 19 `needs-review`, 0 `verified`**;
- Phase 2 verification: **not started**;
- Phase 3: **not started**;
- English translation: **blocked**.

## Phase 1 batch 01 — scans 1–25

Result: **PAGE-RECORD BATCH CREATED — SOURCE BLUR PRESERVED AS EXPLICIT UNCERTAINTY; NO SILENT RECONSTRUCTION.**

Created:

- `pages/0001.md` through `pages/0025.md`;
- covers/title/imprint/introduction/contents/divider/verso all represented;
- poem opening through printed page 8 represented as the present anthology witness;
- scan 25 correctly remains an in-poem continuation boundary into scan 26.

### Blur / uncertainty handling

The user explicitly warned that this PDF contains blurred text. Batch 01 therefore uses a conservative first-pass policy:

- uncertain small imprint text on scan 2 is not guessed;
- blurred prose on scans 4 and 6–14 is left with explicit editorial uncertainty markers where safe reading is not possible;
- small-type contents on scans 15–17 are transcribed where legible, with uncertain title strings explicitly marked rather than normalized;
- scans 21–25 contain visibly blurred verse blocks; only confidently legible lines are transcribed and the unreadable spans remain explicitly unresolved;
- no wording from the separately archived `இதயத்தைத் தந்திடு அண்ணா` witness is used to fill anthology blur;
- OCR, remembered wording, metre, historical context and semantic expectation are not used as authority.

`⟦…⟧` in first-pass page files is an editorial uncertainty marker and is **not** source punctuation or source wording.

### Pages needing Phase-2 attention from this batch

`0002`, `0004`, `0006`–`0017`, `0021`–`0025`.

These records are intentionally **not** promoted to `verified`.

## Source-completeness finding

The supplied PDF is not the complete printed edition.

Intake evidence:

- contents scans **15–17** list entries through at least printed page **444**;
- scan **150** visibly carries printed page **133** and ends with continuing body text;
- therefore the available source terminates mid-collection.

This is a source-availability limitation, not a transcription uncertainty. The repository may faithfully process all 150 supplied scans while preserving the explicit whole-book completeness blocker.

## Cross-witness safeguard

This anthology visibly includes material also represented by separate existing source witnesses in the repository, including `இதயத்தைத் தந்திடு அண்ணா!` and `தென்னவன் காதை`.

Rules:

1. do not copy those existing Tamil transcriptions into this work;
2. do not use their punctuation, lineation or spelling to silently repair this anthology witness;
3. when an apparent difference is found, preserve the present scan reading and document later cross-edition comparison separately;
4. no English reuse is permitted before this anthology reaches Tamil final clearance.

## Phase-1 rules for this work

- direct visual transcription only;
- source lineation and punctuation preserved;
- page records remain `partial` after first pass unless a specific unresolved reading requires `needs-review`;
- only visibly printed page numbers are recorded as printed numbers;
- OCR/extracted text is not controlling authority;
- later-looking labels/stamps/donation marks are distinguished from edition text;
- blank/graphic/divider pages receive page records too;
- systematic continuity and title-witness reconciliation are deferred to Phase 3.

## Open metadata item

SHA-256 of the exact uploaded 486,369,088-byte file remains pending because the current repository-writing interface has not exposed direct source-byte hashing. This value must be computed from the exact source bytes and filled without guesswork.

## Exact next activity

Transcribe **physical scans 26–50** as Phase 1 batch 02 and create `pages/0026.md` through `pages/0050.md`.

Continue the same conservative blur protocol: if a word or line cannot be read safely from the controlling scan, preserve an explicit unresolved marker instead of reconstructing it from the separate poem witness or contextual expectation.

At the end of that batch:

- update this audit with the cumulative page-record count and any genuine unresolved readings;
- extend `indexes/page-map.md` with visible printed-page evidence;
- do not begin Phase 2 in the same activity.