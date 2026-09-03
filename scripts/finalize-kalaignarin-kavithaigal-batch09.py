from pathlib import Path
import re
import subprocess

BASE = "4da40284877295f7c78c4a3ac6cc7875907c3d34"
ROOT = Path(".")

items = {
    "poems/kalaignarin-kavithaigal/translations/en/items/31-i-shall-walk-on-our-ayya-and-annas-path-en.md": (31, list(range(293, 297))),
    "poems/kalaignarin-kavithaigal/translations/en/items/32-presiding-poem-three-great-celebrations-en.md": (32, list(range(297, 311))),
    "poems/kalaignarin-kavithaigal/translations/en/items/33-in-a-changing-town-en.md": (33, list(range(311, 318))),
    "poems/kalaignarin-kavithaigal/translations/en/items/34-views-of-society-en.md": (34, list(range(318, 329))),
    "poems/kalaignarin-kavithaigal/translations/en/items/35-kalaivanar-arangam-poetry-assembly-en.md": (35, list(range(329, 333))),
}

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")

def replace_first(path, old, new, required=False):
    text = read(path)
    if old not in text:
        if required:
            raise SystemExit(f"required text not found in {path}: {old}")
        return False
    write(path, text.replace(old, new, 1))
    return True

def replace_tail(path, heading, new_tail):
    text = read(path)
    idx = text.find(heading)
    if idx < 0:
        raise SystemExit(f"heading not found in {path}: {heading}")
    write(path, text[:idx] + new_tail.rstrip() + "\n")

# Mechanical item certification and promotion.
marker_total = 0
for path, (item, expected) in items.items():
    text = read(path)
    markers = [int(x) for x in re.findall(r"<!-- scan (\d+) -->", text)]
    if markers != expected:
        raise SystemExit(f"marker mismatch {path}: {markers} != {expected}")
    if f"item: {item}\n" not in text:
        raise SystemExit(f"item identity mismatch {path}")
    if 'status: "review-pending"' not in text:
        raise SystemExit(f"review-pending status missing {path}")
    text = text.replace('status: "review-pending"', 'status: "batch-reviewed"', 1)
    write(path, text)
    marker_total += len(markers)
if marker_total != 40:
    raise SystemExit(f"batch marker total {marker_total} != 40")

batch = "poems/kalaignarin-kavithaigal/translations/en/batches/batch-09.md"
replace_first(batch, "**REVIEWED — PASS, pending mechanical promotion/certification.**", "**REVIEWED — PASS.**", required=True)
text = read(batch)
if "## Certification result" not in text:
    text += "\n## Certification result\n\n- exact scan-marker sequences: **40/40 PASS**;\n- item identities: **5/5 PASS**;\n- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes: **0**;\n- Tamil `sections/` changes: **0**.\n"
write(batch, text)

# Translation plan.
plan = "poems/kalaignarin-kavithaigal/translations/en/TRANSLATION_PLAN.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–08 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–09 reviewed PASS.**"),
    ("- batches: **8**;", "- batches: **9**;"),
    ("- items: **30/77**;", "- items: **35/77**;"),
    ("- item-assigned source scans: **271/439**;", "- item-assigned source scans: **311/439**;"),
    ("| 09 | 31–35 | 293–332 | **NEXT** |", "| 09 | 31–35 | 293–332 | **reviewed — PASS** |\n| 10 | 36–40 | 333–378 item-owned scans; structural 372–373 excluded | **NEXT** |"),
    ("| later | 36–77 | five complete items per iteration (final remainder excepted) | pending |", "| later | 41–77 | five complete items per iteration (final remainder excepted) | pending |"),
]:
    replace_first(plan, old, new, required=True)
plan_text = read(plan)
if "## Batch 09 decision record" not in plan_text:
    marker = "## Exact next activity"
    idx = plan_text.find(marker)
    if idx < 0:
        raise SystemExit("translation-plan next heading missing")
    block = """## Batch 09 decision record\n\nBatch 09 reviewed complete items **31–35** across scans **293–332 = 40/40**. Title witnesses are **2 exact + 3 authorised variants**: item 31 terminal punctuation, item 32 `கவியரங்கம்` / `கவியரங்கத்` wording, and item 33 spacing. The reviewed translations preserve the seventy-first-birthday Periyar–Anna path vow; the long Three Great Celebrations Periyar/Anna/DMK rationalist and language-rights polemic; the Puducherry equality/labour/socialism sequence; the *Ananda Vikatan* Golden-Jubilee society satire; and the Kalaivanar Arangam politics-as-social-progress conclusion. Tamil `pages/`/`sections/` changes remain **0**.\n\n"""
    plan_text = plan_text[:idx] + block + plan_text[idx:]
    write(plan, plan_text)
replace_tail(plan, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 10 — items 36–40**: `\"சித்திரைத் திருநாள்\" தலைமைக் கவிதை!`, `எழுத்துக்கள் மூன்று - எண்ணங்கள் மும்மூன்று`, `“அறிஞர் அண்ணா வழியில்”`, `பன்னீர்ச்செல்வமே!`, `கலைத்தாயின் தலைச் செல்வன்!`. Process all five complete poems; preserve structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** outside translations. Batch-10 item-owned coverage is **44/44** across physical span **333–378**, with expected title witnesses **1 exact / 4 authorised variants / 0 unresolved**.""")

# Translation source map.
smap = "poems/kalaignarin-kavithaigal/translations/en/SOURCE_MAP.md"
rows = """| 31 | `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்!` | `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்` | **I Shall Walk on Our Ayya and Anna's Path!** | 293–296 | 276–279 | `items/31-i-shall-walk-on-our-ayya-and-annas-path-en.md` | **batch-reviewed — PASS** |
| 32 | `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை` | `முப்பெரும் விழாக் கவியரங்கத் தலைமைக் கவிதை` | **Presiding Poem at the Three Great Celebrations Poetry Assembly** | 297–310 | 280–293 | `items/32-presiding-poem-three-great-celebrations-en.md` | **batch-reviewed — PASS** |
| 33 | `மாறி வரும் ஊரினிலே` | `மாறிவரும் ஊரினிலே` | **In a Changing Town** | 311–317 | 294–300 | `items/33-in-a-changing-town-en.md` | **batch-reviewed — PASS** |
| 34 | `சமுதாயப் பார்வைகள்...!` | `சமுதாயப் பார்வைகள்...!` | **Views of Society...!** | 318–328 | 301–311 | `items/34-views-of-society-en.md` | **batch-reviewed — PASS** |
| 35 | `கலைவாணர் அரங்கக் கவியரங்கம்` | `கலைவாணர் அரங்கக் கவியரங்கம்` | **Kalaivanar Arangam Poetry Assembly** | 329–332 | 312–315 | `items/35-kalaivanar-arangam-poetry-assembly-en.md` | **batch-reviewed — PASS** |"""
smap_text = read(smap)
if "| 31 | `நடந்திடுவேன்" not in smap_text:
    lines = smap_text.splitlines()
    insert_at = None
    for i, line in enumerate(lines):
        if line.startswith("| 30 |"):
            insert_at = i + 1
            break
    if insert_at is None:
        raise SystemExit("item 30 row not found in source map")
    lines[insert_at:insert_at] = rows.splitlines()
    smap_text = "\n".join(lines) + "\n"
    write(smap, smap_text)
for old, new in [
    ("- reviewed English batches: **8**;", "- reviewed English batches: **9**;"),
    ("- reviewed English items: **30/77**;", "- reviewed English items: **35/77**;"),
    ("- reviewed item-assigned scans: **271/439**;", "- reviewed item-assigned scans: **311/439**;"),
]:
    replace_first(smap, old, new, required=True)
smap_text = read(smap)
if "### Items 31–35 provenance notes" not in smap_text:
    idx = smap_text.find("## Exact next mapping activity")
    if idx < 0:
        raise SystemExit("source-map next heading missing")
    notes = """### Items 31–35 provenance notes\n\n- item 31 owns scans **293–296** (**4/4** represented), with contents witness lacking the canonical terminal `!`;\n- item 32 owns scans **297–310** (**14/14** represented), with authorised `கவியரங்கம்` / `கவியரங்கத்` title variation;\n- item 33 owns scans **311–317** (**7/7** represented), with authorised `மாறி வரும்` / `மாறிவரும்` spacing variation;\n- item 34 owns scans **318–328** (**11/11** represented), exact title witness;\n- item 35 owns scans **329–332** (**4/4** represented), exact title witness;\n- there are no pure anthology structural scans inside Batch 09;\n- no Tamil page or canonical item was changed by Batch 09.\n\n"""
    smap_text = smap_text[:idx] + notes + smap_text[idx:]
    write(smap, smap_text)
replace_tail(smap, "## Exact next mapping activity", """## Exact next mapping activity

Add reviewed mappings for **items 36–40** after Phase-4 Batch 10 passes. Batch 10 owns **44/44 item scans** across physical span **333–378**, while structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** remain outside poem items. Expected title witnesses: **1 exact / 4 authorised variants / 0 unresolved**.""")

# Translation README.
tread = "poems/kalaignarin-kavithaigal/translations/en/README.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–08 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–09 reviewed PASS.**"),
    ("- reviewed English batches: **8**;", "- reviewed English batches: **9**;"),
    ("- reviewed English items: **30/77**;", "- reviewed English items: **35/77**;"),
    ("- item-assigned source scans covered by reviewed English: **271/439**;", "- item-assigned source scans covered by reviewed English: **311/439**;"),
]:
    replace_first(tread, old, new, required=True)
tread_text = read(tread)
if "items/31-i-shall-walk-on-our-ayya" not in tread_text:
    needle = "- `items/30-on-annas-path-en.md` — reviewed English item 30."
    addition = needle + "\n- `batches/batch-09.md` — reviewed Batch-09 record;\n- `items/31-i-shall-walk-on-our-ayya-and-annas-path-en.md` — reviewed English item 31;\n- `items/32-presiding-poem-three-great-celebrations-en.md` — reviewed English item 32;\n- `items/33-in-a-changing-town-en.md` — reviewed English item 33;\n- `items/34-views-of-society-en.md` — reviewed English item 34;\n- `items/35-kalaivanar-arangam-poetry-assembly-en.md` — reviewed English item 35."
    if needle not in tread_text:
        raise SystemExit("translation README item30 line missing")
    tread_text = tread_text.replace(needle, addition, 1)
    write(tread, tread_text)
if "## Batch 09" not in read(tread):
    text = read(tread)
    idx = text.find("## Exact next activity")
    block = """## Batch 09\n\n**Reviewed — PASS.**\n\nStanding five-poem iteration covering items **31–35** across scans **293–332 = 40/40**.\n\n- item 31 → **I Shall Walk on Our Ayya and Anna's Path!**, scans **293–296**;\n- item 32 → **Presiding Poem at the Three Great Celebrations Poetry Assembly**, scans **297–310**;\n- item 33 → **In a Changing Town**, scans **311–317**;\n- item 34 → **Views of Society...!**, scans **318–328**;\n- item 35 → **Kalaivanar Arangam Poetry Assembly**, scans **329–332**;\n- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;\n- unresolved translation issues: **0**;\n- Tamil changes: **0**.\n\n"""
    if idx < 0:
        raise SystemExit("translation README next heading missing")
    write(tread, text[:idx] + block + text[idx:])
replace_tail(tread, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 10 — items 36–40**, preserving structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** outside poem translations. Batch-10 item-owned coverage: **44/44** across physical span **333–378**; expected title witnesses **1 exact / 4 authorised variants / 0 unresolved**.""")

# Compact current-status synchronization in archival controls.
controls = [
    "README.md",
    "TRANSCRIPTION_PHASE_PLAN.md",
    "poems/kalaignarin-kavithaigal/README.md",
    "poems/kalaignarin-kavithaigal/SOURCE_INTAKE.md",
    "poems/kalaignarin-kavithaigal/metadata/source.md",
    "poems/kalaignarin-kavithaigal/indexes/page-map.md",
    "poems/kalaignarin-kavithaigal/PHASE3_TAMIL_FINAL_CLEARANCE.md",
]
for path in controls:
    for old, new in [
        ("Batches 01–08 reviewed PASS", "Batches 01–09 reviewed PASS"),
        ("30/77 items", "35/77 items"),
        ("271/439", "311/439"),
        ("Batch 09 NEXT", "Batch 10 NEXT"),
    ]:
        replace_first(path, old, new, required=False)

# Audit append.
audit = "poems/kalaignarin-kavithaigal/audit.md"
audit_text = read(audit)
if "## Phase 4 Batch 09 audit" not in audit_text:
    audit_text += """\n\n## Phase 4 Batch 09 audit — REVIEWED / PASS\n\nScope: English translation/review of final-cleared canonical items **31–35**.\n\n- items after Batch 09: **35/77**;\n- Batch-09 item-owned scans: **40/40 — scans 293–332**;\n- cumulative reviewed item-owned scans: **311/439**;\n- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;\n- exact English scan-marker sequences: **40/40 PASS**;\n- omission/duplication issues: **0**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page-record changes: **0**;\n- Tamil canonical-item changes: **0**;\n- batch evidence: `translations/en/batches/batch-09.md`.\n\n### Exact next Phase-4 activity\n\n**Batch 10 — items 36–40**; preserve structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** outside poem translations. Item-owned scan total **44/44** across physical span **333–378**.\n"""
    write(audit, audit_text)

# Handover.
handover = "HANDOVER.md"
replace_first(handover, "## Durable state after Phase 4 Batch 08", "## Durable state after Phase 4 Batch 09", required=True)
replace_first(handover, "Batches 01–08 reviewed PASS; 30/77 items; 271/439 item-assigned scans; Batch 09 NEXT", "Batches 01–09 reviewed PASS; 35/77 items; 311/439 item-assigned scans; Batch 10 NEXT", required=True)
replace_first(handover, "the latest reviewed translation batch record (`translations/en/batches/batch-08.md`).", "the latest reviewed translation batch record (`translations/en/batches/batch-09.md`).", required=True)
h = read(handover)
if "## Phase 4 durable result — Batch 09" not in h:
    idx = h.find("## Supplied-transcription rule")
    if idx < 0:
        raise SystemExit("handover insertion point missing")
    block = """## Phase 4 durable result — Batch 09\n\n- standing user cadence: **five poems per iteration**;\n- reviewed batches: **9**;\n- reviewed English items: **35/77**;\n- reviewed item-assigned source scans: **311/439**;\n- Batch 09 items: **31–35**;\n- Batch 09 source scans: **293–332 = 40/40**;\n- item 31 → **I Shall Walk on Our Ayya and Anna's Path!**;\n- item 32 → **Presiding Poem at the Three Great Celebrations Poetry Assembly**;\n- item 33 → **In a Changing Town**;\n- item 34 → **Views of Society...!**;\n- item 35 → **Kalaivanar Arangam Poetry Assembly**;\n- marker certification: **40/40 PASS**;\n- title witnesses: **2 exact / 3 authorised variants / 0 unresolved**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes during Batch 09: **0**;\n- Tamil `sections/` changes during Batch 09: **0**.\n\nBatch review: `translations/en/batches/batch-09.md`.\n\n"""
    h = h[:idx] + block + h[idx:]
    write(handover, h)
replace_tail(handover, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 10 — items 36–40 (`\"சித்திரைத் திருநாள்\" தலைமைக் கவிதை!`, `எழுத்துக்கள் மூன்று - எண்ணங்கள் மும்மூன்று`, `“அறிஞர் அண்ணா வழியில்”`, `பன்னீர்ச்செல்வமே!`, `கலைத்தாயின் தலைச் செல்வன்!`)**. Read final-cleared `sections/36.md` through `sections/40.md` completely. Preserve structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** outside poem translations. Review all five complete items together; item-owned scan total **44/44** across physical span **333–378**; expected title witnesses **1 exact / 4 authorised variants / 0 unresolved**. Leave all Tamil source/page/canonical files unchanged.""")

# Next chat prompt.
nextp = "NEXT_CHAT_PROMPT.md"
for old, new in [
    ("Batches 01–08 reviewed PASS; 30/77 items; 271/439 item scans; Batch 09 NEXT", "Batches 01–09 reviewed PASS; 35/77 items; 311/439 item scans; Batch 10 NEXT"),
    ("Batches 01–08 **reviewed PASS**", "Batches 01–09 **reviewed PASS**"),
]:
    replace_first(nextp, old, new, required=False)
np = read(nextp)
if "## Phase 4 Batch 09 durable result" not in np:
    idx = np.find("## EXACT NEXT ACTIVITY")
    if idx < 0:
        raise SystemExit("next-chat next heading missing")
    block = """## Phase 4 Batch 09 durable result\n\n- standing cadence: **five poems per iteration**;\n- Batches 01–09 **reviewed PASS**;\n- reviewed items **35/77**;\n- reviewed item scans **311/439**;\n- Batch 09 items 31–35, scans **293–332 = 40/40**;\n- title witnesses **2 exact / 3 authorised variants / 0 unresolved**;\n- unresolved translation issues **0**;\n- Tamil page/canonical changes **0**.\n\n"""
    np = np[:idx] + block + np[idx:]
    write(nextp, np)
replace_tail(nextp, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 10 — items 36–40**, physical span **333–378**, with **44/44 item-owned scans**. Structural scans **372–373 (`கண்ணீர்த் துளிகள்`)** stay outside poem translations. Preserve the authorised contents/canonical title variants for items 36, 37, 39 and 40 separately; item 38 is exact. Review together and do not alter Tamil `pages/` or `sections/`.""")

# Guard: no Tamil source/page/canonical paths may appear in the whole Batch-09 diff.
changed = subprocess.check_output(["git", "diff", "--name-only", BASE], text=True).splitlines()
for p in changed:
    if p.startswith("poems/kalaignarin-kavithaigal/pages/") or p.startswith("poems/kalaignarin-kavithaigal/sections/"):
        raise SystemExit(f"forbidden Tamil-layer change detected: {p}")

print("Batch 09 finalizer validation PASS")
print("markers=40; items=5; title witnesses=2 exact + 3 variants; Tamil pages/sections changes=0")
