# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported பதிப்பு அடுக்குகளை source-first முறையில் பாதுகாக்கும் repository.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூல PDF repository-யில் commit செய்யப்படாது. மூல wording, punctuation, lineation, பெயர், தேதி, historical spelling ஆகியவற்றை silently normalize செய்யக்கூடாது.

## Phase-separated workflow

Long/book-length sources may be processed in explicit phases. See `TRANSCRIPTION_PHASE_PLAN.md` and `POEM_PROCESSING_GUIDE.md`.

1. **Phase 1 — transcription only:** build page records from the controlling scan; newly transcribed pages are normally `partial` / `needs-review`, not automatically `verified`.
2. **Phase 2 — source-critical visual verification:** independently reread and verify every transcription against the scan.
3. **Phase 3 — structure/completeness/assembly:** complete mapping, page joins, work boundaries, canonical Tamil assembly and final clearance.
4. **Phase 4 — translation/release:** begin only after Tamil final clearance.

A work's live README/HANDOVER declares its current phase. Do not perform later-phase activities early.

## தற்போதைய படைப்புகள்

| படைப்பு | ஆசிரியர் | நிலை |
|---|---|---|
| காலப் பேழையும் கவிதைச் சாவியும் | மு. கருணாநிதி | **ACTIVE — Phase 2 source-critical visual verification; scans 1–250 verified consecutively; scans 251–275 next** |
| தென்னவன் காதை | மு. கருணாநிதி | **Tamil FINAL-CLEARED; English translation in progress, currently paused while another work is active** |
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | **Tamil source COMPLETE; English translation RELEASE-COMPLETE** |
| அணையா விளக்கு அண்ணா | மு. கருணாநிதி | **Restarted from supplied scan; fresh source setup COMPLETE; page verification STARTED** |

## காலப் பேழையும் கவிதைச் சாவியும் — தற்போதைய நிலை

- controlling PDF: **306 physical scans**;
- Phase 1 transcription: **306/306 physical scans represented**;
- contents: **58/58 entries represented**;
- current phase: **Phase 2 — independent source-critical visual verification**;
- verified range: **scans 1–250 consecutively**;
- completed Phase-2 batches: **1–25**, **26–50**, **51–75**, **76–100**, **101–125**, **126–150**, **151–175**, **176–200**, **201–225**, **226–250**;
- next verification batch: **scans 251–275**;
- Phase-3 continuity/completeness/assembly and Phase-4 translation remain intentionally deferred.

During Phase 2, independently reread each page against the controlling scan and correct only scan-proven discrepancies. Do not promote semantic expectations over visible source evidence.

## அணையா விளக்கு அண்ணா — தற்போதைய நிலை

- previous work: **DELETED at user request**
- controlling source: newly supplied 19-scan PDF
- fresh source identity/checksum: **COMPLETE**
- physical page classification: **19/19 mapped preliminarily**
- verified fresh page records: **2/19**
- Tamil poem transcription: **NOT STARTED**
- Tamil assembly: **PENDING**
- English translation: **PENDING**

When this work is resumed, continue source-first under `poems/anaiya-vilakku-anna/` from its live work documents.
