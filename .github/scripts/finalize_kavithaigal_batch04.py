from pathlib import Path
import re, subprocess, sys

BASE = "487903fa6cff658b4c16335c749fa48d33c95a38"
ROOT = Path("poems/kalaignarin-kavithaigal")
EN = ROOT / "translations/en"


def read(path):
    return Path(path).read_text(encoding="utf-8")

def write(path, text):
    Path(path).write_text(text, encoding="utf-8")

def rep(path, old, new, required=True):
    p = Path(path); t = read(p)
    if old not in t:
        if required:
            raise SystemExit(f"required text missing in {p}: {old[:100]!r}")
        return False
    write(p, t.replace(old, new))
    return True

def replace_tail(path, heading, new_tail):
    p=Path(path); t=read(p)
    i=t.find(heading)
    if i < 0: raise SystemExit(f"heading missing in {p}: {heading}")
    write(p, t[:i] + new_tail.rstrip() + "\n")

# 1. Repair the one drafting provenance omission in item 8.
p8 = EN / "items/08-the-pilavanga-year-en.md"
t = read(p8)
needle = 'those who pour out whatever comes to the tongue,\nsaying “my tongue is simply trained so,”\nwill stand neither in front nor behind in the ranks of intelligence;'
replacement = 'those who pour out whatever comes to the tongue,\nsaying “my tongue is simply trained so,”\nwithin the ranks of intelligence —\n\n<!-- scan 98 -->\n\nwill stand neither in front nor behind;'
if '<!-- scan 98 -->' not in t:
    if needle not in t: raise SystemExit('item 8 scan-98 insertion anchor missing')
    t=t.replace(needle,replacement)
    write(p8,t)

# 2. Exact marker/title/status validation for user-expanded Batch 04.
items = {
  6:("06-freedom-fighters-en.md","விடுதலை வீரர்கள்","Freedom Fighters",range(72,80)),
  7:("07-the-five-senses-en.md","ஐம்புலன்","The Five Senses",range(80,90)),
  8:("08-the-pilavanga-year-en.md","பிலவங்க ஆண்டு","The Pilavanga Year",range(90,101)),
  9:("09-love-or-valour-en.md","காதலா - வீரமா?","Love or Valour?",range(101,116)),
 10:("10-six-in-the-noble-scripture-en.md","அருமறையில் அறுவர்","Six in the Noble Scripture",range(116,128)),
}
marker_total=0
for no,(fn,ta,en,rg) in items.items():
    s=read(EN/"items"/fn)
    if f'item: {no}' not in s or f'title_ta: "{ta}"' not in s or f'title_en: "{en}"' not in s:
        raise SystemExit(f"metadata mismatch item {no}")
    if 'status: "batch-reviewed"' not in s: raise SystemExit(f"status not reviewed item {no}")
    markers=[int(x) for x in re.findall(r'<!-- scan (\d+) -->',s)]
    exp=list(rg)
    if markers != exp: raise SystemExit(f"marker mismatch item {no}: {markers} != {exp}")
    marker_total += len(markers)
if marker_total != 56: raise SystemExit(f"batch marker total {marker_total} != 56")

# 3. Finalize Batch-04 review record.
batch=EN/"batches/batch-04.md"
rep(batch, '**REVIEWED — PASS, subject to final mechanical marker/status synchronization in this same activity.**', '**REVIEWED — PASS.**')
rep(batch, 'Batch-owned source scans: **56/56**.', 'Batch-owned source scans: **56/56**.\n\nMechanical scan-marker certification: **56/56 PASS** — exact marker sequences 72–127 across items 6–10.')

# 4. Translation plan.
plan=EN/"TRANSLATION_PLAN.md"
rep(plan,'**PHASE 4 IN PROGRESS — Batches 01–03 reviewed PASS.**','**PHASE 4 IN PROGRESS — Batches 01–04 reviewed PASS.**')
rep(plan,'- batches: **3**;','- batches: **4**;')
rep(plan,'- items: **5/77**;','- items: **10/77**;')
rep(plan,'- item-assigned source scans: **50/439**;','- item-assigned source scans: **106/439**;')
rep(plan,'| 04 | 6–7 | 72–89 | **NEXT** |\n| later | 8–77 | adaptive complete-item batches | pending |','| 04 | 6–10 | 72–127 | **reviewed — PASS** |\n| 05 | 11–13 | 128–154 | **NEXT** |\n| later | 14–77 | adaptive complete-item batches | pending |')
pt=read(plan)
if '## Batch 04 decision record' not in pt:
    insert='''## Batch 04 decision record\n\nAt the user's explicit direction, Batch 04 was expanded from the planned two items to **items 6–10** and completed as one complete-item batch across scans **72–127**. Structural anthology scans **70–71** remain outside poem translations.\n\nThe reviewed translation preserves:\n\n- item 6 `விடுதலை வீரர்கள்` as **Freedom Fighters**, including the 15 August 1967 Tiruchirappalli Radio context, Kattabomman / Marudhu / Bharati / V. V. S. Aiyar / V. O. C. hand-offs, independence rhetoric and closing social definition of freedom;\n- item 7 `ஐம்புலன்` as **The Five Senses**, including the body/mouth/eye/nose/ear structure, `மெய்` body/truth wordplay, Tirukkural citations and every poet hand-off;\n- item 8 `பிலவங்க ஆண்டு` as **The Pilavanga Year**, retaining cyclic year names, the six-women dream, six Tirukkural virtues, rationalist/social satire and all **11/11** scan markers after mechanical repair of the drafting-only missing scan-98 marker;\n- item 9 canonical `காதலா - வீரமா?` as **Love or Valour?**, while preserving contents witness `காதலா! - வீரமா?` separately, with the full debate alternation and classical/modern examples;\n- item 10 `அருமறையில் அறுவர்` as **Six in the Noble Scripture**, with the six Tirukkural human types, ministerial synthesis and all guest-poet transitions;\n- Batch-04 marker coverage **56/56**, title decisions **4 exact + 1 authorised variant**, unresolved translation issues **0**, Tamil `pages/`/`sections/` changes **0**.\n\n'''
    pt=pt.replace('## Exact next activity\n',insert+'## Exact next activity\n')
    write(plan,pt)
replace_tail(plan,'## Exact next activity\n','''## Exact next activity\n\nExecute **Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)** from the Tamil final-cleared canonical layer. Translate all three complete items across scans **128–154**, preserve item 12's contents witness `உடன்பிறப்பின் பற்று` separately from canonical `உடைமைகள் பத்து`, review the full 27-scan batch, and leave Tamil final-cleared files unchanged.''')

# 5. English source map.
sm=EN/"SOURCE_MAP.md"; st=read(sm)
row5='| 5 | `வாளி மன்னன்` | `வாளி மன்னன்` | **King Vali** | 62–69 | 45–52 | `items/05-king-vali-en.md` | **batch-reviewed — PASS** |'
rows='''| 6 | `விடுதலை வீரர்கள்` | `விடுதலை வீரர்கள்` | **Freedom Fighters** | 72–79 | 55–62 | `items/06-freedom-fighters-en.md` | **batch-reviewed — PASS** |\n| 7 | `ஐம்புலன்` | `ஐம்புலன்` | **The Five Senses** | 80–89 | 63–72 | `items/07-the-five-senses-en.md` | **batch-reviewed — PASS** |\n| 8 | `பிலவங்க ஆண்டு` | `பிலவங்க ஆண்டு` | **The Pilavanga Year** | 90–100 | 73–83 | `items/08-the-pilavanga-year-en.md` | **batch-reviewed — PASS** |\n| 9 | `காதலா - வீரமா?` | `காதலா! - வீரமா?` | **Love or Valour?** | 101–115 | 84–98 | `items/09-love-or-valour-en.md` | **batch-reviewed — PASS** |\n| 10 | `அருமறையில் அறுவர்` | `அருமறையில் அறுவர்` | **Six in the Noble Scripture** | 116–127 | 99–110 | `items/10-six-in-the-noble-scripture-en.md` | **batch-reviewed — PASS** |'''
if '| 6 | `விடுதலை வீரர்கள்`' not in st:
    if row5 not in st: raise SystemExit('source-map item5 row missing')
    st=st.replace(row5,row5+'\n'+rows)
prov='''### Items 6–10 provenance notes\n\n- scans **70–71** remain the separate `கவியரங்கக் கவிதைகள்` anthology divider/verso and are not duplicated into item translations;\n- item 6 owns scans **72–79** (**8/8** represented);\n- item 7 owns scans **80–89** (**10/10** represented);\n- item 8 owns scans **90–100** (**11/11** represented);\n- item 9 owns scans **101–115** (**15/15** represented);\n- item 10 owns scans **116–127** (**12/12** represented);\n- item 9 alone carries an authorised contents-title punctuation variant; items 6, 7, 8 and 10 are exact title witnesses;\n- no Tamil page or canonical item was changed by Batch 04.\n\n'''
if '### Items 6–10 provenance notes' not in st:
    st=st.replace('## Progress\n',prov+'## Progress\n')
st=st.replace('- reviewed English batches: **3**;','- reviewed English batches: **4**;')
st=st.replace('- reviewed English items: **5/77**;','- reviewed English items: **10/77**;')
st=st.replace('- reviewed item-assigned scans: **50/439**;','- reviewed item-assigned scans: **106/439**;')
idx=st.find('## Exact next mapping activity\n')
if idx<0: raise SystemExit('source map next heading missing')
st=st[:idx]+'''## Exact next mapping activity\n\nAdd reviewed mappings for **items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)** after Phase-4 Batch 05 passes. Item 12 must preserve contents witness `உடன்பிறப்பின் பற்று` separately from canonical `உடைமைகள் பத்து`.\n'''
write(sm,st)

# 6. English README.
er=EN/"README.md"; et=read(er)
et=et.replace('**PHASE 4 IN PROGRESS — Batches 01–03 reviewed PASS.**','**PHASE 4 IN PROGRESS — Batches 01–04 reviewed PASS.**')
et=et.replace('- reviewed English batches: **3**;','- reviewed English batches: **4**;')
et=et.replace('- reviewed English items: **5/77**;','- reviewed English items: **10/77**;')
et=et.replace('- item-assigned source scans covered by reviewed English: **50/439**;','- item-assigned source scans covered by reviewed English: **106/439**;')
if '`batches/batch-04.md`' not in et:
    anchor='- `items/05-king-vali-en.md` — reviewed English item 5.'
    addition='''- `batches/batch-04.md` — reviewed Batch-04 record;\n- `items/06-freedom-fighters-en.md` — reviewed English item 6;\n- `items/07-the-five-senses-en.md` — reviewed English item 7;\n- `items/08-the-pilavanga-year-en.md` — reviewed English item 8;\n- `items/09-love-or-valour-en.md` — reviewed English item 9;\n- `items/10-six-in-the-noble-scripture-en.md` — reviewed English item 10.'''
    if anchor not in et: raise SystemExit('English README item5 anchor missing')
    et=et.replace(anchor,anchor+'\n'+addition)
if '## Batch 04' not in et:
    b4='''## Batch 04\n\n**Reviewed — PASS.**\n\nUser-authorized expanded batch covering complete items **6–10** across scans **72–127**. Structural scans **70–71** remain outside poem bodies.\n\n- item 6 `விடுதலை வீரர்கள்` → **Freedom Fighters**, scans **72–79**;\n- item 7 `ஐம்புலன்` → **The Five Senses**, scans **80–89**;\n- item 8 `பிலவங்க ஆண்டு` → **The Pilavanga Year**, scans **90–100**;\n- item 9 `காதலா - வீரமா?` → **Love or Valour?**, scans **101–115**;\n- item 10 `அருமறையில் அறுவர்` → **Six in the Noble Scripture**, scans **116–127**;\n- reviewed scans: **56/56**;\n- title witnesses: **4 exact / 1 authorised variant**;\n- unresolved translation issues: **0**;\n- Tamil changes: **0**.\n\n'''
    et=et.replace('## Exact next activity\n',b4+'## Exact next activity\n')
i=et.find('## Exact next activity\n')
if i<0: raise SystemExit('English README next heading missing')
et=et[:i]+'''## Exact next activity\n\nExecute **Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**, scans **128–154**, reviewing all three complete items before advancing.\n'''
write(er,et)

# 7. Handover.
h=Path('HANDOVER.md'); ht=read(h)
ht=ht.replace('## Durable state after Phase 4 Batch 03','## Durable state after Phase 4 Batch 04')
ht=ht.replace('Phase 4 English translation/release: **IN PROGRESS — Batches 01–03 reviewed PASS; 5/77 items; 50/439 item-assigned scans; Batch 04 NEXT**.','Phase 4 English translation/release: **IN PROGRESS — Batches 01–04 reviewed PASS; 10/77 items; 106/439 item-assigned scans; Batch 05 NEXT**.')
if '## Phase 4 durable result — Batch 04' not in ht:
    sec='''## Phase 4 durable result — Batch 04\n\n- user-authorized expanded batch: **items 6–10**;\n- reviewed batches: **4**;\n- reviewed English items: **10/77**;\n- reviewed item-assigned source scans: **106/439**;\n- Batch 04 source scans: **72–127 = 56/56**;\n- structural anthology scans **70–71** remain outside poem translations;\n- item 6 `விடுதலை வீரர்கள்` → **Freedom Fighters**;\n- item 7 `ஐம்புலன்` → **The Five Senses**;\n- item 8 `பிலவங்க ஆண்டு` → **The Pilavanga Year**;\n- item 9 `காதலா - வீரமா?` → **Love or Valour?**, with contents `காதலா! - வீரமா?` retained separately;\n- item 10 `அருமறையில் அறுவர்` → **Six in the Noble Scripture**;\n- marker certification: **56/56 PASS**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes during Batch 04: **0**;\n- Tamil `sections/` changes during Batch 04: **0**.\n\nBatch review: `translations/en/batches/batch-04.md`.\n\n'''
    ht=ht.replace('## Supplied-transcription rule\n',sec+'## Supplied-transcription rule\n')
ht=ht.replace('`translations/en/batches/batch-03.md`','`translations/en/batches/batch-04.md`')
i=ht.find('## EXACT NEXT ACTIVITY\n')
if i<0: raise SystemExit('handover exact next missing')
ht=ht[:i]+'''## EXACT NEXT ACTIVITY\n\nExecute **Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**.\n\nRead final-cleared `sections/11.md` through `sections/13.md` completely, translate all three complete items across scans **128–154**, preserve item 12 contents witness `உடன்பிறப்பின் பற்று` separately from canonical `உடைமைகள் பத்து`, review them together in `translations/en/batches/batch-05.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged.\n'''
write(h,ht)

# 8. Next-chat prompt.
n=Path('NEXT_CHAT_PROMPT.md'); nt=read(n)
nt=nt.replace('Phase 4 English translation/release **IN PROGRESS — Batches 01–03 reviewed PASS; 5/77 items; 50/439 item scans; Batch 04 NEXT**.','Phase 4 English translation/release **IN PROGRESS — Batches 01–04 reviewed PASS; 10/77 items; 106/439 item scans; Batch 05 NEXT**.')
old_head='## Phase 4 Batches 01–03 durable result\n'
if old_head in nt:
    start=nt.index(old_head); end=nt.index('Follow `translations/en/TRANSLATION_PLAN.md`',start)
    sec='''## Phase 4 Batches 01–04 durable result\n\n- translation scaffold: `translations/en/`;\n- reviewed batches: **4**;\n- reviewed English items: **10/77**;\n- reviewed item scans: **106/439**;\n- Batch 04 is the user-authorized expanded items **6–10** batch, scans **72–127 = 56/56**;\n- item 6 `விடுதலை வீரர்கள்` → **Freedom Fighters**;\n- item 7 `ஐம்புலன்` → **The Five Senses**;\n- item 8 `பிலவங்க ஆண்டு` → **The Pilavanga Year**;\n- item 9 `காதலா - வீரமா?` → **Love or Valour?**, contents `காதலா! - வீரமா?` preserved separately;\n- item 10 `அருமறையில் அறுவர்` → **Six in the Noble Scripture**;\n- structural scans **32–33, 70–71** remain anthology provenance outside poem bodies;\n- Batch-04 marker certification **56/56 PASS**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page/canonical changes: **0**.\n\n'''
    nt=nt[:start]+sec+nt[end:]
i=nt.find('## EXACT NEXT ACTIVITY\n')
if i<0: raise SystemExit('next-chat exact next missing')
nt=nt[:i]+'''## EXACT NEXT ACTIVITY\n\nExecute **Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**.\n\n1. Read final-cleared `sections/11.md`, `sections/12.md`, `sections/13.md` completely.\n2. Translate all three complete items across scans **128–154**.\n3. Preserve item 12 contents witness `உடன்பிறப்பின் பற்று` separately from canonical `உடைமைகள் பத்து`.\n4. Review the full 27-scan batch and update English item files, `batches/batch-05.md` and `SOURCE_MAP.md`.\n5. Do **not** alter Tamil final-cleared `pages/` or `sections/`.\n'''
write(n,nt)

# 9. Shared durable status documents: targeted current-frontier replacements.
shared=[Path('README.md'),Path('TRANSCRIPTION_PHASE_PLAN.md'),ROOT/'README.md',ROOT/'SOURCE_INTAKE.md',ROOT/'metadata/source.md',ROOT/'indexes/page-map.md',ROOT/'PHASE3_TAMIL_FINAL_CLEARANCE.md']
for p in shared:
    x=read(p)
    x=x.replace('Batches 01–03 reviewed PASS; 5/77 items; 50/439 item scans; Batch 04 NEXT','Batches 01–04 reviewed PASS; 10/77 items; 106/439 item scans; Batch 05 NEXT')
    x=x.replace('Batches 01–03 reviewed PASS; 5/77 items; 50/439 item-assigned scans; Batch 04 NEXT','Batches 01–04 reviewed PASS; 10/77 items; 106/439 item-assigned scans; Batch 05 NEXT')
    x=x.replace('Batches 01–03 reviewed PASS','Batches 01–04 reviewed PASS')
    x=x.replace('reviewed batches: **3**','reviewed batches: **4**')
    x=x.replace('reviewed English items: **5/77**','reviewed English items: **10/77**')
    x=x.replace('reviewed items: **5/77**','reviewed items: **10/77**')
    x=x.replace('reviewed item-assigned source scans: **50/439**','reviewed item-assigned source scans: **106/439**')
    x=x.replace('reviewed item scans: **50/439**','reviewed item scans: **106/439**')
    x=x.replace('50/439 item-assigned scans','106/439 item-assigned scans')
    x=x.replace('Batch 04 items 6–7: **NEXT**','Batch 05 items 11–13: **NEXT**')
    x=x.replace('Batch 04 items 6–7 are next','Batch 05 items 11–13 are next')
    x=x.replace('Batch 04 items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)','Batch 05 items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)')
    write(p,x)

# Root README phase-progress paragraph and next activity.
p=Path('README.md'); x=read(p)
x=re.sub(r'## Phase 4 translation progress\n\n.*?\n\n## Supplied lexical controls', '''## Phase 4 translation progress\n\nBatches 01–04 now cover items **1–10**. The reviewed English layer covers **10/77 items** and **106/439 item-assigned source scans** with **0** unresolved reviewed translation issues. Batch 04 is the user-authorized expanded items 6–10 batch across scans **72–127**; structural scans **70–71** remain outside poem translations. Files live under `poems/kalaignarin-kavithaigal/translations/en/`. No Tamil page or canonical item has been changed by translation work.\n\n## Supplied lexical controls''',x,flags=re.S)
x=re.sub(r'## Next activity\n\n.*?\n?\Z','''## Next activity\n\n**Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**, scans **128–154**. Translate and review all three complete final-cleared items; preserve item 12's contents-title variant separately and leave Tamil archival files unchanged.\n''',x,flags=re.S)
write(p,x)

# Phase plan explicit Phase-4 block.
p=Path('TRANSCRIPTION_PHASE_PLAN.md'); x=read(p)
x=x.replace('**IN PROGRESS — Batches 01–03 reviewed PASS.**','**IN PROGRESS — Batches 01–04 reviewed PASS.**')
x=x.replace('- reviewed batches: **3**;','- reviewed batches: **4**;').replace('- reviewed English items: **5/77**;','- reviewed English items: **10/77**;').replace('- reviewed item-assigned source scans: **50/439**;','- reviewed item-assigned source scans: **106/439**;')
x=x.replace('- Batch 03: item 4 `இரணியன்` → **Hiranyan**; item 5 `வாளி மன்னன்` → **King Vali**;','- Batch 03: item 4 `இரணியன்` → **Hiranyan**; item 5 `வாளி மன்னன்` → **King Vali**;\n- Batch 04: items 6–10 → **Freedom Fighters; The Five Senses; The Pilavanga Year; Love or Valour?; Six in the Noble Scripture**, scans **72–127**;') if '- Batch 03: item 4' in x else x
x=re.sub(r'## EXACT NEXT ACTIVITY\n\n.*?\Z','''## EXACT NEXT ACTIVITY\n\nExecute **Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)** from the Tamil final-cleared canonical layer across scans **128–154**. Review all three complete translations before marking the batch PASS; preserve item 12's title witnesses separately and do not alter Tamil final-cleared files.\n''',x,flags=re.S)
write(p,x)

# Active README Phase 4 block and next.
p=ROOT/'README.md'; x=read(p)
x=re.sub(r'## Phase 4 — English translation\n\n.*?\n\n## Next activity', '''## Phase 4 — English translation\n\n**IN PROGRESS — Batches 01–04 reviewed PASS.**\n\n- translation root: `translations/en/`;\n- reviewed batches: **4**;\n- reviewed items: **10/77**;\n- reviewed item-assigned scans: **106/439**;\n- Batch 04: items 6–10 across scans **72–127**, **56/56 PASS**;\n- title decisions in Batch 04: **4 exact / 1 authorised variant**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` / `sections/` changes: **0**.\n\n## Next activity''',x,flags=re.S)
x=re.sub(r'## Next activity\n\n.*?\Z','''## Next activity\n\n**Phase 4 Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**. Translate all three complete final-cleared items across scans **128–154** and review the batch before advancing.\n''',x,flags=re.S)
write(p,x)

# Source intake Phase4 state.
p=ROOT/'SOURCE_INTAKE.md'; x=read(p)
x=x.replace('Batches 01–03 are reviewed PASS; Batch 04 items 6–7 are next.','Batches 01–04 are reviewed PASS; Batch 05 items 11–13 are next.')
idx=x.find('## Phase 4 translation state\n')
if idx>=0:
    x=x[:idx]+'''## Phase 4 translation state\n\n- Batches 01–04: **reviewed PASS**;\n- reviewed items: **10/77**;\n- reviewed item scans: **106/439**;\n- Batch 04: items **6–10**, scans **72–127 = 56/56**;\n- structural scans **70–71** remain outside poem translations;\n- unresolved reviewed translation issues: **0**;\n- Tamil page/canonical changes: **0**;\n- exact next: **Batch 05 items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**, scans **128–154**.\n'''
write(p,x)

# Metadata Phase4 block.
p=ROOT/'metadata/source.md'; x=read(p)
idx=x.find('## Phase 4 translation metadata\n')
if idx>=0:
    x=x[:idx]+'''## Phase 4 translation metadata\n\n- Tamil source/canonical layer remains **FINAL-CLEARED**;\n- reviewed batches: **4**;\n- reviewed English items: **10/77**;\n- reviewed item scans: **106/439**;\n- Batch 04 English items: `../translations/en/items/06-freedom-fighters-en.md` through `../translations/en/items/10-six-in-the-noble-scripture-en.md`;\n- Batch 04 review: `../translations/en/batches/batch-04.md`;\n- Batch 04 marker certification: **56/56 PASS**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page/canonical changes caused by translation: **0**;\n- next translation batch: **items 11–13**, scans **128–154**.\n'''
write(p,x)

# Audit: add Batch 04 and next.
p=ROOT/'audit.md'; x=read(p)
if '## Phase 4 Batch 04 audit' not in x:
    x=re.sub(r'### Exact next Phase-4 activity\n\n.*?\Z','''## Phase 4 Batch 04 audit — REVIEWED / PASS\n\nScope: user-authorized expanded English translation/review of final-cleared canonical items **6–10**.\n\n- items after Batch 04: **10/77**;\n- Batch-04 item-owned scans: **56/56 — scans 72–127**;\n- cumulative reviewed item-owned scans: **106/439**;\n- structural scans **70–71** excluded from poem bodies: **PASS**;\n- title decisions: **4 exact / 1 authorised variant / 0 unresolved**;\n- exact English scan-marker sequences: **56/56 PASS**;\n- omission/duplication issues: **0**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page-record changes: **0**;\n- Tamil canonical-item changes: **0**;\n- batch evidence: `translations/en/batches/batch-04.md`.\n\n### Exact next Phase-4 activity\n\n**Batch 05 — items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**, scans **128–154**.\n''',x,flags=re.S)
write(p,x)

# Page map current translation note.
p=ROOT/'indexes/page-map.md'; x=read(p)
x=re.sub(r'## Phase 4 translation note\n\n.*?\Z','''## Phase 4 translation note\n\nPhase 4 Batches 01–04 reviewed items **1–10** across **106/439** item-assigned scans. Batch 04 covers item scans **72–127 = 56/56**; structural scans **70–71** remain separate anthology provenance. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 05 items **11–13**, scans **128–154**.\n''',x,flags=re.S)
write(p,x)

# Gate6 subsequent-status note.
p=ROOT/'PHASE3_TAMIL_FINAL_CLEARANCE.md'; x=read(p)
x=re.sub(r'## Subsequent Phase 4 status\n\n.*?\Z','''## Subsequent Phase 4 status\n\nPhase 4 has subsequently advanced through **Batches 01–04, all reviewed PASS**. Reviewed English now covers items **1–10/77** and **106/439** item-assigned scans. Batch 04 is the user-authorized items 6–10 expansion across scans **72–127**. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Exact next translation activity: **Batch 05 items 11–13 (`புதிய பாதை`, `உடைமைகள் பத்து`, `நீர்க் குடும்பம்`)**, scans **128–154**.\n''',x,flags=re.S)
write(p,x)

# 10. Final guards: no Tamil source/canonical changes from pre-Batch04 checkpoint.
changed=subprocess.check_output(['git','diff','--name-only',BASE],text=True).splitlines()
for f in changed:
    if f.startswith('poems/kalaignarin-kavithaigal/pages/') or f.startswith('poems/kalaignarin-kavithaigal/sections/'):
        raise SystemExit(f'Tamil layer modified unexpectedly: {f}')

# Confirm current progress records.
for p in [Path('HANDOVER.md'),Path('NEXT_CHAT_PROMPT.md'),EN/'TRANSLATION_PLAN.md',EN/'SOURCE_MAP.md',EN/'README.md']:
    s=read(p)
    if '10/77' not in s or ('106/439' not in s): raise SystemExit(f'progress missing in {p}')

print('Batch04 finalize PASS: items=5 scans=56 cumulative_items=10 cumulative_scans=106 Tamil_changes=0')
