# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported முன்னுரை/பின்னுரை/படக்குறிப்பு போன்ற பதிப்பு அடுக்குகளை மூல ஸ்கேன்களின் பக்க வரிசையைக் காக்கும் வகையில் Markdown-ஆகப் பாதுகாக்கும் களஞ்சியம்.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூலத்தில் இருப்பதை அமைதியாகச் சீர்திருத்தவோ, நவீனப்படுத்தவோ, punctuation/எழுத்து/பெயர்/தேதி/வரி அமைப்பை standardize செய்யவோ, தெளிவில்லாத இடத்தை பொருள் பார்த்து ஊகித்து நிரப்பவோ கூடாது.

**மூல PDF கோப்புகள் repository-யில் commit செய்யப்படாது.** Filename, checksum, scan identity, edition/publication details, page mapping, transcription, audit மற்றும் பின்னர் உருவாகும் translation/review layers மட்டும் repository-யில் இருக்கும்.

## தற்போதைய படைப்பு

| படைப்பு | ஆசிரியர் | source identity | நிலை |
|---|---|---|---|
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | 28-scan-page booklet; scan 13 identifies the poem as a 09-02-1969 Chennai radio tribute to பேரறிஞர் அண்ணா | **12/28 physical scans verified; front matter 1–12 complete; poem 0/14 — next scan 13** |

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

## அடுத்த activity

`இதயத்தைத் தந்திடு அண்ணா` scans **1–12** source-faithfully archived and verified. Begin the poem with **scans 13–18 / printed pages 11–16** as the first poem batch, preserving the scan's exact poetic lineation and keeping the contextual note on scan 13 separate from the verse.
