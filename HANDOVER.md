# HANDOVER — Kalaignar Poems Archive

Repository: `pugazg/kalaignar-poems`, branch `main`. **Live main is authoritative.**

## Current active lane — Bharathiar University secondary witnesses

No new Tamil poem is staged. Four 2009 Bharathiar University / Macmillan English-translation books are onboarded under `secondary-witnesses/bharathiar-university/`.

Exact witness set:

- BU-SP1 — *Shower of Poetry*, Volume I — **249 pages / 101,936,284 bytes / SHA-256 `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536`**;
- BU-SP2 — *Shower of Poetry*, Volume II — **168 pages / 156,922,680 bytes / SHA-256 `e29c294adfe94c508cdb8aeb4f8cadf116b8dc1bdeb4025eef86a7a017f02a31`**;
- BU-SP3 — *Shower of Poetry*, Volume III — **220 pages / 80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6`**;
- BU-TT — *The Treasure Trove of Time and the Verse Key* — **205 pages / 106,152,046 bytes / SHA-256 `17ecd31500ad67ec34d684a8c2d0d208866fd5bca3f630a2941c50baa3b86d4b`**.

Renderer warning: BU-TT may expose only 150 pages in the conversation renderer. For Batch 4, physical pages **151–174** were inspected by direct rendering from the exact checksum-locked PDF bytes; no OCR reconstruction was used.

Initial crosswalk: **176 entries = 55 MATCHED / 3 POSSIBLE / 39 NOT YET REPRESENTED / 79 INVESTIGATE**.

Witness authority:

1. historical Tamil controlling source;
2. FINAL-CLEARED repository Tamil canonical;
3. Bharathiar University English translation as a secondary interpretive/editorial witness.

These books must not silently modify Tamil or RELEASE-CLEARED English.

## Comparison Batch 1 — COMPLETE

`comparisons/01-thalaikettan-thambi.md` — `தலைகேட்டான் தம்பி` vs BU-SP2 item 17: **PASS / REPORT-ONLY**. Tamil/source corrections **0**; released-English changes **0**. Two strong source-supported future English review candidates were recorded.

## Comparison Batch 2 — COMPLETE

`comparisons/02-treasure-trove-items-01-10.md` — BU-TT entries **1–10** vs repository items **1, 2, 5, 6, 11, 17, 19, 20, 21, 22**: **PASS / REPORT-ONLY**, 10/10 compared, mutations **0 / 0**.

## Comparison Batch 3 — COMPLETE

`comparisons/03-treasure-trove-items-11-20.md` — BU-TT entries **11–20** vs repository items **23, 24, 26, 29, 31, 32, 35, 36, 37, 38**: **PASS / REPORT-ONLY**, 10/10 compared, mutations **0 / 0**.

Important durable findings: item 31 source title/body anomaly (`மகனும்` title vs `தாய் மகள்` body), BU `winnowing fan` rejected against verified `முரசு`, and BU female retitle of item 36 rejected against source `இளையவன்; அவன் ஒரு தமிழ் மகன்!`.

## Comparison Batch 4 — COMPLETE

`secondary-witnesses/bharathiar-university/comparisons/04-treasure-trove-items-21-30.md`

Scope: BU-TT entries **21–30**, printed pages **93–144**, supplied PDF physical pages **123–174**, mapped to repository items **39, 40, 44, 45, 46, 47, 49, 50, 51 and 52**.

Result: **PASS / REPORT-ONLY**.

- items compared: **10/10**;
- Tamil/source correction candidates: **0**;
- source-supported released-English correction candidates: **0**;
- title replacements: **0**;
- Tamil / released-English mutations: **0 / 0**.

Key findings:

- BU entry 21 omits repository item 39's final *Periya Puranam* / Sekkizhar Vatapi-campaign quotation;
- BU entry 23 singularizes source `ஈக்களின்` as **a Fly**; repository **Flies** remains source-controlled;
- BU entry 26's **Future Dear** is weaker than source `அருங்காலம்`; repository **Precious Age** remains closer;
- BU entry 30 materially truncates item 52 after the Golden-Handed Pandyan episode, omitting the later Pandya list, *Tolkappiyam* presentation and closing transition;
- dominant pattern continues to be smoothing, condensation, transliteration and interpretive retitling rather than repository defects.

No release-cleared item was reopened.

## Exact next activity

Proceed with **Secondary Witness Comparison Batch 5 — final BU-TT entries 31–34**, mapped to repository items **53, 55, 56 and 57**.

Inspect exact BU pages, compare against FINAL-CLEARED Tamil and RELEASE-CLEARED English, and write **report only**. After Batch 5, create a consolidated **34/34 BU-TT comparison summary** before moving to another secondary-witness lane.

## Release-cleared work remains frozen

`poems/thalaikettan-thambi/`, `poems/aanthaiyum-arasanum/` and all other completed poem workspaces remain closed unless genuinely new source-backed evidence justifies a documented reopen.
