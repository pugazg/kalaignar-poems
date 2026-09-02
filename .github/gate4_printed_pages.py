from pathlib import Path
import hashlib
import json
import re

BASE = Path("poems/kalaignarin-kavithaigal")
SECTIONS = BASE / "sections"
PAGES = BASE / "pages"
OLD_MANIFEST_SHA = "69635ca2edc7c5dc0f0ada58881d05e33ba462c7891b095ad3638c4dbf22d310"


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
    return meta, end


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


def expand_ranges(value):
    out = []
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "–" in part:
            a, b = part.split("–", 1)
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out

page_types = {}
for scan in range(18, 465):
    text = (PAGES / f"{scan:04d}.md").read_text(encoding="utf-8")
    meta, _ = parse_frontmatter(text)
    if meta.get("scan_page") != scan or meta.get("status") != "verified":
        raise SystemExit(f"page metadata/status mismatch at scan {scan}")
    page_types[scan] = str(meta.get("page_type", ""))

items = []
for n in range(1, 78):
    path = SECTIONS / f"{n:02d}.md"
    if not path.exists():
        raise SystemExit(f"missing canonical item file {path}")
    text = path.read_text(encoding="utf-8")
    meta, _ = parse_frontmatter(text)
    scans = expand_ranges(meta["physical_scans"])
    logical_pages = [scan - 17 for scan in scans if page_types[scan] not in {"section-divider", "verso"}]
    printed_pages = compress_numbers(logical_pages)
    text, count = re.subn(r'^printed_pages:\s*".*?"\s*$', f'printed_pages: {json.dumps(printed_pages, ensure_ascii=False)}', text, count=1, flags=re.M)
    if count != 1:
        raise SystemExit(f"printed_pages replacement failed for {path}")
    path.write_text(text, encoding="utf-8")
    meta["printed_pages"] = printed_pages
    items.append((n, meta, scans, path))

spots = {1: "3–14", 2: "17–25", 23: "213–219, 221", 24: "220, 222–227", 31: "276–279", 38: "345–353", 77: "444–447"}
for n, expected in spots.items():
    actual = items[n - 1][1]["printed_pages"]
    if actual != expected:
        raise SystemExit(f"reconciled printed_pages mismatch item {n}: {actual!r} != {expected!r}")

manifest_lines = []
for n, meta, scans, path in items:
    text = path.read_text(encoding="utf-8")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    manifest_lines.append(f"{n:02d}.md  {digest}")
manifest_text = "\n".join(manifest_lines) + "\n"
manifest_sha = hashlib.sha256(manifest_text.encode("utf-8")).hexdigest()

source_map_path = BASE / "indexes" / "canonical-source-map.md"
source_map = source_map_path.read_text(encoding="utf-8")
start = source_map.find("## Canonical item inventory")
end = source_map.find("## Structural anthology scans outside poem/item files", start)
if start < 0 or end < 0:
    raise SystemExit("canonical item inventory section not found")
inventory = ["## Canonical item inventory", "", "`printed_pages` below uses the Gate-1 reconciled logical Arabic pagination. The page-layer `printed_page` field remains source-visible only and is not backfilled.", "", "| Item | Canonical title | Contents title | Title scan | Physical scans | Printed pages | File |", "|---:|---|---|---:|---:|---:|---|"]
for n, meta, scans, path in items:
    title = str(meta["title"]).replace("|", r"\|")
    contents = str(meta["contents_title"]).replace("|", r"\|")
    inventory.append(f"| {n} | `{title}` | `{contents}` | {meta['title_scan']} | {meta['physical_scans']} | {meta['printed_pages']} | `sections/{n:02d}.md` |")
source_map = source_map[:start] + "\n".join(inventory).rstrip() + "\n\n" + source_map[end:]

manifest_start = source_map.find("## Canonical item SHA-256 manifest")
if manifest_start < 0:
    raise SystemExit("canonical manifest section not found")
manifest_section = ["## Canonical item SHA-256 manifest", "", f"Manifest SHA-256: `{manifest_sha}`", "", "```text", manifest_text.rstrip(), "```", ""]
source_map = source_map[:manifest_start] + "\n".join(manifest_section)
source_map_path.write_text(source_map, encoding="utf-8")

status_paths = [BASE / "PHASE3_CANONICAL_ASSEMBLY.md", BASE / "README.md", BASE / "audit.md", Path("HANDOVER.md"), Path("NEXT_CHAT_PROMPT.md"), Path("TRANSCRIPTION_PHASE_PLAN.md"), BASE / "SOURCE_INTAKE.md", BASE / "metadata" / "source.md", BASE / "indexes" / "page-map.md", Path("README.md")]
for path in status_paths:
    text = path.read_text(encoding="utf-8")
    if OLD_MANIFEST_SHA not in text:
        raise SystemExit(f"old manifest SHA not found in {path}")
    path.write_text(text.replace(OLD_MANIFEST_SHA, manifest_sha), encoding="utf-8")

report_path = BASE / "PHASE3_CANONICAL_ASSEMBLY.md"
report = report_path.read_text(encoding="utf-8")
anchor = "- stable filenames: `01.md` … `77.md`;\n"
note = "- canonical `printed_pages` metadata follows the Gate-1 reconciled logical Arabic pagination; source-visible `printed_page` values in page records remain unchanged;\n"
if note not in report:
    if anchor not in report:
        raise SystemExit("Gate-4 report printed-page note anchor missing")
    report = report.replace(anchor, anchor + note, 1)
report_path.write_text(report, encoding="utf-8")

handover_path = Path("HANDOVER.md")
handover = handover_path.read_text(encoding="utf-8")
anchor = "- canonical item-manifest SHA-256:"
note_line = "- canonical item `printed_pages` uses Gate-1 reconciled logical pagination; page-record `printed_page` remains source-visible only;\n"
if note_line not in handover:
    pos = handover.find(anchor)
    if pos < 0:
        raise SystemExit("HANDOVER printed-page note anchor missing")
    line_end = handover.find("\n", pos)
    handover = handover[:line_end + 1] + note_line + handover[line_end + 1:]
handover_path.write_text(handover, encoding="utf-8")

print(f"aligned canonical printed_pages with Gate1 logical pagination; manifest_sha256={manifest_sha}")
