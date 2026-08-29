# Next Chat Prompt — காலப் பேழையும் கவிதைச் சாவியும்

Copy the prompt below into a fresh chat and attach the controlling PDF again when possible.

---

Continue the **Kalaignar Poems archival project** directly in:

`https://github.com/pugazg/kalaignar-poems`

Branch: `main`

Active work:

`poems/kaalap-pezhaiyum-kavithai-saaviyum/`

Controlling source:

`TVA_BOK_0063593_காலப்_பேழையும்_கவிதைச்_சாவியும்.pdf`

Work/title:

**காலப் பேழையும் கவிதைச் சாவியும்** — கலைஞர் மு. கருணாநிதி

Use the GitHub connector and work directly on `main`.

## IMPORTANT — LIVE MAIN IS AUTHORITATIVE

First fetch live GitHub `main` and treat it as authoritative.

The last work-state checkpoint before the handover-document refresh was:

`95d59d9c73f853ba8dbd0ab20cb9f25417784e34`

Commit:

`Record Kaalap Pezhai canonical assembly batch 1`

That SHA is only a checkpoint. The handover/guideline refresh itself creates later commits, and other work may also advance `main`. **Never reset or revert to this SHA. If live `main` is newer, continue from the newer state.**

## MANDATORY STARTUP

Before making any repository change, read completely:

1. `HANDOVER.md`
2. `POEM_PROCESSING_GUIDE.md`
3. `TRANSCRIPTION_PHASE_PLAN.md`
4. repository root `README.md`
5. `NEXT_CHAT_PROMPT.md`
6. `poems/kaalap-pezhaiyum-kavithai-saaviyum/README.md`
7. `poems/kaalap-pezhaiyum-kavithai-saaviyum/metadata/source.md`
8. `poems/kaalap-pezhaiyum-kavithai-saaviyum/indexes/page-map.md`
9. `poems/kaalap-pezhaiyum-kavithai-saaviyum/audit.md`
10. `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_STRUCTURE_AUDIT.md`
11. `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_BOUNDARY_JOIN_AUDIT.md`
12. `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_TITLE_WITNESS_RECONCILIATION.md`
13. `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_CANONICAL_ASSEMBLY.md`
14. all existing canonical files under `poems/kaalap-pezhaiyum-kavithai-saaviyum/sections/`, especially `01.md` through `06.md`
15. the verified `pages/NNNN.md` records needed for the next assembly range.

Inspect the attached controlling source as needed. Do not rely on OCR, semantic expectation or an outside edition as textual authority.

If any root/control document disagrees with the live work README or canonical-assembly record, use the newest live work-level evidence and source, then synchronize the stale document instead of restarting completed work.

## CURRENT DURABLE STATE

This work is in **Phase 3 — canonical Tamil assembly**.

Completed:

- Phase 1 transcription: **306/306 physical scans — COMPLETE**;
- Phase 2 source-critical visual verification: **306/306 — COMPLETE**;
- unresolved readings: **none**;
- exact physical scan ↔ printed-page reconciliation: **COMPLETE**;
- item boundary / page-join audit: **COMPLETE — 58/58 items certified**;
- closing boundary 299→300: **PASS**;
- title-witness reconciliation: **COMPLETE — 14/14 discrepancy cases reconciled**;
- canonical assembly iteration 1: **scans 10–34 — COMPLETE**;
- canonical files already created: **`sections/01.md` through `sections/06.md`**;
- cumulative canonical assembly: **6/58 items**.

Do **not** repeat transcription, Phase-2 verification, scan/page reconciliation, boundary/join auditing or title-witness reconciliation unless a genuine newly discovered source discrepancy requires a documented reopen.

## CANONICAL ASSEMBLY RULES

Canonical assembly is a merge from the verified page layer, not a new transcription.

1. Use only `verified` page records assigned to the certified item.
2. Preserve every verified source-supported spelling, punctuation mark, line break, quotation, separator, note and unusual form.
3. Preserve physical provenance with `<!-- scan_page: N -->` markers, following the exact pattern already used in `sections/01.md` through `sections/06.md`.
4. Use stable numeric filenames `01.md` … `58.md`.
5. Use the **title-page witness** as the canonical displayed title.
6. If contents/title witnesses differ, retain the contents witness separately in front matter. Never create a hybrid/normalized title.
7. Preserve stable item sequence 1–58 even where the source title-page number is anomalous. Item 37 remains item 37 although its title page prints number 36.
8. Work in **25-physical-scan iterations**.
9. If the iteration ends inside an item, **do not create a partial canonical item file**. Carry that item forward until its full certified source range is available.
10. Never silently smooth a source-level abrupt transition already certified by the join audit.
11. If assembly reveals a genuine problem in a verified page record, reopen and correct the source/page layer with audit history and revalidate affected assembly. Do not fix only the assembled file.
12. Do not begin assembly/source-completeness review until all 58 canonical item files exist.
13. Do not begin Phase 4 translation until Tamil final clearance.

## TITLE-WITNESS DISCREPANCIES

The completed reconciliation covers items:

**18, 22, 25, 26, 29, 31, 32, 37, 40, 44, 46, 50, 54 and 58.**

Read `PHASE3_TITLE_WITNESS_RECONCILIATION.md` before assembling any discrepant item. Preserve both witnesses exactly; title-page witness controls canonical display title only.

## EXACT NEXT ACTIVITY

Process the next **25 physical scans: 35–59** as canonical-assembly iteration 2.

Create these complete canonical files:

- item 7 — scans **35–39** → `sections/07.md`
- item 8 — scans **40–43** → `sections/08.md`
- item 9 — scans **44–49** → `sections/09.md`
- item 10 — scans **50–53** → `sections/10.md`
- item 11 — scans **54–57** → `sections/11.md`

Item 12 begins at scan **58** and continues through scan **63**. Because this 25-scan iteration ends at scan 59, **do not create `sections/12.md` yet**. Carry item 12 into the following iteration and publish it only once all scans 58–63 are included.

Before creating 07–11, inspect the existing canonical files 01–06 and the verified page records for scans 35–59. Preserve their exact source text and use the established front-matter/provenance structure.

After completing the iteration:

- update `PHASE3_CANONICAL_ASSEMBLY.md`;
- update the work `README.md`;
- synchronize any status-bearing document that becomes stale;
- report exactly which canonical files were created, cumulative assembly count, resulting live `main` SHA, and exact next 25-scan activity.

When I say **“Proceed with next activity”**, execute this next activity directly without asking me to choose a routine step.

---

## Textual authority reminder

The controlling scan and verified page records preserve source wording. Do not silently normalize Tamil spelling, grammar, punctuation, spacing, dates, historical names, repetitions, English/Latin material, lineation, source anomalies or title witnesses. OCR and outside sources are navigation/corroboration aids only.