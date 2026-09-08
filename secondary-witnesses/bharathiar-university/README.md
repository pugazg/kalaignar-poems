# Bharathiar University English Translation Witnesses

This directory records four 2009 Bharathiar University / Macmillan English-translation books supplied by the user as **institutional secondary witnesses**.

## Witness hierarchy

1. **Controlling historical Tamil scan** — highest authority for Tamil transcription.
2. **FINAL-CLEARED repository Tamil canonical** — authority for repository English translation.
3. **Bharathiar University / Macmillan 2009 English books** — secondary interpretive/editorial witnesses.

These books may help with meaning, person/place identification, Sangam references, title choices and translation review. They must **not** silently change a verified Tamil page, canonical Tamil, or release-cleared English. A later change requires a documented comparison showing that the controlling Tamil supports the change.

This follows the repository's existing cross-witness rule: canonical poem identity and source-witness identity are different facts, and one witness must never be silently normalized against another.

## Four-book set

| Witness | Exact physical pages | Bytes | SHA-256 | Translator | TOC entries |
|---|---:|---:|---|---|---:|
| *Shower of Poetry*, Volume I | 249 | 101,936,284 | `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536` | R. Ganapathy | 52 |
| *Shower of Poetry*, Volume II | 168 | 156,922,680 | `e29c294adfe94c508cdb8aeb4f8cadf116b8dc1bdeb4025eef86a7a017f02a31` | R. Ganapathy | 40 |
| *Shower of Poetry*, Volume III | 220 | 80,185,514 | `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` | V. Murugan | 50 |
| *The Treasure Trove of Time and the Verse Key* | 205 | 106,152,046 | `17ecd31500ad67ec34d684a8c2d0d208866fd5bca3f630a2941c50baa3b86d4b` | P. Marudanayagam | 34 |

All four were edited by **P. Marudanayagam and V. Murugan**, issued by **Bharathiar University, Coimbatore**, with **Macmillan Publishers India Ltd**, first published **2009**.

## Renderer-limit note

The current page renderer exposes only **150 pages** for Volumes I, III and *Treasure Trove*. Exact-byte PDF inspection establishes their real physical lengths as **249, 220 and 205 pages** respectively. The 150-page renderer value is therefore a tooling window, not source-file length.

## Crosswalk state

The four contents witnesses contain **176 translated entries**:

- Volume I: **52** — 20 MATCHED / 3 POSSIBLE / 29 INVESTIGATE;
- Volume II: **40** — 1 MATCHED / 39 NOT YET REPRESENTED;
- Volume III: **50** — 50 INVESTIGATE;
- *Treasure Trove*: **34** — 34 MATCHED.

Overall initial onboarding: **55 MATCHED / 3 POSSIBLE / 39 NOT YET REPRESENTED / 79 INVESTIGATE = 176**.

See the per-book crosswalks plus `MASTER_CROSSWALK.md`.

## High-value established relationships

- Volume II item 17, **The Brother for the Head did Ask!** → `poems/thalaikettan-thambi/` as a later `Sangath Thamizh` English translation witness. Its translation occupies PDF pages **85–89** in the supplied Volume-II file. This establishes a secondary work witness, not authority over the 1966 Murasoli Tamil source.
- Volume I contains numerous selections already represented in `poems/kalaignarin-kavithaigal/`, including `இதயத்தைத் தந்திடு அண்ணா`, `விடுதலை வீரர்கள்`, `ஐம்புலன்`, `புதிய பாதை`, `நீர்க் குடும்பம்`, `பாரதிதாசன்`, `நேரு கண்ட ஜனநாயகம்`, `வெள்ளி விழா`, `தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`, and other matched items.
- *The Treasure Trove of Time and the Verse Key* is a direct **book-level secondary witness** to `poems/kaalap-pezhaiyum-kavithai-saaviyum/`. Its 34 translated TOC entries are mapped to a selected subset of that repository work's 58 canonical items.

## Next activity

Perform payload comparison in controlled batches, beginning with already release-cleared exact matches:

1. `தலைகேட்டான் தம்பி` — compare Volume-II pp.85–89 with FINAL-CLEARED repository Tamil and English;
2. *The Treasure Trove of Time and the Verse Key* — compare the 34 mapped translations against their repository items, recording editorial observations and only source-supported reopen candidates;
3. Volume-I MATCHED/POSSIBLE items;
4. unresolved Volume-I and Volume-III item matching;
5. Volume-II Sangam selections not yet represented.

No comparison batch may directly mutate Tamil or released English text without a separate documented source-backed decision.
