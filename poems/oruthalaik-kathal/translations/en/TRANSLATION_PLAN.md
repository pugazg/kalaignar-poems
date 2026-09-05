# English Translation Plan — ஒருதலைக் காதல்

## Status

**PHASE 4 IN PROGRESS. Translation batches 01–06 COMPLETE / REVIEWED PASS. Full-English assembly/editorial-consistency review COMPLETE / PASS. Final source-coverage/release gate is NEXT.**

Tamil source/canonical layer: **FINAL-CLEARED**. Translation batches: **6/6**. Reviewed standalone English sections: **11/11**. Reviewed source coverage: **95/95 scans**.

## Objective

Produce readable English that retains Kalaignar's poetic voice, dramatic dialogue, repetition, political/historical specificity, Sangam intertext, humour, irony, emotional escalation and recurring verbal motifs without replacing the source with explanatory paraphrase.

## Source hierarchy

Normal working source: Tamil final-cleared canonical `../../sections/01.md` … `../../sections/11.md`.

If a reading is questioned: controlling PDF scan → verified page record → final-cleared canonical section → Phase-3 records. English difficulty does not authorize a Tamil edit.

## Fidelity rules

1. Preserve direct address and speaker changes.
2. Preserve repeated formulations, refrains and rhetorical questions.
3. Preserve source irony, satire, emotional intensity and polemical language.
4. Preserve proper names and literary/historical references traceably.
5. Sangam quotations remain visibly quotations with their source attributions.
6. `பொருள் விளக்கம்` blocks remain separate **Source explanation** material.
7. Source claims are translated as source claims; Phase 4 is not a fact-check layer.
8. Culturally active Tamil terms may be transliterated where a flat substitute would erase meaning; document material choices.
9. English lineation may adjust for grammar but must not proseify the poetic/rhetorical architecture.
10. Full-page illustration scans receive only neutral structural markers.
11. Diamond ornaments and `(முற்றும்)` remain structurally represented.
12. English title remains **One-Sided Love**.
13. Recurring `போர்வாள் ... பூவிதழ்` remains **war-sword / flower-petal** unless a documented source-driven reason requires variation.

## Recurring locks

- `ஒருதலைக் காதல்` → **One-Sided Love**;
- `பொருள் விளக்கம்` → **Source explanation**;
- `காவற்பெண்டு` → **Kavarpentu**;
- `புறப்பாட்டு` → **puram poem/song** where relevant;
- `போர்வாள்` → **war-sword / sword of war**;
- `பூவிதழ்` → **flower-petal**;
- `கரந்தை` → **Karantai battle**;
- `நற்றிணை` → ***Natrinai***;
- `அகநானூறு` → ***Akananuru***;
- `குறுந்தொகை` → ***Kuruntokai***;
- source `ஆளி` in quoted/glossed context → **yali**;
- source-distinct `பாணி` remains unnormalized;
- `பல்வேற்கட்டி` → **Palver Katti**;
- narrative `உறையூர்` → **Uraiyur**;
- quotation-form `உறந்தை` → **Uranthai**;
- `அத்தாணி மண்டபம்` → **Attani council hall / Attani hall**;
- source `நாளவை` context → **day-court**;
- scan-92 `ஊழித்தீ` → **fire of cosmic destruction** in context;
- named `அனிச்சமலர்` → **anicham flower**;
- source `(முற்றும்)` → **(The End)** structurally, retaining final diamonds.

Proper-name continuity includes **Nakkannai, Perunarkilli / Narkilli, Sattanthaiyar / Sattanthai, Tittan, Porkodi, Perungozhinaykan, Kavarpentu, Aiyai, Panan, Palver Katti**. Source-driven form variation is not silently normalized.

## Output model

- reviewed English sections `sections/01.md` … `11.md`: **11/11 complete**;
- batch records `batches/BATCH_01.md` … `BATCH_06.md`: **6/6 PASS**;
- reader-facing full English `oruthalaik-kathal-en.md`: **complete**, **89,457 bytes**, **3,004 lines**, blob `012a3bdaf330bb9b2db66d229c0be2a87d3f46f6`;
- `EDITORIAL_CONSISTENCY_REVIEW.md`: **COMPLETE / PASS**;
- `RELEASE_REPORT.md`: **not yet created — final release gate NEXT**.

## Batch boundaries

| Batch | Sections | Physical scans | Logical pages | Text scans | Illustration scans | Status |
|---:|---:|---:|---:|---:|---|---|
| 01 | 01–02 | 6–20 | 1–15 | 13 | 8, 16 | **PASS** |
| 02 | 03–04 | 21–38 | 16–33 | 16 | 22, 32 | **PASS** |
| 03 | 05–06 | 39–55 | 34–50 | 15 | 40, 48 | **PASS** |
| 04 | 07–08 | 56–73 | 51–68 | 16 | 58, 66 | **PASS** |
| 05 | 09 | 74–82 | 69–77 | 8 | 76 | **PASS** |
| 06 | 10–11 | 83–100 | 78–95 | 16 | 84, 94 | **PASS** |

Total: **95/95 = 84 text-bearing + 11 illustration-only**.

## Post-batch gate

**FULL-WORK ENGLISH ASSEMBLY / EDITORIAL / TERMINOLOGY / VOICE CONSISTENCY REVIEW: PASS.**

The assembled file represents all 11 source sections and all 95 main-work scans exactly once. All illustration markers, section closes, internal separators, quotations/attributions, Source explanations and final work closure are preserved. Unresolved English assembly/editorial issues: **0**.

One English-only correction was made during the post-batch gate: section 3 `karantai battle` → **Karantai battle**. Tamil remained frozen.

## Final-release workflow

1. Verify all **6/6** batch records and **11/11** standalone English sections remain synchronized with the assembly.
2. Certify assembly scan markers **6–100 = 95/95 exactly once** and exclusions **1–5, 101**.
3. Certify illustration markers, numbered-section closes, internal separators, quotation/Source-explanation layers and final **(The End)** structure.
4. Check title/name/term/refrain consistency and section-3 **Karantai battle** synchronization.
5. Check reader-facing cleanliness: no standalone YAML or batch-control prose.
6. Compare from Tamil final-clearance checkpoint `0c6b3d19625a9478441f0f654584d8343163ba37`; require **0 changed active Tamil page/canonical files**.
7. Create `RELEASE_REPORT.md` and grant release clearance only if every check passes with unresolved release issues **0**.

## Exact next activity

**Phase 4 final source-coverage / release-integrity gate.** The work is not RELEASE-CLEARED until that gate passes.
