#!/usr/bin/env python3
from pathlib import Path
import re

A = Path('poems/kalaignarin-kavithaigal')
T = A / 'translations/en'

items = {
    26: ('26-father-periyar-en.md', list(range(254, 261))),
    27: ('27-akam-creations-en.md', list(range(261, 267))),
    28: ('28-pongal-festival-en.md', list(range(267, 273))),
    29: ('29-a-silappathikaram-feast-en.md', list(range(273, 286))),
    30: ('30-on-annas-path-en.md', list(range(286, 293))),
}

def read(p):
    return p.read_text(encoding='utf-8')

def write(p, s):
    p.write_text(s, encoding='utf-8')

def must_replace(s, old, new, count=1, label=''):
    if old not in s:
        raise SystemExit(f'missing expected text: {label or old[:100]!r}')
    return s.replace(old, new, count)

# 1. Mechanical certification and promotion of the five fixed draft files.
for num, (name, expected) in items.items():
    p = T / 'items' / name
    s = read(p)
    markers = [int(x) for x in re.findall(r'<!-- scan (\d+) -->', s)]
    if markers != expected:
        raise SystemExit(f'item {num} scan-marker mismatch: {markers} != {expected}')
    if f'item: {num}\n' not in s:
        raise SystemExit(f'item {num} identity missing')
    if 'title_witness_status: "exact"' not in s:
        raise SystemExit(f'item {num} title witness is not exact')
    s = must_replace(s, 'status: "batch-review-pending"', 'status: "batch-reviewed"', 1, f'item {num} status')
    write(p, s)

# 2. Batch-08 review record.
p = T / 'batches/batch-08.md'
s = read(p)
s = must_replace(s,
    '**REVIEWED — PASS, pending final mechanical/status certification.**',
    '**REVIEWED — PASS.**', 1, 'batch08 status')
if '## Certification result' not in s:
    s += '''\n\n## Certification result\n\n- exact scan-marker sequences: **39/39 PASS**;\n- item identities: **5/5 PASS**;\n- title witnesses: **5 exact / 0 variants / 0 unresolved**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes: **0**;\n- Tamil `sections/` changes: **0**.\n'''
write(p, s)

# 3. Translation README.
p = T / 'README.md'; s = read(p)
s = must_replace(s, '**PHASE 4 IN PROGRESS — Batches 01–07 reviewed PASS.**', '**PHASE 4 IN PROGRESS — Batches 01–08 reviewed PASS.**', 1)
s = must_replace(s, '- reviewed English batches: **7**;', '- reviewed English batches: **8**;', 1)
s = must_replace(s, '- reviewed English items: **25/77**;', '- reviewed English items: **30/77**;', 1)
s = must_replace(s, '- item-assigned source scans covered by reviewed English: **232/439**;', '- item-assigned source scans covered by reviewed English: **271/439**;', 1)
anchor = '- `items/25-for-the-world-to-flourish-en.md` — reviewed English item 25.\n'
add = '''- `items/25-for-the-world-to-flourish-en.md` — reviewed English item 25.\n- `batches/batch-08.md` — reviewed Batch-08 record;\n- `items/26-father-periyar-en.md` — reviewed English item 26;\n- `items/27-akam-creations-en.md` — reviewed English item 27;\n- `items/28-pongal-festival-en.md` — reviewed English item 28;\n- `items/29-a-silappathikaram-feast-en.md` — reviewed English item 29;\n- `items/30-on-annas-path-en.md` — reviewed English item 30.\n'''
s = must_replace(s, anchor, add, 1, 'translation README inventory')
old = '''## Exact next activity\n\nExecute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**.\n'''
new = '''## Batch 08\n\n**Reviewed — PASS.**\n\nStanding five-poem iteration covering items **26–30** across scans **254–292 = 39/39**.\n\n- item 26 `தந்தை பெரியார்` → **Father Periyar**, scans **254–260**;\n- item 27 `அகத்துறைப் படைப்புகள்` → **Akam Creations**, scans **261–266**;\n- item 28 `பொங்கல் விழா` → **Pongal Festival**, scans **267–272**;\n- item 29 `சிலப்பதிகார விருந்து` → **A Silappathikaram Feast**, scans **273–285**;\n- item 30 `அண்ணா வழியில்` → **On Anna's Path**, scans **286–292**;\n- reviewed scans: **39/39**;\n- title witnesses: **5 exact / 0 variants**;\n- unresolved translation issues: **0**;\n- Tamil changes: **0**.\n\n## Exact next activity\n\nExecute **Phase 4 Batch 09 — items 31–35 (`நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்!`, `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை`, `மாறி வரும் ஊரினிலே`, `சமுதாயப் பார்வைகள்...!`, `கலைவாணர் அரங்கக் கவியரங்கம்`)**, scans **293–332 = 40/40**. Preserve the three authorised title-witness variants for items 31–33 separately; items 34–35 are exact.\n'''
s = must_replace(s, old, new, 1, 'translation README next')
write(p, s)

# 4. Translation plan.
p = T / 'TRANSLATION_PLAN.md'; s = read(p)
s = must_replace(s, '**PHASE 4 IN PROGRESS — Batches 01–07 reviewed PASS.**', '**PHASE 4 IN PROGRESS — Batches 01–08 reviewed PASS.**', 1)
s = must_replace(s, '- batches: **7**;', '- batches: **8**;', 1)
s = must_replace(s, '- items: **25/77**;', '- items: **30/77**;', 1)
s = must_replace(s, '- item-assigned source scans: **232/439**;', '- item-assigned source scans: **271/439**;', 1)
s = must_replace(s,
    '| 08 | 26–30 | 254–292 | **NEXT** |\n| later | 31–77 | five complete items per iteration (final remainder excepted) | pending |',
    '| 08 | 26–30 | 254–292 | **reviewed — PASS** |\n| 09 | 31–35 | 293–332 | **NEXT** |\n| later | 36–77 | five complete items per iteration (final remainder excepted) | pending |',
    1, 'translation plan table')
old = '''## Exact next activity\n\nExecute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**.\n'''
new = '''## Batch 08 decision record\n\nBatch 08 reviewed complete items **26–30** across scans **254–292 = 39/39**. All five title witnesses are exact. The reviewed translations preserve Periyar memorial/self-respect and personal-apprenticeship rhetoric; the classical `அகம் / புறம்` and `படைப்பு / பதைப்பு` architecture; the Pongal dream built from classical anthology titles; the Poompuhar / *Silappathikaram* eight-*meyppādu* feast; and Anna's language-reform, rationalist, movement-memory and lamp imagery. Tamil `pages/`/`sections/` changes remain **0**.\n\n## Exact next activity\n\nExecute **Phase 4 Batch 09 — items 31–35**, scans **293–332 = 40/40**. Items 31–33 carry authorised contents/canonical title variants and must preserve both witnesses separately; items 34–35 are exact.\n'''
s = must_replace(s, old, new, 1, 'translation plan next')
write(p, s)

# 5. Translation source map.
p = T / 'SOURCE_MAP.md'; s = read(p)
anchor = '| 25 | `வையம் தழைக்க` | `வையம் தழைக்க` | **For the World to Flourish** | 245–253 | 228–236 | `items/25-for-the-world-to-flourish-en.md` | **batch-reviewed — PASS** |\n'
rows = '''| 25 | `வையம் தழைக்க` | `வையம் தழைக்க` | **For the World to Flourish** | 245–253 | 228–236 | `items/25-for-the-world-to-flourish-en.md` | **batch-reviewed — PASS** |\n| 26 | `தந்தை பெரியார்` | `தந்தை பெரியார்` | **Father Periyar** | 254–260 | 237–243 | `items/26-father-periyar-en.md` | **batch-reviewed — PASS** |\n| 27 | `அகத்துறைப் படைப்புகள்` | `அகத்துறைப் படைப்புகள்` | **Akam Creations** | 261–266 | 244–249 | `items/27-akam-creations-en.md` | **batch-reviewed — PASS** |\n| 28 | `பொங்கல் விழா` | `பொங்கல் விழா` | **Pongal Festival** | 267–272 | 250–255 | `items/28-pongal-festival-en.md` | **batch-reviewed — PASS** |\n| 29 | `சிலப்பதிகார விருந்து` | `சிலப்பதிகார விருந்து` | **A Silappathikaram Feast** | 273–285 | 256–268 | `items/29-a-silappathikaram-feast-en.md` | **batch-reviewed — PASS** |\n| 30 | `அண்ணா வழியில்` | `அண்ணா வழியில்` | **On Anna's Path** | 286–292 | 269–275 | `items/30-on-annas-path-en.md` | **batch-reviewed — PASS** |\n'''
s = must_replace(s, anchor, rows, 1, 'source-map item25 row')
s = must_replace(s, '- reviewed English batches: **7**;', '- reviewed English batches: **8**;', 1)
s = must_replace(s, '- reviewed English items: **25/77**;', '- reviewed English items: **30/77**;', 1)
s = must_replace(s, '- reviewed item-assigned scans: **232/439**;', '- reviewed item-assigned scans: **271/439**;', 1)
old = '''## Exact next mapping activity\n\nAdd reviewed mappings for **items 26–30** after Phase-4 Batch 08 passes. Batch-08 source interval: **254–292 = 39/39 item-owned scans**.\n'''
new = '''### Items 26–30 provenance notes\n\n- item 26 owns scans **254–260** (**7/7** represented);\n- item 27 owns scans **261–266** (**6/6** represented);\n- item 28 owns scans **267–272** (**6/6** represented);\n- item 29 owns scans **273–285** (**13/13** represented);\n- item 30 owns scans **286–292** (**7/7** represented);\n- all five canonical titles exactly match their contents witnesses;\n- there are no pure anthology structural scans inside **254–292**;\n- no Tamil page or canonical item was changed by Batch 08.\n\n## Exact next mapping activity\n\nAdd reviewed mappings for **items 31–35** after Phase-4 Batch 09 passes. The source interval is **293–332 = 40/40**; preserve item-31, item-32 and item-33 contents-title variants separately from their canonical titles.\n'''
s = must_replace(s, old, new, 1, 'source-map next')
write(p, s)

# 6. Handover — top status, durable Batch08 block, startup pointer and next.
p = Path('HANDOVER.md'); s = read(p)
s = must_replace(s, '## Durable state after Phase 4 Batch 07', '## Durable state after Phase 4 Batch 08', 1)
s = must_replace(s,
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item-assigned scans; Batch 08 NEXT**.',
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–08 reviewed PASS; 30/77 items; 271/439 item-assigned scans; Batch 09 NEXT**.', 1)
anchor = 'Batch review: `translations/en/batches/batch-07.md`.\n\n## Supplied-transcription rule'
block = '''Batch review: `translations/en/batches/batch-07.md`.\n\n## Phase 4 durable result — Batch 08\n\n- standing user cadence: **five poems per iteration**;\n- reviewed batches: **8**;\n- reviewed English items: **30/77**;\n- reviewed item-assigned source scans: **271/439**;\n- Batch 08 items: **26–30**;\n- Batch 08 source scans: **254–292 = 39/39**;\n- item 26 `தந்தை பெரியார்` → **Father Periyar**;\n- item 27 `அகத்துறைப் படைப்புகள்` → **Akam Creations**;\n- item 28 `பொங்கல் விழா` → **Pongal Festival**;\n- item 29 `சிலப்பதிகார விருந்து` → **A Silappathikaram Feast**;\n- item 30 `அண்ணா வழியில்` → **On Anna's Path**;\n- marker certification: **39/39 PASS**;\n- title witnesses: **5 exact / 0 variants / 0 unresolved**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes during Batch 08: **0**;\n- Tamil `sections/` changes during Batch 08: **0**.\n\nBatch review: `translations/en/batches/batch-08.md`.\n\n## Supplied-transcription rule'''
s = must_replace(s, anchor, block, 1, 'handover Batch08 insertion')
s = must_replace(s,
    'the latest reviewed translation batch record (`translations/en/batches/batch-07.md`).',
    'the latest reviewed translation batch record (`translations/en/batches/batch-08.md`).', 1)
old = '''Execute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**.\n\nRead final-cleared `sections/26.md` through `sections/30.md` completely and translate all five complete items across scans **254–292 = 39/39**. Review together in `translations/en/batches/batch-08.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged.'''
new = '''Execute **Phase 4 Batch 09 — items 31–35 (`நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்!`, `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை`, `மாறி வரும் ஊரினிலே`, `சமுதாயப் பார்வைகள்...!`, `கலைவாணர் அரங்கக் கவியரங்கம்`)**.\n\nRead final-cleared `sections/31.md` through `sections/35.md` completely and translate all five complete items across scans **293–332 = 40/40**. Preserve the authorised title-witness variants for items 31–33 separately from canonical titles. Review together in `translations/en/batches/batch-09.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged.'''
s = must_replace(s, old, new, 1, 'handover next')
write(p, s)

# 7. Next-chat prompt.
p = Path('NEXT_CHAT_PROMPT.md'); s = read(p)
s = must_replace(s,
    'Phase 4 English translation/release **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.',
    'Phase 4 English translation/release **IN PROGRESS — Batches 01–08 reviewed PASS; 30/77 items; 271/439 item scans; Batch 09 NEXT**.', 1)
if '## Phase 4 Batch 08 durable result' not in s:
    marker = '## EXACT NEXT ACTIVITY\n'
    insert = '''## Phase 4 Batch 08 durable result\n\n- standing cadence: **five poems per iteration**;\n- Batches 01–08 **reviewed PASS**;\n- reviewed items **30/77**;\n- reviewed item scans **271/439**;\n- Batch 08 items 26–30, scans **254–292 = 39/39**;\n- title witnesses **5 exact / 0 variants / 0 unresolved**;\n- unresolved translation issues **0**;\n- Tamil page/canonical changes **0**.\n\n'''
    s = must_replace(s, marker, insert + marker, 1, 'next-chat Batch08 insertion')
old = '''Execute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**. Process all five complete poems in this iteration, review together, update Phase-4 source mapping/status, and do not alter Tamil `pages/` or `sections/`.'''
new = '''Execute **Phase 4 Batch 09 — items 31–35 (`நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்!`, `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை`, `மாறி வரும் ஊரினிலே`, `சமுதாயப் பார்வைகள்...!`, `கலைவாணர் அரங்கக் கவியரங்கம்`)**, scans **293–332 = 40/40**. Process all five complete poems in this iteration. Preserve the authorised contents/canonical title variants for items 31–33 separately; items 34–35 are exact. Review together, update Phase-4 source mapping/status, and do not alter Tamil `pages/` or `sections/`.'''
s = must_replace(s, old, new, 1, 'next-chat next')
write(p, s)

# 8. Root README.
p = Path('README.md'); s = read(p)
s = must_replace(s,
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.',
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–08 reviewed PASS; 30/77 items; 271/439 item scans; Batch 09 NEXT**.', 1)
s = must_replace(s,
    'Batches 01–07 now cover items **1–25**. The reviewed English layer covers **25/77 items** and **232/439 item-assigned source scans**',
    'Batches 01–08 now cover items **1–30**. The reviewed English layer covers **30/77 items** and **271/439 item-assigned source scans**', 1)
s = must_replace(s,
    '**Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**. Translate/review all five complete poems and leave Tamil archival files unchanged.',
    '**Phase 4 Batch 09 — items 31–35**, scans **293–332 = 40/40**. Preserve the three authorised title-witness variants for items 31–33 separately, translate/review all five complete poems, and leave Tamil archival files unchanged.', 1)
write(p, s)

# 9. Transcription phase plan.
p = Path('TRANSCRIPTION_PHASE_PLAN.md'); s = read(p)
s = must_replace(s, '**IN PROGRESS — Batches 01–07 reviewed PASS.**', '**IN PROGRESS — Batches 01–08 reviewed PASS.**', 1)
s = must_replace(s, '- reviewed batches: **7**;', '- reviewed batches: **8**;', 1)
s = must_replace(s, '- reviewed English items: **25/77**;', '- reviewed English items: **30/77**;', 1)
s = must_replace(s, '- reviewed item-assigned source scans: **232/439**;', '- reviewed item-assigned source scans: **271/439**;', 1)
s = must_replace(s, '- Batch 08: items 26–30, scans **254–292 = 39/39**, **NEXT**.', '- Batch 08: items 26–30, scans **254–292 = 39/39**, **reviewed PASS**;\n- Batch 09: items 31–35, scans **293–332 = 40/40**, **NEXT**.', 1)
old = '''Execute **Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**. Review all five complete translations before marking the batch PASS and do not alter Tamil final-cleared files.'''
new = '''Execute **Phase 4 Batch 09 — items 31–35**, scans **293–332 = 40/40**. Preserve the three authorised title-witness variants for items 31–33 separately; review all five complete translations before marking the batch PASS and do not alter Tamil final-cleared files.'''
s = must_replace(s, old, new, 1, 'phase-plan next')
write(p, s)

# 10. Active README.
p = A / 'README.md'; s = read(p)
s = must_replace(s,
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.',
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–08 reviewed PASS; 30/77 items; 271/439 item scans; Batch 09 NEXT**.', 1)
s = must_replace(s, '**IN PROGRESS — Batches 01–07 reviewed PASS.**', '**IN PROGRESS — Batches 01–08 reviewed PASS.**', 1)
s = must_replace(s, '- reviewed batches: **7**;', '- reviewed batches: **8**;', 1)
s = must_replace(s, '- reviewed items: **25/77**;', '- reviewed items: **30/77**;', 1)
s = must_replace(s, '- reviewed item-assigned scans: **232/439**;', '- reviewed item-assigned scans: **271/439**;', 1)
s = must_replace(s,
    '**Phase 4 Batch 08 — items 26–30 (`தந்தை பெரியார்`, `அகத்துறைப் படைப்புகள்`, `பொங்கல் விழா`, `சிலப்பதிகார விருந்து`, `அண்ணா வழியில்`)**, scans **254–292 = 39/39**. Review all five complete final-cleared items before advancing.',
    '**Phase 4 Batch 09 — items 31–35**, scans **293–332 = 40/40**. Preserve the title-witness variants for items 31–33 and review all five complete final-cleared items before advancing.', 1)
write(p, s)

# 11. Source intake.
p = A / 'SOURCE_INTAKE.md'; s = read(p)
s = must_replace(s,
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.',
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–08 reviewed PASS; 30/77 items; 271/439 item scans; Batch 09 NEXT**.', 1)
s = must_replace(s,
    '**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–07 are reviewed PASS; Batch 08 items 26–30 are next.',
    '**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–08 are reviewed PASS; Batch 09 items 31–35 are next.', 1)
s = must_replace(s, '- Batches 01–07: **reviewed PASS**;', '- Batches 01–08: **reviewed PASS**;', 1)
s = must_replace(s, '- reviewed items: **25/77**;', '- reviewed items: **30/77**;', 1)
s = must_replace(s, '- reviewed item scans: **232/439**;', '- reviewed item scans: **271/439**;', 1)
s = must_replace(s, '- exact next: **Batch 08 items 26–30**, scans **254–292 = 39/39**.', '- Batch 08 marker certification: **39/39 PASS**;\n- exact next: **Batch 09 items 31–35**, scans **293–332 = 40/40**, with items 31–33 retaining authorised title variants.', 1)
write(p, s)

# 12. Source metadata.
p = A / 'metadata/source.md'; s = read(p)
s = must_replace(s,
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**.',
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–08 reviewed PASS; 30/77 items; 271/439 item scans; Batch 09 NEXT**.', 1)
s = must_replace(s, '- reviewed batches: **7**;', '- reviewed batches: **8**;', 1)
s = must_replace(s, '- reviewed English items: **25/77**;', '- reviewed English items: **30/77**;', 1)
s = must_replace(s, '- reviewed item scans: **232/439**;', '- reviewed item scans: **271/439**;', 1)
s = must_replace(s,
    '- next translation batch: **items 26–30**, scans **254–292 = 39/39**.',
    '- Batch 08 review: `../translations/en/batches/batch-08.md`;\n- Batch 08 marker certification: **39/39 PASS**;\n- next translation batch: **items 31–35**, scans **293–332 = 40/40**, preserving authorised title variants for items 31–33.', 1)
write(p, s)

# 13. Page map.
p = A / 'indexes/page-map.md'; s = read(p)
s = must_replace(s,
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–07 reviewed PASS; 25/77 items; 232/439 item scans; Batch 08 NEXT**;',
    'Phase 4 English translation/release: **IN PROGRESS — Batches 01–08 reviewed PASS; 30/77 items; 271/439 item scans; Batch 09 NEXT**;', 1)
s = must_replace(s,
    'Phase 4 Batches 01–07 reviewed items **1–25** across **232/439** item-assigned scans. Batch 07 certifies **36/36** item-owned scan markers and preserves the intentional physical sequence **230–236 → 237 → 238 → 239–244**. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 08 items **26–30**, scans **254–292 = 39/39**.',
    'Phase 4 Batches 01–08 reviewed items **1–30** across **271/439** item-assigned scans. Batch 08 certifies **39/39** item-owned scan markers across **254–292**. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 09 items **31–35**, scans **293–332 = 40/40**.', 1)
write(p, s)

# 14. Audit — append only; leave historical next-activity blocks intact.
p = A / 'audit.md'; s = read(p)
if '## Phase 4 Batch 08 audit — REVIEWED / PASS' not in s:
    s += '''\n\n## Phase 4 Batch 08 audit — REVIEWED / PASS\n\nScope: English translation/review of final-cleared canonical items **26–30**.\n\n- items after Batch 08: **30/77**;\n- Batch-08 item-owned scans: **39/39 — scans 254–292**;\n- cumulative reviewed item-owned scans: **271/439**;\n- title witnesses: **5 exact / 0 variants / 0 unresolved**;\n- exact English scan-marker sequences: **39/39 PASS**;\n- omission/duplication issues: **0**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page-record changes: **0**;\n- Tamil canonical-item changes: **0**;\n- batch evidence: `translations/en/batches/batch-08.md`.\n\n### Exact next Phase-4 activity\n\n**Batch 09 — items 31–35**, scans **293–332 = 40/40**. Preserve the authorised title-witness variants for items 31–33 separately; items 34–35 are exact.\n'''
write(p, s)

# 15. Update only the clearly labelled subsequent-Phase-4 follow-up in the historical Tamil-clearance record.
p = A / 'PHASE3_TAMIL_FINAL_CLEARANCE.md'; s = read(p)
old = '''Phase 4 has subsequently advanced through **Batches 01–04, all reviewed PASS**. Reviewed English now covers items **1–10/77** and **106/439** item-assigned scans. Batch 04 is the user-authorized items 6–10 expansion across scans **72–127**. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Exact next translation activity: **Batch 05 items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**, scans **128–154**.'''
new = '''Phase 4 has subsequently advanced through **Batches 01–08, all reviewed PASS**. Reviewed English now covers items **1–30/77** and **271/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Exact next translation activity: **Batch 09 items 31–35**, scans **293–332 = 40/40**, preserving the authorised title-witness variants for items 31–33.'''
s = must_replace(s, old, new, 1, 'Tamil-clearance subsequent status')
write(p, s)

# Remove the one-shot runner before commit so it leaves no durable artifact.
for q in [Path('.github/scripts/finalize_kavithaigal_batch08.py'), Path('.github/workflows/finalize_kavithaigal_batch08.yml')]:
    if q.exists():
        q.unlink()

print('Batch 08 mechanical/status finalization prepared successfully.')
