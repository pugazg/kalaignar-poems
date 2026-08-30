# Audit — கலைஞரின் கவிதைகள்

## Current state

**PHASE 1 TRANSCRIPTION IN PROGRESS — batches 01–02, scans 1–50 recorded.**

- controlling source currently supplied: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`;
- available physical scans: **150**;
- file size: **486,369,088 bytes**;
- SHA-256: **pending exact-byte computation**;
- Phase 1 page records: **50/150**;
- cumulative Phase 1 status: **8 `partial`, 42 `needs-review`, 0 `verified`**;
- Phase 2 verification: **not started**;
- Phase 3: **not started**;
- English translation: **blocked**.

## Phase 1 batch 01 — scans 1–25

Result: **PAGE-RECORD BATCH CREATED — SOURCE BLUR PRESERVED AS EXPLICIT UNCERTAINTY; NO SILENT RECONSTRUCTION.**

Created:

- `pages/0001.md` through `pages/0025.md`;
- cover/title/imprint/introduction/contents/divider/verso represented;
- poem opening through printed page 8 represented as the present anthology witness;
- scan 25 remains an in-poem continuation boundary into scan 26.

Pages needing Phase-2 attention from Batch 01:

`0002`, `0004`, `0006`–`0017`, `0021`–`0025`.

## Phase 1 batch 02 — scans 26–50

Result: **PAGE-RECORD BATCH CREATED — BLURRED WORDING LEFT UNRESOLVED; CROSS-WITNESS TEXT NOT IMPORTED.**

Created:

- `pages/0026.md` through `pages/0050.md`;
- `இதயத்தைத் தந்திடு அண்ணா` continued through scan 31 / visible printed page 14 and closes there;
- scan 32 records the `இனமான எந்தல்கள்` section divider;
- scan 33 records the divider verso/show-through separately;
- `தென்னவன் காதை` is represented from scan 34 through scan 42 / visible printed page 25 and closes before the next item;
- `இந்திரஜித்` opens on scan 43 and continues through scan 50 / visible printed page 33;
- scan 50 remains an in-item continuation boundary into scan 51.

Batch-02 status:

- `partial`: **2** — scans 32–33;
- `needs-review`: **23** — scans 26–31 and 34–50;
- `verified`: **0**.

### Blur / uncertainty handling

The user's warning that the PDF contains blurred text remains an active control.

For Batches 01–02:

- `⟦…⟧` marks an editorial first-pass uncertainty span and is **not** source punctuation or source wording;
- only confidently legible wording is transcribed;
- blurred text is not reconstructed from OCR, metre, grammar, remembered wording, historical expectation or another edition;
- the separately archived `இதயத்தைத் தந்திடு அண்ணா` and `தென்னவன் காதை` files are not used to fill this anthology witness;
- page boundaries and visible printed numbers are preserved independently;
- source-visible artwork/divider/show-through roles are recorded separately from edition text.

### User-directed exclusion safeguard

The repository already contains a durable user instruction excluding one caste-slur term from `தென்னவன் காதை`. This anthology pass does **not** reintroduce that excluded term. The instruction remains in force unless the user explicitly changes it.

### Pages needing Phase-2 attention from Batch 02

`0026`–`0031`, `0034`–`0050`.

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
- source lineation and punctuation preserved where legible;
- page records remain `partial` after first pass unless a specific unresolved reading requires `needs-review`;
- only visibly printed page numbers are recorded as printed numbers;
- OCR/extracted text is not controlling authority;
- later-looking labels/stamps/donation marks are distinguished from edition text;
- blank/graphic/divider pages receive page records too;
- systematic continuity and title-witness reconciliation are deferred to Phase 3.

## Open metadata item

SHA-256 of the exact uploaded 486,369,088-byte file remains pending because the current repository-writing interface has not exposed direct source-byte hashing. This value must be computed from the exact source bytes and filled without guesswork.

## Exact next activity

Transcribe **physical scans 51–75** as Phase 1 batch 03 and create `pages/0051.md` through `pages/0075.md`.

Continue the same conservative blur protocol. If a word or line cannot be read safely from the controlling scan, preserve an explicit unresolved marker instead of reconstructing it from another witness or contextual expectation.

At the end of that batch:

- update this audit with cumulative page-record/status counts;
- extend `indexes/page-map.md` with visible printed-page evidence;
- do not begin Phase 2 in the same activity.