# Phase 3 canonical assembly / source-completeness review — காலப் பேழையும் கவிதைச் சாவியும்

## Status

**COMPLETE — PASS.**

The complete canonical Tamil item set has passed the Phase-3 assembly/source-completeness gate. Canonical assembly remains **58/58** items, and no source-completeness defect requiring a page-record correction was found during this review.

This gate reviews the canonical assembly against the already verified source layer. It does **not** repeat the Phase-2 pixel-level rereading of all 306 scans: the controlling scan remains the highest textual authority, while the locked `pages/NNNN.md` records remain the verified text layer used for assembly.

## Review inputs

- controlling source metadata: `metadata/source.md`;
- certified scan / printed-page ranges: `indexes/page-map.md`;
- contents/title index: `indexes/item-title-map.md`;
- complete boundary / page-join certification: `PHASE3_BOUNDARY_JOIN_AUDIT.md`;
- title-witness authority decisions: `PHASE3_TITLE_WITNESS_RECONCILIATION.md`;
- canonical assembly tracker: `PHASE3_CANONICAL_ASSEMBLY.md`;
- canonical item files: `sections/01.md` through `sections/58.md`;
- verified page layer: `pages/0001.md` through `pages/0306.md`.

Review checkpoint before this record was written: live `main` commit `12bc852e30b3a7424b88e5ae066d447c90e974c8`.

## 1. Canonical inventory

**PASS.**

The live repository tree contains the complete stable sequence:

- first canonical file: `sections/01.md`;
- last canonical file: `sections/58.md`;
- canonical numbered files present: **58/58**;
- missing numbered canonical files: **0**;
- duplicate numbered canonical identities: **0**;
- partial canonical item files: **0**.

The certified numbered-item source block is continuously covered by physical scans **10–299**, which is **290 physical scans**. The 58 certified item ranges are contiguous and non-overlapping. Scans 1–9 are preliminaries/contents/display matter before item 1; scans 300–306 are end matter after the numbered first-part sequence and are not silently folded into a canonical numbered item.

## 2. Metadata reconciliation

**PASS — 58/58 canonical front-matter records checked against `indexes/page-map.md`.**

For every canonical file `sections/01.md` through `sections/58.md`, the following agree with the certified page map:

- `item` sequence identity;
- `title_scan`;
- `physical_scans`;
- `printed_pages`;
- controlling `source_filename`;
- `assembly_status: "assembled-from-verified-pages"`.

The first item correctly records scan range **10–11 / printed pages 9–10**. The final item correctly records scan range **296–299 / printed pages 295–298**. No metadata range gap, overlap, shift, or off-by-one error was found.

## 3. Canonical source provenance and page-order completeness

**PASS.**

Canonical files retain the repository's provenance convention `<!-- scan_page: N -->`, beginning with the certified title scan for each item. The reviewed assembly follows the certified physical ranges and source order established by the completed 58-item boundary/page-join audit.

The review specifically re-opened canonical assemblies across the beginning, middle, discrepancy-heavy and final portions of the source, including items 1, 2, 14, 32, 37, 47, 53, 54, 55 and 58. Their source-page blocks remain in certified order, including long multi-scan items and page-boundary continuations. No evidence of a dropped, duplicated, reordered or cross-item page block was found.

The earlier Phase-3 boundary/join audit remains the controlling structural evidence for all 58 item boundaries and every within-item physical-page join; it records **58/58 PASS**, closing boundary **299→300 PASS**, and no unresolved structural join.

## 4. Title-witness preservation

**PASS — 14/14 documented discrepancy cases remain durably preserved as separate witnesses.**

The canonical front matter was checked for all discrepancy items:

- 18 — `தேய்ந்தது போக...` title-page form versus contents `தேய்ந்ததுபோக...`;
- 22 — title-page enclosing quotation marks preserved;
- 25 — title page omits final `!`;
- 26 — title page omits the contents comma after `இதோ`;
- 29 — title page omits the contents comma after `தாயே`;
- 31 — title page omits the contents comma after `தாயும்`;
- 32 — substantive title-page wording `கோவூரார் கேள்வியுறும் - குனிந்திடும் தலையுறும்` preserved separately from the contents witness;
- 37 — title-page `அன்பால் அவனை விலைகொள்ள முடியுமோ?` preserved separately from the contents witness, with `printed_item_number: 36` retained while canonical identity remains item 37;
- 40 — title page omits final `!`;
- 44 — title page omits the contents comma;
- 46 — title page adds final `!`;
- 50 — title-page `குருதிக்களமே;` preserved separately from contents `குருதிக் களமே!`;
- 54 — joined title-page form `செருவென்றான்!` preserved separately from contents `செரு வென்றான்!`;
- 58 — title-page `பகைவாள்` plus final `!` preserved separately from contents `பகை வாள்` without final `!`.

No hybrid title was found. Title-page authority is used for canonical displayed titles, while `contents_title` retains the contents witness.

## 5. Source-sensitive structure and closing matter

**PASS.**

Source-sensitive material required by earlier audits remains represented in the canonical layer. Checks included:

- internal `★` separators remain edition text where certified inside an item;
- quoted passages and dialogue remain within their certified item/page sequence;
- item 53 retains the scan-270 `குறிப்பு:` block after the internal separator;
- item 54 retains the concluding source-reference `குறிப்பு:` and its poem-number references;
- item 55 retains its concluding parenthetical source note based on `நெடுநல்வாடை`;
- item 37 retains its explicit printed-number source-anomaly note;
- item 58 retains the final source closing `(முதல் பாகம் முற்றிற்று)` on scan 299;
- scan 300 remains outside item 58 as the beginning of separate `குறிப்புகள்` end matter.

No silent modernization, title hybridization, inferred missing passage, or source-level structural smoothing was introduced by this review.

## Review accounting

- canonical item files: **58/58 — PASS**;
- certified canonical source scans: **290/290 represented by item ranges — PASS**;
- metadata records checked: **58/58 — PASS**;
- title-witness discrepancy cases checked: **14/14 — PASS**;
- item-37 printed-number anomaly: **PRESERVED**;
- unresolved source-completeness defects: **0**;
- verified `pages/NNNN.md` records modified during review: **0**;
- canonical files modified during review: **0**;
- Phase-4 translation started: **NO**.

## Gate result

**PASS — Phase-3 activity 5, canonical assembly/source-completeness review, is complete.**

The canonical Tamil assembly is structurally complete and consistent with the verified source/page-map/title-witness records. No source-completeness defect was found that requires reopening Phase 2 or the canonical item files.

## Exact next activity

Perform **Phase-3 activity 6 — Tamil final clearance**.

Tamil final clearance must formally confirm that all preceding Phase-3 gates are PASS and then mark the Tamil source/canonical layer as cleared for Phase 4. Do **not** begin English translation until that final-clearance record has been completed.