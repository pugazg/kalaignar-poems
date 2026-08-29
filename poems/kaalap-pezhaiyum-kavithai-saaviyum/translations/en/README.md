# English translation — காலப் பேழையும் கவிதைச் சாவியும்

Status: **PHASE 4 IN PROGRESS — Batch 01 reviewed PASS; 2/58 items translated and reviewed**

## Scope and source authority

This directory is the controlled English-translation workspace for the 58 final-cleared canonical Tamil items in **காலப் பேழையும் கவிதைச் சாவியும்**.

Tamil source status before Phase 4:

- physical source: **306/306 scans represented and verified**;
- canonical numbered items: **58/58**;
- canonical source range: scans **10–299**;
- title-witness discrepancies: **14/14 reconciled**;
- Phase-3 assembly/source-completeness review: **PASS**;
- Tamil final clearance: **PASS**.

Translation working source is the final-cleared canonical item `../../sections/NN.md`. If a Tamil reading is ever reopened, authority rises to the verified `../../pages/NNNN.md` record and ultimately to the controlling scan. English work must never silently rewrite the final-cleared Tamil layer.

## Governing principle

> **Retain Kalaignar's language.**

English should remain readable while protecting Kalaignar's voice, cadence, rhetorical architecture, direct address, repetition, political and historical specificity, literary references, imagery, satire, dialogue, questions, slogans and source-visible structural devices.

Voice fidelity takes priority over polishing the source into neutral modern prose.

## Planned translation structure

```text
translations/en/
  README.md
  TRANSLATION_PLAN.md
  SOURCE_MAP.md
  batches/
    batch-01.md  # reviewed PASS
    ...
    batch-29.md
  kaalap-pezhaiyum-kavithai-saaviyum-en.md
  EDITORIAL_CONSISTENCY_REVIEW.md
  RELEASE_REPORT.md
```

Each routine translation batch contains **two complete canonical items**. No item may be split merely to satisfy a batch boundary. The 58 items therefore map to **29 planned batches**.

## Translation progress

| Batch | Items | Physical scans | Status |
|---:|---:|---:|---|
| 01 | 1–2 | 10–15 | **reviewed — PASS** |
| 02–29 | 3–58 | 16–299 | planned |

Current totals:

- batches reviewed: **1/29**;
- items translated and reviewed: **2/58**;
- certified source scans represented in reviewed English batches: **6/290 numbered-item scans**;
- unresolved Batch-01 translation issues: **0**;
- Tamil canonical files modified during translation: **0**.

## Title handling

For every item, the Tamil `title` field in the canonical file is the authoritative title-page witness for English-facing title translation. The `contents_title` field remains a separate source witness.

For discrepant items **18, 22, 25, 26, 29, 31, 32, 37, 40, 44, 46, 50, 54 and 58**:

- translate the canonical title-page witness for the displayed English title;
- preserve the Tamil contents witness separately in metadata/source notes;
- do not invent a hybrid title;
- preserve item 37 as stable item **37**, while retaining printed item number **36** only as a source anomaly.

## Batch review rule

A batch is not complete merely because English text exists. Before a batch is marked reviewed, confirm:

1. both complete source items are represented once and in order;
2. no Tamil line, separator, note, quotation or dialogue unit is silently omitted or duplicated;
3. title metadata follows the source-witness rules;
4. direct address, repetition, rhetorical questions, slogans, satire and polemical force remain active in English;
5. names, dates, figures, literary works and political/historical terminology remain traceable to the source;
6. line/stanza architecture is not flattened into prose;
7. any deliberately non-literal English solution is recorded in the batch review notes rather than used to alter Tamil;
8. the batch passes a separate Kalaignar-language/voice read.

Only reviewed batches may enter the eventual complete English collection assembly.

## Batch 01 closure

Reviewed batch: [`batches/batch-01.md`](batches/batch-01.md)

Batch 01 covers:

- item 1 — `பொது உலகம்` — scans **10–11**;
- item 2 — `படிமுறை வளர்ச்சி` — scans **12–15**.

Review result:

- both canonical items represented once and in order: **PASS**;
- source scans represented: **6/6**;
- omissions / duplications: **0 / 0**;
- chronology, figures, names and source claims retained without fact-check substitution: **PASS**;
- rhetorical questions, wordplay, cosmic/evolutionary imagery and political closing retained: **PASS**;
- Kalaignar-language/voice review: **PASS**;
- Tamil source altered for English: **NO**.

## Release gates

Phase 4 proceeds in this order:

1. translation planning/source map — **COMPLETE**;
2. translate and review Batches **01–29** — **IN PROGRESS; 1/29 reviewed**;
3. assemble the complete English collection from reviewed batches only;
4. perform full-work editorial/terminology/voice consistency review;
5. perform source-coverage/release review;
6. mark English release complete only if all gates pass.

## Exact next activity

Translate and review **Batch 02 — items 3–4**:

- item 3 — `‘காந்தக்கல்’ கதையொன்று!` — scans **16–19** — `../../sections/03.md`;
- item 4 — `அன்றிருந்த கற்காலம் - இனி அமையாவிடின் நற்காலம்!` — scans **20–24** — `../../sections/04.md`.

Create `batches/batch-02.md`. Stop after item 4; do not begin item 5.