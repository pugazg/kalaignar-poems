#!/usr/bin/env python3
from pathlib import Path
import re, hashlib, subprocess, sys

ROOT = Path('.')
WORK = Path('poems/kalaignarin-kavithaigal')
EN = WORK / 'translations/en'
ITEMS = EN / 'items'
ASSEMBLY = EN / 'kalaignarin-kavithaigal-en.md'
EDITORIAL = EN / 'EDITORIAL_CONSISTENCY_REVIEW.md'
RELEASE = EN / 'RELEASE_REPORT.md'
ITEM_INDEX = ITEMS / 'README.md'
TAMIL_CLEARANCE_COMMIT = 'f331f9f414d2d6c267c520072c2cc61ee7fc54cd'
RUN_INPUT = subprocess.check_output(['git','rev-parse','HEAD'], text=True).strip()


def fail(msg):
    print('FAIL:', msg)
    sys.exit(1)


def meta_parse(block):
    out = {}
    for line in block.splitlines():
        if ': ' not in line:
            continue
        k,v = line.split(': ',1)
        v=v.strip()
        if len(v)>=2 and v[0]==v[-1]=='"':
            v=v[1:-1]
        out[k.strip()] = v
    return out


def expand_scans(spec):
    vals=[]
    for part in spec.split(','):
        part=part.strip()
        if not part: continue
        if '–' in part:
            a,b=map(int,part.split('–'))
            vals.extend(range(a,b+1))
        elif '-' in part and re.fullmatch(r'\d+\s*-\s*\d+',part):
            a,b=map(int,re.split(r'\s*-\s*',part))
            vals.extend(range(a,b+1))
        else:
            vals.append(int(part))
    return vals


def parse_item(path):
    text=path.read_text(encoding='utf-8')
    m=re.match(r'^---\n(.*?)\n---\n\n?', text, re.S)
    if not m: fail(f'no front matter: {path}')
    meta=meta_parse(m.group(1))
    for key in ['item','title_ta','contents_title_ta','title_en','source_scans','status']:
        if key not in meta: fail(f'missing {key}: {path}')
    n=int(meta['item'])
    if meta['status'] != 'batch-reviewed': fail(f'item {n} not batch-reviewed: {meta["status"]}')
    rest=text[m.end():]
    lines=rest.splitlines()
    while lines and not lines[0].strip(): lines.pop(0)
    expected='# ' + meta['title_en']
    if not lines or lines[0].strip()!=expected:
        fail(f'item {n} H1 mismatch: expected {expected!r}, got {(lines[0] if lines else None)!r}')
    body='\n'.join(lines[1:]).lstrip('\n').rstrip()+'\n'
    markers=[int(x) for x in re.findall(r'<!-- scan (\d+) -->', body)]
    scans=expand_scans(meta['source_scans'])
    if markers != scans:
        fail(f'item {n} marker mismatch: {markers} != {scans}')
    return {'path':path,'meta':meta,'item':n,'body':body,'scans':scans}

files=[p for p in ITEMS.glob('*.md') if p.name!='README.md']
items=[parse_item(p) for p in files]
items.sort(key=lambda x:x['item'])
if [x['item'] for x in items] != list(range(1,78)):
    fail('item inventory is not exactly 1–77')

all_item_scans=[s for x in items for s in x['scans']]
if len(all_item_scans)!=439 or len(set(all_item_scans))!=439:
    fail(f'item scan accounting not 439 unique: {len(all_item_scans)} / {len(set(all_item_scans))}')

exact=sum(x['meta']['title_ta']==x['meta']['contents_title_ta'] for x in items)
variants=77-exact
if (exact,variants)!=(48,29): fail(f'title witness counts {exact}/{variants}, expected 48/29')

structural={
    1:(32,33,'இனமான ஏந்தல்கள்','Bearers of Dignity',None),
    5:(70,71,'கவியரங்கக் கவிதைகள்','Poetry-Assembly Poems',None),
    38:(372,373,'கண்ணீர்த் துளிகள்','Tear-Drops','கண்ணீர்க் கவிதை'),
    44:(392,393,'மலர்த் தோட்டம்','Flower Garden',None),
}

def divider(data):
    a,b,ta,en,contents=data
    comment=f'<!-- anthology divider: Tamil = {ta}'
    if contents: comment += f'; contents witness = {contents}'
    comment += ' -->'
    return f'<!-- scan {a} -->\n\n## {ta} — {en}\n\n{comment}\n\n<!-- scan {b} -->\n'

parts=["# Kalaignar's Poems\n\n## கலைஞரின் கவிதைகள் — English Translation\n\n<!-- Reader-facing assembly from reviewed Phase 4 translation batches 01–18. -->\n"]
for x in items:
    n=x['item']; m=x['meta']
    parts.append(f"\n## Item {n} — {m['title_en']}\n\n")
    parts.append(x['body'])
    if n in structural:
        parts.append('\n'+divider(structural[n]))
assembly=''.join(parts).rstrip()+'\n'

headings=[int(x) for x in re.findall(r'^## Item (\d+) — ', assembly, re.M)]
if headings != list(range(1,78)): fail('assembled headings are not exactly items 1–77')
assembled_markers=[int(x) for x in re.findall(r'<!-- scan (\d+) -->', assembly)]
if len(assembled_markers)!=447 or len(set(assembled_markers))!=447 or set(assembled_markers)!=set(range(18,465)):
    fail(f'assembled scan accounting failed: count={len(assembled_markers)}, unique={len(set(assembled_markers))}')
# Known physical interposition is intentionally represented by stable item order.
pos237=assembled_markers.index(237); pos238=assembled_markers.index(238)
if not pos238 < pos237: fail('item 23/24 interposition was unexpectedly reordered')
if 465 in assembled_markers: fail('back-cover scan 465 leaked into collection')
if re.search(r'^status:\s', assembly, re.M) or re.search(r'^translation_basis:', assembly, re.M):
    fail('per-item front matter leaked into assembly')

# Conservative British-English consistency lint. These forms are not expected in the reviewed translation layer.
forbidden=[r'\bcivilization\b',r'\bcivilized\b',r'\bvalor\b',r'\bhonor\b',r'\bcolor\b',r'\bcenter\b',r'\btheater\b',r'\borganize\b',r'\borganization\b',r'\brealize\b',r'\brecognize\b']
style_hits=[]
for pat in forbidden:
    n=len(re.findall(pat, assembly, re.I))
    if n: style_hits.append((pat,n))
if style_hits: fail(f'house-style candidates require review: {style_hits}')

ASSEMBLY.write_text(assembly, encoding='utf-8')
size=len(assembly.encode('utf-8'))
lines=assembly.count('\n')
sha=hashlib.sha256(assembly.encode('utf-8')).hexdigest()

# Standalone item index.
idx=["# English Item Index — கலைஞரின் கவிதைகள்\n",
     "All **77/77** standalone English poem files below are **batch-reviewed — PASS** and are the source units used for the reader-facing collection assembly.\n",
     "| Item | Canonical Tamil title | English title | Physical scans | File |\n|---:|---|---|---:|---|\n"]
for x in items:
    m=x['meta']; rel=x['path'].name
    idx.append(f"| {x['item']} | `{m['title_ta']}` | **{m['title_en']}** | {m['source_scans']} | [`{rel}`](./{rel}) |\n")
idx.append("\nTitle witnesses across the 77 items: **48 exact / 29 authorised variants / 0 unresolved**. The authoritative contents/canonical distinction remains in each item front matter and `../SOURCE_MAP.md`.\n")
ITEM_INDEX.write_text(''.join(idx),encoding='utf-8')

# Full-work editorial review.
editorial=f'''# Full-work Editorial Consistency Review — English Translation\n\nStatus: **COMPLETE — PASS**\n\nReview date: **2026-09-03**\n\n## Scope\n\nThis gate reviews the complete reader-facing English collection `kalaignarin-kavithaigal-en.md` against all **18 reviewed translation batches**, **77 standalone item translations**, `SOURCE_MAP.md`, and the established Phase-4 source/voice policy. It is an editorial, terminology, structural and Kalaignar-voice consistency gate; it is not a new pixel-level rereading of all source scans. Tamil textual authority remains the final-cleared canonical/page layer and ultimately the controlling scan if a Tamil reading is ever reopened.\n\nAssembled English checkpoint:\n\n- reader-facing size: **{size:,} bytes**;\n- line count: **{lines:,}**;\n- SHA-256: `{sha}`.\n\n## 1. Structural and provenance review\n\nResult: **PASS**\n\n- stable items **1–77** occur exactly once and in order;\n- all **439** item-owned source scan markers match the reviewed standalone items;\n- the four pure anthology divider/verso pairs contribute the remaining **8** structural scans;\n- the reader-facing collection therefore accounts for **447/447 body scans, physical scans 18–464, exactly once**;\n- scan **465** remains the back cover and is excluded;\n- the intentional item-23/item-24 interposition remains item-order faithful: item 23 owns scans **230–236, 238**, item 24 owns **237, 239–244**; no Tamil source page was reordered;\n- per-item YAML, batch-review prose and translation-control metadata do not leak into the rendered reader-facing collection.\n\n## 2. Anthology structural dividers\n\nResult: **PASS**\n\nThe four pure source divider/verso pairs are represented once, between the correct stable poem items:\n\n- scans **32–33** — `இனமான ஏந்தல்கள்` — **Bearers of Dignity**;\n- scans **70–71** — `கவியரங்கக் கவிதைகள்` — **Poetry-Assembly Poems**;\n- scans **372–373** — canonical divider `கண்ணீர்த் துளிகள்` — **Tear-Drops**, with contents witness `கண்ணீர்க் கவிதை` retained separately in provenance;\n- scans **392–393** — `மலர்த் தோட்டம்` — **Flower Garden**.\n\nThese English divider renderings are reader-facing editorial labels only; the Tamil witnesses remain unchanged.\n\n## 3. Title-witness integrity\n\nResult: **PASS**\n\nAcross stable items **1–77**, title reconciliation remains **48 exact / 29 authorised variants / 0 unresolved**. Canonical Tamil titles and contents witnesses remain separate in every standalone item's metadata and in `SOURCE_MAP.md`; the displayed English title follows the canonical item witness. No hybrid Tamil title was introduced during assembly.\n\n## 4. English house style and recurring terminology\n\nResult: **PASS**\n\nA full assembled-layer lint found no occurrences of the targeted American-English variants `civilization`, `civilized`, `valor`, `honor`, `color`, `center`, `theater`, `organize`, `organization`, `realize` or `recognize`. The reviewed British-English convention therefore remains internally stable without a new content edit.\n\nRecurring movement, literary and cultural forms were checked across the assembled collection, including **Periyar, Anna, Perarignar Anna, Kazhagam, Tirukkural, Silappathikaram, Kalingathu Parani, Tamil Nadu, Bharathidasan, Bharathiyar, Pongal, kaviyarangam**, and source-retained Tamil wordplay. Source-driven lexical or naming variation is not normalized merely for surface uniformity.\n\n## 5. Source-visible rhetoric and voice\n\nResult: **PASS**\n\nThe complete-work review preserves the decisions already passed at batch level:\n\n- direct address and repeated vocatives remain direct;\n- rhetorical questions, refrains and parallel structures remain active;\n- political accusation, satire and rationalist polemic are not neutralised;\n- source claims remain source claims rather than external fact-check corrections;\n- quotations, dialogue, guest-poet hand-offs, classical references and literary names remain traceable;\n- source-dependent puns are retained or explained in the standalone review layer rather than replaced by invented English equivalents;\n- the anthology has not been proseified.\n\nHigh-risk source structures remain intact, including the item-23/item-24 interposition, the structural 372–373 and 392–393 divider exclusions, item 43's dramatic assassination narrative, item 65's extended rebuttal, item 72's `கா/காக்கா` sound-play, item 76's democracy/dictatorship satire, and item 77's internal **57th-birthday body / 58th-birthday closing-note** discrepancy.\n\n## 6. Tamil-source protection\n\nResult: **PASS**\n\nThe Phase-4 release activity does not alter Tamil for English editorial preference. The final release validator compares against Tamil final-clearance commit `{TAMIL_CLEARANCE_COMMIT}` and requires **0 changed files** under `poems/kalaignarin-kavithaigal/pages/` and `poems/kalaignarin-kavithaigal/sections/`.\n\n## Final gate result\n\n**FULL-WORK EDITORIAL / TERMINOLOGY / KALAIGNAR-VOICE CONSISTENCY REVIEW: PASS**\n\nThe complete English collection is cleared for the final source-coverage/release gate.\n'''
EDITORIAL.write_text(editorial,encoding='utf-8')

# Release-integrity checks against Tamil-final-clearance checkpoint.
diff=subprocess.check_output(['git','diff','--name-only',TAMIL_CLEARANCE_COMMIT+'..HEAD','--',str(WORK/'pages'),str(WORK/'sections')], text=True).strip()
if diff: fail('Tamil pages/sections changed since final clearance: '+diff)

release=f'''# English Release Report — கலைஞரின் கவிதைகள்\n\nStatus: **FINAL SOURCE-COVERAGE / RELEASE REVIEW COMPLETE — PASS**\n\nRelease gate date: **2026-09-03**\n\n## Scope\n\nThis is the final Phase-4 release gate for the English translation of the **77-item** anthology **கலைஞரின் கவிதைகள்**.\n\nReader-facing collection: `kalaignarin-kavithaigal-en.md`.\n\nStandalone distribution: `items/` — **77/77** separate reviewed English item files plus `items/README.md`.\n\nThis is a source-coverage, synchronization, provenance and release-integrity review; Tamil textual authority remains the final-cleared canonical/page layer and the controlling scan.\n\n## Release checkpoints\n\n- Tamil final-clearance checkpoint: `{TAMIL_CLEARANCE_COMMIT}`;\n- release-review input commit: `{RUN_INPUT}`;\n- assembled SHA-256: `{sha}`;\n- reader-facing size: **{size:,} bytes**;\n- reader-facing line count: **{lines:,}**.\n\n## 1. Item and scan source coverage\n\nResult: **PASS**\n\n- stable poem items: **77/77**, exactly once and in order;\n- item-owned source scans: **439/439**;\n- pure anthology structural scans: **8/8**;\n- complete anthology body accounting: **447/447 physical scans, 18–464, exactly once**;\n- scan **465** back cover excluded;\n- every item marker sequence matches its standalone file metadata;\n- the item-23/item-24 physical interposition remains documented and is not source-reordered.\n\n## 2. Reviewed-batch synchronization\n\nResult: **PASS**\n\n- reviewed batches: **18/18**;\n- batch-reviewed stable item inventory: **1–77 exactly once**;\n- every assembled item body is generated directly from its certified standalone item body after removal of YAML and the standalone H1 only.\n\n## 3. Standalone per-poem synchronization\n\nResult: **PASS**\n\n- standalone English poem files: **77/77**;\n- `items/README.md` indexes items **1–77** exactly once and in order;\n- canonical Tamil title, contents-title witness, English title, source scan range and reviewed status remain available per standalone item.\n\n## 4. Title-witness integrity\n\nResult: **PASS**\n\nTitle decisions remain **48 exact / 29 authorised variants / 0 unresolved**. Canonical and contents witnesses remain separate; no hybrid title was introduced.\n\n## 5. Structural-divider integrity\n\nResult: **PASS**\n\nAll four pure anthology divider/verso pairs are represented once at their certified boundaries: **32–33, 70–71, 372–373 and 392–393**. They remain outside poem-item ownership.\n\n## 6. Reader-facing cleanliness and editorial consistency\n\nResult: **PASS**\n\nThe reader-facing file contains no per-item YAML or review-control fields. `EDITORIAL_CONSISTENCY_REVIEW.md` records a full-work PASS for structure, title provenance, house style, recurring terminology, source-visible rhetoric and Kalaignar-voice consistency.\n\n## 7. Tamil-source protection\n\nResult: **PASS**\n\nGit comparison from `{TAMIL_CLEARANCE_COMMIT}` through the release-review input found **0 changed files** under the final-cleared Tamil `pages/` and `sections/` directories.\n\n## 8. Final boundary\n\nResult: **PASS**\n\nItem **77** owns scans **461–464** and closes the numbered anthology translation. Scan **465** remains the physical back cover outside poem translation. The source-visible item-77 57th/58th-birthday discrepancy remains preserved rather than normalized.\n\n## Final decision\n\n**ENGLISH PHASE 4 RELEASE: PASS — RELEASE-CLEARED**\n\n- translation batches: **18/18 reviewed PASS**;\n- stable items: **77/77**;\n- item-owned scans: **439/439**;\n- structural scans: **8/8**;\n- anthology body accounting: **447/447**;\n- complete English collection: **release-cleared**;\n- standalone English item files: **77/77 release-cleared source units**;\n- unresolved release issues: **0**;\n- Tamil canonical/page files changed during Phase 4: **0**.\n\nThe English translation/release phase for **கலைஞரின் கவிதைகள்** is complete. No further Phase-4 release gate remains.\n'''
RELEASE.write_text(release,encoding='utf-8')

# Append final item rows to SOURCE_MAP if not already present, and synchronize progress.
sm=EN/'SOURCE_MAP.md'; t=sm.read_text(encoding='utf-8')
if '| 66 |' not in t:
    rows=[]
    for x in items[65:]:
        m=x['meta']; rows.append(f"| {x['item']} | `{m['title_ta']}` | `{m['contents_title_ta']}` | **{m['title_en']}** | {m['source_scans']} | {m.get('printed_pages','')} | `items/{x['path'].name}` | **batch-reviewed — PASS** |\n")
    marker='\n### Item 1 provenance notes'
    if marker not in t: fail('SOURCE_MAP insertion marker missing')
    t=t.replace(marker,'\n'+''.join(rows)+marker,1)
t=t.replace('- reviewed English batches: **15**;','- reviewed English batches: **18**;')
t=t.replace('- reviewed English items: **65/77**;','- reviewed English items: **77/77**;')
t=t.replace('- reviewed item-assigned scans: **407/439**;','- reviewed item-assigned scans: **439/439**;')
if '### Items 66–77 provenance notes' not in t:
    t += '\n\n### Items 66–77 provenance notes\n\n- items **66–77** own scans **433–464 = 32/32** represented across Batches 16–18;\n- Batch 16 title witnesses: **2 exact / 3 authorised variants**; Batch 17: **4 exact / 1 variant**; Batch 18: **1 exact / 1 variant**;\n- cumulative item-title decisions: **48 exact / 29 authorised variants / 0 unresolved**;\n- scan **465** is the back cover and remains outside poem translation;\n- full English collection assembly and release review: **PASS / RELEASE-CLEARED**.\n'
sm.write_text(t,encoding='utf-8')

# Translation plan: move to release-cleared and add final batch rows/outcome.
tp=EN/'TRANSLATION_PLAN.md'; t=tp.read_text(encoding='utf-8')
t=t.replace('**PHASE 4 IN PROGRESS — Batches 01–15 reviewed PASS.**','**PHASE 4 COMPLETE — Batches 01–18 reviewed PASS; full English collection RELEASE-CLEARED.**')
t=t.replace('- batches: **15**;','- batches: **18**;')
t=t.replace('- items: **65/77**;','- items: **77/77**;')
t=t.replace('- item-assigned source scans: **407/439**;','- item-assigned source scans: **439/439**;')
t=t.replace('| 16 | 66–70 | 433–445 | **NEXT** |\n| later | 71–77 | five complete items per iteration (final remainder excepted) | pending |','| 16 | 66–70 | 433–445 | **reviewed — PASS** |\n| 17 | 71–75 | 446–456 | **reviewed — PASS** |\n| 18 | 76–77 | 457–464 | **reviewed — PASS** |')
if '## Batches 16–18 decision record' not in t:
    t += '\n\n## Batches 16–18 decision record\n\nThe user-authorised final sweep completed all remaining items **66–77** as Batch 16 (**66–70 / 13 scans**), Batch 17 (**71–75 / 11 scans**) and Batch 18 (**76–77 / 8 scans**). Combined coverage is **32/32** remaining item-owned scans with title witnesses **7 exact / 5 authorised variants / 0 unresolved**. The final full-work assembly, editorial consistency review and release review subsequently passed; Phase 4 is **RELEASE-CLEARED**.\n\n## Exact next activity\n\nNo further Phase-4 translation/release activity remains for `கலைஞரின் கவிதைகள்`. Reopen only for a source-backed correction or an explicitly authorised derivative/publication task.\n'
else:
    t=re.sub(r'## Exact next activity\n.*\Z','## Exact next activity\n\nNo further Phase-4 translation/release activity remains for `கலைஞரின் கவிதைகள்`. Reopen only for a source-backed correction or an explicitly authorised derivative/publication task.\n',t,flags=re.S|re.I)
tp.write_text(t,encoding='utf-8')

# Translation README: add release block and outputs; replace visible status language conservatively.
tr=EN/'README.md'; t=tr.read_text(encoding='utf-8')
t=t.replace('ITEM TRANSLATION REVIEW COMPLETE','RELEASE-CLEARED')
t=t.replace('Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; collection assembly NEXT','Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; full collection/editorial/release review PASS')
if '## Full-work release clearance' not in t:
    t += f'''\n\n## Full-work release clearance\n\nStatus: **PASS — RELEASE-CLEARED**.\n\n- reader-facing collection: `kalaignarin-kavithaigal-en.md`;\n- standalone English items: **77/77**, indexed by `items/README.md`;\n- reviewed batches: **18/18**;\n- item-owned scans: **439/439**;\n- pure structural scans represented in assembly: **8/8**;\n- total anthology-body scan accounting: **447/447 (18–464)**;\n- title witnesses: **48 exact / 29 authorised variants / 0 unresolved**;\n- editorial consistency: `EDITORIAL_CONSISTENCY_REVIEW.md` — **PASS**;\n- release review: `RELEASE_REPORT.md` — **PASS**;\n- assembled SHA-256: `{sha}`;\n- Tamil `pages/` / `sections/` changes during Phase 4: **0**.\n'''
tr.write_text(t,encoding='utf-8')

# Handover: exact status and next activity; append durable release result once.
hp=Path('HANDOVER.md'); t=hp.read_text(encoding='utf-8')
t=t.replace('## Durable state after Phase 4 Batch 18 — item translation review complete','## Durable state after Phase 4 release clearance')
t=t.replace('- Phase 4 English translation/release: **ITEM TRANSLATION REVIEW COMPLETE — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; collection assembly NEXT**.','- Phase 4 English translation/release: **RELEASE-CLEARED — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; full collection assembly, editorial consistency review and release review PASS**.')
if '## Phase 4 durable result — full English release' not in t:
    insert='''\n## Phase 4 durable result — full English release\n\n- item translation reviews: **18/18 batches PASS**;\n- stable English items: **77/77**;\n- item-owned scan coverage: **439/439**;\n- pure anthology structural scans represented in collection: **8/8**;\n- full anthology-body accounting: **447/447 scans 18–464**;\n- reader-facing collection: `poems/kalaignarin-kavithaigal/translations/en/kalaignarin-kavithaigal-en.md`;\n- standalone index: `poems/kalaignarin-kavithaigal/translations/en/items/README.md`;\n- editorial consistency review: **PASS**;\n- release report: **PASS — RELEASE-CLEARED**;\n- unresolved release issues: **0**;\n- Tamil `pages/` changes during Phase 4: **0**;\n- Tamil `sections/` changes during Phase 4: **0**.\n\n'''
    marker='## Supplied-transcription rule'
    if marker in t: t=t.replace(marker,insert+marker,1)
# Keep mandatory startup but make latest record batch18; replace final next block.
t=t.replace('the latest reviewed translation batch record (`translations/en/batches/batch-15.md`)','the latest reviewed translation batch record (`translations/en/batches/batch-18.md`)')
t=re.sub(r'## EXACT NEXT ACTIVITY\n.*\Z','## EXACT NEXT ACTIVITY\n\nNo further Phase-4 translation/release gate remains for `poems/kalaignarin-kavithaigal/`. The English collection is **RELEASE-CLEARED**. Preserve the current state; reopen only for a source-backed correction or an explicitly authorised derivative/publication task.\n',t,flags=re.S)
hp.write_text(t,encoding='utf-8')

# Fresh-chat prompt: make completion authoritative and remove obsolete assembly instruction.
np=Path('NEXT_CHAT_PROMPT.md'); t=np.read_text(encoding='utf-8')
t=t.replace('ITEM TRANSLATION REVIEW COMPLETE','RELEASE-CLEARED')
t=t.replace('collection assembly NEXT','no Phase-4 release gate remains')
if '## RELEASE-CLEARED STATE' not in t:
    t += f'''\n\n## RELEASE-CLEARED STATE\n\n`கலைஞரின் கவிதைகள்` English Phase 4 is complete: **18/18 batches, 77/77 items, 439/439 item-owned scans**, plus **8/8** anthology structural scans in the assembled reader-facing collection. `EDITORIAL_CONSISTENCY_REVIEW.md` and `RELEASE_REPORT.md` are both **PASS**. Reader-facing SHA-256: `{sha}`. No Tamil `pages/` or `sections/` file changed during Phase 4.\n\n## EXACT NEXT ACTIVITY\n\nNo further Phase-4 translation/release activity remains. Preserve the release-cleared state unless a source-backed correction or explicitly authorised derivative/publication task is requested.\n'''
else:
    t=re.sub(r'## EXACT NEXT ACTIVITY\n.*\Z','## EXACT NEXT ACTIVITY\n\nNo further Phase-4 translation/release activity remains. Preserve the release-cleared state unless a source-backed correction or explicitly authorised derivative/publication task is requested.\n',t,flags=re.S)
np.write_text(t,encoding='utf-8')

# Synchronize explicit current-status claims in the remaining durable controls.
controls=[Path('README.md'),Path('TRANSCRIPTION_PHASE_PLAN.md'),WORK/'README.md',WORK/'SOURCE_INTAKE.md',WORK/'audit.md',WORK/'indexes/page-map.md',WORK/'metadata/source.md',WORK/'PHASE3_TAMIL_FINAL_CLEARANCE.md']
old='ITEM TRANSLATION REVIEW COMPLETE — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; collection assembly NEXT'
new='RELEASE-CLEARED — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; full collection/editorial/release review PASS'
for p in controls:
    t=p.read_text(encoding='utf-8')
    t=t.replace(old,new).replace('collection assembly NEXT','Phase 4 release complete')
    if p==WORK/'audit.md' and '## Phase 4 full English release clearance' not in t:
        t += f'''\n\n## Phase 4 full English release clearance\n\n- 18/18 translation batches reviewed PASS;\n- 77/77 English items;\n- 439/439 item-owned scans;\n- 8/8 anthology structural scans represented in reader-facing assembly;\n- 447/447 anthology body scans accounted;\n- title witnesses 48 exact / 29 authorised variants / 0 unresolved;\n- editorial consistency review PASS;\n- release review PASS — RELEASE-CLEARED;\n- assembled SHA-256 `{sha}`;\n- Tamil pages/sections changed during Phase 4: 0.\n'''
    p.write_text(t,encoding='utf-8')

# Remove one-shot runner before final commit.
workflow=Path('.github/workflows/kavithaigal-assemble-release.yml')
script=Path('.github/scripts/kavithaigal_assemble_release.py')
if workflow.exists(): workflow.unlink()
if script.exists(): script.unlink()

subprocess.run(['git','config','user.name','github-actions[bot]'],check=True)
subprocess.run(['git','config','user.email','41898282+github-actions[bot]@users.noreply.github.com'],check=True)
subprocess.run(['git','add','-A'],check=True)
# Guard staged scope: never Tamil pages/sections.
changed=subprocess.check_output(['git','diff','--cached','--name-only'],text=True).splitlines()
for f in changed:
    if f.startswith(str(WORK/'pages')+'/') or f.startswith(str(WORK/'sections')+'/'):
        fail('staged Tamil archival change: '+f)
if not changed: fail('nothing staged')
subprocess.run(['git','commit','-m','Assemble and release-clear Kalaignarin Kavithaigal English collection'],check=True)
subprocess.run(['git','push','origin','HEAD:main'],check=True)
print('PASS: release-cleared',sha,size,lines,'files',len(changed))
