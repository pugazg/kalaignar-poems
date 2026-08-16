# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported முன்னுரை/பின்னுரை/படக்குறிப்பு போன்ற பதிப்பு அடுக்குகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown-ஆகப் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, punctuation/எழுத்து/பெயர்/தேதி/வரி அமைப்பை standardize செய்யவோ, தெளிவில்லாத இடத்தை பொருள் பார்த்து ஊகித்து நிரப்பவோ கூடாது.

**மூல PDF கோப்புகள் repository-யில் commit செய்யப்படாது.** Filename, checksum, scan identity, edition/publication details, page mapping, transcription, audit மற்றும் பின்னர் உருவாகும் translation/review layers மட்டும் repository-யில் இருக்கும்.

## தற்போதைய படைப்பு

| படைப்பு | ஆசிரியர் | source identity | நிலை |
|---|---|---|---|
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | 28-scan-page booklet; scan 13 identifies the poem as a 09-02-1969 Chennai radio tribute to பேரறிஞர் அண்ணா | **28/28 source complete; Tamil assembly PASS; English Batches 01–02 reviewed PASS** |

## களஞ்சிய அமைப்பு

```text
README.md
POEM_PROCESSING_GUIDE.md
HANDOVER.md
poems/
  idhayathai-thanthidu-anna/
    README.md
    metadata/
      source.md
    indexes/
      page-map.md
    pages/
    sections/
    ASSEMBLY_REVIEW.md
    SOURCE_COMPLETENESS_REVIEW.md
    audit.md
    translations/
      en/
        README.md
        TRANSLATION_PLAN.md
        SOURCE_MAP.md
        batches/
          batch-01.md
          batch-02.md
```

விரிவான workflow: [`POEM_PROCESSING_GUIDE.md`](POEM_PROCESSING_GUIDE.md).  
முதல் முழுமையான படைப்பு: [`poems/idhayathai-thanthidu-anna/README.md`](poems/idhayathai-thanthidu-anna/README.md).

## இதயத்தைத் தந்திடு அண்ணா — தற்போதைய நிலை

- scans **1–28**: complete physical source — **verified 28/28**
- scans **13–26**: poem body — **verified 14/14**
- assembled Tamil poem: **reviewed PASS; 0 discrepancies**
- source completeness review: **PASS; 28/28**
- Tamil archival/source layer: **COMPLETE**
- English translation planning: **COMPLETE**
- governing translation principle: **retain Kalaignar's language/voice — cadence, rhetoric, repetition, political/literary density and grief — rather than smoothing him into generic English**
- English Batch 01, scans **13–15 / printed pages 11–13**: [`batch-01.md`](poems/idhayathai-thanthidu-anna/translations/en/batches/batch-01.md) — **REVIEWED PASS**
- English Batch 02, scans **16–19 / printed pages 14–17**: [`batch-02.md`](poems/idhayathai-thanthidu-anna/translations/en/batches/batch-02.md) — **REVIEWED PASS**
- Batches 01–02 source omissions / duplications: **0 / 0**
- Batches 01–02 Kalaignar-voice reviews: **PASS**
- English Batches **03–05**: **not started**

Batch 02 preserves the repeated `முன்றெழுத்து` rhetoric by retaining the key Tamil lexical forms with compact English glosses and repeated `three letters`; Anna's slogans remain slogans, and `Dravidar Kazhagam`, `Munnetra Kazhagam`, `Ayya` and other relationship/political language are not flattened into generic prose.

## அடுத்த activity

Begin English translation **Batch 03 — scans 20–21 / printed pages 18–19**.

Preserve the rhetorical pairing between Batch 02's closing `யாரேனும் கேட்டதுண்டா?` and scan 20's `யாரேனும் புகன்றதுண்டா?`; retain Kalaignar's public/governance praise as rhetoric, named figures and literary references, and scan 21's compact `மலர் / மன்னன் / நூல்` parallelism. Batch 03 must again pass source-fidelity and Kalaignar-voice review before Batch 04.
