# English translation — காலப் பேழையும் கவிதைச் சாவியும்

Status: **PHASE 4 PLANNING COMPLETE — translation not yet started**

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
    batch-01.md
    ...
    batch-29.md
  kaalap-pezhaiyum-kavithai-saaviyum-en.md
  EDITORIAL_CONSISTENCY_REVIEW.md
  RELEASE_REPORT.md
```

Each routine translation batch contains **two complete canonical items**. No item may be split merely to satisfy a batch boundary. The 58 items therefore map to **29 planned batches**.

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

## Release gates

Phase 4 proceeds in this order:

1. translation planning/source map — **COMPLETE**;
2. translate and review Batches **01–29**;
3. assemble the complete English collection from reviewed batches only;
4. perform full-work editorial/terminology/voice consistency review;
5. perform source-coverage/release review;
6. mark English release complete only if all gates pass.

## Exact next activity

Translate and review **Batch 01 — items 1–2**, using canonical `../../sections/01.md` and `../../sections/02.md` as the working Tamil texts and scans **10–15** as their certified provenance range.

Do not begin item 3 during Batch 01.