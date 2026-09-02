from pathlib import Path


def read(path):
    return Path(path).read_text(encoding="utf-8")


def write(path, text):
    Path(path).write_text(text, encoding="utf-8")


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f"missing replacement anchor: {label}")
    return text.replace(old, new, 1)


def replace_between(text, start, end, new_block, label):
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"missing start anchor: {label}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"missing end anchor: {label}")
    return text[:i] + new_block + text[j:]


# HANDOVER
p = "HANDOVER.md"
t = read(p)
t = replace_once(t, "## Durable state after Phase 4 Batch 01", "## Durable state after Phase 4 Batch 02", "handover heading")
t = replace_once(
    t,
    "- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item-assigned scans; Batch 02 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item-assigned scans; Batch 03 NEXT**.",
    "handover phase4 status",
)
block = """## Phase 4 durable result — Batch 02\n\n- Phase 4 status: **IN PROGRESS**;\n- reviewed batches: **2**;\n- reviewed English items: **3/77**;\n- reviewed item-assigned source scans: **35/439**;\n- Batch 02 items: **2 — `தென்னவன் காதை` → The Tale of the Southerner; 3 — `இந்திரஜித்` → Indrajit**;\n- Batch 02 source scans: **34–54 = 21/21**;\n- separate anthology structural scans **32–33** remain outside poem translations;\n- reviewed English items: `translations/en/items/02-the-tale-of-the-southerner-en.md` and `translations/en/items/03-indrajit-en.md`;\n- Batch-02 review: `translations/en/batches/batch-02.md`;\n- translation plan/source map: `translations/en/TRANSLATION_PLAN.md`, `translations/en/SOURCE_MAP.md`;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes during Batch 02: **0**;\n- Tamil `sections/` changes during Batch 02: **0**.\n\nBatch 02 preserves the two exact title witnesses, the Ravana/Indrajit counter-epic framing, source-specific polemic and cultural terms, illustrations/ornaments, the `பத்தரை மாற்று` / `முத்திரை` wordplay notes, and the source-visible final `ஆஎன்` form without Tamil repair.\n\n"""
t = replace_once(t, "\n## Supplied-transcription rule\n", "\n" + block + "## Supplied-transcription rule\n", "handover batch02 insertion")
t = replace_once(
    t,
    "18. canonical item files `sections/01.md` through `sections/77.md` as needed for Phase-4 translation.",
    "18. canonical item files `sections/01.md` through `sections/77.md` as needed for Phase-4 translation;\n19. `poems/kalaignarin-kavithaigal/translations/en/TRANSLATION_PLAN.md`;\n20. `poems/kalaignarin-kavithaigal/translations/en/SOURCE_MAP.md`;\n21. `poems/kalaignarin-kavithaigal/translations/en/README.md`;\n22. the latest reviewed translation batch record (`translations/en/batches/batch-02.md`).",
    "handover mandatory translation docs",
)
marker = "## EXACT NEXT ACTIVITY\n"
if marker not in t:
    raise SystemExit("missing handover next marker")
t = t.split(marker, 1)[0] + marker + "\nExecute **Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.\n\nRead final-cleared `sections/04.md` and `sections/05.md` completely, translate both complete items across scans **55–69**, review them together in `translations/en/batches/batch-03.md`, update `translations/en/SOURCE_MAP.md`, and leave all Tamil source/page/canonical files unchanged. If translation exposes a genuine Tamil discrepancy, reopen the source-backed Tamil layers explicitly before continuing.\n"
write(p, t)

# NEXT_CHAT_PROMPT
p = "NEXT_CHAT_PROMPT.md"
t = read(p)
t = replace_once(
    t,
    "and canonical item files as needed.",
    "canonical item files as needed, and Phase-4 `translations/en/TRANSLATION_PLAN.md`, `translations/en/SOURCE_MAP.md`, `translations/en/README.md`, plus the latest reviewed batch record.",
    "prompt startup translation docs",
)
t = replace_once(
    t,
    "- Phase 4 English translation/release **UNBLOCKED / NOT STARTED — NEXT**.",
    "- Phase 4 English translation/release **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.",
    "prompt phase4 status",
)
new_phase4 = """## Phase 4 Batches 01–02 durable result\n\n- translation scaffold: `translations/en/`;\n- reviewed batches: **2**;\n- reviewed English items: **3/77**;\n- reviewed item scans: **35/439**;\n- item 1: `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**, scans **18–31**;\n- item 2: `தென்னவன் காதை` → **The Tale of the Southerner**, scans **34–42**;\n- item 3: `இந்திரஜித்` → **Indrajit**, scans **43–54**;\n- structural scans **32–33** remain anthology provenance outside poem bodies;\n- Batch reviews: `translations/en/batches/batch-01.md`, `translations/en/batches/batch-02.md`;\n- unresolved reviewed translation issues: **0**;\n- Tamil page/canonical changes: **0**.\n\nFollow `translations/en/TRANSLATION_PLAN.md` and `translations/en/SOURCE_MAP.md` for Phase-4 continuation.\n\n"""
t = replace_between(t, "## Phase 4 Batch 01 durable result\n", "## Locked Phase 3 structure\n", new_phase4, "prompt phase4 block")
marker = "## EXACT NEXT ACTIVITY\n"
if marker not in t:
    raise SystemExit("missing prompt next marker")
t = t.split(marker, 1)[0] + marker + "\nExecute **Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.\n\n1. Read final-cleared `sections/04.md` and `sections/05.md` completely.\n2. Translate both complete items across scans **55–69** with stable item identity and scan provenance.\n3. Review the full batch for omissions, duplication, voice, names, rhetoric and source-specific claims.\n4. Create/update `translations/en/items/`, `translations/en/batches/batch-03.md` and `translations/en/SOURCE_MAP.md`.\n5. Do **not** alter Tamil final-cleared `pages/` or `sections/` during translation.\n"
write(p, t)

# Root README
p = "README.md"
t = read(p)
t = replace_once(
    t,
    "- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.",
    "root phase4 status",
)
t = replace_once(
    t,
    "Batch 01 begins Phase 4 with item 1 `இதயத்தைத் தந்திடு அண்ணா` translated as **Give Me Your Heart, Anna**. The reviewed English layer now covers **1/77 items** and **14/439 item-assigned source scans** with **0** unresolved reviewed translation issues. Files live under `poems/kalaignarin-kavithaigal/translations/en/`. No Tamil page or canonical item has been changed by translation work.",
    "Batches 01–02 now cover items 1–3: `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**, `தென்னவன் காதை` → **The Tale of the Southerner**, and `இந்திரஜித்` → **Indrajit**. The reviewed English layer covers **3/77 items** and **35/439 item-assigned source scans** with **0** unresolved reviewed translation issues. Files live under `poems/kalaignarin-kavithaigal/translations/en/`. No Tamil page or canonical item has been changed by translation work.",
    "root progress paragraph",
)
t = replace_once(
    t,
    "**Phase 4 Batch 02 — items 2–3 (`தென்னவன் காதை`, `இந்திரஜித்`)**. Translate and review both complete final-cleared items; leave Tamil archival files unchanged.",
    "**Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**. Translate and review both complete final-cleared items across scans **55–69**; leave Tamil archival files unchanged.",
    "root next",
)
write(p, t)

# TRANSCRIPTION_PHASE_PLAN
p = "TRANSCRIPTION_PHASE_PLAN.md"
t = read(p)
phase4 = """## Phase 4 — translation and release\n\n**IN PROGRESS — Batches 01–02 reviewed PASS.**\n\n- reviewed batches: **2**;\n- reviewed English items: **3/77**;\n- reviewed item-assigned source scans: **35/439**;\n- Batch 01: item 1 `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**;\n- Batch 02: item 2 `தென்னவன் காதை` → **The Tale of the Southerner**; item 3 `இந்திரஜித்` → **Indrajit**;\n- translation scaffold: `poems/kalaignarin-kavithaigal/translations/en/`;\n- unresolved reviewed translation issues: **0**;\n- Tamil page/canonical changes during Phase 4 so far: **0**;\n- Batch 03 items 4–5: **NEXT**.\n\n"""
t = replace_between(t, "## Phase 4 — translation and release\n", "## EXACT NEXT ACTIVITY\n", phase4, "phase plan phase4")
marker = "## EXACT NEXT ACTIVITY\n"
t = t.split(marker, 1)[0] + marker + "\nExecute **Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)** from the Tamil final-cleared canonical layer across scans **55–69**. Review both complete translations before marking the batch PASS; do not alter Tamil final-cleared files.\n"
write(p, t)

# Active README
p = "poems/kalaignarin-kavithaigal/README.md"
t = read(p)
t = replace_once(
    t,
    "- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.",
    "active status",
)
phase4 = """## Phase 4 — English translation\n\n**IN PROGRESS — Batches 01–02 reviewed PASS.**\n\n- translation root: `translations/en/`;\n- reviewed batches: **2**;\n- reviewed items: **3/77**;\n- reviewed item-assigned scans: **35/439**;\n- item 1 `இதயத்தைத் தந்திடு அண்ணா` → **Give Me Your Heart, Anna**;\n- item 2 `தென்னவன் காதை` → **The Tale of the Southerner**;\n- item 3 `இந்திரஜித்` → **Indrajit**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` / `sections/` changes: **0**.\n\n"""
t = replace_between(t, "## Phase 4 — English translation\n", "## Next activity\n", phase4, "active phase4 block")
marker = "## Next activity\n"
t = t.split(marker, 1)[0] + marker + "\n**Phase 4 Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**. Translate both complete final-cleared canonical items across scans **55–69** and review the batch before advancing.\n"
write(p, t)

# SOURCE_INTAKE
p = "poems/kalaignarin-kavithaigal/SOURCE_INTAKE.md"
t = read(p)
t = replace_once(
    t,
    "- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.",
    "intake status",
)
t = replace_once(
    t,
    "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batch 01 is reviewed PASS; Batch 02 items 2–3 are next.",
    "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–02 are reviewed PASS; Batch 03 items 4–5 are next.",
    "intake next phase gate",
)
phase4 = """## Phase 4 translation state\n\n- Batches 01–02: **reviewed PASS**;\n- reviewed items: **3/77**;\n- reviewed item scans: **35/439**;\n- English item 1: `translations/en/items/01-give-me-your-heart-anna-en.md`;\n- English item 2: `translations/en/items/02-the-tale-of-the-southerner-en.md`;\n- English item 3: `translations/en/items/03-indrajit-en.md`;\n- unresolved reviewed translation issues: **0**;\n- Tamil page/canonical changes: **0**;\n- exact next: **Batch 03 items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.\n"""
i = t.find("## Phase 4 translation state\n")
if i < 0:
    raise SystemExit("missing intake phase4 block")
t = t[:i] + phase4
write(p, t)

# metadata/source.md
p = "poems/kalaignarin-kavithaigal/metadata/source.md"
t = read(p)
t = replace_once(
    t,
    "- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**.",
    "metadata status",
)
phase4 = """## Phase 4 translation metadata\n\n- Tamil source/canonical layer remains **FINAL-CLEARED**;\n- reviewed batches: **2**;\n- reviewed English items: **3/77**;\n- reviewed item scans: **35/439**;\n- Batch 01 English item: `../translations/en/items/01-give-me-your-heart-anna-en.md`;\n- Batch 02 English items: `../translations/en/items/02-the-tale-of-the-southerner-en.md`, `../translations/en/items/03-indrajit-en.md`;\n- Batch 02 review: `../translations/en/batches/batch-02.md`;\n- unresolved reviewed translation issues: **0**;\n- Tamil page/canonical changes caused by translation: **0**;\n- next translation batch: **items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.\n"""
i = t.find("## Phase 4 translation metadata\n")
if i < 0:
    raise SystemExit("missing metadata phase4 block")
t = t[:i] + phase4
write(p, t)

# audit.md — keep Batch01 evidence and replace its next marker with Batch02 evidence + Batch03 next.
p = "poems/kalaignarin-kavithaigal/audit.md"
t = read(p)
old = "### Exact next Phase-4 activity\n\n**Batch 02 — items 2–3 (`தென்னவன் காதை`, `இந்திரஜித்`)**.\n"
new = """## Phase 4 Batch 02 audit — REVIEWED / PASS\n\nScope: English translation/review of final-cleared canonical items **2–3**.\n\n- item 2: `தென்னவன் காதை` → **The Tale of the Southerner**;\n- item 3: `இந்திரஜித்` → **Indrajit**;\n- reviewed items after Batch 02: **3/77**;\n- Batch-02 item-owned scans: **21/21 — scans 34–54**;\n- cumulative reviewed item-owned scans: **35/439**;\n- structural group scans **32–33** excluded from poem bodies: **PASS**;\n- title witnesses: **2 exact / 0 variants**;\n- source scan boundaries represented: **PASS**;\n- counter-epic rhetoric / speaker changes / betrayal sequences retained: **PASS**;\n- cultural and wordplay decisions documented: **PASS**;\n- omission/duplication issues: **0**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page-record changes: **0**;\n- Tamil canonical-item changes: **0**;\n- batch evidence: `translations/en/batches/batch-02.md`;\n- English items: `translations/en/items/02-the-tale-of-the-southerner-en.md`, `translations/en/items/03-indrajit-en.md`.\n\n### Exact next Phase-4 activity\n\n**Batch 03 — items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**, scans **55–69**.\n"""
t = replace_once(t, old, new, "audit Batch02 insertion")
write(p, t)

# page-map.md
p = "poems/kalaignarin-kavithaigal/indexes/page-map.md"
t = read(p)
t = replace_once(
    t,
    "- Phase 4 English translation/release: **IN PROGRESS — Batch 01 reviewed PASS; 1/77 items; 14/439 item scans; Batch 02 NEXT**;",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–02 reviewed PASS; 3/77 items; 35/439 item scans; Batch 03 NEXT**;",
    "page map status",
)
t = replace_once(
    t,
    "Phase 4 Batch 01 reviewed item 1 across scans **18–31** (**14/439** item-assigned scans). This translation milestone changes no scan↔page mapping and no Tamil page/canonical file.",
    "Phase 4 Batches 01–02 reviewed items 1–3 across item-owned scans **18–31, 34–54** (**35/439** item-assigned scans). Structural scans **32–33** remain separate anthology provenance. These translation milestones change no scan↔page mapping and no Tamil page/canonical file.",
    "page map phase4 note",
)
write(p, t)

# PHASE3_TAMIL_FINAL_CLEARANCE.md — historical clearance stays unchanged; only subsequent Phase4 status advances.
p = "poems/kalaignarin-kavithaigal/PHASE3_TAMIL_FINAL_CLEARANCE.md"
t = read(p)
t = replace_once(
    t,
    "Phase 4 has subsequently started. **Batch 01 is reviewed PASS** for item 1 `இதயத்தைத் தந்திடு அண்ணா` (**Give Me Your Heart, Anna**), covering **14/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remained unchanged. Exact next translation activity: **Batch 02 items 2–3**.",
    "Phase 4 has subsequently advanced through **Batches 01–02, both reviewed PASS**. Reviewed English now covers items **1–3/77** and **35/439** item-assigned scans: `இதயத்தைத் தந்திடு அண்ணா` (**Give Me Your Heart, Anna**), `தென்னவன் காதை` (**The Tale of the Southerner**) and `இந்திரஜித்` (**Indrajit**). The Tamil final-cleared `pages/` and `sections/` layers remained unchanged. Exact next translation activity: **Batch 03 items 4–5 (`இரணியன்`, `வாளி மன்னன்`)**.",
    "final clearance subsequent status",
)
write(p, t)

print("Phase 4 Batch 02 durable status synchronization complete")
