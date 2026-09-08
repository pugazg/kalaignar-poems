# HANDOVER — Kalaignar Poems Archive

Repository: `pugazg/kalaignar-poems`, branch `main`. **Live main is authoritative.**

## Current active lane — Bharathiar University secondary witnesses

No new Tamil poem is staged. Four 2009 Bharathiar University / Macmillan English-translation books are onboarded under `secondary-witnesses/bharathiar-university/`.

Exact witness set:

- BU-SP1 — *Shower of Poetry*, Volume I — **249 pages / 101,936,284 bytes / SHA-256 `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536`**;
- BU-SP2 — *Shower of Poetry*, Volume II — **168 pages / 156,922,680 bytes / SHA-256 `e29c294adfe94c508cdb8aeb4f8cadf116b8dc1bdeb4025eef86a7a017f02a31`**;
- BU-SP3 — *Shower of Poetry*, Volume III — **220 pages / 80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6`**;
- BU-TT — *The Treasure Trove of Time and the Verse Key* — **205 pages / 106,152,046 bytes / SHA-256 `17ecd31500ad67ec34d684a8c2d0d208866fd5bca3f630a2941c50baa3b86d4b`**.

Renderer warning: Volumes I, III and BU-TT may expose only 150 pages through a renderer; exact-byte counts above control.

Initial crosswalk: **176 entries = 55 MATCHED / 3 POSSIBLE / 39 NOT YET REPRESENTED / 79 INVESTIGATE**.

Witness authority:

1. historical Tamil controlling source;
2. FINAL-CLEARED repository Tamil canonical;
3. Bharathiar University English translation as a secondary interpretive/editorial witness.

These books must not silently modify Tamil or RELEASE-CLEARED English.

## Comparison Batch 1 — COMPLETE

`secondary-witnesses/bharathiar-university/comparisons/01-thalaikettan-thambi.md`

`தலைகேட்டான் தம்பி` vs BU-SP2 item 17: **PASS / REPORT-ONLY**. Tamil/source corrections **0**; released-English changes **0**. Two strong source-supported future English review candidates were recorded. The work remains CLOSED / RELEASE-CLEARED.

## Comparison Batch 2 — COMPLETE

`secondary-witnesses/bharathiar-university/comparisons/02-treasure-trove-items-01-10.md`

BU-TT entries **1–10** vs repository items **1, 2, 5, 6, 11, 17, 19, 20, 21, 22**: **PASS / REPORT-ONLY**, 10/10 compared, Tamil/source corrections **0**, released-English corrections **0**, mutations **0 / 0**.

Key Batch-2 guardrails: BU entry 6 truncates item 17; BU entry 4's negative Stone-Age interpretation does not override verified `காணமுடியக்`; BU entry 10's “ignorant look” does not override verified `அரியா நோக்கு`.

## Comparison Batch 3 — COMPLETE

`secondary-witnesses/bharathiar-university/comparisons/03-treasure-trove-items-11-20.md`

Scope: BU-TT entries **11–20**, physical PDF pages **75–122** / printed pages **45–92**, mapped to repository items **23, 24, 26, 29, 31, 32, 35, 36, 37 and 38**.

Result: **PASS / REPORT-ONLY**.

- items compared: **10/10**;
- Tamil/source transcription correction candidates: **0**;
- source-supported released-English correction candidates: **0**;
- title replacements: **0**;
- Tamil / released-English changes: **0 / 0**.

Key findings:

- item 31 is a verified **source title/body anomaly**: title `மாண்பு நிறை தாயும் மாசற்ற மகனும்!` says son, but the verified closing body says `மாண்பு நிறை தாய் மகள் வரலாறு`; Bharathiar's **An Honourable Mother and an Upright Daughter** is a later editorial harmonization, not proof of a transcription error;
- BU entry 18 **A Young Lady, She is a Tamil Lady!** is an editorial retitle toward Anni Minjili; source item 36 remains `இளையவன்; அவன் ஒரு தமிழ் மகன்!`;
- BU entry 13's **winnowing fan** cannot override FINAL-CLEARED `முரசு கொண்டு புலி விரட்டிய தமிழச்சி`; repository **war-drum** remains correct for this edition;
- BU entry 16's **the Head That Hung** is a weaker fit for source `குனிந்திடும்`; repository **Heads Bow Down** is retained;
- dominant pattern remains smoothing, condensation, transliteration differences and occasional editorial retitling.

No release-cleared item was reopened.

## Exact next activity

Proceed with **Secondary Witness Comparison Batch 4 — BU-TT entries 21–30**, mapped to repository items **39, 40, 44, 45, 46, 47, 49, 50, 51 and 52**.

Inspect exact BU pages, compare against FINAL-CLEARED Tamil and RELEASE-CLEARED English, and write **report only**. Do not mutate Tamil or released English without a separate documented source-backed reopen.

After Batch 4, process final BU-TT entries **31–34** as Batch 5.

## Release-cleared work remains frozen

`poems/thalaikettan-thambi/`, `poems/aanthaiyum-arasanum/` and all other completed poem workspaces remain closed unless genuinely new source-backed evidence justifies a documented reopen.
