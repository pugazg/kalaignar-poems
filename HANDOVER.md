# HANDOVER — Kalaignar Poems Archive

Repository: `pugazg/kalaignar-poems`, branch `main`. Live `main` is authoritative.

## Active source

`TVA_BOK_0064169_கலைஞரின்_கவியரங்கக்_கவிதைகள்.pdf` — **84 scans**, **93,307,011 bytes**, SHA-256 `d9b70fd65f913c2c4377c25675e115555987bb9d9a4c22681b13ebae98afd168`.

## User-directed processing policy

Process only poems not already represented in the repository. Skip duplicate ranges **9–20, 21–32, 33–45, 71–77, 78–84**. Scan 66 is Rajaji source/context; scans 69–70 are Bharathidasan material.

## Durable Tamil checkpoint

- Item 01 scans **46–57** — `sections/01.md` — **TAMIL FINAL-CLEARED**;
- Item 02 scans **58–65** — `sections/02.md` — **TAMIL FINAL-CLEARED**;
- Item 04 scans **67–68** — `sections/04.md` — **TAMIL FINAL-CLEARED**;
- Phase 1: **22/22 complete**;
- Phase 2: **22/22 verified**;
- Phase 3 Gates 1–6: **COMPLETE / PASS**;
- final-clearance authority: `poems/kalaignarin-kaviyaranga-kavithaigal-1975/PHASE3_TAMIL_FINAL_CLEARANCE.md`;
- canonical payload equality: **22/22 PASS**;
- unresolved Tamil source/canonical defects: **0**;
- canonical manifest SHA-256: `52d0c105cf8d6b14ae87bee871583d2b47d6aa32dabb3b0f2514633592d667e7`.

## Phase 4 checkpoint

**IN PROGRESS — Batch 01 reviewed PASS / 1/3 batches / Batch 02 NEXT.**

Controls:

1. `poems/kalaignarin-kaviyaranga-kavithaigal-1975/translations/en/README.md`
2. `poems/kalaignarin-kaviyaranga-kavithaigal-1975/translations/en/TRANSLATION_PLAN.md`
3. `poems/kalaignarin-kaviyaranga-kavithaigal-1975/translations/en/SOURCE_MAP.md`

Normal translation source is the Tamil final-cleared canonical item. If a Tamil reading is questioned: controlling scan → verified page record → final-cleared canonical section → Phase-3 records.

Batch partition / progress:

- **Batch 01** — Item 01 — scans **46–57** — `translations/en/sections/01.md` — **REVIEWED PASS**;
- **Batch 02** — Item 02 — scans **58–65** — **NEXT**;
- **Batch 03** — Item 04 — scans **67–68** — planned.

Batch-01 durable review:

- English item blob: `4dfbb95c099108398eeccd6bfb368e34d7db2ee0`;
- review record: `translations/en/batches/batch-01.md`;
- source scans / markers: **12/12**, unique and in physical order;
- scan **50→51** source-open quotation state: preserved;
- scan **57** closing separator: structurally preserved;
- `குடி`, `கல்லக்குடி / கள்ளக்குடி`, `பருக்கிடம்`, `சாரம்`, `விணுக்குறியா?`, `ரசவாதம் / அதிரசவாதம்`, `சுருட்டு / புரட்டு` decisions: recorded;
- Bharathi/Bharathidasan quotations translated from the final-cleared witness, not outside English editions;
- omissions / duplications: **0 / 0**;
- unresolved Batch-01 translation issues: **0**;
- Tamil page/canonical changes during Phase 4: **0**.

Source-sensitive locks still pending include Item-02 `மை` wordplay chain and Item-04 direct-title/context distinction plus `சுதந்திராக்கள்`.

## Exact next activity

Perform **Phase 4 Batch 02 — Item 02 only, scans 58–65**. Draft `translations/en/sections/02.md` from final-cleared `sections/02.md`, preserve all **8/8** scan markers and the `மை` wordplay chain, source-review the complete item, and create `translations/en/batches/batch-02.md` as the decision/review record.

Do not start Batch 03 in the same activity.

Existing release-cleared poem trees remain untouched.