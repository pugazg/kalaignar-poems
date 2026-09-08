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

Twenty Volume-I entries are already high-confidence matches to stable items in `poems/kalaignarin-kavithaigal/`; three more are POSSIBLE and require payload comparison. The matched set includes `O Panneerselvam!`, `Long Live, Jeeva!`, `Freedom Fighters`, `The Five Senses`, `The New Path`, `Water Family`, `Bharathidasan`, `Do Give Your Heart to Me, Anna!`, `The Democracy that Nehru Found`, `The Silver Jubilee`, `Thanthai Periyar`, `The Poems of Akam (Love) Mode`, `The Feast of Silappadhikaaram`, `In the Path of Anna`, `Today is Your Birthday`, `Social Outlook`, `Dear Friend of Mine! Why Did You Part from Me?`, `As Your Shadow We Move about!`, `Rationalist, Pandyan`, and `No Day there is That May be his Birthday Called`.

POSSIBLE: `The Beloved Son of the Muse of Arts` and the two `Calculation` entries require direct payload comparison before identity is hardened.

### BU-SP2 → `தலைகேட்டான் தம்பி`

Volume-II item 17 is the established secondary work witness:

- Tamil/transliteration witness: `Thalai Keettaan Thambi!`;
- Bharathiar title: **The Brother for the Head did Ask!**;
- printed start page: **62**;
- supplied PDF physical pages: **85–89**;
- repository target: `poems/thalaikettan-thambi/`.

This is a later `Sangath Thamizh` translation witness and does not override the repository's 1966 Murasoli controlling source.

The four `Pisiraandhaiyaar` items have thematic/historical overlap with material elsewhere in the repository, but no identical-work assertion is made without payload comparison.

### BU-TT → `காலப் பேழையும் கவிதைச் சாவியும்`

The entire book is a secondary English witness to `poems/kaalap-pezhaiyum-kavithai-saaviyum/`. All **34/34** translated entries are mapped to the repository's stable 58-item sequence. See its `crosswalk.md` for exact stable item numbers.

Important preserved translation-title divergences include:

- Bharathiar **An Honourable Mother and an Upright Daughter** ↔ repository item 31 source-controlled title `மாண்பு நிறை தாயும் மாசற்ற மகனும்!` / **The Mother Full of Dignity and the Stainless Son!**;
- Bharathiar **A Young Lady, She is a Tamil Lady!** ↔ repository item 36 source-controlled title `இளையவன்; அவன் ஒரு தமிழ் மகன்!` / **He Is Young; He Is a Son of Tamil!**.

These are evidence for editorial comparison, not permission to normalize the source-controlled Tamil title.

### BU-SP3

All 50 titles are preserved, but item-level mapping is deliberately deferred. English-title similarity alone is insufficient under repository cross-witness policy.

## Completed comparison batches

### Batch 1 — `தலைகேட்டான் தம்பி`

Report: `comparisons/01-thalaikettan-thambi.md`.

Compared BU-SP2 physical PDF pages **85–89** with FINAL-CLEARED Tamil and RELEASE-CLEARED repository English.

Result: **COMPARISON PASS / REPORT-ONLY**.

- Tamil/source correction candidates: **0**;
- title replacement candidates: **0**;
- released English changes: **0**;
- strong future English review candidates: **2**;
- medium semantic refinement candidates: **1**;
- low editorial/idiomatic refinement candidates: **1**.

Strong source-supported candidates if a separate English-only reopen is authorized:

1. `அடுத்தார் பேச்சால் அழிந்த தம்பி` — current repository `ruined by his own words` should be reviewed as **ruined by the words/counsel of those around him**; Bharathiar corroborates `ruined by others' words`.
2. `வாள்முனையில் செங்குருதி தனைக் கண்டான்` — current English `saw red upon the sword-point` omits source **blood** before the later `ரத்தமல்ல; செவ்வண்ணம்` reveal.

The report also records a medium comparative-force refinement for `அலையடிக்கும் கடல்வெல்லும் பரந்த உள்ளம்`, a low idiomatic refinement for `என் நாட்டைத் தொழுதுவிட்டுக் காடேகு`, and the Bharathiar `Puranaanuuru 158, 159 & 162 / Peruncithiranaar` note as secondary research context only.

`poems/thalaikettan-thambi/` remains CLOSED / RELEASE-CLEARED; Batch 1 did not reopen it.

## Status semantics

- **MATCHED** — high-confidence current repository work/item identity established. Payload comparison may still reveal witness-specific wording/translation differences.
- **POSSIBLE** — likely relationship; compare body/source context before hardening identity.
- **NOT YET REPRESENTED** — no exact current repository representation established in this onboarding pass. This is not a claim that the subject is absent from Kalaignar's corpus.
- **INVESTIGATE** — a repository matching pass is still required.

## Comparison policy

For any MATCHED/POSSIBLE entry:

1. preserve the Bharathiar text as a distinct witness;
2. compare it first with FINAL-CLEARED repository Tamil and then with released repository English;
3. classify differences as title choice, interpretation, omission, expansion, transliteration/name choice, structural condensation, or genuine possible mistranslation;
4. never use Bharathiar wording to rewrite Tamil;
5. never update released English unless the controlling Tamil independently supports the revision;
6. if a revision is source-supported, document a formal English-layer reopen with the Bharathiar witness cited as corroborating/diagnostic evidence only.

## Exact next activity

Start **Secondary Witness Comparison Batch 2 — BU-TT mapped entries 1–10**:

- resolve the first ten mapped entries through `treasure-trove-of-time-and-verse-key/crosswalk.md`;
- inspect their exact Bharathiar translation pages;
- compare against corresponding FINAL-CLEARED Tamil and RELEASE-CLEARED English under `poems/kaalap-pezhaiyum-kavithai-saaviyum/`;
- produce a comparison report only;
- identify source-supported English reopen candidates without mutating Tamil or released English.

Then continue BU-TT entries **11–20**, **21–30**, and **31–34** in later controlled batches.
