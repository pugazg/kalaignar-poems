#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path('.')
A = Path('poems/kalaignarin-kavithaigal')
T = A / 'translations/en'

items = {
    16: ('16-pongal-festival-day-en.md', list(range(175,185))),
    17: ('17-on-the-path-called-life-en.md', list(range(185,197))),
    18: ('18-arithmetic-en.md', list(range(197,205))),
    19: ('19-democracy-as-nehru-saw-it-en.md', list(range(205,216))),
    20: ('20-thank-you-thank-you-en.md', list(range(216,218))),
}

def read(p): return p.read_text(encoding='utf-8')
def write(p,s): p.write_text(s, encoding='utf-8')
def must_replace(text, old, new, count=1, label=''):
    if old not in text:
        raise SystemExit(f'missing expected text {label or old[:80]!r}')
    return text.replace(old,new,count)

# 1. Mechanical certification and item-status promotion.
for num,(name,expected) in items.items():
    p=T/'items'/name
    s=read(p)
    markers=[int(x) for x in re.findall(r'<!-- scan (\d+) -->', s)]
    if markers != expected:
        raise SystemExit(f'item {num} scan markers mismatch: {markers} != {expected}')
    if f'item: {num}\n' not in s:
        raise SystemExit(f'item {num} identity missing')
    if 'title_witness_status: "exact"' not in s:
        raise SystemExit(f'item {num} title witness not exact')
    s=must_replace(s,'status: "batch-review-pending"','status: "batch-reviewed"',1,f'item {num} pending status')
    write(p,s)

# 2. Batch review record.
p=T/'batches/batch-06.md'; s=read(p)
s=must_replace(s,'**REVIEWED — PASS, pending final mechanical/status certification.**','**REVIEWED — PASS.**',1,'batch06 status')
if '## Certification result' not in s:
    s += '''\n\n## Certification result\n\n- exact scan-marker sequences: **43/43 PASS**;\n- item identities: **5/5 PASS**;\n- title witnesses: **5 exact / 0 variants / 0 unresolved**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes: **0**;\n- Tamil `sections/` changes: **0**.\n'''
write(p,s)

# 3. English README — current status, inventory, Batch 06 and next.
p=T/'README.md'; s=read(p)
s=must_replace(s,'**PHASE 4 IN PROGRESS — Batches 01–05 reviewed PASS.**','**PHASE 4 IN PROGRESS — Batches 01–06 reviewed PASS.**',1)
s=must_replace(s,'- reviewed English batches: **5**;','- reviewed English batches: **6**;',1)
s=must_replace(s,'- reviewed English items: **15/77**;','- reviewed English items: **20/77**;',1)
s=must_replace(s,'- item-assigned source scans covered by reviewed English: **153/439**;','- item-assigned source scans covered by reviewed English: **196/439**;',1)
anchor='- `items/15-bharathiyar-en.md` — reviewed English item 15.\n'
add='''- `items/15-bharathiyar-en.md` — reviewed English item 15.\n- `batches/batch-06.md` — reviewed Batch-06 record;\n- `items/16-pongal-festival-day-en.md` — reviewed English item 16;\n- `items/17-on-the-path-called-life-en.md` — reviewed English item 17;\n- `items/18-arithmetic-en.md` — reviewed English item 18;\n- `items/19-democracy-as-nehru-saw-it-en.md` — reviewed English item 19;\n- `items/20-thank-you-thank-you-en.md` — reviewed English item 20.\n'''
s=must_replace(s,anchor,add,1,'translation README item15 inventory')
old='''## Exact next activity\n\nExecute **Phase 4 Batch 06 — items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)**, scans **175–217**, reviewing all five complete items before advancing.\n'''
new='''## Batch 06\n\n**Reviewed — PASS.**\n\nStanding five-poem iteration covering items **16–20** across scans **175–217**.\n\n- item 16 `பொங்கல் திருநாள்` → **Pongal Festival Day**, scans **175–184**;\n- item 17 `வாழ்வெனும் பாதையில்` → **On the Path Called Life**, scans **185–196**;\n- item 18 `கணக்கு` → **Arithmetic**, scans **197–204**;\n- item 19 `நேரு கண்ட ஜனநாயகம்` → **Democracy as Nehru Saw It**, scans **205–215**;\n- item 20 `நன்றி, நன்றி!` → **Thank You, Thank You!**, scans **216–217**;\n- reviewed scans: **43/43**;\n- title witnesses: **5 exact / 0 variants**;\n- unresolved translation issues: **0**;\n- Tamil changes: **0**.\n\n## Exact next activity\n\nExecute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Item-owned scans total **36/36** across physical interval **218–253**. Preserve the intentional source interposition **230–236 → 237 → 238 → 239–244** exactly.\n'''
s=must_replace(s,old,new,1,'translation README next')
write(p,s)

# 4. Translation plan.
p=T/'TRANSLATION_PLAN.md'; s=read(p)
s=must_replace(s,'**PHASE 4 IN PROGRESS — Batches 01–05 reviewed PASS.**','**PHASE 4 IN PROGRESS — Batches 01–06 reviewed PASS.**',1)
s=must_replace(s,'- batches: **5**;','- batches: **6**;',1)
s=must_replace(s,'- items: **15/77**;','- items: **20/77**;',1)
s=must_replace(s,'- item-assigned source scans: **153/439**;','- item-assigned source scans: **196/439**;',1)
s=must_replace(s,'| 06 | 16–20 | 175–217 | **NEXT** |\n| later | 21–77 | five complete items per iteration (final remainder excepted) | pending |','| 06 | 16–20 | 175–217 | **reviewed — PASS** |\n| 07 | 21–25 | 218–253 | **NEXT** |\n| later | 26–77 | five complete items per iteration (final remainder excepted) | pending |',1,'plan table')
old='''## Exact next activity\n\nExecute **Phase 4 Batch 06 — items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)** from the Tamil final-cleared canonical layer. Translate all five complete items across scans **175–217**, review them together, update the English source map, and leave Tamil final-cleared files unchanged.\n'''
new='''## Batch 06 decision record\n\nBatch 06 reviewed complete items **16–20** across scans **175–217 = 43/43**. All five title witnesses are exact. The reviewed translations preserve Pongal agrarian/political wordplay; the life-road education/office/wealth/art/fame/devotion structure; arithmetic operation satire; Nehru floral elegy, secular-democratic and rights sequence; and the improvised `நன்றி` stage poem. Tamil `pages/`/`sections/` changes remain **0**.\n\n## Exact next activity\n\nExecute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Preserve item 23 scans **230–236, 238** and item 24 scans **237, 239–244** without source reordering; the physical sequence **230–236 → 237 → 238 → 239–244** is intentional.\n'''
s=must_replace(s,old,new,1,'plan next')
write(p,s)

# 5. Source map.
p=T/'SOURCE_MAP.md'; s=read(p)
anchor='| 15 | `பாரதியார்` | `பாரதியார்` | **Bharathiyar** | 170–174 | 153–157 | `items/15-bharathiyar-en.md` | **batch-reviewed — PASS** |\n'
rows='''| 15 | `பாரதியார்` | `பாரதியார்` | **Bharathiyar** | 170–174 | 153–157 | `items/15-bharathiyar-en.md` | **batch-reviewed — PASS** |\n| 16 | `பொங்கல் திருநாள்` | `பொங்கல் திருநாள்` | **Pongal Festival Day** | 175–184 | 158–167 | `items/16-pongal-festival-day-en.md` | **batch-reviewed — PASS** |\n| 17 | `வாழ்வெனும் பாதையில்` | `வாழ்வெனும் பாதையில்` | **On the Path Called Life** | 185–196 | 168–179 | `items/17-on-the-path-called-life-en.md` | **batch-reviewed — PASS** |\n| 18 | `கணக்கு` | `கணக்கு` | **Arithmetic** | 197–204 | 180–187 | `items/18-arithmetic-en.md` | **batch-reviewed — PASS** |\n| 19 | `நேரு கண்ட ஜனநாயகம்` | `நேரு கண்ட ஜனநாயகம்` | **Democracy as Nehru Saw It** | 205–215 | 188–198 | `items/19-democracy-as-nehru-saw-it-en.md` | **batch-reviewed — PASS** |\n| 20 | `நன்றி, நன்றி!` | `நன்றி, நன்றி!` | **Thank You, Thank You!** | 216–217 | 199–200 | `items/20-thank-you-thank-you-en.md` | **batch-reviewed — PASS** |\n'''
s=must_replace(s,anchor,rows,1,'source map item15')
prog='''- reviewed English batches: **5**;\n- reviewed English items: **15/77**;\n- reviewed item-assigned scans: **153/439**;'''
s=must_replace(s,prog,'''- reviewed English batches: **6**;\n- reviewed English items: **20/77**;\n- reviewed item-assigned scans: **196/439**;''',1,'source map progress')
old='''## Exact next mapping activity\n\nAdd reviewed mappings for **items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)** after Phase-4 Batch 06 passes. Batch-06 source interval: **175–217**.\n'''
new='''### Items 16–20 provenance notes\n\n- item 16 owns scans **175–184** (**10/10** represented);\n- item 17 owns scans **185–196** (**12/12** represented);\n- item 18 owns scans **197–204** (**8/8** represented);\n- item 19 owns scans **205–215** (**11/11** represented);\n- item 20 owns scans **216–217** (**2/2** represented);\n- all five canonical titles exactly match their contents witnesses;\n- there are no pure anthology structural scans inside **175–217**;\n- no Tamil page or canonical item was changed by Batch 06.\n\n## Exact next mapping activity\n\nAdd reviewed mappings for **items 21–25** after Phase-4 Batch 07 passes. Preserve the item-23/item-24 interposition exactly: item 23 = **230–236, 238**; item 24 = **237, 239–244**.\n'''
s=must_replace(s,old,new,1,'source map next')
write(p,s)

# 6. Handover: top current state, add Batch06, latest batch pointer, exact next.
p=Path('HANDOVER.md'); s=read(p)
s=must_replace(s,'## Durable state after Phase 4 Batch 05','## Durable state after Phase 4 Batch 06',1)
s=must_replace(s,'Phase 4 English translation/release: **IN PROGRESS — Batches 01–05 reviewed PASS; 15/77 items; 153/439 item-assigned scans; Batch 06 NEXT**.','Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item-assigned scans; Batch 07 NEXT**.',1)
anchor='Batch review: `translations/en/batches/batch-05.md`.\n\n## Supplied-transcription rule'
block='''Batch review: `translations/en/batches/batch-05.md`.\n\n## Phase 4 durable result — Batch 06\n\n- standing user cadence: **five poems per iteration**;\n- reviewed batches: **6**;\n- reviewed English items: **20/77**;\n- reviewed item-assigned source scans: **196/439**;\n- Batch 06 items: **16–20**;\n- Batch 06 source scans: **175–217 = 43/43**;\n- item 16 `பொங்கல் திருநாள்` → **Pongal Festival Day**;\n- item 17 `வாழ்வெனும் பாதையில்` → **On the Path Called Life**;\n- item 18 `கணக்கு` → **Arithmetic**;\n- item 19 `நேரு கண்ட ஜனநாயகம்` → **Democracy as Nehru Saw It**;\n- item 20 `நன்றி, நன்றி!` → **Thank You, Thank You!**;\n- marker certification: **43/43 PASS**;\n- title witnesses: **5 exact / 0 variants / 0 unresolved**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes during Batch 06: **0**;\n- Tamil `sections/` changes during Batch 06: **0**.\n\nBatch review: `translations/en/batches/batch-06.md`.\n\n## Supplied-transcription rule'''
s=must_replace(s,anchor,block,1,'handover batch06 insertion')
s=s.replace('the latest reviewed translation batch record (`translations/en/batches/batch-05.md`).','the latest reviewed translation batch record (`translations/en/batches/batch-06.md`).',1)
old='''Execute **Phase 4 Batch 06 — items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)**.\n\nRead final-cleared `sections/16.md` through `sections/20.md` completely, translate all five complete items across scans **175–217**, review them together in `translations/en/batches/batch-06.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged. Continue thereafter in five-poem iterations.'''
new='''Execute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**.\n\nRead final-cleared `sections/21.md` through `sections/25.md` completely and translate all five complete items. Preserve physical source order and the non-contiguous ownership exactly: item 23 = **230–236, 238**; item 24 = **237, 239–244**. Review together in `translations/en/batches/batch-07.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged.'''
s=must_replace(s,old,new,1,'handover next')
write(p,s)

# 7. Next-chat prompt: current-state and exact-next only; historical Batch05 block remains history.
p=Path('NEXT_CHAT_PROMPT.md'); s=read(p)
s=must_replace(s,'Phase 4 English translation/release **IN PROGRESS — Batches 01–05 reviewed PASS; 15/77 items; 153/439 item scans; Batch 06 NEXT**.','Phase 4 English translation/release **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.',1)
old='''Execute **Phase 4 Batch 06 — items 16–20 (`பொங்கல் திருநாள்`, `வாழ்வெனும் பாதையில்`, `கணக்கு`, `நேரு கண்ட ஜனநாயகம்`, `நன்றி, நன்றி!`)**, scans **175–217**. Process all five complete poems in this iteration, review together, update Phase-4 source mapping/status, and do not alter Tamil `pages/` or `sections/`. Continue future iterations in groups of five poems.'''
new='''Execute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Process all five complete poems in this iteration. Preserve item 23 scans **230–236, 238** and item 24 scans **237, 239–244** exactly in the source's physical order **230–236 → 237 → 238 → 239–244**. Review together, update Phase-4 source mapping/status, and do not alter Tamil `pages/` or `sections/`.'''
s=must_replace(s,old,new,1,'next chat exact next')
if '## Phase 4 Batch 06 durable result' not in s:
    marker='## EXACT NEXT ACTIVITY\n'
    insert='''## Phase 4 Batch 06 durable result\n\n- standing cadence: **five poems per iteration**;\n- Batches 01–06 **reviewed PASS**;\n- reviewed items **20/77**;\n- reviewed item scans **196/439**;\n- Batch 06 items 16–20, scans **175–217 = 43/43**;\n- title witnesses **5 exact / 0 variants / 0 unresolved**;\n- unresolved translation issues **0**;\n- Tamil page/canonical changes **0**.\n\n'''
    s=must_replace(s,marker,insert+marker,1,'next chat batch06 insertion')
write(p,s)

# 8. Root README current summary and Phase4 progress/next.
p=Path('README.md'); s=read(p)
s=must_replace(s,'Phase 4 English translation/release: **IN PROGRESS — Batches 01–05 reviewed PASS; 15/77 items; 153/439 item scans; Batch 06 NEXT**.','Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.',1)
s=s.replace('Batches 01–04 now cover items **1–10**. The reviewed English layer covers **10/77 items** and **106/439 item-assigned source scans**','Batches 01–06 now cover items **1–20**. The reviewed English layer covers **20/77 items** and **196/439 item-assigned source scans**',1)
s=s.replace('**Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**, scans **128–154**. Translate and review all three complete final-cleared items; preserve item 12\'s contents-title variant separately and leave Tamil archival files unchanged.','**Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Preserve the intentional item-23/item-24 physical interposition and leave Tamil archival files unchanged.',1)
write(p,s)

# 9. Transcription phase plan: repair stale current Phase4 section and next.
p=Path('TRANSCRIPTION_PHASE_PLAN.md'); s=read(p)
s=must_replace(s,'**IN PROGRESS — Batches 01–05 reviewed PASS.**','**IN PROGRESS — Batches 01–06 reviewed PASS.**',1)
s=must_replace(s,'- reviewed batches: **5**;','- reviewed batches: **6**;',1)
s=must_replace(s,'- reviewed English items: **15/77**;','- reviewed English items: **20/77**;',1)
s=must_replace(s,'- reviewed item-assigned source scans: **153/439**;','- reviewed item-assigned source scans: **196/439**;',1)
s=s.replace('- Batch 05 items 11–13: **NEXT**.','- Batch 05: items 11–15, scans **128–174 = 47/47**, **reviewed PASS**;\n- Batch 06: items 16–20, scans **175–217 = 43/43**, **reviewed PASS**;\n- standing cadence: **five complete poems per iteration**;\n- Batch 07: items 21–25 **NEXT**.',1)
old='''Execute **Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)** from the Tamil final-cleared canonical layer across scans **128–154**. Review all three complete translations before marking the batch PASS; preserve item 12's title witnesses separately and do not alter Tamil final-cleared files.'''
new='''Execute **Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Preserve item 23 = **230–236, 238** and item 24 = **237, 239–244** exactly; do not reorder the physical interposition. Review all five complete translations before marking the batch PASS and do not alter Tamil final-cleared files.'''
s=must_replace(s,old,new,1,'phase plan next')
write(p,s)

# 10. Active README.
p=A/'README.md'; s=read(p)
s=must_replace(s,'Phase 4 English translation/release: **IN PROGRESS — Batches 01–05 reviewed PASS; 15/77 items; 153/439 item scans; Batch 06 NEXT**.','Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.',1)
s=s.replace('- reviewed batches: **5**;\n- reviewed items: **10/77**;\n- reviewed item-assigned scans: **153/439**;','- reviewed batches: **6**;\n- reviewed items: **20/77**;\n- reviewed item-assigned scans: **196/439**;',1)
s=s.replace('**Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**. Translate all three complete final-cleared items across scans **128–154** and review the batch before advancing.','**Phase 4 Batch 07 — items 21–25 (`வெள்ளி விழா`, `அண்ணன் இருக்கின்றார்`, `அண்ணன் ஒரு கவியரங்கம்`, `தமிழ் வளர வழிநடைப் பயணம்`, `வையம் தழைக்க`)**. Preserve the 230–244 physical interposition exactly and review all five complete final-cleared items before advancing.',1)
write(p,s)

# 11. Intake, metadata, page-map — current translation state only.
p=A/'SOURCE_INTAKE.md'; s=read(p)
s=must_replace(s,'Phase 4 English translation/release: **IN PROGRESS — Batches 01–05 reviewed PASS; 15/77 items; 153/439 item scans; Batch 06 NEXT**.','Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.',1)
s=s.replace('Batches 01–03 are reviewed PASS; Batch 05 items 11–13 are next.','Batches 01–06 are reviewed PASS; Batch 07 items 21–25 are next.',1)
s=s.replace('- Batches 01–04: **reviewed PASS**;\n- reviewed items: **10/77**;\n- reviewed item scans: **153/439**;','- Batches 01–06: **reviewed PASS**;\n- reviewed items: **20/77**;\n- reviewed item scans: **196/439**;',1)
s=s.replace('- exact next: **Batch 05 items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**, scans **128–154**.','- exact next: **Batch 07 items 21–25**, preserving item 23 = **230–236, 238** and item 24 = **237, 239–244**.',1)
write(p,s)

p=A/'metadata/source.md'; s=read(p)
s=must_replace(s,'Phase 4 English translation/release: **IN PROGRESS — Batches 01–05 reviewed PASS; 15/77 items; 153/439 item scans; Batch 06 NEXT**.','Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**.',1)
s=s.replace('- reviewed batches: **5**;\n- reviewed English items: **15/77**;\n- reviewed item scans: **153/439**;','- reviewed batches: **6**;\n- reviewed English items: **20/77**;\n- reviewed item scans: **196/439**;',1)
s=s.replace('- next translation batch: **items 11–13**, scans **128–154**.','- Batch 06 review: `../translations/en/batches/batch-06.md`;\n- Batch 06 marker certification: **43/43 PASS**;\n- next translation batch: **items 21–25**, with the 230–244 interposition preserved.',1)
write(p,s)

p=A/'indexes/page-map.md'; s=read(p)
s=must_replace(s,'Phase 4 English translation/release: **IN PROGRESS — Batches 01–05 reviewed PASS; 15/77 items; 153/439 item scans; Batch 06 NEXT**;','Phase 4 English translation/release: **IN PROGRESS — Batches 01–06 reviewed PASS; 20/77 items; 196/439 item scans; Batch 07 NEXT**;',1)
s=s.replace('Phase 4 Batches 01–04 reviewed items **1–10** across **106/439** item-assigned scans. Batch 04 covers item scans **72–127 = 56/56**; structural scans **70–71** remain separate anthology provenance. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 05 items **11–13**, scans **128–154**.','Phase 4 Batches 01–06 reviewed items **1–20** across **196/439** item-assigned scans. Batch 06 covers item scans **175–217 = 43/43**. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 07 items **21–25**; preserve item 23 = **230–236, 238** and item 24 = **237, 239–244**.',1)
write(p,s)

# 12. Audit — append current Batch06 record; do not rewrite historical next-activity records.
p=A/'audit.md'; s=read(p)
if '## Phase 4 Batch 06 audit — REVIEWED / PASS' not in s:
    s += '''\n\n## Phase 4 Batch 06 audit — REVIEWED / PASS\n\nScope: English translation/review of final-cleared canonical items **16–20**.\n\n- items after Batch 06: **20/77**;\n- Batch-06 item-owned scans: **43/43 — scans 175–217**;\n- cumulative reviewed item-owned scans: **196/439**;\n- title witnesses: **5 exact / 0 variants / 0 unresolved**;\n- exact English scan-marker sequences: **43/43 PASS**;\n- omission/duplication issues: **0**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page-record changes: **0**;\n- Tamil canonical-item changes: **0**;\n- batch evidence: `translations/en/batches/batch-06.md`.\n\n### Exact next Phase-4 activity\n\n**Batch 07 — items 21–25**. Preserve the intentional physical interposition exactly: item 23 = **230–236, 238** and item 24 = **237, 239–244**.\n'''
write(p,s)

# 13. Optional Phase-3 clearance follow-up status: only if a Phase4 follow-up line exists.
p=A/'PHASE3_TAMIL_FINAL_CLEARANCE.md'
s=read(p)
if 'Batches 01–05 reviewed PASS' in s:
    s=s.replace('Batches 01–05 reviewed PASS','Batches 01–06 reviewed PASS',1)
if '15/77' in s and 'Phase 4' in s:
    # limit replacement to last Phase4 status conventions; historical clearance inventory 77/77 is untouched.
    idx=s.rfind('Phase 4')
    if idx>=0:
        tail=s[idx:].replace('15/77','20/77').replace('153/439','196/439').replace('Batch 06 NEXT','Batch 07 NEXT')
        s=s[:idx]+tail
write(p,s)

# 14. No Tamil source-layer modifications allowed.
# Remove one-shot files before commit so they leave no durable net artifact.
for q in [Path('.github/scripts/finalize_kavithaigal_batch06.py'), Path('.github/workflows/finalize_kavithaigal_batch06.yml')]:
    if q.exists(): q.unlink()

# We cannot inspect git diff until after this script exits; workflow performs the hard scope guard.
print('Batch 06 content/status edits prepared successfully.')
