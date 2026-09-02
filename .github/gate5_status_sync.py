from pathlib import Path
import re

ROOT = Path('.')
BASE = Path('poems/kalaignarin-kavithaigal')


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    Path(path).write_text(text.rstrip() + '\n', encoding='utf-8')


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly one occurrence, found {count}')
    return text.replace(old, new, 1)


def sub_once(text, pattern, repl, label):
    new, count = re.subn(pattern, repl, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f'{label}: regex replacement count {count}')
    return new


# Root README
p = Path('README.md')
t = read(p)
t = replace_once(t,
    '- Phase 3 Gate 5 assembly/source-completeness review: **NEXT / NOT STARTED**;',
    '- Phase 3 Gate 5 assembly/source-completeness review: **COMPLETE / PASS**;', 'root gate5 status')
t = replace_once(t,
    '- Tamil final clearance and translation: **NOT STARTED**.',
    '- Phase 3 Gate 6 Tamil final clearance: **NEXT / NOT STARTED**;\n- translation: **NOT STARTED**.', 'root gate6 status')
insert = '''Gate 5 independently re-derived the 77-item sequence from the verified page-layer section witnesses and compared every canonical item payload against the verified source-facing page text. Result: **77/77 canonical items PASS**, **447/447 body scans accounted**, **439/439 item scans**, **8/8 structural group scans**, **0 silent-normalization/source-completeness defects**, and **0 page-record/canonical-item changes**. Evidence: `poems/kalaignarin-kavithaigal/PHASE3_CANONICAL_SOURCE_REVIEW.md`.

'''
t = replace_once(t, '## Supplied lexical controls\n', insert + '## Supplied lexical controls\n', 'root gate5 insertion')
t = sub_once(t, r'## Next activity\n\n.*\Z', '''## Next activity

**Phase 3 Gate 6 — Tamil final clearance only.** Formally confirm Gates 1–5 are PASS and decide whether the Tamil source/canonical layer can be marked final-cleared for Phase 4. Do not begin English translation in the same activity.''', 'root next')
write(p, t)

# Active README
p = BASE / 'README.md'
t = read(p)
t = replace_once(t,
    '- Phase 3 Gate 5 assembly/source-completeness review: **NEXT / NOT STARTED**;',
    '- Phase 3 Gate 5 assembly/source-completeness review: **COMPLETE / PASS**;', 'active gate5 status')
t = replace_once(t,
    '- Tamil final clearance / translation: **NOT STARTED**.',
    '- Phase 3 Gate 6 Tamil final clearance: **NEXT / NOT STARTED**;\n- translation: **NOT STARTED**.', 'active gate6 status')
gate5_section = '''## Gate 5 — assembly/source-completeness review

**COMPLETE / PASS.** Evidence: `PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical item inventory: **77/77 PASS**;
- verified body scan accounting: **447/447 PASS**;
- item-assigned source scans: **439/439 PASS**;
- structural group scans: **8/8 PASS**;
- canonical payload equality against the verified page layer: **77/77 PASS**;
- item title witnesses: **48 exact / 29 authorized variants**;
- pure group title witnesses: **3 exact / 1 authorized variant**;
- unresolved source-completeness defects: **0**;
- verified page records modified during Gate 5: **0**;
- canonical item files modified during Gate 5: **0**.

'''
t = replace_once(t, '## Next activity\n', gate5_section + '## Next activity\n', 'active gate5 insertion')
t = sub_once(t, r'## Next activity\n\n.*\Z', '''## Next activity

**Phase 3 Gate 6 — Tamil final clearance only.** Confirm Gates 1–5 are PASS and decide whether the Tamil source/canonical layer can be final-cleared for Phase 4. Do not begin English translation in the same activity.''', 'active next')
write(p, t)

# Phase plan
p = Path('TRANSCRIPTION_PHASE_PLAN.md')
t = read(p)
t = replace_once(t,
    '5. **Assembly/source-completeness review — NEXT / NOT STARTED.**',
    '5. **Assembly/source-completeness review — COMPLETE / PASS.**\n   - canonical items: **77/77 PASS**;\n   - verified body accounting: **447/447 PASS**;\n   - canonical payload equality: **77/77 PASS**;\n   - title witnesses: **48 exact + 29 variants across items; 3 exact + 1 variant across pure groups**;\n   - unresolved source-completeness defects: **0**;\n   - page-record/canonical-item changes during review: **0**;\n   - evidence: `poems/kalaignarin-kavithaigal/PHASE3_CANONICAL_SOURCE_REVIEW.md`.', 'phase gate5')
t = replace_once(t,
    '6. **Tamil final clearance — NOT STARTED.**',
    '6. **Tamil final clearance — NEXT / NOT STARTED.**', 'phase gate6')
t = sub_once(t, r'## EXACT NEXT ACTIVITY\n\n.*\Z', '''## EXACT NEXT ACTIVITY

Execute **Phase 3 Gate 6 — Tamil final clearance only**. Formally confirm that Gates 1–5 remain PASS and decide whether the Tamil source/canonical layer can be marked final-cleared for Phase 4.

Do **not** begin English translation in the same activity.''', 'phase next')
write(p, t)

# Handover
p = Path('HANDOVER.md')
t = read(p)
t = replace_once(t, '## Durable state after Phase 3 Gate 4', '## Durable state after Phase 3 Gate 5', 'handover heading')
t = replace_once(t,
    '- Phase 3 Gate 5 — assembly/source-completeness review: **NOT STARTED — NEXT**;',
    '- Phase 3 Gate 5 — assembly/source-completeness review: **COMPLETE / PASS**;', 'handover gate5')
t = replace_once(t,
    '- Tamil final clearance: **NOT STARTED**;',
    '- Phase 3 Gate 6 — Tamil final clearance: **NOT STARTED — NEXT**;', 'handover gate6')
gate5_handover = '''## Gate 5 durable result

Gate-5 evidence: `poems/kalaignarin-kavithaigal/PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical item inventory: **77/77 PASS**;
- verified body scan accounting: **447/447 PASS**;
- canonical item scan coverage: **439/439 PASS**;
- structural group scans: **8/8 PASS**;
- canonical payload equality against the verified page layer: **77/77 PASS**;
- Gate-3 item title decisions preserved: **48 exact / 29 variants**;
- pure group title decisions preserved: **3 exact / 1 variant**;
- unresolved source-completeness defects: **0**;
- verified `pages/NNNN.md` records changed during Gate 5: **0**;
- canonical `sections/NN.md` files changed during Gate 5: **0**;
- Tamil final clearance granted: **no**;
- translation started: **no**.

The review independently reconstructed every canonical item's source-facing payload from the verified page layer and found no dropped, duplicated, reordered, cross-item or silently normalized source passage. The 236→237→238→239 interposition and 370→371→372→373→374 divider sequence remain explicitly preserved.

'''
t = replace_once(t, '## Supplied-transcription rule\n', gate5_handover + '## Supplied-transcription rule\n', 'handover gate5 insertion')
t = replace_once(t,
    '16. canonical item files `sections/01.md` through `sections/77.md` as needed for Gate-5 review.',
    '16. `PHASE3_CANONICAL_SOURCE_REVIEW.md`;\n17. canonical item files `sections/01.md` through `sections/77.md` as needed for Gate-6 final-clearance confirmation.', 'handover startup')
t = sub_once(t, r'## EXACT NEXT ACTIVITY\n\n.*\Z', '''## EXACT NEXT ACTIVITY

Execute **Phase 3 Gate 6 — Tamil final clearance only**.

Formally confirm that Phase 3 Gates 1–5 are all PASS, confirm there are no unresolved Tamil source/completeness defects, and decide whether to mark the Tamil source/canonical layer final-cleared for Phase 4.

Do **not** begin English translation in the same activity.''', 'handover next')
write(p, t)

# Next chat prompt
p = Path('NEXT_CHAT_PROMPT.md')
t = read(p)
t = replace_once(t,
    '`PHASE3_CANONICAL_ASSEMBLY.md`, `indexes/canonical-source-map.md`, and the Gate-4 canonical output as needed.',
    '`PHASE3_CANONICAL_ASSEMBLY.md`, `PHASE3_CANONICAL_SOURCE_REVIEW.md`, `indexes/canonical-source-map.md`, and canonical item files as needed.', 'prompt startup')
t = replace_once(t,
    '- Phase 3 Gate 5 assembly/source-completeness review **NEXT / NOT STARTED**;',
    '- Phase 3 Gate 5 assembly/source-completeness review **COMPLETE / PASS**;', 'prompt gate5')
t = replace_once(t,
    '- Tamil final clearance / translation **NOT STARTED**.',
    '- Phase 3 Gate 6 Tamil final clearance **NEXT / NOT STARTED**;\n- translation **NOT STARTED**.', 'prompt gate6')
gate5_prompt = '''## Gate 5 durable result

Evidence: `PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical items **77/77 PASS**;
- verified body scan accounting **447/447 PASS**;
- item scans **439/439 PASS**;
- structural group scans **8/8 PASS**;
- canonical payload equality against verified page records **77/77 PASS**;
- item title witnesses **48 exact / 29 variants**;
- pure group title witnesses **3 exact / 1 variant**;
- unresolved source-completeness defects **0**;
- page-record changes during Gate 5 **0**;
- canonical-item changes during Gate 5 **0**;
- Tamil final clearance and translation were **not** started.

'''
t = replace_once(t, '## Locked Phase 3 structure\n', gate5_prompt + '## Locked Phase 3 structure\n', 'prompt gate5 insertion')
t = sub_once(t, r'## EXACT NEXT ACTIVITY\n\n.*\Z', '''## EXACT NEXT ACTIVITY

Execute **Phase 3 Gate 6 — Tamil final clearance only**.

1. Confirm Gates 1–5 are all durably PASS.
2. Confirm there are no unresolved Tamil source/completeness defects.
3. Confirm the final canonical inventory remains `sections/01.md` through `sections/77.md` with the Gate-5 review unchanged.
4. If all controls pass, create the durable Tamil-final-clearance record and synchronize status documents.
5. Do **not** begin English translation in the same activity.''', 'prompt next')
write(p, t)

# Audit
p = BASE / 'audit.md'
t = read(p)
gate5_audit = '''## Phase 3 Gate 5 audit — COMPLETE / PASS

Scope: **canonical assembly/source-completeness review only**. Evidence: `PHASE3_CANONICAL_SOURCE_REVIEW.md`.

### Review accounting

- canonical item inventory: **77/77 PASS**;
- verified body interval accounting: **447/447 PASS**;
- item-assigned source scans: **439/439 PASS**;
- pure structural group scans: **8/8 PASS**;
- item-file scan markers: **439/439 PASS**;
- canonical metadata records: **77/77 PASS**;
- canonical payload equality against verified page records: **77/77 PASS**;
- item title witnesses: **48 exact / 29 authorized variants**;
- pure group title witnesses: **3 exact / 1 authorized variant**;
- unresolved source-completeness defects: **0**;
- dropped/duplicated/reordered/cross-item source passages: **0**;
- silent lexical normalization detected: **0**;
- verified page records modified during Gate 5: **0**;
- canonical item files modified during Gate 5: **0**.

### Gate result

**Gate 5 PASS.** Tamil final clearance was not granted and translation was not started during this review.

## Next audit gate

**Phase 3 Gate 6 — Tamil final clearance only.** Confirm Gates 1–5 remain PASS and decide whether the Tamil source/canonical layer can be marked final-cleared for Phase 4. Do not begin English translation in the same activity.'''
t = sub_once(t, r'## Next audit gate\n\n.*\Z', gate5_audit, 'audit next')
write(p, t)

# Source intake
p = BASE / 'SOURCE_INTAKE.md'
t = read(p)
t = replace_once(t,
    '- Phase 3 Gate 5 assembly/source-completeness review: **NEXT / NOT STARTED**;',
    '- Phase 3 Gate 5 assembly/source-completeness review: **COMPLETE / PASS**;', 'intake gate5')
t = replace_once(t,
    '- Tamil final clearance / translation: **NOT STARTED**.',
    '- Phase 3 Gate 6 Tamil final clearance: **NEXT / NOT STARTED**;\n- translation: **NOT STARTED**.', 'intake gate6')
t = sub_once(t, r'## Next phase gate\n\n.*\Z', '''## Gate 5 review result

Evidence: `PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical items **77/77 PASS**;
- body scan accounting **447/447 PASS**;
- item scans **439/439 PASS**;
- structural scans **8/8 PASS**;
- canonical payload equality **77/77 PASS**;
- unresolved source-completeness defects **0**;
- page-record/canonical-item changes during review **0**.

## Next phase gate

**Phase 3 Gate 6 — Tamil final clearance only.** Translation remains deferred.''', 'intake next')
write(p, t)

# Source metadata
p = BASE / 'metadata/source.md'
t = read(p)
t = replace_once(t,
    '- Phase 3 Gate 5 assembly/source-completeness review: **NEXT / NOT STARTED**;',
    '- Phase 3 Gate 5 assembly/source-completeness review: **COMPLETE / PASS**;', 'metadata gate5')
t = replace_once(t,
    '- Tamil final clearance / translation: **NOT STARTED**.',
    '- Phase 3 Gate 6 Tamil final clearance: **NEXT / NOT STARTED**;\n- translation: **NOT STARTED**.', 'metadata gate6')
metadata_gate5 = '''
## Gate 5 source-completeness review metadata

Evidence: `../PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical inventory: **77/77 PASS**;
- verified body scan accounting: **447/447 PASS**;
- canonical item scan coverage: **439/439 PASS**;
- structural group scans: **8/8 PASS**;
- canonical payload equality against verified page records: **77/77 PASS**;
- unresolved source-completeness defects: **0**;
- verified page/canonical item modifications during review: **0**;
- next ordered gate: **Phase 3 Gate 6 — Tamil final clearance**.
'''
if '## Gate 5 source-completeness review metadata' in t:
    raise SystemExit('metadata Gate 5 section already exists unexpectedly')
t = t.rstrip() + '\n' + metadata_gate5
write(p, t)

# Page map
p = BASE / 'indexes/page-map.md'
t = read(p)
t = replace_once(t,
    '- Gate 5 assembly/source-completeness review: **NEXT / NOT STARTED**;',
    '- Gate 5 assembly/source-completeness review: **COMPLETE / PASS**;', 'pagemap gate5')
t = replace_once(t,
    '- Tamil final clearance / translation: **NOT STARTED**.',
    '- Gate 6 Tamil final clearance: **NEXT / NOT STARTED**;\n- translation: **NOT STARTED**.', 'pagemap gate6')
pagemap_gate5 = '''## Phase 3 Gate 5 — assembly/source-completeness review COMPLETE / PASS

Evidence: `../PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical item files: **77/77 PASS**;
- body scan accounting: **447/447 PASS**;
- item scan accounting: **439/439 PASS**;
- structural group scans: **8/8 PASS**;
- canonical metadata records: **77/77 PASS**;
- canonical payload equality against verified page records: **77/77 PASS**;
- unresolved source-completeness defects: **0**;
- page-record/canonical-item changes during review: **0**.

'''
t = replace_once(t, '## Phase status\n', pagemap_gate5 + '## Phase status\n', 'pagemap insertion')
write(p, t)

# Gate 4 assembly tracker: retain historical scope, append subsequent outcome and change next gate.
p = BASE / 'PHASE3_CANONICAL_ASSEMBLY.md'
t = read(p)
t = sub_once(t, r'## Exact next gate\n\n.*\Z', '''## Subsequent Gate 5 outcome

Phase 3 Gate 5 subsequently completed **PASS**. Durable evidence: `PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical item inventory: **77/77 PASS**;
- verified body scan accounting: **447/447 PASS**;
- item scans: **439/439 PASS**;
- structural group scans: **8/8 PASS**;
- canonical payload equality against the verified page layer: **77/77 PASS**;
- unresolved source-completeness defects: **0**;
- verified page-record changes during Gate 5: **0**;
- canonical item changes during Gate 5: **0**.

## Exact next gate

Proceed to **Phase 3 Gate 6 — Tamil final clearance only**. Confirm Gates 1–5 are all PASS and decide whether the Tamil source/canonical layer can be final-cleared for Phase 4. Do not begin English translation in the same activity.''', 'assembly next')
write(p, t)

print('Gate 5 status synchronization complete across 10 durable status-bearing files; canonical/page layers untouched')
