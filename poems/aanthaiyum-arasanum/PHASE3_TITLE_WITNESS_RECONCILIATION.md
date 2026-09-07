# Phase 3 Gate 3 — title-witness reconciliation — ஆந்தையும் அரசனும்

Date: **2026-09-07**.

Controlling source: `TVA_PRL_0001631_முரசொலி_ பொங்கல் மலர்_ 1965.pdf` — **102 physical pages / 381,558,891 bytes / SHA-256 `523a038dcd391f5cbe48f564d2ecac566fd0065066e05d29fc5b738aa4964819`**.

Active work range: physical scans **18–25**.

Prerequisites:

- Phase 1: **COMPLETE — 8/8 lexically complete**;
- Phase 2: **PASS — 8/8 verified / 0 unresolved**;
- Phase 3 Gate 1: **PASS — pagination reconciled**;
- Phase 3 Gate 2: **PASS — opening / joins / closing certified**.

## Repository rule

The repository processing guide requires differing title witnesses to be preserved exactly, with an explicit assembly-authority decision. Canonical assembly must not silently normalize punctuation or create a hybrid title.

## Witnesses

| Witness | Exact form | Provenance | Durable role |
|---|---|---|---|
| bibliographic / work metadata | `ஆந்தையும் அரசனும்` | user-supplied bibliographic record and repository work identity | retained as bibliographic/search/work metadata |
| direct edition title | `ஆந்தையும் அரசனும்!` | decorated title on controlling scan 18; verified in `pages/0018.md` | source-title witness and canonical heading authority |

The witnesses have the same lexical wording. Their difference is the **source-visible terminal exclamation mark** on the direct edition title. Because punctuation is part of the verified source layer, this difference must not be silently removed.

## Assembly-authority decision

**Canonical Tamil assembly title authority: direct scan-18 source witness `ஆந்தையும் அரசனும்!`.**

Reason:

1. the controlling 1965 scan is the repository's textual authority;
2. `pages/0018.md` independently verified the title exactly as `ஆந்தையும் அரசனும்!`;
3. canonical assembly is a provenance-preserving merge of verified page records, not a normalized bibliographic edition;
4. the bibliographic form remains useful metadata but does not override source punctuation.

Therefore canonical assembly must use exactly:

`# ஆந்தையும் அரசனும்!`

The bibliographic form `ஆந்தையும் அரசனும்` remains preserved in metadata and work-level identification. No hybrid such as `ஆந்தையும் அரசனும் !` and no punctuation-normalized title may be introduced.

## Page-layer effect

- page-text changes required by Gate 3: **0**;
- page-status changes: **0**;
- all page records remain **8/8 `verified`**;
- unresolved title holds: **0**.

## Gate result

**PHASE 3 GATE 3 PASS — BOTH TITLE WITNESSES PRESERVED / DIRECT SCAN-18 TITLE `ஆந்தையும் அரசனும்!` LOCKED AS CANONICAL ASSEMBLY AUTHORITY / 0 UNRESOLVED / 0 PAGE-TEXT CHANGES.**

Exact next activity: **Phase 3 Gate 4 — canonical Tamil assembly**. Assemble only from verified page records `pages/0018.md`–`0025.md`, preserve certified page joins/separators/quotation continuity and physical-page provenance, use `ஆந்தையும் அரசனும்!` as the canonical heading, and do not perform final clearance in the same gate.
