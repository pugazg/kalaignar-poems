# English Translation Plan — இதயத்தைத் தந்திடு அண்ணா

## Status

**Planning complete. Batches 01–02 reviewed PASS; Batches 03–05 not started.**

Tamil source status before translation:

- physical source: **28/28 verified**;
- poem scans: **14/14 verified**;
- Tamil assembly: **PASS**;
- assembly discrepancies: **0**;
- unresolved poem readings: **0**.

## Translation objective

Produce an English version that is faithful not only to what Kalaignar says, but to **how Kalaignar speaks and writes**.

The governing instruction is:

> **Retain Kalaignar's language — his voice, cadence, rhetorical architecture, political memory, literary allusion, repetition and grief — while making the English genuinely readable.**

Readability is not permission to paraphrase away source texture.

## Voice-fidelity rules

### 1. Direct address stays direct

When Kalaignar addresses Anna as `அண்ணா`, `எம் அண்ணா`, `இதயமன்னா`, or through other vocatives, the English must preserve the act of address rather than convert it into third-person narration.

### 2. Repetition is meaning

Repeated words, phrases, questions, exclamations and accumulative structures are rhetorical devices and must normally remain repeated.

### 3. Oratory must remain audible

Preserve calls to listeners, rising sequences, slogans, rhetorical questions, apostrophes, antithesis, parallel phrasing and catalogue/list structures. English lineation may adapt, but it must still feel speakable.

### 4. Political vocabulary is not background decoration

References to movements, parties, leaders, conferences, struggles, linguistic politics and public life must not be neutralized into vague abstractions.

### 5. Literary/classical echoes remain visible

Do not flatten specific Tamil literary traditions, figures, genres or works into generic “ancient literature” language.

### 6. Imagery should remain Kalaignar's imagery

Do not replace source metaphors with more familiar English poetic metaphors.

### 7. Elegiac intensity must not be softened

The closing movement uses repeated questions, direct appeals, physical imagery and grief. Preserve its pressure and immediacy.

### 8. Source oddities are not translator licence

The English translation should interpret from the verified source, not silently “correct” the Tamil in order to translate a more expected reading. If more than one English reading remains plausible, flag it in the batch note instead of guessing.

### 9. No fake archaism

Retaining Kalaignar's language does not mean forcing pseudo-Victorian diction into English. The target should be elevated where the Tamil is elevated, conversational where the Tamil is conversational, and politically direct where the Tamil is direct.

## Batch plan

| Batch | Source scans | Visible printed pages | Broad movement | Status |
|---|---:|---:|---|---|
| 01 | 13–15 | 11–13 | opening praise; martial/literary tribute; `அவலப் பரணி` turn | **reviewed — PASS** |
| 02 | 16–19 | 14–17 | three-letter motif; Anna's sayings; movement history; split and new movement | **reviewed — PASS** |
| 03 | 20–21 | 18–19 | governance/public praise; scholars; Tamil/social critique begins | not started |
| 04 | 22–23 | 20–21 | social decline; Valluvar dialogue; Anna figured as renewed Tamil leadership | not started |
| 05 | 24–26 | 22–23 + unnumbered final scan | Anna's roles; statues/cultural memory; final elegy and heart appeal | not started |

Batch boundaries follow verified physical page markers and rhetorical movement. They do not alter the Tamil assembly.

## Per-batch workflow

For each batch:

1. read the corresponding verified Tamil page files;
2. read the same range in the reviewed Tamil assembly for continuity;
3. check beginning/end continuation notes in `SOURCE_MAP.md`;
4. draft English line by line / rhetorical unit by rhetorical unit;
5. compare draft back to Tamil for omissions and additions;
6. perform a **Kalaignar voice pass** for cadence, repetition, direct address, slogans, rhetorical questions and emotional register;
7. record difficult translation decisions beneath the batch text, outside the poem body;
8. mark the batch `reviewed` only after source/voice checks pass.

Do not draft the next batch merely to keep momentum if the current batch has unresolved meaning or voice issues.

## Batch file format

Each `batches/batch-XX.md` contains YAML provenance, source range, English translation only, translator's notes outside the verse, review checklists and final batch status.

Do not interleave Tamil and English line-by-line in release text. Tamil may be quoted sparingly in review notes when needed to explain a translation decision.

## Proper names and titles

- retain familiar established names in readable Roman form;
- do not silently substitute modern institutional names for historical/source wording;
- retain `Anna` as a meaningful form of address/title;
- preserve relationship/title distinctions when rhetorically active;
- use translator notes instead of explanatory expansion inside the poem.

## Quotations and slogans

Quoted sayings should remain recognisably quotational and memorable. Where a Tamil slogan depends on compact parallelism, the English should first seek a similarly compact form.

## Lineation policy for English

- do not mechanically mirror every Tamil physical line;
- preserve stanza boundaries and major rhetorical units;
- preserve short emphatic lines when their force depends on isolation;
- preserve stepped/list movement where it contributes to crescendo or contrast;
- do not collapse verse into prose paragraphs.

## Notes policy

Translator's notes are permitted for historically specific political references, classical/literary allusions, wordplay that cannot survive fully in English, puzzling source-supported images, and material translation choices. Notes must remain concise.

## Batch 01 closure

Created: [`batches/batch-01.md`](batches/batch-01.md)

Review result:

- scans covered: **13–15 / 3 of 3**;
- omitted / duplicated source units: **0 / 0**;
- continuation checks: **PASS**;
- `வெள்ளம்! / வெள்ளம்! / மாபெரும் வெள்ளம்!` preserved;
- source oddities handled without silent normalization: **PASS**;
- Kalaignar voice review: **PASS**.

## Batch 02 closure

Created: [`batches/batch-02.md`](batches/batch-02.md)

Review result:

- scans covered: **16–19 / 4 of 4**;
- omitted / duplicated source units: **0 / 0**;
- scan 17 → 18 and scan 18 → 19 continuation checks: **PASS**;
- repeated `முன்றெழுத்து` wordplay preserved through Tamil lexical forms + English glosses + repeated `three letters`: **PASS**;
- compact slogans and quotations preserved as speech: **PASS**;
- `Dravidar Kazhagam`, `Munnetra Kazhagam`, `Ayya` and relationship-language retained: **PASS**;
- difficult source forms handled with notes/transliteration rather than guessed normalization: **PASS**;
- Kalaignar voice review: **PASS**.

Batch 02 deliberately ends with `Has anyone ever heard of such a thing?`; Batch 03 must pick up scan 20's paired `யாரேனும் புகன்றதுண்டா?` without losing the call-and-response cadence across the batch boundary.

## Assembly and release stages

After all five batches are reviewed:

1. create `idhayathai-thanthidu-anna-en.md` from reviewed batches only;
2. compare assembled English against every batch and the Tamil source map;
3. create `EDITORIAL_CONSISTENCY_REVIEW.md` covering names, titles, recurring terms, quotation style, punctuation philosophy and voice consistency;
4. perform a full Kalaignar voice review across the poem;
5. create `RELEASE_REPORT.md` only after all checks pass.

## Release criteria

English may be called release-ready only when all five batches are reviewed, no Tamil source unit is omitted/duplicated, no explanatory invention enters the verse, recurring terms are consistent, rhetorical repetitions remain intact unless documented otherwise, and the final editorial/voice review passes.

## Exact next activity

Begin **Batch 03 — scans 20–21 / printed pages 18–19**.

Before drafting, reread Batch 02's closing `Has anyone ever heard of such a thing?`, then `pages/0020.md`–`pages/0021.md` and the corresponding Tamil assembly blocks. Preserve scan 20's answering/paired question `யாரேனும் புகன்றதுண்டா?`, keep governance/public praise as Kalaignar's rhetoric rather than neutral prose, and preserve scan 21's compact literary parallelism and turn toward social critique.
