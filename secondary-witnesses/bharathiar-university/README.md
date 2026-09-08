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

The current page renderer may expose only **150 pages** for Volumes I, III and *Treasure Trove*. Exact-byte PDF inspection establishes their real physical lengths as **249, 220 and 205 pages** respectively. For BU-TT Batch 4, physical pages **151–174** were inspected by direct rendering from the same checksum-locked PDF bytes; no OCR reconstruction was used.

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
Correction addendum: `comparisons/03A-item31-title-correction.md`.

Compared supplied BU-TT physical PDF pages **75–122** / printed pages **45–92** with repository items **23, 24, 26, 29, 31, 32, 35, 36, 37 and 38**.

Original result was report-only. One later **source-backed correction** supersedes the original item-31 title conclusion:

- contents witness remains **`மாண்பு நிறை தாயும், மாசற்ற மகனும்!`**;
- direct poem-opening scan 148 visibly reads **`மாண்பு நிறை தாயும் மாசற்ற மகளும்!`**;
- repository title policy gives the direct poem-page witness canonical authority;
- stable item 31 is therefore corrected to **`மாண்பு நிறை தாயும் மாசற்ற மகளும்!` / The Mother Full of Dignity and the Stainless Daughter!**;
- BU entry 15 **An Honourable Mother and an Upright Daughter** is reclassified as corroborating secondary evidence, not as an editorial emendation;
- the item body/close concerning Madhavi and Manimekalai (`தாய் மகள் வரலாறு`) corroborates the correction but was not the textual authority for it.

Other Batch-3 findings remain: BU's `winnowing fan` substitution does not override verified `முரசு`, and the protagonist-oriented female retitle of item 36 does not override source title `இளையவன்; அவன் ஒரு தமிழ் மகன்!`.

### Batch 4 — BU-TT entries 21–30

Report: `comparisons/04-treasure-trove-items-21-30.md`.

Compared BU-TT printed pages **93–144** / supplied PDF physical pages **123–174** with repository items **39, 40, 44, 45, 46, 47, 49, 50, 51 and 52**.

Result: **PASS / REPORT-ONLY**.

- items compared: **10/10**;
- Tamil/source correction candidates: **0**;
- source-supported released-English correction candidates: **0**;
- title replacements: **0**;
- Tamil / released-English mutations: **0 / 0**.

High-value findings:

- BU entry 21 omits repository item 39's closing *Periya Puranam* / Sekkizhar campaign quotation;
- BU entry 23 singularizes source `ஈக்களின்` as **a Fly**, while the source-controlled repository correctly retains **Flies**;
- BU entry 26's **Future Dear** is weaker than source `அருங்காலம்`; repository **Precious Age** remains closer;
- BU entry 30 materially truncates repository item 52 after the Golden-Handed Pandyan episode, omitting the later Pandya list, *Tolkappiyam* presentation and transition to the Pandya-history continuation;
- the dominant pattern remains smoothing, condensation, transliteration and interpretive title wording rather than repository defects.

## Source-backed item-31 reopen

Primary work-level record: `poems/kaalap-pezhaiyum-kavithai-saaviyum/POST_RELEASE_ITEM31_TITLE_CORRECTION.md`.

This correction is intentionally narrow: **title only**. It changes no narrative/body wording, scan boundaries or stable item identity. The contents `மகனும்` witness is retained exactly; the canonical/title-page layer uses `மகளும்`.

## High-value established relationships

- BU-SP2 item 17 → `poems/thalaikettan-thambi/` as a later `Sangath Thamizh` English translation witness.
- Volume I contains numerous selections already represented in `poems/kalaignarin-kavithaigal/`.
- *The Treasure Trove of Time and the Verse Key* is a direct **book-level secondary witness** to `poems/kaalap-pezhaiyum-kavithai-saaviyum/`; its 34 TOC entries map to stable repository items.

### Batch 5 — BU-TT entries 31–34 — COMPLETE

Report: `comparisons/05-treasure-trove-items-31-34.md`.

Compared BU-TT entries **31–34** with repository items **53, 55, 56 and 57**. Result: **PASS / REPORT-ONLY — 4/4**, Tamil/source correction candidates **0**, released-English correction candidates **0**, mutations **0 / 0**. High-value findings: entry 31 modernizes `கடற்கோள்` to **tsunami**, converts `எழுபது காதம்` to **seven hundred miles** and omits the final historical-source note; entry 32 omits item 55's complete opening Pandya/Sangam prelude and closing source note; entry 33 narrows `பற்று` to **love**; entry 34 modernizes source-position `கானப்பேர் கோயில்` to Kalaiyar Koyil and compresses the title's `அழகு`.

### BU-TT consolidated closure — COMPLETE 34/34

Consolidated report: `comparisons/TREASURE_TROVE_34_ENTRY_SUMMARY.md`. All **34/34** BU-TT translations have been compared. Apart from the separately source-verified item-31 title correction, the lane established **0 Tamil body corrections and 0 other released-English mutations**. The dominant Bharathiar pattern is condensation/smoothing, scholarly transliteration, interpretive retitling and occasional modernization rather than repository textual defects.

## Next activity

Proceed with **BU-SP1 identity hardening** for the three current `POSSIBLE` rows before broad Volume-I payload comparison:

1. entry 8 **The Beloved Son of the Muse of Arts** → possible `poems/kalaignarin-kavithaigal/` item 40;
2. entry 18 **Calculation - 1** → possible item 18;
3. entry 43 **Calculation-2** → possible item 18.

Compare payloads and classify each as MATCHED / distinct work or segment / not a match. This is identity/crosswalk work only; no Tamil or released-English mutation is authorized by the matching step.
