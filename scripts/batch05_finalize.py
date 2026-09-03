from pathlib import Path
import re, subprocess

ROOT = Path('.')
BASE = Path('poems/kalaignarin-kavithaigal')
TRANS = BASE / 'translations/en'
ORIGINAL_BATCH04 = 'c76fe94d3e982572bbc5cbda9e3a27fdc96d9183'

items = {
  11: ('11-new-path-en.md',128,137,'புதிய பாதை','புதிய பாதை','New Path'),
  12: ('12-ten-possessions-en.md',138,143,'உடைமைகள் பத்து','உடன்பிறப்பின் பற்று','Ten Possessions'),
  13: ('13-water-family-en.md',144,154,'நீர்க் குடும்பம்','நீர்க் குடும்பம்','The Water Family'),
  14: ('14-bharathidasan-en.md',155,169,'பாரதிதாசன்','பாரதிதாசன்','Bharathidasan'),
  15: ('15-bharathiyar-en.md',170,174,'பாரதியார்','பாரதியார்','Bharathiyar'),
}

# Exact item/marker certification and status promotion.
for n,(fn,start,end,ta,contents,en) in items.items():
    p = TRANS/'items'/fn
    s = p.read_text()
    markers = [int(x) for x in re.findall(r'<!-- scan (\d+) -->', s)]
    expected = list(range(start,end+1))
    assert markers == expected, (n, markers, expected)
    assert f'item: {n}' in s
    assert f'title_ta: "{ta}"' in s
    assert f'contents_title_ta: "{contents}"' in s
    assert f'title_en: "{en}"' in s
    assert 'status: "batch-review-pending"' in s
    p.write_text(s.replace('status: "batch-review-pending"','status: "batch-reviewed"',1))

# Batch certificate.
bp = TRANS/'batches/batch-05.md'
s = bp.read_text()
assert '**REVIEW PENDING FINAL MECHANICAL CERTIFICATION.**' in s
s = s.replace('**REVIEW PENDING FINAL MECHANICAL CERTIFICATION.**','**REVIEWED — PASS.**',1)
s = s.replace('Target cumulative frontier after certification:', 'Cumulative reviewed frontier after this batch:',1)
s = s.replace('Target result: **4 exact / 1 authorised variant / 0 unresolved**.', 'Result: **4 exact / 1 authorised variant / 0 unresolved**.',1)
s = s.replace('## Mechanical certification required before PASS','## Mechanical certification — PASS',1)
s += '\n\n## Certification result\n\n- exact scan-marker sequences: **47/47 PASS**;\n- item identities: **5/5 PASS**;\n- title witnesses: **4 exact / 1 authorised variant / 0 unresolved**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes: **0**;\n- Tamil `sections/` changes: **0**.\n'
bp.write_text(s)

# Translation README.
p = TRANS/'README.md'; s=p.read_text()
s=s.replace('**PHASE 4 IN PROGRESS — Batches 01–04 reviewed PASS.**','**PHASE 4 IN PROGRESS — Batches 01–05 reviewed PASS.**')
s=s.replace('reviewed English batches: **4**','reviewed English batches: **5**')
s=s.replace('reviewed English items: **10/77**','reviewed English items: **15/77**')
s=s.replace('item-assigned source scans covered by reviewed English: **106/439**','item-assigned source scans covered by reviewed English: **153/439**')
needle='- `items/10-six-in-the-noble-scripture-en.md` — reviewed English item 10.\n'
add=needle+'- `batches/batch-05.md` — reviewed Batch-05 record;\n- `items/11-new-path-en.md` — reviewed English item 11;\n- `items/12-ten-possessions-en.md` — reviewed English item 12;\n- `items/13-water-family-en.md` — reviewed English item 13;\n- `items/14-bharathidasan-en.md` — reviewed English item 14;\n- `items/15-bharathiyar-en.md` — reviewed English item 15.\n'
assert needle in s
s=s.replace(needle,add,1)
next_idx=s.index('## Exact next activity')
s=s[:next_idx]+'''## Batch 05\n\n**Reviewed — PASS.**\n\nStanding five-poem iteration covering items **11–15** across scans **128–174**.\n\n- item 11 `புதிய பாதை` → **New Path**, scans **128–137**;\n- item 12 `உடைமைகள் பத்து` → **Ten Possessions**, scans **138–143**, with contents witness `உடன்பிறப்பின் பற்று` preserved separately;\n- item 13 `நீர்க் குடும்பம்` → **The Water Family**, scans **144–154**;\n- item 14 `பாரதிதாசன்` → **Bharathidasan**, scans **155–169**;\n- item 15 `பாரதியார்` → **Bharathiyar**, scans **170–174**;\n- reviewed scans: **47/47**;\n- title witnesses: **4 exact / 1 authorised variant**;\n- unresolved translation issues: **0**;\n- Tamil changes: **0**.\n\n## Exact next activity\n\nExecute **Phase 4 Batch 06 — items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)**, scans **175–217**, reviewing all five complete items before advancing.\n'''
p.write_text(s)

# Source map rows + provenance.
p=TRANS/'SOURCE_MAP.md'; s=p.read_text()
row10='| 10 | `அருமறையில் அறுவர்` | `அருமறையில் அறுவர்` | **Six in the Noble Scripture** | 116–127 | 99–110 | `items/10-six-in-the-noble-scripture-en.md` | **batch-reviewed — PASS** |\n'
rows=row10+'''| 11 | `புதிய பாதை` | `புதிய பாதை` | **New Path** | 128–137 | 111–120 | `items/11-new-path-en.md` | **batch-reviewed — PASS** |\n| 12 | `உடைமைகள் பத்து` | `உடன்பிறப்பின் பற்று` | **Ten Possessions** | 138–143 | 121–126 | `items/12-ten-possessions-en.md` | **batch-reviewed — PASS** |\n| 13 | `நீர்க் குடும்பம்` | `நீர்க் குடும்பம்` | **The Water Family** | 144–154 | 127–137 | `items/13-water-family-en.md` | **batch-reviewed — PASS** |\n| 14 | `பாரதிதாசன்` | `பாரதிதாசன்` | **Bharathidasan** | 155–169 | 138–152 | `items/14-bharathidasan-en.md` | **batch-reviewed — PASS** |\n| 15 | `பாரதியார்` | `பாரதியார்` | **Bharathiyar** | 170–174 | 153–157 | `items/15-bharathiyar-en.md` | **batch-reviewed — PASS** |\n'''
assert row10 in s and '| 11 |' not in s
s=s.replace(row10,rows,1)
prov='''\n### Items 11–15 provenance notes\n\n- item 11 owns scans **128–137** (**10/10** represented);\n- item 12 owns scans **138–143** (**6/6** represented) and preserves contents witness `உடன்பிறப்பின் பற்று` separately from canonical `உடைமைகள் பத்து`;\n- item 13 owns scans **144–154** (**11/11** represented);\n- item 14 owns scans **155–169** (**15/15** represented);\n- item 15 owns scans **170–174** (**5/5** represented);\n- items 11, 13, 14 and 15 have exact title witnesses; item 12 carries one authorised contents-title variant;\n- there are no pure anthology structural scans inside **128–174**;\n- no Tamil page or canonical item was changed by Batch 05.\n\n'''
s=s.replace('\n## Progress\n',prov+'## Progress\n',1)
s=s.replace('reviewed English batches: **4**','reviewed English batches: **5**')
s=s.replace('reviewed English items: **10/77**','reviewed English items: **15/77**')
s=s.replace('reviewed item-assigned scans: **106/439**','reviewed item-assigned scans: **153/439**')
idx=s.index('## Exact next mapping activity')
s=s[:idx]+'''## Exact next mapping activity\n\nAdd reviewed mappings for **items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)** after Phase-4 Batch 06 passes. Batch-06 source interval: **175–217**.\n'''
p.write_text(s)

# Translation plan: standing five-poem cadence.
p=TRANS/'TRANSLATION_PLAN.md'; s=p.read_text()
s=s.replace('**PHASE 4 IN PROGRESS — Batches 01–04 reviewed PASS.**','**PHASE 4 IN PROGRESS — Batches 01–05 reviewed PASS.**')
s=s.replace('- batches: **4**;','- batches: **5**;')
s=s.replace('- items: **10/77**;','- items: **15/77**;')
s=s.replace('- item-assigned source scans: **106/439**;','- item-assigned source scans: **153/439**;')
old='''Batch size is adaptive to source length and complexity:\n\n- long/complex items may form a one-item batch;\n- routine work may combine two or three complete adjacent items;\n- source-order interposition remains authoritative and must be represented rather than reordered.\n'''
new='''Standing user cadence from Batch 05 onward: **process five complete adjacent poems/items per iteration**. Complete-item boundaries remain mandatory, source order remains authoritative, and the final remainder batch may contain fewer than five items only when fewer than five remain. A poem is never split merely to satisfy a scan target.\n'''
assert old in s
s=s.replace(old,new,1)
s=s.replace('| 05 | 11–13 | 128–154 | **NEXT** |\n| later | 14–77 | adaptive complete-item batches | pending |','| 05 | 11–15 | 128–174 | **reviewed — PASS** |\n| 06 | 16–20 | 175–217 | **NEXT** |\n| later | 21–77 | five complete items per iteration (final remainder excepted) | pending |')
idx=s.index('## Exact next activity')
s=s[:idx]+'''## Batch 05 decision record\n\nAt the user's explicit direction, the standing Phase-4 cadence is now **five poems per iteration**. Batch 05 therefore expanded from the earlier plan of items 11–13 to **items 11–15**, covering scans **128–174**.\n\nThe reviewed translation preserves:\n\n- item 11 `புதிய பாதை` as **New Path**, including river-name/agricultural wordplay, scientific-farming rhetoric, crop-variety hand-offs and policy conclusion;\n- item 12 `உடைமைகள் பத்து` as **Ten Possessions**, while keeping contents witness `உடன்பிறப்பின் பற்று` separate, with Tirukkural virtues, fire-setting grief, language-rights rhetoric and `வள் / வாள் / வாள்வாள்` wordplay documented;\n- item 13 `நீர்க் குடும்பம்` as **The Water Family**, retaining the sea → rain → river → well → pond → tears → sweat architecture and every guest-poet hand-off;\n- item 14 `பாரதிதாசன்` as **Bharathidasan**, retaining embedded Bharati/Bharathidasan quotations, social and literary polemic, dream-stage humour, family-planning passage and poet hand-offs;\n- item 15 `பாரதியார்` as **Bharathiyar**, preserved as a distinct adjacent item with its separate Bharati-festival guest-poet sequence;\n- Batch-05 marker coverage **47/47**, title decisions **4 exact + 1 authorised variant**, unresolved translation issues **0**, Tamil `pages/`/`sections/` changes **0**.\n\n## Exact next activity\n\nExecute **Phase 4 Batch 06 — items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)** from the Tamil final-cleared canonical layer. Translate all five complete items across scans **175–217**, review them together, update the English source map, and leave Tamil final-cleared files unchanged.\n'''
p.write_text(s)

# Generic durable status documents.
status_paths=[
 Path('HANDOVER.md'), Path('NEXT_CHAT_PROMPT.md'), Path('README.md'), Path('TRANSCRIPTION_PHASE_PLAN.md'),
 BASE/'README.md', BASE/'SOURCE_INTAKE.md', BASE/'metadata/source.md', BASE/'audit.md', BASE/'indexes/page-map.md', BASE/'PHASE3_TAMIL_FINAL_CLEARANCE.md'
]
repls={
 'Batches 01–04 reviewed PASS; 10/77 items; 106/439 item-assigned scans; Batch 05 NEXT':'Batches 01–05 reviewed PASS; 15/77 items; 153/439 item-assigned scans; Batch 06 NEXT',
 'Batches 01–04 reviewed PASS; 10/77 items; 106/439 item scans; Batch 05 NEXT':'Batches 01–05 reviewed PASS; 15/77 items; 153/439 item scans; Batch 06 NEXT',
 'Batches 01–04 reviewed PASS; 10/77 items; 106/439 item scans':'Batches 01–05 reviewed PASS; 15/77 items; 153/439 item scans',
 'Batches 01–04 reviewed PASS; 10/77 items; 106/439 item-assigned scans':'Batches 01–05 reviewed PASS; 15/77 items; 153/439 item-assigned scans',
 'Batches 01–04 reviewed PASS':'Batches 01–05 reviewed PASS',
 'reviewed batches: **4**':'reviewed batches: **5**',
 'reviewed English items: **10/77**':'reviewed English items: **15/77**',
 'reviewed item-assigned source scans: **106/439**':'reviewed item-assigned source scans: **153/439**',
 'reviewed item-assigned scans: **106/439**':'reviewed item-assigned scans: **153/439**',
 'reviewed item scans: **106/439**':'reviewed item scans: **153/439**',
 'reviewed item scans **106/439**':'reviewed item scans **153/439**',
}
for p in status_paths:
    s=p.read_text()
    for a,b in repls.items(): s=s.replace(a,b)
    p.write_text(s)

# Handover: durable Batch 05 block and exact next activity.
p=Path('HANDOVER.md'); s=p.read_text()
if '## Phase 4 durable result — Batch 05' not in s:
    marker='## Supplied-transcription rule'
    block='''## Phase 4 durable result — Batch 05\n\n- standing user cadence: **five poems per iteration**;\n- reviewed batches: **5**;\n- reviewed English items: **15/77**;\n- reviewed item-assigned source scans: **153/439**;\n- Batch 05 items: **11–15**;\n- Batch 05 source scans: **128–174 = 47/47**;\n- item 11 `புதிய பாதை` → **New Path**;\n- item 12 `உடைமைகள் பத்து` → **Ten Possessions**, contents witness `உடன்பிறப்பின் பற்று` preserved separately;\n- item 13 `நீர்க் குடும்பம்` → **The Water Family**;\n- item 14 `பாரதிதாசன்` → **Bharathidasan**;\n- item 15 `பாரதியார்` → **Bharathiyar**;\n- marker certification: **47/47 PASS**;\n- title witnesses: **4 exact / 1 authorised variant / 0 unresolved**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes during Batch 05: **0**;\n- Tamil `sections/` changes during Batch 05: **0**.\n\nBatch review: `translations/en/batches/batch-05.md`.\n\n'''
    assert marker in s
    s=s.replace(marker,block+marker,1)
idx=s.index('## EXACT NEXT ACTIVITY')
s=s[:idx]+'''## EXACT NEXT ACTIVITY\n\nExecute **Phase 4 Batch 06 — items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)**.\n\nRead final-cleared `sections/16.md` through `sections/20.md` completely, translate all five complete items across scans **175–217**, review them together in `translations/en/batches/batch-06.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged. Continue thereafter in five-poem iterations.\n'''
p.write_text(s)

# Next-chat exact activity/status tail.
p=Path('NEXT_CHAT_PROMPT.md'); s=p.read_text()
if 'Phase 4 Batch 05 durable result' not in s:
    insert='''\n## Phase 4 Batch 05 durable result\n\n- standing cadence: **five poems per iteration**;\n- Batches 01–05 **reviewed PASS**;\n- reviewed items **15/77**;\n- reviewed item scans **153/439**;\n- Batch 05 items 11–15, scans **128–174 = 47/47**;\n- title witnesses **4 exact / 1 authorised variant / 0 unresolved**;\n- unresolved translation issues **0**;\n- Tamil page/canonical changes **0**.\n'''
    idx=s.index('## EXACT NEXT ACTIVITY')
    s=s[:idx]+insert+'\n'+s[idx:]
idx=s.index('## EXACT NEXT ACTIVITY')
s=s[:idx]+'''## EXACT NEXT ACTIVITY\n\nExecute **Phase 4 Batch 06 — items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)**, scans **175–217**. Process all five complete poems in this iteration, review together, update Phase-4 source mapping/status, and do not alter Tamil `pages/` or `sections/`. Continue future iterations in groups of five poems.\n'''
p.write_text(s)

# Add concise Batch 05 audit note if not already present.
p=BASE/'audit.md'; s=p.read_text()
if 'Phase 4 Batch 05 audit' not in s:
    s += '''\n\n## Phase 4 Batch 05 audit — REVIEWED / PASS\n\nItems **11–15**, scans **128–174**, passed English translation review: **47/47** markers, **4 exact + 1 authorised title variant**, **0 unresolved translation issues**, **0 Tamil page changes**, **0 Tamil canonical changes**. Standing continuation cadence: **five poems per iteration**; Batch 06 = items 16–20.\n'''
p.write_text(s)

# Scope guard from pre-Batch-05 checkpoint.
changed=subprocess.check_output(['git','diff','--name-only',ORIGINAL_BATCH04]).decode().splitlines()
for name in changed:
    if name.startswith('poems/kalaignarin-kavithaigal/pages/') or name.startswith('poems/kalaignarin-kavithaigal/sections/'):
        raise SystemExit(f'Forbidden Tamil-layer change: {name}')

# Final required text checks.
for n,(fn,start,end,ta,contents,en) in items.items():
    s=(TRANS/'items'/fn).read_text()
    assert 'status: "batch-reviewed"' in s
assert '**REVIEWED — PASS.**' in bp.read_text()
assert '15/77' in (TRANS/'README.md').read_text()
assert '153/439' in (TRANS/'SOURCE_MAP.md').read_text()
assert 'items 16–20' in Path('HANDOVER.md').read_text()

# Self-remove one-shot runner files before commit.
for q in [Path('.github/workflows/batch05-finalize.yml'), Path('scripts/batch05_finalize.py')]:
    if q.exists(): q.unlink()
