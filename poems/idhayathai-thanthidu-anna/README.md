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

- verified physical page records: **26 / 28** — scans **1–26**
- remaining physical pages: **2 / 28** — scans **27–28**, both non-poem back matter
- poem-body verified: **14 / 14** — scans **13–26**
- poem `needs-review`: **0**
- poem `blocked`: **0**
- assembled Tamil poem: [`sections/idhayathai-thanthidu-anna.md`](sections/idhayathai-thanthidu-anna.md) — **created**
- assembly review: [`ASSEMBLY_REVIEW.md`](ASSEMBLY_REVIEW.md) — **PASS**
- assembly page blocks checked: **14 / 14**
- assembly discrepancies: **0**
- English translation: **not started / intentionally deferred until physical booklet closure**

Current audit: [`audit.md`](audit.md).

## Tamil assembly

The assembled poem is built **only** from the verified `Poem text` blocks in scans **13–26**.

Assembly rules applied:

1. scan 13's printed contextual note is represented outside the verse body;
2. scan 26's printer imprint is excluded from verse;
3. no cross-page wording was silently joined or rewritten;
4. physical page boundaries remain traceable through hidden source comments;
5. page-supported indentation, stanza breaks, punctuation and unusual source forms remain unchanged.

A direct page-to-assembly comparison was completed after creation. The review found **14/14 page blocks present, no duplicates, no missing blocks, and no textual discrepancies**. See [`ASSEMBLY_REVIEW.md`](ASSEMBLY_REVIEW.md).

Source-fidelity examples retained in the assembly include `களப்பரணி..`, `அய்ம்பத்திரண்டுதனில்`, repeated `முன்றெழுத்து`, `மாண்பே! .`, `பிரிவாய்மாறி`, `கீரியென்றால்`, `மாறிற்றுத் தமிழர் மனம்`, `கடிதோச்சி`, `போதாகி மலர்கின்ற`, `கால்டுவெல் போப்புக்கும் சிலை`, `பற்றுதனை உலகறிய ; அந்த`, and `இதயத்தை தந்திடண்ணா..`.

## Page structure

```text
pages/
  0001.md  # verified
  ...
  0026.md  # verified poem conclusion + separate printer imprint
  0027.md  # next — poster
  0028.md  # next — back cover
sections/
  idhayathai-thanthidu-anna.md  # assembled + reviewed
ASSEMBLY_REVIEW.md               # PASS
```

## Next activity

Archive the remaining physical-source back matter:

1. create `pages/0027.md` from scan 27, preserving its poster/congratulatory material as printed;
2. create `pages/0028.md` from scan 28, preserving its photograph caption and visible artwork/text without identity inference beyond printed labels;
3. update `indexes/page-map.md` and `audit.md` to **28/28** if both verify cleanly;
4. run a final physical-source completeness check.

Do **not** begin English translation until that closure is complete.
