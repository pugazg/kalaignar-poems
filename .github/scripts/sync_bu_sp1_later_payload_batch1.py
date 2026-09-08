from pathlib import Path


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f"{label}: expected exactly 1 occurrence, found {n}")
    return text.replace(old, new, 1)


def insert_before_once(text, marker, block, label):
    n = text.count(marker)
    if n != 1:
        raise SystemExit(f"{label}: expected exactly 1 marker, found {n}")
    return text.replace(marker, block + marker, 1)


report = "`comparisons/18-shower-of-poetry-vol-1-later-matched-payload-batch-01.md`"

# Per-book crosswalk
p = "secondary-witnesses/bharathiar-university/shower-of-poetry-vol-1/crosswalk.md"
t = read(p)
old = """## Exact next activity

Volume-I identity work is closed. Proceed to **BU-SP3 Identity Investigation Batch 1 — entries 1–10** under the repository-wide phase plan.
"""
new = """## Later-established MATCHED payload comparison Batch 1 — COMPLETE — 2026-09-08

Authority: `../comparisons/18-shower-of-poetry-vol-1-later-matched-payload-batch-01.md`.

Compared later-established MATCHED entries **2, 5, 6, 7, 17, 20, 24, 29, 41 and 42** against actual BU payload, FINAL-CLEARED Tamil and RELEASE-CLEARED English. Result: **PASS / REPORT-ONLY — 10/10**; Tamil/source correction candidates **0**; released-English correction candidates **0**; Tamil / released-English mutations **0 / 0**.

Historical payload milestone remains **22/22 of the matches known at that stage**. Separate later-match payload debt is now **10/11 compared**, so total current MATCHED payload coverage is **32/33** without relabelling the historical 22/22 record.

## Exact next activity

Compare the final later-established MATCHED remainder: **BU-SP1 entry 45 — `A Petty Village Full of Folks Illiterate!` → `poems/kalaignarin-kavithaigal/` item 67 `பாமரர் நிறைந்த பட்டிக்காடு!`**. Report first; do not mutate Tamil or RELEASE-CLEARED English unless the controlling Tamil independently supports a documented reopen.
"""
t = replace_once(t, old, new, "SP1 crosswalk next block")
write(p, t)

# BU README
p = "secondary-witnesses/bharathiar-university/README.md"
t = read(p)
block = """### BU-SP1 later-established MATCHED payload Batch 1 — COMPLETE

Report: `comparisons/18-shower-of-poetry-vol-1-later-matched-payload-batch-01.md`. Compared entries **2, 5, 6, 7, 17, 20, 24, 29, 41 and 42** against actual BU payload, FINAL-CLEARED Tamil and RELEASE-CLEARED English. Result: **PASS / REPORT-ONLY — 10/10**, correction candidates **0 / 0**, Tamil / released-English mutations **0 / 0**. Historical payload closure remains **22/22 of the matches known at that stage**; the separate later-match debt is now **10/11 compared**, giving current MATCHED payload coverage **32/33**.

"""
t = insert_before_once(t, "## Next activity\n", block, "BU README next marker")
t = replace_once(t,
    "All **176/176** BU entries now have identity dispositions. Resume payload comparison for the **11 BU-SP1 entries matched only after the historical 22/22 payload lane had closed**. First batch: entries **2, 5, 6, 7, 17, 20, 24, 29, 41, 42**; entry **45** is the final remainder. Keep BU-SP2's 39 `NOT YET REPRESENTED` rows on source-acquisition hold absent new source evidence.",
    "All **176/176** BU entries have identity dispositions. Complete the remaining BU-SP1 later-match payload debt with **entry 45 — `A Petty Village Full of Folks Illiterate!` → `கலைஞரின் கவிதைகள்` item 67 `பாமரர் நிறைந்த பட்டிக்காடு!`**. Keep the historical 22/22 payload milestone distinct; current overall MATCHED payload coverage is **32/33**. BU-SP2's 39 `NOT YET REPRESENTED` rows remain on source-acquisition hold absent new source evidence.",
    "BU README next activity")
write(p, t)

# MASTER_CROSSWALK
p = "secondary-witnesses/bharathiar-university/MASTER_CROSSWALK.md"
t = read(p)
block = """## BU-SP1 later-established MATCHED payload Batch 1 — COMPLETE

Report: `comparisons/18-shower-of-poetry-vol-1-later-matched-payload-batch-01.md`. Entries **2, 5, 6, 7, 17, 20, 24, 29, 41 and 42** were compared against actual BU payload, FINAL-CLEARED Tamil and RELEASE-CLEARED English: **PASS / REPORT-ONLY — 10/10**, corrections/mutations **0 / 0**. The historical `SHOWER_OF_POETRY_VOL_1_22_MATCHED_SUMMARY.md` record remains exactly **22/22 of the matches known at that stage**. Separate later-match debt: **10/11 compared; entry 45 pending**. Overall current BU-SP1 MATCHED payload coverage: **32/33**.

"""
t = insert_before_once(t, "## Exact next activity\n", block, "MASTER next marker")
t = replace_once(t,
    "Identity classification is now complete for **176/176** BU entries. Start payload comparison of the **11 BU-SP1 matches established after the historical 22/22 payload lane closed**. First source-order batch: **2, 5, 6, 7, 17, 20, 24, 29, 41, 42**; final remainder: **45**. BU-SP2's 39 `NOT YET REPRESENTED` rows remain on source-acquisition hold absent new source evidence.",
    "Identity classification remains complete for **176/176** BU entries. Run the final later-established BU-SP1 MATCHED payload comparison: **entry 45 — `A Petty Village Full of Folks Illiterate!` → `poems/kalaignarin-kavithaigal/` item 67 `பாமரர் நிறைந்த பட்டிக்காடு!`**. Historical 22/22 payload closure remains untouched; current overall MATCHED payload coverage is **32/33**. BU-SP2's 39 `NOT YET REPRESENTED` rows remain on source-acquisition hold absent new source evidence.",
    "MASTER next activity")
write(p, t)

# Root HANDOVER
p = "HANDOVER.md"
t = read(p)
block = """## BU-SP1 later-established MATCHED payload Batch 1 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/18-shower-of-poetry-vol-1-later-matched-payload-batch-01.md`. Entries **2, 5, 6, 7, 17, 20, 24, 29, 41 and 42** were compared against actual BU-SP1 payload, FINAL-CLEARED Tamil and RELEASE-CLEARED English. Exact-source rendering beyond the 150-page viewer boundary reconfirmed Volume I at **249 pages / 101,936,284 bytes / SHA-256 `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536`** for entries 29, 41 and 42. Result: **PASS / REPORT-ONLY — 10/10**; source/Tamil correction candidates **0**; released-English correction candidates **0**; mutations **0 / 0**.

Historical BU-SP1 payload closure remains **22/22 of the matches known at that stage**. Separate later-match debt is **10/11 compared**, so current total MATCHED payload coverage is **32/33**. Do not rewrite the historical milestone as 32/32 or 33/33.

"""
t = insert_before_once(t, "## Exact next activity\n", block, "HANDOVER next marker")
old = """Run **BU-SP1 later-MATCHED payload comparison Batch 1** for entries **2, 5, 6, 7, 17, 20, 24, 29, 41 and 42** in source order. These 10 are part of the 11 identities established after the historical 22/22 payload lane closed; entry **45** is the final remainder. Compare actual BU payload with FINAL-CLEARED Tamil and RELEASE-CLEARED English and report differences. Do not mutate either layer unless the controlling Tamil independently supports a documented reopen.

BU-SP2's **39 NOT YET REPRESENTED** entries remain on source-acquisition hold absent new source evidence.
"""
new = """Run the final **BU-SP1 later-MATCHED payload remainder**: entry **45 — `A Petty Village Full of Folks Illiterate!`**, repository target `poems/kalaignarin-kavithaigal/` item **67 — `பாமரர் நிறைந்த பட்டிக்காடு!`**. Compare actual BU payload with FINAL-CLEARED Tamil and RELEASE-CLEARED English; report first. Do not mutate either layer unless the controlling Tamil independently supports a documented reopen.

BU-SP2's **39 NOT YET REPRESENTED** entries remain on source-acquisition hold absent new source evidence.
"""
t = replace_once(t, old, new, "HANDOVER exact next")
write(p, t)

# TRANSCRIPTION_PHASE_PLAN
p = "TRANSCRIPTION_PHASE_PLAN.md"
t = read(p)
block = """### BU-SP1 later-established MATCHED payload Batch 1 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/18-shower-of-poetry-vol-1-later-matched-payload-batch-01.md`. Entries **2, 5, 6, 7, 17, 20, 24, 29, 41 and 42** → **PASS / REPORT-ONLY — 10/10**, correction candidates **0 / 0**, Tamil / released-English mutations **0 / 0**. Historical payload milestone remains **22/22 of the matches known at that stage**; separate later-match debt is now **10/11**, total MATCHED payload coverage **32/33**.

"""
t = insert_before_once(t, "### Current comparison activity — NEXT\n", block, "PHASE next marker")
t = replace_once(t,
    "**BU-SP1 later-MATCHED payload comparison Batch 1 — entries 2, 5, 6, 7, 17, 20, 24, 29, 41 and 42 in source order.**",
    "**BU-SP1 later-MATCHED final payload remainder — entry 45 `A Petty Village Full of Folks Illiterate!` → item 67 `பாமரர் நிறைந்த பட்டிக்காடு!`.**",
    "PHASE current activity")
t = replace_once(t,
    "1. BU-SP1 — payload-compare the **11 later-established MATCHED** entries not included in the historical 22/22 payload lane: first batch **2, 5, 6, 7, 17, 20, 24, 29, 41, 42**, then final remainder **45**;",
    "1. BU-SP1 — complete the **1 remaining later-established MATCHED payload**: entry **45**; the first 10 later matches are report-complete and the historical 22/22 lane remains separately preserved;",
    "PHASE planned sequence")
t = replace_once(t,
    "Proceed with **BU-SP1 later-MATCHED payload comparison Batch 1 — entries 2, 5, 6, 7, 17, 20, 24, 29, 41, 42 — report-first comparison only**.",
    "Proceed with **BU-SP1 later-MATCHED final payload remainder — entry 45 → item 67 — report-first comparison only**.",
    "PHASE exact next")
write(p, t)

# Root README
p = "README.md"
t = read(p)
t = replace_once(t,
    "Exact next secondary-witness activity: **BU-SP1 later-MATCHED payload comparison Batch 1 — entries 2, 5, 6, 7, 17, 20, 24, 29, 41 and 42**. These identities were established after the historical 22/22 payload lane closed; compare them now without retroactively rewriting that historical count. Entry 45 is the final remainder.",
    "BU-SP1 later-established MATCHED payload Batch 1 is **COMPLETE — 10/10 / report-only / 0 mutations**. Historical payload closure remains **22/22 of the matches known at that stage**; separate later-match debt is **10/11**, so current MATCHED payload coverage is **32/33**. Exact next secondary-witness activity: **entry 45 `A Petty Village Full of Folks Illiterate!` → item 67 `பாமரர் நிறைந்த பட்டிக்காடு!`**.",
    "README top next")
t = replace_once(t,
    "Current next activity: **BU-SP1 later-MATCHED payload comparison Batch 1 — entries 2, 5, 6, 7, 17, 20, 24, 29, 41, 42; report first, no Tamil/released-English mutation without controlling-source support.**",
    "Current next activity: **BU-SP1 later-MATCHED final payload remainder — entry 45 `A Petty Village Full of Folks Illiterate!` → item 67 `பாமரர் நிறைந்த பட்டிக்காடு!`; report first, no Tamil/released-English mutation without controlling-source support.**",
    "README tail next")
write(p, t)

# NEXT_CHAT_PROMPT — replace with a concise live handoff for the final remainder.
p = "NEXT_CHAT_PROMPT.md"
write(p, """# Next Chat Prompt — Kalaignar Poems Archive / BU-SP1 Final Later-Matched Payload Remainder

Continue `pugazg/kalaignar-poems`, branch `main`. **Fetch live `main` first** and preserve every newer durable/release-cleared source, Tamil canonical and English release.

## Active lane

No new Tamil poem is staged. Work only in `secondary-witnesses/bharathiar-university/`.

## Authority

1. controlling historical Tamil scan;
2. FINAL-CLEARED repository Tamil canonical;
3. RELEASE-CLEARED repository English;
4. Bharathiar University 2009 English as institutional secondary/interpretive witness.

Never silently rewrite Tamil or RELEASE-CLEARED English from BU. A BU discrepancy may diagnose a problem; the controlling Tamil must independently support any correction.

## Durable BU state

- all **176/176** BU entries identity-classified;
- four-book identity tally: **68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE**;
- BU-TT comparison: **CLOSED 34/34**;
- BU-SP3 identity: **CLOSED 50/50**;
- BU-SP1 identity: **CLOSED 52/52 — 33 MATCHED / 19 NOT YET REPRESENTED**;
- historical BU-SP1 payload lane: **CLOSED 22/22 of the matches known at that stage** — do not relabel this 33/33;
- later-established BU-SP1 MATCHED payload Batch 1: **COMPLETE 10/10** — entries **2, 5, 6, 7, 17, 20, 24, 29, 41, 42**;
- report: `secondary-witnesses/bharathiar-university/comparisons/18-shower-of-poetry-vol-1-later-matched-payload-batch-01.md`;
- Batch-1 corrections/mutations: **0 / 0**;
- current overall BU-SP1 MATCHED payload coverage: **32/33**;
- remaining later-established payload debt: **1/11 — entry 45 only**.

## Exact BU-SP1 witness

`TVA_BOK_0065522_Shower_of_poetry_Vol_1.pdf`

- **249 physical pages**;
- **101,936,284 bytes**;
- SHA-256 `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536`.

The ordinary renderer may stop at 150 pages. Treat that only as a tooling boundary; use the exact checksum-locked source for later physical pages.

## Exact next activity

Compare the final later-established MATCHED remainder:

- BU-SP1 entry **45 — `A Petty Village Full of Folks Illiterate!`** — printed start p.190;
- repository target `poems/kalaignarin-kavithaigal/` item **67 — `பாமரர் நிறைந்த பட்டிக்காடு!`**;
- Tamil canonical: `poems/kalaignarin-kavithaigal/sections/67.md`;
- RELEASE-CLEARED English: `poems/kalaignarin-kavithaigal/translations/en/items/67-a-backwater-full-of-ignorant-folk-en.md`.

Read actual BU entry-45 payload from the exact witness and compare it first with FINAL-CLEARED Tamil, then RELEASE-CLEARED English. Classify title choice, interpretation, omission, expansion, transliteration/name choice, condensation or possible mistranslation. **Report first. Do not mutate Tamil or RELEASE-CLEARED English unless the controlling Tamil independently supports a documented reopen.**

After entry 45, close the separate 11/11 later-established MATCHED payload-debt lane and record total current BU-SP1 MATCHED payload coverage **33/33**, while preserving the historical 22/22 milestone as its own chronological record.

BU-SP2's **39 NOT YET REPRESENTED** rows remain on source-acquisition hold absent new source evidence.
""")
