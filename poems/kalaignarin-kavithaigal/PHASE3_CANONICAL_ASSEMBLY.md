# Phase 3 Canonical Tamil Assembly — Gate 4

Work: **கலைஞரின் கவிதைகள்**
Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

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
- marker-only/non-edition-text scans retained inside item files: **2**;
- physical source section runs retained in provenance: **83**;
- Gate-3 title variants retained separately: **30/30** (**29 item variants + 1 pure-group variant**);
- stable filenames: `01.md` … `77.md`;
- canonical `printed_pages` metadata follows the Gate-1 reconciled logical Arabic pagination; source-visible `printed_page` values in page records remain unchanged;
- canonical item-manifest SHA-256: `74f7bbd84edb1d13dec6d775f854a793929ef530b0c78897cc205004ba78972f`;
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

## Subsequent Gate 5 outcome

Phase 3 Gate 5 subsequently completed **PASS**. Durable evidence: `PHASE3_CANONICAL_SOURCE_REVIEW.md`.

- canonical item inventory: **77/77 PASS**;
- verified body scan accounting: **447/447 PASS**;
- item scans: **439/439 PASS**;
- structural group scans: **8/8 PASS**;
- canonical payload equality against the verified page layer: **77/77 PASS**;
- unresolved source-completeness defects: **0**;
- verified page-record changes during Gate 5: **0**;
- canonical item changes during Gate 5: **0**.

## Exact next gate

Proceed to **Phase 3 Gate 6 — Tamil final clearance only**. Confirm Gates 1–5 are all PASS and decide whether the Tamil source/canonical layer can be final-cleared for Phase 4. Do not begin English translation in the same activity.
