# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported முன்னுரை/பின்னுரை/படக்குறிப்பு போன்ற பதிப்பு அடுக்குகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown-ஆகப் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, punctuation/எழுத்து/பெயர்/தேதி/வரி அமைப்பை standardize செய்யவோ, தெளிவில்லாத இடத்தை பொருள் பார்த்து ஊகித்து நிரப்பவோ கூடாது.

**மூல PDF கோப்புகள் repository-யில் commit செய்யப்படாது.** Filename, checksum, scan identity, edition/publication details, page mapping, transcription, audit மற்றும் பின்னர் உருவாகும் translation/review layers மட்டும் repository-யில் இருக்கும்.

## தற்போதைய படைப்பு

| படைப்பு | ஆசிரியர் | source identity | நிலை |
|---|---|---|---|
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | 28-scan-page booklet; scan 13 identifies the poem as a 09-02-1969 Chennai radio tribute to பேரறிஞர் அண்ணா | **Tamil archival layer COMPLETE — 28/28 scans verified; poem 14/14; assembly PASS** |

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
```

விரிவான workflow: [`POEM_PROCESSING_GUIDE.md`](POEM_PROCESSING_GUIDE.md).  
முதல் முழுமையான படைப்பு: [`poems/idhayathai-thanthidu-anna/README.md`](poems/idhayathai-thanthidu-anna/README.md).

## இதயத்தைத் தந்திடு அண்ணா — இறுதி நிலை

- scans **1–12**: front matter / photographs / `என்னுரை` — **verified**
- scans **13–26**: complete poem body — **verified 14/14**
- scan **26**: printer imprint separately recorded and excluded from poem assembly
- scan **27**: colour poster / World Classical Tamil Conference back matter — **verified**
- scan **28**: back cover — **verified**
- verified physical scans overall: **28 / 28**
- physical `needs-review`: **0**
- physical `blocked`: **0**
- assembled Tamil poem: [`sections/idhayathai-thanthidu-anna.md`](poems/idhayathai-thanthidu-anna/sections/idhayathai-thanthidu-anna.md) — **created and reviewed**
- assembly review: [`ASSEMBLY_REVIEW.md`](poems/idhayathai-thanthidu-anna/ASSEMBLY_REVIEW.md) — **PASS; 14/14 source page blocks matched, 0 discrepancies**
- source completeness review: [`SOURCE_COMPLETENESS_REVIEW.md`](poems/idhayathai-thanthidu-anna/SOURCE_COMPLETENESS_REVIEW.md) — **PASS; 28/28**
- Tamil archival/source layer: **COMPLETE**
- English translation: **not yet started**

## அடுத்த activity

The first work is now fully closed at the Tamil archival/source level. The next activity can establish the **English translation plan and review workflow** for `இதயத்தைத் தந்திடு அண்ணா`, while keeping all verified Tamil source files immutable except for documented source corrections.
