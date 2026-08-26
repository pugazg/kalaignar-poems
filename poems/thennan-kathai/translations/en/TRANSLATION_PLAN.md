# English Translation Plan — தென்னவன் காதை

## 1. Objective

Create an English literary translation of **தென்னவன் காதை** from the final-cleared canonical Tamil assembly while preserving the poem's narrative stance, rhetoric, repetition, imagery, invective, dramatic speech and political-cultural framing.

This is a translation layer, not a correction or modernization of the Tamil archive.

## 2. Controlling Tamil text

Translation authority:

`../../sections/thennan-kathai.md`

Supporting provenance:

- `../../pages/0145.md` through `../../pages/0152.md`;
- `../../ASSEMBLY_REVIEW.md`;
- `../../audit.md`.

Earlier superseded readings must never be reintroduced from old commits, OCR, catalogue text, prior chat text, or visual guesses.

## 3. Non-negotiable fidelity rules

1. Preserve the **speaker/narrator's viewpoint** rather than neutralizing it.
2. Preserve strong praise, accusation, satire and insult where they remain in the canonical Tamil text; do not soften them merely for modern taste.
3. Do not intensify rhetoric beyond the Tamil.
4. Preserve repeated words and parallel constructions when they carry rhetorical force.
5. Preserve major metaphors and similes rather than replacing them with explanatory prose.
6. Do not silently harmonize contradictions, unusual grammar, spelling or historical usage.
7. Do not import wording from the Ramayana tradition or modern retellings merely because a passage is familiar.
8. Names and titles may use readable English forms, but the Tamil source meaning and role must remain traceable.
9. The English poem need not reproduce every physical Tamil line break mechanically, but stanza structure, speech boundaries and rhetorical pacing must remain visible.
10. Where the Tamil has an unresolved or deliberately unusual form, do not guess a smoother English meaning without recording the decision during review.

## 4. User-directed omission on scan 151

The canonical Tamil text contains one explicit user-directed omission of a caste-based slur.

Translation policy for that location:

- do **not** restore the omitted word;
- do **not** transliterate it;
- do **not** insert an English substitute such as an insult, caste label or descriptive adjective;
- translate only the canonical Tamil words that remain;
- keep the omission documented in editorial/review metadata, not inside the poem as a bracketed reconstruction.

This instruction overrides any earlier source-faithfulness rule at that single location.

## 5. Names and terminology — Gate A baseline

Gate A has reviewed the initial voice/terminology choices. Use these forms consistently unless a later batch review documents a context-specific exception.

| Tamil | English handling | Review note |
|---|---|---|
| இராவணன் | Ravana | retain name consistently |
| இராமன் / ராமன் | Rama | do not normalize the Tamil archival layer; English uses one standard name |
| சீதை / சீதாதேவி | Sita / Sita Devi according to local rhetorical context | retain local form when rhetorically useful |
| இலக்குவன் | Lakshmana | standard readable English form |
| கும்பகர்ணன் | Kumbhakarna | standard readable English form |
| வீடணன் / விபீஷணா | Vibhishana | English normalization allowed only in translation layer |
| சுக்ரீவன் | Sugriva | standard readable English form |
| அனுமன் | Hanuman | standard readable English form |
| மண்டோதரி | Mandodari | retain name |
| ஆரியர் / ஆரியர்கள் | Aryan / Aryans | preserve the poem's political-rhetorical use; do not replace with a neutral historical paraphrase |
| தமிழர் / தமிழினம் | Tamils / Tamil people according to exact context | do not weaken the narrator's identity rhetoric |
| பார்ப்பனர் / பார்ப்பனர்கள் | Brahmin / Brahmins | preserve direct reference where present |
| பூசுரர்கள் | earth-god priests | Gate A choice; do not silently collapse into `Brahmins` |
| இருடிகள் | rishis | Gate A choice |

Gate A also established that compressed source images should remain open where possible: do not add unsupported attributes simply to make an image sound more natural in English.

## 6. Translation style

Target style:

- literary but clear English;
- energetic narrative movement;
- preserve exclamations, commands and direct address;
- retain rhetorical repetition such as paired or repeated cries where possible;
- keep metaphorical density rather than explaining metaphors in-line;
- avoid archaic pseudo-Biblical English unless the Tamil itself specifically demands an elevated register;
- avoid academic explanatory language inside the poem.

Explanatory context, if needed, belongs in translation notes/review documents rather than in the verse body.

## 7. Batch plan

### EN-01 — scans 145–146

Scope:

- poem opening and Ravana/Mandodari portrait;
- rejection of sacrificial violence;
- transition into the forest episode;
- Muthunagai episode through the end of scan 146.

Status: **REVIEWED / PASS — Gate A cleared**.

Review record: `GATE_A_REVIEW.md`.

### EN-02 — scans 147–148

Scope:

- aftermath of Muthunagai's mutilation;
- Ravana/Sita encounter;
- abduction passage;
- Lanka, Vibhishana and Aryan-strategy passages through the end of scan 148.

Special care:

- quotation boundaries on scan 147 are unusual and must not be silently repaired;
- page 148 follows the user-confirmed lexical-control text;
- use the Gate A voice/terminology baseline.

Status: **NOT STARTED — next permitted batch**.

### EN-03 — scans 149–151

Scope:

- Sugriva passage;
- Vibhishana conflict;
- Kumbhakarna sequence;
- Ravana's long speech beginning on scan 149, continuing through scan 150 and closing on scan 151;
- battle narrative through the end of scan 151.

Special care:

- keep the cross-page speech continuous in English even though source-page provenance remains tracked;
- preserve the user-directed omission on scan 151 without replacement.

Status: **BLOCKED pending Gate B**.

### EN-04 — scan 152

Scope:

- final battle;
- Vibhishana's spear attack;
- Ravana's fall and final speech;
- reaction of Lanka;
- terminal separator.

Status: **BLOCKED**.

## 8. Batch file plan

```text
translations/en/batches/
  EN-01-scans-145-146.md
  EN-02-scans-147-148.md
  EN-03-scans-149-151.md
  EN-04-scan-152.md
```

Each batch should contain:

1. source-scan range;
2. Tamil-source pointers;
3. English translation only;
4. a short translator-review section listing deliberate terminology or structural decisions;
5. no speculative reconstruction of omitted or unclear source material.

## 9. Review gates

### Gate A — EN-01 voice review

**CLEARED.** See `GATE_A_REVIEW.md`.

Gate A reviewed:

- Ravana/Rama naming;
- Aryan/Tamil/Brahmin terminology;
- treatment of rhetorical insults;
- line/stanza density;
- punctuation and quotation style;
- whether the English sounds literary without becoming freer than the Tamil.

It also caught and corrected one surviving scan-145 source punctuation discrepancy before approval.

### Gate B — EN-02 consistency review

After drafting EN-02, check continuity of terminology, direct speech, unusual scan-147 quotation handling and fidelity to the user-controlled scan-148 text before EN-03.

### Gate C — EN-03 omission and speech review

Explicitly confirm:

- the scan-149→150→151 speech is continuous;
- the scan-151 omitted term has not been restored or paraphrased;
- no superseded Tamil reading has returned.

### Gate D — EN-04 + full-work review

After EN-04, compare the complete English draft to `SOURCE_MAP.md`, then create the final assembled English poem only after every batch passes.

## 10. Final deliverables — later stages

```text
translations/en/batches/*.md
translations/en/thennan-kathai-en.md
translations/en/EDITORIAL_CONSISTENCY_REVIEW.md
translations/en/RELEASE_REPORT.md
```

## 11. Current status

- plan: **REVIEWED / PASS**;
- source map: **REVIEWED / PASS**;
- EN-01: **REVIEWED / PASS — Gate A cleared**;
- EN-02: **NOT STARTED — next permitted batch**;
- EN-03: **BLOCKED pending Gate B**;
- EN-04: **BLOCKED**;
- final assembled English poem: **NOT STARTED**;
- next permissible translation activity: **EN-02 scans 147–148 only**.

Do not begin EN-03 in the same activity as EN-02 drafting. Gate B must be completed first.