# Next Chat Prompt — Kalaignar Poems Archival Project

Use this prompt when continuing **any poem/PDF** in `pugazg/kalaignar-poems` in a fresh chat. Replace the `<...>` placeholders only where needed. Live GitHub state and the attached controlling source always take precedence over stale status text in the prompt.

---

Continue the **Kalaignar Poems archival project** directly in:

`https://github.com/pugazg/kalaignar-poems`

Branch: `main`

Active work:

`poems/<WORK-ID>/`

Attached controlling source:

`<ATTACHED-PDF-FILENAME>`

Expected title/work identity, if known:

`<TITLE OR UNKNOWN — VERIFY FROM SOURCE>`

Use the GitHub connector and work directly in the existing repository on `main`.

## MANDATORY STARTUP

Before making any repository change:

1. Read `HANDOVER.md` **completely**.
2. Read `POEM_PROCESSING_GUIDE.md` **completely**.
3. Read `TRANSCRIPTION_PHASE_PLAN.md` **completely**.
4. Read root `README.md`.
5. Read this file, `NEXT_CHAT_PROMPT.md`.
6. Inspect the current repository and confirm whether this work already exists under the same title, an alternate title, another filename, or an existing `poems/<WORK-ID>/` directory.
7. If the work already exists, **continue it; do not create a duplicate**.
8. For an existing work, read its available control/state files completely, especially:
   - `poems/<WORK-ID>/README.md`
   - `poems/<WORK-ID>/metadata/source.md`
   - `poems/<WORK-ID>/indexes/page-map.md`
   - `poems/<WORK-ID>/audit.md`
   - relevant files under `poems/<WORK-ID>/notes/`
   - all existing page records needed to understand the current activity.
9. Inspect current GitHub `main` and treat it as authoritative over old SHAs, counts, summaries, or previous-chat claims.
10. Inspect the attached controlling PDF/source before resuming work.
11. Determine the **declared current phase** from live repository documents before acting. Do not perform work assigned to a later phase.
12. Do not restart completed work merely because this is a new chat.

## TEXTUAL AUTHORITY

The archival goal is fidelity to the controlling source unless a documented user instruction explicitly establishes a different editorial treatment.

- Source scan pixels are the normal highest textual authority.
- OCR, extracted text, catalogue text, outside editions, previous transcriptions, semantic expectation, and earlier chat answers are aids only unless the user explicitly designates supplied text as the lexical control.
- Never silently normalize spelling, grammar, punctuation, spacing, repetitions, unusual forms, English/Latin material, page boundaries, or typographical anomalies.
- Never substitute a plausible Tamil word merely because it makes better semantic or grammatical sense.
- Later library stamps, handwriting, bleed-through/show-through, and unrelated marks are not edition text.
- Never invent text from missing physical pages.

## PHASE GATING

When a work is in explicit phased mode, follow `TRANSCRIPTION_PHASE_PLAN.md`.

### Phase 1 — transcription only

- transcribe the controlling scan directly into page records;
- preserve source spelling, punctuation, lineation, headings, quotation marks and unusual forms;
- record physical scan number and only visibly printed page numbers;
- mark genuine uncertainty instead of guessing;
- newly transcribed pages normally remain `partial`, or `needs-review` for a specific unresolved reading;
- do **not** mark a page `verified` merely because it has been transcribed once;
- existing pages genuinely verified before the phase switch remain verified;
- do not conduct a separate glyph-by-glyph verification pass;
- do not conduct systematic continuity/page-join or work-wide structural audits;
- do not assemble canonical Tamil;
- do not begin translation;
- do not churn `README.md`, `audit.md`, or `page-map.md` after every small batch unless a milestone, anomaly, or phase change needs documentation.

### Phase 2 — source-critical visual verification

Independently reread and verify every transcribed page against the scan, including old-typeface/glyph endings, punctuation, lineation and documented lexical controls. Only then may pages be promoted to `verified`.

### Phase 3 — structure / completeness / assembly / Tamil final clearance

Complete page mapping, item/work boundaries, joins, completeness review, canonical Tamil assembly and final clearance.

### Phase 4 — translation / release

Begin translation or other derivative/release work only after Tamil final clearance.

Do not advance phases without explicit user authorization or a live repository instruction that clearly records the user's authorization.

## OLD TAMIL TYPEFACE WARNING

This repository has demonstrated that older Tamil print can be misread even after multiple visual verification passes. High-resolution enlargement alone does not guarantee correctness.

Known failure classes include:

1. suffix and grammatical-ending loss/substitution, especially forms involving `-ளை`, `-ை`, `-ஆம்`, `-னால்`, `-ஆள்`, and `-னான்`;
2. older vowel-sign/glyph confusion, including repeated `-ஆன்` versus `-உன்` misclassification;
3. whole-word substitution caused by recognizing a plausible word silhouette instead of accounting for every printed glyph;
4. loss or invention of punctuation, dots, hyphens/dashes, quotation marks, separators, and physical line breaks.

During Phase 1, produce the best source-faithful transcription possible and explicitly mark genuine uncertainty; the independent systematic old-typeface re-audit belongs to Phase 2.

During Phase 2 and later verification work:

- compare **complete lines**, not isolated guessed words;
- account for every glyph and word ending;
- use enlarged crops when necessary, but do not treat interpolation as new source detail;
- if a glyph remains genuinely unresolved, record it as unresolved rather than guessing;
- a previous `verified` or `PASS` label is not proof when later evidence contradicts it.

## USER-SUPPLIED LEXICAL CONTROL

If the user supplies an exact transcription/extraction for a page and explicitly says it is correct, use that supplied text as the **lexical control** for reconciliation.

In that situation:

- do not override the user's confirmed lexical reading with another visual guess;
- use the physical scan for page identity, page/column order, illustrations, page joins, and clearly visible structural/typographic evidence where applicable;
- document the reconciliation and supersede earlier incorrect PASS/verification claims;
- preserve any explicit user-directed editorial omission or treatment and document it without silently restoring the excluded material later.

## REPOSITORY DISCIPLINE

- Work on `main` unless the user explicitly instructs otherwise.
- Do not create duplicate work directories or duplicate page records.
- Keep correction/failure history when archivally useful.
- Make focused commits with meaningful messages.
- Respect the current phase instead of trying to complete later-phase checks early.
- After each requested activity, report what was transcribed/changed, files changed, current phase/status, commit SHA, and exact next activity.

## CURRENT WORK-SPECIFIC CONTINUATION

After startup, derive the exact next activity from live GitHub state.

### காலப் பேழையும் கவிதைச் சாவியும்

For `poems/kaalap-pezhaiyum-kavithai-saaviyum/`, the current declared phase is **Phase 1 — transcription only**.

- scans 1–9 were genuinely verified before the phase switch and remain verified;
- scan 10 is the next page to transcribe;
- from scan 10 onward, create source-faithful page records sequentially and normally keep them `partial` until Phase 2;
- do not interrupt Phase 1 to perform item-wide verification, page-join audits, assembly, completeness review or translation;
- continue transcription through the source until Phase 1 is complete or the user changes direction.

### தென்னவன் காதை

For `தென்னவன் காதை`, preserve the existing documented user-directed editorial omission on page 151. Do not restore the excluded caste-based term during audit, assembly, translation, or later cleanup.
