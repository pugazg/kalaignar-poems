# English Release Report — காலப் பேழையும் கவிதைச் சாவியும்

Status: **FINAL SOURCE-COVERAGE / RELEASE REVIEW COMPLETE — PASS**

Release gate date: **2026-08-30**

## Scope

This is the final Phase-4 release gate for the English translation of the 58-item numbered collection **காலப் பேழையும் கவிதைச் சாவியும்**.

Reader-facing collection: `kaalap-pezhaiyum-kavithai-saaviyum-en.md`.

Standalone distribution: `items/` — **58/58** separate English item files plus `items/README.md`.

This is a source-coverage, synchronization, provenance and release-integrity review; it is **not** a fresh pixel-level rereading of all 290 numbered-item scans. Tamil textual authority remains the final-cleared canonical/page layer and, if reopened, the controlling scan.

## Release checkpoints

- Tamil final-clearance durable checkpoint: `09551dbe9bf6615d4b3c26f21792151ba64089e4`;
- release-review input commit: `7e3d83092c1ed96f3d6ffd14def928291433ec37`;
- editorial-reviewed assembled SHA-256: `902cbb83d3746e42947ed0639652623907a544b40fdabee748878e432f5ec87e`;
- reader-facing size: **321,102 bytes**;
- reader-facing line count: **16,308**.

## 1. Item and scan source coverage

Result: **PASS**

- stable numbered items: **58/58**, exactly once and in order;
- numbered-item scans: **290/290**, exactly scans **10–299**, once each and in order;
- every item scan-marker sequence matches its canonical `physical_scans` range;
- scan-300 end matter is excluded.

## 2. Reviewed-batch synchronization

Result: **PASS**

- reviewed batches: **21/21**;
- batch item inventory: **1–58 exactly once**;
- each assembled item heading plus English translation body is byte-for-byte aligned with the corresponding reviewed batch translation body.

## 3. Standalone per-poem synchronization

Result: **PASS**

- standalone files: **58/58**;
- stable standalone identities: **1–58 exactly once**;
- each standalone translated body is byte-for-byte aligned with the corresponding assembled item body;
- canonical Tamil title, contents-title witness, English title, witness status and scan range are synchronized;
- `items/README.md` indexes items **1–58** exactly once and in order.

## 4. Title-witness integrity

Result: **PASS**

The discrepancy register remains exactly **18, 22, 25, 26, 29, 31, 32, 37, 40, 44, 46, 50, 54 and 58**. Canonical/title-page and contents witnesses remain separate. Item 37 remains stable item 37 while printed item number 36 is preserved only as a source anomaly.

## 5. Source-visible structure

Result: **PASS**

The reader-facing collection is byte-identical to the full-work editorial-PASS checkpoint. Its structural inventory remains **53** compact `★ ★ ★` separators, **6** wide `★     ★     ★` separators, **2** single `★` separators, **4** `**Note:**` blocks and **290** scan-provenance comments.

Because every item is also byte-aligned with its reviewed batch translation body, previously cleared quotations, dialogue, glossary material, parenthetical source material and high-risk item structures remain intact.

## 6. Reader-facing cleanliness

Result: **PASS**

No batch/editorial apparatus is present in the reader-facing collection.

## 7. Tamil-source protection

Result: **PASS**

A Git comparison from the durable Tamil final-clearance checkpoint through the release-review input commit found **0 changed files** under the canonical `sections/` and verified `pages/` directories.

## 8. Final boundary

Result: **PASS**

Item 58 contains scans **296–299** and the collection ends exactly with `(First Part Complete)`, occurring once. Scan-300 end matter remains excluded.

## Final decision

**ENGLISH PHASE 4 RELEASE: PASS — RELEASE-CLEARED**

- translation batches: **21/21 reviewed PASS**;
- stable items: **58/58**;
- numbered-item scans: **290/290**;
- complete English collection: **release-cleared**;
- standalone English item files: **58/58 release-cleared synchronized copies**;
- unresolved release issues: **0**;
- Tamil canonical/page files changed during Phase 4: **0**.

The English translation phase for this numbered first-part collection is complete. No further Phase-4 release gate remains.
