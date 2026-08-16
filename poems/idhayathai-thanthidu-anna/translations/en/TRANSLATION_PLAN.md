# English Translation Plan — இதயத்தைத் தந்திடு அண்ணா

## Status

**Planning complete. Translation drafting has not started.**

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

Do not make an intimate/public lament sound like detached biography.

### 2. Repetition is meaning

Repeated words, phrases, questions, exclamations and accumulative structures are rhetorical devices and must normally remain repeated.

Do not reduce repetition simply because English editorial style might regard it as redundant.

### 3. Oratory must remain audible

This poem moves like spoken public verse. Preserve:

- calls to listeners;
- rising sequences;
- slogans and quotable formulations;
- rhetorical questions;
- sudden apostrophes;
- antithesis and parallel phrasing;
- catalogue/list structures.

English lineation may adapt, but it must still feel speakable.

### 4. Political vocabulary is not background decoration

References to movements, parties, leaders, conferences, struggles, linguistic politics and public life must not be neutralized into vague abstractions.

Where a Tamil political term/name has no clean English equivalent, retain the specific reference and clarify in a note if necessary.

### 5. Literary/classical echoes remain visible

Do not flatten references to Tamil literary traditions, figures, genres or works into generic phrases such as “ancient literature” when the source is specific.

Where the force depends on a culturally specific term, prefer transliteration or a precise English rendering plus a restrained note.

### 6. Imagery should remain Kalaignar's imagery

Do not replace source metaphors with more familiar English poetic metaphors.

If the Tamil image feels unusual in English, first attempt to preserve it. Explain only when necessary.

### 7. Elegiac intensity must not be softened

The closing movement uses repeated questions, direct appeals, physical imagery and grief. Preserve its pressure and immediacy.

Avoid turning it into polished commemorative prose.

### 8. Source oddities are not translator licence

The verified Tamil layer contains unusual forms and punctuation. The English translation should interpret from that verified source, not silently “correct” the Tamil in order to translate a more expected reading.

If an unusual form materially affects meaning and more than one English reading remains plausible, flag it in the batch note instead of guessing.

### 9. No fake archaism

Retaining Kalaignar's language does **not** mean forcing “thou/thee” or pseudo-Victorian diction into English unless a very specific local effect requires it.

The target should sound rhetorically elevated where the Tamil is elevated, conversational where the Tamil is conversational, and politically direct where the Tamil is direct.

## Batch plan

Translation will proceed in five reviewable batches.

| Batch | Source scans | Visible printed pages | Broad movement | Draft status |
|---|---:|---:|---|---|
| 01 | 13–15 | 11–13 | opening praise; martial/literary tribute; `அவலப் பரணி` turn | not started |
| 02 | 16–19 | 14–17 | three-letter motif; Anna's sayings; movement history; split and new movement | not started |
| 03 | 20–21 | 18–19 | governance/public praise; scholars; Tamil/social critique begins | not started |
| 04 | 22–23 | 20–21 | social decline; Valluvar dialogue; Anna figured as renewed Tamil leadership | not started |
| 05 | 24–26 | 22–23 + unnumbered final scan | Anna's roles; statues/cultural memory; final elegy and heart appeal | not started |

Batch boundaries deliberately follow verified physical page markers and rhetorical movement. They do not alter the Tamil assembly.

## Per-batch workflow

For each batch:

1. read the corresponding verified Tamil page files;
2. read the same range in the reviewed Tamil assembly for continuity;
3. check beginning/end continuation notes in `SOURCE_MAP.md`;
4. draft English line by line / rhetorical unit by rhetorical unit;
5. compare draft back to Tamil for omissions and additions;
6. perform a **Kalaignar voice pass** specifically for cadence, repetition, direct address, slogans, rhetorical questions and emotional register;
7. record difficult translation decisions beneath the batch text, outside the poem body;
8. mark the batch `draft`, then `reviewed` only after the source/voice checks pass.

Do not draft the next batch merely to keep momentum if the current batch has unresolved meaning or voice issues.

## Batch file format

Each `batches/batch-XX.md` should contain:

```yaml
---
work: "idhayathai-thanthidu-anna"
language: "en"
batch: 1
source_scans: "13-15"
status: "draft"
translation_basis: "verified Tamil page records + reviewed Tamil assembly"
---
```

Then:

- source range;
- English translation only;
- translator's notes / unresolved choices outside the verse;
- review checklist;
- status.

Do not interleave Tamil and English line-by-line in the release text. Tamil may be quoted sparingly in review notes where needed to explain a translation decision.

## Proper names and titles

Default policy:

- retain familiar established names in readable Roman form;
- do not silently substitute modern institutional names for historical/source wording;
- retain `Anna` as a meaningful form of address/title rather than reducing every occurrence to a personal name;
- preserve distinctions such as leader/title/relationship when rhetorically active in the Tamil;
- use translator notes for references that would otherwise become opaque, rather than expanding explanations inside the poem.

## Quotations and slogans

Quoted sayings should remain recognisably quotational and memorable.

Where a Tamil slogan depends on compact parallelism, the English should first seek a similarly compact form. A literal but lifeless explanatory sentence is a fallback, not the goal.

## Lineation policy for English

- do not mechanically mirror every Tamil physical line;
- do preserve stanza boundaries and major rhetorical units;
- preserve short emphatic lines when their force depends on isolation;
- preserve visible stepped/list movement when it contributes to crescendo or contrast;
- do not collapse verse into prose paragraphs.

## Notes policy

Translator's notes are permitted for:

- historically specific political references;
- classical/literary allusions;
- wordplay that cannot survive fully in English;
- a source-supported expression whose literal image may puzzle an English reader;
- a translation choice where two plausible English renderings materially differ.

Notes must be concise and must not become a second interpretive essay.

## Assembly and release stages

After all five batches are reviewed:

1. create `idhayathai-thanthidu-anna-en.md` from **reviewed batches only**;
2. compare assembled English against every batch and the Tamil source map;
3. create `EDITORIAL_CONSISTENCY_REVIEW.md` covering names, titles, recurring terms, quotation style, punctuation philosophy and voice consistency;
4. perform a full **Kalaignar voice review** across the poem, especially repeated phrases and the final elegiac sequence;
5. create `RELEASE_REPORT.md` only after all checks pass.

## Release criteria

English may be called release-ready only when:

- all five batches are reviewed;
- no Tamil source unit is omitted or duplicated;
- no explanatory invention appears inside the verse;
- recurring Tamil terms/names are translated consistently unless context requires variation;
- rhetorical repetitions remain intact unless a documented exception is necessary;
- the English remains recognisably Kalaignar in directness, public cadence, literary-political density and grief;
- final editorial consistency review passes.

## Exact next activity

Begin **Batch 01 — scans 13–15 / printed pages 11–13**.

Before drafting, reread `pages/0013.md`–`pages/0015.md` and the corresponding assembly blocks. Translate only that batch, then perform source-fidelity and Kalaignar-voice review before moving to Batch 02.
