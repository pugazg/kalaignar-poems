# Scan 146 — third source-critical re-audit

Date: **2026-08-25**

## Why this re-audit was required

Scan 146 had already passed two earlier verification cycles, yet a fresh user review identified eleven incorrect readings. That demonstrates that the previous recovery method was still too dependent on whole-word recognition and familiar Tamil forms.

The controlling authority remains the scan pixels. The user-supplied corrected forms were treated as hypotheses and rechecked against the native source image and enlarged source crops before being admitted to the canonical page record.

## Confirmed corrections

| Previous repository reading | Correct source reading | Failure type |
|---|---|---|
| `உருவினை` | `உருவினான்` | word-final `-னான்` lost; whole-word silhouette misread |
| `கொடுவாள்` | `கொடுவாளை` | accusative `-ளை` ending lost |
| `தாள்` | `தாளை` | final `-ை` lost |
| `பாறை` | `பாளை` | internal `ற/ள` substitution reinforced by familiar word shape |
| `ஆரியத்தேன்` | `ஆரியத்தேளை` | final `-ளை` cluster lost |
| `தவசிகள்` | `தவசிகளை` | accusative ending omitted |
| `சின்னவனும்` | `சின்னவனாம்` | `-ஆம்` misread as `-உம்` |
| `கள்ளப்பினில்` | `களைப்பினால்` | whole-word segmentation failure plus `-னால்` ending loss |
| `தூங்குகின்றுள்` | `தூங்குகின்றாள்` | final `-ஆள்` misread |
| `கண்ணழகித்` | `கண்மூடித்` | semantic/word-shape substitution; multiple internal glyphs misread |
| `தாயவள்` | `தூயவளை` | internal vowel plus accusative `-ளை` lost |

## Corrected source lines

The corrections restore these source-visible lines:

```text
கொடுமையென உருவினான் கொடுவாளை!
...
அவன் தாளை, அந்தப்
பருவ மங்கையரின் சிரிப்போ பிளந்த பாளை!
அட, தொடுவேனோ ஆரியத்தேளை என
...
தண்டகாரண்யத் தவசிகளை எதிர்த்து ஊதி
...
சின்னவனாம் இலக்குவனும் சீதையெனும்
...
களைப்பினால் தூங்குகின்றாள் கனிமரச்
சோலையோரம்.
...
கமலமலர்க் கண்மூடித் தூங்குகின்ற தூயவளை
```

## What failed in the earlier method

This pass establishes several concrete failure modes:

1. **Suffix blindness** — `-ளை`, `-ை`, `-ஆம்`, `-னால்`, and `-ஆள்` were repeatedly lost or replaced.
2. **Whole-word completion** — the reader recognized a plausible Tamil word silhouette first and then filled uncertain glyphs from expectation.
3. **Semantic anchoring** — familiar forms such as `பாறை`, `கண்ணழகித்`, and `தாயவள்` were accepted even when the printed letter sequence differed.
4. **Repeated-candidate confirmation** — once an incorrect candidate entered the repository, later enlarged checks tended to verify the candidate rather than independently account for every glyph.
5. **Upscaling overconfidence** — a larger render improves visibility but does not create missing source detail; it cannot substitute for comparing complete lines and grammatical endings against the native scan.

## Revised checking rule

For the final 145–152 audit, every line must be checked as a sequence of printed characters, not as recognized words. In particular:

- explicitly account for every word-final vowel marker and consonant;
- check `-ளை/-ை/-ஆம்/-னால்/-ஆள்/-ன்/-னான்` endings independently;
- compare complete lines before cropping individual words;
- use semantic sense only as a reason to re-inspect, never as evidence for a reading;
- any page that produces a comparable cluster of corrections must have its earlier `verified` claim treated as superseded by the later pass.

## Repository consequence

`pages/0146.md` has been corrected and re-verified under this stricter third-pass procedure. The earlier scan-146 PASS descriptions are historical only and must not be cited as evidence for the corrected text.

The work-wide **145–152 final continuity/transcription audit remains mandatory** before Tamil assembly or English translation.