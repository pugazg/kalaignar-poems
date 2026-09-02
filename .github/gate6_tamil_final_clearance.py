from pathlib import Path
import re

ROOT = Path('poems/kalaignarin-kavithaigal')
CHECKPOINT = '2d91080503f0f2d2fc7b47e864494b329557b320'

# Preconditions
for rel in [
    'PHASE3_STRUCTURE_AUDIT.md',
    'PHASE3_BOUNDARY_JOIN_AUDIT.md',
    'PHASE3_TITLE_WITNESS_RECONCILIATION.md',
    'PHASE3_CANONICAL_ASSEMBLY.md',
    'PHASE3_CANONICAL_SOURCE_REVIEW.md',
]:
    if not (ROOT / rel).exists():
        raise SystemExit(f'missing prerequisite: {rel}')

review = (ROOT / 'PHASE3_CANONICAL_SOURCE_REVIEW.md').read_text(encoding='utf-8')
for needle in [
    '**COMPLETE — PASS.**',
    'canonical item files: **77/77 — PASS**',
    'verified body scan accounting: **447/447 — PASS**',
    'unresolved source-completeness defects: **0**',
    'verified `pages/NNNN.md` records modified during Gate 5: **0**',
    'canonical `sections/NN.md` files modified during Gate 5: **0**',
]:
    if needle not in review:
        raise SystemExit(f'Gate 5 prerequisite missing: {needle}')

sections = sorted((ROOT / 'sections').glob('[0-9][0-9].md'))
expected_sections = [ROOT / 'sections' / f'{i:02d}.md' for i in range(1, 78)]
if sections != expected_sections:
    raise SystemExit('canonical inventory is not exactly sections/01.md..77.md')
if (ROOT / 'sections' / 'kalaignarin-kavithaigal.md').exists():
    raise SystemExit('obsolete monolithic canonical file exists')

pages = sorted((ROOT / 'pages').glob('[0-9][0-9][0-9][0-9].md'))
if len(pages) != 465:
    raise SystemExit(f'expected 465 page records, found {len(pages)}')
for p in pages:
    text = p.read_text(encoding='utf-8')
    if not re.search(r'^status:\s*["\']?verified["\']?\s*$', text, re.M):
        raise SystemExit(f'non-verified page at final clearance: {p}')

# Create Gate 6 record.
clearance = f'''# Phase 3 Tamil Final Clearance — கலைஞரின் கவிதைகள்

## Status

**PHASE 3 COMPLETE — TAMIL FINAL CLEARANCE: PASS.**

The Tamil source/canonical layer for `கலைஞரின் கவிதைகள்` is formally cleared for Phase 4.

This clearance introduces no new transcription, normalization, correction, translation or editorial rewriting. It confirms that the ordered Phase-3 gates have all passed against the already verified source layer and that no unresolved Tamil source/completeness defect remains.

Clearance checkpoint before this record was written: live `main` commit `{CHECKPOINT}`.

## Gate confirmation

### Gate 1 — physical scan ↔ printed-page reconciliation

**PASS.**

- controlling source: **465 physical scans**;
- physical source accounting: **465/465**;
- scan 1: front cover;
- scans 2–17: logical Roman I–XVI;
- scans 18–464: logical Arabic 1–447 (`scan_page - 17`);
- scan 465: back cover;
- `printed_page` remains source-visible only.

Governing records: `PHASE3_STRUCTURE_AUDIT.md` and `indexes/page-map.md`.

### Gate 2 — boundary / page-join audit

**PASS.**

- adjacent physical joins certified: **464/464**;
- missing/duplicated physical pages: **0**;
- unresolved structural joins: **0**;
- intentional source ordering preserved, including **236→237→238→239** and **370→371→372→373→374**.

Governing record: `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

### Gate 3 — title-witness reconciliation

**PASS.**

- title/group witnesses: **81**;
- exact witnesses: **51**;
- source-valid variants: **30**;
- unresolved witnesses: **0**;
- hybrid/normalized canonical titles: **0**.

Dedicated divider/title/opening witnesses remain canonical title authority; contents witnesses remain separately preserved.

Governing record: `PHASE3_TITLE_WITNESS_RECONCILIATION.md`.

### Gate 4 — canonical Tamil assembly

**PASS.**

- canonical item files: **77/77** (`sections/01.md` through `sections/77.md`);
- verified body interval: scans **18–464 = 447/447**;
- item-assigned canonical scans: **439/439**;
- separate anthology group-divider/verso scans: **8/8**;
- canonical provenance markers: **439/439**;
- canonical item-manifest SHA-256: `74f7bbd84edb1d13dec6d775f854a793929ef530b0c78897cc205004ba78972f`;
- verified page records modified by assembly: **0**.

Governing records: `PHASE3_CANONICAL_ASSEMBLY.md` and `indexes/canonical-source-map.md`.

### Gate 5 — assembly/source-completeness review

**PASS.**

- canonical inventory: **77/77 PASS**;
- verified body scan accounting: **447/447 PASS**;
- canonical payload equality against verified page layer: **77/77 PASS**;
- item title witnesses: **48 exact / 29 variants**;
- pure group title witnesses: **3 exact / 1 variant**;
- dropped/duplicated/reordered/cross-item source passages: **0**;
- silent lexical normalization detected: **0**;
- unresolved source-completeness defects: **0**;
- page-record or canonical-item corrections required by Gate 5: **0**.

Governing record: `PHASE3_CANONICAL_SOURCE_REVIEW.md`.

## Tamil final-clearance judgement

All required Phase-3 gates are complete and PASS.

Therefore:

- Phase 1 transcription: **COMPLETE — 465/465**;
- Phase 2 source-critical visual verification: **COMPLETE — 465/465 verified**;
- Phase 3 Gate 1: **COMPLETE / PASS**;
- Phase 3 Gate 2: **COMPLETE / PASS**;
- Phase 3 Gate 3: **COMPLETE / PASS**;
- Phase 3 Gate 4: **COMPLETE / PASS — 77/77 canonical items**;
- Phase 3 Gate 5: **COMPLETE / PASS**;
- **Tamil final clearance: PASS**;
- unresolved Tamil source issues: **none recorded**;
- Tamil source/canonical layer: **FINAL-CLEARED**.

The controlling scan remains the highest textual authority. Final clearance does not prevent a future source-backed correction if a genuine discrepancy is later demonstrated; such a correction must reopen the affected page/audit/canonical layers rather than silently changing only a derivative file.

## Phase transition

**Phase 4 is now unblocked.**

No English translation was created or modified as part of this Gate-6 clearance activity.

## Exact next activity

Begin **Phase 4 — English translation and release workflow**, following `POEM_PROCESSING_GUIDE.md` and the repository translation policy, using only the Tamil final-cleared canonical item layer as the translation source.
'''
(ROOT / 'PHASE3_TAMIL_FINAL_CLEARANCE.md').write_text(clearance, encoding='utf-8')


def replace_once(path, old, new):
    p = Path(path)
    s = p.read_text(encoding='utf-8')
    if old not in s:
        raise SystemExit(f'replacement target not found in {path}: {old[:80]!r}')
    p.write_text(s.replace(old, new, 1), encoding='utf-8')

# HANDOVER
replace_once('HANDOVER.md', '## Durable state after Phase 3 Gate 5', '## Durable state after Phase 3 Gate 6')
replace_once('HANDOVER.md', '- Phase 3 Gate 6 — Tamil final clearance: **NOT STARTED — NEXT**;\n- translation: **NOT STARTED**.', '- Phase 3 Gate 6 — Tamil final clearance: **COMPLETE / PASS**;\n- Tamil source/canonical layer: **FINAL-CLEARED**;\n- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.')
replace_once('HANDOVER.md', '## Supplied-transcription rule', '''## Gate 6 durable result

Gate-6 evidence: `poems/kalaignarin-kavithaigal/PHASE3_TAMIL_FINAL_CLEARANCE.md`.

- Gates 1–5: **all COMPLETE / PASS**;
- Tamil final clearance: **PASS**;
- Tamil source/canonical layer: **FINAL-CLEARED**;
- unresolved Tamil source/completeness defects: **0**;
- canonical inventory at clearance: **77/77**;
- verified page records changed during Gate 6: **0**;
- canonical item files changed during Gate 6: **0**;
- English translation created/modified during Gate 6: **no**;
- Phase 4: **UNBLOCKED**.

The controlling scan remains highest textual authority. Any later genuine source-backed discrepancy must reopen the affected source/page/audit/canonical layers.

## Supplied-transcription rule''')
replace_once('HANDOVER.md', '16. `PHASE3_CANONICAL_SOURCE_REVIEW.md`;\n17. canonical item files `sections/01.md` through `sections/77.md` as needed for Gate-6 final-clearance confirmation.', '16. `PHASE3_CANONICAL_SOURCE_REVIEW.md`;\n17. `PHASE3_TAMIL_FINAL_CLEARANCE.md`;\n18. canonical item files `sections/01.md` through `sections/77.md` as needed for Phase-4 translation.')
idx = Path('HANDOVER.md').read_text(encoding='utf-8').index('## EXACT NEXT ACTIVITY')
s = Path('HANDOVER.md').read_text(encoding='utf-8')[:idx] + '''## EXACT NEXT ACTIVITY

Begin **Phase 4 — English translation and release workflow** from the Tamil final-cleared canonical item layer.

Follow `POEM_PROCESSING_GUIDE.md` and the repository translation policy. Do not alter Tamil source/page/canonical text as part of translation work; if a genuine Tamil source discrepancy is discovered, reopen the affected Tamil layers explicitly before continuing.
'''
Path('HANDOVER.md').write_text(s, encoding='utf-8')

# NEXT CHAT PROMPT
replace_once('NEXT_CHAT_PROMPT.md', '- Phase 3 Gate 6 Tamil final clearance **NEXT / NOT STARTED**;\n- translation **NOT STARTED**.', '- Phase 3 Gate 6 Tamil final clearance **COMPLETE / PASS**;\n- Tamil source/canonical layer **FINAL-CLEARED**;\n- Phase 4 English translation/release **UNBLOCKED / NOT STARTED — NEXT**.')
replace_once('NEXT_CHAT_PROMPT.md', '## Locked Phase 3 structure', '''## Gate 6 durable result

Evidence: `PHASE3_TAMIL_FINAL_CLEARANCE.md`.

- Gates 1–5 **all COMPLETE / PASS**;
- Tamil final clearance **PASS**;
- Tamil source/canonical layer **FINAL-CLEARED**;
- unresolved Tamil source/completeness defects **0**;
- canonical inventory **77/77**;
- page-record changes during Gate 6 **0**;
- canonical-item changes during Gate 6 **0**;
- English translation created/modified during Gate 6 **no**;
- Phase 4 **UNBLOCKED**.

## Locked Phase 3 structure''')
idx = Path('NEXT_CHAT_PROMPT.md').read_text(encoding='utf-8').index('## EXACT NEXT ACTIVITY')
s = Path('NEXT_CHAT_PROMPT.md').read_text(encoding='utf-8')[:idx] + '''## EXACT NEXT ACTIVITY

Begin **Phase 4 — English translation and release workflow**.

1. Treat `PHASE3_TAMIL_FINAL_CLEARANCE.md` and the final-cleared `sections/01.md` through `sections/77.md` as the Tamil translation source layer.
2. Follow `POEM_PROCESSING_GUIDE.md` and the repository translation policy.
3. Preserve source-item identity and provenance in translation mapping.
4. Do not silently edit Tamil final-cleared files during translation.
5. If a genuine Tamil discrepancy is found, reopen the affected Tamil source/page/audit/canonical layers before continuing.
'''
Path('NEXT_CHAT_PROMPT.md').write_text(s, encoding='utf-8')

# Phase plan
replace_once('TRANSCRIPTION_PHASE_PLAN.md', '6. **Tamil final clearance — NEXT / NOT STARTED.**', '6. **Tamil final clearance — COMPLETE / PASS.**\n   - Tamil source/canonical layer: **FINAL-CLEARED**;\n   - unresolved Tamil source/completeness defects: **0**;\n   - evidence: `poems/kalaignarin-kavithaigal/PHASE3_TAMIL_FINAL_CLEARANCE.md`.')
idx = Path('TRANSCRIPTION_PHASE_PLAN.md').read_text(encoding='utf-8').index('## EXACT NEXT ACTIVITY')
s = Path('TRANSCRIPTION_PHASE_PLAN.md').read_text(encoding='utf-8')[:idx] + '''## Phase 4 — translation and release

**UNBLOCKED / NOT STARTED — NEXT.**

Translation and derivative/release work may now begin from the Tamil final-cleared canonical item layer, following `POEM_PROCESSING_GUIDE.md` and the repository translation policy.

## EXACT NEXT ACTIVITY

Begin **Phase 4 — English translation and release workflow** from `poems/kalaignarin-kavithaigal/sections/01.md` through `sections/77.md`.
'''
Path('TRANSCRIPTION_PHASE_PLAN.md').write_text(s, encoding='utf-8')

# Root README
replace_once('README.md', '- Phase 3 Gate 6 Tamil final clearance: **NEXT / NOT STARTED**;\n- translation: **NOT STARTED**.', '- Phase 3 Gate 6 Tamil final clearance: **COMPLETE / PASS**;\n- Tamil source/canonical layer: **FINAL-CLEARED**;\n- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.')
replace_once('README.md', '## Supplied lexical controls', '''Gate 6 formally confirms Gates 1–5 are all PASS and records the Tamil source/canonical layer as **FINAL-CLEARED**. Evidence: `poems/kalaignarin-kavithaigal/PHASE3_TAMIL_FINAL_CLEARANCE.md`. No Tamil page/canonical file or English translation was changed by the clearance activity.

## Supplied lexical controls''')
idx = Path('README.md').read_text(encoding='utf-8').index('## Next activity')
s = Path('README.md').read_text(encoding='utf-8')[:idx] + '''## Next activity

**Phase 4 — English translation and release workflow.** Translate only from the Tamil final-cleared canonical item layer and follow the repository translation policy.
'''
Path('README.md').write_text(s, encoding='utf-8')

# Active README
replace_once(ROOT / 'README.md', '- Phase 3 Gate 6 Tamil final clearance: **NEXT / NOT STARTED**;\n- translation: **NOT STARTED**.', '- Phase 3 Gate 6 Tamil final clearance: **COMPLETE / PASS**;\n- Tamil source/canonical layer: **FINAL-CLEARED**;\n- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.')
replace_once(ROOT / 'README.md', '## Next activity', '''## Gate 6 — Tamil final clearance

**COMPLETE / PASS — Tamil source/canonical layer FINAL-CLEARED.** Evidence: `PHASE3_TAMIL_FINAL_CLEARANCE.md`.

No page record, canonical item or English translation was changed during Gate 6. Phase 4 is now unblocked.

## Next activity''')
idx = (ROOT / 'README.md').read_text(encoding='utf-8').index('## Next activity')
s = (ROOT / 'README.md').read_text(encoding='utf-8')[:idx] + '''## Next activity

**Phase 4 — English translation and release workflow.** Use only the Tamil final-cleared `sections/01.md` through `sections/77.md` as the translation source layer.
'''
(ROOT / 'README.md').write_text(s, encoding='utf-8')

# SOURCE_INTAKE / metadata / page-map: status transition + clearance evidence.
for path in [ROOT / 'SOURCE_INTAKE.md', ROOT / 'metadata/source.md']:
    text = path.read_text(encoding='utf-8')
    text = text.replace('- Phase 3 Gate 6 Tamil final clearance: **NEXT / NOT STARTED**;\n- translation: **NOT STARTED**.', '- Phase 3 Gate 6 Tamil final clearance: **COMPLETE / PASS**;\n- Tamil source/canonical layer: **FINAL-CLEARED**;\n- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.')
    text = text.replace('**Phase 3 Gate 6 — Tamil final clearance only.**', '**Phase 4 — English translation and release workflow.**')
    if 'PHASE3_TAMIL_FINAL_CLEARANCE.md' not in text:
        text += '\n## Tamil final clearance\n\n**PASS — FINAL-CLEARED.** Evidence: `PHASE3_TAMIL_FINAL_CLEARANCE.md`. Gates 1–5 remain PASS; unresolved Tamil source/completeness defects are **0**; Gate 6 changed **0** page records, **0** canonical items and **0** English translations. Phase 4 is unblocked.\n'
    path.write_text(text, encoding='utf-8')

# page-map
p = ROOT / 'indexes/page-map.md'
text = p.read_text(encoding='utf-8')
text = text.replace('- Gate 5 assembly/source-completeness review: **COMPLETE / PASS**;\n- Gate 6 Tamil final clearance: **NEXT / NOT STARTED**;\n- translation: **NOT STARTED**.', '- Gate 5 assembly/source-completeness review: **COMPLETE / PASS**;\n- Gate 6 Tamil final clearance: **COMPLETE / PASS**;\n- Tamil source/canonical layer: **FINAL-CLEARED**;\n- Phase 4 English translation/release: **UNBLOCKED / NOT STARTED — NEXT**.')
if '## Phase 3 Gate 6 — Tamil final clearance COMPLETE / PASS' not in text:
    text += '\n## Phase 3 Gate 6 — Tamil final clearance COMPLETE / PASS\n\nEvidence: `../PHASE3_TAMIL_FINAL_CLEARANCE.md`. All Gates 1–5 remain PASS; unresolved Tamil source/completeness defects are **0**; canonical inventory remains **77/77**; page/canonical changes during clearance are **0**. Tamil source/canonical layer is **FINAL-CLEARED** and Phase 4 is unblocked.\n'
p.write_text(text, encoding='utf-8')

# audit
p = ROOT / 'audit.md'
text = p.read_text(encoding='utf-8')
if '## Phase 3 Gate 6 audit — COMPLETE / PASS' not in text:
    text += '''\n## Phase 3 Gate 6 audit — COMPLETE / PASS

Scope: **Tamil final clearance only**.

- Gates 1–5: **all COMPLETE / PASS**;
- canonical inventory at clearance: **77/77**;
- unresolved Tamil source/completeness defects: **0**;
- verified page records changed during Gate 6: **0**;
- canonical item files changed during Gate 6: **0**;
- English translation created/modified during Gate 6: **0**;
- Tamil source/canonical layer: **FINAL-CLEARED**;
- Phase 4: **UNBLOCKED**.

Evidence: `PHASE3_TAMIL_FINAL_CLEARANCE.md`.

## Next phase

**Phase 4 — English translation and release workflow.** Use only the Tamil final-cleared canonical item layer as translation source.
'''
p.write_text(text, encoding='utf-8')

# Gate 5 record: append subsequent Gate 6 outcome for durable transition.
p = ROOT / 'PHASE3_CANONICAL_SOURCE_REVIEW.md'
text = p.read_text(encoding='utf-8')
if '## Subsequent Gate 6 outcome' not in text:
    text += '\n## Subsequent Gate 6 outcome\n\nPhase 3 Gate 6 subsequently completed **PASS — TAMIL FINAL CLEARANCE**. The Tamil source/canonical layer is **FINAL-CLEARED** for Phase 4. Gate 6 changed no page records or canonical item files and created no English translation. Final-clearance record: `PHASE3_TAMIL_FINAL_CLEARANCE.md`.\n'
p.write_text(text, encoding='utf-8')

print('Gate 6 prepared: Tamil final clearance PASS; 77 canonical items; 465 verified pages; Phase 4 unblocked')
