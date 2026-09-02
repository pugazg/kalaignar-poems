from pathlib import Path
import json
import re

BASE = Path("poems/kalaignarin-kavithaigal")
PAGES = BASE / "pages"
SECTIONS = BASE / "sections"
SOURCE_MAP = BASE / "indexes" / "canonical-source-map.md"
GATE3 = BASE / "PHASE3_TITLE_WITNESS_RECONCILIATION.md"
REPORT = BASE / "PHASE3_CANONICAL_SOURCE_REVIEW.md"

SOURCE_FILENAME = "TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf"
START_HEAD = "401c4541f570a1cad4097ad029bede4a1cbf4754"
PURE_GROUPS = {
    "இனமான ஏந்தல்கள்": [32, 33],
    "கவியரங்கக் கவிதைகள்": [70, 71],
    "கண்ணீர்த் துளிகள்": [372, 373],
    "மலர்த் தோட்டம்": [392, 393],
}

ADMIN_PATTERNS = [
    r"verification", r"visual", r"physical", r"\bnote\b", r"audit",
    r"review", r"status", r"method", r"provenance", r"reconciliation",
    r"boundary", r"lexical-control", r"clearance", r"placement",
    r"^phase[- ]", r"^c\d+\b", r"source check", r"quality check",
    r"archival", r"transcription method"
]
SOURCE_HINTS = [
    "poem", "printed", "edition text", "context", "caption", "contents",
    "preface", "foreword", "title", "heading", "speaker", "dialogue",
    "body text", "publication text", "imprint text"
]


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        raise SystemExit("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise SystemExit("unterminated frontmatter")
    raw = text[4:end]
    meta = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v == "null":
            value = None
        elif len(v) >= 2 and v[0] == '"' and v[-1] == '"':
            value = json.loads(v)
        elif re.fullmatch(r"-?\d+", v):
            value = int(v)
        else:
            value = v
        meta[k.strip()] = value
    return meta, text[end + 5:]


def source_heading(heading):
    h = heading.strip().lower()
    if any(x in h for x in SOURCE_HINTS):
        return True
    if any(re.search(p, h) for p in ADMIN_PATTERNS):
        return False
    return True


def clean_source_chunk(chunk):
    lines = chunk.splitlines()
    out = []
    for line in lines:
        if re.fullmatch(r"```(?:text|markdown)?\s*", line.strip(), flags=re.I):
            continue
        if line.strip() == "```":
            continue
        out.append(line.rstrip())
    text = "\n".join(out).strip("\n")
    non_source_sentinels = {
        "No positively identified edition text is transcribed on this page.",
        "No positively identified edition text is transcribed on this side.",
        "No edition text is transcribed on this page.",
        "No source text is transcribed on this page.",
    }
    if text.strip() in non_source_sentinels:
        return ""
    return text


def extract_source(body):
    lines = body.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    chunks = []
    heading = None
    buf = []

    def flush():
        nonlocal buf, heading
        if heading is not None and source_heading(heading):
            cleaned = clean_source_chunk("\n".join(buf))
            if cleaned:
                chunks.append(cleaned)
        buf = []

    for line in lines:
        if line.startswith("## "):
            flush()
            heading = line[3:].strip()
        else:
            buf.append(line)
    flush()
    return "\n\n".join(chunks).strip()


def compact_ranges(nums):
    nums = list(nums)
    if not nums:
        return ""
    out = []
    start = prev = nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
            continue
        out.append(str(start) if start == prev else f"{start}–{prev}")
        start = prev = n
    out.append(str(start) if start == prev else f"{start}–{prev}")
    return ", ".join(out)


records = {}
for n in range(1, 466):
    path = PAGES / f"{n:04d}.md"
    if not path.exists():
        raise SystemExit(f"missing page record: {path}")
    meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    if meta.get("scan_page") != n:
        raise SystemExit(f"scan mismatch at {path}: {meta.get('scan_page')}")
    if meta.get("status") != "verified":
        raise SystemExit(f"non-verified page record: {path} = {meta.get('status')}")
    if meta.get("source_filename") != SOURCE_FILENAME:
        raise SystemExit(f"source filename mismatch at {path}")
    records[n] = (meta, extract_source(body))

for group, scans in PURE_GROUPS.items():
    actual = [n for n in range(18, 465) if records[n][0].get("section") == group]
    if actual != scans:
        raise SystemExit(f"group scan mismatch for {group}: {actual} != {scans}")

item_scans_by_title = {}
item_order = []
for n in range(18, 465):
    sec = records[n][0].get("section")
    if not sec:
        raise SystemExit(f"missing section metadata at scan {n}")
    if sec in PURE_GROUPS:
        continue
    if sec not in item_scans_by_title:
        item_scans_by_title[sec] = []
        item_order.append(sec)
    item_scans_by_title[sec].append(n)

if len(item_order) != 77:
    raise SystemExit(f"expected 77 item section identities, found {len(item_order)}")

all_item_scans = [n for title in item_order for n in item_scans_by_title[title]]
if len(all_item_scans) != 439 or len(set(all_item_scans)) != 439:
    raise SystemExit(f"item scan accounting mismatch: total={len(all_item_scans)} unique={len(set(all_item_scans))}")

structural_scans = sorted(n for scans in PURE_GROUPS.values() for n in scans)
if sorted(all_item_scans + structural_scans) != list(range(18, 465)):
    raise SystemExit("447-scan body accounting does not close exactly")

if item_scans_by_title.get("அண்ணன் ஒரு கவியரங்கம்") != list(range(230, 237)) + [238]:
    raise SystemExit("item 23 interleave range changed")
if item_scans_by_title.get("தமிழ் வளர வழிநடைப் பயணம்") != [237] + list(range(239, 245)):
    raise SystemExit("item 24 interleave range changed")

gate3 = GATE3.read_text(encoding="utf-8")
exact_region = gate3.split("## Exact-match inventory — 51", 1)[1].split("## Variant inventory — 30", 1)[0]
exact_titles = set(re.findall(r"`([^`\n]+)`", exact_region))

variant_region = gate3.split("## Variant inventory — 30", 1)[1]
variant_pairs = set()
for line in variant_region.splitlines():
    if not re.match(r"^\|\s*\d+\s*\|", line):
        continue
    cells = re.findall(r"`([^`\n]+)`", line)
    if len(cells) >= 2:
        variant_pairs.add((cells[0], cells[1]))
if len(variant_pairs) != 30:
    raise SystemExit(f"expected 30 Gate-3 variant pairs, found {len(variant_pairs)}")

section_files = sorted(SECTIONS.glob("*.md"))
expected_names = [f"{i:02d}.md" for i in range(1, 78)]
actual_names = [p.name for p in section_files]
if actual_names != expected_names:
    raise SystemExit(f"canonical section inventory mismatch: {actual_names}")
if (SECTIONS / "kalaignarin-kavithaigal.md").exists():
    raise SystemExit("obsolete monolithic canonical file still exists")

source_map = SOURCE_MAP.read_text(encoding="utf-8")
variant_item_count = 0
exact_item_count = 0
marker_count = 0
marker_only_count = 0

for i, expected_title in enumerate(item_order, start=1):
    path = SECTIONS / f"{i:02d}.md"
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    expected_scans = item_scans_by_title[expected_title]
    expected_scan_string = compact_ranges(expected_scans)
    expected_printed = compact_ranges([n - 17 for n in expected_scans])

    if meta.get("item") != i:
        raise SystemExit(f"item identity mismatch in {path}: {meta.get('item')}")
    if meta.get("title") != expected_title:
        raise SystemExit(f"title mismatch in {path}: {meta.get('title')!r} != {expected_title!r}")
    if meta.get("title_scan") != expected_scans[0]:
        raise SystemExit(f"title_scan mismatch in {path}")
    if meta.get("physical_scans") != expected_scan_string:
        raise SystemExit(f"physical_scans mismatch in {path}: {meta.get('physical_scans')} != {expected_scan_string}")
    if meta.get("printed_pages") != expected_printed:
        raise SystemExit(f"printed_pages mismatch in {path}: {meta.get('printed_pages')} != {expected_printed}")
    if meta.get("source_filename") != SOURCE_FILENAME:
        raise SystemExit(f"source_filename mismatch in {path}")
    if meta.get("assembly_status") != "assembled-from-verified-pages":
        raise SystemExit(f"assembly_status mismatch in {path}")

    contents_title = meta.get("contents_title")
    if contents_title == expected_title:
        if expected_title not in exact_titles:
            raise SystemExit(f"exact item title not found in Gate-3 exact inventory: item {i} {expected_title}")
        exact_item_count += 1
    else:
        if (contents_title, expected_title) not in variant_pairs:
            raise SystemExit(f"item title variant not authorized by Gate 3: item {i}: {contents_title!r} -> {expected_title!r}")
        variant_item_count += 1

    for n in expected_scans:
        if records[n][0].get("section") != expected_title:
            raise SystemExit(f"cross-item section mismatch: item {i}, scan {n}")

    expected_body_parts = [
        f"# {expected_title}",
        "",
        "<!-- Source assembly from verified page records; source wording and lineation preserved. -->",
        "",
    ]
    for n in expected_scans:
        expected_body_parts.append(f"<!-- scan_page: {n} -->")
        expected_body_parts.append("")
        payload = records[n][1]
        if payload:
            expected_body_parts.append(payload)
            expected_body_parts.append("")
        else:
            marker_only_count += 1
    expected_body = "\n".join(expected_body_parts).rstrip() + "\n"
    actual_body = body.lstrip("\n")
    if actual_body != expected_body:
        raise SystemExit(f"canonical payload mismatch / silent-normalization risk in {path}")

    markers = [int(x) for x in re.findall(r"<!-- scan_page: (\d+) -->", actual_body)]
    if markers != expected_scans:
        raise SystemExit(f"scan marker mismatch in {path}")
    marker_count += len(markers)

    row = (
        f"| {i} | `{expected_title}` | `{contents_title}` | {expected_scans[0]} | "
        f"{expected_scan_string} | {expected_printed} | `sections/{i:02d}.md` |"
    )
    if row not in source_map:
        raise SystemExit(f"source-map item row mismatch for item {i}")

if exact_item_count != 48 or variant_item_count != 29:
    raise SystemExit(f"Gate-3 item title accounting mismatch: exact={exact_item_count} variants={variant_item_count}")
if marker_count != 439:
    raise SystemExit(f"expected 439 item scan markers, found {marker_count}")
if marker_only_count != 2:
    raise SystemExit(f"expected 2 marker-only item scans, found {marker_only_count}")

for title in ("இனமான ஏந்தல்கள்", "கவியரங்கக் கவிதைகள்", "மலர்த் தோட்டம்"):
    if title not in exact_titles:
        raise SystemExit(f"pure group exact witness missing in Gate 3: {title}")
if ("கண்ணீர்க் கவிதை", "கண்ணீர்த் துளிகள்") not in variant_pairs:
    raise SystemExit("Gate-3 pure-group variant missing")

required_group_rows = [
    "| 2 | `இனமான ஏந்தல்கள்` | `இனமான ஏந்தல்கள்` | 2–5 | 32–33 |",
    "| 3 | `கவியரங்கக் கவிதைகள்` | `கவியரங்கக் கவிதைகள்` | 6–38 | 70–71 |",
    "| 4 | `கண்ணீர்க் கவிதை` | `கண்ணீர்த் துளிகள்` | 39–44 | 372–373 |",
    "| 5 | `மலர்த் தோட்டம்` | `மலர்த் தோட்டம்` | 45–77 | 392–393 |",
]
for row in required_group_rows:
    if row not in source_map:
        raise SystemExit(f"missing structural group source-map row: {row}")

for phrase in (
    "indexed poem/items from contents scans **15–17**: **77/77**",
    "scans **18–464 = 447/447**",
    "**439** item-assigned scans exactly once",
    "**8** pure anthology group-divider/verso scans",
    "explicit item-file `scan_page` markers: **439/439**",
):
    if phrase not in source_map:
        raise SystemExit(f"source-map accounting phrase missing: {phrase}")

report = f"""# Phase 3 Canonical Assembly / Source-Completeness Review — Gate 5

Work: **கலைஞரின் கவிதைகள்**  
Controlling source: `{SOURCE_FILENAME}`

## Status

**COMPLETE — PASS.**

The corrected anthology canonical Tamil item set has passed **Phase 3 Gate 5 — assembly/source-completeness review**. Canonical assembly remains **77/77** items, and no source-completeness defect requiring a verified page-record or canonical-item correction was found.

This gate reviews the canonical assembly against the already verified page layer. It does **not** repeat Phase-2 scan-by-scan visual verification. The controlling scan remains the highest textual authority; the locked `pages/NNNN.md` records are the verified textual/structural substrate used for this review.

Review checkpoint before this record was written: live `main` commit `{START_HEAD}`.

## Review inputs

- `POEM_PROCESSING_GUIDE.md`;
- `TRANSCRIPTION_PHASE_PLAN.md`;
- `metadata/source.md`;
- `indexes/page-map.md`;
- `PHASE3_STRUCTURE_AUDIT.md`;
- `PHASE3_BOUNDARY_JOIN_AUDIT.md`;
- `PHASE3_TITLE_WITNESS_RECONCILIATION.md`;
- `PHASE3_CANONICAL_ASSEMBLY.md`;
- `indexes/canonical-source-map.md`;
- canonical items `sections/01.md` through `sections/77.md`;
- verified page layer `pages/0001.md` through `pages/0465.md`.

## 1. Canonical inventory

**PASS — 77/77.**

- stable canonical numbered files: **77/77**, exactly `sections/01.md` through `sections/77.md`;
- missing numbered files: **0**;
- duplicate numbered identities: **0**;
- obsolete monolithic `sections/kalaignarin-kavithaigal.md`: **absent**;
- partial canonical item files: **0**.

The canonical item sequence was independently re-derived from the verified page-layer `section` witnesses, excluding only the four certified pure anthology group-divider identities. That derivation produces exactly **77** unique poem/item identities in source order.

## 2. One-time physical-scan coverage

**PASS — 447/447 body scans accounted exactly once by item or structural role.**

- physical body interval: scans **18–464 = 447**;
- canonical item-assigned scans: **439/439**, unique and non-overlapping;
- pure anthology group-divider/verso scans outside poem files: **8/8**;
- canonical item `scan_page` provenance markers: **439/439**;
- marker-only/non-edition-text scans intentionally retained inside item files: **2**;
- dropped body scans: **0**;
- duplicated body scans: **0**.

The separate structural scans remain exactly:

- `இனமான ஏந்தல்கள்`: **32–33**;
- `கவியரங்கக் கவிதைகள்`: **70–71**;
- `கண்ணீர்த் துளிகள்`: **372–373**;
- `மலர்த் தோட்டம்`: **392–393**.

## 3. Canonical metadata reconciliation

**PASS — 77/77 canonical front-matter records.**

For every `sections/01.md` through `sections/77.md`, Gate 5 independently checked:

- sequential `item` identity;
- canonical `title` against the verified page-layer `section` witness;
- `title_scan`;
- `physical_scans`;
- Gate-1 reconciled logical `printed_pages`;
- controlling `source_filename`;
- `assembly_status: \"assembled-from-verified-pages\"`;
- agreement with the corresponding item row in `indexes/canonical-source-map.md`.

No range gap, overlap, title shift or off-by-one printed-page defect was found.

The intentional physical interposition remains preserved exactly:

- item 23 `அண்ணன் ஒரு கவியரங்கம்`: scans **230–236, 238**, logical pages **213–219, 221**;
- item 24 `தமிழ் வளர வழிநடைப் பயணம்`: scans **237, 239–244**, logical pages **220, 222–227**.

No source page was reordered to make either item artificially contiguous.

## 4. Canonical payload / silent-normalization review

**PASS — 77/77 canonical item payloads match the verified page layer.**

Gate 5 mechanically reconstructed each canonical item's source-facing payload from its certified verified page records and compared it to the canonical file, including exact lineation, punctuation, quotation structure, separators, notes, context/performance text and blank/marker-only provenance.

Result:

- canonical items matching their verified page-derived payload: **77/77**;
- source-facing item scans compared: **439/439**;
- silent lexical normalization detected: **0**;
- dropped source-facing passage detected: **0**;
- duplicated source-facing passage detected: **0**;
- cross-item page contamination detected: **0**.

This is an assembly-completeness comparison against the verified textual layer, not a replacement for the already completed Phase-2 direct visual verification.

## 5. Title-witness preservation

**PASS — all Gate-3 title decisions remain intact.**

Across the 77 poem/items:

- exact contents/opening item witnesses: **48**;
- authorized source-valid item variants: **29**;
- unauthorized/hybrid item titles: **0**.

Pure anthology group witnesses add:

- exact group witnesses: **3**;
- source-valid group variant: **1** — contents `கண்ணீர்க் கவிதை` versus dedicated divider `கண்ணீர்த் துளிகள்`.

Therefore the full Gate-3 accounting remains **51 exact + 30 variants = 81 witnesses**, with **0 unresolved** and **0 hybrid titles**.

Canonical `title` continues to use the dedicated divider/title/opening authority, while `contents_title` preserves the contents witness separately. The contents locator anomaly for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்` remains preserved; canonical item 31 correctly begins at scan **293 / logical printed page 276**.

## 6. High-risk source-order and structural checks

**PASS.**

Gate 5 specifically revalidated the previously locked exceptional structures:

- **236→237→238→239** remains the intentional A→B→A→B interposition;
- item 23 and item 24 carry non-contiguous canonical scan ranges rather than reordered source pages;
- **370→371→372→373→374** remains intact, with the `கண்ணீர்த் துளிகள்` divider/verso kept outside poem files;
- group-divider scans **32–33, 70–71, 372–373, 392–393** are not silently promoted into poem items;
- the earlier Gate-4 source-backed title metadata corrections at scans **406, 409, 457–460** remain authoritative.

No new source-layer discrepancy was exposed by this review.

## Review accounting

- canonical item files: **77/77 — PASS**;
- verified body scan accounting: **447/447 — PASS**;
- item-assigned source scans: **439/439 — PASS**;
- structural group scans: **8/8 — PASS**;
- canonical metadata records: **77/77 — PASS**;
- canonical payload equality against verified page layer: **77/77 — PASS**;
- item title witnesses: **48 exact / 29 variants — PASS**;
- pure group title witnesses: **3 exact / 1 variant — PASS**;
- unresolved source-completeness defects: **0**;
- verified `pages/NNNN.md` records modified during Gate 5: **0**;
- canonical `sections/NN.md` files modified during Gate 5: **0**;
- Tamil final clearance granted during Gate 5: **NO**;
- translation started during Gate 5: **NO**.

## Gate result

**PASS — Phase 3 Gate 5, canonical assembly/source-completeness review, is complete.**

The 77-item canonical Tamil assembly is structurally complete and consistent with the verified page layer, Gate-1 pagination model, Gate-2 boundary certification and Gate-3 title authority.

## Exact next activity

Perform **Phase 3 Gate 6 — Tamil final clearance only**.

That gate must formally confirm Gates 1–5 are PASS and then decide whether to mark the Tamil source/canonical layer final-cleared for Phase 4. **Do not begin English translation in the same activity.**
"""
REPORT.write_text(report, encoding="utf-8")

print(
    "Gate5 PASS: "
    f"items=77; item_scans={len(all_item_scans)}; structural_scans={len(structural_scans)}; "
    f"markers={marker_count}; exact_item_titles={exact_item_count}; variant_item_titles={variant_item_count}; "
    f"marker_only={marker_only_count}; defects=0"
)
