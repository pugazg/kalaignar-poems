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

- Volume I: **52** — 33 MATCHED / 0 POSSIBLE / 19 NOT YET REPRESENTED / 0 INVESTIGATE;
- Volume II: **40** — 1 MATCHED / 39 NOT YET REPRESENTED;
- Volume III: **50** — 0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE — identity CLOSED;
- *Treasure Trove*: **34** — 34 MATCHED.

Current hardened crosswalk: **68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE = 176 — 176/176 identity-classified**.

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

### BU-SP1 identity hardening — COMPLETE

Report: `comparisons/06-shower-of-poetry-vol-1-identity-hardening.md`. Result: **3/3 former POSSIBLE rows resolved** — entry 8 MATCHED item 40; entry 18 MATCHED item 18; entry 43 is a distinct 1995 Pongal/Sun TV work and is NOT item 18, so it remains INVESTIGATE for repository representation. Mutations: **0 / 0**.

### BU-SP1 payload comparison Batch 1 — COMPLETE

Report: `comparisons/07-shower-of-poetry-vol-1-matched-batch-01.md`.

Compared confirmed MATCHED entries **1, 8, 9, 11, 12, 13, 14, 15, 16 and 18** against FINAL-CLEARED Tamil and RELEASE-CLEARED English. Result: **PASS / REPORT-ONLY — 10/10**; Tamil/source correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**.

High-value diagnostics: BU entry 1 mistranslates `பஞ்சைகளல்ல` as **cowards** rather than paupers and inserts **tricks and frauds** into the opening; entry 8 flattens the `Nalla Thambi / Panam / Manamagal` film-title chain and reads source `கிந்தன்` as **Kandan**; entry 13 omits the extended river-name love sequence; entry 14 heavily condenses the water-family architecture; entry 15 omits the Muthusamy → Muthamma dream sequence; entry 18 mistranslates `மணக்கணக்கு` as **mental calculation**, `வேங்கை` as **lion**, and source river multiplication as multiplying **rains**. These are secondary-witness weaknesses, not repository defects.

### BU-SP1 payload comparison Batch 2 — COMPLETE

Report: `comparisons/08-shower-of-poetry-vol-1-matched-batch-02.md`.

Compared confirmed MATCHED entries **19, 21, 22, 23, 25, 26, 27, 28, 30 and 33** against FINAL-CLEARED Tamil and RELEASE-CLEARED English. Result: **PASS / REPORT-ONLY — 10/10**; Tamil/source correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**.

High-value diagnostics: BU entry 19 omits the long Nehru/Rose flower-garden allegory; entry 21 mistranslates source `பொன்விழா` as **Diamond Jubilee** and carries an impossible **10-08-1922** Silver-Jubilee footnote date; entry 25 heavily condenses the Silappathikaram/Tolkappiyam/abhinaya architecture; entry 26 mistranslates `ஆத்திகம்` as **agnosticism** and omits the Kamban/Ravana plus Anna-work-title chain; entry 28 gives **07-11-1980** where the controlling Tamil opening is **7.1.80**. These are secondary-witness defects/condensations, not repository defects.

### BU-SP1 payload comparison Batch 3 — COMPLETE

Report: `comparisons/09-shower-of-poetry-vol-1-matched-batch-03.md`.

Compared the final confirmed MATCHED entries **39 and 40** against FINAL-CLEARED Tamil and RELEASE-CLEARED English using direct renders of exact Volume-I physical pages **194–198**. Result: **PASS / REPORT-ONLY — 2/2**; Tamil/source correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**. Strong diagnostics: entry 39 `பவள விழா` → BU **Platinum Jubilee** and source **1929** → BU **1928**, with Ayyappan / `பொய்யப்பா` wordplay flattened; entry 40 `வெல்லம்` → BU **sugar cane** and `அர்ச்சனைகள்` → BU **censure**, reversing the source's ritual-praise sense.

### BU-SP1 confirmed-MATCHED payload lane — COMPLETE 22/22

Consolidated summary: `comparisons/SHOWER_OF_POETRY_VOL_1_22_MATCHED_SUMMARY.md`. All **22/22** confirmed MATCHED Volume-I entries are payload-compared. Across the lane, Tamil/source corrections **0**, released-English corrections **0**, title replacements **0**, mutations **0 / 0**. This 22/22 payload count is historical to the matches known at that stage; later identity work expands the identity classification without retroactively expanding this payload lane.

### BU-SP1 identity investigation Batches 1–3 — COMPLETE / IDENTITY CLOSED 52/52

- Batch 1: `comparisons/10-shower-of-poetry-vol-1-identity-investigation-batch-01.md` — **7 MATCHED / 3 NOT YET REPRESENTED**.
- Batch 2: `comparisons/11-shower-of-poetry-vol-1-identity-investigation-batch-02.md` — **3 MATCHED / 7 NOT YET REPRESENTED**.
- Batch 3: `comparisons/12-shower-of-poetry-vol-1-identity-investigation-batch-03.md` — **1 MATCHED / 9 NOT YET REPRESENTED**, final ten rows resolved.
- Final BU-SP1 identity state: **33 MATCHED / 0 POSSIBLE / 19 NOT YET REPRESENTED / 0 INVESTIGATE = 52**.
- Batch 3 used exact checksum-locked Volume-I bytes and rendered physical pages 206–249; English OCR was a reading/navigation aid for this secondary witness only, with no Tamil reconstruction.
- All identity work remained report/crosswalk-only; Tamil / released-English mutations **0 / 0**.
- The earlier 22/22 confirmed-MATCHED payload lane remains a separate historical closure; 11 later identity matches are not silently counted as payload-compared.

### BU-SP1 consolidated identity closure — COMPLETE 52/52

Consolidated identity record: `comparisons/SHOWER_OF_POETRY_VOL_1_IDENTITY_52_ENTRY_SUMMARY.md`. Final state: **33 MATCHED / 0 POSSIBLE / 19 NOT YET REPRESENTED / 0 INVESTIGATE = 52 — IDENTITY CLOSED**. The historical payload-comparison closure remains **22/22 of the matches known at that stage**; eleven later identity matches are not retroactively counted as payload-compared. Tamil / released-English mutations from BU-SP1 identity work: **0 / 0**.

### BU-SP3 identity investigation Batch 1 — COMPLETE

Report: `comparisons/13-shower-of-poetry-vol-3-identity-investigation-batch-01.md`. Entries **1–10** were inspected from actual Volume-III page images, physical pages **27–59** / printed pages **1–33**. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**; Tamil / RELEASE-CLEARED English mutations **0 / 0**.

### BU-SP3 identity investigation Batch 2 — COMPLETE

Report: `comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** were inspected from actual Volume-III page images, physical pages **60–99** / printed pages **34–73**. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**; Tamil / RELEASE-CLEARED English mutations **0 / 0**.

### BU-SP3 identity investigation Batch 3 — COMPLETE

Report: `comparisons/15-shower-of-poetry-vol-3-identity-investigation-batch-03.md`. Entries **21–30** were inspected from actual Volume-III page images, physical pages **100–136** / printed pages **74–110**. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**; Tamil / RELEASE-CLEARED English mutations **0 / 0**. Current BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 30 NOT YET REPRESENTED / 20 INVESTIGATE = 50**.

### BU-SP3 identity investigation Batch 4 — COMPLETE

Report: `comparisons/16-shower-of-poetry-vol-3-identity-investigation-batch-04.md`. Entries **31–40** were inspected from the exact Volume-III witness, physical pages **137–176** / printed pages **111–150**. The normal renderer covered physical pages 137–150; exact checksum-locked source rendering covered the later range beyond that tool boundary. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**; Tamil / RELEASE-CLEARED English mutations **0 / 0**. Current BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE = 50**.

### BU-SP3 identity investigation Batch 5 — COMPLETE / VOLUME III IDENTITY CLOSED 50/50

Report: `comparisons/17-shower-of-poetry-vol-3-identity-investigation-batch-05.md`; consolidated closure: `comparisons/SHOWER_OF_POETRY_VOL_3_IDENTITY_50_ENTRY_SUMMARY.md`. Entries **41–50**, physical pages **177–215** / printed pages **151–189**, were read from the exact checksum-locked 220-page witness. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**, Tamil / RELEASE-CLEARED English mutations **0 / 0**. Final BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE = 50 — CLOSED**.

### BU-SP1 later-established MATCHED payload Batch 1 — COMPLETE

Report: `comparisons/18-shower-of-poetry-vol-1-later-matched-payload-batch-01.md`. Compared entries **2, 5, 6, 7, 17, 20, 24, 29, 41 and 42** against actual BU payload, FINAL-CLEARED Tamil and RELEASE-CLEARED English. Result: **PASS / REPORT-ONLY — 10/10**, correction candidates **0 / 0**, Tamil / released-English mutations **0 / 0**. Historical payload closure remains **22/22 of the matches known at that stage**; the separate later-match debt is now **10/11 compared**, giving current MATCHED payload coverage **32/33**.

## Next activity

All **176/176** BU entries have identity dispositions. Complete the remaining BU-SP1 later-match payload debt with **entry 45 — `A Petty Village Full of Folks Illiterate!` → `கலைஞரின் கவிதைகள்` item 67 `பாமரர் நிறைந்த பட்டிக்காடு!`**. Keep the historical 22/22 payload milestone distinct; current overall MATCHED payload coverage is **32/33**. BU-SP2's 39 `NOT YET REPRESENTED` rows remain on source-acquisition hold absent new source evidence.
