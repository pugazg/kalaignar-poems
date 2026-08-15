# இதயத்தைத் தந்திடு அண்ணா

கலைஞர் மு. கருணாநிதியின் **இதயத்தைத் தந்திடு அண்ணா** கவிதையை, அதை வெளியிட்டுள்ள இந்த 28-scan-page booklet-ன் physical/source context-உடன் source-first முறையில் பாதுகாக்கும் archival work directory.

## Source authority

> **இந்த work-க்கு supplied scan தான் controlling source.**

மூலத்தில் இருப்பதை silently modernize, correct, normalize, reconstruct அல்லது improve செய்யக்கூடாது. குறிப்பாக கவிதையின் line breaks, indentation, punctuation, quotation marks, ellipses மற்றும் repetition source feature-களாகக் கருதப்பட வேண்டும்.

Source PDF repository-யில் commit செய்யப்படவில்லை; checksum மற்றும் source identity மட்டும் metadata-வில் பதிவு செய்யப்பட்டுள்ளது.

## Source identity

- Source filename: `TVA_BOK_0064132_இதயத்தைத்_தந்திடு_அண்ணா.pdf`
- Scan pages: **28**
- Poem opening: scan **13**
- Poem end: scan **26**
- Scan 13 printed page: **11**
- Scans 13–25 visible printed pages: **11–23**
- Scan 26 visible printed page number: **none observed**

Full source note: [`metadata/source.md`](metadata/source.md).

## Poem context printed in the source

The heading on scan 13 identifies this as **இதயத்தைத் தந்திடு அண்ணா** and states in parentheses that on **9.2.1969**, on **சென்னை வானொலி**, **கலைஞர் மு. கருணாநிதி** offered the poem as a **கண்ணீர்க் கவிதாஞ்சலி** to **பேரறிஞர் அண்ணா**.

This wording is preserved as source evidence rather than rewritten into a normalized historical description.

## Physical publication structure

| Scan range | Role | Status |
|---|---|---|
| 1 | front cover | verified |
| 2 | book-donation advertisement/list | verified |
| 3–4 | photograph / portrait front matter | verified |
| 5–10 | `என்னுரை` by குறிஞ்சி சுப்பிரமணியன் | verified |
| 11–12 | captioned photograph pages | verified |
| 13–26 | complete poem body; scan 26 also carries printer imprint | **verified 14/14** |
| 27 | colour poster / congratulatory back matter | not started |
| 28 | back cover photograph and caption | not started |

Detailed mapping: [`indexes/page-map.md`](indexes/page-map.md).

## Current archival status

- repository structure: **created**
- source checksum / file size / page count: **recorded**
- physical page map: **current through scan 26**
- verified physical page records: **26 / 28** — scans **1–26**
- remaining physical pages: **2 / 28** — scans **27–28**, both non-poem back matter
- poem-body verified: **14 / 14** — scans **13–26**
- poem `needs-review`: **0**
- poem `blocked`: **0**
- assembled Tamil poem: **not yet created intentionally**
- assembly readiness: **READY**
- English translation: **not started / intentionally deferred**

Current audit: [`audit.md`](audit.md).

## Page structure

```text
pages/
  0001.md  # verified
  ...
  0012.md  # verified front matter
  0013.md  # verified poem opening
  ...
  0026.md  # verified poem conclusion + separate printer imprint
  0027.md  # not started — poster
  0028.md  # not started — back cover
```

## Poem source status

The Tamil poem source layer at page-record level is now complete:

- scans **13–18 / printed pages 11–16** — verified;
- scans **19–25 / printed pages 17–23** — verified;
- scan **26** — final poem lines verified; no printed page number inferred; printer imprint separated from verse.

Source-fidelity decisions include retaining unusual or difficult readings only after direct scan comparison. Examples from the second batch include:

- scan 20: `மகாத்மாவின் தோன்றல்`, `கீரியென்றால்`;
- scan 21: `பல்லாவரத்தார்`, `ஈன்றாள் எனினும்;`;
- scan 22: `மாறிற்றுத் தமிழர் மனம்`, `வாடினாள்`, `சுடுநெருப்பில்`;
- scan 23: `கடிதோச்சி`, `அமுத மொழி`, `போதாகி`;
- scan 24: `வளையாத நெஞ்சுப் பாரதிக்கும்`, `கால்டுவெல் போப்புக்கும்`;
- scan 25: source punctuation such as `வைத்த போது..` and `எம் அண்ணா.. இதயமன்னா...`;
- scan 26: `இதயத்தை தந்திடண்ணா..` and the final `அண்ணா...`.

See [`audit.md`](audit.md) for the complete verification trail.

## Assembly target

After this page-level closure, the poem should be assembled at:

```text
sections/idhayathai-thanthidu-anna.md
```

Assembly rules:

1. use **only** verified verse from scans 13–26;
2. keep scan 13's printed contextual note outside poem verse;
3. keep scan 26's printer imprint outside poem verse;
4. preserve page-supported lineation, stanza boundaries, punctuation and source forms;
5. perform a page-to-assembly comparison and record it in `ASSEMBLY_REVIEW.md` before translation.

## Next activity

Create and review the assembled Tamil poem from the verified page records **13–26**. Do not begin English translation yet.

Scans **27–28** remain a separate physical-source closure task and must also be archived before the entire 28-scan booklet is declared source-complete.
