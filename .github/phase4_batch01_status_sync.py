from pathlib import Path

ROOT = Path('.')
ACTIVE = Path('poems/kalaignarin-kavithaigal')

PHASE4_LINE = '**IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item-assigned scans reviewed.**'
NEXT = '**Phase 4 Batch 02 — items 2–3 (`தென்னவன் காதை`, `இந்திரஜித்`)**'


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    Path(path).write_text(text, encoding='utf-8')


def replace_any(text, olds, new):
    found = False
    for old in olds:
        if old in text:
            text = text.replace(old, new)
            found = True
    return text, found


def replace_tail(path, marker, tail):
    text = read(path)
    if marker not in text:
        raise SystemExit(f'missing tail marker {marker!r} in {path}')
    text = text.split(marker, 1)[0].rstrip() + '\n\n' + marker + '\n\n' + tail.rstrip() + '\n'
    write(path, text)

# HANDOVER
p = 'HANDOVER.md'
s = read(p)
s = s.replace('## Durable state after Phase 3 Gate 6', '## Durable state after Phase 4 Batch 01')
s, _ = replace_any(s, [
    '- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.',
    '- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**;'
], '- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item-assigned scans; Batch 02 NEXT**.')
phase4_block = '''## Phase 4 durable result — Batch 01

Translation scaffold: `poems/kalaignarin-kavithaigal/translations/en/`.

- Phase 4 status: **IN PROGRESS**;
- reviewed batches: **1**;
- reviewed English items: **1/77**;
- reviewed item-assigned source scans: **14/439**;
- Batch 01 item: **1 — `இதயத்தைத் தந்திடு அண்ணா`**;
- English title: **Give Me Your Heart, Anna**;
- source scans: **18–31**;
- reviewed English item: `translations/en/items/01-give-me-your-heart-anna-en.md`;
- Batch-01 review: `translations/en/batches/batch-01.md`;
- translation plan: `translations/en/TRANSLATION_PLAN.md`;
- English source map: `translations/en/SOURCE_MAP.md`;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes during Batch 01: **0**;
- Tamil `sections/` changes during Batch 01: **0**.

Batch 01 is intentionally a one-item batch because item 1 spans scans 18–31 and must not be split. The translation preserves the canonical/contents title distinction, Tamil three-letter wordplay through source tokens, quoted Anna rhetoric, the source-visible `அவர்` anomaly without silent Tamil repair, and the closing sea-shore elegy.
'''
if '## Phase 4 durable result — Batch 01' not in s:
    marker = '## Supplied-transcription rule'
    if marker not in s:
        raise SystemExit('HANDOVER insertion marker missing')
    s = s.replace(marker, phase4_block + '\n' + marker, 1)
write(p, s)
replace_tail(p, '## EXACT NEXT ACTIVITY', '''Execute **Phase 4 Batch 02 — items 2–3 (`தென்னவன் காதை`, `இந்திரஜித்`)**.

Read the final-cleared `sections/02.md` and `sections/03.md` completely, translate both complete items under `translations/en/items/`, review them together in `translations/en/batches/batch-02.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged. If a genuine Tamil discrepancy is exposed, reopen the Tamil source-backed layers explicitly before continuing.''')

# NEXT_CHAT_PROMPT
p = 'NEXT_CHAT_PROMPT.md'
s = read(p)
s, _ = replace_any(s, [
    '- Phase 4 English translation/release **UNBLOCKED / NOT STARTED — NEXT**;',
    '- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**;'
], '- Phase 4 English translation/release **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**;')
if '## Phase 4 Batch 01 durable result' not in s:
    insert = '''## Phase 4 Batch 01 durable result

- translation scaffold: `translations/en/`;
- Batch 01: **reviewed PASS**;
- reviewed English items: **1/77**;
- reviewed item scans: **14/439**;
- item 1: `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**;
- English item: `translations/en/items/01-give-me-your-heart-anna-en.md`;
- Batch review: `translations/en/batches/batch-01.md`;
- unresolved reviewed translation issues: **0**;
- Tamil page/canonical changes: **0**.

Follow `translations/en/TRANSLATION_PLAN.md` and `translations/en/SOURCE_MAP.md` for Phase-4 continuation.

'''
    marker = '## Locked Phase 3 structure'
    if marker not in s:
        raise SystemExit('NEXT_CHAT insertion marker missing')
    s = s.replace(marker, insert + marker, 1)
write(p, s)
replace_tail(p, '## EXACT NEXT ACTIVITY', '''Execute **Phase 4 Batch 02 — items 2–3 (`தென்னவன் காதை`, `இந்திரஜித்`)**.

1. Read final-cleared `sections/02.md` and `sections/03.md` completely.
2. Translate both complete items with stable item identity and scan provenance.
3. Review the full batch for omissions, duplication, voice, names, rhetoric and source-specific claims.
4. Create/update `translations/en/items/`, `translations/en/batches/batch-02.md` and `translations/en/SOURCE_MAP.md`.
5. Do **not** alter Tamil final-cleared `pages/` or `sections/` during translation.''')

# TRANSCRIPTION_PHASE_PLAN
p = 'TRANSCRIPTION_PHASE_PLAN.md'
s = read(p)
old = '''## Phase 4 — translation and release

**UNBLOCKED / NOT STARTED — NEXT.**

Translation and derivative/release work may now begin from the Tamil final-cleared canonical item layer, following `POEM_PROCESSING_GUIDE.md` and the repository translation policy.
'''
new = '''## Phase 4 — translation and release

**IN PROGRESS — Batch 01 reviewed PASS.**

- reviewed batches: **1**;
- reviewed English items: **1/77**;
- reviewed item-assigned source scans: **14/439**;
- Batch 01: item 1 `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**;
- translation scaffold: `poems/kalaignarin-kavithaigal/translations/en/`;
- unresolved reviewed translation issues: **0**;
- Tamil page/canonical changes during Phase 4 so far: **0**;
- Batch 02 items 2–3: **NEXT**.
'''
if old not in s:
    raise SystemExit('phase4 block missing in TRANSCRIPTION_PHASE_PLAN')
s = s.replace(old, new, 1)
write(p, s)
replace_tail(p, '## EXACT NEXT ACTIVITY', '''Execute **Phase 4 Batch 02 — items 2–3 (`தென்னவன் காதை`, `இந்திரஜித்`)** from the Tamil final-cleared canonical layer. Review both complete translations before marking the batch PASS; do not alter Tamil final-cleared files.''')

# Root README
p = 'README.md'
s = read(p)
s, _ = replace_any(s, ['- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.'], '- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**.')
if 'Batch 01 begins Phase 4' not in s:
    marker = '## Supplied lexical controls'
    block = '''## Phase 4 translation progress

Batch 01 begins Phase 4 with item 1 `இதயத்தைத் தந்திடு அண்ணா` translated as **Give Me Your Heart, Anna**. The reviewed English layer now covers **1/77 items** and **14/439 item-assigned source scans** with **0** unresolved reviewed translation issues. Files live under `poems/kalaignarin-kavithaigal/translations/en/`. No Tamil page or canonical item has been changed by translation work.

'''
    if marker not in s:
        raise SystemExit('root README marker missing')
    s = s.replace(marker, block + marker, 1)
write(p, s)
replace_tail(p, '## Next activity', '''**Phase 4 Batch 02 — items 2–3 (`தென்னவன் காதை`, `இந்திரஜித்`)**. Translate and review both complete final-cleared items; leave Tamil archival files unchanged.''')

# Active README
p = ACTIVE / 'README.md'
s = read(p)
s, _ = replace_any(s, ['- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.'], '- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**.')
if '## Phase 4 — English translation' not in s:
    marker = '## Next activity'
    block = '''## Phase 4 — English translation

**IN PROGRESS — Batch 01 reviewed PASS.**

- translation root: `translations/en/`;
- reviewed batches: **1**;
- reviewed items: **1/77**;
- reviewed item-assigned scans: **14/439**;
- item 1 `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` / `sections/` changes: **0**.

'''
    if marker not in s:
        raise SystemExit('active README marker missing')
    s = s.replace(marker, block + marker, 1)
write(p, s)
replace_tail(p, '## Next activity', '''**Phase 4 Batch 02 — items 2–3 (`தென்னவன் காதை`, `இந்திரஜித்`)**. Translate both complete final-cleared canonical items and review the batch before advancing.''')

# SOURCE_INTAKE
p = ACTIVE / 'SOURCE_INTAKE.md'
s = read(p)
s, _ = replace_any(s, ['- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.'], '- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**.')
s = s.replace('**Phase 4 — English translation and release workflow.** Translation remains deferred.', '**Phase 4 — English translation and release workflow is IN PROGRESS.** Batch 01 is reviewed PASS; Batch 02 items 2–3 are next.')
if '## Phase 4 translation state' not in s:
    s += '''\n## Phase 4 translation state\n\n- Batch 01: **reviewed PASS**;\n- reviewed items: **1/77**;\n- reviewed item scans: **14/439**;\n- English item 1: `translations/en/items/01-give-me-your-heart-anna-en.md`;\n- Tamil page/canonical changes: **0**;\n- exact next: **Batch 02 items 2–3**.\n'''
write(p, s)

# metadata/source.md
p = ACTIVE / 'metadata/source.md'
s = read(p)
s, _ = replace_any(s, ['- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.'], '- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**.')
if '## Phase 4 translation metadata' not in s:
    s += '''\n## Phase 4 translation metadata\n\n- Tamil source/canonical layer remains **FINAL-CLEARED**;\n- reviewed batches: **1**;\n- reviewed English items: **1/77**;\n- reviewed item scans: **14/439**;\n- Batch 01 English item: `../translations/en/items/01-give-me-your-heart-anna-en.md`;\n- Tamil page/canonical changes caused by translation: **0**;\n- next translation batch: **items 2–3**.\n'''
write(p, s)

# indexes/page-map.md — status only, no pagination changes
p = ACTIVE / 'indexes/page-map.md'
s = read(p)
s, _ = replace_any(s, [
    '- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**;',
    '- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.'
], '- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**;')
if 'Phase 4 Batch 01 reviewed' not in s:
    s += '''\n## Phase 4 translation note\n\nPhase 4 Batch 01 reviewed item 1 across scans **18–31** (**14/439** item-assigned scans). This translation milestone changes no scan↔page mapping and no Tamil page/canonical file.\n'''
write(p, s)

# audit.md
p = ACTIVE / 'audit.md'
s = read(p)
if '## Phase 4 Batch 01 audit' not in s:
    s += '''\n## Phase 4 Batch 01 audit — REVIEWED / PASS\n\nScope: English translation/review of final-cleared canonical item **1** only.\n\n- item: `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**;\n- reviewed items: **1/77**;\n- reviewed item-owned scans: **14/439 — scans 18–31**;\n- source-facing poem/context scans: **12/12 — scans 20–31**;\n- structural title/marker-only scans represented: **2/2 — scans 18–19**;\n- canonical/contents title witnesses preserved separately: **PASS**;\n- omission/duplication issues: **0**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page-record changes: **0**;\n- Tamil canonical-item changes: **0**;\n- batch evidence: `translations/en/batches/batch-01.md`;\n- English item: `translations/en/items/01-give-me-your-heart-anna-en.md`.\n\n### Exact next Phase-4 activity\n\n**Batch 02 — items 2–3 (`தென்னவன் காதை`, `இந்திரஜித்`)**.\n'''
write(p, s)

# Phase-3 final-clearance record gets a non-destructive subsequent-status note.
p = ACTIVE / 'PHASE3_TAMIL_FINAL_CLEARANCE.md'
s = read(p)
if '## Subsequent Phase 4 status' not in s:
    s += '''\n## Subsequent Phase 4 status\n\nPhase 4 has subsequently started. **Batch 01 is reviewed PASS** for item 1 `இதயத்தைத் தந்திடு அண்ணா` (**Give Me Your Heart, Anna**), covering **14/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remained unchanged. Exact next translation activity: **Batch 02 items 2–3**.\n'''
write(p, s)

print('Phase 4 Batch 01 status synchronization complete')
