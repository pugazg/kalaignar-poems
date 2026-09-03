from pathlib import Path
import re
import subprocess

BASE = "a35c2de64e1c8fdd7cffed2069c10bb310c5c931"
ROOT = Path(".")
WORK = "poems/kalaignarin-kavithaigal"
EN = f"{WORK}/translations/en"

items = {
    f"{EN}/items/51-know-it-as-a-storm-en.md": (51, [405], "variant"),
    f"{EN}/items/52-have-you-heard-en.md": (52, [406], "exact"),
    f"{EN}/items/53-varna-or-death-en.md": (53, [407], "exact"),
    f"{EN}/items/54-when-does-defeat-come-en.md": (54, [408], "exact"),
    f"{EN}/items/55-still-this-clamour-en.md": (55, [409], "exact"),
    f"{EN}/items/56-green-parrot-en.md": (56, [410,411,412], "variant"),
    f"{EN}/items/57-fountain-of-imagination-en.md": (57, [413,414], "exact"),
    f"{EN}/items/58-o-sky-pour-down-en.md": (58, [415,416], "exact"),
    f"{EN}/items/59-a-letter-in-verse-en.md": (59, [417], "variant"),
    f"{EN}/items/60-will-he-realise-who-knows-en.md": (60, [418,419], "exact"),
    f"{EN}/items/61-let-it-whirl-as-a-battle-sword-en.md": (61, [420,421], "variant"),
    f"{EN}/items/62-whose-names-have-still-not-appeared-en.md": (62, [422,423,424], "variant"),
    f"{EN}/items/63-a-drop-of-honey-en.md": (63, [425,426,427], "variant"),
    f"{EN}/items/64-let-it-sprout-as-seed-and-put-forth-roots-en.md": (64, [428], "variant"),
    f"{EN}/items/65-he-calls-the-sun-an-ice-cube-en.md": (65, [429,430,431,432], "variant"),
}


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(path, old, new, count=1):
    text = read(path)
    if text.count(old) < count:
        raise SystemExit(f"required text missing in {path}: {old!r}")
    write(path, text.replace(old, new, count))


def insert_before(path, marker, block):
    text = read(path)
    if block.strip() in text:
        return
    idx = text.rfind(marker)
    if idx < 0:
        raise SystemExit(f"marker missing in {path}: {marker}")
    write(path, text[:idx] + block.rstrip() + "\n\n" + text[idx:])


def replace_tail(path, heading, new_tail):
    text = read(path)
    idx = text.rfind(heading)
    if idx < 0:
        raise SystemExit(f"tail heading missing in {path}: {heading}")
    write(path, text[:idx] + new_tail.rstrip() + "\n")


# 1. Mechanical certification and promotion for all fifteen items.
marker_total = 0
exact = 0
variant = 0
for path, (item, expected, kind) in items.items():
    text = read(path)
    markers = [int(x) for x in re.findall(r"<!-- scan (\d+) -->", text)]
    if markers != expected:
        raise SystemExit(f"marker mismatch {path}: {markers} != {expected}")
    if f"item: {item}\n" not in text:
        raise SystemExit(f"item identity mismatch {path}")
    if 'status: "review-pending"' not in text:
        raise SystemExit(f"review-pending status missing {path}")
    if kind == "exact":
        if 'title_witness_status: "exact"' not in text:
            raise SystemExit(f"exact title status missing {path}")
        exact += 1
    else:
        if 'title_witness_status: "variant' not in text:
            raise SystemExit(f"variant title status missing {path}")
        variant += 1
    write(path, text.replace('status: "review-pending"', 'status: "batch-reviewed"', 1))
    marker_total += len(markers)

if marker_total != 28 or (exact, variant) != (7, 8):
    raise SystemExit(f"15-poem certification mismatch markers={marker_total} exact={exact} variants={variant}")

# 2. Review records.
for batch, total, exact_n, variant_n in [(13,5,4,1),(14,10,3,2),(15,13,0,5)]:
    path = f"{EN}/batches/batch-{batch:02d}.md"
    replace_required(path, "**REVIEWED — PASS, pending mechanical promotion/certification.**", "**REVIEWED — PASS.**")
    text = read(path)
    if "## Certification result" not in text:
        text += f"""

## Certification result

- exact scan-marker sequences: **{total}/{total} PASS**;
- item identities: **5/5 PASS**;
- title witnesses: **{exact_n} exact / {variant_n} authorised variants / 0 unresolved**;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes: **0**;
- Tamil `sections/` changes: **0**.
"""
        write(path, text)

# 3. Translation plan.
plan = f"{EN}/TRANSLATION_PLAN.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–12 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–15 reviewed PASS.**"),
    ("- batches: **12**;", "- batches: **15**;"),
    ("- items: **50/77**;", "- items: **65/77**;"),
    ("- item-assigned source scans: **379/439**;", "- item-assigned source scans: **407/439**;"),
    ("| 13 | 51–55 | 405–409 | **NEXT** |\n| later | 56–77 | five complete items per iteration (final remainder excepted) | pending |",
     "| 13 | 51–55 | 405–409 | **reviewed — PASS** |\n| 14 | 56–60 | 410–419 | **reviewed — PASS** |\n| 15 | 61–65 | 420–432 | **reviewed — PASS** |\n| 16 | 66–70 | 433–445 | **NEXT** |\n| later | 71–77 | five complete items per iteration (final remainder excepted) | pending |"),
]:
    replace_required(plan, old, new)
insert_before(plan, "## Exact next activity", """## Batches 13–15 decision record

User-authorised 15-poem iteration completed as three normal five-poem review units: **Batch 13 items 51–55 (5/5 scans 405–409), Batch 14 items 56–60 (10/10 scans 410–419), and Batch 15 items 61–65 (13/13 scans 420–432)**. Combined coverage: **28/28 item-owned scans**; title witnesses **7 exact + 8 authorised variants / 0 unresolved**. Review preserved the 1945 polemical miniatures and source-backed title corrections; the prison/parrot and Orlando-fountain sequences; drought, movement-duty and office-seeking rhetoric; named language-agitation memorials; election-fund and campaign wordplay; Pongal/Rising-Sun imagery; and the four-scan *Ananda Vikatan* rebuttal. Semantic review corrected item 57's closing “luckily alone” joke and item 63's `பணத்தோட்டா` money-bullet image before certification. Tamil `pages/`/`sections/` changes remain **0**.""")
replace_tail(plan, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 16 — items 66–70**: `நடையை நிறுத்தாதே!`, `பாமரர் நிறைந்த பட்டிக்காடு!`, `கொள்ளை போகுதம்மா தமிழ்நாடு`, `என்ன தேசமடா இது?`, `முகமூடி கிழித்தெறிவோம் வாரீர்!`. Process all five complete poems across scans **433–445 = 13/13**. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**. Leave Tamil `pages/` and `sections/` unchanged.""")

# 4. English source map.
smap = f"{EN}/SOURCE_MAP.md"
rows = """| 51 | `புயல் என அறிக!` | `புயல் என அறிக` | **Know It as a Storm!** | 405 | 388 | `items/51-know-it-as-a-storm-en.md` | **batch-reviewed — PASS** |
| 52 | `கேட்டுண்டோ?` | `கேட்டுண்டோ?` | **Have You Heard?** | 406 | 389 | `items/52-have-you-heard-en.md` | **batch-reviewed — PASS** |
| 53 | `வருணமா? மரணமா?` | `வருணமா? மரணமா?` | **Varna or Death?** | 407 | 390 | `items/53-varna-or-death-en.md` | **batch-reviewed — PASS** |
| 54 | `தோல்வி எப்பொழுது?` | `தோல்வி எப்பொழுது?` | **When Does Defeat Come?** | 408 | 391 | `items/54-when-does-defeat-come-en.md` | **batch-reviewed — PASS** |
| 55 | `இன்றுமா கூச்சல்?` | `இன்றுமா கூச்சல்?` | **Still This Clamour?** | 409 | 392 | `items/55-still-this-clamour-en.md` | **batch-reviewed — PASS** |
| 56 | `பச்சைக் கிளி` | `பச்சைக்கிளி` | **Green Parrot** | 410–412 | 393–395 | `items/56-green-parrot-en.md` | **batch-reviewed — PASS** |
| 57 | `கற்பனை ஊற்று` | `கற்பனை ஊற்று` | **Fountain of Imagination** | 413–414 | 396–397 | `items/57-fountain-of-imagination-en.md` | **batch-reviewed — PASS** |
| 58 | `வானமே பொழிக நீ!` | `வானமே பொழிக நீ!` | **O Sky, Pour Down!** | 415–416 | 398–399 | `items/58-o-sky-pour-down-en.md` | **batch-reviewed — PASS** |
| 59 | `கவிதையில் ஒரு மடல்!` | `கவிதையில் ஒரு மடல்` | **A Letter in Verse!** | 417 | 400 | `items/59-a-letter-in-verse-en.md` | **batch-reviewed — PASS** |
| 60 | `அவர் உணர்வாரோ! யார் அறிவார்?` | `அவர் உணர்வாரோ! யார் அறிவார்?` | **Will He Realise? Who Knows?** | 418–419 | 401–402 | `items/60-will-he-realise-who-knows-en.md` | **batch-reviewed — PASS** |
| 61 | `போர்வாளாய்ச் சுழலட்டும்!` | `போர்வாளாய்ச் சுழலட்டுமே!` | **Let It Whirl as a Battle-Sword!** | 420–421 | 403–404 | `items/61-let-it-whirl-as-a-battle-sword-en.md` | **batch-reviewed — PASS** |
| 62 | `இன்னும் யார் யார் பெயர்கள் வரவில்லை?` | `இன்னும் யார் - யார் பெயர்கள் வரவில்லை` | **Whose Names Have Still Not Appeared?** | 422–424 | 405–407 | `items/62-whose-names-have-still-not-appeared-en.md` | **batch-reviewed — PASS** |
| 63 | `ஒரு சொட்டுத் தேன்!` | `ஒரு சொட்டுத் தேன்` | **A Drop of Honey!** | 425–427 | 408–410 | `items/63-a-drop-of-honey-en.md` | **batch-reviewed — PASS** |
| 64 | `விதையாய் முளைத்து விழுதுகள் விடட்டும்!` | `விதையாய் முளைத்து விழுதுகள் விட்டோம்` | **Let It Sprout as Seed and Put Forth Roots!** | 428 | 411 | `items/64-let-it-sprout-as-seed-and-put-forth-roots-en.md` | **batch-reviewed — PASS** |
| 65 | `சூரியனைப் பனிக்கட்டி என்கின்றார்!` | `சூரியனைப் பனிக்கட்டி என்கிறாய்!` | **He Calls the Sun an Ice Cube!** | 429–432 | 412–415 | `items/65-he-calls-the-sun-an-ice-cube-en.md` | **batch-reviewed — PASS** |"""
text = read(smap)
if "| 51 | `புயல் என அறிக!`" not in text:
    lines = text.splitlines()
    pos = next((i + 1 for i, line in enumerate(lines) if line.startswith("| 50 |")), None)
    if pos is None:
        raise SystemExit("SOURCE_MAP item50 row missing")
    lines[pos:pos] = rows.splitlines()
    write(smap, "\n".join(lines) + "\n")
for old, new in [
    ("- reviewed English batches: **12**;", "- reviewed English batches: **15**;"),
    ("- reviewed English items: **50/77**;", "- reviewed English items: **65/77**;"),
    ("- reviewed item-assigned scans: **379/439**;", "- reviewed item-assigned scans: **407/439**;"),
]:
    replace_required(smap, old, new)
insert_before(smap, "## Exact next mapping activity", """### Items 51–65 provenance notes

- Batch 13: items **51–55**, scans **405–409 = 5/5**, title witnesses **4 exact + 1 authorised variant**;
- Batch 14: items **56–60**, scans **410–419 = 10/10**, title witnesses **3 exact + 2 authorised variants**;
- Batch 15: items **61–65**, scans **420–432 = 13/13**, title witnesses **0 exact + 5 authorised variants**;
- combined iteration: **28/28** item-owned scans represented exactly;
- scans **405–409** retain the verified 1945 publication notes; Gate-4 title corrections at scans **406** and **409** remain authoritative;
- item 57 semantic review corrected the direction of the closing solitary-viewing/sari joke before certification;
- item 63 semantic review preserves `பணத்தோட்டா` as the money-bullet/cartridge image;
- no Tamil page or canonical item was changed by Batches 13–15.""")
replace_tail(smap, "## Exact next mapping activity", """## Exact next mapping activity

Add reviewed mappings for **items 66–70** after Phase-4 Batch 16 passes. Batch 16 owns **13/13 item scans** across physical span **433–445**. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**.""")

# 5. English README.
tread = f"{EN}/README.md"
for old, new in [
    ("**PHASE 4 IN PROGRESS — Batches 01–12 reviewed PASS.**", "**PHASE 4 IN PROGRESS — Batches 01–15 reviewed PASS.**"),
    ("- reviewed English batches: **12**;", "- reviewed English batches: **15**;"),
    ("- reviewed English items: **50/77**;", "- reviewed English items: **65/77**;"),
    ("- item-assigned source scans covered by reviewed English: **379/439**;", "- item-assigned source scans covered by reviewed English: **407/439**;"),
]:
    replace_required(tread, old, new)
text = read(tread)
if "items/51-know-it-as-a-storm-en.md" not in text:
    needle = "- `items/50-would-they-accept-en.md` — reviewed English item 50."
    block = needle + "\n- `batches/batch-13.md` — reviewed Batch-13 record;\n- `items/51-know-it-as-a-storm-en.md` — reviewed English item 51;\n- `items/52-have-you-heard-en.md` — reviewed English item 52;\n- `items/53-varna-or-death-en.md` — reviewed English item 53;\n- `items/54-when-does-defeat-come-en.md` — reviewed English item 54;\n- `items/55-still-this-clamour-en.md` — reviewed English item 55;\n- `batches/batch-14.md` — reviewed Batch-14 record;\n- `items/56-green-parrot-en.md` — reviewed English item 56;\n- `items/57-fountain-of-imagination-en.md` — reviewed English item 57;\n- `items/58-o-sky-pour-down-en.md` — reviewed English item 58;\n- `items/59-a-letter-in-verse-en.md` — reviewed English item 59;\n- `items/60-will-he-realise-who-knows-en.md` — reviewed English item 60;\n- `batches/batch-15.md` — reviewed Batch-15 record;\n- `items/61-let-it-whirl-as-a-battle-sword-en.md` — reviewed English item 61;\n- `items/62-whose-names-have-still-not-appeared-en.md` — reviewed English item 62;\n- `items/63-a-drop-of-honey-en.md` — reviewed English item 63;\n- `items/64-let-it-sprout-as-seed-and-put-forth-roots-en.md` — reviewed English item 64;\n- `items/65-he-calls-the-sun-an-ice-cube-en.md` — reviewed English item 65."
    if needle not in text:
        raise SystemExit("translation README item50 line missing")
    write(tread, text.replace(needle, block, 1))
insert_before(tread, "## Exact next activity", """## Batches 13–15

**Reviewed — PASS.** User-authorised 15-poem iteration completed as three five-poem batches.

- Batch 13: items **51–55**, scans **405–409 = 5/5**, title witnesses **4 exact / 1 variant**;
- Batch 14: items **56–60**, scans **410–419 = 10/10**, title witnesses **3 exact / 2 variants**;
- Batch 15: items **61–65**, scans **420–432 = 13/13**, title witnesses **0 exact / 5 variants**;
- combined markers: **28/28 PASS**;
- unresolved translation issues: **0**;
- Tamil changes: **0**.""")
replace_tail(tread, "## Exact next activity", """## Exact next activity

Execute **Phase 4 Batch 16 — items 66–70**, scans **433–445 = 13/13**. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**. Review all five complete final-cleared items and do not alter Tamil `pages/` or `sections/`.""")

# 6. Work audit.
audit = f"{WORK}/audit.md"
replace_tail(audit, "### Exact next Phase-4 activity", """## Phase 4 Batch 13 audit — REVIEWED / PASS

- items after Batch 13: **55/77**;
- Batch-13 item-owned scans: **5/5 — scans 405–409**;
- cumulative reviewed item-owned scans: **384/439**;
- title witnesses: **4 exact / 1 authorised variant / 0 unresolved**;
- exact English scan-marker sequences: **5/5 PASS**;
- unresolved reviewed translation issues: **0**;
- Tamil page-record/canonical-item changes: **0**;
- evidence: `translations/en/batches/batch-13.md`.

## Phase 4 Batch 14 audit — REVIEWED / PASS

- items after Batch 14: **60/77**;
- Batch-14 item-owned scans: **10/10 — scans 410–419**;
- cumulative reviewed item-owned scans: **394/439**;
- title witnesses: **3 exact / 2 authorised variants / 0 unresolved**;
- exact English scan-marker sequences: **10/10 PASS**;
- unresolved reviewed translation issues: **0**;
- Tamil page-record/canonical-item changes: **0**;
- evidence: `translations/en/batches/batch-14.md`.

## Phase 4 Batch 15 audit — REVIEWED / PASS

- items after Batch 15: **65/77**;
- Batch-15 item-owned scans: **13/13 — scans 420–432**;
- cumulative reviewed item-owned scans: **407/439**;
- title witnesses: **0 exact / 5 authorised variants / 0 unresolved**;
- exact English scan-marker sequences: **13/13 PASS**;
- unresolved reviewed translation issues: **0**;
- Tamil page-record/canonical-item changes: **0**;
- evidence: `translations/en/batches/batch-15.md`.

### Exact next Phase-4 activity

**Batch 16 — items 66–70**, scans **433–445 = 13/13**; expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**.""")

# 7. Repository/work current-state docs.
root_readme = "README.md"
replace_required(root_readme,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–15 reviewed PASS; 65/77 items; 407/439 item scans; Batch 16 NEXT**.")
replace_required(root_readme,
    "Batches 01–12 now cover items **1–50**. The reviewed English layer covers **50/77 items** and **379/439 item-assigned source scans** with **0** unresolved reviewed translation issues.",
    "Batches 01–15 now cover items **1–65**. The reviewed English layer covers **65/77 items** and **407/439 item-assigned source scans** with **0** unresolved reviewed translation issues. The latest user-authorised iteration processed items 51–65 as Batches 13–15.")
replace_tail(root_readme, "## Next activity", """## Next activity

**Phase 4 Batch 16 — items 66–70**, scans **433–445 = 13/13**. Expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**; translate/review all five complete poems and leave Tamil archival files unchanged.""")

work_readme = f"{WORK}/README.md"
replace_required(work_readme,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–15 reviewed PASS; 65/77 items; 407/439 item scans; Batch 16 NEXT**.")
for old, new in [
    ("**IN PROGRESS — Batches 01–12 reviewed PASS.**", "**IN PROGRESS — Batches 01–15 reviewed PASS.**"),
    ("- reviewed batches: **12**;", "- reviewed batches: **15**;"),
    ("- reviewed items: **50/77**;", "- reviewed items: **65/77**;"),
    ("- reviewed item-assigned scans: **379/439**;", "- reviewed item-assigned scans: **407/439**;"),
]:
    replace_required(work_readme, old, new)
replace_tail(work_readme, "## Next activity", """## Next activity

**Phase 4 Batch 16 — items 66–70**, scans **433–445 = 13/13**. Expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**; review all five complete final-cleared items before advancing.""")

source_intake = f"{WORK}/SOURCE_INTAKE.md"
replace_required(source_intake,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–15 reviewed PASS; 65/77 items; 407/439 item scans; Batch 16 NEXT**.")
replace_required(source_intake,
    "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–12 are reviewed PASS; Batch 13 items 51–55 are next.",
    "**Phase 4 — English translation and release workflow is IN PROGRESS.** Batches 01–15 are reviewed PASS; Batch 16 items 66–70 are next.")
for old, new in [
    ("- Batches 01–12: **reviewed PASS**;", "- Batches 01–15: **reviewed PASS**;"),
    ("- reviewed items: **50/77**;", "- reviewed items: **65/77**;"),
    ("- reviewed item scans: **379/439**;", "- reviewed item scans: **407/439**;"),
    ("- Batch 12 marker certification: **9/9 PASS**;\n- exact next: **Batch 13 items 51–55**, scans **405–409 = 5/5**.",
     "- Batch 12 marker certification: **9/9 PASS**;\n- Batch 13 marker certification: **5/5 PASS**;\n- Batch 14 marker certification: **10/10 PASS**;\n- Batch 15 marker certification: **13/13 PASS**;\n- exact next: **Batch 16 items 66–70**, scans **433–445 = 13/13**."),
]:
    replace_required(source_intake, old, new)

metadata = f"{WORK}/metadata/source.md"
replace_required(metadata,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–15 reviewed PASS; 65/77 items; 407/439 item scans; Batch 16 NEXT**.")
for old, new in [
    ("- reviewed batches: **12**;", "- reviewed batches: **15**;"),
    ("- reviewed English items: **50/77**;", "- reviewed English items: **65/77**;"),
    ("- reviewed item scans: **379/439**;", "- reviewed item scans: **407/439**;"),
    ("- Batch 12 review: `../translations/en/batches/batch-12.md`;\n- Batch 12 marker certification: **9/9 PASS**;\n- next translation batch: **items 51–55**, scans **405–409 = 5/5**.",
     "- Batch 12 review: `../translations/en/batches/batch-12.md`;\n- Batch 12 marker certification: **9/9 PASS**;\n- Batch 13 review: `../translations/en/batches/batch-13.md`; marker certification: **5/5 PASS**;\n- Batch 14 review: `../translations/en/batches/batch-14.md`; marker certification: **10/10 PASS**;\n- Batch 15 review: `../translations/en/batches/batch-15.md`; marker certification: **13/13 PASS**;\n- next translation batch: **items 66–70**, scans **433–445 = 13/13**."),
]:
    replace_required(metadata, old, new)

pmap = f"{WORK}/indexes/page-map.md"
replace_required(pmap,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**;",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–15 reviewed PASS; 65/77 items; 407/439 item scans; Batch 16 NEXT**;")
replace_required(pmap,
    "Phase 4 Batches 01–12 reviewed items **1–50** across **379/439** item-assigned scans. Batch 12 certifies **9/9** item-owned scan markers across physical span **396–404**. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 13 items **51–55**, scans **405–409 = 5/5**.",
    "Phase 4 Batches 01–15 reviewed items **1–65** across **407/439** item-assigned scans. Batches 13–15 certify **28/28** item-owned scan markers across physical span **405–432**. Translation milestones change no scan↔page mapping and no Tamil page/canonical file. Exact next: Batch 16 items **66–70**, scans **433–445 = 13/13**.")

clearance = f"{WORK}/PHASE3_TAMIL_FINAL_CLEARANCE.md"
replace_required(clearance,
    "Phase 4 has subsequently advanced through **Batches 01–12, all reviewed PASS**. Reviewed English now covers items **1–50/77** and **379/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Batch 12 certifies scans **396–404 = 9/9**. Exact next translation activity: **Batch 13 items 51–55**, scans **405–409 = 5/5**.",
    "Phase 4 has subsequently advanced through **Batches 01–15, all reviewed PASS**. Reviewed English now covers items **1–65/77** and **407/439** item-assigned scans. The Tamil final-cleared `pages/` and `sections/` layers remain unchanged. Batches 13–15 certify scans **405–432 = 28/28**. Exact next translation activity: **Batch 16 items 66–70**, scans **433–445 = 13/13**.")

# 8. Phase plan.
phase = "TRANSCRIPTION_PHASE_PLAN.md"
for old, new in [
    ("**IN PROGRESS — Batches 01–12 reviewed PASS.**", "**IN PROGRESS — Batches 01–15 reviewed PASS.**"),
    ("- reviewed batches: **12**;", "- reviewed batches: **15**;"),
    ("- reviewed English items: **50/77**;", "- reviewed English items: **65/77**;"),
    ("- reviewed item-assigned source scans: **379/439**;", "- reviewed item-assigned source scans: **407/439**;"),
    ("- Batch 13: items 51–55, scans **405–409 = 5/5**, **NEXT**.",
     "- Batch 13: items 51–55, scans **405–409 = 5/5**, **reviewed PASS**;\n- Batch 14: items 56–60, scans **410–419 = 10/10**, **reviewed PASS**;\n- Batch 15: items 61–65, scans **420–432 = 13/13**, **reviewed PASS**;\n- Batch 16: items 66–70, scans **433–445 = 13/13**, **NEXT**."),
]:
    replace_required(phase, old, new)
replace_tail(phase, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 16 — items 66–70**, scans **433–445 = 13/13**. Expected title witnesses: **2 exact / 3 authorised variants / 0 unresolved**. Do not alter Tamil final-cleared files.""")

# 9. Handover and next-chat prompt.
handover = "HANDOVER.md"
replace_required(handover, "## Durable state after Phase 4 Batch 12", "## Durable state after Phase 4 Batch 15")
replace_required(handover,
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item-assigned scans; Batch 13 NEXT**.",
    "- Phase 4 English translation/release: **IN PROGRESS — Batches 01–15 reviewed PASS; 65/77 items; 407/439 item-assigned scans; Batch 16 NEXT**.")
insert_before(handover, "## Supplied-transcription rule", """## Phase 4 durable result — Batches 13–15

- user-authorised current iteration: **15 poems**, retained as three five-poem review batches;
- reviewed batches: **15**;
- reviewed English items: **65/77**;
- reviewed item-assigned source scans: **407/439**;
- Batch 13: items **51–55**, scans **405–409 = 5/5**, title witnesses **4 exact / 1 variant**;
- Batch 14: items **56–60**, scans **410–419 = 10/10**, title witnesses **3 exact / 2 variants**;
- Batch 15: items **61–65**, scans **420–432 = 13/13**, title witnesses **0 exact / 5 variants**;
- combined marker certification: **28/28 PASS**;
- semantic review corrections before certification: item 57 closing solitary-viewing/sari direction; item 63 `பணத்தோட்டா` money-bullet image;
- unresolved reviewed translation issues: **0**;
- Tamil `pages/` changes: **0**;
- Tamil `sections/` changes: **0**.

Batch reviews: `translations/en/batches/batch-13.md`, `batch-14.md`, `batch-15.md`.""")
replace_required(handover,
    "22. the latest reviewed translation batch record (`translations/en/batches/batch-12.md`).",
    "22. the latest reviewed translation batch record (`translations/en/batches/batch-15.md`).")
replace_tail(handover, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 16 — items 66–70 (`நடையை நிறுத்தாதே!`, `பாமரர் நிறைந்த பட்டிக்காடு!`, `கொள்ளை போகுதம்மா தமிழ்நாடு`, `என்ன தேசமடா இது?`, `முகமூடி கிழித்தெறிவோம் வாரீர்!`)**. Read final-cleared `sections/66.md` through `sections/70.md` completely. Review all five complete items together across scans **433–445 = 13/13**. Expected title witnesses **2 exact / 3 authorised variants / 0 unresolved**. Leave all Tamil source/page/canonical files unchanged.""")

nextp = "NEXT_CHAT_PROMPT.md"
replace_required(nextp,
    "- Phase 4 English translation/release **IN PROGRESS — Batches 01–12 reviewed PASS; 50/77 items; 379/439 item scans; Batch 13 NEXT**.",
    "- Phase 4 English translation/release **IN PROGRESS — Batches 01–15 reviewed PASS; 65/77 items; 407/439 item scans; Batch 16 NEXT**.")
insert_before(nextp, "## EXACT NEXT ACTIVITY", """## Phase 4 Batches 13–15 durable result

- user-authorised current iteration: **15 poems**, recorded as Batches **13–15**;
- Batches 01–15 **reviewed PASS**;
- reviewed items **65/77**;
- reviewed item scans **407/439**;
- Batch 13 items 51–55, **5/5 scans**;
- Batch 14 items 56–60, **10/10 scans**;
- Batch 15 items 61–65, **13/13 scans**;
- combined title witnesses **7 exact / 8 authorised variants / 0 unresolved**;
- combined marker certification **28/28 PASS**;
- unresolved translation issues **0**;
- Tamil page/canonical changes **0**.""")
replace_tail(nextp, "## EXACT NEXT ACTIVITY", """## EXACT NEXT ACTIVITY

Execute **Phase 4 Batch 16 — items 66–70**, physical span **433–445**, with **13/13 item-owned scans**. Preserve the authorised contents/canonical title variants for items 67, 68 and 70 separately; items 66 and 69 are exact. Review together and do not alter Tamil `pages/` or `sections/`.""")

# 10. Scope guard over the whole 15-poem iteration.
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
    ".github/workflows/phase4-batches13-15-finalize.yml",
    "scripts/finalize-kalaignarin-kavithaigal-batches13-15.py",
}
unexpected = [p for p in changed if p not in allowed_exact and not any(p.startswith(pref) for pref in allowed_prefixes)]
if unexpected:
    raise SystemExit(f"unexpected Batches 13–15 changed paths: {unexpected}")

print("Batches 13–15 certification/status synchronization PASS")
