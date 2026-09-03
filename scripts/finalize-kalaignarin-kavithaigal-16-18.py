#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess

BASE = "17ea39bf6ef69a989e9225af81b9414cc12a6845"
ROOT = Path("poems/kalaignarin-kavithaigal")
TR = ROOT / "translations/en"

items = {
66: ("66-dont-stop-your-stride-en.md", [433,434], "exact"),
67: ("67-a-backwater-full-of-ignorant-folk-en.md", [435,436,437], "variant"),
68: ("68-tamil-nadu-is-being-looted-en.md", [438,439], "variant"),
69: ("69-what-kind-of-country-is-this-en.md", [440,441,442], "exact"),
70: ("70-come-let-us-tear-off-the-mask-en.md", [443,444,445], "variant"),
71: ("71-what-is-the-answer-tell-us-en.md", [446,447], "exact"),
72: ("72-ka-ka-ka-en.md", [448,449], "exact"),
73: ("73-let-us-rise-in-the-east-like-the-sun-en.md", [450,451,452], "variant"),
74: ("74-is-this-diversion-justified-en.md", [453,454], "exact"),
75: ("75-it-is-over-a-comedy-drama-en.md", [455,456], "exact"),
76: ("76-there-are-some-countries-en.md", [457,458,459,460], "variant"),
77: ("77-you-bless-your-footwear-en.md", [461,462,463,464], "exact"),
}

# Scope guard across the whole user-requested final sweep.
changed = subprocess.check_output(["git", "diff", "--name-only", f"{BASE}..HEAD"], text=True).splitlines()
for p in changed:
    if p.startswith(str(ROOT / "pages") + "/") or p.startswith(str(ROOT / "sections") + "/"):
        raise SystemExit(f"Tamil archival layer changed during final translation sweep: {p}")

all_markers = []
exact = variants = 0
for n, (name, scans, witness) in items.items():
    path = TR / "items" / name
    text = path.read_text()
    if f"item: {n}\n" not in text:
        raise SystemExit(f"item identity mismatch: {path}")
    if 'status: "review-pending"' not in text:
        raise SystemExit(f"review-pending status missing: {path}")
    markers = [int(x) for x in re.findall(r"<!-- scan (\d+) -->", text)]
    if markers != scans:
        raise SystemExit(f"marker mismatch item {n}: {markers} != {scans}")
    all_markers.extend(markers)
    if witness == "exact":
        if 'title_witness_status: "exact"' not in text:
            raise SystemExit(f"title witness mismatch item {n}")
        exact += 1
    else:
        if 'title_witness_status: "variant' not in text:
            raise SystemExit(f"title witness mismatch item {n}")
        variants += 1

if all_markers != list(range(433,465)):
    raise SystemExit(f"combined marker sequence mismatch: {all_markers}")
if (exact, variants) != (7,5):
    raise SystemExit(f"title witness totals mismatch: {(exact, variants)}")

# Promote all remaining item translations.
for n, (name, scans, witness) in items.items():
    path = TR / "items" / name
    text = path.read_text()
    text = text.replace('status: "review-pending"', 'status: "batch-reviewed"', 1)
    path.write_text(text)

# Compute immutable final item blob witnesses after promotion.
blob = {}
for n, (name, _, _) in items.items():
    path = TR / "items" / name
    blob[n] = subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()

batch_specs = {
16: (range(66,71), "13/13", "5/5", "2 exact / 3 authorised variants / 0 unresolved"),
17: (range(71,76), "11/11", "5/5", "4 exact / 1 authorised variant / 0 unresolved"),
18: (range(76,78), "8/8", "2/2", "1 exact / 1 authorised variant / 0 unresolved"),
}
for b, (nums, markers, identities, titles) in batch_specs.items():
    path = TR / "batches" / f"batch-{b:02d}.md"
    text = path.read_text()
    if "## Certification result" in text:
        raise SystemExit(f"batch already certified unexpectedly: {path}")
    lines = [
        "",
        "## Certification result",
        "",
        f"- exact scan-marker sequences: **{markers} PASS**;",
        f"- item identities: **{identities} PASS**;",
        f"- title witnesses: **{titles}**;",
        "- unresolved reviewed translation issues: **0**;",
        "- Tamil `pages/` changes: **0**;",
        "- Tamil `sections/` changes: **0**.",
        "",
        "## Final reviewed item blob witnesses",
        "",
        "These are the exact item blobs certified after `status` promotion to `batch-reviewed`:",
        "",
    ]
    for n in nums:
        lines.append(f"- item {n} final blob: `{blob[n]}`;")
    path.write_text(text.rstrip() + "\n" + "\n".join(lines) + "\n")

completion = """## Phase 4 item-translation completion\n\n- reviewed batches: **18/18**;\n- reviewed English items: **77/77**;\n- reviewed item-assigned source scans: **439/439**;\n- final sweep Batches 16–18: items **66–77**, scans **433–464 = 32/32**;\n- final-sweep title witnesses: **7 exact / 5 authorised variants / 0 unresolved**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes during Phase 4: **0**;\n- Tamil `sections/` changes during Phase 4: **0**;\n- item translation/review layer: **COMPLETE / PASS**;\n- next ordered activity: **full English collection assembly**, then editorial consistency review and release report.\n"""

# HANDOVER: authoritative durable frontier and next activity.
p = Path("HANDOVER.md")
t = p.read_text()
t = t.replace("## Durable state after Phase 4 Batch 15", "## Durable state after Phase 4 Batch 18 — item translation review complete", 1)
t = re.sub(r"Phase 4 English translation/release: \*\*IN PROGRESS — Batches 01–15 reviewed PASS; 65/77 items; 407/439 item-assigned scans; Batch 16 NEXT\*\*\.", "Phase 4 English translation/release: **ITEM TRANSLATION REVIEW COMPLETE — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; collection assembly NEXT**.", t, count=1)
if "## Phase 4 durable result — Batches 16–18" not in t:
    block = """## Phase 4 durable result — Batches 16–18\n\n- user-authorised final sweep: **12 remaining poems**, retained as Batches **16–18**;\n- Batch 16: items **66–70**, scans **433–445 = 13/13**, title witnesses **2 exact / 3 variants**;\n- Batch 17: items **71–75**, scans **446–456 = 11/11**, title witnesses **4 exact / 1 variant**;\n- Batch 18: items **76–77**, scans **457–464 = 8/8**, title witnesses **1 exact / 1 variant**;\n- combined final-sweep marker certification: **32/32 PASS**;\n- cumulative reviewed English items: **77/77**;\n- cumulative reviewed item-assigned scans: **439/439**;\n- unresolved reviewed translation issues: **0**;\n- Tamil `pages/` changes: **0**;\n- Tamil `sections/` changes: **0**;\n- scan **465** remains back cover outside poem translation.\n\nBatch reviews: `translations/en/batches/batch-16.md`, `batch-17.md`, `batch-18.md`.\n\n"""
    t = t.replace("## Supplied-transcription rule", block + "## Supplied-transcription rule", 1)
t = re.sub(r"## EXACT NEXT ACTIVITY\n\nExecute \*\*Phase 4 Batch 16[\s\S]*$", "## EXACT NEXT ACTIVITY\n\nExecute **Phase 4 full English collection assembly** from the **77/77 batch-reviewed item translations**. Preserve item order, the four pure anthology structural divider/verso pairs, title-witness provenance and all item boundaries. Then perform the deferred **editorial consistency review** and prepare the **release report**. Do not alter Tamil `pages/` or `sections/` merely for English editorial preference.\n", t)
p.write_text(t)

# NEXT_CHAT_PROMPT: current state and next activity.
p = Path("NEXT_CHAT_PROMPT.md")
t = p.read_text()
t = re.sub(r"Phase 4 English translation/release \*\*IN PROGRESS — Batches 01–15 reviewed PASS; 65/77 items; 407/439 item scans; Batch 16 NEXT\*\*\.", "Phase 4 English translation/release **ITEM TRANSLATION REVIEW COMPLETE — Batches 01–18 reviewed PASS; 77/77 items; 439/439 item scans; collection assembly NEXT**.", t, count=1)
if "## Phase 4 Batches 16–18 durable result" not in t:
    block = """## Phase 4 Batches 16–18 durable result\n\n- final 12-poem sweep complete: items **66–77**;\n- Batch 16 scans **433–445 = 13/13**; Batch 17 scans **446–456 = 11/11**; Batch 18 scans **457–464 = 8/8**;\n- combined marker certification **32/32 PASS**;\n- title witnesses **7 exact / 5 authorised variants / 0 unresolved**;\n- cumulative reviewed English **77/77 items, 439/439 item scans**;\n- unresolved translation issues **0**;\n- Tamil page/canonical changes **0**;\n- item translation/review layer **COMPLETE / PASS**.\n\n"""
    t = t.replace("## EXACT NEXT ACTIVITY", block + "## EXACT NEXT ACTIVITY", 1)
t = re.sub(r"## EXACT NEXT ACTIVITY\n\nExecute \*\*Phase 4 Batch 16[\s\S]*$", "## EXACT NEXT ACTIVITY\n\nExecute **Phase 4 full English collection assembly** from all **77/77 batch-reviewed item translations**. Preserve source order, pure anthology structural divider/verso provenance, canonical/contents title distinctions and item boundaries. After assembly, run the deferred **editorial consistency review** and prepare the **release report**. Leave Tamil `pages/` and `sections/` unchanged unless a genuine source-backed discrepancy is independently demonstrated.\n", t)
p.write_text(t)

# TRANSLATION_PLAN: close item-review inventory and set collection assembly next.
p = TR / "TRANSLATION_PLAN.md"
t = p.read_text()
t = t.replace("**PHASE 4 IN PROGRESS — Batches 01–15 reviewed PASS.**", "**PHASE 4 ITEM TRANSLATION REVIEW COMPLETE — Batches 01–18 reviewed PASS.**", 1)
t = t.replace("- batches: **15**;", "- batches: **18**;", 1)
t = t.replace("- items: **65/77**;", "- items: **77/77**;", 1)
t = t.replace("- item-assigned source scans: **407/439**;", "- item-assigned source scans: **439/439**;", 1)
t = t.replace("| 16 | 66–70 | 433–445 | **NEXT** |\n| later | 71–77 | five complete items per iteration (final remainder excepted) | pending |", "| 16 | 66–70 | 433–445 | **reviewed — PASS** |\n| 17 | 71–75 | 446–456 | **reviewed — PASS** |\n| 18 | 76–77 | 457–464 | **reviewed — PASS** |")
t = re.sub(r"## Exact next activity\n\nExecute \*\*Phase 4 Batch 16[\s\S]*$", "## Batches 16–18 decision record\n\nThe user authorised processing all remaining poems in one final sweep. The work was retained as normal review units: **Batch 16 items 66–70 (13/13 scans 433–445), Batch 17 items 71–75 (11/11 scans 446–456), and Batch 18 items 76–77 (8/8 scans 457–464)**. Combined final-sweep title witnesses are **7 exact + 5 authorised variants / 0 unresolved**. The reviewed translations preserve the journey/duty-dignity-discipline movement rhetoric; panchayat and corruption satire; anti-fraud-ascetic polemic; `கா / காக்கா` sound-play; rationalist Narakasura challenge; stage-farce repetition; democracy-child and Bangabandhu/ball wordplay; and the final autobiographical footwear-service metaphor. Item 77 preserves both the body’s 57th-birthday witness and the closing 58th-birthday source note. Tamil `pages/`/`sections/` changes remain **0**.\n\n## Exact next activity\n\nAssemble the **full English collection** from all **77/77 batch-reviewed item translations**, preserving anthology structure and source provenance. Then run the deferred **editorial consistency review** and prepare the **release report**.\n", t)
p.write_text(t)

# SOURCE_MAP: complete reviewed correspondence through item 77.
p = TR / "SOURCE_MAP.md"
t = p.read_text()
row65 = "| 65 | `சூரியனைப் பனிக்கட்டி என்கின்றார்!` | `சூரியனைப் பனிக்கட்டி என்கிறாய்!` | **He Calls the Sun an Ice Cube!** | 429–432 | 412–415 | `items/65-he-calls-the-sun-an-ice-cube-en.md` | **batch-reviewed — PASS** |"
rows = """
| 66 | `நடையை நிறுத்தாதே!` | `நடையை நிறுத்தாதே!` | **Don't Stop Your Stride!** | 433–434 | 416–417 | `items/66-dont-stop-your-stride-en.md` | **batch-reviewed — PASS** |
| 67 | `பாமரர் நிறைந்த பட்டிக்காடு!` | `பாமர் நிறைந்த பட்டிக்காடு` | **A Backwater Full of Ignorant Folk!** | 435–437 | 418–420 | `items/67-a-backwater-full-of-ignorant-folk-en.md` | **batch-reviewed — PASS** |
| 68 | `கொள்ளை போகுதம்மா தமிழ்நாடு` | `கொள்ளை போதும்மா தமிழ்நாடு` | **Tamil Nadu Is Being Looted** | 438–439 | 421–422 | `items/68-tamil-nadu-is-being-looted-en.md` | **batch-reviewed — PASS** |
| 69 | `என்ன தேசமடா இது?` | `என்ன தேசமடா இது?` | **What Kind of Country Is This?** | 440–442 | 423–425 | `items/69-what-kind-of-country-is-this-en.md` | **batch-reviewed — PASS** |
| 70 | `முகமூடி கிழித்தெறிவோம் வாரீர்!` | `முடியுமா? கிழித்தெறிவோம் வாரீர்!` | **Come, Let Us Tear Off the Mask!** | 443–445 | 426–428 | `items/70-come-let-us-tear-off-the-mask-en.md` | **batch-reviewed — PASS** |
| 71 | `பதில் என்ன? பகர்ந்திடுக!` | `பதில் என்ன? பகர்ந்திடுக!` | **What Is the Answer? Tell Us!** | 446–447 | 429–430 | `items/71-what-is-the-answer-tell-us-en.md` | **batch-reviewed — PASS** |
| 72 | `கா, கா, கா!` | `கா, கா, கா!` | **Kā, Kā, Kā!** | 448–449 | 431–432 | `items/72-ka-ka-ka-en.md` | **batch-reviewed — PASS** |
| 73 | `பகலவனாய்க் கிழக்கில் உதித்திடுவோம்!` | `பகலவனாய்க் கிழக்கில் உதித்திடுவோம்` | **Let Us Rise in the East Like the Sun!** | 450–452 | 433–435 | `items/73-let-us-rise-in-the-east-like-the-sun-en.md` | **batch-reviewed — PASS** |
| 74 | `திசை திருப்பல் நியாயம்தானா?` | `திசை திருப்பல் நியாயம்தானா?` | **Is This Diversion Justified?** | 453–454 | 436–437 | `items/74-is-this-diversion-justified-en.md` | **batch-reviewed — PASS** |
| 75 | `நடந்து முடிந்ததம்மா; ஒரு நகைச்சுவை நாடகம்!` | `நடந்து முடிந்ததம்மா; ஒரு நகைச்சுவை நாடகம்!` | **It Is Over—a Comedy Drama!** | 455–456 | 438–439 | `items/75-it-is-over-a-comedy-drama-en.md` | **batch-reviewed — PASS** |
| 76 | `சில நாடுகள் இருக்கின்றன!` | `சில நாடுகள் இருக்கின்றன` | **There Are Some Countries!** | 457–460 | 440–443 | `items/76-there-are-some-countries-en.md` | **batch-reviewed — PASS** |
| 77 | `உன் காலணியை வாழ்த்துகிறாய்` | `உன் காலணியை வாழ்த்துகிறாய்` | **You Bless Your Footwear** | 461–464 | 444–447 | `items/77-you-bless-your-footwear-en.md` | **batch-reviewed — PASS** |""".strip("\n")
if "| 66 | `நடையை நிறுத்தாதே!`" not in t:
    if row65 not in t:
        raise SystemExit("SOURCE_MAP row65 anchor missing")
    t = t.replace(row65, row65 + "\n" + rows, 1)
t = t.replace("- reviewed English batches: **15**;", "- reviewed English batches: **18**;", 1)
t = t.replace("- reviewed English items: **65/77**;", "- reviewed English items: **77/77**;", 1)
t = t.replace("- reviewed item-assigned scans: **407/439**;", "- reviewed item-assigned scans: **439/439**;", 1)
if "### Items 66–77 provenance notes" not in t:
    t += "\n\n### Items 66–77 provenance notes\n\n- Batches 16–18 cover the final **32/32** item-owned scans **433–464**; scan **465** is the back cover and is not poem content;\n- title witnesses across items 66–77: **7 exact / 5 authorised variants / 0 unresolved**;\n- item 72 retains `கா / காக்கா` sound-play and item 76 retains the `வங்க பந்து / பந்து` kin/ball wordplay through explicit translator notes;\n- item 77 retains both the body’s 57th-birthday wording and the closing 58th-birthday source note;\n- all **77/77** canonical Tamil items now have one **batch-reviewed — PASS** English item;\n- reviewed English provenance covers **439/439** item-assigned scans;\n- Tamil page/canonical modifications during Phase 4 remain **0**.\n"
p.write_text(t)

# English README: close item-review status and expose the final files.
p = TR / "README.md"
t = p.read_text()
t = t.replace("**PHASE 4 IN PROGRESS — Batches 01–15 reviewed PASS.**", "**PHASE 4 ITEM TRANSLATION REVIEW COMPLETE — Batches 01–18 reviewed PASS.**", 1)
t = t.replace("- reviewed English batches: **15**;", "- reviewed English batches: **18**;", 1)
t = t.replace("- reviewed English items: **65/77**;", "- reviewed English items: **77/77**;", 1)
t = t.replace("- item-assigned source scans covered by reviewed English: **407/439**;", "- item-assigned source scans covered by reviewed English: **439/439**;", 1)
anchor = "A complete English collection, editorial consistency review and release report are deferred until all 77 item translations are reviewed."
if anchor in t:
    listing = """- `batches/batch-16.md` — reviewed Batch-16 record;\n- `batches/batch-17.md` — reviewed Batch-17 record;\n- `batches/batch-18.md` — reviewed final-remainder Batch-18 record;\n- `items/66-dont-stop-your-stride-en.md` through `items/77-you-bless-your-footwear-en.md` — reviewed English items 66–77.\n\nAll **77/77** item translations are now reviewed. Full English collection assembly is next, followed by editorial consistency review and the release report."""
    t = t.replace(anchor, listing, 1)
p.write_text(t)

# Audit: append final certified audits and new next activity.
p = ROOT / "audit.md"
t = p.read_text()
if "## Phase 4 Batches 16–18 audit — REVIEWED / PASS" not in t:
    t += "\n\n## Phase 4 Batches 16–18 audit — REVIEWED / PASS\n\n- items after Batch 18: **77/77**;\n- Batch-16 markers: **13/13 PASS — scans 433–445**;\n- Batch-17 markers: **11/11 PASS — scans 446–456**;\n- Batch-18 markers: **8/8 PASS — scans 457–464**;\n- cumulative reviewed item-owned scans: **439/439**;\n- final-sweep title witnesses: **7 exact / 5 authorised variants / 0 unresolved**;\n- omission/duplication issues: **0**;\n- unresolved reviewed translation issues: **0**;\n- Tamil page-record changes: **0**;\n- Tamil canonical-item changes: **0**;\n- scan **465** remains back cover outside poem translation.\n\n### Exact next Phase-4 activity\n\nAssemble the full English collection from all **77/77 batch-reviewed items**, then conduct the deferred editorial consistency review and prepare the release report.\n"
p.write_text(t)

# Secondary status documents: update their leading current progress where present and append an unambiguous completion note.
secondary = [
    Path("README.md"),
    Path("TRANSCRIPTION_PHASE_PLAN.md"),
    ROOT / "README.md",
    ROOT / "SOURCE_INTAKE.md",
    ROOT / "indexes/page-map.md",
    ROOT / "metadata/source.md",
    ROOT / "PHASE3_TAMIL_FINAL_CLEARANCE.md",
]
for p in secondary:
    t = p.read_text()
    t = re.sub(r"Batches 01–15 reviewed PASS; 65/77 items; 407/439 item(?:-assigned)? scans; Batch 16 NEXT", "Batches 01–18 reviewed PASS; 77/77 items; 439/439 item-assigned scans; item translation review COMPLETE; collection assembly NEXT", t, count=1)
    t = re.sub(r"Batches 01–15 reviewed PASS", "Batches 01–18 reviewed PASS", t, count=1)
    t = re.sub(r"reviewed batches: \*\*15\*\*;", "reviewed batches: **18**;", t, count=1)
    t = re.sub(r"reviewed English items: \*\*65/77\*\*;", "reviewed English items: **77/77**;", t, count=1)
    t = re.sub(r"reviewed item(?:-assigned)? scans: \*\*407/439\*\*;", "reviewed item-assigned scans: **439/439**;", t, count=1)
    if "## Phase 4 item-translation completion" not in t:
        t = t.rstrip() + "\n\n" + completion + "\n"
    p.write_text(t)

# Remove the one-shot runner from the final tree.
Path(".github/workflows/finalize-kalaignarin-kavithaigal-16-18.yml").unlink()
Path("scripts/finalize-kalaignarin-kavithaigal-16-18.py").unlink()

# Final local scope check before commit.
for p in subprocess.check_output(["git", "diff", "--name-only"], text=True).splitlines():
    if p.startswith(str(ROOT / "pages") + "/") or p.startswith(str(ROOT / "sections") + "/"):
        raise SystemExit(f"finalizer attempted Tamil archival change: {p}")

print("PASS: 12/12 items, 32/32 markers, 7 exact + 5 variants, 77/77 cumulative items, 439/439 cumulative item scans")
