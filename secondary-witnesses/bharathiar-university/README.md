# Bharathiar University English Translation Witnesses

This directory records four 2009 Bharathiar University / Macmillan English-translation books supplied by the user as **institutional secondary witnesses**.

## Witness hierarchy

1. **Controlling historical Tamil scan** — highest authority for Tamil transcription.
2. **FINAL-CLEARED repository Tamil canonical** — authority for repository English translation.
3. **Bharathiar University / Macmillan 2009 English books** — secondary interpretive/editorial witnesses.

These books may help with meaning, person/place identification, Sangam references, title choices and translation review. They must **not** silently change a verified Tamil page, canonical Tamil, or release-cleared English. A later change requires a documented comparison showing that the controlling Tamil supports the change.

## Four-book set

| Witness | Exact physical pages | Bytes | SHA-256 | Translator | TOC entries |
|---|---:|---:|---|---|---:|
| *Shower of Poetry*, Volume I | 249 | 101,936,284 | `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536` | R. Ganapathy | 52 |
| *Shower of Poetry*, Volume II | 168 | 156,922,680 | `e29c294adfe94c508cdb8aeb4f8cadf116b8dc1bdeb4025eef86a7a017f02a31` | R. Ganapathy | 40 |
| *Shower of Poetry*, Volume III | 220 | 80,185,514 | `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` | V. Murugan | 50 |
| *The Treasure Trove of Time and the Verse Key* | 205 | 106,152,046 | `17ecd31500ad67ec34d684a8c2d0d208866fd5bca3f630a2941c50baa3b86d4b` | P. Marudanayagam | 34 |

All four were edited by **P. Marudanayagam and V. Murugan**, issued by **Bharathiar University, Coimbatore**, with **Macmillan Publishers India Ltd**, first published **2009**.

## Renderer-limit note

The current page renderer may expose only **150 pages** for Volumes I, III and *Treasure Trove*. Exact-byte PDF inspection establishes their real physical lengths as **249, 220 and 205 pages** respectively. The 150-page renderer value is a tooling window, not source-file length.

## Crosswalk state

The four contents witnesses contain **176 translated entries**:

- Volume I: **52** — 20 MATCHED / 3 POSSIBLE / 29 INVESTIGATE;
- Volume II: **40** — 1 MATCHED / 39 NOT YET REPRESENTED;
- Volume III: **50** — 50 INVESTIGATE;
- *Treasure Trove*: **34** — 34 MATCHED.

Overall initial onboarding: **55 MATCHED / 3 POSSIBLE / 39 NOT YET REPRESENTED / 79 INVESTIGATE = 176**.

See `MASTER_CROSSWALK.md` and the per-book crosswalks.

## Completed comparisons

### Batch 1 — `தலைகேட்டான் தம்பி`

Report: `comparisons/01-thalaikettan-thambi.md`.

Result: **PASS / REPORT-ONLY**. Tamil/source correction candidates **0**; released English changes **0**; two strong future English review candidates, one medium refinement and one low editorial refinement were recorded. `poems/thalaikettan-thambi/` remains CLOSED / RELEASE-CLEARED.

### Batch 2 — BU-TT entries 1–10

Report: `comparisons/02-treasure-trove-items-01-10.md`.

Compared supplied BU-TT physical PDF pages **31–74** / printed pages **1–44** with stable repository items **1, 2, 5, 6, 11, 17, 19, 20, 21 and 22**.

Result: **PASS / REPORT-ONLY** — 10/10 compared, Tamil/source corrections **0**, released-English corrections **0**, text mutations **0 / 0**. Dominant pattern: smoothing, condensation and transliteration differences. Major preserved findings include BU entry 6 truncating repository item 17, BU entry 4's negative Stone-Age normalization conflicting with verified `காணமுடியக்`, and BU entry 10's `ignorant look` conflicting with verified `அரியா நோக்கு`.

### Batch 3 — BU-TT entries 11–20

Report: `comparisons/03-treasure-trove-items-11-20.md`.

Compared supplied BU-TT physical PDF pages **75–122** / printed pages **45–92** with repository items **23, 24, 26, 29, 31, 32, 35, 36, 37 and 38**.

Result: **PASS / REPORT-ONLY**.

- items compared: **10/10**;
- Tamil/source transcription correction candidates: **0**;
- source-supported released-English correction candidates: **0**;
- title replacements: **0**;
- Tamil / released-English changes: **0 / 0**.

High-value findings:

- item 31 is a genuine **source title/body anomaly**: verified title `மாண்பு நிறை தாயும் மாசற்ற மகனும்!` says **son**, while the verified body closes with `மாண்பு நிறை தாய் மகள் வரலாறு`; Bharathiar's **An Honourable Mother and an Upright Daughter** is a later editorial harmonization, not evidence that the source title was mistranscribed;
- BU entry 18 **A Young Lady, She is a Tamil Lady!** is a later protagonist-oriented retitling; verified source item 36 remains `இளையவன்; அவன் ஒரு தமிழ் மகன்!`;
- BU entry 13 says a Tamil woman drove away a tiger with a **winnowing fan**, but FINAL-CLEARED scan 130 explicitly reads `முரசு கொண்டு புலி விரட்டிய தமிழச்சி`; repository **war-drum** remains source-controlled;
- BU entry 16 **the Head That Hung** is a weaker fit for source `குனிந்திடும்`; repository **Heads Bow Down** is retained;
- structural condensation remains recurrent across all ten entries.

No release-cleared item was reopened.

## High-value established relationships

- BU-SP2 item 17 → `poems/thalaikettan-thambi/` as a later `Sangath Thamizh` English translation witness.
- Volume I contains numerous selections already represented in `poems/kalaignarin-kavithaigal/`.
- *The Treasure Trove of Time and the Verse Key* is a direct **book-level secondary witness** to `poems/kaalap-pezhaiyum-kavithai-saaviyum/`; its 34 TOC entries map to stable repository items.

## Next activity

Perform **Secondary Witness Comparison Batch 4 — BU-TT mapped entries 21–30**, corresponding to repository items **39, 40, 44, 45, 46, 47, 49, 50, 51 and 52**.

Continue report-only. No comparison batch may directly mutate Tamil or released English without a separate documented source-backed decision. After Batch 4, process the final BU-TT entries **31–34** as Batch 5.
