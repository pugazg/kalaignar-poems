# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள், கவியரங்கப் பாடல்கள், தனிநூல்களாக வெளியான கவிதைப் பதிப்புகள் மற்றும் அவற்றைச் சூழ்ந்த source-supported பதிப்பு அடுக்குகளை source-first முறையில் பாதுகாக்கும் repository.

## மூலக் கொள்கை

> **மூல ஸ்கேன் தான் controlling source. Markdown ஒரு பாதுகாப்பு அடுக்கு; திருத்தப்பட்ட புதிய பதிப்பு அல்ல.**

மூல PDF repository-யில் commit செய்யப்படாது. மூல wording, punctuation, lineation, பெயர், தேதி, historical spelling ஆகியவற்றை silently normalize செய்யக்கூடாது.

Live GitHub `main` is authoritative for continuation. Old prompt text or checkpoint SHAs must never be used to roll back a newer completed state.

## Phase-separated workflow

See `TRANSCRIPTION_PHASE_PLAN.md` and `POEM_PROCESSING_GUIDE.md`.

1. **Phase 1 — transcription only**
2. **Phase 2 — source-critical visual verification**
3. **Phase 3 — structure/completeness/assembly and Tamil final clearance**
4. **Phase 4 — translation/release after Tamil final clearance**

## தற்போதைய படைப்புகள்

| படைப்பு | ஆசிரியர் | நிலை |
|---|---|---|
| காலப் பேழையும் கவிதைச் சாவியும் | மு. கருணாநிதி | **ACTIVE — Phase 3 canonical assembly; 11/58 item files assembled; next scans 60–84** |
| தென்னவன் காதை | மு. கருணாநிதி | **Tamil FINAL-CLEARED; English translation in progress, currently paused while another work is active** |
| இதயத்தைத் தந்திடு அண்ணா | மு. கருணாநிதி | **Tamil source COMPLETE; English translation RELEASE-COMPLETE** |
| அணையா விளக்கு அண்ணா | மு. கருணாநிதி | **Existing separate work; consult its live work README before resuming** |

## காலப் பேழையும் கவிதைச் சாவியும் — தற்போதைய நிலை

Work directory: `poems/kaalap-pezhaiyum-kavithai-saaviyum/`

- controlling PDF: `TVA_BOK_0063593_காலப்_பேழையும்_கவிதைச்_சாவியும்.pdf`;
- physical scans: **306**;
- Phase 1 transcription: **306/306 — COMPLETE**;
- contents: **58/58 entries verified**;
- Phase 2 source-critical verification: **306/306 — COMPLETE**;
- unresolved readings after Phase 2: **none**;
- Phase 3 activity 1 — exact physical scan ↔ printed-page reconciliation: **COMPLETE**;
- numbered pagination: scans **5–299** correspond continuously to printed pages **4–298**;
- all **306 physical scans** structurally accounted for;
- all **58 contents start pages** align with title scans by `title scan = contents start page + 1`;
- Phase 3 activity 2 — item boundary / within-item page-join audit: **COMPLETE — 58/58 certified**;
- Phase 3 activity 3 — title-witness reconciliation: **COMPLETE — 14/14 discrepancy cases reconciled**;
- Phase 3 activity 4 — canonical Tamil assembly: **IN PROGRESS — 11/58 canonical item files assembled**;
- completed canonical files: `sections/01.md` through `sections/11.md`;
- latest canonical-assembly iteration: **scans 35–59 — COMPLETE**;
- exact next activity: **process scans 60–84 as the next 25-scan canonical-assembly iteration**, completing carried item 12 from scans 58–63;
- create `sections/12.md` through `sections/15.md` from their full verified ranges;
- item 16 begins at scan 82 and runs through scan 87, so **do not publish a partial `sections/16.md` at scan 84**;
- assembly/source-completeness review: **BLOCKED until 58/58 canonical item files exist**;
- Tamil final clearance: **PENDING assembly/source-completeness review**;
- Phase 4 translation: **BLOCKED until Tamil final clearance**.

Detailed Phase-3 records:

- `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_STRUCTURE_AUDIT.md`;
- `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_BOUNDARY_JOIN_AUDIT.md`;
- `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_TITLE_WITNESS_RECONCILIATION.md`;
- `poems/kaalap-pezhaiyum-kavithai-saaviyum/PHASE3_CANONICAL_ASSEMBLY.md`;
- `poems/kaalap-pezhaiyum-kavithai-saaviyum/indexes/page-map.md`.

### Canonical assembly title rule

Contents/title-page witness differences exist for items **18, 22, 25, 26, 29, 31, 32, 37, 40, 44, 46, 50, 54 and 58**.

For assembly:

- title-page witness = displayed canonical title;
- contents witness = preserved source/index witness and alternate metadata;
- no hybrid normalized title;
- stable item sequence remains **1–58**;
- item 37 remains sequence item 37 although its title page visibly prints item number **36**.

## தென்னவன் காதை — continuation guardrail

Tamil source/assembly layer is **FINAL-CLEARED**. English translation is partially complete. When explicitly resumed, read its live translation control files first. The next permitted translation batch is **EN-03 — scans 149–151**, followed by Gate C before EN-04.

A documented user-directed omission on scan 151 is durable editorial control: do not restore, reconstruct, quote, transliterate, paraphrase, replace or indirectly supply the excluded term unless the user explicitly changes that instruction.

## இதயத்தைத் தந்திடு அண்ணா

Tamil archival/source layer is complete and English translation is **RELEASE-COMPLETE**. Do not retranscribe, normalize, retranslate or alter this released work unless a genuine source-level discrepancy is found and documented or the user explicitly requests a separately tracked revision.

## Continuation rule

A fresh chat must reconstruct state from live GitHub before doing work. Read `HANDOVER.md`, `NEXT_CHAT_PROMPT.md`, `POEM_PROCESSING_GUIDE.md`, `TRANSCRIPTION_PHASE_PLAN.md`, this README, and the active work's control/state files completely. Do not restart completed phases because an older document or prompt says otherwise.
