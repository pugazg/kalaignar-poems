# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள் மற்றும் source-supported பதிப்பு அடுக்குகளை source-first முறையில் பாதுகாக்கும் repository.

> **மூல ஸ்கேன் controlling source.** Explicitly user-designated exact-source word-for-word transcription may control lexical words for its stated range; source-established scan structure controls placement, punctuation, quotation structure, lineation and non-body separation.

## Phase-separated workflow

1. Phase 1 — transcription only
2. Phase 2 — source-critical verification / lexical-control clearance
3. Phase 3 — structure, completeness, canonical assembly, Tamil final clearance
4. Phase 4 — translation/release

## தற்போதைய படைப்புகள்

| படைப்பு | நிலை |
|---|---|
| கலைஞரின் கவிதைகள் | **ACTIVE — Phase 1 COMPLETE; Phase 2 source coverage 465/465 COMPLETE; C01–C11 COMPLETE; C12 PARTIAL; Phase 3 BLOCKED** |
| காலப் பேழையும் கவிதைச் சாவியும் | Tamil FINAL-CLEARED; English RELEASE-CLEARED |
| தென்னவன் காதை | Tamil FINAL-CLEARED; English translation paused |
| இதயத்தைத் தந்திடு அண்ணா | Tamil COMPLETE; English RELEASE-COMPLETE |

## கலைஞரின் கவிதைகள் — active source

- work directory: `poems/kalaignarin-kavithaigal/`;
- controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`;
- physical pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: **`19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`**;
- Phase 1: **465/465 COMPLETE**;
- Phase 2 source coverage: **465/465 COMPLETE**;
- cumulative status: **0 partial, 169 needs-review, 296 verified**;
- unresolved backlog: **169 pages**;
- verified: **0001–0275, 0285, 0292–0300, 0310, 0317, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**;
- durable contiguous verified boundary: **scans 1–275**.

### Clearance C12 — PARTIAL

C12 physical window is **276–300** and was intended to use uploaded `kavi5.md`, whose header identifies `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_012_pages_276-300.pdf`.

The actual attached Markdown payload does **not** contain lexical text for the whole claimed range. It begins with printed page **276**, which maps to physical scan **293**, and continues through printed page **283**, physical scan **300**. No supplied lexical text is present for physical scans **276–292** / printed pages **259–275**.

Accordingly:

- scans **293–300** are reconciled to the supplied lexical control and are `verified`;
- scan **296** retained its pre-existing verified status while being reconciled;
- scans **276–292** were **not** silently filled from scan-derived wording;
- pre-existing verified scans **285** and **292** remain verified;
- C12 is **PARTIAL**, not complete.

### Exact next activity

Recover/re-attach the missing word-for-word transcription for **physical scans 276–292 / printed pages 259–275** from the intended `part_012_pages_276-300` range, then finish C12 under the same lexical-control rule. Do not begin C13, Phase 3, canonical assembly or translation before C12 closes.
