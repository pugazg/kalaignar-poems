# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Authority rule

**Treat live GitHub `main` as authoritative.**

A SHA, count, phase label or next-step instruction copied into an older chat/prompt is only a checkpoint. If live `main` has advanced, continue from the newer repository state and do not revert completed work.

The controlling source scan remains the highest textual authority for Tamil source wording unless a documented user instruction explicitly establishes another lexical/editorial control.

## Mandatory startup for every continuation

Before making any repository change:

1. inspect live `main` and note its current HEAD;
2. read `POEM_PROCESSING_GUIDE.md` **completely**;
3. read `TRANSCRIPTION_PHASE_PLAN.md` **completely**;
4. read root `README.md` **completely**;
5. read `NEXT_CHAT_PROMPT.md` **completely**;
6. for the active work, read its `README.md`, `metadata/source.md`, `indexes/page-map.md`, `audit.md` and every phase-specific control/audit file relevant to the current activity;
7. inspect existing output files before creating anything; continue them and do not duplicate records;
8. inspect the controlling source when the current activity requires direct source verification;
9. do not commit source PDFs;
10. determine the declared current phase/gate from live work-level evidence before acting;
11. if status-bearing documents disagree, reconcile stale documents to the newest live work state rather than restarting an older phase;
12. do not restart completed work merely because this is a fresh chat.

---

# CURRENT ACTIVE WORK — காலப் பேழையும் கவிதைச் சாவியும்

Work directory: `poems/kaalap-pezhaiyum-kavithai-saaviyum/`  
Tamil title: **காலப் பேழையும் கவிதைச் சாவியும்**  
Author: **கலைஞர் மு. கருணாநிதி**  
Controlling source: `TVA_BOK_0063593_காலப்_பேழையும்_கவிதைச்_சாவியும்.pdf`  
SHA-256: `ad5a6a4b4d2b111120f99baa4aff4ab639cf1a9f9c71a6899e0c3d2c4a08bcc3`  
Physical scans: **306**.

## Current phase

**Phase 3 — canonical Tamil assembly is active.**

Do not return to transcription, Phase-2 verification, scan/page reconciliation, boundary auditing or title-witness reconciliation unless a genuine newly discovered source discrepancy requires a documented reopen.

### Completed gates

- Phase 1 page-record transcription: **306/306 — COMPLETE**;
- contents: **58/58 verified**;
- Phase 2 independent source-critical visual verification: **306/306 — COMPLETE**;
- unresolved readings after Phase 2: **none**;
- Phase 3 scan ↔ printed-page reconciliation: **COMPLETE**;
- all **306 scans** structurally accounted for;
- scans **5–299** correspond to logical printed pages **4–298** continuously;
- all **58** contents start pages align with title scans by `title scan = contents start page + 1`;
- Phase 3 boundary / within-item page-join audit: **COMPLETE — 58/58 items certified**;
- closing boundary **299→300: PASS**; scan 299 closes the numbered sequence with `(முதல் பாகம் முற்றிற்று)`, scan 300 begins separate `குறிப்புகள்` end matter;
- Phase 3 title-witness reconciliation: **COMPLETE — 14/14 discrepancy cases reconciled**.

### Current canonical assembly state

Canonical assembly status: **6/58 item files assembled**.

Existing canonical files:

- `sections/01.md` — item 1 — scans 10–11;
- `sections/02.md` — item 2 — scans 12–15;
- `sections/03.md` — item 3 — scans 16–19;
- `sections/04.md` — item 4 — scans 20–24;
- `sections/05.md` — item 5 — scans 25–28;
- `sections/06.md` — item 6 — scans 29–34.

Canonical-assembly iteration 1, scans **10–34**, is complete.

The work-state checkpoint immediately before this handover refresh was commit `95d59d9c73f853ba8dbd0ab20cb9f25417784e34` (`Record Kaalap Pezhai canonical assembly batch 1`). **Do not assume that SHA is still HEAD; always fetch live `main` first.**

## Canonical assembly rules

The governing record is:

`poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_CANONICAL_ASSEMBLY.md`

Mandatory rules:

1. assemble stable item sequence **1–58**;
2. derive body text only from the item's `verified` `pages/NNNN.md` records;
3. preserve verified spelling, punctuation, lineation, quotation structure, separators, notes and unusual source forms;
4. preserve physical-page provenance with `<!-- scan_page: N -->` markers;
5. use stable numeric filenames `01.md` … `58.md`;
6. use the **item-opening title-page witness** as the canonical displayed title;
7. when the contents title differs, preserve the contents witness separately in front matter / source metadata — never create a hybrid title;
8. preserve item 37's title-page printed number **36** as a source anomaly while keeping stable sequence identity **37**;
9. routine assembly proceeds in **25-physical-scan iterations**;
10. if an iteration ends inside an item, **do not create a partial canonical item file**; carry the whole item forward until its complete certified range is available;
11. if assembly uncovers a genuine discrepancy in a verified source record, reopen/document/correct the source layer and revalidate affected assembly rather than silently fixing only `sections/`;
12. do not begin assembly/source-completeness review before all **58/58** canonical item files exist;
13. do not begin Phase 4 translation before Tamil final clearance.

## Title-witness discrepancy set

The contents and title-page witnesses differ for items:

**18, 22, 25, 26, 29, 31, 32, 37, 40, 44, 46, 50, 54 and 58.**

The completed reconciliation rule is: title-page witness for canonical display title; contents witness preserved separately; no hybrid normalization.

Important source anomalies include:

- item 37: contents `அன்பால் அவனை விலை கொள்ள முடியுமா?`; title page `அன்பால் அவனை விலைகொள்ள முடியுமோ?`; title page visibly prints item number **36**;
- item 50: contents `குருதிக் களமே! கொலு மண்டபம் ஆனது!`; title page `குருதிக்களமே; கொலு மண்டபம் ஆனது!`;
- item 54: contents `தலையாலங்கானத்துச் செரு வென்றான்!`; title page `தலையாலங்கானத்துச் செருவென்றான்!`;
- item 58: contents `பகை வாள் முனை மருங்க; நாள் எல்லாம் உழைப்போம்`; title page `பகைவாள் முனை மருங்க; நாள் எல்லாம் உழைப்போம்!`.

Read the full decision record before encountering these items:

`PHASE3_TITLE_WITNESS_RECONCILIATION.md`.

## Exact next activity

Process **physical scans 35–59** as canonical-assembly iteration 2.

Create only the complete certified items contained in that 25-scan window:

- item 7 — scans **35–39** → `sections/07.md`;
- item 8 — scans **40–43** → `sections/08.md`;
- item 9 — scans **44–49** → `sections/09.md`;
- item 10 — scans **50–53** → `sections/10.md`;
- item 11 — scans **54–57** → `sections/11.md`.

Item 12 begins at scan **58** and continues through scan **63**. Because the next iteration ends at scan 59, **do not create `sections/12.md` in this iteration**. Carry item 12 forward until its full certified range is available in the following iteration.

Before creating 07–11, inspect `sections/01.md` through `sections/06.md` for the canonical front-matter/provenance pattern and read the verified page records for scans 35–59.

At iteration completion:

- update `PHASE3_CANONICAL_ASSEMBLY.md`;
- update the work `README.md`;
- synchronize any other status-bearing file whose progress claim becomes stale;
- report files created/changed, cumulative canonical count, resulting live `main` SHA and exact next 25-scan activity.

---

# Other work — தென்னவன் காதை

Work directory: `poems/thennan-kathai/`.

Tamil archival/source layer: **FINAL-CLEARED**.

English translation is partially complete and currently paused while another work is active. When this work is explicitly resumed:

- read all live translation control files first;
- next permitted batch: **EN-03 — scans 149–151 only**;
- then perform **Gate C omission/speech review** before beginning EN-04;
- do not start EN-04 in the same activity as the EN-03 draft.

A scan-151 user-directed editorial omission is durable control. The excluded caste-based term must **not** be restored, reconstructed, quoted, transliterated, paraphrased, replaced or indirectly supplied unless the user explicitly changes that instruction.

---

# Completed work — இதயத்தைத் தந்திடு அண்ணா

Work directory: `poems/idhayathai-thanthidu-anna/`.

- Tamil archival/source layer: **COMPLETE**;
- English translation: **RELEASE-COMPLETE**.

Do not retranscribe, normalize, retranslate or modify this released work unless a genuine source-level discrepancy is found and documented or the user explicitly requests a separately tracked editorial revision.

The established translation principle remains:

> **Retain Kalaignar's language while translating.**

Voice fidelity takes priority over generic elegance: preserve direct address, public cadence, repetition, political specificity, literary/classical references, imagery and emotional escalation.

---

# General continuation rule

For any work in this repository:

- inspect live source/work state first;
- continue, do not duplicate;
- preserve controlling-source evidence;
- respect the declared phase/gate;
- keep user lexical/editorial controls durable;
- synchronize stale status documents at phase/handoff boundaries;
- when the user says **“Proceed with next activity”**, execute the exact next operation recorded in live state without asking them to choose a routine step.