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
| 13–18 | poem body — first batch | verified |
| 19–26 | poem body remainder; scan 26 also carries printer imprint | not started |
| 27 | colour poster / congratulatory back matter | not started |
| 28 | back cover photograph and caption | not started |

Detailed mapping: [`indexes/page-map.md`](indexes/page-map.md).

## Current archival status

- repository structure: **created**
- source checksum / file size / page count: **recorded**
- physical page map: **current through scan 18**
- verified page records: **18 / 28** — scans **1–18**
- front matter scans 1–12: **complete / verified**
- poem-body verified: **6 / 14** — scans **13–18**
- poem-body remaining: **8 / 14** — scans **19–26**
- `needs-review` poem scans: **0**
- `blocked` poem scans: **0**
- assembled Tamil poem: **not yet started intentionally**
- audit: **current through scan 18**
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
  0018.md  # verified poem
  0019.md  # next
  ...
  0028.md
```

Each physical scan gets its own record, including non-poem material. After all poem scans are verified and source comparison is complete, the poem will be assembled separately at:

```text
sections/idhayathai-thanthidu-anna.md
```

## First poem batch — scans 13–18

The first six poem scans are now directly compared with the source and marked `verified`.

Source-fidelity decisions recorded in the page files/audit include:

- scan 13: printed radio/context note kept separate from verse;
- scan 14: unusual readings such as `தங்கு சனி வேல்`, `வேது`, `பொருதடக்கை`, and `களப்பரணி..` retained;
- scan 15: `அரு மூன்று எழுத்தாலே` and `அய்ம்பத்திரண்டுதனில்` retained;
- scan 16: repeated `முன்றெழுத்து` and `எடெல்லாம் வீடெல்லாம் தமிழ்` retained;
- scan 17: `மாண்பே! .` and `நாலைந்து` retained;
- scan 18: source forms such as `பனிமலர் வீழ் தும்பியதாய்த்`, `கோலற்ற குருடர்`, and `தீர் அண்ணா திராவிடர் கழகமெனும்` retained.

No web text, remembered version, metre-based reconstruction or silent normalization was used as authority.

## Source variations already preserved in front matter

The foreword contains source-supported variations which have deliberately **not** been normalized, including:

- scan 10: `மொழிபெயர்ப்பு செய்யப்பட்டு`;
- scan 10: later title occurrence `“இதயத்தை தந்திடு அண்ணா”`, while other occurrences print `“இதயத்தைத் தந்திடு அண்ணா”`.

See [`audit.md`](audit.md) for the verification trail.

## Next activity

Continue the poem from **scan 19 / printed page 17**. Process **scans 19–26** as the next poem batch if practical:

1. re-open every scan directly at high enough resolution;
2. create `pages/0019.md` through `pages/0026.md`;
3. preserve exact poem lineation, indentation, stanza spacing, quotation marks, dashes, repetition and ellipses;
4. on scan 26, keep the poem conclusion separate from the printer imprint;
5. update page map and audit counts;
6. only after all poem-body scans 13–26 are verified, consider assembling `sections/idhayathai-thanthidu-anna.md` and performing an assembly review.

Do **not** begin English translation yet.
