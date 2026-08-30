# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Authority rule

**Treat live GitHub `main` as authoritative.**

A SHA, count, phase label or next-step instruction copied into an older chat/prompt is only a checkpoint. If live `main` has advanced, use the newer repository state and do not revert completed work.

The controlling source scan remains the highest textual authority for Tamil source wording unless a documented user instruction explicitly establishes another lexical/editorial control.

## Mandatory startup for every continuation

Before changing an existing work:

1. fetch live `main` and note the current HEAD;
2. read `POEM_PROCESSING_GUIDE.md` completely;
3. read `TRANSCRIPTION_PHASE_PLAN.md` completely;
4. read root `README.md` and `NEXT_CHAT_PROMPT.md` completely;
5. read the target work's current README, source metadata, page map, audit/control records and relevant phase/release files;
6. inspect existing outputs before creating anything;
7. use the controlling source directly whenever the requested activity requires source verification;
8. never commit source PDFs;
9. if status-bearing documents disagree, reconcile them to the newest live work-level evidence instead of restarting an older phase;
10. when the user says **“Proceed with next activity”**, execute the exact next operation recorded in live state.

---

# CURRENT ACTIVE WORK — கலைஞரின் கவிதைகள்

Work directory: `poems/kalaignarin-kavithaigal/`  
Tamil title: **கலைஞரின் கவிதைகள்**  
Author: **கலைஞர் மு. கருணாநிதி**  
Controlling source currently supplied: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

## Durable intake state

**SOURCE INTAKE REGISTERED — PHASE 1 TRANSCRIPTION NEXT.**

- available physical scans: **150**;
- file size: **486,369,088 bytes**;
- SHA-256: **PENDING exact-byte computation; do not guess**;
- source type: image-based scanned PDF with no usable parsed text layer;
- publisher visible: **பாரதி பதிப்பகம்**;
- English imprint: **fourth edition, March 1995**;
- Phase 1 page records created: **0/150**;
- Phase 2: **not started**;
- Phase 3: **not started**;
- translation: **blocked until Tamil final clearance**.

## Critical source-completeness boundary

The supplied 150-scan PDF is **not the complete printed edition**.

Direct source evidence:

- physical scans **15–17** contain the printed contents;
- those contents list entries beginning through at least printed page **444**;
- physical scan **150** visibly carries printed page **133** and still contains continuing body text.

Therefore:

- the available PDF tranche can be fully transcribed as 150/150 scans;
- 150/150 must **never** be described as whole-book completion;
- whole-book source completeness, Tamil final clearance and release remain blocked until continuation source is supplied and reconciled.

## Intake navigation anchors

- scans 1–14: cover/title/imprint and introductory matter;
- scans 15–17: contents;
- scans 18–19: divider / verso;
- scan 20: `இதயத்தைத் தந்திடு அண்ணா` opening, visibly printed page 3;
- scan 150: visibly printed page 133, source ends mid-collection.

Do not infer invisible printed page numbers during Phase 1. Exhaustive scan ↔ printed-page reconciliation belongs to Phase 3.

## Cross-witness safeguard

The anthology includes works already represented elsewhere in the repository from different controlling sources, including at least:

- `இதயத்தைத் தந்திடு அண்ணா!`;
- `தென்னவன் காதை`.

Do **not** copy their existing transcriptions into this anthology. Treat the 1995 anthology as an independent source witness and transcribe every line directly from `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`.

## Exact next activity

Begin **Phase 1 transcription batch 01 — physical scans 1–25**.

Create:

`pages/0001.md` through `pages/0025.md`

Rules:

- direct visual transcription only;
- preserve spelling, punctuation, lineation, headings, quotation marks and unusual forms;
- distinguish later physical marks/labels from edition text;
- record only visibly printed page numbers;
- first-pass records should normally be `partial`, not `verified`;
- include cover, blank/divider, contents and other non-poem pages as page records;
- do not begin Phase 2 in the same activity.

At batch completion update `audit.md` and `indexes/page-map.md` with the durable Phase-1 boundary and exact next batch.

Governing active-work records:

- `poems/kalaignarin-kavithaigal/README.md`;
- `poems/kalaignarin-kavithaigal/SOURCE_INTAKE.md`;
- `poems/kalaignarin-kavithaigal/metadata/source.md`;
- `poems/kalaignarin-kavithaigal/indexes/page-map.md`;
- `poems/kalaignarin-kavithaigal/audit.md`.

---

# Completed work — காலப் பேழையும் கவிதைச் சாவியும்

Work directory: `poems/kaalap-pezhaiyum-kavithai-saaviyum/`.

- Tamil archival/source layer: **FINAL-CLEARED**;
- English Phase 4: **COMPLETE — RELEASE-CLEARED — PASS**;
- canonical Tamil items: **58/58**;
- English items: **58/58**;
- standalone English poem files: **58/58**;
- final source-coverage/release review: **PASS**;
- unresolved release issues: **0**.

There is no remaining routine activity for this released work. Reopen only for an explicit new scope or a genuine source-backed discrepancy.

---

# Paused work — தென்னவன் காதை

Work directory: `poems/thennan-kathai/`.

Tamil archival/source layer: **FINAL-CLEARED**. English translation is partially complete and paused.

When explicitly resumed:

- next permitted batch: **EN-03 — scans 149–151 only**;
- then perform **Gate C omission/speech review** before EN-04;
- preserve the documented scan-151 user-directed omission exactly; do not restore, reconstruct, quote, transliterate, paraphrase, replace or indirectly supply the excluded term unless the user explicitly changes that instruction.

The fact that `தென்னவன் காதை` also appears in the active 1995 anthology does not merge these source witnesses.

---

# Completed work — இதயத்தைத் தந்திடு அண்ணா

Work directory: `poems/idhayathai-thanthidu-anna/`.

- Tamil archival/source layer: **COMPLETE**;
- English translation: **RELEASE-COMPLETE**.

The fact that `இதயத்தைத் தந்திடு அண்ணா` also appears in the active 1995 anthology does not authorize copying the released standalone transcription into the new source witness.

---

# General continuation rule

For every work:

- live `main` is authoritative;
- continue, do not duplicate;
- preserve controlling-source evidence;
- respect declared phase/gate/completion boundaries;
- keep user lexical/editorial controls durable;
- synchronize stale phase/progress/next-activity claims at milestones and handoffs;
- do not merge distinct printed witnesses merely because they contain the same titled work.
