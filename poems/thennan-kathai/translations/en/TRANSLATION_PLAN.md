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

Gate C and Gate D both confirmed that the omission remains preserved without replacement.

## 5. Names and terminology — reviewed baseline

| Tamil | English handling | Review note |
|---|---|---|
| இராவணன் | Ravana | retain name consistently |
| இராமன் / ராமன் | Rama | English uses one standard name |
| சீதை / சீதாதேவி | Sita / Sita Devi according to local rhetorical context | retain local form when rhetorically useful |
| இலக்குவன் | Lakshmana | standard readable English form |
| கும்பகர்ணன் | Kumbhakarna | standard readable English form |
| வீடணன் / விபீஷணா | Vibhishana | English normalization allowed only in translation layer |
| சுக்ரீவன் | Sugriva | standard readable English form |
| அனுமன் | Hanuman | standard readable English form |
| மண்டோதரி | Mandodari | retain name |
| ஆரியர் / ஆரியர்கள் | Aryan / Aryans | preserve the poem's political-rhetorical use |
| தமிழர் / தமிழினம் | Tamils / Tamil people according to context | do not weaken identity rhetoric |
| பார்ப்பனர் / பார்ப்பனர்கள் | Brahmin / Brahmins | preserve direct reference where present |
| பூசுரர்கள் | earth-god priests | Gate A choice; do not collapse into `Brahmins` |
| இருடிகள் | rishis | Gate A choice |

Additional reviewed choices include **the Southerner**, **fifth-column force**, and transliterated **aidai** for the unresolved canonical `ஐடை`.

## 6. Translation style

Target style:

- literary but clear English;
- energetic narrative movement;
- preserve exclamations, commands and direct address;
- retain rhetorical repetition where possible;
- keep metaphorical density rather than explaining metaphors in-line;
- avoid archaic pseudo-Biblical English unless demanded by the Tamil;
- avoid academic explanatory language inside the poem.

Explanatory context belongs in translation notes/review documents rather than in the verse body.

## 7. Batch plan and reviewed state

### EN-01 — scans 145–146

Scope: opening portrait; Ravana/Mandodari; rejection of sacrificial violence; forest/Muthunagai sequence through scan 146.

Status: **REVIEWED / PASS — Gate A cleared**.

Batch: `batches/EN-01-scans-145-146.md`  
Review: `GATE_A_REVIEW.md`

### EN-02 — scans 147–148

Scope: mutilation aftermath; Ravana/Sita encounter; boarding/abduction; Lanka/Vibhishana/Aryan-strategy sequence.

Special care: preserve scan 147's unusual quotation structure and the user-controlled scan-148 lexical reading.

Status: **REVIEWED / PASS — Gate B cleared**.

Batch: `batches/EN-02-scans-147-148.md`  
Review: `GATE_B_REVIEW.md`

### EN-03 — scans 149–151

Scope: Sugriva; Vibhishana conflict; Kumbhakarna; Ravana's long speech across scans 149–151; battle narrative through scan 151.

Special care: keep the cross-page speech continuous and preserve the scan-151 editorial omission without replacement.

Status: **REVIEWED / PASS — Gate C cleared**.

Batch: `batches/EN-03-scans-149-151.md`  
Review: `GATE_C_REVIEW.md`

### EN-04 — scan 152

Scope: final battle; Vibhishana's spear attack; Ravana's fall and final speech; Lanka's reaction; terminal separator.

Special care: preserve the 151→152 continuation, user-controlled scan-152 forms, self-contained final speech and terminal `★`.

Status: **REVIEWED / PASS — Gate D cleared**.

Batch: `batches/EN-04-scan-152.md`  
Full-work review: `GATE_D_REVIEW.md`

## 8. Batch file set

```text
translations/en/batches/
  EN-01-scans-145-146.md
  EN-02-scans-147-148.md
  EN-03-scans-149-151.md
  EN-04-scan-152.md
```

All four batch files are now reviewed and passed.

## 9. Review gates

### Gate A — EN-01 voice review

**CLEARED.** See `GATE_A_REVIEW.md`.

Established the voice/terminology baseline and corrected one surviving scan-145 source-punctuation discrepancy before approval.

### Gate B — EN-02 consistency review

**CLEARED.** See `GATE_B_REVIEW.md`.

Confirmed terminology continuity, scan-147 quotation handling, 147→148 narrative continuity, user-controlled scan-148 wording and two retained separators.

### Gate C — EN-03 omission and speech review

**CLEARED.** See `GATE_C_REVIEW.md`.

Confirmed the 149→150→151 continuous speech, preservation of the scan-151 omission without replacement, no return of superseded readings and all three scan-149 separators.

### Gate D — EN-04 + full-work review

**CLEARED.** See `GATE_D_REVIEW.md`.

Gate D confirmed:

- complete batch coverage for scans 145–152 with no overlap or gap;
- all seven cross-page joins;
- all eight `★` separators;
- quotation/speech continuity;
- terminology and rhetorical-force consistency;
- no reintroduction of superseded Tamil readings;
- continued preservation of the scan-151 editorial omission;
- EN-04 terminal speech and terminal separator.

## 10. Final deliverables — remaining stages

```text
translations/en/thennan-kathai-en.md
translations/en/EDITORIAL_CONSISTENCY_REVIEW.md
translations/en/RELEASE_REPORT.md
```

The final assembled English poem is now permitted but has **not** been created yet.

## 11. Current status

- plan: **REVIEWED / PASS**;
- source map: **REVIEWED / PASS**;
- EN-01: **REVIEWED / PASS — Gate A cleared**;
- EN-02: **REVIEWED / PASS — Gate B cleared**;
- EN-03: **REVIEWED / PASS — Gate C cleared**;
- EN-04: **REVIEWED / PASS — Gate D cleared**;
- full-work English review: **PASS**;
- final assembled English poem: **NOT STARTED — now permitted**;
- editorial consistency review: **NOT STARTED**;
- release report: **NOT STARTED**.

## Exact next activity

Create `translations/en/thennan-kathai-en.md` by concatenating only the reviewed English poem bodies from EN-01 through EN-04.

Preserve all seven narrative joins, all eight `★` separators, the scan-149→151 continuous speech, the scan-151 editorial omission, and the terminal `★` with no poem text after it.

Then perform `EDITORIAL_CONSISTENCY_REVIEW.md` before preparing `RELEASE_REPORT.md`.
