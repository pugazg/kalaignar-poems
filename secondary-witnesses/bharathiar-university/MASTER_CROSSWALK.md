# Bharathiar University English Translation Witness — Master Crosswalk

## Purpose

This is the master index for the four user-supplied 2009 Bharathiar University / Macmillan English-translation books. It records **secondary witness identity and repository relationships only**. It changes no Tamil transcription, canonical Tamil, released English, title authority or source-critical decision.

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

Per-book complete title/start-page tables and mapping decisions:

- `shower-of-poetry-vol-1/crosswalk.md`;
- `shower-of-poetry-vol-2/crosswalk.md`;
- `shower-of-poetry-vol-3/crosswalk.md`;
- `treasure-trove-of-time-and-verse-key/crosswalk.md`.

## Confirmed repository relationships

### BU-SP1 → `கலைஞரின் கவிதைகள்`

Twenty Volume-I entries are already high-confidence matches to stable items in `poems/kalaignarin-kavithaigal/`; three more are POSSIBLE and require payload comparison.

### BU-SP2 → `தலைகேட்டான் தம்பி`

Volume-II item 17 is the established secondary work witness:

- Tamil/transliteration witness: `Thalai Keettaan Thambi!`;
- Bharathiar title: **The Brother for the Head did Ask!**;
- printed start page: **62**;
- supplied PDF physical pages: **85–89**;
- repository target: `poems/thalaikettan-thambi/`.

This is a later `Sangath Thamizh` translation witness and does not override the repository's 1966 Murasoli controlling source.

### BU-TT → `காலப் பேழையும் கவிதைச் சாவியும்`

The entire book is a secondary English witness to `poems/kaalap-pezhaiyum-kavithai-saaviyum/`. All **34/34** translated entries are mapped to the repository's stable 58-item sequence.

Important preserved translation-title divergences include:

- Bharathiar **An Honourable Mother and an Upright Daughter** ↔ repository item 31 source-controlled title `மாண்பு நிறை தாயும் மாசற்ற மகனும்!` / **The Mother Full of Dignity and the Stainless Son!**;
- Bharathiar **A Young Lady, She is a Tamil Lady!** ↔ repository item 36 source-controlled title `இளையவன்; அவன் ஒரு தமிழ் மகன்!` / **He Is Young; He Is a Son of Tamil!**.

### BU-SP3

All 50 titles are preserved, but item-level mapping is deliberately deferred. English-title similarity alone is insufficient under repository cross-witness policy.

## Completed comparison batches

### Batch 1 — `தலைகேட்டான் தம்பி`

Report: `comparisons/01-thalaikettan-thambi.md`.

Result: **COMPARISON PASS / REPORT-ONLY**. Tamil/source corrections **0**; released-English changes **0**; two strong future English review candidates recorded. `poems/thalaikettan-thambi/` remains CLOSED / RELEASE-CLEARED.

### Batch 2 — BU-TT entries 1–10

Report: `comparisons/02-treasure-trove-items-01-10.md`.

Mapped/reviewed repository items: **1, 2, 5, 6, 11, 17, 19, 20, 21, 22**. Bharathiar witness range: supplied PDF physical pages **31–74** / printed pages **1–44**.

Result: **COMPARISON PASS / REPORT-ONLY** — 10/10 compared; Tamil/source correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**.

Principal findings: BU entry 6 substantially truncates repository item 17; BU entry 8 condenses item 20's Sangam quotation/citation apparatus; BU entry 4's negative Stone-Age reading does not override verified `காணமுடியக்`; BU entry 10's “ignorant look” does not override verified `அரியா நோக்கு`.

### Batch 3 — BU-TT entries 11–20

Report: `comparisons/03-treasure-trove-items-11-20.md`.

Mapped/reviewed repository items: **23, 24, 26, 29, 31, 32, 35, 36, 37, 38**. Bharathiar witness range: supplied PDF physical pages **75–122** / printed pages **45–92**.

Result: **COMPARISON PASS / REPORT-ONLY** — 10/10 compared; Tamil/source correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**.

Principal findings:

1. **Item 31 source title/body anomaly:** verified title says `மாசற்ற மகனும்` / stainless son, while verified closing body says `மாண்பு நிறை தாய் மகள் வரலாறு` / mother-daughter history. Bharathiar's title is a later editorial harmonization, not proof of a source transcription error.
2. **Item 36 retitling:** verified source title is `இளையவன்; அவன் ஒரு தமிழ் மகன்!`; Bharathiar retitles toward Anni Minjili, the eventual protagonist.
3. **Item 26 lexical substitution:** Bharathiar uses **winnowing fan** but FINAL-CLEARED scan 130 explicitly prints `முரசு`; repository **war-drum** is source-controlled.
4. **Item 32 title fit:** Bharathiar **the Head That Hung** is a weaker fit for `குனிந்திடும்`; repository **Heads Bow Down** remains closer.

### Batch 4 — BU-TT entries 21–30

Report: `comparisons/04-treasure-trove-items-21-30.md`.

Mapped/reviewed repository items: **39, 40, 44, 45, 46, 47, 49, 50, 51, 52**. Bharathiar witness range: supplied PDF physical pages **123–174** / printed pages **93–144**.

Result: **COMPARISON PASS / REPORT-ONLY**.

- items compared: **10/10**;
- Tamil/source transcription correction candidates: **0**;
- source-supported released-English correction candidates: **0**;
- authorized title replacements: **0**;
- Tamil/released-English mutations: **0 / 0**.

Principal findings:

1. **Entry 21 / item 39:** Bharathiar omits the final *Periya Puranam* / Sekkizhar quotation describing Paranjothi's Vatapi campaign and booty; repository remains source-complete.
2. **Entry 23 / item 44:** Bharathiar singular **a Fly** conflicts with source plural `ஈக்களின்`; repository **Flies** remains source-controlled.
3. **Entry 26 / item 47:** Bharathiar **Future Dear** is an awkward rendering of `அருங்காலம்`; repository **Precious Age** remains closer to source.
4. **Entry 30 / item 52:** Bharathiar ends after the Golden-Handed Pandyan episode and omits the later Pandya list, *Tolkappiyam* presentation and closing transition; repository is materially more source-complete.
5. Across Batch 4, the dominant pattern continues to be **smoothing, condensation, transliteration and interpretive title wording** rather than repository defects.

The conversation renderer caps BU-TT at 150 visible pages; physical pages 151–174 used in Batch 4 were directly rendered from the exact checksum-locked 205-page PDF bytes without OCR reconstruction.

## Status semantics

- **MATCHED** — high-confidence current repository work/item identity established. Payload comparison may still reveal witness-specific wording/translation differences.
- **POSSIBLE** — likely relationship; compare body/source context before hardening identity.
- **NOT YET REPRESENTED** — no exact current repository representation established in this onboarding pass.
- **INVESTIGATE** — a repository matching pass is still required.

## Comparison policy

For any MATCHED/POSSIBLE entry:

1. preserve the Bharathiar text as a distinct witness;
2. compare it first with FINAL-CLEARED repository Tamil and then with released repository English;
3. classify differences as title choice, interpretation, omission, expansion, transliteration/name choice, structural condensation, or genuine possible mistranslation;
4. never use Bharathiar wording to rewrite Tamil;
5. never update released English unless the controlling Tamil independently supports the revision;
6. if a revision is source-supported, document a formal English-layer reopen with Bharathiar as corroborating/diagnostic evidence only.

## Exact next activity

Complete **Secondary Witness Comparison Batch 5 — final BU-TT entries 31–34**:

- repository items **53, 55, 56 and 57**;
- inspect exact Bharathiar translation pages, not only TOC titles;
- compare with corresponding FINAL-CLEARED Tamil and RELEASE-CLEARED English;
- produce a report only;
- identify source-supported English reopen candidates without mutating Tamil or released English.

After Batch 5, produce a consolidated **34/34 BU-TT comparison summary** and choose the next secondary-witness lane.
