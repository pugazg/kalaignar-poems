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
10. when the user says **“Proceed with next activity”**, execute the exact next operation recorded in live state. If a completed work explicitly records that no routine next activity remains, do not invent a new project scope.

---

# Completed work — காலப் பேழையும் கவிதைச் சாவியும்

Work directory: `poems/kaalap-pezhaiyum-kavithai-saaviyum/`  
Tamil title: **காலப் பேழையும் கவிதைச் சாவியும்**  
Author: **கலைஞர் மு. கருணாநிதி**  
Controlling source: `TVA_BOK_0063593_காலப்_பேழையும்_கவிதைச்_சாவியும்.pdf`  
SHA-256: `ad5a6a4b4d2b111120f99baa4aff4ab639cf1a9f9c71a6899e0c3d2c4a08bcc3`  
Physical scans: **306**.

## Final durable state

**Tamil archival/source layer: FINAL-CLEARED.**  
**English Phase 4: COMPLETE — RELEASE-CLEARED — PASS.**

Durable release record: `poems/kaalap-pezhaiyum-kavithai-saaviyum/translations/en/RELEASE_REPORT.md`.

Final counts and gates:

- Phase 1 page-record transcription: **306/306 — COMPLETE**;
- Phase 2 source-critical visual verification: **306/306 — COMPLETE**;
- unresolved Tamil readings: **0**;
- scan ↔ printed-page reconciliation: **COMPLETE**;
- boundary / page-join audit: **58/58 items — PASS**;
- title-witness reconciliation: **14/14 discrepancy cases — PASS**;
- canonical Tamil assembly: **58/58** (`sections/01.md` … `sections/58.md`);
- assembly/source-completeness review: **PASS**;
- Tamil final clearance: **PASS**;
- English translation batches: **21/21 reviewed PASS**;
- English stable items: **58/58**;
- numbered-item English scan coverage: **290/290**, scans **10–299**;
- complete reader-facing English assembly: **RELEASE-CLEARED**;
- standalone English poem files: **58/58**, indexed under `translations/en/items/`;
- full-work editorial/terminology/Kalaignar-voice review: **PASS**;
- final source-coverage/release review: **PASS**;
- unresolved release issues: **0**;
- Tamil canonical/page files changed during Phase 4: **0**.

The numbered first-part collection ends at scan **299** with `(முதல் பாகம் முற்றிற்று)` / `(First Part Complete)`. Scan **300** begins separate `குறிப்புகள்` end matter and is not part of item 58's English translation.

The 14 title-witness discrepancy items remain:

**18, 22, 25, 26, 29, 31, 32, 37, 40, 44, 46, 50, 54 and 58.**

Item 37 remains stable item **37** while preserving printed item number **36** only as a source anomaly.

## Completion boundary

There is **no remaining routine Phase-4 activity** for `காலப் பேழையும் கவிதைச் சாவியும்`.

Do not retranscribe, reassemble, retranslate, normalize or reopen this released work merely because a fresh chat begins. A future change requires either:

- a genuine source-backed discrepancy with a documented reopen of the affected source/audit/canonical/release layers; or
- an explicit new editorial/derivative scope from the user.

---

# Paused work — தென்னவன் காதை

Work directory: `poems/thennan-kathai/`.

Tamil archival/source layer: **FINAL-CLEARED**.

English translation is partially complete and paused. It is **not automatically selected merely because the Kaalap work is complete**. Resume it only when the user explicitly selects that work or gives a clearly equivalent instruction.

When explicitly resumed:

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

Do not modify this released work unless a genuine source-level discrepancy is documented or the user explicitly requests a separately tracked revision.

---

# General continuation rule

For every work:

- live `main` is authoritative;
- continue, do not duplicate;
- preserve controlling-source evidence;
- respect declared phase/gate/completion boundaries;
- keep user lexical/editorial controls durable;
- synchronize stale phase/progress/next-activity claims at milestones and handoffs;
- never infer that completion of one work authorizes starting another work without user scope.
