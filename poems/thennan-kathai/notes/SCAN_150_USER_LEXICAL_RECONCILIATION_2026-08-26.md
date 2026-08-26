# Scan 150 — user lexical-control reconciliation

Date: **2026-08-26**

## Why this reconciliation was required

Pages 146–149 demonstrated that the earlier visual-reading workflow could repeatedly misclassify older Tamil typeface forms, including whole words and compact vowel/suffix shapes. The user therefore supplied the page-150 text directly as the lexical control.

The previous scan-150 recovery PASS is **superseded**.

## Canonical corrections

| Previous repository reading | User-supplied lexical reading |
|---|---|
| `இழிதொழிலோர்—பண்பிழந்தோர்—எத்திப் / பிழைப்போர்—` | `இழிதொழிலோர் - பண்பிழந்தோர் - எத்திப் / பிழைப்போர் -` |
| `அன்னவரையும்` | `அனைவரையும்` |
| `புலிகள் நண்பர்களே!` | `புலிநிகர் நண்பர்களே!` |
| `விட்டார்—தமிழக்` | `விட்டார் - தமிழ்க்` |
| `மடங்களாய்ப் போனதம்மோ!` | `மடங்களாய்ப் போன தம்போ!!` |
| `இழி சுக்கிரிவன்` | `இழி சுக்ரீவன்` |
| `எதிர்க்கின்றூர் என்ன / பென்றால்,` | `எதிர்க்கின்றார் என்னை / யென்றால்,` |
| `வேண்டும் / மன்றே?` | `வேண்டு / மன்றோ?` |
| `வேண்டுமென்று—` | `வேண்டுமென்று-` |
| `போடுகின்றூர்,` | `போடுகின்றார்,` |
| `பூப்பந்தனைய பொன் மகளாம்—என் துணைவி` | `பூப்பந்தனைய பொன் மகளாம்-என் துணைவி` |
| `யாப்புணையும்` | `பாப்புனையும்` |
| `கிட்டாத` | `கிட்டா த` |
| `பைந்தமிழாம்—` | `பைந்தமிழாம்-` |
| `கட்டி!` | `கட்டி !` |

## Page-structure handling

The physical scan is retained for page identity, illustration context, column order and directly unambiguous page structure. It shows no `★` separator on scan 150.

The supplied extraction places `அருமைத் தம்பிக்குத்...` immediately after `மடங்களாய்ப் போன தம்போ!!`; the canonical page record separates these at the physical column transition without changing either lexical sequence.

## Failure pattern reinforced

Scan 150 confirms that the earlier failures were not limited to the `-ஆன்` / `-உன்` distinction. The problem also includes:

- whole-word substitution (`அன்னவரையும்` / `அனைவரையும்`, `புலிகள்` / `புலிநிகர்`);
- consonant/vowel-sign misclassification (`தமிழக்` / `தமிழ்க்`);
- old-typeface reading drift (`எதிர்க்கின்றூர்` / `எதிர்க்கின்றார்`, `போடுகின்றூர்` / `போடுகின்றார்`);
- lexical replacement (`யாப்புணையும்` / `பாப்புனையும்`);
- silent punctuation and spacing normalization.

For this work, user-supplied exact corrective text must not be overridden by a conflicting visual guess.

## Result

`pages/0150.md` is reconciled to the user-supplied lexical control. The work remains **not final-cleared**; scans 151–152 still require the same strengthened review before Tamil assembly.