from pathlib import Path
import re
import subprocess

BASE = "85bb0f36c5ae5844bf973e3803e0bda4f081d66c"
ROOT = Path(".")
WORK = "poems/kalaignarin-kavithaigal"
EN = f"{WORK}/translations/en"

items = {
    f"{EN}/items/36-chithirai-festival-presiding-poem-en.md": (36, list(range(333, 346)), "variant"),
    f"{EN}/items/37-three-letters-thoughts-three-times-three-en.md": (37, list(range(346, 362)), "variant"),
    f"{EN}/items/38-on-arignar-annas-path-en.md": (38, list(range(362, 372)), "exact"),
    f"{EN}/items/39-panneerselvam-en.md": (39, list(range(374, 376)), "variant"),
    f"{EN}/items/40-mother-arts-foremost-son-en.md": (40, list(range(376, 379)), "variant"),
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


# 1) Mechanical certification and status promotion.
marker_total = 0
variant_count = 0
exact_count = 0
for path, (item, expected, witness_kind) in items.items():
    text = read(path)
    markers = [int(x) for x in re.findall(r"<!-- scan (\d+) -->", text)]
    if markers != expected:
        raise SystemExit(f"marker mismatch {path}: {markers} != {expected}")
    if 372 in markers or 373 in markers:
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
    text = text.replace('status: "review-pending"', 'status: "batch-reviewed"', 1)
    write(path, text)
    marker_total += len(markers)

if marker_total != 44:
    raise SystemExit(f"Batch 10 marker total {marker_total} != 44")
if (exact_count, variant_count) != (1, 4):
    raise SystemExit(f"title witness count mismatch exact={exact_count} variant={variant_count}")

batch = f"{EN}/batches/batch-10.md"
batch_text = read(batch)
if "## Certification result" not in batch_text:
    batch_text += """

## Certification result

- exact scan-marker sequences: **44/44 PASS**;
- item identities: **5/5 PASS**;
- structural scans **372–373** excluded from all five English item files: **PASS**;
- title witnesses: **1 exact / 4 authorised variants / 0 unresolved**;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes: **0**;
- Tamil `sections/` changes: **0**.
"""
    write(batch, batch_text)

# 2) Translation plan current frontier and decision record.
plan = f"{EN}/TRANSLATION_PLAN.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–09 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–10 reviewed PASS.**"),
    ("- batches: **9**;", "- batches: **10**;"),
    ("- items: **35/77**;", "- items: **40/77**;"),
    ("- item-assigned source scans: **311/439**;", "- item-assigned source scans: **355/439**;"),
    ("| 10 | 36–40 | 333–378 item-owned scans; structural 372–373 excluded | **NEXT** |", "| 10 | 36–40 | 333–378 item-owned scans; structural 372–373 excluded | **reviewed — PASS** |\n| 11 | 41–45 | 379–395 item-owned scans; structural 392–393 excluded | **NEXT** |"),
    ("| later | 41–77 | five complete items per iteration (final remainder excepted) | pending |", "| later | 46–77 | five complete items per iteration (final remainder excepted) | pending |"),
]:
    replace_required(plan, old, new)
if "## Batch 10 decision record" not in read(plan):
    insert_before(plan, "## Exact next activity", """## Batch 10 decision record

Batch 10 reviewed complete items **36–40** with **44/44 item-owned source scans** across physical span **333–378**. Structural anthology scans **372–373 (`கண்ணீர்த் துளிகள்`)** remain outside poem translations. Title witnesses are **1 exact + 4 authorised variants**. The reviewed translations preserve the Chithirai/Tamil-month wordplay and 1990 welfare/common-ownership address; the three-letter/Mandal/reservation movement argument; the 1994 Anna-name/simile-strike and rationalist polemic; the youthful Panneerselvam Oman-Sea elegy; and the N. S. Krishnan laughter/film/reform elegy. Tamil `pages/`/`sections/` changes remain **0**.""")
replace_tail(plan, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 11 — items 41–45**: `உன் நிழலாக அசைகின்றோம்!`, `வாழ்க ஜீவா`, `மறைந்த மாவீரன்`, `என் இனிய நண்பா! ஏன் பிரிந்தாய்?`, `இன்றைக்கு உன்றன் பிறந்த நாள்`. Process all five complete poems with **15/15 item-owned scans** across physical span **379–395**, while structural scans **392–393 (`மலர்த் தோட்டம்`)** remain outside poem translations. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**. Leave Tamil `pages/` and `sections/` unchanged.""")

# 3) Translation source map.
smap = f"{EN}/SOURCE_MAP.md"
smap_text = read(smap)
rows = """| 36 | `\"சித்திரைத் திருநாள்\" தலைமைக் கவிதை!` | `“சித்திரைத் திருநாள்” தலைமைக் கவிதை` | **\"Chithirai Festival\" — Presiding Poem!** | 333–345 | 316–328 | `items/36-chithirai-festival-presiding-poem-en.md` | **batch-reviewed — PASS** |
| 37 | `எழுத்துக்கள் மூன்று - எண்ணங்கள் மும்மூன்று` | `“எழுத்துக்கள் மூன்று - எண்ணங்கள் மும்மூன்று”` | **Three Letters — Thoughts Three Times Three** | 346–361 | 329–344 | `items/37-three-letters-thoughts-three-times-three-en.md` | **batch-reviewed — PASS** |
| 38 | `“அறிஞர் அண்ணா வழியில்”` | `“அறிஞர் அண்ணா வழியில்”` | **“On Arignar Anna’s Path”** | 362–371 | 345–353 | `items/38-on-arignar-annas-path-en.md` | **batch-reviewed — PASS** |
| 39 | `பன்னீர்ச்செல்வமே!` | `பன்னீர்ச் செல்வமே` | **Panneerselvam!** | 374–375 | 357–358 | `items/39-panneerselvam-en.md` | **batch-reviewed — PASS** |
| 40 | `கலைத்தாயின் தலைச் செல்வன்!` | `கலைத்தாயின் தலைச்செல்வன்` | **Mother Art’s Foremost Son!** | 376–378 | 359–361 | `items/40-mother-arts-foremost-son-en.md` | **batch-reviewed — PASS** |"""
if "| 36 | `\"சித்திரைத் திருநாள்\"" not in smap_text:
    lines = smap_text.splitlines()
    pos = next((i + 1 for i, line in enumerate(lines) if line.startswith("| 35 |")), None)
    if pos is None:
        raise SystemExit("SOURCE_MAP item35 row missing")
    lines[pos:pos] = rows.splitlines()
    write(smap, "\n".join(lines) + "\n")
for old, new in [
    ("- reviewed English batches: **9**;", "- reviewed English batches: **10**;"),
    ("- reviewed English items: **35/77**;", "- reviewed English items: **40/77**;"),
    ("- reviewed item-assigned scans: **311/439**;", "- reviewed item-assigned scans: **355/439**;"),
]:
    replace_required(smap, old, new)
if "### Items 36–40 provenance notes" not in read(smap):
    insert_before(smap, "## Exact next mapping activity", """### Items 36–40 provenance notes

- item 36 owns scans **333–345** (**13/13** represented), with authorised quote-glyph/terminal-punctuation title variation;
- item 37 owns scans **346–361** (**16/16** represented), with contents-only quotation marks;
- item 38 owns scans **362–371** (**10/10** represented), exact title witness; scan **371** is the item-owned blank/show-through provenance leaf;
- structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** remain outside all English poem items;
- item 39 owns scans **374–375** (**2/2** represented), with authorised spacing/punctuation title variation;
- item 40 owns scans **376–378** (**3/3** represented), with authorised spacing/punctuation title variation;
- no Tamil page or canonical item was changed by Batch 10.""")
replace_tail(smap, "## Exact next mapping activity", """## Exact next mapping activity

Add reviewed mappings for **items 41–45** after Phase-4 Batch 11 passes. Batch 11 owns **15/15 item scans** across physical span **379–395**, while structural scans **392–393 (`மலர்த் தோட்டம்`)** remain outside poem items. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**.""")

# 4) Translation README.
tread = f"{EN}/README.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–09 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–10 reviewed PASS.**"),
    ("- reviewed English batches: **9**;", "- reviewed English batches: **10**;"),
    ("- reviewed English items: **35/77**;", "- reviewed English items: **40/77**;"),
    ("- item-assigned source scans covered by reviewed English: **311/439**;", "- item-assigned source scans covered by reviewed English: **355/439**;"),
]:
    replace_required(tread, old, new)
tread_text = read(tread)
if "items/36-chithirai-festival-presiding-poem-en.md" not in tread_text:
    needle = "- `items/35-kalaivanar-arangam-poetry-assembly-en.md` — reviewed English item 35."
    addition = needle + "\n- `batches/batch-10.md` — reviewed Batch-10 record;\n- `items/36-chithirai-festival-presiding-poem-en.md` — reviewed English item 36;\n- `items/37-three-letters-thoughts-three-times-three-en.md` — reviewed English item 37;\n- `items/38-on-arignar-annas-path-en.md` — reviewed English item 38;\n- `items/39-panneerselvam-en.md` — reviewed English item 39;\n- `items/40-mother-arts-foremost-son-en.md` — reviewed English item 40."
    if needle not in tread_text:
        raise SystemExit("translation README item35 line missing")
    write(tread, tread_text.replace(needle, addition, 1))
if "## Batch 10" not in read(tread):
    insert_before(tread, "## Exact next activity", """## Batch 10

**Reviewed — PASS.**

Standing five-poem iteration covering items **36–40** with **44/44 item-owned scans** across physical span **333–378**. Structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** remain outside poem bodies.

- item 36 → **\"Chithirai Festival\" — Presiding Poem!**, scans **333–345**;
- item 37 → **Three Letters — Thoughts Three Times Three**, scans **346–361**;
- item 38 → **“On Arignar Anna’s Path”**, scans **362–371**;
- item 39 → **Panneerselvam!**, scans **374–375**;
- item 40 → **Mother Art’s Foremost Son!**, scans **376–378**;
- title witnesses: **1 exact / 4 authorised variants / 0 unresolved**;
- unresolved translation issues: **0**;
- Tamil changes: **0**.""")
replace_tail(tread, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 11 — items 41–45**, with **15/15 item-owned scans** across physical span **379–395**. Keep structural scans **392–393 (`மலர்த் தோட்டம்`)** outside poem translations. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**.""")

# 5) HANDOVER: current frontier, new durable block, latest batch pointer, exact next.
hand = "HANDOVER.md"
replace_required(hand, "## Durable state after Phase 4 Batch 09", "## Durable state after Phase 4 Batch 10")
replace_required(hand, "Phase 4 English translation/release: **IN PROGRESS — Batches 01–09 reviewed PASS; 35/77 items; 311/439 item-assigned scans; Batch 10 NEXT**", "Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item-assigned scans; Batch 11 NEXT**")
if "## Phase 4 durable result — Batch 10" not in read(hand):
    insert_before(hand, "## Supplied-transcription rule", """## Phase 4 durable result — Batch 10

- standing user cadence: **five poems per iteration**;
- reviewed batches: **10**;
- reviewed English items: **40/77**;
- reviewed item-assigned source scans: **355/439**;
- Batch 10 items: **36–40**;
- Batch 10 item-owned scans: **44/44** across physical span **333–378**;
- structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** remain outside poem translations;
- item 36 → **\"Chithirai Festival\" — Presiding Poem!**;
- item 37 → **Three Letters — Thoughts Three Times Three**;
- item 38 → **“On Arignar Anna’s Path”**;
- item 39 → **Panneerselvam!**;
- item 40 → **Mother Art’s Foremost Son!**;
- marker certification: **44/44 PASS**;
- title witnesses: **1 exact / 4 authorised variants / 0 unresolved**;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes during Batch 10: **0**;
- Tamil `sections/` changes during Batch 10: **0**.

Batch review: `translations/en/batches/batch-10.md`.""")
replace_required(hand, "the latest reviewed translation batch record (`translations/en/batches/batch-09.md`)", "the latest reviewed translation batch record (`translations/en/batches/batch-10.md`)")
replace_tail(hand, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 11 — items 41–45 (`உன் நிழலாக அசைகின்றோம்!`, `வாழ்க ஜீவா`, `மறைந்த மாவீரன்`, `என் இனிய நண்பா! ஏன் பிரிந்தாய்?`, `இன்றைக்கு உன்றன் பிறந்த நாள்`)**. Read final-cleared `sections/41.md` through `sections/45.md` completely. Preserve structural scans **392–393 (`மலர்த் தோட்டம்`)** outside poem translations. Review all five complete items together; item-owned scan total **15/15** across physical span **379–395**; expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**. Leave all Tamil source/page/canonical files unchanged.""")

# 6) NEXT_CHAT_PROMPT current frontier and next batch.
prompt = "NEXT_CHAT_PROMPT.md"
replace_required(prompt, "Phase 4 English translation/release **IN PROGRESS — Batches 01–09 reviewed PASS; 35/77 items; 311/439 item scans; Batch 10 NEXT**", "Phase 4 English translation/release **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**")
# Correct one known historical heading typo without changing its historical counters.
replace_if_present(prompt, "## Phase 4 Batch 08 durable result\n\n- standing cadence: **five poems per iteration**;\n- Batches 01–09 **reviewed PASS**;", "## Phase 4 Batch 08 durable result\n\n- standing cadence: **five poems per iteration**;\n- Batches 01–08 **reviewed PASS**;")
if "## Phase 4 Batch 10 durable result" not in read(prompt):
    insert_before(prompt, "## EXACT NEXT ACTIVITY", """## Phase 4 Batch 10 durable result

- standing cadence: **five poems per iteration**;
- Batches 01–10 **reviewed PASS**;
- reviewed items **40/77**;
- reviewed item scans **355/439**;
- Batch 10 items 36–40, **44/44 item-owned scans**;
- structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** excluded from poem translations;
- title witnesses **1 exact / 4 authorised variants / 0 unresolved**;
- unresolved translation issues **0**;
- Tamil page/canonical changes **0**.""")
replace_tail(prompt, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 11 — items 41–45**, physical span **379–395**, with **15/15 item-owned scans**. Structural scans **392–393 (`மலர்த் தோட்டம்`)** stay outside poem translations. Preserve the authorised contents/canonical title variants for items 41, 42 and 45 separately; items 43–44 are exact. Review together and do not alter Tamil `pages/` or `sections/`.""")

# 7) Root README: top status + stale lower Phase-4 summary/next activity.
rootread = "README.md"
replace_required(rootread, "Phase 4 English translation/release: **IN PROGRESS — Batches 01–09 reviewed PASS; 35/77 items; 311/439 item scans; Batch 10 NEXT**", "Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**")
replace_required(rootread, "Batches 01–08 now cover items **1–30**. The reviewed English layer covers **30/77 items** and **271/439 item-assigned source scans**", "Batches 01–10 now cover items **1–40**. The reviewed English layer covers **40/77 items** and **355/439 item-assigned source scans**")
replace_tail(rootread, "## Next activity", """## Next activity

**Phase 4 Batch 11 — items 41–45**, with **15/15 item-owned scans** across physical span **379–395**. Preserve structural scans **392–393 (`மலர்த் தோட்டம்`)** outside poem translations; expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**. Translate/review all five complete poems and leave Tamil archival files unchanged.""")

# 8) Phase plan: repair stale counters and advance current row.
phase = "TRANSCRIPTION_PHASE_PLAN.md"
replace_required(phase, "**IN PROGRESS — Batches 01–09 reviewed PASS.**", "**IN PROGRESS — Batches 01–10 reviewed PASS.**")
replace_required(phase, "- reviewed batches: **8**;", "- reviewed batches: **10**;")
replace_required(phase, "- reviewed English items: **30/77**;", "- reviewed English items: **40/77**;")
replace_required(phase, "- reviewed item-assigned source scans: **311/439**;", "- reviewed item-assigned source scans: **355/439**;")
replace_required(phase, "- Batch 09: items 31–35, scans **293–332 = 40/40**, **NEXT**.", "- Batch 09: items 31–35, scans **293–332 = 40/40**, **reviewed PASS**;\n- Batch 10: items 36–40, **44/44 item-owned scans**, structural **372–373** excluded, **reviewed PASS**;\n- Batch 11: items 41–45, **15/15 item-owned scans**, structural **392–393** excluded, **NEXT**.")
replace_tail(phase, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 11 — items 41–45**, with **15/15 item-owned scans** across physical span **379–395**. Preserve structural scans **392–393 (`மலர்த் தோட்டம்`)** outside poem translations. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**. Do not alter Tamil final-cleared files.""")

# 9) Active README.
active = f"{WORK}/README.md"
replace_required(active, "Phase 4 English translation/release: **IN PROGRESS — Batches 01–09 reviewed PASS; 35/77 items; 311/439 item scans; Batch 10 NEXT**", "Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**")
replace_required(active, "**IN PROGRESS — Batches 01–08 reviewed PASS.**", "**IN PROGRESS — Batches 01–10 reviewed PASS.**")
replace_required(active, "- reviewed batches: **8**;", "- reviewed batches: **10**;")
replace_required(active, "- reviewed items: **30/77**;", "- reviewed items: **40/77**;")
replace_required(active, "- reviewed item-assigned scans: **271/439**;", "- reviewed item-assigned scans: **355/439**;")
replace_tail(active, "## Next activity", """## Next activity

**Phase 4 Batch 11 — items 41–45**, with **15/15 item-owned scans** across physical span **379–395**. Preserve structural scans **392–393 (`மலர்த் தோட்டம்`)** outside poem translations. Expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**; review all five complete final-cleared items before advancing.""")

# 10) SOURCE_INTAKE stale lower Phase-4 state.
intake = f"{WORK}/SOURCE_INTAKE.md"
replace_required(intake, "Phase 4 English translation/release: **IN PROGRESS — Batches 01–09 reviewed PASS; 35/77 items; 311/439 item scans; Batch 10 NEXT**", "Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**")
replace_required(intake, "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–08 are reviewed PASS; Batch 09 items 31–35 are next.", "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–10 are reviewed PASS; Batch 11 items 41–45 are next.")
replace_required(intake, "- Batches 01–08: **reviewed PASS**;", "- Batches 01–10: **reviewed PASS**;")
replace_required(intake, "- reviewed items: **30/77**;", "- reviewed items: **40/77**;")
replace_required(intake, "- reviewed item scans: **271/439**;", "- reviewed item scans: **355/439**;")
replace_required(intake, "- exact next: **Batch 09 items 31–35**, scans **293–332 = 40/40**, with items 31–33 retaining authorised title variants.", "- Batch 09 marker certification: **40/40 PASS**;\n- Batch 10 marker certification: **44/44 PASS**, with structural scans **372–373** excluded;\n- exact next: **Batch 11 items 41–45**, **15/15 item scans** across physical span **379–395**, with structural scans **392–393** excluded.")

# 11) metadata/source lower Phase-4 metadata.
meta = f"{WORK}/metadata/source.md"
replace_required(meta, "Phase 4 English translation/release: **IN PROGRESS — Batches 01–09 reviewed PASS; 35/77 items; 311/439 item scans; Batch 10 NEXT**", "Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**")
replace_required(meta, "- reviewed batches: **8**;", "- reviewed batches: **10**;")
replace_required(meta, "- reviewed English items: **30/77**;", "- reviewed English items: **40/77**;")
replace_required(meta, "- reviewed item scans: **271/439**;", "- reviewed item scans: **355/439**;")
replace_required(meta, "- next translation batch: **items 31–35**, scans **293–332 = 40/40**, preserving authorised title variants for items 31–33.", "- Batch 09 review: `../translations/en/batches/batch-09.md`;\n- Batch 09 marker certification: **40/40 PASS**;\n- Batch 10 review: `../translations/en/batches/batch-10.md`;\n- Batch 10 marker certification: **44/44 PASS**, structural scans **372–373** excluded;\n- next translation batch: **items 41–45**, **15/15 item scans** across physical span **379–395**, preserving structural scans **392–393** outside poem translations.")

# 12) page-map current Phase-4 note.
pmap = f"{WORK}/indexes/page-map.md"
replace_required(pmap, "Phase 4 English translation/release: **IN PROGRESS — Batches 01–09 reviewed PASS; 35/77 items; 311/439 item scans; Batch 10 NEXT**", "Phase 4 English translation/release: **IN PROGRESS — Batches 01–10 reviewed PASS; 40/77 items; 355/439 item scans; Batch 11 NEXT**")
replace_required(pmap, "Phase 4 Batches 01–08 reviewed items **1–30** across **271/439** item-assigned scans. Batch 08 certifies **39/39** item-owned scan markers across **254–292**. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 09 items **31–35**, scans **293–332 = 40/40**.", "Phase 4 Batches 01–10 reviewed items **1–40** across **355/439** item-assigned scans. Batch 10 certifies **44/44** item-owned scan markers across physical span **333–378**, with structural **372–373** excluded. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 11 items **41–45**, **15/15 item scans** across physical span **379–395**, with structural **392–393** excluded.")

# 13) Phase-3 final clearance subsequent status note.
clear = f"{WORK}/PHASE3_TAMIL_FINAL_CLEARANCE.md"
replace_required(clear, "Phase 4 has subsequently advanced through **Batches 01–08, all reviewed PASS**. Reviewed English now covers items **1–30/77** and **311/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Exact next translation activity: **Batch 09 items 31–35**, scans **293–332 = 40/40**, preserving the authorised title-witness variants for items 31–33.", "Phase 4 has subsequently advanced through **Batches 01–10, all reviewed PASS**. Reviewed English now covers items **1–40/77** and **355/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Batch 10 preserves structural scans **372–373** outside poem translations. Exact next translation activity: **Batch 11 items 41–45**, **15/15 item scans** across physical span **379–395**, preserving structural scans **392–393** outside poem translations.")

# 14) Audit: replace final 'next Batch 10' tail with durable Batch 10 audit + Batch 11 next.
audit = f"{WORK}/audit.md"
replace_tail(audit, "### Exact next Phase-4 activity", """## Phase 4 Batch 10 audit — REVIEWED / PASS

Scope: English translation/review of final-cleared canonical items **36–40**.

- items after Batch 10: **40/77**;
- Batch-10 item-owned scans: **44/44** across physical span **333–378**;
- cumulative reviewed item-owned scans: **355/439**;
- structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** excluded from poem translations: **PASS**;
- title witnesses: **1 exact / 4 authorised variants / 0 unresolved**;
- exact English scan-marker sequences: **44/44 PASS**;
- omission/duplication issues: **0**;
- unresolved reviewed translation issues: **0**;
- Tamil page-record changes: **0**;
- Tamil canonical-item changes: **0**;
- batch evidence: `translations/en/batches/batch-10.md`.

### Exact next Phase-4 activity

**Batch 11 — items 41–45**, with **15/15 item-owned scans** across physical span **379–395**. Preserve structural scans **392–393 (`மலர்த் தோட்டம்`)** outside poem translations; expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**.""")

# 15) Scope guard: no Tamil page/canonical source files may have changed since pre-Batch10 checkpoint.
changed = subprocess.check_output(["git", "diff", "--name-only", BASE], text=True).splitlines()
for path in changed:
    if path.startswith(f"{WORK}/pages/") or path.startswith(f"{WORK}/sections/"):
        raise SystemExit(f"forbidden Tamil-layer change detected: {path}")

# Final in-worktree validation of counters and markers.
if "Batches 01–10 reviewed PASS; 40/77 items; 355/439 item-assigned scans; Batch 11 NEXT" not in read(hand):
    raise SystemExit("HANDOVER current frontier did not synchronize")
if "**PHASE 4 IN PROGRESS — Batches 01–10 reviewed PASS.**" not in read(plan):
    raise SystemExit("translation plan frontier did not synchronize")
if "- reviewed English items: **40/77**;" not in read(smap):
    raise SystemExit("source map progress did not synchronize")

print("Batch 10 certification and synchronization PASS")
print("markers=44/44; titles=1 exact + 4 variants; structural 372-373 excluded; Tamil pages/sections unchanged")
