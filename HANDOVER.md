# HANDOVER — Kalaignar Poems Archive

Repository: `pugazg/kalaignar-poems`, branch `main`. **Live main is authoritative.**

## Current active lane — Bharathiar University secondary witnesses

No new Tamil poem is staged. The user supplied four 2009 Bharathiar University / Macmillan English-translation books, onboarded under:

`secondary-witnesses/bharathiar-university/`

Exact witness set:

- BU-SP1 — *Shower of Poetry*, Volume I — **249 pages / 101,936,284 bytes / SHA-256 `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536`**;
- BU-SP2 — *Shower of Poetry*, Volume II — **168 pages / 156,922,680 bytes / SHA-256 `e29c294adfe94c508cdb8aeb4f8cadf116b8dc1bdeb4025eef86a7a017f02a31`**;
- BU-SP3 — *Shower of Poetry*, Volume III — **220 pages / 80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6`**;
- BU-TT — *The Treasure Trove of Time and the Verse Key* — **205 pages / 106,152,046 bytes / SHA-256 `17ecd31500ad67ec34d684a8c2d0d208866fd5bca3f630a2941c50baa3b86d4b`**.

Renderer warning: Volumes I, III and BU-TT may expose only 150 pages through a renderer; exact-byte counts above control.

Initial crosswalk: **176 entries = 55 MATCHED / 3 POSSIBLE / 39 NOT YET REPRESENTED / 79 INVESTIGATE**.

Witness authority rule:

1. historical Tamil controlling source;
2. FINAL-CLEARED repository Tamil canonical;
3. Bharathiar University English translation as a secondary interpretive/editorial witness.

These books must not silently modify Tamil or RELEASE-CLEARED English.

## Secondary Witness Comparison Batch 1 — COMPLETE

Work: `தலைகேட்டான் தம்பி`.

Bharathiar witness: BU-SP2 item 17, **The Brother for the Head did Ask!**, supplied Volume-II physical pages **85–89**.

Durable report:

`secondary-witnesses/bharathiar-university/comparisons/01-thalaikettan-thambi.md`

Result: **COMPARISON PASS / REPORT-ONLY**.

- Tamil/source correction candidates: **0**;
- title replacement candidates: **0**;
- released English modified: **No**;
- strong source-supported English review candidates: **2**;
- medium semantic refinement candidates: **1**;
- low editorial/idiomatic refinement candidates: **1**.

Strong candidates recorded for a future explicitly authorized English-only reopen:

1. `அடுத்தார் பேச்சால் அழிந்த தம்பி` — current English `ruined by his own words` is not supported; source sense is **ruined by the words/counsel of those around him**. BU corroborates `ruined by others' words`.
2. `வாள்முனையில் செங்குருதி தனைக் கண்டான்` — current English `saw red upon the sword-point` omits source `செங்குருதி` / blood and weakens the later reveal `ரத்தமல்ல; செவ்வண்ணம்`; future review should restore the blood perception before the red-colour reveal.

Additional review notes:

- `அலையடிக்கும் கடல்வெல்லும் பரந்த உள்ளம்` may warrant **surpasses the wave-beaten sea** rather than `as vast as`;
- `என் நாட்டைத் தொழுதுவிட்டுக் காடேகு` may read more idiomatically as **take leave of / bow farewell to my country and go to the forest**;
- `குலை யறுக்கும் செய்தி` remains semantic-investigation only; the Bharathiar free rendering does not settle it;
- BU's appended `Puranaanuuru 158, 159 & 162 / Peruncithiranaar` note is preserved as secondary research context only, not inserted into the 1966 canonical layer.

`poems/thalaikettan-thambi/` remains **CLOSED / RELEASE-CLEARED**; no release status is revoked by Batch 1.

## Exact next activity

Proceed with **Secondary Witness Comparison Batch 2 — BU-TT mapped items 1–10** against `poems/kaalap-pezhaiyum-kavithai-saaviyum/`.

For each of the first ten Bharathiar *Treasure Trove* entries:

1. inspect the exact BU-TT translation pages;
2. compare with the corresponding FINAL-CLEARED Tamil stable item and RELEASE-CLEARED repository English;
3. classify title/semantic/omission/expansion/transliteration/structural differences;
4. record only source-supported English reopen candidates;
5. write a report only — **no Tamil or released-English mutation**.

If the user explicitly asks to fix `தலைகேட்டான் தம்பி` English before Batch 2, open a separate English-only editorial-reopen record and adjudicate E1/E2 first, with Tamil frozen.

## Release-cleared work remains frozen

- `poems/thalaikettan-thambi/` — CLOSED / RELEASE-CLEARED — 2026-09-08;
- `poems/aanthaiyum-arasanum/` — CLOSED / RELEASE-CLEARED — 2026-09-07;
- other preserved release-cleared work includes `poomudi`, `anna-kaviyarangam`, `gunanayagar-nehru`, `oruthalaik-kathal`, `kalaignarin-kavithaigal`, `kalaignarin-kaviyaranga-kavithaigal-1975`, and `kanchithan-annan`.
