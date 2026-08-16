# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported முன்னுரை/பின்னுரை/படக்குறிப்பு போன்ற பதிப்பு அடுக்குகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown-ஆகப் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, punctuation/எழுத்து/பெயர்/தேதி/வரி அமைப்பை standardize செய்யவோ, தெளிவில்லாத இடத்தை பொருள் பார்த்து ஊகித்து நிரப்பவோ கூடாது.

**மூல PDF கோப்புகள் repository-யில் commit செய்யப்படாது.** Filename, checksum, scan identity, edition/publication details, page mapping, transcription, audit மற்றும் பின்னர் உருவாகும் translation/review layers மட்டும் repository-யில் இருக்கும்.

## தற்போதைய படைப்பு

| படைப்பு | ஆசிரியர் | source identity | நிலை |
|---|---|---|---|
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | 28-scan-page booklet; scan 13 identifies the poem as a 09-02-1969 Chennai radio tribute to பேரறிஞர் அண்ணா | **28/28 source complete; Tamil assembly PASS; English translation planning complete** |

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
```

விரிவான workflow: [`POEM_PROCESSING_GUIDE.md`](POEM_PROCESSING_GUIDE.md).  
முதல் முழுமையான படைப்பு: [`poems/idhayathai-thanthidu-anna/README.md`](poems/idhayathai-thanthidu-anna/README.md).

## இதயத்தைத் தந்திடு அண்ணா — தற்போதைய நிலை

- scans **1–28**: complete physical source — **verified 28/28**
- scans **13–26**: poem body — **verified 14/14**
- poem `needs-review`: **0**
- poem `blocked`: **0**
- assembled Tamil poem: [`sections/idhayathai-thanthidu-anna.md`](poems/idhayathai-thanthidu-anna/sections/idhayathai-thanthidu-anna.md) — **created and reviewed**
- assembly review: [`ASSEMBLY_REVIEW.md`](poems/idhayathai-thanthidu-anna/ASSEMBLY_REVIEW.md) — **PASS; 14/14 source page blocks matched, 0 discrepancies**
- source completeness review: [`SOURCE_COMPLETENESS_REVIEW.md`](poems/idhayathai-thanthidu-anna/SOURCE_COMPLETENESS_REVIEW.md) — **PASS; 28/28**
- Tamil archival/source layer: **COMPLETE**
- English translation planning: **COMPLETE**
- governing translation principle: **retain Kalaignar's language/voice — cadence, rhetoric, repetition, political/literary density and grief — rather than smoothing him into generic English**
- English translation drafting: **not started**

## அடுத்த activity

Begin English translation **Batch 01 — scans 13–15 / printed pages 11–13** using:

- [`translations/en/README.md`](poems/idhayathai-thanthidu-anna/translations/en/README.md)
- [`translations/en/TRANSLATION_PLAN.md`](poems/idhayathai-thanthidu-anna/translations/en/TRANSLATION_PLAN.md)
- [`translations/en/SOURCE_MAP.md`](poems/idhayathai-thanthidu-anna/translations/en/SOURCE_MAP.md)

Translate only Batch 01 first. Before moving to Batch 02, perform both **source-fidelity** review and an explicit **Kalaignar-voice fidelity** review.
