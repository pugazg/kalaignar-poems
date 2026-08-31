# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Authority rule

**Treat live GitHub `main` as authoritative.** The controlling source scan remains the highest textual authority for Tamil wording unless a documented user instruction establishes another lexical/editorial control.

## Mandatory startup for every continuation

Before changing this repository in a fresh chat:

1. fetch live `main` and note current HEAD;
2. read `POEM_PROCESSING_GUIDE.md` completely;
3. read `TRANSCRIPTION_PHASE_PLAN.md` completely;
4. read root `README.md` and `NEXT_CHAT_PROMPT.md` completely;
5. read `poems/kalaignarin-kavithaigal/README.md`, `SOURCE_INTAKE.md`, `metadata/source.md`, `indexes/page-map.md`, and `audit.md` completely;
6. inspect `poems/kalaignarin-kavithaigal/pages/0001.md` before beginning Phase 2 and retain `pages/0465.md` as the end-of-source boundary record;
7. use the controlling PDF directly whenever transcription/verification requires source evidence;
8. never commit the source PDF or page-range access derivatives;
9. synchronize status-bearing files at each completed verification batch;
10. when the user says **“Proceed with next activity”**, execute the exact next routine operation recorded in live state.

# CURRENT ACTIVE WORK — கலைஞரின் கவிதைகள்

Work directory: `poems/kalaignarin-kavithaigal/`  
Author: **கலைஞர் மு. கருணாநிதி**  
Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

## Exact controlling-source identity

- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: **`19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`**;
- printed title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

### Renderer / access-derivative warning

An earlier interface exposed only pages 1–150; that is not the source length. Exact-byte inspection established **465 physical pages**.

The user supplied `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_001_pages_350-465.pdf`, a 116-page page-range access derivative. Its page 1 is original physical scan 350. It is **not a separate witness** and does not change the controlling-source identity. Batch 19 used derivative pages **102–116**, corresponding exactly to original physical scans **451–465**.

## Durable phase state at handoff

**PHASE 1 TRANSCRIPTION COMPLETE — all 465 physical scans have page records.**

- Phase 1 page records: **465/465**;
- files created: `pages/0001.md` through `pages/0465.md`;
- cumulative status after Phase 1: **10 `partial`, 455 `needs-review`, 0 `verified`**;
- completed Phase-1 batches: **01–19**;
- Phase 2 source-critical verification: **not started**;
- Phase 3 structure/assembly/final clearance: **not started**;
- English translation/release: **blocked until Tamil final clearance**.

Phase 1 completion means the page-record layer covers the complete source. It does **not** mean the Tamil text is verified or final-cleared.

## Final Phase-1 source/item boundaries

- `பகலவனாய்க் கிழக்கில் உதித்திடுவோம்!` continues from scan 450 and **closes 452 / printed 435**;
- `திசை திருப்பல் நியாயம்தானா?` — **453–454**, closes **454 / printed 437**;
- `நடந்து முடிந்ததம்மா; ஒரு நகைச்சுவை நாடகம்!` — **455–456**, closes **456 / printed 439**;
- `சில நாடுகள் இருக்கின்றன` — **457–460**, closes **460 / printed 443**;
- `உன் காலணியை வாழ்த்துகிறாய்` — **461–464**, closes **464 / printed 447**;
- scan **465** is the full-colour back cover and final physical scan.

## Durable blur / difficult-reading rule

Phase 1 preserved explicit `⟦…⟧` markers wherever the controlling scan did not safely support an exact reading. These markers are editorial and are not source text. Do not resolve them from OCR, memory, grammar, metre, rhyme, historical context, likely wording, or another edition.

During Phase 2, independently reread the source itself. Correct a page only when the scan supports the correction. Promote a page to `verified` only after word/glyph, punctuation, lineation, quotation, separator and non-Tamil material all pass direct visual review.

## Cross-witness safeguard

Do not copy separate source-witness transcriptions into this anthology. The existing user-directed exclusion applicable to `தென்னவன் காதை` remains in force.

## Other repository work states to preserve

- `காலப் பேழையும் கவிதைச் சாவியும்` — Tamil FINAL-CLEARED; English RELEASE-CLEARED; 58/58 items;
- `தென்னவன் காதை` — Tamil FINAL-CLEARED; English translation paused;
- `இதயத்தைத் தந்திடு அண்ணா` — Tamil COMPLETE; English RELEASE-COMPLETE.

## EXACT NEXT ACTIVITY

Begin **Phase 2 Verification Batch 01 — physical scans 1–25**.

For each scan 1–25:

- independently reread the controlling scan rather than trusting the Phase-1 wording;
- compare every glyph/word ending, punctuation mark, line break, quotation mark, separator and non-Tamil element;
- use enlarged crops/non-destructive rendering where needed;
- resolve `⟦…⟧` only when the controlling scan supports an exact reading;
- preserve old Tamil forms and source anomalies without normalization;
- promote a page to `verified` only if the complete page passes; otherwise leave it `partial`/`needs-review` with explicit unresolved notes.

At completion synchronize all status-bearing files to **Phase 2 Verification Batch 02 — scans 26–50**. Do **not** begin Phase 3, canonical assembly or translation in the same activity.
