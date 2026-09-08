from pathlib import Path
import re


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_required(text, old, new, label, count=None):
    n = text.count(old)
    if n == 0:
        raise SystemExit(f"{label}: old text not found")
    if count is not None and n != count:
        raise SystemExit(f"{label}: expected {count} occurrence(s), found {n}")
    return text.replace(old, new)


def insert_before(text, marker, block, label):
    if marker not in text:
        raise SystemExit(f"{label}: marker not found")
    return text.replace(marker, block + marker, 1)


# ---------------------------------------------------------------------------
# BU-SP3 crosswalk — close entries 41–50 and the identity lane.
# ---------------------------------------------------------------------------
p = "secondary-witnesses/bharathiar-university/shower-of-poetry-vol-3/crosswalk.md"
t = read(p)
rows = {
41: ("We Need to Cultivate a Mind for Service", 151, "10-01-2004 Netumaran / 18-month prison return / 1938 and Emergency banner-service reflection / Appar / Mother Teresa; no current source-backed representation established"),
42: ("The Umbrella of Power and the Umbrella of Victory", 155, "11-01-2004 transience meditation / power as water-bubble umbrella / enduring character, self-respect, honour and victory; no current representation established"),
43: ("Pieces of Straw on the Wavy Ocean", 160, "13-01-2004 widowhood / Bharathidasan `Kaimmai` / older remarriage verse / `vitavai`–`kaimpen` dot wordplay; distinct 2004 reflection, no current representation established"),
44: ("Piccaiyappan and Piccaiyappan", 163, "14-01-2004 Paccaiyappan / Piccaiyappan / Cinkarayar / dentist Paramanandam `showing teeth` comic wordplay; no current representation established"),
45: ("Let Progressiveness Blossom", 167, "15-01-2004 Pongal labour-poverty / farmhand / weaver / washerfolk / government employees and teachers / political-progress close; no current representation established"),
46: ("May You too Live Long Acquiring the Training I Have Acquired!", 170, "23-01-2004 meditation / `medicine and monkey` / yoga / breathing / walking / personal health-and-longevity practice; no current representation established"),
47: ("A Word of Counsel to Our Cricket Team", 174, "24-01-2004 cricket team-spirit versus individual scores / sportsmanship / advertising critique / political-party analogy; no current representation established"),
48: ("The Mother Who Voted for Tamil", 179, "03-02-2004 Inpacakaran / dying mother / Tamil classical-language election / mother votes for Tamil and dies / Mother-Tamil sacrifice allegory; no current representation established"),
49: ("This is a Book of History", 184, "19-02-2004 election-front / Dravidian youth / dictatorship and betrayal / Anna one-life principle / Party-Movement as history text; no current representation established"),
50: ("Opposition Will Go to Smithereens", 188, "17-04-2004 adversity / Anna abusive-hoarding-and-light counsel / heart that bears anything / opposition destroyed; no current representation established"),
}
for n, (title, page, note) in rows.items():
    old = f"| {n} | {title} | {page} | **INVESTIGATE** | — | item-level matching pending |"
    new = f"| {n} | {title} | {page} | **NOT YET REPRESENTED** | — | {note} |"
    t = replace_required(t, old, new, f"crosswalk row {n}", 1)

batch5 = """## Identity investigation Batch 5 — COMPLETE — 2026-09-08

Authority: `../comparisons/17-shower-of-poetry-vol-3-identity-investigation-batch-05.md`.

Entries **41–50** were inspected from the exact Volume-III witness, physical pages **177–215** / printed pages **151–189**. All ten entries lie beyond the ordinary 150-page renderer window, so the exact TDL source was independently reconfirmed at **220 pages / 80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6`** before direct rasterization. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**, Tamil / RELEASE-CLEARED English mutations **0 / 0**.

Consolidated identity closure: `../comparisons/SHOWER_OF_POETRY_VOL_3_IDENTITY_50_ENTRY_SUMMARY.md`.

"""
t = insert_before(t, "## Current tally\n", batch5, "crosswalk current tally")
t = replace_required(t,
    "**0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE = 50.**",
    "**0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE = 50 — IDENTITY CLOSED 50/50.**",
    "crosswalk tally", 1)
t = re.sub(
    r"## Exact next activity\n\nRun \*\*BU-SP3 Identity Investigation Batch 5 — entries 41–50 in source order\*\*\.[\s\S]*$",
    """## Exact next activity

BU-SP3 identity classification is **CLOSED 50/50**. The next actionable secondary-witness lane is payload comparison of the **11 BU-SP1 matches established after the historical 22/22 payload lane closed**.

Run the first source-order batch of ten later matches: **BU-SP1 entries 2, 5, 6, 7, 17, 20, 24, 29, 41 and 42**. Compare actual BU payload against FINAL-CLEARED repository Tamil and RELEASE-CLEARED English; report only unless the controlling Tamil independently supports a correction. Entry **45** remains the final one-item remainder after that batch.

Keep BU-SP2's **39 NOT YET REPRESENTED** rows on source-acquisition hold unless new source evidence establishes identities.
""",
    t,
    count=1,
)
write(p, t)


# ---------------------------------------------------------------------------
# BU-SP3 source metadata.
# ---------------------------------------------------------------------------
p = "secondary-witnesses/bharathiar-university/shower-of-poetry-vol-3/source.md"
t = read(p)
t = replace_required(t,
    "Batch 4 crossed that boundary. The exact TDL source was independently downloaded and reconfirmed at **80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` / 220 pages** before physical pages **149–176** were rasterized. English OCR was used only as a reading/navigation aid for this institutional English secondary witness; it did not reconstruct or mutate Tamil.",
    "Batches 4–5 crossed that boundary. The exact TDL source was independently downloaded and reconfirmed at **80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` / 220 pages** before later physical pages were rasterized; Batch 5 directly inspected physical pages **177–215** / printed **151–189**. English OCR was used only as a reading/navigation aid for this institutional English secondary witness; it did not reconstruct or mutate Tamil.",
    "source tooling note", 1)
t = replace_required(t,
    "See `../MASTER_CROSSWALK.md` and `crosswalk.md`. Initial onboarding left all 50 entries at `INVESTIGATE`; identity Batches 1–4 have now hardened entries **1–40** to `NOT YET REPRESENTED` from actual payload/context review. Current Volume-III state: **0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE = 50**. English title similarity alone is insufficient to assert canonical identity.",
    "See `../MASTER_CROSSWALK.md` and `crosswalk.md`. Initial onboarding left all 50 entries at `INVESTIGATE`; identity Batches 1–5 have now classified **all 50/50** entries from actual payload/event/date/person context. Final Volume-III state: **0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE = 50 — IDENTITY CLOSED**. English title similarity alone is insufficient to assert canonical identity. Consolidated closure: `../comparisons/SHOWER_OF_POETRY_VOL_3_IDENTITY_50_ENTRY_SUMMARY.md`.",
    "source repository use", 1)
write(p, t)


# ---------------------------------------------------------------------------
# Secondary-witness README.
# ---------------------------------------------------------------------------
p = "secondary-witnesses/bharathiar-university/README.md"
t = read(p)
t = replace_required(t,
    "- Volume III: **50** — 0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE;",
    "- Volume III: **50** — 0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE — identity CLOSED;",
    "BU README SP3 tally", 1)
t = replace_required(t,
    "Current hardened crosswalk: **68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE = 176**.",
    "Current hardened crosswalk: **68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE = 176 — 176/176 identity-classified**.",
    "BU README aggregate", 1)
batch5 = """### BU-SP3 identity investigation Batch 5 — COMPLETE / VOLUME III IDENTITY CLOSED 50/50

Report: `comparisons/17-shower-of-poetry-vol-3-identity-investigation-batch-05.md`; consolidated closure: `comparisons/SHOWER_OF_POETRY_VOL_3_IDENTITY_50_ENTRY_SUMMARY.md`. Entries **41–50**, physical pages **177–215** / printed pages **151–189**, were read from the exact checksum-locked 220-page witness. Result: **0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**, Tamil / RELEASE-CLEARED English mutations **0 / 0**. Final BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE = 50 — CLOSED**.

"""
t = insert_before(t, "## Next activity\n", batch5, "BU README next marker")
# Replace the first paragraph after Next activity irrespective of prior Batch-5 wording.
t = re.sub(
    r"## Next activity\n\n[\s\S]*$",
    """## Next activity

All **176/176** BU entries now have identity dispositions. Resume payload comparison for the **11 BU-SP1 entries matched only after the historical 22/22 payload lane had closed**. First batch: entries **2, 5, 6, 7, 17, 20, 24, 29, 41, 42**; entry **45** is the final remainder. Keep BU-SP2's 39 `NOT YET REPRESENTED` rows on source-acquisition hold absent new source evidence.
""",
    t,
    count=1,
)
write(p, t)


# ---------------------------------------------------------------------------
# MASTER_CROSSWALK.
# ---------------------------------------------------------------------------
p = "secondary-witnesses/bharathiar-university/MASTER_CROSSWALK.md"
t = read(p)
t = replace_required(t,
    "| BU-SP3 | *Shower of Poetry*, Volume III | 220 | 80,185,514 | `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` | 50 | 0 MATCHED / 0 POSSIBLE / 40 NOT YET REPRESENTED / 10 INVESTIGATE |",
    "| BU-SP3 | *Shower of Poetry*, Volume III | 220 | 80,185,514 | `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6` | 50 | 0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE — CLOSED |",
    "master SP3 row", 1)
t = replace_required(t,
    "**Total: 176 entries — 68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE.**",
    "**Total: 176 entries — 68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE — 176/176 identity-classified.**",
    "master total", 1)
batch5 = """## BU-SP3 identity investigation Batch 5 — COMPLETE / IDENTITY CLOSED 50/50

Report: `comparisons/17-shower-of-poetry-vol-3-identity-investigation-batch-05.md`; consolidated closure: `comparisons/SHOWER_OF_POETRY_VOL_3_IDENTITY_50_ENTRY_SUMMARY.md`. Entries **41–50** → **10 NOT YET REPRESENTED** after exact-source payload review, with **0 MATCHED / 0 unresolved**. Final BU-SP3 state: **0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE = 50**. Current four-book tally: **68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

"""
t = insert_before(t, "## Exact next activity\n", batch5, "master next marker")
t = re.sub(
    r"## Exact next activity\n\n[\s\S]*$",
    """## Exact next activity

Identity classification is now complete for **176/176** BU entries. Start payload comparison of the **11 BU-SP1 matches established after the historical 22/22 payload lane closed**. First source-order batch: **2, 5, 6, 7, 17, 20, 24, 29, 41, 42**; final remainder: **45**. BU-SP2's 39 `NOT YET REPRESENTED` rows remain on source-acquisition hold absent new source evidence.
""",
    t,
    count=1,
)
write(p, t)


# ---------------------------------------------------------------------------
# Root README.
# ---------------------------------------------------------------------------
p = "README.md"
t = read(p)
t = replace_required(t,
    "Current hardened state after BU-SP1 identity closure and BU-SP3 Batches 1–4: **68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE**.",
    "Current hardened state after BU-SP1 and BU-SP3 identity closure: **176/176 identity-classified — 68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE**.",
    "root README aggregate", 1)
t = replace_required(t,
    "Exact next secondary-witness activity: **BU-SP3 Identity Investigation Batch 5 — Volume-III entries 41–50; report/crosswalk only, no Tamil or released-English mutation.** Because all ten remaining entries are beyond the ordinary 150-page renderer window, use the exact checksum-locked 220-page source rather than treating that tool boundary as the end of the book.",
    "Exact next secondary-witness activity: **BU-SP1 later-MATCHED payload comparison Batch 1 — entries 2, 5, 6, 7, 17, 20, 24, 29, 41 and 42**. These identities were established after the historical 22/22 payload lane closed; compare them now without retroactively rewriting that historical count. Entry 45 is the final remainder.",
    "root README next", 1)
t = replace_required(t,
    "Current next activity: **BU-SP3 Identity Investigation Batch 5 — entries 41–50; report/crosswalk only.**",
    "Current next activity: **BU-SP1 later-MATCHED payload comparison Batch 1 — entries 2, 5, 6, 7, 17, 20, 24, 29, 41, 42; report first, no Tamil/released-English mutation without controlling-source support.**",
    "root README bottom next", 1)
write(p, t)


# ---------------------------------------------------------------------------
# Root HANDOVER.
# ---------------------------------------------------------------------------
p = "HANDOVER.md"
t = read(p)
t = replace_required(t,
    "Current hardened crosswalk: **176 entries = 68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE**.",
    "Current hardened crosswalk: **176/176 identity-classified = 68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE**.",
    "handover aggregate", 1)
batch5 = """## BU-SP3 identity investigation Batch 5 — COMPLETE / VOLUME III IDENTITY CLOSED 50/50

Report: `secondary-witnesses/bharathiar-university/comparisons/17-shower-of-poetry-vol-3-identity-investigation-batch-05.md`; consolidated closure: `secondary-witnesses/bharathiar-university/comparisons/SHOWER_OF_POETRY_VOL_3_IDENTITY_50_ENTRY_SUMMARY.md`. Entries **41–50** were hardened **NOT YET REPRESENTED** from the exact Volume-III witness, physical pages **177–215** / printed **151–189**. The exact TDL source was reconfirmed at **220 pages / 80,185,514 bytes / SHA-256 `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6`** before rasterization. Batch result: **PASS / REPORT-ONLY — 10/10; 0 MATCHED / 10 NOT YET REPRESENTED / 0 unresolved**. Final BU-SP3: **0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE = 50 — CLOSED**; four-book tally **68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE = 176**. Tamil / released-English mutations: **0 / 0**.

"""
t = insert_before(t, "## Exact next activity\n", batch5, "handover next marker")
t = re.sub(
    r"## Exact next activity\n\n[\s\S]*$",
    """## Exact next activity

Run **BU-SP1 later-MATCHED payload comparison Batch 1** for entries **2, 5, 6, 7, 17, 20, 24, 29, 41 and 42** in source order. These 10 are part of the 11 identities established after the historical 22/22 payload lane closed; entry **45** is the final remainder. Compare actual BU payload with FINAL-CLEARED Tamil and RELEASE-CLEARED English and report differences. Do not mutate either layer unless the controlling Tamil independently supports a documented reopen.

BU-SP2's **39 NOT YET REPRESENTED** entries remain on source-acquisition hold absent new source evidence.
""",
    t,
    count=1,
)
write(p, t)


# ---------------------------------------------------------------------------
# TRANSCRIPTION_PHASE_PLAN.
# ---------------------------------------------------------------------------
p = "TRANSCRIPTION_PHASE_PLAN.md"
t = read(p)
t = replace_required(t,
    "- classifications: **68 MATCHED / 0 POSSIBLE / 98 NOT YET REPRESENTED / 10 INVESTIGATE**;",
    "- classifications: **176/176 identity-classified — 68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE**;",
    "phase classifications", 1)
batch5 = """### BU-SP3 identity investigation Batch 5 — COMPLETE / IDENTITY CLOSED 50/50

Report: `secondary-witnesses/bharathiar-university/comparisons/17-shower-of-poetry-vol-3-identity-investigation-batch-05.md`; consolidated closure: `secondary-witnesses/bharathiar-university/comparisons/SHOWER_OF_POETRY_VOL_3_IDENTITY_50_ENTRY_SUMMARY.md`. Entries **41–50** → **10 NOT YET REPRESENTED**, with **0 MATCHED / 0 unresolved** and Tamil / released-English mutations **0 / 0**. Final BU-SP3: **0 MATCHED / 0 POSSIBLE / 50 NOT YET REPRESENTED / 0 INVESTIGATE = 50 — CLOSED**.

"""
t = insert_before(t, "### Current comparison activity — NEXT\n", batch5, "phase current marker")
t = replace_required(t,
    "**BU-SP3 Identity Investigation Batch 5 — entries 41–50 in source order.**",
    "**BU-SP1 later-MATCHED payload comparison Batch 1 — entries 2, 5, 6, 7, 17, 20, 24, 29, 41 and 42 in source order.**",
    "phase current activity", 1)
t = re.sub(
    r"### Planned witness sequence\n\n1\. BU-SP3 — complete item-level identity investigation of the \*\*10 remaining INVESTIGATE\*\* entries, entries 41–50, using exact-source rendering beyond the normal 150-page viewer boundary;\n2\. BU-SP2 — retain its 39 NOT YET REPRESENTED entries until source-backed identities are established or a new controlling/source witness is supplied\.",
    """### Planned witness sequence

1. BU-SP1 — payload-compare the **11 later-established MATCHED** entries not included in the historical 22/22 payload lane: first batch **2, 5, 6, 7, 17, 20, 24, 29, 41, 42**, then final remainder **45**;
2. BU-SP2 — retain its **39 NOT YET REPRESENTED** entries on source-acquisition hold until source-backed identities are established or a new controlling/source witness is supplied.
""",
    t,
    count=1,
)
t = replace_required(t,
    "Proceed with **BU-SP3 Identity Investigation Batch 5 — entries 41–50 — identity/crosswalk report only**.",
    "Proceed with **BU-SP1 later-MATCHED payload comparison Batch 1 — entries 2, 5, 6, 7, 17, 20, 24, 29, 41, 42 — report-first comparison only**.",
    "phase exact next", 1)
write(p, t)


# ---------------------------------------------------------------------------
# NEXT_CHAT_PROMPT — replace wholesale so the handoff cannot remain stale.
# ---------------------------------------------------------------------------
p = "NEXT_CHAT_PROMPT.md"
next_prompt = """# Next Chat Prompt — Kalaignar Poems Archive / Bharathiar University Secondary Witnesses

Continue `pugazg/kalaignar-poems`, branch `main`. **Fetch live `main` first** and preserve every newer durable/release-cleared source, Tamil canonical and English release.

## Active lane

No new Tamil poem is staged. Current activity remains `secondary-witnesses/bharathiar-university/`.

Read before further witness work:

1. `POEM_PROCESSING_GUIDE.md`;
2. `WAVE4_CROSS_WITNESS_AUDIT.md`;
3. root `HANDOVER.md`;
4. `TRANSCRIPTION_PHASE_PLAN.md`;
5. this prompt;
6. `secondary-witnesses/bharathiar-university/README.md`;
7. `secondary-witnesses/bharathiar-university/MASTER_CROSSWALK.md`;
8. `secondary-witnesses/bharathiar-university/comparisons/SHOWER_OF_POETRY_VOL_1_22_MATCHED_SUMMARY.md`;
9. `secondary-witnesses/bharathiar-university/comparisons/SHOWER_OF_POETRY_VOL_1_IDENTITY_52_ENTRY_SUMMARY.md`;
10. `secondary-witnesses/bharathiar-university/comparisons/SHOWER_OF_POETRY_VOL_3_IDENTITY_50_ENTRY_SUMMARY.md`;
11. the relevant BU-SP1 per-book `source.md` / `crosswalk.md` and the final BU-SP3 Batch-5 report for historical context.

## Authority

1. controlling historical Tamil scan;
2. FINAL-CLEARED repository Tamil canonical;
3. RELEASE-CLEARED repository English;
4. Bharathiar University 2009 English as institutional secondary/interpretive witness.

Never silently rewrite Tamil or RELEASE-CLEARED English from the Bharathiar books. A secondary witness may diagnose a problem; the controlling Tamil must independently support any correction.

## Exact witness set

- BU-SP1 — *Shower of Poetry*, Volume I — **249 pages / 101,936,284 bytes / SHA `f353a833679b1aa743b07ac0e586d99a43ca77ebfe14822e26879f0c5f9a7536`**;
- BU-SP2 — *Shower of Poetry*, Volume II — **168 pages / 156,922,680 bytes / SHA `e29c294adfe94c508cdb8aeb4f8cadf116b8dc1bdeb4025eef86a7a017f02a31`**;
- BU-SP3 — *Shower of Poetry*, Volume III — **220 pages / 80,185,514 bytes / SHA `90d64eb19a75c93ae78a5081fe1f6ad1733fc92dff1568e65eadb6bb5213afb6`**;
- BU-TT — *The Treasure Trove of Time and the Verse Key* — **205 pages / 106,152,046 bytes / SHA `17ecd31500ad67ec34d684a8c2d0d208866fd5bca3f630a2941c50baa3b86d4b`**.

## Closed identity / comparison lanes

- BU-TT comparison: **CLOSED 34/34**;
- BU-SP1 identity classification: **CLOSED 52/52 — 33 MATCHED / 19 NOT YET REPRESENTED**;
- BU-SP3 identity classification: **CLOSED 50/50 — 0 MATCHED / 50 NOT YET REPRESENTED**;
- all BU contents entries now identity-classified: **176/176 — 68 MATCHED / 0 POSSIBLE / 108 NOT YET REPRESENTED / 0 INVESTIGATE**.

BU-SP3 Batch 5 report: `comparisons/17-shower-of-poetry-vol-3-identity-investigation-batch-05.md`. Entries **41–50** were read from exact physical pages **177–215** beyond the normal 150-page renderer boundary after checksum/page-count reconfirmation. Result: **10 NOT YET REPRESENTED**, mutations **0 / 0**.

## Important BU-SP1 payload-count distinction

The historical BU-SP1 payload-comparison lane is **CLOSED 22/22 of the matches known at that stage**. Later identity work established **11 additional MATCHED entries**:

**2, 5, 6, 7, 17, 20, 24, 29, 41, 42, 45.**

Do **not** retroactively describe the historical lane as 33/33. These eleven form a new, explicitly separate payload-comparison debt.

## Exact next activity — BU-SP1 later-MATCHED payload comparison Batch 1

Compare the first ten later matches in source order:

1. entry **2** `Periyar`;
2. entry **5** `Green Parrot!`;
3. entry **6** `The Mother in Puranaanooru - 2`;
4. entry **7** `A Heroic Warrior Killed`;
5. entry **17** `The Paari Festival`;
6. entry **20** `The Fountain of Imagination`;
7. entry **24** `Pour Plenteously O Sky!`;
8. entry **29** `Some Countries there are!`;
9. entry **41** `Do Not Your Onward March Give up!`;
10. entry **42** `We Shall Tear the Mask to Pieces!`.

Repository targets are recorded in the BU-SP1 consolidated identity summary. Read the actual BU payloads and compare them with FINAL-CLEARED repository Tamil first, then RELEASE-CLEARED English. Classify differences as title choice, interpretation, omission, expansion, transliteration/name choice, structural condensation or possible mistranslation.

Report first. **Do not mutate FINAL-CLEARED Tamil or RELEASE-CLEARED English unless the controlling Tamil independently supports a documented reopen.**

After Batch 1, entry **45** `A Petty Village Full of Folks Illiterate!` is the final later-MATCHED remainder.

BU-SP2's **39 NOT YET REPRESENTED** rows remain on source-acquisition hold absent new source evidence.
"""
write(p, next_prompt)

print("BU-SP3 Batch 5 durable state synchronized")
