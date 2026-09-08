# HANDOVER — Kalaignar Poems Archive

Repository: `pugazg/kalaignar-poems`, branch `main`. **Live main is authoritative.**

## Current active lane — Bharathiar University secondary witnesses

No new Tamil poem is staged. The user supplied four 2009 Bharathiar University / Macmillan English-translation books, now onboarded under:

`secondary-witnesses/bharathiar-university/`

Exact witness set:

- BU-SP1 — *Shower of Poetry*, Volume I — **249 pages / 101,936,284 bytes / SHA-256 `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536`**;
- BU-SP2 — *Shower of Poetry*, Volume II — **168 pages / 156,922,680 bytes / SHA-256 `e29c294adfe94c508cdb8aeb4f8cadf116b8dc1bdeb4025eef86a7a017f02a31`**;
- BU-SP3 — *Shower of Poetry*, Volume III — **220 pages / 80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6`**;
- BU-TT — *The Treasure Trove of Time and the Verse Key* — **205 pages / 106,152,046 bytes / SHA-256 `17ecd31500ad67ec34d684a8c2d0d208866fd5bca3f630a2941c50baa3b86d4b`**.

Renderer warning: Volumes I, III and BU-TT currently expose only 150 pages through the renderer, but exact-byte PDF inspection establishes the longer physical counts above. Never treat 150 as their source-file length.

`secondary-witnesses/bharathiar-university/MASTER_CROSSWALK.md` indexes all **176** TOC entries:

- **55 MATCHED**;
- **3 POSSIBLE**;
- **39 NOT YET REPRESENTED**;
- **79 INVESTIGATE**.

Witness authority rule:

1. historical Tamil controlling source;
2. FINAL-CLEARED repository Tamil canonical;
3. Bharathiar University English translation as a secondary interpretive/editorial witness.

These books must not silently modify Tamil or RELEASE-CLEARED English.

Confirmed high-value relationships:

- BU-SP2 item 17 `Thalai Keettaan Thambi! / The Brother for the Head did Ask!` → `poems/thalaikettan-thambi/`; supplied Volume-II physical pages **85–89**. It is a later `Sangath Thamizh` witness, not authority over the 1966 Murasoli source.
- BU-SP1 has **20 MATCHED + 3 POSSIBLE** relationships, primarily into `poems/kalaignarin-kavithaigal/`; see its crosswalk.
- BU-TT is a book-level secondary witness to `poems/kaalap-pezhaiyum-kavithai-saaviyum/`; **34/34** translated TOC entries map to stable repository items.
- BU-SP3 remains **50/50 INVESTIGATE** pending item-level matching.

## Exact next activity

Perform **Secondary Witness Comparison Batch 1 — `தலைகேட்டான் தம்பி`**:

1. read `secondary-witnesses/bharathiar-university/README.md`, `MASTER_CROSSWALK.md`, BU-SP2 `source.md` and `crosswalk.md`;
2. compare Bharathiar University Volume-II PDF pages **85–89** against FINAL-CLEARED repository Tamil `poems/thalaikettan-thambi/sections/01.md` and RELEASE-CLEARED English;
3. classify differences: title, interpretation, omission/condensation, expansion, names/transliteration, structure, or possible mistranslation;
4. write a **comparison report only**;
5. do not alter Tamil or released English during the comparison batch;
6. any later English revision requires a separate source-backed reopen proving that the controlling Tamil supports the change.

After Batch 1, process the 34 mapped BU-TT items in controlled comparison batches.

## Release-cleared work remains frozen

### தலைகேட்டான் தம்பி (1966)

`poems/thalaikettan-thambi/` — **CLOSED / RELEASE-CLEARED — 2026-09-08**. Tamil canonical blob `fcf3ed8c3d2e8af90c8c4ea06a506ef5b4ae9d0f`; reviewed English blob `008a4a50678fe69d3dd90165ac10e34f1145e88f`; reader-facing blob `4dacd0819bb510a795ca034ce8fefec02133b259`. Unresolved issues 0.

### ஆந்தையும் அரசனும்! (1965)

`poems/aanthaiyum-arasanum/` — **CLOSED / RELEASE-CLEARED — 2026-09-07**. Do not reopen without genuinely new source-backed evidence.

Other preserved release-cleared work includes `poomudi`, `anna-kaviyarangam`, `gunanayagar-nehru`, `oruthalaik-kathal`, `kalaignarin-kavithaigal`, `kalaignarin-kaviyaranga-kavithaigal-1975`, and `kanchithan-annan`.
