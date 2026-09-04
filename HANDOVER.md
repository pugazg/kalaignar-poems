# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems` — branch `main`.

**Live `main` is authoritative. Fetch it first in every fresh chat and preserve any newer durable state.**

## Active work — ஒருதலைக் காதல்

Workspace: `poems/oruthalaik-kathal/`

Controlling source: `TVA_BOK_0065554_ஒருதலைக்_காதல்.pdf`

Exact source identity:

- physical PDF pages: **101**;
- bytes: **200,800,237**;
- SHA-256: `a9b0ff45820155a4775074f630e791a8304073a90e5e36ab793bdf702ec33184`;
- title: **ஒருதலைக் காதல்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **திருமகள் நிலையம்**;
- first edition: **December 1998**;
- source pagination statement: **95 + IV**.

The publisher's preface describes the work as an **ஓவியக் கவிதை நாவல்**. Treat the scan as controlling source; do not silently modernize or reconstruct wording.

## Durable source-intake state

Source intake for `ஒருதலைக் காதல்` is **COMPLETE**:

- exact-byte source identity: PASS;
- physical scans accounted: **101/101**;
- page-record scaffolds: **101/101**;
- Phase-1 lexical transcription: **0/101**;
- current page statuses: **101 not-started**;
- Phase 2: not started;
- Phase 3: not started;
- Phase 4: not started.

Physical structure:

- scan 1 front cover;
- scan 2 title page;
- scan 3 publication details;
- scan 4 `பதிப்புரை`;
- scan 5 photograph / publisher tribute;
- scans 6–100 logical printed pages 1–95, invariant `logical_page = scan_page - 5`;
- scan 101 back cover;
- numbered section starts: **1→6, 2→14, 3→21, 4→31, 5→39, 6→46, 7→56, 8→64, 9→74, 10→83, 11→93**;
- illustration-only scans: **8, 16, 22, 32, 40, 48, 58, 66, 76, 84, 94**;
- scan 100 / logical printed page 95 ends with `(முற்றும்)`.

### Printed-page rule

`printed_page` in page front matter records only a numeral visibly printed on that scan. Section-opening and full-page illustration scans suppress the numeral and therefore retain `printed_page: null`; their logical position is separately preserved in `indexes/page-map.md`.

## Preserved completed work — கலைஞரின் கவிதைகள்

`poems/kalaignarin-kavithaigal/` remains **RELEASE-CLEARED**:

- Phase 1: 465/465 complete;
- Phase 2: 465/465 verified;
- Phase 3 Gates 1–6: PASS;
- Tamil layer: FINAL-CLEARED;
- English Phase 4: 18/18 batches PASS;
- canonical items: 77/77;
- item-owned scans: 439/439;
- unresolved release issues: 0.

Do **not** reopen or modify that completed workspace merely because this handover now points to a different active source.

## Wave-4 freeze note

`WAVE4_SOURCE_FREEZE.md` freezes the earlier six-workspace source boundary at its recorded source commit. `poems/oruthalaik-kathal/` was added later and is outside that historical freeze. The old 6/6 statement must not be interpreted as current seven-workspace coverage.

## Mandatory startup for continuation

Before changing the active work, read completely:

1. `POEM_PROCESSING_GUIDE.md`;
2. `TRANSCRIPTION_PHASE_PLAN.md`;
3. root `README.md`;
4. this `HANDOVER.md`;
5. root `NEXT_CHAT_PROMPT.md`;
6. `poems/oruthalaik-kathal/README.md`;
7. `poems/oruthalaik-kathal/SOURCE_INTAKE.md`;
8. `poems/oruthalaik-kathal/metadata/source.md`;
9. `poems/oruthalaik-kathal/indexes/page-map.md`;
10. `poems/oruthalaik-kathal/audit.md`;
11. `poems/oruthalaik-kathal/HANDOVER.md`;
12. `poems/oruthalaik-kathal/NEXT_CHAT_PROMPT.md`;
13. the active page records required by the current batch.

## EXACT NEXT ACTIVITY

**Phase 1 Batch 01 — transcribe scans 1–25** into the existing `pages/0001.md`–`pages/0025.md` records.

Rules:

- use only the controlling scan for lexical authority;
- preserve visible spelling, punctuation, lineation, headings and non-text page roles;
- do not infer suppressed printed numerals;
- keep first-pass pages `partial` unless genuinely independently verified later;
- record unresolved glyphs explicitly rather than guessing;
- do not start Phase 2 verification, Phase 3 assembly, English translation or Digital Library work in this activity.

After the batch, synchronize the active-work README, audit, page map if source discoveries require it, root handover/next prompt, and record the next contiguous Phase-1 batch.
