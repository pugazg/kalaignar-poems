# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Authority rule

**Treat live GitHub `main` as authoritative.**

The controlling source scan remains the highest textual authority for Tamil wording unless a documented user instruction establishes another lexical/editorial control. A SHA, count, boundary or next-step instruction copied into an older chat is only a checkpoint; if live `main` has advanced, preserve the newer work and continue from it.

## Mandatory startup for every continuation

Before changing this repository in a fresh chat:

1. fetch live `main` and note the current HEAD;
2. read `POEM_PROCESSING_GUIDE.md` completely;
3. read `TRANSCRIPTION_PHASE_PLAN.md` completely;
4. read root `README.md` and `NEXT_CHAT_PROMPT.md` completely;
5. read the active work's `README.md`, `SOURCE_INTAKE.md`, `metadata/source.md`, `indexes/page-map.md`, and `audit.md` completely;
6. inspect the current boundary page record(s), especially `pages/0150.md`, before creating the next record;
7. use the controlling PDF directly whenever transcription/verification requires source evidence;
8. never commit the source PDF;
9. when status-bearing files disagree, resolve from the newest live work-level evidence and the controlling source, then synchronize stale records;
10. when the user says **“Proceed with next activity”**, execute the exact next operation recorded in live state without asking them to choose a routine continuation step.

---

# CURRENT ACTIVE WORK — கலைஞரின் கவிதைகள்

Work directory: `poems/kalaignarin-kavithaigal/`  
Author: **கலைஞர் மு. கருணாநிதி**  
Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

## Exact controlling-source identity

These values were established from the exact supplied PDF bytes and are durable:

- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: **`19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`**;
- printed title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

### Critical renderer warning

An earlier chat/file renderer exposed only pages 1–150 and reported `total_pages: 150`. That was **not** the PDF's actual length. Exact-byte inspection established **465 physical pages**, and direct rendering from the same PDF confirmed scan 151 exists and continues the text.

Therefore:

- never replace the durable **465-page** count with a renderer/window count;
- never describe scan 150 as the end of the PDF;
- if a high-level page renderer stops at 150, use the exact mounted/source PDF bytes with a source-byte-capable PDF renderer for scan 151 onward;
- keep physical scan numbering 1-indexed and stable against the same controlling PDF hash above.

## Durable Phase-1 state at handoff

**PHASE 1 TRANSCRIPTION IN PROGRESS — physical scans 1–150 / 465 recorded.**

- Phase 1 page records: **150/465**;
- files created: `pages/0001.md` through `pages/0150.md`;
- cumulative status: **10 `partial`, 140 `needs-review`, 0 `verified`**;
- Phase 2 source-critical verification: **not started**;
- Phase 3 structure/assembly/final clearance: **not started**;
- English translation/release: **blocked until Tamil final clearance**.

Completed Phase-1 batches:

- Batch 01 — scans **1–25**;
- Batch 02 — scans **26–50**;
- Batch 03 — scans **51–75**;
- Batch 04 — scans **76–100**;
- Batch 05 — scans **101–125**;
- Batch 06 — scans **126–150**.

## Durable source/item boundaries established so far

- scans 1–17 — cover/title/imprint/front matter/contents;
- `இதயத்தைத் தந்திடு அண்ணா` — scans **20–31**, closes scan 31;
- scans 32–33 — `இனமான எந்தல்கள்` divider/verso;
- `தென்னவன் காதை` — scans **34–42**, closes scan 42;
- `இந்திரஜித்` — scans **43–54**, closes scan 54;
- `இரணியன்` — scans **55–61**, closes scan 61;
- `வாளி மன்னன்` — scans **62–69**, closes scan 69;
- scans 70–71 — `கவியரங்கக் கவிதைகள்` divider/verso;
- `விடுதலை வீரர்கள்` — scans **72–79**, closes scan 79;
- `ஐம்புலன்` — scans **80–89**, closes scan 89;
- `பிலவங்க ஆண்டு` — scans **90–100**, closes scan 100;
- `காதலா - வீரமா?` — scans **101–115**, closes scan 115;
- `அருமறையில் அறுவர்` — scans **116–127**, closes scan 127;
- `புதிய பாதை` — scans **128–137**, closes scan 137;
- `உடைமைகள் பத்து` — scans **138–143**, closes scan 143;
- `நீர்க் குடும்பம்` — opens scan **144** and **continues beyond scan 150**.

Boundary evidence:

- scan **150** visibly prints page **133** and ends mid-item after the chair introduces the `மழை` movement;
- scan **151** has already been source-access checked, visibly prints page **134**, and continues `நீர்க் குடும்பம்`;
- `pages/0151.md` has **not** yet been created; it belongs to the next batch.

## Durable blur / difficult-reading rule

The user explicitly warned that this PDF contains blurred text. Preserve that constraint through the entire source.

During Phase 1:

- transcribe only what the controlling scan safely supports;
- use explicit `⟦…⟧` editorial markers for genuinely unresolved spans;
- `⟦…⟧` is not source punctuation or source wording;
- do **not** reconstruct blur from OCR, memory, grammar, metre, rhyme, historical context, likely wording, or another edition;
- do not silently normalize spelling, punctuation, sandhi, names, dates, numbers, or lineation;
- preserve visible speaker labels, poet introductions, performance notes, quotations, separators and page boundaries where legible;
- record only a **visibly printed** page numeral in `printed_page`; do not write an inferred number as if printed;
- pages with unresolved wording remain `needs-review`; do not promote them to `verified` during Phase 1.

Independent glyph-by-glyph resolution belongs to Phase 2, not this transcription pass.

## Cross-witness safeguard

This anthology includes works that already have separate source-specific witnesses in the repository, especially:

- `இதயத்தைத் தந்திடு அண்ணா!`;
- `தென்னவன் காதை`.

Those existing transcriptions are **not** authority for this 1995 anthology. Do not copy them into blurred spans, and do not harmonize punctuation/lineation/spelling between editions. Any later cross-edition comparison must be explicit and provenance-preserving.

The existing user-directed exclusion applicable to `தென்னவன் காதை` remains in force and must not be reintroduced through this anthology.

## Exact next activity

Execute **Phase 1 Batch 07 — physical scans 151–175**.

Create:

`poems/kalaignarin-kavithaigal/pages/0151.md` through `pages/0175.md`

Execution requirements:

- continue directly from unfinished `நீர்க் குடும்பம்` at scan 150;
- use the exact same 465-page controlling PDF identified by the SHA-256 above;
- render/inspect scans 151–175 directly from the source; do not depend on the old 150-page renderer window;
- preserve the conservative blur protocol;
- do not infer item boundaries—record only what the scans establish;
- do not begin Phase 2, Phase 3, canonical assembly, or translation in the same activity.

At Batch-07 completion:

- update `audit.md` with the new cumulative counts and discovered boundaries;
- extend `indexes/page-map.md` through scan 175;
- update the active work README;
- synchronize `HANDOVER.md` and `NEXT_CHAT_PROMPT.md` with the exact next 25-page Phase-1 batch;
- keep source metadata stable unless a genuine source-identity correction is discovered.

---

# Completed work — காலப் பேழையும் கவிதைச் சாவியும்

- Tamil archival/source layer: **FINAL-CLEARED**;
- English Phase 4: **COMPLETE — RELEASE-CLEARED — PASS**;
- canonical/English items: **58/58**;
- standalone English poem files: **58/58**;
- unresolved release issues: **0**.

Do not reopen this released work without explicit new scope or a genuine source-backed discrepancy.

---

# Paused work — தென்னவன் காதை

Tamil archival/source layer: **FINAL-CLEARED**; English translation partially complete and paused.

When explicitly resumed:

- next permitted batch: **EN-03 — scans 149–151 only**;
- then Gate C omission/speech review;
- preserve the documented user-directed omission exactly unless the user explicitly changes it.

The fact that `தென்னவன் காதை` appears inside the active anthology does not merge the two source witnesses.

---

# Completed work — இதயத்தைத் தந்திடு அண்ணா

- Tamil archival/source layer: **COMPLETE**;
- English translation: **RELEASE-COMPLETE**.

The fact that this poem appears inside the active anthology does not authorize copying the released standalone transcription into the anthology witness.

---

# General continuation rule

Live `main` is authoritative. Continue, do not duplicate. Preserve controlling-source evidence, phase/gate boundaries, exact source identity and user editorial controls. Never merge distinct printed witnesses merely because they contain the same titled work.