# Next Chat Prompt — Kalaignar Poems Archive / Bharathiar University Secondary Witnesses

Continue `pugazg/kalaignar-poems`, branch `main`. **Fetch live `main` first** and preserve every newer durable/release-cleared source, Tamil canonical and English release.

## Active lane

No new Tamil poem is staged. The current activity is:

`secondary-witnesses/bharathiar-university/`

Read before further witness work:

1. `POEM_PROCESSING_GUIDE.md`;
2. `WAVE4_CROSS_WITNESS_AUDIT.md`;
3. root `HANDOVER.md`;
4. `TRANSCRIPTION_PHASE_PLAN.md`;
5. this prompt;
6. `secondary-witnesses/bharathiar-university/README.md`;
7. `secondary-witnesses/bharathiar-university/MASTER_CROSSWALK.md`;
8. relevant per-book `source.md` and `crosswalk.md`;
9. completed comparison reports under `secondary-witnesses/bharathiar-university/comparisons/`.

## Witness hierarchy

1. controlling historical Tamil scan = highest Tamil authority;
2. FINAL-CLEARED repository Tamil canonical = authority for repository English;
3. Bharathiar University 2009 English = institutional secondary/interpretive witness.

Never use the Bharathiar books to silently rewrite Tamil or RELEASE-CLEARED English. Any English change requires a separate documented reopen and independent support from the controlling Tamil.

## Exact witness set

- BU-SP1 — *Shower of Poetry*, Volume I — **249 pages / 101,936,284 bytes / SHA-256 `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536`**;
- BU-SP2 — *Shower of Poetry*, Volume II — **168 pages / 156,922,680 bytes / SHA-256 `e29c294adfe94c508cdb8aeb4f8cadf116b8dc1bdeb4025eef86a7a017f02a31`**;
- BU-SP3 — *Shower of Poetry*, Volume III — **220 pages / 80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6`**;
- BU-TT — *The Treasure Trove of Time and the Verse Key* — **205 pages / 106,152,046 bytes / SHA-256 `17ecd31500ad67ec34d684a8c2d0d208866fd5bca3f630a2941c50baa3b86d4b`**.

Renderer note: Volumes I, III and BU-TT may expose only a 150-page tooling window. The physical counts above control.

## Completed — Secondary Witness Comparison Batch 1

Work: `தலைகேட்டான் தம்பி`.

Report:

`secondary-witnesses/bharathiar-university/comparisons/01-thalaikettan-thambi.md`

Result: **PASS / REPORT-ONLY**.

- Tamil changes: **0**;
- released English changes: **0**;
- strong future English review candidates: **2**:
  1. `அடுத்தார் பேச்சால் அழிந்த தம்பி` — `ruined by his own words` should be reviewed as **ruined by the words/counsel of those around him**;
  2. `வாள்முனையில் செங்குருதி தனைக் கண்டான்` — current English omits **blood** before the later `not blood—red colour` reveal;
- medium candidate: preserve comparative force in `அலையடிக்கும் கடல்வெல்லும் பரந்த உள்ளம்`;
- low editorial candidate: idiomatic handling of `என் நாட்டைத் தொழுதுவிட்டுக் காடேகு`.

Do not fix these silently. `poems/thalaikettan-thambi/` remains CLOSED / RELEASE-CLEARED unless the user explicitly authorizes an English-only reopen.

## Exact next activity — Secondary Witness Comparison Batch 2

Book: **BU-TT — The Treasure Trove of Time and the Verse Key**.

Scope: **mapped entries 1–10**.

Repository target: `poems/kaalap-pezhaiyum-kavithai-saaviyum/`.

For each entry:

1. use the BU-TT per-book crosswalk to resolve the stable repository item number;
2. inspect the exact Bharathiar translation pages, not just the TOC title;
3. read the corresponding FINAL-CLEARED Tamil item and RELEASE-CLEARED repository English;
4. classify differences as title choice, semantic interpretation, omission/condensation, expansion, transliteration/name choice, structural reshaping or possible mistranslation;
5. distinguish Bharathiar errors/condensations from genuine repository-English review candidates;
6. produce one durable Batch-2 report covering items 1–10;
7. make **no Tamil or released-English text changes**.

After Batch 2, continue BU-TT entries 11–20, 21–30 and 31–34 unless the user directs another scope.
