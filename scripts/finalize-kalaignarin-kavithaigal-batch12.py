from pathlib import Path
import re
import subprocess

BASE = "04f1aec2b75e13a995cd71416f3b6ac6f6bbefad"
ROOT = Path(".")
WORK = "poems/kalaignarin-kavithaigal"
EN = f"{WORK}/translations/en"

items = {
    f"{EN}/items/46-no-one-day-called-his-birthday-en.md": (46, [396, 397], "variant"),
    f"{EN}/items/47-precious-remedy-anbazhaga-beloved-sibling-en.md": (47, [398, 399], "variant"),
    f"{EN}/items/48-rationalist-pandianar-en.md": (48, [400, 401, 402], "variant"),
    f"{EN}/items/49-scales-of-justice-en.md": (49, [403], "exact"),
    f"{EN}/items/50-would-they-accept-en.md": (50, [404], "exact"),
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


# 1) Mechanical certification and status promotion.
marker_total = 0
exact_count = 0
variant_count = 0
for path, (item, expected, witness_kind) in items.items():
    text = read(path)
    markers = [int(x) for x in re.findall(r"<!-- scan (\d+) -->", text)]
    if markers != expected:
        raise SystemExit(f"marker mismatch {path}: {markers} != {expected}")
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

if marker_total != 9:
    raise SystemExit(f"Batch 12 marker total {marker_total} != 9")
if (exact_count, variant_count) != (2, 3):
    raise SystemExit(f"title witness count mismatch exact={exact_count} variant={variant_count}")

batch = f"{EN}/batches/batch-12.md"
replace_required(batch, "**REVIEWED — PASS, pending mechanical promotion/certification.**", "**REVIEWED — PASS.**")
batch_text = read(batch)
if "## Certification result" not in batch_text:
    batch_text += """

## Certification result

- exact scan-marker sequences: **9/9 PASS**;
- item identities: **5/5 PASS**;
- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes: **0**;
- Tamil `sections/` changes: **0**.
"""
    write(batch, batch_text)

# 2) Translation plan current frontier.
plan = f"{EN}/TRANSLATION_PLAN.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–11 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–12 reviewed PASS.**"),
    ("- batches: **11**;", "- batches: **12**;"),
    ("- items: **45/77**;", "- items: **50/77**;"),
    ("- item-assigned source scans: **370/439**;", "- item-assigned source scans: **379/439**;"),
    ("| 12 | 46–50 | 396–404 | **NEXT** |", "| 12 | 46–50 | 396–404 | **reviewed — PASS** |\n| 13 | 51–55 | 405–409 | **NEXT** |"),
    ("| later | 51–77 | five complete items per iteration (final remainder excepted) | pending |", "| later | 56–77 | five complete items per iteration (final remainder excepted) | pending |"),
]:
    replace_required(plan, old, new)
if "## Batch 12 decision record" not in read(plan):
    insert_before(plan, "## Exact next activity", """## Batch 12 decision record

Batch 12 reviewed complete items **46–50** across scans **396–404 = 9/9**. There is no separate anthology structural scan inside the batch. Title witnesses are **2 exact + 3 authorised variants**. The reviewed translations preserve Anna's every-day-is-birthday paradox and source-visible broken brooding-hen join; the `அன்பழக` Anbazhaga address and sixtieth-jubilee movement imagery; Soundarapandian rationalist biography and `சவுந்தரம்` / `அய்யப்பன்–பொய்யப்பா` wordplay; the 1945 widow-remarriage double-standard poem; and the 1945 Puranic/chastity satire without devotional harmonisation. Tamil `pages/`/`sections/` changes remain **0**.""")
replace_tail(plan, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 13 — items 51–55**: `புயல் என அறிக!`, `கேட்டுண்டோ?`, `வருணமா? மரணமா?`, `தோல்வி எப்பொழுது?`, `இன்றுமா கூச்சல்?`. Process all five complete poems across scans **405–409 = 5/5**. There is no separate anthology structural scan inside this batch. Expected title witnesses: **4 exact / 1 authorised variant / 0 unresolved**. Leave Tamil `pages/` and `sections/` unchanged.""")

# 3) Translation source map.
smap = f"{EN}/SOURCE_MAP.md"
rows = """| 46 | `அவன் பிறந்தநாள் என ஒன்றில்லை!` | `அவன் பிறந்தநாள் ஏன் ஒன்றில்லை!` | **There Is No One Day Called His Birthday!** | 396–397 | 379–380 | `items/46-no-one-day-called-his-birthday-en.md` | **batch-reviewed — PASS** |
| 47 | `அருமருந்தே! அன்பழக உடன்பிறப்பே!` | `அருமருந்தே! அன்புறவு உடன்பிறப்பே!` | **Precious Remedy! Anbazhaga, Beloved Sibling!** | 398–399 | 381–382 | `items/47-precious-remedy-anbazhaga-beloved-sibling-en.md` | **batch-reviewed — PASS** |
| 48 | `பகுத்தறிவுப் பாண்டியனார்!` | `பகுத்தறிவுப் பாண்டியனார்` | **Rationalist Pandianar!** | 400–402 | 383–385 | `items/48-rationalist-pandianar-en.md` | **batch-reviewed — PASS** |
| 49 | `நியாயத் தராசு` | `நியாயத் தராசு` | **The Scales of Justice** | 403 | 386 | `items/49-scales-of-justice-en.md` | **batch-reviewed — PASS** |
| 50 | `ஏற்பாரோ?` | `ஏற்பாரோ?` | **Would They Accept?** | 404 | 387 | `items/50-would-they-accept-en.md` | **batch-reviewed — PASS** |"""
smap_text = read(smap)
if "| 46 | `அவன் பிறந்தநாள் என ஒன்றில்லை!`" not in smap_text:
    lines = smap_text.splitlines()
    pos = next((i + 1 for i, line in enumerate(lines) if line.startswith("| 45 |")), None)
    if pos is None:
        raise SystemExit("SOURCE_MAP item45 row missing")
    lines[pos:pos] = rows.splitlines()
    write(smap, "\n".join(lines) + "\n")
for old, new in [
    ("- reviewed English batches: **11**;", "- reviewed English batches: **12**;"),
    ("- reviewed English items: **45/77**;", "- reviewed English items: **50/77**;"),
    ("- reviewed item-assigned scans: **370/439**;", "- reviewed item-assigned scans: **379/439**;"),
]:
    replace_required(smap, old, new)
if "### Items 46–50 provenance notes" not in read(smap):
    insert_before(smap, "## Exact next mapping activity", """### Items 46–50 provenance notes

- item 46 owns scans **396–397** (**2/2** represented), with authorised canonical `என` / contents `ஏன்` title variation;
- item 47 owns scans **398–399** (**2/2** represented), with authorised canonical `அன்பழக` / contents `அன்புறவு` title variation;
- item 48 owns scans **400–402** (**3/3** represented), with an authorised terminal-punctuation title variant;
- item 49 owns scan **403** (**1/1** represented), exact title witness;
- item 50 owns scan **404** (**1/1** represented), exact title witness;
- there is no separate anthology structural scan inside Batch 12;
- no Tamil page or canonical item was changed by Batch 12.""")
replace_tail(smap, "## Exact next mapping activity", """## Exact next mapping activity

Add reviewed mappings for **items 51–55** after Phase-4 Batch 13 passes. Batch 13 owns **5/5 item scans** across physical span **405–409** and contains no separate anthology structural scan. Expected title witnesses: **4 exact / 1 authorised variant / 0 unresolved**.""")

# 4) Translation README.
tread = f"{EN}/README.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–11 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–12 reviewed PASS.**"),
    ("- reviewed English batches: **11**;", "- reviewed English batches: **12**;"),
    ("- reviewed English items: **45/77**;", "- reviewed English items: **50/77**;"),
    ("- item-assigned source scans covered by reviewed English: **370/439**;", "- item-assigned source scans covered by reviewed English: **379/439**;"),
]:
    replace_required(tread, old, new)
tread_text = read(tread)
if "items/46-no-one-day-called-his-birthday-en.md" not in tread_text:
    needle = "- `items/45-today-is-your-birthday-en.md` — reviewed English item 45."
    addition = needle + "\n- `batches/batch-12.md` — reviewed Batch-12 record;\n- `items/46-no-one-day-called-his-birthday-en.md` — reviewed English item 46;\n- `items/47-precious-remedy-anbazhaga-beloved-sibling-en.md` — reviewed English item 47;\n- `items/48-rationalist-pandianar-en.md` — reviewed English item 48;\n- `items/49-scales-of-justice-en.md` — reviewed English item 49;\n- `items/50-would-they-accept-en.md` — reviewed English item 50."
    if needle not in tread_text:
        raise SystemExit("translation README item45 line missing")
    write(tread, tread_text.replace(needle, addition, 1))
if "## Batch 12" not in read(tread):
    insert_before(tread, "## Exact next activity", """## Batch 12

**Reviewed — PASS.**

Standing five-poem iteration covering items **46–50** across scans **396–404 = 9/9**. There is no separate anthology structural scan inside the batch.

- item 46 → **There Is No One Day Called His Birthday!**, scans **396–397**;
- item 47 → **Precious Remedy! Anbazhaga, Beloved Sibling!**, scans **398–399**;
- item 48 → **Rationalist Pandianar!**, scans **400–402**;
- item 49 → **The Scales of Justice**, scan **403**;
- item 50 → **Would They Accept?**, scan **404**;
- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;
- unresolved translation issues: **0**;
- Tamil changes: **0**.""")
replace_tail(tread, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 13 — items 51–55**, scans **405–409 = 5/5**. There is no separate anthology structural scan inside the batch. Expected title witnesses: **4 exact / 1 authorised variant / 0 unresolved**.""")

# 5) Work audit.
audit = f"{WORK}/audit.md"
replace_tail(audit, "### Exact next Phase-4 activity", """## Phase 4 Batch 12 audit — REVIEWED / PASS

Scope: English translation/review of final-cleared canonical items **46–50**.

- items after Batch 12: **50/77**;
- Batch-12 item-owned scans: **9/9 — scans 396–404**;
- cumulative reviewed item-owned scans: **379/439**;
- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;
- exact English scan-marker sequences: **9/9 PASS**;
- omission/duplication issues: **0**;
- unresolved reviewed translation issues: **0**;
- Tamil page-record changes: **0**;
- Tamil canonical-item changes: **0**;
- batch evidence: `translations/en/batches/batch-12.md`.

### Exact next Phase-4 activity

**Batch 13 — items 51–55**, scans **405–409 = 5/5**. There is no separate anthology structural scan inside the batch; expected title witnesses **4 exact / 1 authorised variant / 0 unresolved**.""")

# 6) Root/work status docs.
root_readme = "README.md"
replace_required(root_readme,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.")
replace_required(root_readme,
    "Batches 01–11 now cover items **1–45**. The reviewed English layer covers **45/77 items** and **370/439 item-assigned source scans** with **0** unresolved reviewed translation issues.",
    "Batches 01–12 now cover items **1–50**. The reviewed English layer covers **50/77 items** and **379/439 item-assigned source scans** with **0** unresolved reviewed translation issues.")
replace_tail(root_readme, "## Next activity", """## Next activity

**Phase 4 Batch 13 — items 51–55**, scans **405–409 = 5/5**. There is no separate anthology structural scan inside the batch. Expected title witnesses **4 exact / 1 authorised variant / 0 unresolved**; translate/review all five complete poems and leave Tamil archival files unchanged.""")

work_readme = f"{WORK}/README.md"
replace_required(work_readme,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.")
for old, new in [
    ("**IN PROGRESS — Batches 01–11 reviewed PASS.**", "**IN PROGRESS — Batches 01–12 reviewed PASS.**"),
    ("- reviewed batches: **11**;", "- reviewed batches: **12**;"),
    ("- reviewed items: **45/77**;", "- reviewed items: **50/77**;"),
    ("- reviewed item-assigned scans: **370/439**;", "- reviewed item-assigned scans: **379/439**;"),
]:
    replace_required(work_readme, old, new)
replace_tail(work_readme, "## Next activity", """## Next activity

**Phase 4 Batch 13 — items 51–55**, scans **405–409 = 5/5**. There is no separate anthology structural scan inside the batch. Expected title witnesses **4 exact / 1 authorised variant / 0 unresolved**; review all five complete final-cleared items before advancing.""")

source_intake = f"{WORK}/SOURCE_INTAKE.md"
replace_required(source_intake,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.")
replace_required(source_intake,
    "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–11 are reviewed PASS; Batch 12 items 46–50 are next.",
    "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–12 are reviewed PASS; Batch 13 items 51–55 are next.")
for old, new in [
    ("- Batches 01–11: **reviewed PASS**;", "- Batches 01–12: **reviewed PASS**;"),
    ("- reviewed items: **45/77**;", "- reviewed items: **50/77**;"),
    ("- reviewed item scans: **370/439**;", "- reviewed item scans: **379/439**;"),
    ("- exact next: **Batch 12 items 46–50**, scans **396–404 = 9/9**.", "- Batch 12 marker certification: **9/9 PASS**;\n- exact next: **Batch 13 items 51–55**, scans **405–409 = 5/5**."),
]:
    replace_required(source_intake, old, new)

metadata = f"{WORK}/metadata/source.md"
replace_required(metadata,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.")
for old, new in [
    ("- reviewed batches: **11**;", "- reviewed batches: **12**;"),
    ("- reviewed English items: **45/77**;", "- reviewed English items: **50/77**;"),
    ("- reviewed item scans: **370/439**;", "- reviewed item scans: **379/439**;"),
    ("- next translation batch: **items 46–50**, scans **396–404 = 9/9**.", "- Batch 12 review: `../translations/en/batches/batch-12.md`;\n- Batch 12 marker certification: **9/9 PASS**;\n- next translation batch: **items 51–55**, scans **405–409 = 5/5**."),
]:
    replace_required(metadata, old, new)

pmap = f"{WORK}/indexes/page-map.md"
replace_required(pmap,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**;",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**;")
replace_required(pmap,
    "Phase 4 Batches 01–11 reviewed items **1–45** across **370/439** item-assigned scans. Batch 11 certifies **15/15** item-owned scan markers across physical span **379–395**, with structural **392–393** excluded. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 12 items **46–50**, scans **396–404 = 9/9**.",
    "Phase 4 Batches 01–12 reviewed items **1–50** across **379/439** item-assigned scans. Batch 12 certifies **9/9** item-owned scan markers across physical span **396–404**. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 13 items **51–55**, scans **405–409 = 5/5**.")

clearance = f"{WORK}/PHASE3_TAMIL_FINAL_CLEARANCE.md"
replace_required(clearance,
    "Phase 4 has subsequently advanced through **Batches 01–11, all reviewed PASS**. Reviewed English now covers items **1–45/77** and **370/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Batch 11 preserves structural scans **392–393** outside poem translations. Exact next translation activity: **Batch 12 items 46–50**, scans **396–404 = 9/9**.",
    "Phase 4 has subsequently advanced through **Batches 01–12, all reviewed PASS**. Reviewed English now covers items **1–50/77** and **379/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Batch 12 certifies scans **396–404 = 9/9**. Exact next translation activity: **Batch 13 items 51–55**, scans **405–409 = 5/5**.")

# 7) Phase plan.
phase = "TRANSCRIPTION_PHASE_PLAN.md"
for old, new in [
    ("**IN PROGRESS — Batches 01–11 reviewed PASS.**", "**IN PROGRESS — Batches 01–12 reviewed PASS.**"),
    ("- reviewed batches: **11**;", "- reviewed batches: **12**;"),
    ("- reviewed English items: **45/77**;", "- reviewed English items: **50/77**;"),
    ("- reviewed item-assigned source scans: **370/439**;", "- reviewed item-assigned source scans: **379/439**;"),
    ("- Batch 12: items 46–50, scans **396–404 = 9/9**, **NEXT**.", "- Batch 12: items 46–50, scans **396–404 = 9/9**, **reviewed PASS**;\n- Batch 13: items 51–55, scans **405–409 = 5/5**, **NEXT**."),
]:
    replace_required(phase, old, new)
replace_tail(phase, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 13 — items 51–55**, scans **405–409 = 5/5**. There is no separate anthology structural scan inside the batch. Expected title witnesses: **4 exact / 1 authorised variant / 0 unresolved**. Do not alter Tamil final-cleared files.""")

# 8) Handover and next-chat prompt.
handover = "HANDOVER.md"
replace_required(handover, "## Durable state after Phase 4 Batch 11", "## Durable state after Phase 4 Batch 12")
replace_required(handover,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item-assigned scans; Batch 12 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item-assigned scans; Batch 13 NEXT**.")
if "## Phase 4 durable result — Batch 12" not in read(handover):
    insert_before(handover, "## Supplied-transcription rule", """## Phase 4 durable result — Batch 12

- standing user cadence: **five poems per iteration**;
- reviewed batches: **12**;
- reviewed English items: **50/77**;
- reviewed item-assigned source scans: **379/439**;
- Batch 12 items: **46–50**;
- Batch 12 item-owned scans: **396–404 = 9/9**;
- there is no separate anthology structural scan inside Batch 12;
- item 46 → **There Is No One Day Called His Birthday!**;
- item 47 → **Precious Remedy! Anbazhaga, Beloved Sibling!**;
- item 48 → **Rationalist Pandianar!**;
- item 49 → **The Scales of Justice**;
- item 50 → **Would They Accept?**;
- marker certification: **9/9 PASS**;
- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes during Batch 12: **0**;
- Tamil `sections/` changes during Batch 12: **0**.

Batch review: `translations/en/batches/batch-12.md`.""")
replace_required(handover,
    "22. the latest reviewed translation batch record (`translations/en/batches/batch-11.md`).",
    "22. the latest reviewed translation batch record (`translations/en/batches/batch-12.md`).")
replace_tail(handover, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 13 — items 51–55 (`புயல் என அறிக!`, `கேட்டுண்டோ?`, `வருணமா? மரணமா?`, `தோல்வி எப்பொழுது?`, `இன்றுமா கூச்சல்?`)**. Read final-cleared `sections/51.md` through `sections/55.md` completely. Review all five complete items together across scans **405–409 = 5/5**; there is no separate anthology structural scan inside the batch. Expected title witnesses **4 exact / 1 authorised variant / 0 unresolved**. Leave all Tamil source/page/canonical files unchanged.""")

nextp = "NEXT_CHAT_PROMPT.md"
replace_required(nextp,
    "- Phase 4 English translation/release **IN PROGRESS — Batches 01–11 reviewed PASS; 45/77 items; 370/439 item scans; Batch 12 NEXT**.",
    "- Phase 4 English translation/release **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.")
if "## Phase 4 Batch 12 durable result" not in read(nextp):
    insert_before(nextp, "## EXACT NEXT ACTIVITY", """## Phase 4 Batch 12 durable result

- standing cadence: **five poems per iteration**;
- Batches 01–12 **reviewed PASS**;
- reviewed items **50/77**;
- reviewed item scans **379/439**;
- Batch 12 items 46–50, scans **396–404 = 9/9**;
- no separate anthology structural scan occurs inside Batch 12;
- title witnesses **2 exact / 3 authorised variants / 0 unresolved**;
- unresolved translation issues **0**;
- Tamil page/canonical changes **0**.""")
replace_tail(nextp, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 13 — items 51–55**, physical span **405–409**, with **5/5 item-owned scans**. There is no separate anthology structural scan inside the batch. Preserve the authorised terminal-punctuation title variant for item 51 separately; items 52–55 are exact. Review together and do not alter Tamil `pages/` or `sections/`.""")

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
    ".github/workflows/phase4-batch12-finalize.yml",
    "scripts/finalize-kalaignarin-kavithaigal-batch12.py",
}
unexpected = [p for p in changed if p not in allowed_exact and not any(p.startswith(pref) for pref in allowed_prefixes)]
if unexpected:
    raise SystemExit(f"unexpected Batch 12 changed paths: {unexpected}")

print("Batch 12 certification/status synchronization PASS")
