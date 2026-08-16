# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported முன்னுரை/பின்னுரை/படக்குறிப்பு போன்ற பதிப்பு அடுக்குகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown-ஆகப் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, punctuation/எழுத்து/பெயர்/தேதி/வரி அமைப்பை standardize செய்யவோ, தெளிவில்லாத இடத்தை பொருள் பார்த்து ஊகித்து நிரப்பவோ கூடாது.

**மூல PDF கோப்புகள் repository-யில் commit செய்யப்படாது.**

## தற்போதைய படைப்பு

| படைப்பு | ஆசிரியர் | source identity | நிலை |
|---|---|---|---|
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | 28-scan-page booklet; scan 13 identifies the poem as a 09-02-1969 Chennai radio tribute to பேரறிஞர் அண்ணா | **28/28 source complete; Tamil assembly PASS; English Batches 01–03 reviewed PASS** |

## களஞ்சிய அமைப்பு

```text
README.md
POEM_PROCESSING_GUIDE.md
HANDOVER.md
poems/
  idhayathai-thanthidu-anna/
    README.md
    metadata/source.md
    indexes/page-map.md
    pages/
    sections/
    ASSEMBLY_REVIEW.md
    SOURCE_COMPLETENESS_REVIEW.md
    audit.md
    translations/en/
      README.md
      TRANSLATION_PLAN.md
      SOURCE_MAP.md
      batches/
        batch-01.md
        batch-02.md
        batch-03.md
```

விரிவான workflow: [`POEM_PROCESSING_GUIDE.md`](POEM_PROCESSING_GUIDE.md).  
தற்போதைய work: [`poems/idhayathai-thanthidu-anna/README.md`](poems/idhayathai-thanthidu-anna/README.md).

## இதயத்தைத் தந்திடு அண்ணா — தற்போதைய நிலை

- physical source: **28/28 verified**
- poem body: **14/14 verified**
- Tamil assembly: **PASS; 0 discrepancies**
- Tamil archival/source layer: **COMPLETE**
- governing English principle: **retain Kalaignar's language/voice — cadence, rhetoric, repetition, political/literary density and grief**
- English Batch 01, scans **13–15**: **REVIEWED PASS**
- English Batch 02, scans **16–19**: **REVIEWED PASS**
- English Batch 03, scans **20–21**: [`batch-03.md`](poems/idhayathai-thanthidu-anna/translations/en/batches/batch-03.md) — **REVIEWED PASS**
- Batches 01–03 source omissions / duplications: **0 / 0**
- Batches 01–03 Kalaignar-voice reviews: **PASS**
- English Batches **04–05**: **not started**

Batch 03 preserves the paired public questions across the Batch 02 → 03 boundary, Kalaignar's governance/political praise, the tiger/plough and Giri mountain-cloud imagery, named literary figures, the `மலர் / மன்னன் / நூல்` parallelism, and the sharp turn into caste/social critique. Difficult `சழக்கரால்` is not silently normalized.

## அடுத்த activity

Begin English translation **Batch 04 — scans 22–23 / printed pages 20–21**.

Carry forward the social critique into scan 22, preserve Mother Tamil's personification and the Valluvar dialogue, and protect the scan 22 → 23 quotation continuation. Batch 04 must pass source-fidelity and Kalaignar-voice review before Batch 05.
