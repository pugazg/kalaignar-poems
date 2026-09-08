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

## Completed comparison — Batch 1

`comparisons/01-thalaikettan-thambi.md`

Compared BU-SP2 **The Brother for the Head did Ask!** (supplied PDF pp.85–89) with `poems/thalaikettan-thambi/` FINAL-CLEARED Tamil and RELEASE-CLEARED English.

Result: **PASS / REPORT-ONLY**.

- Tamil/source correction candidates: **0**;
- released English changes: **0**;
- strong source-supported future English review candidates: **2**;
- medium semantic refinement: **1**;
- low editorial refinement: **1**.

Strong candidates:

1. `அடுத்தார் பேச்சால் அழிந்த தம்பி` — current `ruined by his own words` should be reviewed as **ruined by the words/counsel of those around him**;
2. `வாள்முனையில் செங்குருதி தனைக் கண்டான்` — current English should be reviewed for restoring source **blood** before the later `not blood—red colour` reveal.

No text was changed. `poems/thalaikettan-thambi/` remains CLOSED / RELEASE-CLEARED.

## High-value established relationships

- BU-SP2 item 17 → `poems/thalaikettan-thambi/` as a later `Sangath Thamizh` English translation witness.
- Volume I contains numerous selections already represented in `poems/kalaignarin-kavithaigal/`.
- *The Treasure Trove of Time and the Verse Key* is a direct **book-level secondary witness** to `poems/kaalap-pezhaiyum-kavithai-saaviyum/`; its 34 TOC entries map to stable repository items.

## Next activity

Perform **Secondary Witness Comparison Batch 2 — BU-TT mapped entries 1–10** against `poems/kaalap-pezhaiyum-kavithai-saaviyum/`.

The batch must inspect the actual Bharathiar translation pages, compare against FINAL-CLEARED Tamil and RELEASE-CLEARED English, and produce a report only. No comparison batch may directly mutate Tamil or released English without a separate documented source-backed decision.
