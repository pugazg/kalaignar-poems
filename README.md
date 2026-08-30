# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported பதிப்பு அடுக்குகளை source-first முறையில் பாதுகாக்கும் repository.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

Source PDF repository-யில் commit செய்யப்படாது. Source wording, punctuation, lineation, பெயர்கள், தேதிகள், historical spelling மற்றும் source anomalies silently normalize செய்யப்படக் கூடாது.

Live GitHub `main` is authoritative. Old prompt text or checkpoint SHAs must never roll back newer completed work.

## Phase-separated workflow

See `TRANSCRIPTION_PHASE_PLAN.md` and `POEM_PROCESSING_GUIDE.md`.

1. **Phase 1 — transcription only**
2. **Phase 2 — source-critical visual verification**
3. **Phase 3 — structure/completeness/assembly and Tamil final clearance**
4. **Phase 4 — translation/release after Tamil final clearance**

## தற்போதைய படைப்புகள்

| படைப்பு | ஆசிரியர் | நிலை |
|---|---|---|
| கலைஞரின் கவிதைகள் | மு. கருணாநிதி | **ACTIVE — new source intake registered; 150-scan partial source tranche; Phase 1 batch 01 scans 1–25 NEXT** |
| காலப் பேழையும் கவிதைச் சாவியும் | மு. கருணாநிதி | **Tamil FINAL-CLEARED; English Phase 4 COMPLETE — RELEASE-CLEARED; 58/58 items; 58/58 standalone English files** |
| தென்னவன் காதை | மு. கருணாநிதி | **Tamil FINAL-CLEARED; English translation paused; resume only by explicit user scope** |
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | **Tamil source COMPLETE; English translation RELEASE-COMPLETE** |
| அணையா விளக்கு அண்ணா | மு. கருணாநிதி | **Existing separate work; consult its live work README before resuming** |

## கலைஞரின் கவிதைகள் — active source

Work directory: `poems/kalaignarin-kavithaigal/`

Controlling source currently supplied: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`.

- physical scans available: **150**;
- file size: **486,369,088 bytes**;
- source checksum: **pending exact-byte computation**;
- printed source: **கலைஞரின் கவிதைகள்**, **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**;
- Phase 1 page records: **0/150**;
- exact next activity: **Phase 1 scans 1–25**.

Critical completeness boundary: this 150-scan PDF is only a partial scan of the printed edition. Contents scans 15–17 list entries beginning through at least printed page 444, while scan 150 visibly carries printed page 133 and still contains continuing body text. Therefore 150/150 available-scan transcription must never be described as whole-book completion. Continuation source is required before whole-book Tamil final clearance.

The anthology also contains works already represented by other controlling sources in this repository, including `இதயத்தைத் தந்திடு அண்ணா!` and `தென்னவன் காதை`. Those existing texts are not transcription authority for this edition witness and must not be copied into the new work.

## காலப் பேழையும் கவிதைச் சாவியும் — final state

Work directory: `poems/kaalap-pezhaiyum-kavithai-saaviyum/`

- controlling PDF: `TVA_BOK_0063593_காலப்_பேழையும்_கவிதைச்_சாவியும்.pdf`;
- physical scans: **306**;
- Phase 1 transcription: **306/306 — COMPLETE**;
- Phase 2 source-critical verification: **306/306 — COMPLETE**;
- Phase 3 structural gates: **COMPLETE — PASS**;
- canonical Tamil items: **58/58**;
- Tamil final clearance: **PASS**;
- English translation batches: **21/21 reviewed PASS**;
- English stable items: **58/58**;
- numbered-item English scan coverage: **290/290**, scans **10–299**;
- editorial consistency/Kalaignar-voice review: **PASS**;
- final source-coverage/release review: **PASS**;
- complete English collection: `translations/en/kaalap-pezhaiyum-kavithai-saaviyum-en.md` — **RELEASE-CLEARED**;
- standalone English item files: `translations/en/items/` — **58/58 release-cleared synchronized copies**;
- durable release report: `translations/en/RELEASE_REPORT.md`;
- unresolved release issues: **0**;
- Tamil canonical/page files changed during Phase 4: **0**.

The numbered item range is scans **10–299**. Scan 299 closes with `(முதல் பாகம் முற்றிற்று)`; scan 300 begins separate `குறிப்புகள்` end matter and is outside the numbered-poem English release.

No routine Phase-4 activity remains for this work. Do not reopen it without explicit user scope or a genuine source-backed discrepancy.

## தென்னவன் காதை — continuation guardrail

Tamil source/assembly layer is **FINAL-CLEARED**. English translation is partially complete and paused. Resume only when explicitly selected. Its next permitted translation batch is **EN-03 — scans 149–151**, followed by Gate C before EN-04.

A documented user-directed omission on scan 151 is durable editorial control: do not restore, reconstruct, quote, transliterate, paraphrase, replace or indirectly supply the excluded term unless the user explicitly changes that instruction.

## இதயத்தைத் தந்திடு அண்ணா

Tamil archival/source layer is complete and English translation is **RELEASE-COMPLETE**. Do not retranscribe, normalize, retranslate or alter this released work unless a genuine source-level discrepancy is documented or the user explicitly requests a separately tracked revision.

## Continuation rule

A fresh chat must reconstruct state from live GitHub before doing work. Read `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, `POEM_PROCESSING_GUIDE.md`, `TRANSCRIPTION_PHASE_PLAN.md`, this README and the selected work's live state/control files completely. Completion of one work does not authorize silently selecting another project.
