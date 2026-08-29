# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported பதிப்பு அடுக்குகளை source-first முறையில் பாதுகாக்கும் repository.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூல PDF repository-யில் commit செய்யப்படாது. மூல wording, punctuation, lineation, பெயர், தேதி, historical spelling ஆகியவற்றை silently normalize செய்யக்கூடாது.

## Phase-separated workflow

See `TRANSCRIPTION_PHASE_PLAN.md` and `POEM_PROCESSING_GUIDE.md`.

1. **Phase 1 — transcription only**
2. **Phase 2 — source-critical visual verification**
3. **Phase 3 — structure/completeness/assembly and Tamil final clearance**
4. **Phase 4 — translation/release after Tamil final clearance**

## தற்போதைய படைப்புகள்

| படைப்பு | ஆசிரியர் | நிலை |
|---|---|---|
| காலப் பேழையும் கவிதைச் சாவியும் | மு. கருணாநிதி | **ACTIVE — Phase 3; scan↔printed-page reconciliation COMPLETE; 58-item boundary/page-join audit NEXT** |
| தென்னவன் காதை | மு. கருணாநிதி | **Tamil FINAL-CLEARED; English translation in progress, currently paused while another work is active** |
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | **Tamil source COMPLETE; English translation RELEASE-COMPLETE** |
| அணையா விளக்கு அண்ணா | மு. கருணாநிதி | **Restarted from supplied scan; fresh source setup COMPLETE; page verification STARTED** |

## காலப் பேழையும் கவிதைச் சாவியும் — தற்போதைய நிலை

- controlling PDF: **306 physical scans**;
- Phase 1 transcription: **306/306 — COMPLETE**;
- contents: **58/58 entries verified**;
- Phase 2 source-critical verification: **306/306 — COMPLETE**;
- unresolved readings after Phase 2: **none**;
- Phase 3 activity 1 — exact physical scan ↔ printed-page reconciliation: **COMPLETE**;
- numbered pagination: scans **5–299** correspond continuously to printed pages **4–298**;
- all **306 physical scans** are structurally accounted for;
- all **58 contents start pages** align with title scans by `title scan = contents start page + 1`;
- detailed Phase-3 mapping: `poems/kaalap-pezhaiyum-kavithai-saaviyum/indexes/page-map.md`;
- Phase-3 structural audit: `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_STRUCTURE_AUDIT.md`;
- exact next activity: **58-item boundary certification and within-item page-join continuity audit**;
- canonical Tamil assembly remains blocked until that structural audit passes;
- Phase 4 translation remains blocked until Tamil final clearance.

Known contents/title-page witness differences and source anomalies remain separate witnesses and must not be silently normalized during Phase 3.

## அணையா விளக்கு அண்ணா — தற்போதைய நிலை

- previous work: **DELETED at user request**;
- controlling source: newly supplied 19-scan PDF;
- fresh source identity/checksum: **COMPLETE**;
- physical page classification: **19/19 mapped preliminarily**;
- verified fresh page records: **2/19**;
- Tamil poem transcription: **NOT STARTED**;
- Tamil assembly: **PENDING**;
- English translation: **PENDING**.
