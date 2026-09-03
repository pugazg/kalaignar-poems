from pathlib import Path


def load(path):
    return Path(path).read_text(encoding='utf-8')


def save(path, text):
    Path(path).write_text(text, encoding='utf-8')


def must_replace(path, old, new, count=1):
    text = load(path)
    found = text.count(old)
    if found < count:
        raise SystemExit(f'{path}: expected at least {count} occurrence(s), found {found}: {old[:100]!r}')
    text = text.replace(old, new, count)
    save(path, text)

# Root README
must_replace('README.md',
'- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.',
'- Phase 4 English translation/release: **IN PROGRESS — Batches 01–03 reviewed PASS; 5/77 items; 50/439 item scans; Batch 04 NEXT**.')
must_replace('README.md',
'Batches 01–02 now cover items 1–3: `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**, `தென்னவன் காதை` → **The Tale of the Southerner**, and `இந்திரஜித்` → **Indrajit**. The reviewed English layer covers **3/77 items** and **35/439 item-assigned source scans** with **0** unresolved reviewed translation issues. Files live under `poems/kalaignarin-kavithaigal/translations/en/`. No Tamil page or canonical item has been changed by translation work.',
'Batches 01–03 now cover items 1–5: `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**, `தென்னவன் காதை` → **The Tale of the Southerner**, `இந்திரஜித்` → **Indrajit**, `இரணியன்` → **Hiranyan**, and `வாளி மன்னன்` → **King Vali**. The reviewed English layer covers **5/77 items** and **50/439 item-assigned source scans** with **0** unresolved reviewed translation issues. Files live under `poems/kalaignarin-kavithaigal/translations/en/`. No Tamil page or canonical item has been changed by translation work.')
must_replace('README.md',
'**Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**. Translate and review both complete final-cleared items across scans **55–69**; leave Tamil archival files unchanged.',
'**Phase 4 Batch 04 — items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)**. Keep structural group-divider/verso scans **70–71** outside poem translations; translate and review both complete final-cleared items across scans **72–89**; leave Tamil archival files unchanged.')

# Phase plan
must_replace('TRANSCRIPTION_PHASE_PLAN.md', '**IN PROGRESS — Batches 01–02 reviewed PASS.**', '**IN PROGRESS — Batches 01–03 reviewed PASS.**')
must_replace('TRANSCRIPTION_PHASE_PLAN.md', '- reviewed batches: **2**;', '- reviewed batches: **3**;')
must_replace('TRANSCRIPTION_PHASE_PLAN.md', '- reviewed English items: **3/77**;', '- reviewed English items: **5/77**;')
must_replace('TRANSCRIPTION_PHASE_PLAN.md', '- reviewed item-assigned source scans: **35/439**;', '- reviewed item-assigned source scans: **50/439**;')
must_replace('TRANSCRIPTION_PHASE_PLAN.md',
'- Batch 02: item 2 `தென்னவன் காதை` → **The Tale of the Southerner**; item 3 `இந்திரஜித்` → **Indrajit**;\n',
'- Batch 02: item 2 `தென்னவன் காதை` → **The Tale of the Southerner**; item 3 `இந்திரஜித்` → **Indrajit**;\n- Batch 03: item 4 `இரணியன்` → **Hiranyan**; item 5 `வாளி மன்னன்` → **King Vali**;\n')
must_replace('TRANSCRIPTION_PHASE_PLAN.md', '- Batch 03 items 4–5: **NEXT**.', '- Batch 04 items 6–7: **NEXT**.')
must_replace('TRANSCRIPTION_PHASE_PLAN.md',
'Execute **Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)** from the Tamil final-cleared canonical layer across scans **55–69**. Review both complete translations before marking the batch PASS; do not alter Tamil final-cleared files.',
'Execute **Phase 4 Batch 04 — items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)** from the Tamil final-cleared canonical layer. Keep structural group-divider/verso scans **70–71** outside poem translations, review both complete translations across scans **72–89** before marking the batch PASS, and do not alter Tamil final-cleared files.')

# Active README
p = 'poems/kalaignarin-kavithaigal/README.md'
must_replace(p, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.', '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–03 reviewed PASS; 5/77 items; 50/439 item scans; Batch 04 NEXT**.')
must_replace(p, '**IN PROGRESS — Batches 01–02 reviewed PASS.**', '**IN PROGRESS — Batches 01–03 reviewed PASS.**')
must_replace(p, '- reviewed batches: **2**;', '- reviewed batches: **3**;')
must_replace(p, '- reviewed items: **3/77**;', '- reviewed items: **5/77**;')
must_replace(p, '- reviewed item-assigned scans: **35/439**;', '- reviewed item-assigned scans: **50/439**;')
must_replace(p, '- item 3 `இந்திரஜித்` → **Indrajit**;\n', '- item 3 `இந்திரஜித்` → **Indrajit**;\n- item 4 `இரணியன்` → **Hiranyan**;\n- item 5 `வாளி மன்னன்` → **King Vali**;\n')
must_replace(p, '**Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**. Translate both complete final-cleared canonical items across scans **55–69** and review the batch before advancing.', '**Phase 4 Batch 04 — items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)**. Keep structural scans **70–71** outside poem translations; translate both complete final-cleared canonical items across scans **72–89** and review the batch before advancing.')

# Source intake
p = 'poems/kalaignarin-kavithaigal/SOURCE_INTAKE.md'
must_replace(p, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.', '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–03 reviewed PASS; 5/77 items; 50/439 item scans; Batch 04 NEXT**.')
must_replace(p, '**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–02 are reviewed PASS; Batch 03 items 4–5 are next.', '**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–03 are reviewed PASS; Batch 04 items 6–7 are next.')
must_replace(p, '- Batches 01–02: **reviewed PASS**;', '- Batches 01–03: **reviewed PASS**;')
must_replace(p, '- reviewed items: **3/77**;', '- reviewed items: **5/77**;')
must_replace(p, '- reviewed item scans: **35/439**;', '- reviewed item scans: **50/439**;')
must_replace(p, '- English item 3: `translations/en/items/03-indrajit-en.md`;\n', '- English item 3: `translations/en/items/03-indrajit-en.md`;\n- English item 4: `translations/en/items/04-hiranyan-en.md`;\n- English item 5: `translations/en/items/05-king-vali-en.md`;\n')
must_replace(p, '- exact next: **Batch 03 items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.', '- exact next: **Batch 04 items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)**, scans **72–89**, with structural scans **70–71** kept outside poem translations.')

# Source metadata
p = 'poems/kalaignarin-kavithaigal/metadata/source.md'
must_replace(p, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.', '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–03 reviewed PASS; 5/77 items; 50/439 item scans; Batch 04 NEXT**.')
must_replace(p, '- reviewed batches: **2**;', '- reviewed batches: **3**;')
must_replace(p, '- reviewed English items: **3/77**;', '- reviewed English items: **5/77**;')
must_replace(p, '- reviewed item scans: **35/439**;', '- reviewed item scans: **50/439**;')
must_replace(p, '- Batch 02 review: `../translations/en/batches/batch-02.md`;\n', '- Batch 02 review: `../translations/en/batches/batch-02.md`;\n- Batch 03 English items: `../translations/en/items/04-hiranyan-en.md`, `../translations/en/items/05-king-vali-en.md`;\n- Batch 03 review: `../translations/en/batches/batch-03.md`;\n')
must_replace(p, '- next translation batch: **items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.', '- next translation batch: **items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)**, scans **72–89**, after structural scans **70–71**.')

# Page map
p = 'poems/kalaignarin-kavithaigal/indexes/page-map.md'
must_replace(p, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**;', '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–03 reviewed PASS; 5/77 items; 50/439 item scans; Batch 04 NEXT**;')
must_replace(p, 'Phase 4 Batches 01–02 reviewed items 1–3 across item-owned scans **18–31, 34–54** (**35/439** item-assigned scans). Structural scans **32–33** remain separate anthology provenance. These translation milestones change no scan↔page mapping and no Tamil page/canonical file.', 'Phase 4 Batches 01–03 reviewed items 1–5 across item-owned scans **18–31, 34–69** (**50/439** item-assigned scans). Structural scans **32–33** remain separate anthology provenance; the next structural pair **70–71** is also outside poem translations. These translation milestones change no scan↔page mapping and no Tamil page/canonical file.')

# Final-clearance follow-up
p = 'poems/kalaignarin-kavithaigal/PHASE3_TAMIL_FINAL_CLEARANCE.md'
must_replace(p, 'Phase 4 has subsequently advanced through **Batches 01–02, both reviewed PASS**. Reviewed English now covers items **1–3/77** and **35/439** item-assigned scans: `இதயத்தைத் தந்திடு அண்ணா` (**Give Me Your Heart, Anna**), `தென்னவன் காதை` (**The Tale of the Southerner**) and `இந்திரஜித்` (**Indrajit**). The Tamil final-cleared `pages/` and `sections/` layers remained unchanged. Exact next translation activity: **Batch 03 items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.', 'Phase 4 has subsequently advanced through **Batches 01–03, all reviewed PASS**. Reviewed English now covers items **1–5/77** and **50/439** item-assigned scans: `இதயத்தைத் தந்திடு அண்ணா` (**Give Me Your Heart, Anna**), `தென்னவன் காதை` (**The Tale of the Southerner**), `இந்திரஜித்` (**Indrajit**), `இரணியன்` (**Hiranyan**) and `வாளி மன்னன்` (**King Vali**). The Tamil final-cleared `pages/` and `sections/` layers remained unchanged. Exact next translation activity: **Batch 04 items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)**, with structural scans **70–71** kept outside poem translations.')

# Audit: replace the prior next marker with Batch 03 audit + new next marker
p = 'poems/kalaignarin-kavithaigal/audit.md'
old = '''### Exact next Phase-4 activity

**Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**, scans **55–69**.'''
new = '''## Phase 4 Batch 03 audit — REVIEWED / PASS

Scope: English translation/review of final-cleared canonical items **4–5**.

- item 4: `இரணியன்` → **Hiranyan**;
- item 5: `வாளி மன்னன்` → **King Vali**;
- reviewed items after Batch 03: **5/77**;
- Batch-03 item-owned scans: **15/15 — scans 55–69**;
- cumulative reviewed item-owned scans: **50/439**;
- title witnesses: **2 exact / 0 variants**;
- source scan boundaries represented: **PASS**;
- counter-mythic/rationalist polemic and source-form wordplay retained: **PASS**;
- Tara/Sugriva confrontation and Vali/Rama hidden-arrow accusation retained: **PASS**;
- closing ornaments represented: **2/2**;
- omission/duplication issues: **0**;
- unresolved reviewed translation issues: **0**;
- Tamil page-record changes: **0**;
- Tamil canonical-item changes: **0**;
- batch evidence: `translations/en/batches/batch-03.md`;
- English items: `translations/en/items/04-hiranyan-en.md`, `translations/en/items/05-king-vali-en.md`.

### Exact next Phase-4 activity

**Batch 04 — items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)**, scans **72–89**. Preserve structural group-divider/verso scans **70–71** outside poem translations.'''
must_replace(p, old, new)

# HANDOVER
p = 'HANDOVER.md'
must_replace(p, '## Durable state after Phase 4 Batch 02', '## Durable state after Phase 4 Batch 03')
must_replace(p, '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item-assigned scans; Batch 03 NEXT**.', '- Phase 4 English translation/release: **IN PROGRESS — Batches 01–03 reviewed PASS; 5/77 items; 50/439 item-assigned scans; Batch 04 NEXT**.')
insert_before = '## Supplied-transcription rule\n'
text = load(p)
if '## Phase 4 durable result — Batch 03' not in text:
    block = '''## Phase 4 durable result — Batch 03

- Phase 4 status: **IN PROGRESS**;
- reviewed batches: **3**;
- reviewed English items: **5/77**;
- reviewed item-assigned source scans: **50/439**;
- Batch 03 items: **4 — `இரணியன்` → Hiranyan; 5 — `வாளி மன்னன்` → King Vali**;
- Batch 03 source scans: **55–69 = 15/15**;
- title witnesses: **2 exact / 0 variants**;
- reviewed English items: `translations/en/items/04-hiranyan-en.md` and `translations/en/items/05-king-vali-en.md`;
- Batch-03 review: `translations/en/batches/batch-03.md`;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes during Batch 03: **0**;
- Tamil `sections/` changes during Batch 03: **0**.

Batch 03 preserves the Hiranyan/Prahlada counter-myth, source-form Tamil wordplay and magnetic-pillar conspiracy as source rhetoric; it also preserves Tara's political voice, Sugriva/Hanuman intrigue, Rama's source-quoted description and Vali's hidden-arrow accusation without external harmonisation. Both closing ornaments remain represented.

'''
    if insert_before not in text:
        raise SystemExit('HANDOVER.md: insertion anchor missing')
    text = text.replace(insert_before, block + insert_before, 1)
    save(p, text)
must_replace(p, '22. the latest reviewed translation batch record (`translations/en/batches/batch-02.md`).', '22. the latest reviewed translation batch record (`translations/en/batches/batch-03.md`).')
old = '''Execute **Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.

Read final-cleared `sections/04.md` and `sections/05.md` completely, translate both complete items across scans **55–69**, review them together in `translations/en/batches/batch-03.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged. If translation exposes a genuine Tamil discrepancy, reopen the source-backed Tamil layers explicitly before continuing.'''
new = '''Execute **Phase 4 Batch 04 — items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)**.

Preserve structural group-divider/verso scans **70–71** outside poem translations. Read final-cleared `sections/06.md` and `sections/07.md` completely, translate both complete items across scans **72–89**, review them together in `translations/en/batches/batch-04.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged. If translation exposes a genuine Tamil discrepancy, reopen the source-backed Tamil layers explicitly before continuing.'''
must_replace(p, old, new)

# NEXT_CHAT_PROMPT
p = 'NEXT_CHAT_PROMPT.md'
must_replace(p, '- Phase 4 English translation/release **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.', '- Phase 4 English translation/release **IN PROGRESS — Batches 01–03 reviewed PASS; 5/77 items; 50/439 item scans; Batch 04 NEXT**.')
must_replace(p, '## Phase 4 Batches 01–02 durable result', '## Phase 4 Batches 01–03 durable result')
must_replace(p, '- reviewed batches: **2**;', '- reviewed batches: **3**;')
must_replace(p, '- reviewed English items: **3/77**;', '- reviewed English items: **5/77**;')
must_replace(p, '- reviewed item scans: **35/439**;', '- reviewed item scans: **50/439**;')
must_replace(p, '- item 3: `இந்திரஜித்` → **Indrajit**, scans **43–54**;\n', '- item 3: `இந்திரஜித்` → **Indrajit**, scans **43–54**;\n- item 4: `இரணியன்` → **Hiranyan**, scans **55–61**;\n- item 5: `வாளி மன்னன்` → **King Vali**, scans **62–69**;\n')
must_replace(p, '- Batch reviews: `translations/en/batches/batch-01.md`, `translations/en/batches/batch-02.md`;', '- Batch reviews: `translations/en/batches/batch-01.md`, `translations/en/batches/batch-02.md`, `translations/en/batches/batch-03.md`;')
old = '''Execute **Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.

1. Read final-cleared `sections/04.md` and `sections/05.md` completely.
2. Translate both complete items across scans **55–69** with stable item identity and scan provenance.
3. Review the full batch for omissions, duplication, voice, names, rhetoric and source-specific claims.
4. Create/update `translations/en/items/`, `translations/en/batches/batch-03.md` and `translations/en/SOURCE_MAP.md`.
5. Do **not** alter Tamil final-cleared `pages/` or `sections/` during translation.'''
new = '''Execute **Phase 4 Batch 04 — items 6–7 (`விடுதலை வீரர்கள்`, `ஐம்புலன்`)**.

1. Preserve structural group-divider/verso scans **70–71** outside poem translations.
2. Read final-cleared `sections/06.md` and `sections/07.md` completely.
3. Translate both complete items across scans **72–89** with stable item identity and scan provenance.
4. Review the full batch for omissions, duplication, voice, names, rhetoric and source-specific claims.
5. Create/update `translations/en/items/`, `translations/en/batches/batch-04.md` and `translations/en/SOURCE_MAP.md`.
6. Do **not** alter Tamil final-cleared `pages/` or `sections/` during translation.'''
must_replace(p, old, new)

print('Phase 4 Batch 03 durable status synchronization complete')
