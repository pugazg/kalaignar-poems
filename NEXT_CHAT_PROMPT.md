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
3. Read root `README.md`.
4. Read this file, `NEXT_CHAT_PROMPT.md`.
5. Inspect the current repository and confirm whether this work already exists under the same title, an alternate title, another filename, or an existing `poems/<WORK-ID>/` directory.
6. If the work already exists, **continue it; do not create a duplicate**.
7. For an existing work, read its available control/state files completely, especially:
   - `poems/<WORK-ID>/README.md`
   - `poems/<WORK-ID>/metadata/source.md`
   - `poems/<WORK-ID>/indexes/page-map.md`
   - `poems/<WORK-ID>/audit.md`
   - relevant files under `poems/<WORK-ID>/notes/`
   - all existing page records needed to understand the current activity.
8. Inspect current GitHub `main` and treat it as authoritative over old SHAs, counts, summaries, or previous-chat claims.
9. Inspect the attached controlling PDF/source before resuming transcription or verification.
10. Do not restart completed work merely because this is a new chat.

## TEXTUAL AUTHORITY

The archival goal is fidelity to the controlling source unless a documented user instruction explicitly establishes a different editorial treatment.

- Source scan pixels are the normal highest textual authority.
- OCR, extracted text, catalogue text, outside editions, previous transcriptions, semantic expectation, and earlier chat answers are aids only unless the user explicitly designates supplied text as the lexical control.
- Never silently normalize spelling, grammar, punctuation, spacing, repetitions, unusual forms, English/Latin material, page boundaries, or typographical anomalies.
- Never substitute a plausible Tamil word merely because it makes better semantic or grammatical sense.
- Later library stamps, handwriting, bleed-through/show-through, and unrelated marks are not edition text.
- Never invent text from missing physical pages.

## OLD TAMIL TYPEFACE WARNING

This repository has demonstrated that older Tamil print can be misread even after multiple visual verification passes. High-resolution enlargement alone does not guarantee correctness.

Known failure classes include:

1. suffix and grammatical-ending loss/substitution, especially forms involving `-ளை`, `-ை`, `-ஆம்`, `-னால்`, `-ஆள்`, and `-னான்`;
2. older vowel-sign/glyph confusion, including repeated `-ஆன்` versus `-உன்` misclassification;
3. whole-word substitution caused by recognizing a plausible word silhouette instead of accounting for every printed glyph;
4. loss or invention of punctuation, dots, hyphens/dashes, quotation marks, separators, and physical line breaks.

Therefore:

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

## PAGE WORKFLOW

For each page being processed or reopened:

1. Establish the correct physical scan page and its role in the work.
2. Check continuity from the preceding page and into the following page when available.
3. Transcribe/reconcile the full visible text line by line.
4. Check every word ending and compact old-type glyph explicitly.
5. Check punctuation, quotation carry-over, separators such as `★`, lineation, column order, and page boundaries.
6. Use crops/enlargements for ambiguous regions.
7. Compare against the existing repository record only after establishing an independent reading/control witness; do not let the existing text anchor the reading.
8. Correct only source-backed or user-control-backed differences.
9. Update the page record plus all relevant tracking documents (`page-map.md`, `audit.md`, work `README.md`, and a note when the correction history warrants one).
10. Do not mark a page/work final-cleared until the required review actually passes.

## WORK-WIDE COMPLETION

Before assembling a Tamil poem from page records:

- every physical page in the confirmed work range must be accounted for or explicitly documented as unavailable;
- all page records must have completed the required verification/reconciliation;
- all page joins must be checked;
- quotation carry-over, separators, punctuation and continuation lines must be reconciled;
- known user corrections and lexical-control pages must be preserved;
- any documented editorial omission must remain omitted exactly as directed;
- `audit.md`, `indexes/page-map.md`, and the work `README.md` must agree on status.

Only after this work-wide audit passes may Tamil assembly be marked ready.

Do **not** begin English translation until the Tamil source text has reached the repository's required final-clearance state.

## REPOSITORY DISCIPLINE

- Work on `main` unless the user explicitly instructs otherwise.
- Do not create duplicate work directories or duplicate page records.
- Keep correction/failure history when it is archivally useful; supersede misleading PASS claims rather than erasing the evidence of why they failed.
- Make focused commits with meaningful messages.
- After each requested activity, report:
  - exactly what was checked;
  - exact corrections made;
  - files changed;
  - current work status;
  - commit SHA;
  - exact next activity.

## CURRENT WORK-SPECIFIC CONTINUATION

After completing the mandatory startup, derive the **current exact next activity from live GitHub state** for `poems/<WORK-ID>/` and continue from there. Do not trust a copied previous-chat status if GitHub shows a newer state.

---

For `தென்னவன் காதை` specifically, also preserve the existing documented user-directed editorial omission on page 151. Do not restore the excluded caste-based term during audit, assembly, translation, or later cleanup.