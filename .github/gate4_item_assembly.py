from pathlib import Path
import hashlib
import json
import re

BASE = Path("poems/kalaignarin-kavithaigal")
PAGES = BASE / "pages"
OUT_DIR = BASE / "sections"
SOURCE_FILENAME = "TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf"


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
        "No source text is transcribed on this page."
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


def yaml_quote(value):
    return json.dumps(str(value), ensure_ascii=False)


def md_unescape(value):
    value = value.strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    return value.replace(r'\"', '"').replace(r"\|", "|").strip()


def compress_numbers(nums):
    nums = sorted(set(int(n) for n in nums))
    if not nums:
        return ""
    parts = []
    a = b = nums[0]
    for n in nums[1:]:
        if n == b + 1:
            b = n
            continue
        parts.append(str(a) if a == b else f"{a}–{b}")
        a = b = n
    parts.append(str(a) if a == b else f"{a}–{b}")
    return ", ".join(parts)


def printed_num(value):
    if isinstance(value, int):
        return value
    if isinstance(value, str) and re.fullmatch(r"\d+", value.strip()):
        return int(value.strip())
    return None


def replace_between(path, start_heading, end_heading, replacement):
    text = path.read_text(encoding="utf-8")
    start = text.find(start_heading)
    end = text.find(end_heading, start + len(start_heading))
    if start < 0 or end < 0:
        raise SystemExit(f"cannot replace section in {path}: {start_heading!r} -> {end_heading!r}")
    new = text[:start] + replacement.rstrip() + "\n\n" + text[end:]
    path.write_text(new, encoding="utf-8")


records = []
for n in range(1, 466):
    path = PAGES / f"{n:04d}.md"
    if not path.exists():
        raise SystemExit(f"missing page record {path}")
    text = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    if meta.get("scan_page") != n:
        raise SystemExit(f"scan_page mismatch in {path}: {meta.get('scan_page')}")
    if meta.get("status") != "verified":
        raise SystemExit(f"non-verified page record {path}: {meta.get('status')}")
    records.append((meta, extract_source(body)))

items = []
groups = {}
current_group = None
for scan in (15, 16, 17):
    text = (PAGES / f"{scan:04d}.md").read_text(encoding="utf-8")
    blocks = re.findall(r"```text\n(.*?)\n```", text, flags=re.S)
    if len(blocks) != 1:
        raise SystemExit(f"expected one contents text block at scan {scan}, found {len(blocks)}")
    for raw_line in blocks[0].splitlines():
        line = raw_line.strip()
        if not line or line == "பக்கம்":
            continue
        item_match = re.match(r"^(?:(\d+)\.\s+)?(.+?)\s+(\d+)\s*$", line)
        if item_match:
            prefix, title, locator = item_match.groups()
            title = title.strip()
            if prefix:
                current_group = int(prefix)
                groups[current_group] = {"contents_title": title, "contents_scan": scan}
            if current_group is None:
                raise SystemExit(f"item before group at contents scan {scan}: {line}")
            items.append({"item": len(items) + 1, "contents_title": title, "contents_locator": int(locator), "contents_scan": scan, "group": current_group})
            continue
        group_match = re.match(r"^(\d+)\.\s+(.+?)\s*$", line)
        if group_match:
            current_group = int(group_match.group(1))
            groups[current_group] = {"contents_title": group_match.group(2).strip(), "contents_scan": scan}

if len(items) != 77:
    raise SystemExit(f"expected 77 indexed poem/items, found {len(items)}")
if sorted(groups) != [1, 2, 3, 4, 5]:
    raise SystemExit(f"expected anthology groups 1-5, found {sorted(groups)}")

gate3 = (BASE / "PHASE3_TITLE_WITNESS_RECONCILIATION.md").read_text(encoding="utf-8")
variant_lines = [ln for ln in gate3.splitlines() if re.match(r"^\|\s*\d+\s*\|", ln)]
if len(variant_lines) != 30:
    raise SystemExit(f"expected 30 Gate-3 variants, found {len(variant_lines)}")
variant_map = {}
for line in variant_lines:
    parts = [p.strip() for p in line.strip().strip("|").split("|")]
    if len(parts) < 5:
        raise SystemExit(f"malformed Gate-3 variant row: {line}")
    contents = md_unescape(parts[1])
    canonical = md_unescape(parts[2])
    variant_map[contents] = canonical

for item in items:
    item["title"] = variant_map.get(item["contents_title"], item["contents_title"])
for g in groups.values():
    g["title"] = variant_map.get(g["contents_title"], g["contents_title"])
if len({i["title"] for i in items}) != 77:
    raise SystemExit("canonical item titles are not unique")

section_to_scans = {}
for scan in range(18, 465):
    meta = records[scan - 1][0]
    section_to_scans.setdefault(meta.get("section"), []).append(scan)

for item in items:
    scans = section_to_scans.get(item["title"], [])
    if not scans:
        raise SystemExit(f"no verified page records for item {item['item']}: {item['title']}")
    item["scans"] = scans
    item["title_scan"] = min(scans)
    visible_pages = [printed_num(records[s - 1][0].get("printed_page")) for s in scans]
    item["printed_pages"] = [p for p in visible_pages if p is not None]

structural_group_scans = {}
for gnum in (2, 3, 4, 5):
    title = groups[gnum]["title"]
    scans = section_to_scans.get(title, [])
    if not scans:
        raise SystemExit(f"missing structural scans for anthology group {gnum}: {title}")
    structural_group_scans[gnum] = scans

assigned = set()
for item in items:
    overlap = assigned.intersection(item["scans"])
    if overlap:
        raise SystemExit(f"canonical item scan overlap at {sorted(overlap)}")
    assigned.update(item["scans"])
structural = set()
for scans in structural_group_scans.values():
    structural.update(scans)
body_scans = set(range(18, 465))
if assigned.intersection(structural):
    raise SystemExit(f"item/structural scan overlap: {sorted(assigned.intersection(structural))}")
if assigned.union(structural) != body_scans:
    missing = sorted(body_scans - assigned - structural)
    extra = sorted((assigned | structural) - body_scans)
    raise SystemExit(f"body accounting mismatch; missing={missing}, extra={extra}")
if len(assigned) != 439 or len(structural) != 8:
    raise SystemExit(f"expected 439 item scans + 8 structural scans, found {len(assigned)} + {len(structural)}")

by_title = {i["title"]: i for i in items}
if by_title["அண்ணன் ஒரு கவியரங்கம்"]["scans"] != list(range(230, 237)) + [238]:
    raise SystemExit("அண்ணன் ஒரு கவியரங்கம் non-contiguous scan ownership mismatch")
if by_title["தமிழ் வளர வழிநடைப் பயணம்"]["scans"] != [237] + list(range(239, 245)):
    raise SystemExit("தமிழ் வளர வழிநடைப் பயணம் non-contiguous scan ownership mismatch")

runs = []
start = 18
cur = records[17][0].get("section")
types = []
for scan in range(18, 465):
    meta = records[scan - 1][0]
    sec = meta.get("section")
    if sec != cur:
        runs.append((start, scan - 1, cur, sorted(set(types))))
        start = scan
        cur = sec
        types = []
    types.append(str(meta.get("page_type", "")))
runs.append((start, 464, cur, sorted(set(types))))
if len(runs) != 83:
    raise SystemExit(f"expected 83 physical section runs, found {len(runs)}")

OUT_DIR.mkdir(exist_ok=True)
existing = sorted(p.name for p in OUT_DIR.glob("*.md"))
allowed_existing = {"kalaignarin-kavithaigal.md"} | {f"{n:02d}.md" for n in range(1, 78)}
unexpected = [name for name in existing if name not in allowed_existing]
if unexpected:
    raise SystemExit(f"unexpected active section files: {unexpected}")
for p in OUT_DIR.glob("*.md"):
    p.unlink()

manifest_lines = []
marker_only_item_scans = 0
for item in items:
    physical_scans = compress_numbers(item["scans"])
    printed_pages = compress_numbers(item["printed_pages"])
    front = ["---", f"item: {item['item']}", f"title: {yaml_quote(item['title'])}", f"contents_title: {yaml_quote(item['contents_title'])}", f"title_scan: {item['title_scan']}", f"physical_scans: {yaml_quote(physical_scans)}", f"printed_pages: {yaml_quote(printed_pages)}", f"source_filename: {yaml_quote(SOURCE_FILENAME)}", 'assembly_status: "assembled-from-verified-pages"', "---", "", f"# {item['title']}", "", "<!-- Source assembly from verified page records; source wording and lineation preserved. -->", ""]
    body = []
    for scan in item["scans"]:
        source = records[scan - 1][1]
        body.append(f"<!-- scan_page: {scan} -->")
        body.append("")
        if source:
            body.append(source)
            body.append("")
        else:
            marker_only_item_scans += 1
    text = "\n".join(front + body).rstrip() + "\n"
    filename = f"{item['item']:02d}.md"
    (OUT_DIR / filename).write_text(text, encoding="utf-8")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    item["sha256"] = digest
    manifest_lines.append(f"{filename}  {digest}")

manifest_text = "\n".join(manifest_lines) + "\n"
manifest_sha = hashlib.sha256(manifest_text.encode("utf-8")).hexdigest()
item_variant_count = sum(1 for i in items if i["contents_title"] in variant_map)
group_only_variant_count = len(variant_map) - item_variant_count

source_map = ["# Canonical source map — கலைஞரின் கவிதைகள்", "", "Phase 3 Gate 4 canonical poem/item outputs: `../sections/01.md` through `../sections/77.md`.", "", "- indexed poem/items from contents scans **15–17**: **77/77**;", "- verified physical source body accounted: scans **18–464 = 447/447**;", "- canonical item files cover **439** item-assigned scans exactly once;", "- **8** pure anthology group-divider/verso scans are structural provenance outside poem files and are accounted below;", "- explicit item-file `scan_page` markers: **439/439**;", f"- marker-only/non-edition-text scans retained inside item files: **{marker_only_item_scans}**;", "- stable canonical filenames: `01.md` … `77.md`;", "- physical source order remains authoritative; item files may therefore carry non-contiguous scan ranges where the source interleaves works;", "- canonical title authority is the Gate-3 dedicated divider/title/opening witness; contents variants remain separate source witnesses.", "", "## Anthology group structure", "", "| Group | Contents witness | Canonical group authority | Item range | Separate structural scans |", "|---:|---|---|---:|---:|"]
for gnum in range(1, 6):
    member_nums = [i["item"] for i in items if i["group"] == gnum]
    item_range = str(member_nums[0]) if len(member_nums) == 1 else f"{member_nums[0]}–{member_nums[-1]}"
    structural_display = "shares item 01; scans 18–19 retained within item 01" if gnum == 1 else compress_numbers(structural_group_scans[gnum])
    source_map.append(f"| {gnum} | `{groups[gnum]['contents_title']}` | `{groups[gnum]['title']}` | {item_range} | {structural_display} |")
source_map += ["", "## Canonical item inventory", "", "| Item | Canonical title | Contents title | Title scan | Physical scans | Printed pages | File |", "|---:|---|---|---:|---:|---:|---|"]
for item in items:
    title = item["title"].replace("|", r"\|")
    contents_title = item["contents_title"].replace("|", r"\|")
    source_map.append(f"| {item['item']} | `{title}` | `{contents_title}` | {item['title_scan']} | {compress_numbers(item['scans'])} | {compress_numbers(item['printed_pages'])} | `sections/{item['item']:02d}.md` |")
source_map += ["", "## Structural anthology scans outside poem/item files", "", "These scans remain verified source records and are intentionally **not duplicated** into neighboring poem files.", "", "| Group | Canonical group witness | Physical scans |", "|---:|---|---:|"]
for gnum in (2, 3, 4, 5):
    source_map.append(f"| {gnum} | `{groups[gnum]['title']}` | {compress_numbers(structural_group_scans[gnum])} |")
source_map += ["", "## Physical-order section runs", "", "| Scan run | Canonical verified `section` witness | Page type(s) |", "|---:|---|---|"]
for a, b, sec, pts in runs:
    rng = str(a) if a == b else f"{a}–{b}"
    sec_cell = str(sec).replace("|", r"\|")
    source_map.append(f"| {rng} | `{sec_cell}` | {', '.join(pts)} |")
table_start = gate3.find("| # | Contents witness | Dedicated divider/title/opening witness |")
anomaly_start = gate3.find("## Contents locator anomaly recorded during Gate 3")
if table_start < 0 or anomaly_start < 0 or anomaly_start <= table_start:
    raise SystemExit("cannot recover Gate-3 variant table")
variant_table = gate3[table_start:anomaly_start].rstrip()
source_map += ["", "## Contents/title witness variants retained from Gate 3", "", variant_table, "", "## Gate-3 contents locator anomaly retained", "", "Contents scan 16 points `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்` to printed page **279**; the verified dedicated opening is scan **293 / printed page 276**. Item assembly follows the verified opening and does not rewrite the contents witness.", "", "## Canonical item SHA-256 manifest", "", f"Manifest SHA-256: `{manifest_sha}`", "", "```text", manifest_text.rstrip(), "```", ""]
(BASE / "indexes" / "canonical-source-map.md").write_text("\n".join(source_map), encoding="utf-8")

report = f'''# Phase 3 Canonical Tamil Assembly — Gate 4

Work: **கலைஞரின் கவிதைகள்**
Controlling source: `{SOURCE_FILENAME}`

## Scope

This record closes **Phase 3 Gate 4 — canonical Tamil assembly only** after correcting the anthology output model. It does not perform Gate 5 assembly/source-completeness review, Tamil final clearance, translation or release work.

## Result

**PASS — 77/77 indexed poem/items assembled as stable canonical item files from the verified page layer.**

- page layer checked: **465/465 `verified`**;
- contents-derived canonical item inventory: **77/77**;
- canonical outputs: `sections/01.md` through `sections/77.md`;
- verified body interval accounted: **18–464 = 447/447 physical scans**;
- item-assigned canonical scan coverage: **439/439**, with no overlaps or omissions;
- pure anthology group-divider/verso structural scans outside poem files: **8/8**, explicitly retained in `indexes/canonical-source-map.md`;
- explicit item-file `scan_page` provenance markers: **439/439**;
- marker-only/non-edition-text scans retained inside item files: **{marker_only_item_scans}**;
- physical source section runs retained in provenance: **83**;
- Gate-3 title variants retained separately: **30/30** (**{item_variant_count} item variants + {group_only_variant_count} pure-group variant**);
- stable filenames: `01.md` … `77.md`;
- canonical item-manifest SHA-256: `{manifest_sha}`;
- verified page-record lexical changes made by this structural correction: **0**.

## Correction of the earlier Gate-4 representation

The earlier Gate-4 pass emitted one whole-volume file, `sections/kalaignarin-kavithaigal.md`. That representation was structurally inappropriate for this anthology and has been removed.

The corrected assembly follows the repository's established multi-item convention used by works such as `kaalap-pezhaiyum-kavithai-saaviyum`: one stable numeric canonical file per indexed poem/item, while anthology group dividers remain separate structural provenance.

This correction changes **assembly structure only**. It does not retranscribe or normalize poem wording.

## Interleaved physical-source exception

The verified source intentionally interleaves two poems:

- `அண்ணன் ஒரு கவியரங்கம்` → scans **230–236, 238**;
- `தமிழ் வளர வழிநடைப் பயணம்` → scans **237, 239–244**.

Their canonical item files preserve those non-contiguous physical scan ranges explicitly. No physical source page is reordered or duplicated.

The certified **370→371→372→373→374** sequence is also preserved: item text/verso through scan 371, then the separate `கண்ணீர்த் துளிகள்` divider/verso on scans 372–373, then item assembly resumes at scan 374.

## Gate-4 title authority

Gate-3 authority remains unchanged:

- dedicated divider/title/opening witnesses control canonical `title`;
- contents wording is retained separately as `contents_title`;
- no hybrid title is created;
- the contents locator anomaly for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்` remains preserved, while the canonical item begins at verified scan 293 / printed page 276.

The earlier source-backed metadata corrections at scans **406, 409 and 457–460** remain in force. This structural correction required **no further page-record changes**.

## Gate closure

**Phase 3 Gate 4 is COMPLETE / PASS — corrected canonical form is 77/77 numbered item files.**

## Exact next gate

Proceed to **Phase 3 Gate 5 — assembly/source-completeness review only**. Review all 77 canonical item files plus the structural group-scan accounting against the verified page layer for one-time coverage, exclusions, title authority, source-order fidelity, source-note preservation and silent-normalization risk.

Do **not** grant Tamil final clearance or begin translation/release work in that same activity.
'''
(BASE / "PHASE3_CANONICAL_ASSEMBLY.md").write_text(report, encoding="utf-8")

gate4_block = f'''## Gate 4 — canonical Tamil assembly

**COMPLETE / PASS — corrected anthology item model.**

- indexed poem/items: **77/77**;
- canonical outputs: `sections/01.md` through `sections/77.md`;
- source map: `indexes/canonical-source-map.md`;
- audit: `PHASE3_CANONICAL_ASSEMBLY.md`;
- verified body interval accounted: **18–464 = 447/447 scans**;
- canonical item scan coverage: **439/439**;
- pure anthology group-divider/verso scans outside poem files: **8/8**, separately accounted;
- explicit item-file scan provenance: **439/439**;
- physical source section runs retained: **83**;
- Gate-3 variants preserved separately: **30/30**;
- canonical item-manifest SHA-256: `{manifest_sha}`.

The earlier single whole-volume file was a structural assembly error for an anthology and has been removed. Gate 4 now follows the repository's multi-item convention: one stable numeric file per indexed poem/item. The intentional `அண்ணன் ஒரு கவியரங்கம்` / `தமிழ் வளர வழிநடைப் பயணம்` interposition is represented as non-contiguous scan ranges rather than reordered source pages.

The earlier Gate-4 source-backed title corrections at scans **406, 409, 457–460** remain valid. This structural correction changed **0** verified poem words and modified **0** page records.'''
replace_between(BASE / "README.md", "## Gate 4 — canonical Tamil assembly", "## Next activity", gate4_block)

audit_block = f'''## Phase 3 Gate 4 audit — COMPLETE / PASS

Scope: **canonical Tamil anthology item assembly only**.

### Final accounting

- eligible page records checked: **465/465 `verified`**;
- indexed poem/item inventory: **77/77**;
- canonical outputs: `sections/01.md` through `sections/77.md`;
- verified body interval accounted: **scans 18–464 = 447/447**;
- canonical item scan coverage: **439/439**, exactly once;
- pure anthology group-divider/verso scans outside poem files: **8/8**, separately accounted;
- explicit item-file `scan_page` markers: **439/439**;
- physical source section runs retained: **83**;
- Gate-3 source-valid variants retained separately: **30/30**;
- source map: `indexes/canonical-source-map.md`;
- Gate-4 evidence: `PHASE3_CANONICAL_ASSEMBLY.md`;
- canonical item-manifest SHA-256: `{manifest_sha}`.

### Structural correction during Gate 4

The earlier whole-volume `sections/kalaignarin-kavithaigal.md` representation was reopened because this source is an anthology. It has been removed and replaced with **77 stable numeric poem/item files**, matching the established multi-item repository convention.

The source's intentional interposition is preserved without reordering:

- `அண்ணன் ஒரு கவியரங்கம்`: scans **230–236, 238**;
- `தமிழ் வளர வழிநடைப் பயணம்`: scans **237, 239–244**.

The four later pure anthology group dividers/versos account for the eight body scans not duplicated into poem files.

### Source-record integrity

The earlier source-backed title metadata corrections at scans **406, 409 and 457–460** remain valid. The anthology-structure correction made **0 poem-body lexical changes** and modified **0 verified page records**. All **465/465** records remain `verified`.

### Gate result

**Gate 4 PASS — corrected canonical form is 77/77 item files.**'''
replace_between(BASE / "audit.md", "## Phase 3 Gate 4 audit — COMPLETE / PASS", "## Next audit gate", audit_block)

handover_block = f'''## Gate 4 durable result

Gate-4 evidence: `poems/kalaignarin-kavithaigal/PHASE3_CANONICAL_ASSEMBLY.md`.

Canonical outputs:

- `poems/kalaignarin-kavithaigal/sections/01.md` through `sections/77.md`;
- `poems/kalaignarin-kavithaigal/indexes/canonical-source-map.md`.

Locked accounting:

- indexed poem/items: **77/77**;
- body interval accounted: **18–464 = 447/447 physical scans**;
- canonical item scan coverage: **439/439**;
- pure anthology group-divider/verso structural scans outside poem files: **8/8**;
- explicit item-file scan provenance: **439/439**;
- physical source section runs retained: **83**;
- Gate-3 variants preserved separately: **30/30**;
- canonical item-manifest SHA-256: `{manifest_sha}`.

The earlier single `sections/kalaignarin-kavithaigal.md` file was reopened as a structural error because this source is an anthology. It has been removed and replaced with one stable numeric canonical file per indexed poem/item, following the repository's established multi-item convention.

The intentional physical interposition is preserved explicitly: `அண்ணன் ஒரு கவியரங்கம்` uses scans **230–236, 238** and `தமிழ் வளர வழிநடைப் பயணம்` uses scans **237, 239–244**. No source page was reordered.

The earlier source-backed title corrections in verified records **0406, 0409 and 0457–0460** remain authoritative. This structural correction changed **0** poem-body words and modified **0** page records; all 465 records remain `verified`.'''
replace_between(Path("HANDOVER.md"), "## Gate 4 durable result", "## Supplied-transcription rule", handover_block)
handover_path = Path("HANDOVER.md")
handover_text = handover_path.read_text(encoding="utf-8")
old = "16. canonical output `sections/kalaignarin-kavithaigal.md` as needed for Gate-5 review."
new = "16. canonical item files `sections/01.md` through `sections/77.md` as needed for Gate-5 review."
if old not in handover_text:
    raise SystemExit("HANDOVER mandatory-startup canonical-output line not found")
handover_path.write_text(handover_text.replace(old, new), encoding="utf-8")

prompt_block = f'''## Gate 4 durable output

- canonical poem/items: **77/77**;
- canonical files: `sections/01.md` through `sections/77.md`;
- provenance/source map: `indexes/canonical-source-map.md`;
- Gate-4 audit: `PHASE3_CANONICAL_ASSEMBLY.md`;
- verified body interval accounted: **18–464 = 447/447 scans**;
- canonical item scan coverage: **439/439**;
- pure anthology group-divider/verso scans outside item files: **8/8**, separately accounted;
- explicit item-file scan provenance: **439/439**;
- physical source section runs: **83**;
- Gate-3 variants preserved: **30/30**;
- canonical item-manifest SHA-256: `{manifest_sha}`.

The former whole-volume `sections/kalaignarin-kavithaigal.md` output was a structural error for this anthology and has been removed. The corrected Gate-4 layer follows the established repository pattern of one stable numeric file per indexed poem/item.

Preserve the non-contiguous physical ownership exactly: `அண்ணன் ஒரு கவியரங்கம்` = **230–236, 238**; `தமிழ் வளர வழிநடைப் பயணம்` = **237, 239–244**. The structural correction made **0** verified poem-word changes and **0** page-record changes.'''
replace_between(Path("NEXT_CHAT_PROMPT.md"), "## Gate 4 durable output", "## Locked Phase 3 structure", prompt_block)

phase_path = Path("TRANSCRIPTION_PHASE_PLAN.md")
phase_text = phase_path.read_text(encoding="utf-8")
start = phase_text.find("4. **Canonical Tamil assembly — COMPLETE / PASS.**")
end = phase_text.find("5. **Assembly/source-completeness review — NEXT / NOT STARTED.**", start)
if start < 0 or end < 0:
    raise SystemExit("cannot replace Phase-3 Gate-4 list block")
phase_gate4 = f'''4. **Canonical Tamil assembly — COMPLETE / PASS — corrected anthology item model.**
   - verified substrate: **465/465**;
   - indexed poem/items: **77/77**;
   - canonical outputs: `poems/kalaignarin-kavithaigal/sections/01.md` through `sections/77.md`;
   - verified body interval accounted: **18–464 = 447/447 physical scans**;
   - canonical item scan coverage: **439/439**;
   - pure anthology group-divider/verso scans outside item files: **8/8**;
   - explicit item-file `scan_page` provenance: **439/439**;
   - physical source section runs retained: **83**;
   - Gate-3 variants retained separately: **30/30**;
   - source map: `poems/kalaignarin-kavithaigal/indexes/canonical-source-map.md`;
   - evidence: `poems/kalaignarin-kavithaigal/PHASE3_CANONICAL_ASSEMBLY.md`;
   - canonical item-manifest SHA-256: `{manifest_sha}`.
'''
phase_text = phase_text[:start] + phase_gate4 + phase_text[end:]
phase_path.write_text(phase_text, encoding="utf-8")
phase_correction = '''## Gate-4 correction record

The earlier single whole-volume canonical file was reopened as a structural error for an anthology. Gate 4 now emits **77/77** stable numbered item files and separately accounts for the four later pure anthology group-divider/verso pairs. The intentional 230–244 interposition is represented with non-contiguous item scan ranges rather than source reordering.

Earlier source-backed title metadata corrections at scans **406, 409, 457–460** remain in force. The structural correction made **0** additional page-record or poem-word changes.'''
replace_between(phase_path, "## Gate-4 correction record", "## EXACT NEXT ACTIVITY", phase_correction)

source_intake_block = f'''## Gate 4 result

Canonical outputs: `sections/01.md` through `sections/77.md`. Source map: `indexes/canonical-source-map.md`. Evidence: `PHASE3_CANONICAL_ASSEMBLY.md`.

- indexed poem/items **77/77**;
- verified body interval accounted **18–464 = 447/447**;
- canonical item scan coverage **439/439**;
- pure anthology group-divider/verso structural scans outside item files **8/8**;
- explicit item-file `scan_page` markers **439/439**;
- physical source section runs **83**;
- Gate-3 variants retained **30/30**;
- canonical item-manifest SHA-256 `{manifest_sha}`.

The earlier monolithic canonical file was removed after reopening Gate 4 for anthology structure. The corrected layer uses one stable numbered file per indexed poem/item. No verified poem wording or page record was changed by this structural correction.'''
replace_between(BASE / "SOURCE_INTAKE.md", "## Gate 4 result", "## Next phase gate", source_intake_block)

metadata_path = BASE / "metadata" / "source.md"
metadata_text = metadata_path.read_text(encoding="utf-8")
start = metadata_text.find("## Gate 4 canonical assembly metadata")
if start < 0:
    raise SystemExit("metadata Gate-4 section not found")
metadata_block = f'''## Gate 4 canonical assembly metadata

- canonical items: **77/77**;
- canonical files: `../sections/01.md` through `../sections/77.md`;
- canonical source map: `../indexes/canonical-source-map.md`;
- Gate-4 evidence: `../PHASE3_CANONICAL_ASSEMBLY.md`;
- verified body interval accounted: **18–464 = 447/447 scans**;
- canonical item scan coverage: **439/439**;
- pure anthology group-divider/verso structural scans outside item files: **8/8**;
- explicit item-file scan provenance: **439/439**;
- physical source section runs: **83**;
- Gate-3 variants retained separately: **30/30**;
- canonical item-manifest SHA-256: `{manifest_sha}`.

The earlier monolithic `../sections/kalaignarin-kavithaigal.md` representation was removed after Gate 4 was reopened for anthology structure. The corrected assembly follows the repository's multi-item convention with one stable numeric file per indexed poem/item. No verified page text was changed by this structural correction.

Earlier source-backed title metadata corrections at scans **406, 409 and 457–460** remain authoritative; every page record remains `verified`.
'''
metadata_path.write_text(metadata_text[:start] + metadata_block, encoding="utf-8")

page_map_block = f'''## Phase 3 Gate 4 — canonical Tamil assembly COMPLETE / PASS

Canonical outputs: `../sections/01.md` through `../sections/77.md`.

Canonical provenance map: `canonical-source-map.md`.

Gate-4 evidence: `../PHASE3_CANONICAL_ASSEMBLY.md`.

- indexed poem/items: **77/77**;
- verified body interval accounted: **18–464 = 447/447**;
- canonical item scan coverage: **439/439**;
- pure anthology group-divider/verso scans outside item files: **8/8**;
- explicit item-file `scan_page` markers: **439/439**;
- physical source section runs: **83**;
- Gate-3 title variants retained in provenance: **30/30**;
- canonical item-manifest SHA-256: `{manifest_sha}`.

The earlier monolithic canonical file was removed after Gate 4 was reopened for anthology structure. The corrected assembly uses 77 stable numeric item files. The intentional `230–236, 238` / `237, 239–244` interposition is represented without reordering. No verified poem wording or page record changed.'''
replace_between(BASE / "indexes" / "page-map.md", "## Phase 3 Gate 4 — canonical Tamil assembly COMPLETE / PASS", "## Phase status", page_map_block)

root_path = Path("README.md")
root_text = root_path.read_text(encoding="utf-8")
pattern = re.compile(r"Gate 4 assembles verified body scans \*\*18–464\*\* into `poems/kalaignarin-kavithaigal/sections/kalaignarin-kavithaigal\.md`.*?Neighboring boundaries remained valid and poem-body lexical wording was unchanged\.\n", flags=re.S)
root_replacement = f'''Gate 4 assembles the anthology as **77/77 stable canonical poem/item files**, `poems/kalaignarin-kavithaigal/sections/01.md` through `sections/77.md`. The verified body interval scans **18–464 = 447/447** is fully accounted: **439** item-assigned scans occur exactly once in canonical item files and **8** later anthology group-divider/verso scans remain separate structural provenance in `indexes/canonical-source-map.md`. The item-manifest SHA-256 is `{manifest_sha}`.

The earlier single whole-volume canonical file was reopened as a structural error for an anthology and removed. The corrected Gate-4 layer follows the repository's established multi-item pattern while preserving the source's intentional interposition (`அண்ணன் ஒரு கவியரங்கம்`: **230–236, 238**; `தமிழ் வளர வழிநடைப் பயணம்`: **237, 239–244**) without reordering. Earlier source-backed title corrections at scans **406, 409, 457–460** remain valid; the structural correction changed no verified poem wording or page records.
'''
root_text, count = pattern.subn(root_replacement, root_text, count=1)
if count != 1:
    raise SystemExit(f"root README Gate-4 prose replacement count={count}")
root_path.write_text(root_text, encoding="utf-8")

print(f"corrected Gate4 anthology assembly: items={len(items)}; item_scans={len(assigned)}; structural_scans={len(structural)}; marker_only_item_scans={marker_only_item_scans}; section_runs={len(runs)}; manifest_sha256={manifest_sha}")
