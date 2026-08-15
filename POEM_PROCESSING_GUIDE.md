# Kalaignar Poems Processing Guide

இந்த repository-யில் கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், இரங்கற்பாக்கள், வாழ்த்துப் பாடல்கள் மற்றும் தனிநூலாக வெளியான கவிதைப் பதிப்புகளை source-first முறையில் மின்னாக்குவதற்கான நிரந்தர வழிகாட்டி.

## 1. அடிப்படை விதி

> **மூல ஸ்கேன் தான் controlling source.**

Markdown உரை மூலத்தைப் பாதுகாக்க வேண்டும்; புதிய/திருத்தப்பட்ட பதிப்பை உருவாக்கக் கூடாது.

அமைதியாக செய்யக்கூடாதவை:

- எழுத்துப்பிழை என்று தோன்றுவதைத் திருத்துதல்;
- பழைய எழுத்து/சொல் வடிவங்களை நவீனப்படுத்துதல்;
- punctuation, sandhi, பெயர்கள், எண்கள், தேதிகளை standardize செய்தல்;
- வரி முறிப்பை prose போல மறுவடிவமைத்தல்;
- rhyme/metre/meaning பார்த்து source-ல் தெளிவில்லாத சொல்லை ஊகித்தல்;
- மற்ற பதிப்பு அல்லது இணைய உரையை controlling scan-க்கு பதிலாகப் பயன்படுத்துதல்;
- scan-ல் இல்லாத heading அல்லது stanza label-ஐ body text-க்குள் silently சேர்த்தல்.

## 2. PDF policy

Source PDF repository-க்குள் commit செய்யப்படாது.

ஒவ்வொரு source-க்கும் `metadata/source.md`-ல் குறைந்தது பின்வருவன பதிவு செய்ய வேண்டும்:

- source filename;
- SHA-256 checksum;
- file size;
- scan page count;
- title / author as printed;
- edition / publication details visible in scan;
- poem performance/publication context visible in scan;
- printed-page numbering behaviour;
- scan condition;
- photographs, captions, advertisements, library marks, handwriting, bleed-through போன்ற anomalies.

## 3. ஒவ்வொரு படைப்பிற்குமான அமைப்பு

```text
poems/<slug>/
  README.md
  metadata/
    source.md
  indexes/
    page-map.md
  pages/
    0001.md
    0002.md
    ...
  sections/
  audit.md
```

பின்னர் தேவைக்கேற்ப:

```text
  ASSEMBLY_REVIEW.md
  HANDOVER.md
  translations/en/
    README.md
    TRANSLATION_PLAN.md
    SOURCE_MAP.md
    batches/
    <slug>-en.md
    EDITORIAL_CONSISTENCY_REVIEW.md
    RELEASE_REPORT.md
```

## 4. பக்கவாரி பதிவு

ஒவ்வொரு scan page-க்கும் Markdown record இருக்க வேண்டும் — cover, advertisement, photograph, preface, poem, imprint, back cover அனைத்தும் உட்பட.

Example front matter:

```yaml
---
scan_page: 1
printed_page: null
work: "idhayathai-thanthidu-anna"
section: "cover"
page_type: "cover"
status: "verified"
language: "ta"
source_filename: "...pdf"
transcription_method: "direct visual comparison with source scan"
---
```

Status values:

- `not-started`
- `partial`
- `needs-review`
- `verified`
- `blocked`

`verified` என்பது scan-ஐ நேரடியாகப் பார்த்து எழுத்து, punctuation, lineation, page role மற்றும் non-text marks அனைத்தையும் உறுதிப்படுத்திய பின்னரே பயன்படுத்த வேண்டும்.

## 5. கவிதை lineation policy

கவிதைக்கு வரி அமைப்பு உரையின் ஒரு பகுதி. ஆகவே:

1. source-ல் ஒரு poetic line எங்கு முடிகிறதோ அங்கு Markdown-லும் line break காக்க வேண்டும்;
2. indentation source-ல் தெளிவாக semantic/poetic அமைப்பாக இருந்தால் காக்க வேண்டும்;
3. scan layout காரணமாக மட்டும் உடைந்த long line என்பதை உறுதிப்படுத்தாமல் join செய்யக்கூடாது;
4. stanza இடைவெளிகள் source-ல் இருப்பின் blank line-ஆகப் பாதுகாக்க வேண்டும்;
5. quotation marks, ellipses, dashes, repeated punctuation source-supported வடிவிலேயே இருக்க வேண்டும்;
6. verse-ஐ prose paragraph-ஆக மாற்றக்கூடாது;
7. later assembled `sections/<slug>.md` page records-ன் verified lineation-ஐ மட்டுமே இணைக்க வேண்டும்.

## 6. Difficult reading protocol

ஒரு கவிதை வாசிப்பு கடினமாக இருப்பதற்காக உடனே `blocked` விடக்கூடாது.

முன் முயற்சிக்க வேண்டியவை:

1. native/high-resolution scan inspection;
2. enlarged crops;
3. grayscale/contrast/sharpening போன்ற non-destructive variants;
4. neighbouring glyph/typeform comparison;
5. previous/next line and page-boundary continuation checks;
6. repeated phrase / refrain / internal parallelism only as a clue — never as authority;
7. user-supplied reading-ஐ source pixels-க்கு எதிராக verify செய்தல்;
8. தேவைப்பட்டால் provenance-உடைய independent secondary witness-ஐ corroboration-க்கு மட்டும் பயன்படுத்துதல்.

Secondary witness wording controlling scan-க்கு silently import செய்யக்கூடாது. தீர்வு source image ஆதரிப்பதாக இருக்க வேண்டும்; witness வேறுபாடு audit-ல் பதிவு செய்ய வேண்டும்.

## 7. Printed-page mapping

`indexes/page-map.md`-ல் scan number மற்றும் **visible** printed page number தனித்தனியாகப் பதிவு செய்ய வேண்டும்.

Printed number தெரியாத இடத்தில் inferred number-ஐ printed value போல எழுதக்கூடாது. தேவையானால் note column-ல் sequence inference தனியாகக் குறிப்பிடலாம்.

## 8. Front matter / photographs / advertisements

கவிதை மட்டும் அல்லாமல் source publication-ன் physical evidence-யும் archive செய்யப்படும்.

- preface/foreword முழுமையாக page records-ல் பாதுகாக்க வேண்டும்;
- photograph pages-ல் visible caption இருந்தால் verbatim transcription செய்ய வேண்டும்;
- caption இல்லாத புகைப்படத்தை identity inference செய்து label செய்யக்கூடாது;
- advertisements/posters poem body-இல் சேர்க்கப்படாது; தனி page type-ஆகப் பாதுகாக்கப்படும்;
- library stamp, handwriting போன்ற later marks printed text-இல் இருந்து வேறுபடுத்தி note செய்ய வேண்டும்.

## 9. Poem-body scope

ஒவ்வொரு work README-யும் poem body எந்த scan-ல் தொடங்கி எந்த scan-ல் முடிகிறது என்பதை source-supported முறையில் பதிவு செய்ய வேண்டும்.

Assembled poem:

```text
sections/<slug>.md
```

இந்த file:

- verified poem pages-ஐ மட்டும் சேர்க்க வேண்டும்;
- scan-page markers அல்லது source map references வைத்திருக்கலாம்;
- front matter, publisher advertisement, printer imprint ஆகியவற்றை poem verse-க்குள் கலந்து விடக்கூடாது.

## 10. Audit

`audit.md`-ல் குறைந்தது:

- page status totals;
- poem-body verified / needs-review / blocked counts;
- difficult readings;
- source marks affecting text;
- corrections/reopens;
- assembled-poem readiness;
- translation readiness

பதிவு செய்ய வேண்டும்.

## 11. Translation policy

English translation archival Tamil transcription complete ஆன பிறகே தொடங்க வேண்டும்.

Translation:

- source meaning, rhetoric, repetition மற்றும் imagery-ஐ பாதுகாக்க வேண்டும்;
- Tamil lineation-ஐ blindly mimic செய்ய வேண்டிய அவசியம் இல்லை; ஆனால் poetic structure மறையக்கூடாது;
- names/titles/context normalize செய்யப்படும் இடங்களில் notes/provenance தேவை;
- unresolved Tamil reading இருந்தால் English-ல் silently guess செய்யக்கூடாது.

## 12. Commit discipline

- work directly on `main` unless the user explicitly requests another workflow;
- duplicate work directories உருவாக்கக்கூடாது;
- source PDF commit செய்யக்கூடாது;
- ஒவ்வொரு activity-க்கும் தெளிவான archival commit message பயன்படுத்த வேண்டும்;
- activity முடிவில் README/HANDOVER-ல் exact next step update செய்ய வேண்டும்.

## 13. Completion criteria

ஒரு கவிதையின் Tamil archival layer source-complete என்று கருதுவதற்கு:

- எல்லா physical scan pages-க்கும் page records இருக்க வேண்டும்;
- poem-body scan pages அனைத்தும் `verified` அல்லது documented terminal `blocked` ஆக இருக்க வேண்டும்;
- assembled poem page records-க்கு எதிராக review செய்யப்பட்டிருக்க வேண்டும்;
- silent normalization இருக்கக்கூடாது;
- audit page/source counts match ஆக வேண்டும்;
- source PDF repository-க்கு வெளியே இருக்க வேண்டும்.

நிரந்தர நோக்கம்: **source fidelity first; readability second; editorial interpretation always explicit.**
