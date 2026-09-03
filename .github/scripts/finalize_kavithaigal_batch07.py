#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path('.')
A = Path('poems/kalaignarin-kavithaigal')
T = A / 'translations/en'

items = {
    21: ('21-silver-jubilee-en.md', list(range(218, 227))),
    22: ('22-anna-is-here-en.md', list(range(227, 230))),
    23: ('23-anna-a-poetry-assembly-en.md', [230,231,232,233,234,235,236,238]),
    24: ('24-a-walking-journey-for-tamil-to-flourish-en.md', [237,239,240,241,242,243,244]),
    25: ('25-for-the-world-to-flourish-en.md', list(range(245, 254))),
}


def read(p):
    return p.read_text(encoding='utf-8')


def write(p, s):
    p.write_text(s, encoding='utf-8')


def must_replace(text, old, new, count=1, label=''):
    if old not in text:
        raise SystemExit(f'missing expected text {label or old[:100]!r}')
    return text.replace(old, new, count)


def replace_if(text, old, new, count=1):
    if old in text:
        return text.replace(old, new, count)
    return text


# 1. Mechanical certification and promotion of item status.
for num, (name, expected) in items.items():
    p = T / 'items' / name
    s = read(p)
    markers = [int(x) for x in re.findall(r'<!-- scan (\d+) -->', s)]
    if markers != expected:
        raise SystemExit(f'item {num} scan markers mismatch: {markers} != {expected}')
    if f'item: {num}\n' not in s:
        raise SystemExit(f'item {num} identity missing')
    if 'title_witness_status: "exact"' not in s:
        raise SystemExit(f'item {num} title witness not exact')
    if num == 23 and 237 in markers:
        raise SystemExit('item 23 incorrectly contains scan 237')
    if num == 24 and 238 in markers:
        raise SystemExit('item 24 incorrectly contains scan 238')
    s = must_replace(s, 'status: "batch-review-pending"', 'status: "batch-reviewed"', 1, f'item {num} pending status')
    write(p, s)

# 2. Batch-07 review record.
p = T / 'batches/batch-07.md'
s = read(p)
s = must_replace(s, '**REVIEWED — PASS, pending final mechanical/status certification.**', '**REVIEWED — PASS.**', 1, 'batch07 status')
if '## Certification result' not in s:
    s += '''\n\n## Certification result\n\n- exact scan-marker sequences: **36/36 PASS**;\n- item identities: **5/5 PASS**;\n- title witnesses: **5 exact / 0 variants / 0 unresolved**;\n- item-23/item-24 physical interposition: **PASS**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes: **0**;\n- Tamil `sections/` changes: **0**.\n'''
write(p, s)

# 3. English translation README.
p = T / 'README.md'; s = read(p)
s = must_replace(s, '**PHASE 4 IN PROGRESS — Batches 01–06 reviewed PASS.**', '**PHASE 4 IN PROGRESS — Batches 01–07 reviewed PASS.**', 1)
s = must_replace(s, '- reviewed English batches: **6**;', '- reviewed English batches: **7**;', 1)
s = must_replace(s, '- reviewed English items: **20/77**;', '- reviewed English items: **25/77**;', 1)
s = must_replace(s, '- item-assigned source scans covered by reviewed English: **196/439**;', '- item-assigned source scans covered by reviewed English: **232/439**;', 1)
anchor = '- `items/20-thank-you-thank-you-en.md` — reviewed English item 20.\n'
add = '''- `items/20-thank-you-thank-you-en.md` — reviewed English item 20.\n- `batches/batch-07.md` — reviewed Batch-07 record;\n- `items/21-silver-jubilee-en.md` — reviewed English item 21;\n- `items/22-anna-is-here-en.md` — reviewed English item 22;\n- `items/23-anna-a-poetry-assembly-en.md` — reviewed English item 23;\n- `items/24-a-walking-journey-for-tamil-to-flourish-en.md` — reviewed English item 24;\n- `items/25-for-the-world-to-flourish-en.md` — reviewed English item 25.\n'''
s = must_replace(s, anchor, add, 1, 'translation README item20 inventory')
old = '''## Exact next activity\n\nExecute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Item-owned scans total **36/36** across physical interval **218–253**. Preserve the intentional source interposition **230–236 → 237 → 238 → 239–244** exactly.\n'''
new = '''## Batch 07\n\n**Reviewed — PASS.**\n\nStanding five-poem iteration covering items **21–25** with **36/36** item-owned scans.\n\n- item 21 `வெள்ளி விழா` → **Silver Jubilee**, scans **218–226**;\n- item 22 `அண்ணன் இருக்கின்றார்` → **Anna Is Here**, scans **227–229**;\n- item 23 `அண்ணன் ஒரு கவியரங்கம்` → **Anna, a Poetry Assembly**, scans **230–236, 238**;\n- item 24 `தமிழ் வளர வழிநடைப் பயணம்` → **A Walking Journey for Tamil to Flourish**, scans **237, 239–244**;\n- item 25 `வையம் தழைக்க` → **For the World to Flourish**, scans **245–253**;\n- title witnesses: **5 exact / 0 variants**;\n- intentional physical interposition: **preserved**;\n- unresolved translation issues: **0**;\n- Tamil changes: **0**.\n\n## Exact next activity\n\nExecute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**.\n'''
s = must_replace(s, old, new, 1, 'translation README next')
write(p, s)

# 4. Translation plan.
p = T / 'TRANSLATION_PLAN.md'; s = read(p)
s = must_replace(s, '**PHASE 4 IN PROGRESS — Batches 01–06 reviewed PASS.**', '**PHASE 4 IN PROGRESS — Batches 01–07 reviewed PASS.**', 1)
s = must_replace(s, '- batches: **6**;', '- batches: **7**;', 1)
s = must_replace(s, '- items: **20/77**;', '- items: **25/77**;', 1)
s = must_replace(s, '- item-assigned source scans: **196/439**;', '- item-assigned source scans: **232/439**;', 1)
s = must_replace(s, '| 07 | 21–25 | 218–253 | **NEXT** |\n| later | 26–77 | five complete items per iteration (final remainder excepted) | pending |', '| 07 | 21–25 | 218–253 | **reviewed — PASS** |\n| 08 | 26–30 | 254–292 | **NEXT** |\n| later | 31–77 | five complete items per iteration (final remainder excepted) | pending |', 1, 'plan table')
old = '''## Exact next activity\n\nExecute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Preserve item 23 scans **230–236, 238** and item 24 scans **237, 239–244** without source reordering; the physical sequence **230–236 → 237 → 238 → 239–244** is intentional.\n'''
new = '''## Batch 07 decision record\n\nBatch 07 reviewed complete items **21–25** across **36/36 item-owned scans**. All five title witnesses are exact. The reviewed translations preserve the Silver-Jubilee freedom-fighter sequence; Anna-presence elegy; Anna-as-*kaviyarangam* conceit and movement/state-rights rhetoric; the eight-path Pari-festival journey; and the six-theme `-ஆல்` New-Year structure. The intentional item-23/item-24 physical interposition **230–236 → 237 → 238 → 239–244** is preserved exactly. Tamil `pages/`/`sections/` changes remain **0**.\n\n## Exact next activity\n\nExecute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**.\n'''
s = must_replace(s, old, new, 1, 'plan next')
write(p, s)

# 5. Source map.
p = T / 'SOURCE_MAP.md'; s = read(p)
anchor = '| 20 | `நன்றி, நன்றி!` | `நன்றி, நன்றி!` | **Thank You, Thank You!** | 216–217 | 199–200 | `items/20-thank-you-thank-you-en.md` | **batch-reviewed — PASS** |\n'
rows = '''| 20 | `நன்றி, நன்றி!` | `நன்றி, நன்றி!` | **Thank You, Thank You!** | 216–217 | 199–200 | `items/20-thank-you-thank-you-en.md` | **batch-reviewed — PASS** |\n| 21 | `வெள்ளி விழா` | `வெள்ளி விழா` | **Silver Jubilee** | 218–226 | 201–209 | `items/21-silver-jubilee-en.md` | **batch-reviewed — PASS** |\n| 22 | `அண்ணன் இருக்கின்றார்` | `அண்ணன் இருக்கின்றார்` | **Anna Is Here** | 227–229 | 210–212 | `items/22-anna-is-here-en.md` | **batch-reviewed — PASS** |\n| 23 | `அண்ணன் ஒரு கவியரங்கம்` | `அண்ணன் ஒரு கவியரங்கம்` | **Anna, a Poetry Assembly** | 230–236, 238 | 213–219, 221 | `items/23-anna-a-poetry-assembly-en.md` | **batch-reviewed — PASS** |\n| 24 | `தமிழ் வளர வழிநடைப் பயணம்` | `தமிழ் வளர வழிநடைப் பயணம்` | **A Walking Journey for Tamil to Flourish** | 237, 239–244 | 220, 222–227 | `items/24-a-walking-journey-for-tamil-to-flourish-en.md` | **batch-reviewed — PASS** |\n| 25 | `வையம் தழைக்க` | `வையம் தழைக்க` | **For the World to Flourish** | 245–253 | 228–236 | `items/25-for-the-world-to-flourish-en.md` | **batch-reviewed — PASS** |\n'''
s = must_replace(s, anchor, rows, 1, 'source map item20')
s = must_replace(s, '- reviewed English batches: **6**;\n- reviewed English items: **20/77**;\n- reviewed item-assigned scans: **196/439**;', '- reviewed English batches: **7**;\n- reviewed English items: **25/77**;\n- reviewed item-assigned scans: **232/439**;', 1, 'source map progress')
old = '''## Exact next mapping activity\n\nAdd reviewed mappings for **items 21–25** after Phase-4 Batch 07 passes. Preserve the item-23/item-24 interposition exactly: item 23 = **230–236, 238**; item 24 = **237, 239–244**.\n'''
new = '''### Items 21–25 provenance notes\n\n- item 21 owns scans **218–226** (**9/9** represented);\n- item 22 owns scans **227–229** (**3/3** represented);\n- item 23 owns scans **230–236, 238** (**8/8** represented);\n- item 24 owns scans **237, 239–244** (**7/7** represented);\n- item 25 owns scans **245–253** (**9/9** represented);\n- all five canonical titles exactly match their contents witnesses;\n- the physical source order **230–236 → 237 → 238 → 239–244** is preserved without renumbering or reordering;\n- there are no pure anthology structural scans inside the Batch-07 item set;\n- no Tamil page or canonical item was changed by Batch 07.\n\n## Exact next mapping activity\n\nAdd reviewed mappings for **items 26–30** after Phase-4 Batch 08 passes. Batch-08 source interval: **254–292 = 39/39 item-owned scans**.\n'''
s = must_replace(s, old, new, 1, 'source map next')
write(p, s)

# 6. Handover.
p = Path('HANDOVER.md'); s = read(p)
s = must_replace(s, '## Durable state after Phase 4 Batch 06', '## Durable state after Phase 4 Batch 07', 1)
s = must_replace(s, 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item-assigned scans; Batch 07 NEXT**.', 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item-assigned scans; Batch 08 NEXT**.', 1)
anchor = 'Batch review: `translations/en/batches/batch-06.md`.\n\n## Supplied-transcription rule'
block = '''Batch review: `translations/en/batches/batch-06.md`.\n\n## Phase 4 durable result — Batch 07\n\n- standing user cadence: **five poems per iteration**;\n- reviewed batches: **7**;\n- reviewed English items: **25/77**;\n- reviewed item-assigned source scans: **232/439**;\n- Batch 07 items: **21–25**;\n- Batch 07 item-owned scans: **36/36**;\n- item 21 `வெள்ளி விழா` → **Silver Jubilee**;\n- item 22 `அண்ணன் இருக்கின்றார்` → **Anna Is Here**;\n- item 23 `அண்ணன் ஒரு கவியரங்கம்` → **Anna, a Poetry Assembly**, scans **230–236, 238**;\n- item 24 `தமிழ் வளர வழிநடைப் பயணம்` → **A Walking Journey for Tamil to Flourish**, scans **237, 239–244**;\n- item 25 `வையம் தழைக்க` → **For the World to Flourish**;\n- marker certification: **36/36 PASS**;\n- title witnesses: **5 exact / 0 variants / 0 unresolved**;\n- source interposition **230–236 → 237 → 238 → 239–244**: **preserved / PASS**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes during Batch 07: **0**;\n- Tamil `sections/` changes during Batch 07: **0**.\n\nBatch review: `translations/en/batches/batch-07.md`.\n\n## Supplied-transcription rule'''
s = must_replace(s, anchor, block, 1, 'handover batch07 insertion')
s = must_replace(s, 'the latest reviewed translation batch record (`translations/en/batches/batch-06.md`).', 'the latest reviewed translation batch record (`translations/en/batches/batch-07.md`).', 1, 'handover latest batch')
old = '''Execute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**.\n\nRead final-cleared `sections/21.md` through `sections/25.md` completely and translate all five complete items. Preserve physical source order and the non-contiguous ownership exactly: item 23 = **230–236, 238**; item 24 = **237, 239–244**. Review together in `translations/en/batches/batch-07.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged.'''
new = '''Execute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**.\n\nRead final-cleared `sections/26.md` through `sections/30.md` completely and translate all five complete items across scans **254–292 = 39/39**. Review together in `translations/en/batches/batch-08.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged.'''
s = must_replace(s, old, new, 1, 'handover next')
write(p, s)

# 7. Next-chat prompt.
p = Path('NEXT_CHAT_PROMPT.md'); s = read(p)
s = must_replace(s, 'Phase 4 English translation/release **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.', 'Phase 4 English translation/release **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.', 1)
if '## Phase 4 Batch 07 durable result' not in s:
    marker = '## EXACT NEXT ACTIVITY\n'
    insert = '''## Phase 4 Batch 07 durable result\n\n- standing cadence: **five poems per iteration**;\n- Batches 01–07 **reviewed PASS**;\n- reviewed items **25/77**;\n- reviewed item scans **232/439**;\n- Batch 07 items 21–25, **36/36 item-owned scans**;\n- item 23 = **230–236, 238**; item 24 = **237, 239–244**;\n- physical interposition preserved **230–236 → 237 → 238 → 239–244**;\n- title witnesses **5 exact / 0 variants / 0 unresolved**;\n- unresolved translation issues **0**;\n- Tamil page/canonical changes **0**.\n\n'''
    s = must_replace(s, marker, insert + marker, 1, 'next chat batch07 insertion')
old = '''Execute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Process all five complete poems in this iteration. Preserve item 23 scans **230–236, 238** and item 24 scans **237, 239–244** exactly in the source's physical order **230–236 → 237 → 238 → 239–244**. Review together, update Phase-4 source mapping/status, and do not alter Tamil `pages/` or `sections/`.'''
new = '''Execute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**. Process all five complete poems in this iteration, review together, update Phase-4 source mapping/status, and do not alter Tamil `pages/` or `sections/`.'''
s = must_replace(s, old, new, 1, 'next chat exact next')
write(p, s)

# 8. Root README.
p = Path('README.md'); s = read(p)
s = must_replace(s, 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.', 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.', 1)
s = must_replace(s, 'Batches 01–06 now cover items **1–20**. The reviewed English layer covers **20/77 items** and **196/439 item-assigned source scans**', 'Batches 01–07 now cover items **1–25**. The reviewed English layer covers **25/77 items** and **232/439 item-assigned source scans**', 1, 'root phase4 progress')
s = must_replace(s, '**Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Preserve the intentional item-23/item-24 physical interposition and leave Tamil archival files unchanged.', '**Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**. Translate/review all five complete poems and leave Tamil archival files unchanged.', 1, 'root next')
write(p, s)

# 9. Phase plan.
p = Path('TRANSCRIPTION_PHASE_PLAN.md'); s = read(p)
s = must_replace(s, '**IN PROGRESS — Batches 01–06 reviewed PASS.**', '**IN PROGRESS — Batches 01–07 reviewed PASS.**', 1)
s = must_replace(s, '- reviewed batches: **6**;', '- reviewed batches: **7**;', 1)
s = must_replace(s, '- reviewed English items: **20/77**;', '- reviewed English items: **25/77**;', 1)
s = must_replace(s, '- reviewed item-assigned source scans: **196/439**;', '- reviewed item-assigned source scans: **232/439**;', 1)
s = must_replace(s, '- Batch 07: items 21–25 **NEXT**.', '- Batch 07: items 21–25, **36/36 item-owned scans**, **reviewed PASS**;\n- Batch 08: items 26–30, scans **254–292 = 39/39**, **NEXT**.', 1, 'phase plan batch line')
old = '''Execute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Preserve item 23 = **230–236, 238** and item 24 = **237, 239–244** exactly; do not reorder the physical interposition. Review all five complete translations before marking the batch PASS and do not alter Tamil final-cleared files.'''
new = '''Execute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**. Review all five complete translations before marking the batch PASS and do not alter Tamil final-cleared files.'''
s = must_replace(s, old, new, 1, 'phase plan next')
write(p, s)

# 10. Active README — also repair its pre-existing stale internal Phase4 heading.
p = A / 'README.md'; s = read(p)
s = must_replace(s, 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.', 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.', 1)
s = must_replace(s, '**IN PROGRESS — Batches 01–05 reviewed PASS.**', '**IN PROGRESS — Batches 01–07 reviewed PASS.**', 1, 'active README stale Phase4 heading')
s = must_replace(s, '- reviewed batches: **6**;', '- reviewed batches: **7**;', 1)
s = must_replace(s, '- reviewed items: **20/77**;', '- reviewed items: **25/77**;', 1)
s = must_replace(s, '- reviewed item-assigned scans: **196/439**;', '- reviewed item-assigned scans: **232/439**;', 1)
s = must_replace(s, '**Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Preserve the 230–244 physical interposition exactly and review all five complete final-cleared items before advancing.', '**Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**. Review all five complete final-cleared items before advancing.', 1, 'active README next')
write(p, s)

# 11. Source intake.
p = A / 'SOURCE_INTAKE.md'; s = read(p)
s = must_replace(s, 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.', 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.', 1)
s = must_replace(s, 'Batches 01–06 are reviewed PASS; Batch 07 items 21–25 are next.', 'Batches 01–07 are reviewed PASS; Batch 08 items 26–30 are next.', 1, 'intake next phase')
s = must_replace(s, '- Batches 01–06: **reviewed PASS**;\n- reviewed items: **20/77**;\n- reviewed item scans: **196/439**;', '- Batches 01–07: **reviewed PASS**;\n- reviewed items: **25/77**;\n- reviewed item scans: **232/439**;', 1, 'intake translation state')
s = must_replace(s, '- exact next: **Batch 07 items 21–25**, preserving item 23 = **230–236, 238** and item 24 = **237, 239–244**.', '- Batch 07 interposition certification: **PASS**;\n- exact next: **Batch 08 items 26–30**, scans **254–292 = 39/39**.', 1, 'intake next')
write(p, s)

# 12. Source metadata.
p = A / 'metadata/source.md'; s = read(p)
s = must_replace(s, 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.', 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.', 1)
s = must_replace(s, '- reviewed batches: **6**;\n- reviewed English items: **20/77**;\n- reviewed item scans: **196/439**;', '- reviewed batches: **7**;\n- reviewed English items: **25/77**;\n- reviewed item scans: **232/439**;', 1, 'metadata translation counts')
s = must_replace(s, '- next translation batch: **items 21–25**, with the 230–244 interposition preserved.', '- Batch 07 review: `../translations/en/batches/batch-07.md`;\n- Batch 07 marker certification: **36/36 PASS**;\n- item-23/item-24 physical interposition: **preserved / PASS**;\n- next translation batch: **items 26–30**, scans **254–292 = 39/39**.', 1, 'metadata next')
write(p, s)

# 13. Page map.
p = A / 'indexes/page-map.md'; s = read(p)
s = must_replace(s, 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**;', 'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**;', 1)
s = must_replace(s, 'Phase 4 Batches 01–06 reviewed items **1–20** across **196/439** item-assigned scans. Batch 06 covers item scans **175–217 = 43/43**. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 07 items **21–25**; preserve item 23 = **230–236, 238** and item 24 = **237, 239–244**.', 'Phase 4 Batches 01–07 reviewed items **1–25** across **232/439** item-assigned scans. Batch 07 certifies **36/36** item-owned scan markers and preserves the intentional physical sequence **230–236 → 237 → 238 → 239–244**. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 08 items **26–30**, scans **254–292 = 39/39**.', 1, 'page map phase4 note')
write(p, s)

# 14. Audit: append Batch07 without rewriting historical next-activity records.
p = A / 'audit.md'; s = read(p)
if '## Phase 4 Batch 07 audit — REVIEWED / PASS' not in s:
    s += '''\n\n## Phase 4 Batch 07 audit — REVIEWED / PASS\n\nScope: English translation/review of final-cleared canonical items **21–25**.\n\n- items after Batch 07: **25/77**;\n- Batch-07 item-owned scans: **36/36**;\n- cumulative reviewed item-owned scans: **232/439**;\n- title witnesses: **5 exact / 0 variants / 0 unresolved**;\n- exact English scan-marker sequences: **36/36 PASS**;\n- item 23 provenance: **230–236, 238 PASS**;\n- item 24 provenance: **237, 239–244 PASS**;\n- physical interposition **230–236 → 237 → 238 → 239–244**: **PASS**;\n- omission/duplication issues: **0**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page-record changes: **0**;\n- Tamil canonical-item changes: **0**;\n- batch evidence: `translations/en/batches/batch-07.md`.\n\n### Exact next Phase-4 activity\n\n**Batch 08 — items 26–30**, scans **254–292 = 39/39**.\n'''
write(p, s)

# 15. Phase-3 final-clearance follow-up line, only when the current Phase4 state is explicitly present.
p = A / 'PHASE3_TAMIL_FINAL_CLEARANCE.md'; s = read(p)
s = replace_if(s, 'Batches 01–06 reviewed PASS', 'Batches 01–07 reviewed PASS', 1)
s = replace_if(s, '20/77', '25/77', 1)
s = replace_if(s, '196/439', '232/439', 1)
s = replace_if(s, 'Batch 07 NEXT', 'Batch 08 NEXT', 1)
write(p, s)

# 16. Remove one-shot runner files before the workflow commits the durable result.
for q in [Path('.github/scripts/finalize_kavithaigal_batch07.py'), Path('.github/workflows/finalize_kavithaigal_batch07.yml')]:
    if q.exists():
        q.unlink()

print('Batch 07 content/status edits prepared successfully.')
