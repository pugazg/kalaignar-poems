# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported முன்னுரை/பின்னுரை/படக்குறிப்பு போன்ற பதிப்பு அடுக்குகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown-ஆகப் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, punctuation/எழுத்து/பெயர்/தேதி/வரி அமைப்பை standardize செய்யவோ, தெளிவில்லாத இடத்தை பொருள் பார்த்து ஊகித்து நிரப்பவோ கூடாது.

**மூல PDF கோப்புகள் repository-யில் commit செய்யப்படாது.** Filename, checksum, scan identity, edition/publication details, page mapping, transcription, audit மற்றும் பின்னர் உருவாகும் translation/review layers மட்டும் repository-யில் இருக்கும்.

## தற்போதைய படைப்பு

| படைப்பு | ஆசிரியர் | source identity | நிலை |
|---|---|---|---|
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | 28-scan-page booklet; scan 13 identifies the poem as a 09-02-1969 Chennai radio tribute to பேரறிஞர் அண்ணா | **26/28 physical scans verified; poem 14/14 verified; Tamil assembly next** |

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
    audit.md
    translations/
```

விரிவான workflow: [`POEM_PROCESSING_GUIDE.md`](POEM_PROCESSING_GUIDE.md).  
தற்போதைய படைப்பு: [`poems/idhayathai-thanthidu-anna/README.md`](poems/idhayathai-thanthidu-anna/README.md).

## தற்போதைய நிலை

- scans **1–12**: front matter / photographs / `என்னுரை` — **verified**
- scans **13–26**: complete poem body — **verified 14/14**
- poem `needs-review`: **0**
- poem `blocked`: **0**
- scan **26**: poem conclusion verified; printer imprint separately recorded and excluded from poem assembly scope
- scans **27–28**: non-poem back matter — **not started**
- verified physical scans overall: **26 / 28**
- assembled Tamil poem: **not yet created intentionally; READY for assembly**
- English translation: **deferred until Tamil assembly/source review is stable**

## அடுத்த activity

Assemble **இதயத்தைத் தந்திடு அண்ணா** from the verified poem page records **scans 13–26**, excluding scan 13's contextual note from verse and excluding scan 26's printer imprint. Perform a page-to-assembly source comparison and record it in `ASSEMBLY_REVIEW.md` before any English translation.

The non-poem back-matter scans **27–28** remain to be archived before the entire physical booklet is declared source-complete.
