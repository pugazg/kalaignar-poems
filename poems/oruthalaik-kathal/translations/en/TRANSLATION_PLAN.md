# English Translation Plan — ஒருதலைக் காதல்

## Status

**PHASE 4 T0 COMPLETE / PASS. Batch 01 is NEXT.**

Tamil source/canonical layer: **FINAL-CLEARED**. Translation batches completed: **0/6**.

## Objective

Produce readable English that retains Kalaignar's poetic voice, dramatic dialogue, repetition, political/historical specificity, Sangam intertext, humour, irony, emotional escalation and recurring verbal motifs without replacing the source with explanatory paraphrase.

## Source hierarchy

### Normal working source

Use only the Tamil final-cleared canonical files `../../sections/01.md` … `../../sections/11.md` for ordinary translation.

### Textual authority if a reading is questioned

1. **controlling PDF scan** — ultimate textual authority;
2. **verified page record** under `../../pages/`;
3. **final-cleared canonical section** under `../../sections/`;
4. Phase-3 structural/title/assembly/completeness/final-clearance records.

An English translation problem does not authorize a Tamil edit. If translation exposes a genuine Tamil discrepancy, reopen the affected Tamil source workflow, correct source/page/canonical layers together, revalidate as required, and only then resume English.

## Fidelity rules

1. Preserve direct address and speaker changes.
2. Preserve repeated formulations and refrains; do not compress them for elegance.
3. Preserve rhetorical questions as questions.
4. Preserve source irony, mockery, satire and emotional intensity.
5. Preserve proper names and literary/historical references traceably; do not replace a source name with a more familiar outside-edition equivalent without a documented translator note.
6. Sangam quotations remain visibly quotations and retain their source attributions.
7. `பொருள் விளக்கம்` blocks are translated as source explanatory material, not silently merged into the poem.
8. Source claims are translated as source claims; Phase 4 is not a fact-check layer.
9. Culturally active Tamil terms may be transliterated where a flat English substitute would erase meaning; document the choice when material.
10. Source punctuation and lineation guide English structure. English syntax may require different breaks, but the poem must not be turned into undifferentiated prose.
11. Full-page illustration scans have no lexical body text. English may record a neutral structural marker such as `<!-- full-page illustration; no source caption -->`; it must not invent caption or narrative content.
12. Diamond ornaments and `(முற்றும்)` are structural source witnesses and remain represented in the English layer.
13. The recurring `போர்வாளைத்தான் ... பூவிதழை அல்ல` motif must be translated consistently unless context gives a documented reason for variation.
14. The English work title will be fixed during Batch 01 review from canonical Tamil `ஒருதலைக் காதல்`; no title translation is silently locked during T0.

## Output model

- reviewed English section files: `sections/01.md` … `sections/11.md`;
- batch review records: `batches/BATCH_01.md` … `BATCH_06.md`;
- later, only after all six batches PASS: full English assembly, editorial-consistency review and release report.

Every English section must retain explicit Tamil-source mapping in front matter or header metadata, including the Tamil section number and physical scan range.

## Batch boundaries

Batch boundaries follow complete Tamil numbered sections and source order. No Tamil section is split across batches.

| Batch | Sections | Physical scans | Logical pages | Text scans | Illustration scans |
|---:|---:|---:|---:|---:|---|
| 01 | 01–02 | 6–20 | 1–15 | 13 | 8, 16 |
| 02 | 03–04 | 21–38 | 16–33 | 16 | 22, 32 |
| 03 | 05–06 | 39–55 | 34–50 | 15 | 40, 48 |
| 04 | 07–08 | 56–73 | 51–68 | 16 | 58, 66 |
| 05 | 09 | 74–82 | 69–77 | 8 | 76 |
| 06 | 10–11 | 83–100 | 78–95 | 16 | 84, 94 |

Total translation-source coverage: **95/95 main-work scans**, consisting of **84** text-bearing scans and **11** illustration-only scans.

## Per-batch workflow

For each batch:

1. fetch live `main` and preserve newer durable state;
2. read the assigned final-cleared Tamil section files completely;
3. consult `SOURCE_MAP.md` and Phase-3 records for source-sensitive joins/title/ornament decisions;
4. consult verified page records only when source-sensitive wording or provenance needs confirmation;
5. draft the English section files without changing Tamil;
6. review line-by-line for omissions, duplication, speaker integrity, quotations, glossaries and structural marks;
7. review voice/rhetorical fidelity and recurring-term consistency;
8. record material translator decisions in the batch review record;
9. mark the batch PASS only after all assigned sections pass.

## T0 source freeze

The Tamil canonical blob SHAs used to establish this plan are recorded in `SOURCE_MAP.md`. Any later Tamil canonical change must be source-backed and must trigger translation-source reconciliation before affected English work is treated as current.

## Exact next activity

**Batch 01 — sections 01–02, scans 6–20.** Translate and review both complete sections, create English `sections/01.md` and `sections/02.md`, and create `batches/BATCH_01.md`. Do not proceed to Batch 02 in the same activity unless explicitly requested.
