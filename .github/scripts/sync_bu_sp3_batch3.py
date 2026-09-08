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


# BU README
p = "secondary-witnesses/bharathiar-university/README.md"
t = read(p)
t = replace_once(
    t,
    "- Volume III: **50** — 0 MATCHED / 0 POSSIBLE / 20 NOT YET REPRESENTED / 30 INVESTIGATE;",
    "- Volume III: **50** — 0 MATCHED / 0 POSSIBLE / 30 NOT YET REPRESENTED / 20 INVESTIGATE;",
    "BU README Volume III tally",
)
t = replace_once(
    t,
    "Current hardened crosswalk: **68 MATCHED / 0 POSSIBLE / 78 NOT YET REPRESENTED / 30 INVESTIGATE = 176**.",
    "Current hardened crosswalk: **68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE = 176**.",
    "BU README aggregate",
)
old = """### BU-SP3 identity investigation Batch 2 — COMPLETE

Report: `comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** were inspected from actual Volume-III page images, physical pages **60–99** / printed pages **34–73**. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**; Tamil / RELEASE-CLEARED English mutations **0 / 0**. Current BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 20 NOT YET REPRESENTED / 30 INVESTIGATE = 50**.

## Next activity

Proceed to **BU-SP3 Identity Investigation Batch 3 — entries 21–30 in source order**. Use actual Volume-III payload/event/source context; report/crosswalk only; do not mutate FINAL-CLEARED Tamil or RELEASE-CLEARED English."""
new = """### BU-SP3 identity investigation Batch 2 — COMPLETE

Report: `comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** were inspected from actual Volume-III page images, physical pages **60–99** / printed pages **34–73**. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**; Tamil / RELEASE-CLEARED English mutations **0 / 0**.

### BU-SP3 identity investigation Batch 3 — COMPLETE

Report: `comparisons/15-shower-of-poetry-vol-3-identity-investigation-batch-03.md`. Entries **21–30** were inspected from actual Volume-III page images, physical pages **100–136** / printed pages **74–110**. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**; Tamil / RELEASE-CLEARED English mutations **0 / 0**. Current BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 30 NOT YET REPRESENTED / 20 INVESTIGATE = 50**.

## Next activity

Proceed to **BU-SP3 Identity Investigation Batch 4 — entries 31–40 in source order**. Use actual Volume-III payload/event/source context; report/crosswalk only; do not mutate FINAL-CLEARED Tamil or RELEASE-CLEARED English."""
t = replace_once(t, old, new, "BU README Batch 3 tail")
write(p, t)


# MASTER_CROSSWALK
p = "secondary-witnesses/bharathiar-university/MASTER_CROSSWALK.md"
t = read(p)
t = replace_once(
    t,
    "| BU-SP3 | *Shower of Poetry*, Volume III | 220 | 80,185,514 | `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` | 50 | 0 MATCHED / 0 POSSIBLE / 20 NOT YET REPRESENTED / 30 INVESTIGATE |",
    "| BU-SP3 | *Shower of Poetry*, Volume III | 220 | 80,185,514 | `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` | 50 | 0 MATCHED / 0 POSSIBLE / 30 NOT YET REPRESENTED / 20 INVESTIGATE |",
    "master SP3 row",
)
t = replace_once(
    t,
    "**Total: 176 entries — 68 MATCHED / 0 POSSIBLE / 78 NOT YET REPRESENTED / 30 INVESTIGATE.**",
    "**Total: 176 entries — 68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE.**",
    "master total",
)
old = """## BU-SP3 identity investigation Batch 2 — COMPLETE

Report: `comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** → **NOT YET REPRESENTED** after direct page-image/payload review; no MATCHED or unresolved rows in the batch. Current BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 20 NOT YET REPRESENTED / 30 INVESTIGATE = 50**. Current four-book tally: **68 MATCHED / 0 POSSIBLE / 78 NOT YET REPRESENTED / 30 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

## Exact next activity

Proceed to **BU-SP3 Identity Investigation Batch 3 — entries 21–30**. Harden identities only from actual Volume-III payload/event/source context and current repository inventories; report/crosswalk only."""
new = """## BU-SP3 identity investigation Batch 2 — COMPLETE

Report: `comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** → **NOT YET REPRESENTED** after direct page-image/payload review; no MATCHED or unresolved rows in the batch. Tamil / released-English mutations: **0 / 0**.

## BU-SP3 identity investigation Batch 3 — COMPLETE

Report: `comparisons/15-shower-of-poetry-vol-3-identity-investigation-batch-03.md`. Entries **21–30** → **NOT YET REPRESENTED** after direct page-image/payload review; no MATCHED or unresolved rows in the batch. Current BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 30 NOT YET REPRESENTED / 20 INVESTIGATE = 50**. Current four-book tally: **68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

## Exact next activity

Proceed to **BU-SP3 Identity Investigation Batch 4 — entries 31–40**. Harden identities only from actual Volume-III payload/event/source context and current repository inventories; report/crosswalk only."""
t = replace_once(t, old, new, "master Batch 3 tail")
write(p, t)


# Root HANDOVER
p = "HANDOVER.md"
t = read(p)
t = replace_once(
    t,
    "Current hardened crosswalk: **176 entries = 68 MATCHED / 0 POSSIBLE / 78 NOT YET REPRESENTED / 30 INVESTIGATE**.",
    "Current hardened crosswalk: **176 entries = 68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE**.",
    "handover current aggregate",
)
old = """Report: `secondary-witnesses/bharathiar-university/comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** were hardened **NOT YET REPRESENTED** from direct physical pages **60–99** / printed pages **34–73**. Batch result: **PASS / REPORT-ONLY — 10/10; 0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**. BU-SP3 now stands at **0 MATCHED / 0 POSSIBLE / 20 NOT YET REPRESENTED / 30 INVESTIGATE = 50**; four-book tally **68 MATCHED / 0 POSSIBLE / 78 NOT YET REPRESENTED / 30 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

## Exact next activity

Run **BU-SP3 Identity Investigation Batch 3 — entries 21–30 in source order**. Report/crosswalk only; no FINAL-CLEARED Tamil or RELEASE-CLEARED English mutation."""
new = """Report: `secondary-witnesses/bharathiar-university/comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** were hardened **NOT YET REPRESENTED** from direct physical pages **60–99** / printed pages **34–73**. Batch result: **PASS / REPORT-ONLY — 10/10; 0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**. Tamil / released-English mutations: **0 / 0**.

## BU-SP3 identity investigation Batch 3 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/15-shower-of-poetry-vol-3-identity-investigation-batch-03.md`. Entries **21–30** were hardened **NOT YET REPRESENTED** from direct physical pages **100–136** / printed pages **74–110**. Batch result: **PASS / REPORT-ONLY — 10/10; 0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**. BU-SP3 now stands at **0 MATCHED / 0 POSSIBLE / 30 NOT YET REPRESENTED / 20 INVESTIGATE = 50**; four-book tally **68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

## Exact next activity

Run **BU-SP3 Identity Investigation Batch 4 — entries 31–40 in source order**. Report/crosswalk only; no FINAL-CLEARED Tamil or RELEASE-CLEARED English mutation."""
t = replace_once(t, old, new, "handover Batch 3 tail")
write(p, t)


# TRANSCRIPTION_PHASE_PLAN
p = "TRANSCRIPTION_PHASE_PLAN.md"
t = read(p)
t = replace_once(
    t,
    "- classifications: **68 MATCHED / 0 POSSIBLE / 58 NOT YET REPRESENTED / 50 INVESTIGATE**;",
    "- classifications: **68 MATCHED / 0 POSSIBLE / 88 NOT YET REPRESENTED / 20 INVESTIGATE**;",
    "phase current classifications",
)
old = """### BU-SP3 identity investigation Batch 2 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** → **10 NOT YET REPRESENTED**, with **0 MATCHED / 0 unresolved** and Tamil / released-English mutations **0 / 0**. Current BU-SP3: **0 MATCHED / 0 POSSIBLE / 20 NOT YET REPRESENTED / 30 INVESTIGATE = 50**.

### Current comparison activity — NEXT

**BU-SP3 Identity Investigation Batch 3 — entries 21–30 in source order.**

### Planned witness sequence

1. BU-SP3 — continue item-level matching of the **30 remaining INVESTIGATE** entries, next entries 21–30;
2. BU-SP2 — retain its 39 NOT YET REPRESENTED entries until source-backed identities are established or a new controlling/source witness is supplied.

## Most recently completed Tamil work — தலைகேட்டான் தம்பி — 1966

Phase 1–4 complete; Tamil FINAL-CLEARED; English RELEASE-CLEARED; status **CLOSED — 2026-09-08**. Other release-cleared work remains frozen.

## Exact next activity

Proceed with **BU-SP3 Identity Investigation Batch 3 — entries 21–30 — identity/crosswalk report only**."""
new = """### BU-SP3 identity investigation Batch 2 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/14-shower-of-poetry-vol-3-identity-investigation-batch-02.md`. Entries **11–20** → **10 NOT YET REPRESENTED**, with **0 MATCHED / 0 unresolved** and Tamil / released-English mutations **0 / 0**.

### BU-SP3 identity investigation Batch 3 — COMPLETE

Report: `secondary-witnesses/bharathiar-university/comparisons/15-shower-of-poetry-vol-3-identity-investigation-batch-03.md`. Entries **21–30** → **10 NOT YET REPRESENTED**, with **0 MATCHED / 0 unresolved** and Tamil / released-English mutations **0 / 0**. Current BU-SP3: **0 MATCHED / 0 POSSIBLE / 30 NOT YET REPRESENTED / 20 INVESTIGATE = 50**.

### Current comparison activity — NEXT

**BU-SP3 Identity Investigation Batch 4 — entries 31–40 in source order.**

### Planned witness sequence

1. BU-SP3 — continue item-level matching of the **20 remaining INVESTIGATE** entries, next entries 31–40;
2. BU-SP2 — retain its 39 NOT YET REPRESENTED entries until source-backed identities are established or a new controlling/source witness is supplied.

## Most recently completed Tamil work — தலைகேட்டான் தம்பி — 1966

Phase 1–4 complete; Tamil FINAL-CLEARED; English RELEASE-CLEARED; status **CLOSED — 2026-09-08**. Other release-cleared work remains frozen.

## Exact next activity

Proceed with **BU-SP3 Identity Investigation Batch 4 — entries 31–40 — identity/crosswalk report only**."""
t = replace_once(t, old, new, "phase Batch 3 tail")
write(p, t)
