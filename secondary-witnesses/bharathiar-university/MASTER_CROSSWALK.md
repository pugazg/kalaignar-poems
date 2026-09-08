# Bharathiar University English Translation Witness — Master Crosswalk

## Purpose

This is the master index for the four user-supplied 2009 Bharathiar University / Macmillan English-translation books. It records **secondary witness identity and repository relationships**. Secondary witnesses cannot silently rewrite Tamil; any repository correction must be independently supported by the controlling Tamil scan.

Authority remains:

1. controlling historical Tamil scan;
2. FINAL-CLEARED repository Tamil canonical;
3. Bharathiar University English translation as an institutional secondary/interpretive witness.

## Exact witness set

| Code | Book | Exact pages | Bytes | SHA-256 | Entries | Crosswalk state |
|---|---|---:|---:|---|---:|---|
| BU-SP1 | *Shower of Poetry*, Volume I | 249 | 101,936,284 | `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536` | 52 | 20 MATCHED / 3 POSSIBLE / 29 INVESTIGATE |
| BU-SP2 | *Shower of Poetry*, Volume II | 168 | 156,922,680 | `e29c294adfe94c508cdb8aeb4f8cadf116b8dc1bdeb4025eef86a7a017f02a31` | 40 | 1 MATCHED / 39 NOT YET REPRESENTED |
| BU-SP3 | *Shower of Poetry*, Volume III | 220 | 80,185,514 | `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` | 50 | 50 INVESTIGATE |
| BU-TT | *The Treasure Trove of Time and the Verse Key* | 205 | 106,152,046 | `17ecd31500ad67ec34d684a8c2d0d208866fd5bca3f630a2941c50baa3b86d4b` | 34 | 34 MATCHED |

**Total: 176 entries — 55 MATCHED / 3 POSSIBLE / 39 NOT YET REPRESENTED / 79 INVESTIGATE.**

Per-book tables:

- `shower-of-poetry-vol-1/crosswalk.md`;
- `shower-of-poetry-vol-2/crosswalk.md`;
- `shower-of-poetry-vol-3/crosswalk.md`;
- `treasure-trove-of-time-and-verse-key/crosswalk.md`.

## Confirmed repository relationships

### BU-SP1 → `கலைஞரின் கவிதைகள்`

Twenty Volume-I entries are high-confidence matches to stable items in `poems/kalaignarin-kavithaigal/`; three more are POSSIBLE and require payload comparison.

### BU-SP2 → `தலைகேட்டான் தம்பி`

Volume-II item 17 is the established secondary work witness:

- Tamil/transliteration witness: `Thalai Keettaan Thambi!`;
- Bharathiar title: **The Brother for the Head did Ask!**;
- printed start page: **62**;
- supplied PDF physical pages: **85–89**;
- repository target: `poems/thalaikettan-thambi/`.

This is a later `Sangath Thamizh` translation witness and does not override the repository's 1966 Murasoli controlling source.

### BU-TT → `காலப் பேழையும் கவிதைச் சாவியும்`

The entire book is a secondary English witness to `poems/kaalap-pezhaiyum-kavithai-saaviyum/`. All **34/34** translated entries map to stable repository items.

Important title-witness cases:

- **Item 31 — corrected 2026-09-08:** contents `மாண்பு நிறை தாயும், மாசற்ற மகனும்!`; direct poem-opening scan 148 `மாண்பு நிறை தாயும் மாசற்ற மகளும்!`. The direct title-page witness governs canonical assembly, so the repository title is **`மாண்பு நிறை தாயும் மாசற்ற மகளும்!` / The Mother Full of Dignity and the Stainless Daughter!**. BU **An Honourable Mother and an Upright Daughter** now corroborates the direct source witness rather than constituting an editorial retitle. See `comparisons/03A-item31-title-correction.md` and the work-level `POST_RELEASE_ITEM31_TITLE_CORRECTION.md`.
- Bharathiar **A Young Lady, She is a Tamil Lady!** ↔ repository item 36 source title `இளையவன்; அவன் ஒரு தமிழ் மகன்!` / **He Is Young; He Is a Son of Tamil!**; this remains a genuine secondary editorial retitling.

### BU-SP3

All 50 titles are preserved, but item-level mapping is deliberately deferred. English-title similarity alone is insufficient under repository cross-witness policy.

## Completed comparison batches

### Batch 1 — `தலைகேட்டான் தம்பி`

`comparisons/01-thalaikettan-thambi.md` — **PASS / REPORT-ONLY**. Two strong future English-review candidates were recorded; no release mutation occurred during the comparison.

### Batch 2 — BU-TT entries 1–10

`comparisons/02-treasure-trove-items-01-10.md` — items **1, 2, 5, 6, 11, 17, 19, 20, 21, 22**, physical pages **31–74** / printed **1–44**. **PASS / REPORT-ONLY**.

Principal findings: BU entry 6 truncates item 17; BU entry 8 condenses item 20's Sangam apparatus; BU entry 4's negative Stone-Age interpretation does not override verified `காணமுடியக்`; BU entry 10's “ignorant look” does not override verified `அரியா நோக்கு`.

### Batch 3 — BU-TT entries 11–20

Original report: `comparisons/03-treasure-trove-items-11-20.md`.  
Source-correction addendum: `comparisons/03A-item31-title-correction.md`.

Scope items **23, 24, 26, 29, 31, 32, 35, 36, 37, 38**, physical pages **75–122** / printed **45–92**.

The original report's item-31 `son` conclusion is **SUPERSEDED**. A direct reread of controlling Tamil scan 148 established `மாசற்ற மகளும்!`, while the contents independently retains `மாசற்ற மகனும்!`. That source-backed correction has been applied to the page record, canonical Tamil title and English title layer. The poem body about Madhavi and Manimekalai corroborates but does not substitute for the direct title-page evidence.

Other Batch-3 conclusions remain valid:

- BU entry 13's **winnowing fan** does not override verified `முரசு` / repository **war-drum**;
- BU entry 16's **Head That Hung** remains a weaker fit for `குனிந்திடும்` than repository **Heads Bow Down**;
- BU entry 18 remains a protagonist-oriented retitle of item 36.

### Batch 4 — BU-TT entries 21–30

`comparisons/04-treasure-trove-items-21-30.md` — items **39, 40, 44, 45, 46, 47, 49, 50, 51, 52**, physical pages **123–174** / printed **93–144**. **PASS / REPORT-ONLY**.

Principal findings:

1. entry 21 omits item 39's final *Periya Puranam* / Sekkizhar quotation;
2. entry 23 singular **a Fly** conflicts with source plural `ஈக்களின்`; repository **Flies** remains source-controlled;
3. entry 26 **Future Dear** is weaker than source `அருங்காலம்`; repository **Precious Age** remains closer;
4. entry 30 truncates item 52 after the Golden-Handed Pandyan episode, omitting the later Pandya list, *Tolkappiyam* presentation and closing transition;
5. dominant pattern: smoothing, condensation, transliteration and interpretive title wording rather than repository defects.

The conversation renderer caps BU-TT at 150 visible pages; physical pages 151–174 used in Batch 4 were directly rendered from the exact checksum-locked 205-page PDF bytes without OCR reconstruction.

## Status semantics

- **MATCHED** — high-confidence current repository work/item identity established.
- **POSSIBLE** — likely relationship; compare body/source context before hardening identity.
- **NOT YET REPRESENTED** — no exact current repository representation established in this onboarding pass.
- **INVESTIGATE** — a repository matching pass is still required.

## Comparison policy

For any MATCHED/POSSIBLE entry:

1. preserve the Bharathiar text as a distinct witness;
2. compare it first with FINAL-CLEARED repository Tamil and then with released repository English;
3. classify differences as title choice, interpretation, omission, expansion, transliteration/name choice, structural condensation, or possible mistranslation;
4. never use Bharathiar wording alone to rewrite Tamil;
5. update released English only when the controlling Tamil independently supports the revision;
6. any revision requires a documented source-backed reopen; Bharathiar can serve as corroborating/diagnostic evidence.

## Exact next activity

After the item-31 correction synchronization is fully recorded, complete **Secondary Witness Comparison Batch 5 — final BU-TT entries 31–34**:

- repository items **53, 55, 56 and 57**;
- inspect exact Bharathiar translation pages;
- compare with corresponding FINAL-CLEARED Tamil and RELEASE-CLEARED English;
- produce a report only;
- identify source-supported English reopen candidates without mutating source layers in the comparison step.

After Batch 5, produce a consolidated **34/34 BU-TT comparison summary** and choose the next secondary-witness lane.
