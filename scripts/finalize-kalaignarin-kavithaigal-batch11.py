from pathlib import Path
import re
import subprocess

BASE = "b5be277f95b5f3be06f7ce6a9649a91ff52278f6"
ROOT = Path(".")
WORK = "poems/kalaignarin-kavithaigal"
EN = f"{WORK}/translations/en"

items = {
    f"{EN}/items/41-we-move-as-your-shadow-en.md": (41, list(range(379, 382)), "variant"),
    f"{EN}/items/42-long-live-jeeva-en.md": (42, list(range(382, 384)), "variant"),
    f"{EN}/items/43-the-fallen-hero-en.md": (43, list(range(384, 390)), "exact"),
    f"{EN}/items/44-my-dear-friend-why-did-you-leave-en.md": (44, list(range(390, 392)), "exact"),
    f"{EN}/items/45-today-is-your-birthday-en.md": (45, list(range(394, 396)), "variant"),
}


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(path, old, new, count=1):
    text = read(path)
    found = text.count(old)
    if found < count:
        raise SystemExit(f"required text not found enough times in {path}: {old!r} found={found}")
    write(path, text.replace(old, new, count))


def replace_if_present(path, old, new, count=1):
    text = read(path)
    if old in text:
        write(path, text.replace(old, new, count))
        return True
    return False


def insert_before(path, marker, block):
    text = read(path)
    if block.strip() in text:
        return
    idx = text.find(marker)
    if idx < 0:
        raise SystemExit(f"marker not found in {path}: {marker}")
    write(path, text[:idx] + block.rstrip() + "\n\n" + text[idx:])


def replace_tail(path, heading, new_tail):
    text = read(path)
    idx = text.rfind(heading)
    if idx < 0:
        raise SystemExit(f"tail heading not found in {path}: {heading}")
    write(path, text[:idx] + new_tail.rstrip() + "\n")


# 1) Mechanical item certification and status promotion.
marker_total = 0
exact_count = 0
variant_count = 0
for path, (item, expected, witness_kind) in items.items():
    text = read(path)
    markers = [int(x) for x in re.findall(r"<!-- scan (\d+) -->", text)]
    if markers != expected:
        raise SystemExit(f"marker mismatch {path}: {markers} != {expected}")
    if 392 in markers or 393 in markers:
        raise SystemExit(f"structural scan leaked into item translation: {path}")
    if f"item: {item}\n" not in text:
        raise SystemExit(f"item identity mismatch {path}")
    if witness_kind == "exact":
        if 'title_witness_status: "exact"' not in text:
            raise SystemExit(f"exact title status missing {path}")
        exact_count += 1
    else:
        if 'title_witness_status: "variant' not in text:
            raise SystemExit(f"variant title status missing {path}")
        variant_count += 1
    if 'status: "review-pending"' not in text:
        raise SystemExit(f"review-pending status missing {path}")
    write(path, text.replace('status: "review-pending"', 'status: "batch-reviewed"', 1))
    marker_total += len(markers)

if marker_total != 15:
    raise SystemExit(f"Batch 11 marker total {marker_total} != 15")
if (exact_count, variant_count) != (2, 3):
    raise SystemExit(f"title witness count mismatch exact={exact_count} variant={variant_count}")

batch = f"{EN}/batches/batch-11.md"
replace_required(batch, "**REVIEWED — PASS, pending mechanical promotion/certification.**", "**REVIEWED — PASS.**")
batch_text = read(batch)
if "## Certification result" not in batch_text:
    batch_text += """

## Certification result

- exact scan-marker sequences: **15/15 PASS**;
- item identities: **5/5 PASS**;
- structural scans **392–393** excluded from all five English item files: **PASS**;
- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes: **0**;
- Tamil `sections/` changes: **0**.
"""
    write(batch, batch_text)

# 2) Translation plan.
plan = f"{EN}/TRANSLATION_PLAN.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–10 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–11 reviewed PASS.**"),
    ("- batches: **10**;", "- batches: **11**;"),
    ("- items: **40/77**;", "- items: **45/77**;"),
    ("- item-assigned source scans: **355/439**;", "- item-assigned source scans: **370/439**;"),
    ("| 11 | 41–45 | 379–395 item-owned scans; structural 392–393 excluded | **NEXT** |", "| 11 | 41–45 | 379–395 item-owned scans; structural 392–393 excluded | **reviewed — PASS** |\n| 12 | 46–50 | 396–404 | **NEXT** |"),
    ("| later | 46–77 | five complete items per iteration (final remainder excepted) | pending |", "| later | 51–77 | five complete items per iteration (final remainder excepted) | pending |"),
]:
    replace_required(plan, old, new)
if "## Batch 11 decision record" not in read(plan):
    insert_before(plan, "## Exact next activity", """## Batch 11 decision record

Batch 11 reviewed complete items **41–45** with **15/15 item-owned scans** across physical span **379–395**. Structural anthology scans **392–393 (`மலர்த் தோட்டம்`)** remain outside poem translations. Title witnesses are **2 exact + 3 authorised variants**. The reviewed translations preserve Anna's seventy-five/sixty refrain and shadow elegy; Jeeva's fragrance/service/prison rhetoric; the full K. V. K. Sami lover-warrior narrative and assassination sequence with source-sensitive `ஓதிய மிலார்`, `முடை` and final caste-marked abuse documented rather than normalized; the intimate Kannadasan friendship elegy; and the Kamaraj birthday tribute with verified `கருத்திருக்கும்` repetition left unrepaired. Tamil `pages/`/`sections/` changes remain **0**.""")
replace_tail(plan, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 12 — items 46–50**: `அவன் பிறந்தநாள் என ஒன்றில்லை!`, `அருமருந்தே! அன்பழக உடன்பிறப்பே!`, `பகுத்தறிவுப் பாண்டியனார்!`, `நியாயத் தராசு`, `ஏற்பாரோ?`. Process all five complete poems across scans **396–404 = 9/9**. There is no separate anthology structural scan inside this batch. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**. Leave Tamil `pages/` and `sections/` unchanged.""")

# 3) Translation source map.
smap = f"{EN}/SOURCE_MAP.md"
rows = """| 41 | `உன் நிழலாக அசைகின்றோம்!` | `உன் நிழலாக அசைகின்றோம்` | **We Move as Your Shadow!** | 379–381 | 362–364 | `items/41-we-move-as-your-shadow-en.md` | **batch-reviewed — PASS** |
| 42 | `வாழ்க ஜீவா` | `வாழ்க ஜீவா!` | **Long Live Jeeva** | 382–383 | 365–366 | `items/42-long-live-jeeva-en.md` | **batch-reviewed — PASS** |
| 43 | `மறைந்த மாவீரன்` | `மறைந்த மாவீரன்` | **The Fallen Hero** | 384–389 | 367–372 | `items/43-the-fallen-hero-en.md` | **batch-reviewed — PASS** |
| 44 | `என் இனிய நண்பா! ஏன் பிரிந்தாய்?` | `என் இனிய நண்பா! ஏன் பிரிந்தாய்?` | **My Dear Friend! Why Did You Leave?** | 390–391 | 373–374 | `items/44-my-dear-friend-why-did-you-leave-en.md` | **batch-reviewed — PASS** |
| 45 | `இன்றைக்கு உன்றன் பிறந்த நாள்` | `இன்றைக்கு உன் பிறந்த நாள்` | **Today Is Your Birthday** | 394–395 | 377–378 | `items/45-today-is-your-birthday-en.md` | **batch-reviewed — PASS** |"""
smap_text = read(smap)
if "| 41 | `உன் நிழலாக அசைகின்றோம்!`" not in smap_text:
    lines = smap_text.splitlines()
    pos = next((i + 1 for i, line in enumerate(lines) if line.startswith("| 40 |")), None)
    if pos is None:
        raise SystemExit("SOURCE_MAP item40 row missing")
    lines[pos:pos] = rows.splitlines()
    write(smap, "\n".join(lines) + "\n")
for old, new in [
    ("- reviewed English batches: **10**;", "- reviewed English batches: **11**;"),
    ("- reviewed English items: **40/77**;", "- reviewed English items: **45/77**;"),
    ("- reviewed item-assigned scans: **355/439**;", "- reviewed item-assigned scans: **370/439**;"),
]:
    replace_required(smap, old, new)
if "### Items 41–45 provenance notes" not in read(smap):
    insert_before(smap, "## Exact next mapping activity", """### Items 41–45 provenance notes

- item 41 owns scans **379–381** (**3/3** represented), with an authorised terminal-punctuation title variant;
- item 42 owns scans **382–383** (**2/2** represented), with an authorised terminal-punctuation title variant;
- item 43 owns scans **384–389** (**6/6** represented), exact title witness;
- item 44 owns scans **390–391** (**2/2** represented), exact title witness;
- structural scans **392–393 (`மலர்த் தோட்டம்`)** remain outside all English poem items;
- item 45 owns scans **394–395** (**2/2** represented), with authorised `உன்றன்` / `உன்` title variation;
- no Tamil page or canonical item was changed by Batch 11.""")
replace_tail(smap, "## Exact next mapping activity", """## Exact next mapping activity

Add reviewed mappings for **items 46–50** after Phase-4 Batch 12 passes. Batch 12 owns **9/9 item scans** across physical span **396–404** and contains no separate anthology structural scan. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**.""")

# 4) Translation README.
tread = f"{EN}/README.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–10 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–11 reviewed PASS.**"),
    ("- reviewed English batches: **10**;", "- reviewed English batches: **11**;"),
    ("- reviewed English items: **40/77**;", "- reviewed English items: **45/77**;"),
    ("- item-assigned source scans covered by reviewed English: **355/439**;", "- item-assigned source scans covered by reviewed English: **370/439**;"),
]:
    replace_required(tread, old, new)
tread_text = read(tread)
if "items/41-we-move-as-your-shadow-en.md" not in tread_text:
    needle = "- `items/40-mother-arts-foremost-son-en.md` — reviewed English item 40."
    addition = needle + "\n- `batches/batch-11.md` — reviewed Batch-11 record;\n- `items/41-we-move-as-your-shadow-en.md` — reviewed English item 41;\n- `items/42-long-live-jeeva-en.md` — reviewed English item 42;\n- `items/43-the-fallen-hero-en.md` — reviewed English item 43;\n- `items/44-my-dear-friend-why-did-you-leave-en.md` — reviewed English item 44;\n- `items/45-today-is-your-birthday-en.md` — reviewed English item 45."
    if needle not in tread_text:
        raise SystemExit("translation README item40 line missing")
    write(tread, tread_text.replace(needle, addition, 1))
if "## Batch 11" not in read(tread):
    insert_before(tread, "## Exact next activity", """## Batch 11

**Reviewed — PASS.**

Standing five-poem iteration covering items **41–45** with **15/15 item-owned scans** across physical span **379–395**. Structural scans **392–393 (`மலர்த் தோட்டம்`)** remain outside poem bodies.

- item 41 → **We Move as Your Shadow!**, scans **379–381**;
- item 42 → **Long Live Jeeva**, scans **382–383**;
- item 43 → **The Fallen Hero**, scans **384–389**;
- item 44 → **My Dear Friend! Why Did You Leave?**, scans **390–391**;
- item 45 → **Today Is Your Birthday**, scans **394–395**;
- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;
- unresolved translation issues: **0**;
- Tamil changes: **0**.""")
replace_tail(tread, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 12 — items 46–50**, scans **396–404 = 9/9**. There is no separate anthology structural scan inside the batch. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**.""")

# 5) Work audit.
audit = f"{WORK}/audit.md"
replace_tail(audit, "### Exact next Phase-4 activity", """## Phase 4 Batch 11 audit — REVIEWED / PASS

Scope: English translation/review of final-cleared canonical items **41–45**.

- items after Batch 11: **45/77**;
- Batch-11 item-owned scans: **15/15** across physical span **379–395**;
- cumulative reviewed item-owned scans: **370/439**;
- structural scans **392–393 (`மலர்த் தோட்டம்`)** excluded from poem translations: **PASS**;
- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;
- exact English scan-marker sequences: **15/15 PASS**;
- omission/duplication issues: **0**;
- unresolved reviewed translation issues: **0**;
- Tamil page-record changes: **0**;
- Tamil canonical-item changes: **0**;
- batch evidence: `translations/en/batches/batch-11.md`.

### Exact next Phase-4 activity

**Batch 12 — items 46–50**, scans **396–404 = 9/9**. There is no separate anthology structural scan inside the batch; expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**.""")

# 6) Repository and work status docs.
root_readme = "README.md"
replace_required(root_readme,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.")
replace_required(root_readme,
    "Batches 01–10 now cover items **1–40**. The reviewed English layer covers **40/77 items** and **355/439 item-assigned source scans** with **0** unresolved reviewed translation issues.",
    "Batches 01–11 now cover items **1–45**. The reviewed English layer covers **45/77 items** and **370/439 item-assigned source scans** with **0** unresolved reviewed translation issues.")
replace_tail(root_readme, "## Next activity", """## Next activity

**Phase 4 Batch 12 — items 46–50**, scans **396–404 = 9/9**. There is no separate anthology structural scan inside the batch. Expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**; translate/review all five complete poems and leave Tamil archival files unchanged.""")

work_readme = f"{WORK}/README.md"
replace_required(work_readme,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.")
for old, new in [
    ("**IN PROGRESS — Batches 01–10 reviewed PASS.**", "**IN PROGRESS — Batches 01–11 reviewed PASS.**"),
    ("- reviewed batches: **10**;", "- reviewed batches: **11**;"),
    ("- reviewed items: **40/77**;", "- reviewed items: **45/77**;"),
    ("- reviewed item-assigned scans: **355/439**;", "- reviewed item-assigned scans: **370/439**;"),
]:
    replace_required(work_readme, old, new)
replace_tail(work_readme, "## Next activity", """## Next activity

**Phase 4 Batch 12 — items 46–50**, scans **396–404 = 9/9**. There is no separate anthology structural scan inside the batch. Expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**; review all five complete final-cleared items before advancing.""")

source_intake = f"{WORK}/SOURCE_INTAKE.md"
replace_required(source_intake,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.")
replace_required(source_intake,
    "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–10 are reviewed PASS; Batch 11 items 41–45 are next.",
    "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–11 are reviewed PASS; Batch 12 items 46–50 are next.")
for old, new in [
    ("- Batches 01–10: **reviewed PASS**;", "- Batches 01–11: **reviewed PASS**;"),
    ("- reviewed items: **40/77**;", "- reviewed items: **45/77**;"),
    ("- reviewed item scans: **355/439**;", "- reviewed item scans: **370/439**;"),
    ("- exact next: **Batch 11 items 41–45**, **15/15 item scans** across physical span **379–395**, with structural scans **392–393** excluded.", "- Batch 11 marker certification: **15/15 PASS**, with structural scans **392–393** excluded;\n- exact next: **Batch 12 items 46–50**, scans **396–404 = 9/9**."),
]:
    replace_required(source_intake, old, new)

metadata = f"{WORK}/metadata/source.md"
replace_required(metadata,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.")
for old, new in [
    ("- reviewed batches: **10**;", "- reviewed batches: **11**;"),
    ("- reviewed English items: **40/77**;", "- reviewed English items: **45/77**;"),
    ("- reviewed item scans: **355/439**;", "- reviewed item scans: **370/439**;"),
    ("- next translation batch: **items 41–45**, **15/15 item scans** across physical span **379–395**, preserving structural scans **392–393** outside poem translations.", "- Batch 11 review: `../translations/en/batches/batch-11.md`;\n- Batch 11 marker certification: **15/15 PASS**, structural scans **392–393** excluded;\n- next translation batch: **items 46–50**, scans **396–404 = 9/9**."),
]:
    replace_required(metadata, old, new)

pmap = f"{WORK}/indexes/page-map.md"
replace_required(pmap,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**;",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**;")
replace_required(pmap,
    "Phase 4 Batches 01–10 reviewed items **1–40** across **355/439** item-assigned scans. Batch 10 certifies **44/44** item-owned scan markers across physical span **333–378**, with structural **372–373** excluded. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 11 items **41–45**, **15/15 item scans** across physical span **379–395**, with structural **392–393** excluded.",
    "Phase 4 Batches 01–11 reviewed items **1–45** across **370/439** item-assigned scans. Batch 11 certifies **15/15** item-owned scan markers across physical span **379–395**, with structural **392–393** excluded. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 12 items **46–50**, scans **396–404 = 9/9**.")

clearance = f"{WORK}/PHASE3_TAMIL_FINAL_CLEARANCE.md"
replace_required(clearance,
    "Phase 4 has subsequently advanced through **Batches 01–10, all reviewed PASS**. Reviewed English now covers items **1–40/77** and **355/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Batch 10 preserves structural scans **372–373** outside poem translations. Exact next translation activity: **Batch 11 items 41–45**, **15/15 item scans** across physical span **379–395**, preserving structural scans **392–393** outside poem translations.",
    "Phase 4 has subsequently advanced through **Batches 01–11, all reviewed PASS**. Reviewed English now covers items **1–45/77** and **370/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Batch 11 preserves structural scans **392–393** outside poem translations. Exact next translation activity: **Batch 12 items 46–50**, scans **396–404 = 9/9**.")

# 7) Phase plan.
phase = "TRANSCRIPTION_PHASE_PLAN.md"
for old, new in [
    ("**IN PROGRESS — Batches 01–10 reviewed PASS.**", "**IN PROGRESS — Batches 01–11 reviewed PASS.**"),
    ("- reviewed batches: **10**;", "- reviewed batches: **11**;"),
    ("- reviewed English items: **40/77**;", "- reviewed English items: **45/77**;"),
    ("- reviewed item-assigned source scans: **355/439**;", "- reviewed item-assigned source scans: **370/439**;"),
    ("- Batch 11: items 41–45, **15/15 item-owned scans**, structural **392–393** excluded, **NEXT**.", "- Batch 11: items 41–45, **15/15 item-owned scans**, structural **392–393** excluded, **reviewed PASS**;\n- Batch 12: items 46–50, scans **396–404 = 9/9**, **NEXT**."),
]:
    replace_required(phase, old, new)
replace_tail(phase, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 12 — items 46–50**, scans **396–404 = 9/9**. There is no separate anthology structural scan inside the batch. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**. Do not alter Tamil final-cleared files.""")

# 8) Handover and next-chat prompt.
handover = "HANDOVER.md"
replace_required(handover, "## Durable state after Phase 4 Batch 10", "## Durable state after Phase 4 Batch 11")
replace_required(handover,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item-assigned scans; Batch 11 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item-assigned scans; Batch 12 NEXT**.")
if "## Phase 4 durable result — Batch 11" not in read(handover):
    insert_before(handover, "## Supplied-transcription rule", """## Phase 4 durable result — Batch 11

- standing user cadence: **five poems per iteration**;
- reviewed batches: **11**;
- reviewed English items: **45/77**;
- reviewed item-assigned source scans: **370/439**;
- Batch 11 items: **41–45**;
- Batch 11 item-owned scans: **15/15** across physical span **379–395**;
- structural scans **392–393 (`மலர்த் தோட்டம்`)** remain outside poem translations;
- item 41 → **We Move as Your Shadow!**;
- item 42 → **Long Live Jeeva**;
- item 43 → **The Fallen Hero**;
- item 44 → **My Dear Friend! Why Did You Leave?**;
- item 45 → **Today Is Your Birthday**;
- marker certification: **15/15 PASS**;
- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes during Batch 11: **0**;
- Tamil `sections/` changes during Batch 11: **0**.

Batch review: `translations/en/batches/batch-11.md`.""")
replace_required(handover,
    "22. the latest reviewed translation batch record (`translations/en/batches/batch-10.md`).",
    "22. the latest reviewed translation batch record (`translations/en/batches/batch-11.md`).")
replace_tail(handover, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 12 — items 46–50 (`அவன் பிறந்தநாள் என ஒன்றில்லை!`, `அருமருந்தே! அன்பழக உடன்பிறப்பே!`, `பகுத்தறிவுப் பாண்டியனார்!`, `நியாயத் தராசு`, `ஏற்பாரோ?`)**. Read final-cleared `sections/46.md` through `sections/50.md` completely. Review all five complete items together across scans **396–404 = 9/9**; there is no separate anthology structural scan inside the batch. Expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**. Leave all Tamil source/page/canonical files unchanged.""")

nextp = "NEXT_CHAT_PROMPT.md"
replace_required(nextp,
    "- Phase 4 English translation/release **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**.",
    "- Phase 4 English translation/release **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.")
if "## Phase 4 Batch 11 durable result" not in read(nextp):
    insert_before(nextp, "## EXACT NEXT ACTIVITY", """## Phase 4 Batch 11 durable result

- standing cadence: **five poems per iteration**;
- Batches 01–11 **reviewed PASS**;
- reviewed items **45/77**;
- reviewed item scans **370/439**;
- Batch 11 items 41–45, **15/15 item-owned scans** across physical span **379–395**;
- structural scans **392–393 (`மலர்த் தோட்டம்`)** excluded from poem translations;
- title witnesses **2 exact / 3 authorised variants / 0 unresolved**;
- unresolved translation issues **0**;
- Tamil page/canonical changes **0**.""")
replace_tail(nextp, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 12 — items 46–50**, physical span **396–404**, with **9/9 item-owned scans**. There is no separate anthology structural scan inside the batch. Preserve the authorised contents/canonical title variants for items 46, 47 and 48 separately; items 49–50 are exact. Review together and do not alter Tamil `pages/` or `sections/`.""")

# 9) Guard against Tamil archival changes and unexpected scope.
changed = subprocess.check_output(["git", "diff", "--name-only", BASE, "--"], text=True).splitlines()
blocked = [p for p in changed if p.startswith(f"{WORK}/pages/") or p.startswith(f"{WORK}/sections/")]
if blocked:
    raise SystemExit(f"Tamil source/canonical files changed unexpectedly: {blocked}")

allowed_prefixes = [f"{EN}/"]
allowed_exact = {
    "HANDOVER.md", "NEXT_CHAT_PROMPT.md", "README.md", "TRANSCRIPTION_PHASE_PLAN.md",
    f"{WORK}/README.md", f"{WORK}/SOURCE_INTAKE.md", f"{WORK}/audit.md",
    f"{WORK}/indexes/page-map.md", f"{WORK}/metadata/source.md",
    f"{WORK}/PHASE3_TAMIL_FINAL_CLEARANCE.md",
    ".github/workflows/phase4-batch11-finalize.yml",
    "scripts/finalize-kalaignarin-kavithaigal-batch11.py",
}
unexpected = [p for p in changed if p not in allowed_exact and not any(p.startswith(pref) for pref in allowed_prefixes)]
if unexpected:
    raise SystemExit(f"unexpected Batch 11 changed paths: {unexpected}")

print("Batch 11 certification/status synchronization PASS")
