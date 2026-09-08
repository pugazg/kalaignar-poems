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


# BU README
p = "secondary-witnesses/bharathiar-university/README.md"
t = read(p)
t = replace_once(t,
    "- Volume III: **50** — 0 MATCHED / 0 POSSIBLE / 30 NOT YET REPRESENTED / 20 INVESTIGATE;",
    "- Volume III: **50** — 0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE;",
    "BU README Volume III tally")
t = replace_once(t,
    "Current hardened crosswalk: **68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE = 176**.",
    "Current hardened crosswalk: **68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE = 176**.",
    "BU README aggregate")
block = """### BU-SP3 identity investigation Batch 4 — COMPLETE

Report: `comparisons/16-shower-of-poetry-vol-3-identity-investigation-batch-04.md`. Entries **31–40** were inspected from the exact Volume-III witness, physical pages **137–176** / printed pages **111–150**. The normal renderer covered physical pages 137–150; exact checksum-locked source rendering covered the later range beyond that tool boundary. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**; Tamil / RELEASE-CLEARED English mutations **0 / 0**. Current BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE = 50**.

"""
t = insert_before_once(t, "## Next activity\n", block, "BU README next marker")
t = replace_once(t,
    "Proceed to **BU-SP3 Identity Investigation Batch 4 — entries 31–40 in source order**. Use actual Volume-III payload/event/source context; report/crosswalk only; do not mutate FINAL-CLEARED Tamil or RELEASE-CLEARED English.",
    "Proceed to **BU-SP3 Identity Investigation Batch 5 — entries 41–50 in source order**. All remaining entries lie beyond the normal 150-page renderer window; use the exact checksum-locked 220-page Volume-III witness. Report/crosswalk only; do not mutate FINAL-CLEARED Tamil or RELEASE-CLEARED English.",
    "BU README next activity")
write(p, t)


# MASTER_CROSSWALK
p = "secondary-witnesses/bharathiar-university/MASTER_CROSSWALK.md"
t = read(p)
t = replace_once(t,
    "| BU-SP3 | *Shower of Poetry*, Volume III | 220 | 80,185,514 | `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` | 50 | 0 MATCHED / 0 POSSIBLE / 30 NOT YET REPRESENTED / 20 INVESTIGATE |",
    "| BU-SP3 | *Shower of Poetry*, Volume III | 220 | 80,185,514 | `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` | 50 | 0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE |",
    "master SP3 row")
t = replace_once(t,
    "**Total: 176 entries — 68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE.**",
    "**Total: 176 entries — 68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE.**",
    "master total")
block = """## BU-SP3 identity investigation Batch 4 — COMPLETE

Report: `comparisons/16-shower-of-poetry-vol-3-identity-investigation-batch-04.md`. Entries **31–40** → **NOT YET REPRESENTED** after exact-source payload review; no MATCHED or unresolved rows in the batch. Current BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE = 50**. Current four-book tally: **68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

"""
t = insert_before_once(t, "## Exact next activity\n", block, "master next marker")
t = replace_once(t,
    "Proceed to **BU-SP3 Identity Investigation Batch 4 — entries 31–40**. Harden identities only from actual Volume-III payload/event/source context and current repository inventories; report/crosswalk only.",
    "Proceed to **BU-SP3 Identity Investigation Batch 5 — entries 41–50**. Harden identities only from the exact 220-page Volume-III payload/event/source context and current repository inventories; report/crosswalk only.",
    "master next activity")
write(p, t)


# Root HANDOVER
p = "HANDOVER.md"
t = read(p)
t = replace_once(t,
    "Current hardened crosswalk: **176 entries = 68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE**.",
    "Current hardened crosswalk: **176 entries = 68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE**.",
    "handover current aggregate")
block = """## BU-SP3 identity investigation Batch 4 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/16-shower-of-poetry-vol-3-identity-investigation-batch-04.md`. Entries **31–40** were hardened **NOT YET REPRESENTED** from the exact Volume-III witness, physical pages **137–176** / printed pages **111–150**. The first part was directly visible in the normal renderer; the later range was rendered from independently checksum-verified exact bytes after reconfirming **220 pages / 80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6`**. Batch result: **PASS / REPORT-ONLY — 10/10; 0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**. BU-SP3 now stands at **0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE = 50**; four-book tally **68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

"""
t = insert_before_once(t, "## Exact next activity\n", block, "handover next marker")
t = replace_once(t,
    "Run **BU-SP3 Identity Investigation Batch 4 — entries 31–40 in source order**. Report/crosswalk only; no FINAL-CLEARED Tamil or RELEASE-CLEARED English mutation.",
    "Run **BU-SP3 Identity Investigation Batch 5 — entries 41–50 in source order**. All ten remaining entries are beyond the normal 150-page renderer window, so use the exact checksum-locked 220-page source. Report/crosswalk only; no FINAL-CLEARED Tamil or RELEASE-CLEARED English mutation.",
    "handover next activity")
write(p, t)


# TRANSCRIPTION_PHASE_PLAN
p = "TRANSCRIPTION_PHASE_PLAN.md"
t = read(p)
t = replace_once(t,
    "- classifications: **68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE**;",
    "- classifications: **68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE**;",
    "phase current classifications")
block = """### BU-SP3 identity investigation Batch 4 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/16-shower-of-poetry-vol-3-identity-investigation-batch-04.md`. Entries **31–40** → **10 NOT YET REPRESENTED**, with **0 MATCHED / 0 unresolved** and Tamil / released-English mutations **0 / 0**. Current BU-SP3: **0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE = 50**.

"""
t = insert_before_once(t, "### Current comparison activity — NEXT\n", block, "phase next marker")
t = replace_once(t,
    "**BU-SP3 Identity Investigation Batch 4 — entries 31–40 in source order.**",
    "**BU-SP3 Identity Investigation Batch 5 — entries 41–50 in source order.**",
    "phase current activity")
t = replace_once(t,
    "1. BU-SP3 — continue item-level matching of the **20 remaining INVESTIGATE** entries, next entries 31–40;",
    "1. BU-SP3 — complete item-level identity investigation of the **10 remaining INVESTIGATE** entries, entries 41–50, using exact-source rendering beyond the normal 150-page viewer boundary;",
    "phase planned sequence")
t = replace_once(t,
    "Proceed with **BU-SP3 Identity Investigation Batch 4 — entries 31–40 — identity/crosswalk report only**.",
    "Proceed with **BU-SP3 Identity Investigation Batch 5 — entries 41–50 — identity/crosswalk report only**.",
    "phase exact next")
write(p, t)
