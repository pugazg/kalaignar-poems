# Phase 3 Structure Audit — Gate 1

Work: **பூமுடி**  
Workspace: `poems/poomudi/`  
Controlling source: `TVA_PRL_0001656_முரசொலி_அண்ணா மலர்_1965.pdf`

- physical PDF pages: **65**;
- file size: **247,645,717 bytes**;
- SHA-256: `7312d5f8686f7968d62bbac9318c2452ca32873a0ae889f10a7151e5de81ab5a`;
- scoped work range: physical scan **4 only**.

## Gate 1 scope

This record performs **Phase 3 Gate 1 only: physical scan ↔ printed-page reconciliation**. It does not reopen or modify the verified Tamil text, punctuation, lineation, title, signature, historical-glyph decisions, or the final user-controlled Phase-2 corrections. It does not perform Gate 2 boundary certification.

## Direct source review

The controlling source and neighbouring scans were re-opened visually for this gate.

Physical scan **4** is the sole active work scan. It contains the decorated title **பூமுடி**, the complete scoped poem, the stylized `மு.கருணாநிதி` attribution, and non-poem decorative/portrait material.

No source-printed page numeral is visible on scan 4. The small mark at the top margin is handwritten/library-style material, not printed pagination. Therefore the verified page-record value `printed_page: null` is source-supported and remains unchanged.

| Physical scan | Page role | Source-visible printed-page witness | Page-record value | Gate 1 result |
|---:|---|---|---|---|
| 4 | decorated title + complete poem + source signature | no printed page numeral visible | `null` | PASS |

The one physical scan is accounted for exactly once in the scoped page layer.

## Printed-page policy

`printed_page` records only a numeral visibly printed by the source. No sequence-derived or inferred page number is introduced for scan 4.

This gate does not reconstruct the pagination system of the full 65-page publication and does not treat handwritten/library marks as printed page witnesses.

## No-regression result

- physical scoped scans accounted: **1/1**;
- directly certified printed numerals: **0/1**;
- scans with no visible printed numeral and therefore `printed_page: null`: **1/1 — scan 4**;
- inferred printed numerals added: **0**;
- page-record text changes during Gate 1: **0**;
- page-record front-matter changes during Gate 1: **0**;
- Phase-2 verification state preserved: **1/1 VERIFIED / PASS**;
- final user-controlled source locks preserved: **`கமழுகின்ற`, `தலைமீது`, `பொன்வைத்தால்`, `உனைக்காக்க`**;
- unresolved pagination issues requiring a guessed value: **0**.

**PHASE 3 GATE 1 — COMPLETE / PASS.**

## Exact next gate

Proceed with **Phase 3 Gate 2 — boundary / page-join audit only**. Because this is a one-scan work, certify the opening and closing boundaries using scans 3 and 5 as neighbouring evidence and record that there are no internal physical page joins to reconcile. Do not begin Gate 3 title-witness reconciliation, canonical assembly, completeness review, Tamil final clearance, or translation in the same activity.