from pathlib import Path
import re, subprocess

FILES = [
    Path('README.md'),
    Path('TRANSCRIPTION_PHASE_PLAN.md'),
    Path('NEXT_CHAT_PROMPT.md'),
    Path('poems/kalaignarin-kavithaigal/README.md'),
    Path('poems/kalaignarin-kavithaigal/SOURCE_INTAKE.md'),
    Path('poems/kalaignarin-kavithaigal/metadata/source.md'),
    Path('poems/kalaignarin-kavithaigal/indexes/page-map.md'),
]

release_status = '**RELEASE-CLEARED — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; full collection assembly, editorial consistency review and release review PASS**'

def must_replace(text, old, new, label):
    if old not in text:
        raise SystemExit(f'missing target: {label}')
    return text.replace(old, new, 1)

def replace_section(text, start, end, replacement, label):
    pat = re.compile(re.escape(start) + r'.*?(?=' + re.escape(end) + r')', re.S)
    out, n = pat.subn(replacement.rstrip() + '\n\n', text, count=1)
    if n != 1:
        raise SystemExit(f'section target count {n}: {label}')
    return out

# root README
p=Path('README.md'); t=p.read_text()
t=must_replace(t, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; item translation review COMPLETE; Phase 4 release complete**.', '- Phase 4 English translation/release: ' + release_status + '.', 'root status')
t=replace_section(t, '## Phase 4 translation progress', '## Supplied lexical controls', '''## Phase 4 translation/release result

- reviewed batches: **18/18**;
- reviewed English items: **77/77**;
- item-owned scans: **439/439**;
- structural anthology scans in reader-facing assembly: **8/8**;
- complete body accounting: **447/447 physical scans, 18–464**;
- full English collection: `poems/kalaignarin-kavithaigal/translations/en/kalaignarin-kavithaigal-en.md`;
- editorial consistency review: **PASS**;
- release report: **PASS — RELEASE-CLEARED**;
- unresolved release issues: **0**;
- Tamil `pages/` / `sections/` changes during Phase 4: **0**.''', 'root phase4')
t=replace_section(t, '## Next activity', '## Phase 4 item-translation completion', '''## Next activity

No further Phase-4 translation/release activity remains for `கலைஞரின் கவிதைகள்`. Preserve the release-cleared state unless a source-backed correction or explicitly authorised derivative/publication task is requested.''', 'root next')
t=t.replace('- next ordered activity: **full English collection assembly**, then editorial consistency review and release report.', '- release state: **full English collection assembled; editorial consistency review PASS; release report PASS — RELEASE-CLEARED**.')
p.write_text(t)

# active README
p=Path('poems/kalaignarin-kavithaigal/README.md'); t=p.read_text()
t=must_replace(t, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; item translation review COMPLETE; Phase 4 release complete**.', '- Phase 4 English translation/release: ' + release_status + '.', 'work status')
t=replace_section(t, '## Phase 4 — English translation', '## Phase 4 item-translation completion', '''## Phase 4 — English translation and release

**COMPLETE / PASS — RELEASE-CLEARED.**

- translation root: `translations/en/`;
- reviewed batches: **18/18**;
- reviewed items: **77/77**;
- item-owned source scans: **439/439**;
- structural anthology scans represented in the assembled collection: **8/8**;
- complete anthology body accounting: **447/447 scans, 18–464**;
- reader-facing collection: `translations/en/kalaignarin-kavithaigal-en.md`;
- editorial consistency review: `translations/en/EDITORIAL_CONSISTENCY_REVIEW.md` — **PASS**;
- release report: `translations/en/RELEASE_REPORT.md` — **PASS / RELEASE-CLEARED**;
- unresolved release issues: **0**;
- Tamil `pages/` / `sections/` changes during Phase 4: **0**;
- next activity: **none within Phase 4**; reopen only for a source-backed correction or explicitly authorised derivative/publication task.''', 'work phase4')
t=t.replace('- next ordered activity: **full English collection assembly**, then editorial consistency review and release report.', '- release state: **full English collection assembled; editorial consistency review PASS; release report PASS — RELEASE-CLEARED**.')
p.write_text(t)

# source intake
p=Path('poems/kalaignarin-kavithaigal/SOURCE_INTAKE.md'); t=p.read_text()
t=must_replace(t, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; item translation review COMPLETE; Phase 4 release complete**.', '- Phase 4 English translation/release: ' + release_status + '.', 'intake status')
t=replace_section(t, '## Next phase gate', '## Tamil final clearance', '''## Next phase gate

No Phase-4 gate remains. The English collection is **RELEASE-CLEARED**. Reopen only for a source-backed correction or explicitly authorised derivative/publication task.''', 'intake next gate')
t=replace_section(t, '## Phase 4 translation state', '## Phase 4 item-translation completion', '''## Phase 4 translation/release state

- reviewed batches: **18/18**;
- reviewed English items: **77/77**;
- item-owned scans: **439/439**;
- structural anthology scans in reader-facing assembly: **8/8**;
- complete body accounting: **447/447 scans, 18–464**;
- full collection assembly: **PASS**;
- editorial consistency review: **PASS**;
- release review: **PASS — RELEASE-CLEARED**;
- unresolved reviewed/release issues: **0**;
- Tamil page/canonical changes: **0**.''', 'intake phase4')
t=t.replace('- next ordered activity: **full English collection assembly**, then editorial consistency review and release report.', '- release state: **full English collection assembled; editorial consistency review PASS; release report PASS — RELEASE-CLEARED**.')
p.write_text(t)

# metadata
p=Path('poems/kalaignarin-kavithaigal/metadata/source.md'); t=p.read_text()
t=must_replace(t, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; item translation review COMPLETE; Phase 4 release complete**.', '- Phase 4 English translation/release: ' + release_status + '.', 'metadata status')
t=replace_section(t, '## Phase 4 translation metadata', '## Phase 4 item-translation completion', '''## Phase 4 translation/release metadata

- Tamil source/canonical layer remains **FINAL-CLEARED**;
- reviewed batches: **18/18**;
- reviewed English items: **77/77**;
- item-owned source scans: **439/439**;
- structural anthology scans represented in assembly: **8/8**;
- complete body accounting: **447/447 scans, 18–464**;
- assembled reader-facing collection: `../translations/en/kalaignarin-kavithaigal-en.md`;
- editorial consistency review: `../translations/en/EDITORIAL_CONSISTENCY_REVIEW.md` — **PASS**;
- release report: `../translations/en/RELEASE_REPORT.md` — **PASS / RELEASE-CLEARED**;
- unresolved release issues: **0**;
- Tamil page/canonical changes caused by Phase 4: **0**.''', 'metadata phase4')
t=t.replace('- next ordered activity: **full English collection assembly**, then editorial consistency review and release report.', '- release state: **full English collection assembled; editorial consistency review PASS; release report PASS — RELEASE-CLEARED**.')
p.write_text(t)

# page map
p=Path('poems/kalaignarin-kavithaigal/indexes/page-map.md'); t=p.read_text()
t=must_replace(t, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; item translation review COMPLETE; Phase 4 release complete**;', '- Phase 4 English translation/release: ' + release_status + ';', 'page-map status')
t=replace_section(t, '## Phase 4 translation note', '## Phase 4 item-translation completion', '''## Phase 4 translation/release note

Phase 4 is **COMPLETE / RELEASE-CLEARED**. Reviewed English covers **77/77 items and 439/439 item-owned scans**; the assembled reader-facing collection additionally accounts for all **8/8 structural anthology scans**, yielding **447/447 body scans, 18–464**. Translation/release milestones changed no scan↔page mapping and no Tamil page/canonical file. No Phase-4 gate remains.''', 'page-map phase4')
t=t.replace('- next ordered activity: **full English collection assembly**, then editorial consistency review and release report.', '- release state: **full English collection assembled; editorial consistency review PASS; release report PASS — RELEASE-CLEARED**.')
p.write_text(t)

# transcription phase plan: replace current Phase 4 block through EOF
p=Path('TRANSCRIPTION_PHASE_PLAN.md'); t=p.read_text()
idx=t.find('## Phase 4 — translation and release')
if idx < 0: raise SystemExit('phase plan Phase4 heading missing')
t=t[:idx] + '''## Phase 4 — translation and release

**COMPLETE / PASS — RELEASE-CLEARED.**

- reviewed batches: **18/18**;
- reviewed English items: **77/77**;
- reviewed item-owned source scans: **439/439**;
- structural anthology scans represented in the reader-facing assembly: **8/8**;
- complete anthology body accounting: **447/447 physical scans, 18–464**;
- reader-facing collection: `poems/kalaignarin-kavithaigal/translations/en/kalaignarin-kavithaigal-en.md`;
- editorial consistency review: **PASS**;
- final source-coverage/release review: **PASS**;
- unresolved release issues: **0**;
- Tamil `pages/` / `sections/` changes during Phase 4: **0**.

## EXACT NEXT ACTIVITY

No further Phase-4 translation/release activity remains for `கலைஞரின் கவிதைகள்`. Preserve this release-cleared state unless a source-backed correction or explicitly authorised derivative/publication task is requested.
'''
p.write_text(t)

# NEXT_CHAT_PROMPT: remove obsolete pre-release EXACT NEXT ACTIVITY, retain release-cleared final one
p=Path('NEXT_CHAT_PROMPT.md'); t=p.read_text()
old='''## EXACT NEXT ACTIVITY\n\nExecute **Phase 4 full English collection assembly** from all **77/77 batch-reviewed item translations**. Preserve source order, pure anthology structural divider/verso provenance, canonical/contents title distinctions and item boundaries. After assembly, run the deferred **editorial consistency review** and prepare the **release report**. Leave Tamil `pages/` and `sections/` unchanged unless a genuine source-backed discrepancy is independently demonstrated.\n\n\n'''
if old not in t: raise SystemExit('obsolete next-chat assembly pointer missing')
t=t.replace(old,'',1)
p.write_text(t)

# Assert intended content paths only; workflow/script removals are allowed separately.
subprocess.run(['git','config','user.name','github-actions[bot]'],check=True)
subprocess.run(['git','config','user.email','41898282+github-actions[bot]@users.noreply.github.com'],check=True)
for helper in [Path('.github/scripts/kavithaigal_release_doc_sync.py'), Path('.github/workflows/kavithaigal-release-doc-sync.yml')]:
    if helper.exists(): helper.unlink()
subprocess.run(['git','add','-A'],check=True)
changed=subprocess.check_output(['git','diff','--cached','--name-only'],text=True).splitlines()
expected=sorted(str(x) for x in FILES)
if sorted(changed) != expected:
    raise SystemExit(f'unexpected net files: {changed}; expected {expected}')
# Tamil hard guard
if any(x.startswith('poems/kalaignarin-kavithaigal/pages/') or x.startswith('poems/kalaignarin-kavithaigal/sections/') for x in changed):
    raise SystemExit('Tamil archival path entered documentation sync')
subprocess.run(['git','commit','-m','Synchronize Kalaignarin Kavithaigal release documentation'],check=True)
subprocess.run(['git','push','origin','HEAD:main'],check=True)
