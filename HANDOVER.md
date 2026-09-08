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

Current hardened crosswalk: **176 entries = 68 MATCHED / 0 POSSIBLE / 78 NOT YET REPRESENTED / 30 INVESTIGATE**.

Witness authority:

1. historical Tamil controlling source;
2. FINAL-CLEARED repository Tamil canonical;
3. Bharathiar University English translation as a secondary interpretive/editorial witness.

These books must not silently modify Tamil or RELEASE-CLEARED English. If a later witness exposes a possible problem, the controlling Tamil source must be reread before any correction.

## Comparison Batch 1 — COMPLETE

`comparisons/01-thalaikettan-thambi.md` — `தலைகேட்டான் தம்பி` vs BU-SP2 item 17: **PASS / REPORT-ONLY**. Two strong future English review candidates were recorded; no mutation occurred during the comparison.

## Comparison Batch 2 — COMPLETE

`comparisons/02-treasure-trove-items-01-10.md` — BU-TT entries **1–10** vs repository items **1, 2, 5, 6, 11, 17, 19, 20, 21, 22**: **PASS / REPORT-ONLY**, 10/10 compared, mutations **0 / 0**.

## Comparison Batch 3 — COMPLETE + item-31 correction addendum

Original report: `comparisons/03-treasure-trove-items-11-20.md`.  
Correction addendum: `comparisons/03A-item31-title-correction.md`.

Scope: BU-TT entries **11–20** vs repository items **23, 24, 26, 29, 31, 32, 35, 36, 37, 38**.

### Source-backed item-31 reopen — 2026-09-08

The user identified a contents/poem-page discrepancy and reattached the controlling Tamil PDF. Direct visual reread of **scan 148** established:

- contents witness: **`மாண்பு நிறை தாயும், மாசற்ற மகனும்!`**;
- direct poem-opening/title-page witness: **`மாண்பு நிறை தாயும் மாசற்ற மகளும்!`**.

Repository policy already gives the direct title-page witness canonical/display authority. The prior page/canonical record had accidentally copied contents `மகனும்` into the title-page layer. The correction is therefore source-backed, not semantic normalization.

Durable correction authority: `poems/kaalap-pezhaiyum-kavithai-saaviyum/POST_RELEASE_ITEM31_TITLE_CORRECTION.md`.

Canonical item 31 is now **`மாண்பு நிறை தாயும் மாசற்ற மகளும்!` / The Mother Full of Dignity and the Stainless Daughter!**. Contents `மகனும்` remains preserved as a separate source witness. The poem body concerning Madhavi and Manimekalai, including closing `மாண்பு நிறை தாய் மகள் வரலாறு`, corroborates but is not the authority for the title correction. BU **An Honourable Mother and an Upright Daughter** is now corroborating secondary evidence rather than an editorial emendation.

Other Batch-3 findings remain: BU `winnowing fan` does not override verified `முரசு`; BU female retitle of item 36 does not override source `இளையவன்; அவன் ஒரு தமிழ் மகன்!`.

## Comparison Batch 4 — COMPLETE

`secondary-witnesses/bharathiar-university/comparisons/04-treasure-trove-items-21-30.md`

Scope: BU-TT entries **21–30**, printed pages **93–144**, supplied PDF physical pages **123–174**, mapped to repository items **39, 40, 44, 45, 46, 47, 49, 50, 51 and 52**.

Result: **PASS / REPORT-ONLY** — 10/10 compared; Tamil/source correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**.

Key findings:

- BU entry 21 omits repository item 39's final *Periya Puranam* / Sekkizhar Vatapi-campaign quotation;
- BU entry 23 singularizes source `ஈக்களின்` as **a Fly**; repository **Flies** remains source-controlled;
- BU entry 26's **Future Dear** is weaker than source `அருங்காலம்`; repository **Precious Age** remains closer;
- BU entry 30 materially truncates item 52 after the Golden-Handed Pandyan episode, omitting the later Pandya list, *Tolkappiyam* presentation and closing transition.

## BU-TT comparison lane — COMPLETE 34/34

Final Batch 5: `secondary-witnesses/bharathiar-university/comparisons/05-treasure-trove-items-31-34.md` — entries **31–34** → repository items **53, 55, 56, 57**, **PASS / REPORT-ONLY**, corrections/mutations **0 / 0**. Consolidated closure: `secondary-witnesses/bharathiar-university/comparisons/TREASURE_TROVE_34_ENTRY_SUMMARY.md`.

The full BU-TT witness is now **34/34 compared**. Apart from the separately source-verified item-31 `மகளும்` title correction, the lane established no Tamil body correction and no other released-English mutation.

## BU-SP1 identity hardening — COMPLETE

Report `secondary-witnesses/bharathiar-university/comparisons/06-shower-of-poetry-vol-1-identity-hardening.md`: **entry 8 MATCHED item 40; entry 18 MATCHED item 18; entry 43 DISTINCT 1995 work / not item 18, representation INVESTIGATE**. BU-SP1 is now **22 MATCHED / 0 POSSIBLE / 30 INVESTIGATE**. Tamil/released-English mutations **0 / 0**.

## BU-SP1 payload comparison Batch 1 — COMPLETE

Report `secondary-witnesses/bharathiar-university/comparisons/07-shower-of-poetry-vol-1-matched-batch-01.md`: confirmed MATCHED entries **1, 8, 9, 11, 12, 13, 14, 15, 16 and 18**, **PASS / REPORT-ONLY — 10/10**. Tamil/source correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**. Strong diagnostics include BU `பஞ்சைகளல்ல` → **cowards**, `கிந்தன்` → **Kandan**, omission of the New Path river-love sequence and Bharathidasan Muthamma dream, and Calculation-I `மணக்கணக்கு` → **mental calculation** / `வேங்கை` → **lion** / river → **rains**.

## BU-SP1 payload comparison Batch 2 — COMPLETE

Report `secondary-witnesses/bharathiar-university/comparisons/08-shower-of-poetry-vol-1-matched-batch-02.md`: entries **19, 21, 22, 23, 25, 26, 27, 28, 30 and 33**, **PASS / REPORT-ONLY — 10/10**. Tamil/source correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**. Exact-byte direct rendering was used for physical Volume-I pages beyond the normal 150-page renderer window; no OCR reconstruction.

Key diagnostics: entry 19 omits the Nehru/Rose allegory; entry 21 has `பொன்விழா` → **Diamond Jubilee** plus a BU **1922** metadata error; entry 25 heavily condenses the Silappathikaram/Tolkappiyam/abhinaya blocks; entry 26 has `ஆத்திகம்` → **agnosticism** and omits the Kamban/Ravana + Anna-title chain; entry 28 has BU **07-11-1980** against source **7.1.80**.

## BU-SP1 payload comparison Batch 3 — COMPLETE

Report `secondary-witnesses/bharathiar-university/comparisons/09-shower-of-poetry-vol-1-matched-batch-03.md`: final MATCHED entries **39 and 40**, **PASS / REPORT-ONLY — 2/2**. Tamil/source correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**. Direct exact-byte renders were used for Volume-I physical pages **194–198**, with no OCR reconstruction. Strong BU defects: `பவள விழா` → **Platinum Jubilee**; source **1929** → BU **1928**; `வெல்லம்` → **sugar cane**; `அர்ச்சனைகள்` → **censure**.

## BU-SP1 confirmed-MATCHED comparison lane — COMPLETE 22/22

Consolidated authority: `secondary-witnesses/bharathiar-university/comparisons/SHOWER_OF_POETRY_VOL_1_22_MATCHED_SUMMARY.md`. All **22/22** confirmed MATCHED BU-SP1 payloads are compared. Aggregate mutations **0 / 0**; Volume-I classification remains **22 MATCHED / 0 POSSIBLE / 30 INVESTIGATE**.

## BU-SP1 identity investigation Batches 1–3 — COMPLETE / IDENTITY CLOSED 52/52

Reports `comparisons/10-shower-of-poetry-vol-1-identity-investigation-batch-01.md`, `comparisons/11-shower-of-poetry-vol-1-identity-investigation-batch-02.md` and `comparisons/12-shower-of-poetry-vol-1-identity-investigation-batch-03.md`. Across the identity batches, **11 new MATCHED** identities and **19 NOT YET REPRESENTED** dispositions were hardened from source payload/event context.

Batch 3 final ten: **entry 45 MATCHED** `கலைஞரின் கவிதைகள்` item 67; entries **43, 44, 46, 47, 48, 49, 50, 51, 52 NOT YET REPRESENTED**. Final BU-SP1 identity state: **33 MATCHED / 0 POSSIBLE / 19 NOT YET REPRESENTED / 0 INVESTIGATE = 52**. Four-book tally immediately after BU-SP1 closure: **68 MATCHED / 0 POSSIBLE / 78 NOT YET REPRESENTED / 30 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

For Batch 3, exact Volume-I bytes were independently locked to **249 pages / 101,936,284 bytes / SHA-256 `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536`** before physical pages **206–249** were rendered. English OCR was used only as a reading/navigation aid for this institutional secondary witness; it did not reconstruct or mutate Tamil.

The earlier confirmed-MATCHED payload lane remains **22/22 for the matches known at that stage**. Eleven later identity matches exist, but are not retroactively claimed as payload-compared.

## BU-SP1 consolidated identity closure — COMPLETE 52/52

Consolidated authority: `secondary-witnesses/bharathiar-university/comparisons/SHOWER_OF_POETRY_VOL_1_IDENTITY_52_ENTRY_SUMMARY.md`. Final BU-SP1 identity state is **33 MATCHED / 0 POSSIBLE / 19 NOT YET REPRESENTED / 0 INVESTIGATE = 52 — CLOSED**. The separate historical payload-comparison closure remains **22/22 of the matches known at that stage**.

## BU-SP3 identity investigation Batch 1 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/13-shower-of-poetry-vol-3-identity-investigation-batch-01.md`. Entries **1–10** were hardened **NOT YET REPRESENTED** from direct physical pages **27–59** / printed pages **1–33**. Batch result: **PASS / REPORT-ONLY — 10/10; 0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**. Tamil / released-English mutations: **0 / 0**.

## BU-SP3 identity investigation Batch 2 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** were hardened **NOT YET REPRESENTED** from direct physical pages **60–99** / printed pages **34–73**. Batch result: **PASS / REPORT-ONLY — 10/10; 0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**. BU-SP3 now stands at **0 MATCHED / 0 POSSIBLE / 20 NOT YET REPRESENTED / 30 INVESTIGATE = 50**; four-book tally **68 MATCHED / 0 POSSIBLE / 78 NOT YET REPRESENTED / 30 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

## Exact next activity

Run **BU-SP3 Identity Investigation Batch 3 — entries 21–30 in source order**. Report/crosswalk only; no FINAL-CLEARED Tamil or RELEASE-CLEARED English mutation.

## Release-cleared work rule

Completed workspaces remain frozen unless genuinely new source-backed evidence justifies a documented reopen. Item 31 above is such a documented exception; its reopen is deliberately title-only and does not alter narrative/body text or item boundaries.
