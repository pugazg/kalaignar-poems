# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Authority rule

**Treat live GitHub `main` as authoritative.**

The controlling source scan remains the highest textual authority for Tamil wording unless a documented user instruction establishes another lexical/editorial control.

## Mandatory startup for every continuation

1. fetch live `main` and note the current HEAD;
2. read `POEM_PROCESSING_GUIDE.md` and `TRANSCRIPTION_PHASE_PLAN.md`;
3. read root `README.md` and `NEXT_CHAT_PROMPT.md`;
4. read the target work's README, source metadata, page map and audit;
5. inspect existing boundary page records before continuing;
6. never commit source PDFs;
7. when status documents disagree, reconcile to the newest live work-level evidence;
8. when the user says **“Proceed with next activity”**, execute the exact next operation recorded in live state.

---

# CURRENT ACTIVE WORK — கலைஞரின் கவிதைகள்

Work directory: `poems/kalaignarin-kavithaigal/`  
Author: **கலைஞர் மு. கருணாநிதி**  
Source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

## Durable Phase-1 state

**PHASE 1 TRANSCRIPTION IN PROGRESS — physical scans 1–125 recorded.**

- file size: **486,369,088 bytes**;
- source PDF length: **more than 450 physical pages — user-confirmed; exact integer pending direct full-file metadata verification**;
- current ChatGPT Files page renderer exposes only scans **1–150**;
- **important correction:** the old `150-page PDF / 150-scan tranche` interpretation was wrong; 150 is only the current renderer-access limit;
- SHA-256: **PENDING exact-byte computation; do not guess**;
- edition: **fourth edition, March 1995**;
- Phase 1 records: **125**;
- cumulative status: **10 `partial`, 115 `needs-review`, 0 `verified`**;
- Phase 2: **not started**;
- Phase 3: **not started**;
- translation: **blocked until Tamil final clearance**.

Completed batches:

- Batch 01 — scans **1–25**;
- Batch 02 — scans **26–50**;
- Batch 03 — scans **51–75**;
- Batch 04 — scans **76–100**;
- Batch 05 — scans **101–125**.

Current source boundaries:

- `இதயத்தைத் தந்திடு அண்ணா` closes 31;
- `தென்னவன் காதை` 34–42;
- `இந்திரஜித்` 43–54;
- `இரணியன்` 55–61;
- `வாளி மன்னன்` 62–69;
- `விடுதலை வீரர்கள்` 72–79;
- `ஐம்புலன்` 80–89;
- `பிலவங்க ஆண்டு` 90–100;
- `காதலா - வீரமா?` 101–115, closes on 115;
- `அருமறையில் அறுவர்` opens on 116 and continues beyond 125.

Title evidence newly clarified in Batch 05:

- scan 101 clearly reads **`காதலா - வீரமா?`**;
- scan 116 clearly reads **`அருமறையில் அறுவர்`**;
- earlier blurred contents-page readings remain for Phase-2 reconciliation rather than silent rewriting.

## Durable blur-control rule

- uncertain text remains explicit `⟦…⟧`, never guessed;
- do not fill blur from OCR, memory, grammar, metre, historical expectation or another edition;
- do not copy the separate `இதயத்தைத் தந்திடு அண்ணா` or `தென்னவன் காதை` source witnesses into this anthology;
- preserve source-visible speaker labels/performance notes where legible;
- record only visibly printed page numbers;
- `needs-review` is expected and waits for independent Phase-2 visual/glyph review.

The existing user-directed exclusion applicable to `தென்னவன் காதை` remains in force and must not be reintroduced.

## Source-access correction / blocker

The full user-supplied PDF has **more than 450 pages**, but the current Files renderer exposes only through physical page 150. A page-151 image request did not yield a rendered page.

Therefore:

- scan 150 is **not** the end of the PDF;
- Batch 06 may process scans 126–150 now;
- after that, Phase 1 must continue with scan 151 onward from the same PDF as soon as tooling exposes the remainder;
- do **not** begin Phase 2 merely because the present renderer reaches scan 150.

## Exact next activity

Execute **Phase 1 Batch 06 — physical scans 126–150**.

Create:

`pages/0126.md` through `pages/0150.md`

Continue directly from unfinished `அருமறையில் அறுவர்` at scan 125. Maintain the conservative blur policy. At batch completion, update `audit.md`, `indexes/page-map.md`, README/handover state, and record the tooling-access requirement for scan 151 onward.

---

# Completed work — காலப் பேழையும் கவிதைச் சாவியும்

- Tamil archival/source layer: **FINAL-CLEARED**;
- English Phase 4: **COMPLETE — RELEASE-CLEARED — PASS**;
- canonical/English items: **58/58**;
- standalone English poem files: **58/58**;
- unresolved release issues: **0**.

---

# Paused work — தென்னவன் காதை

Tamil archival/source layer: **FINAL-CLEARED**; English translation partially complete and paused.

When explicitly resumed:

- next permitted batch: **EN-03 — scans 149–151 only**;
- then Gate C omission/speech review;
- preserve the documented user-directed omission exactly unless the user explicitly changes it.

---

# Completed work — இதயத்தைத் தந்திடு அண்ணா

- Tamil archival/source layer: **COMPLETE**;
- English translation: **RELEASE-COMPLETE**.

---

# General continuation rule

Live `main` is authoritative. Continue, do not duplicate; preserve controlling-source evidence and declared phase/gate boundaries; keep user editorial controls durable; never merge distinct printed witnesses merely because they contain the same titled work.