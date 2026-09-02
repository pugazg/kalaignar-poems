# கலைஞர் கவிதைகள் — மின்னாக்கக் களஞ்சியம்

கலைஞர் மு. கருணாநிதியின் கவிதைகள் மற்றும் source-supported பதிப்பு அடுக்குகளை source-first முறையில் பாதுகாக்கும் repository.

> **மூல ஸ்கேன் controlling source.** Explicitly user-designated exact-source word-for-word transcription may control lexical words only where its supplied body text actually matches the source. **Markdown-ல் உள்ள page-number labels positional authority அல்ல; first/last matching body word/paragraph anchors மூலமாகவே alignment செய்ய வேண்டும்.** Source-established scan structure controls placement, punctuation, quotation structure, lineation and non-body separation.

## Phase-separated workflow

1. Phase 1 — transcription only
2. Phase 2 — source-critical verification / lexical-control clearance
3. Phase 3 — structure, completeness, canonical assembly, Tamil final clearance
4. Phase 4 — translation/release

## தற்போதைய படைப்புகள்

| படைப்பு | நிலை |
|---|---|
| கலைஞரின் கவிதைகள் | **ACTIVE — Phase 1 COMPLETE; Phase 2 source coverage 465/465 COMPLETE; C01–C12 COMPLETE; C13 NEXT; Phase 3 BLOCKED** |
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
- cumulative status: **0 partial, 154 needs-review, 311 verified**;
- unresolved backlog: **154 pages**;
- verified: **0001–0300, 0310, 0317, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**;
- durable contiguous verified boundary: **scans 1–300**.

### Clearance C12 — COMPLETE

C12 covers physical scans **276–300**.

User clarified that Markdown page numbers must not be used to locate supplied transcription; the correct alignment is by starting and ending body words/paragraphs. Applying that rule showed:

- `kavi5.md` starts with `நடந்திடுவேன் நமது அய்யா, / அண்ணா வழியில்!`, which matches physical scan **293** / attached `part_012` page 18;
- it ends with `அழுக்குருவின் சிரத்தை அறுத்தெறிந்தார்`, matching physical scan **300** / attached `part_012` page 25;
- therefore `kavi5.md` is lexical control for **293–300**, irrespective of its internal page labels;
- scans **276–292** have no matching supplied Markdown body text and were independently verified directly against the newly attached exact-source `part_012_pages_276-300.pdf`;
- pre-existing verified scans **285, 292, 296** remained verified.

Direct-source C12 corrections included source-visible `சேறு`, two `குழந்தைகட்கு` forms, `சூளுரை`, `மேடைப் பேச்சரங்கில்`, `அழித்தாராம்`, and `வாக்குக்குச்` on scans 280, 284, 286, 287 and 288.

Result: **276–300 = 25/25 verified**. C12 adds **15** new promotions to the earlier partial state and advances the contiguous verified boundary to **1–300**.

### Exact next activity

Begin **C13 — physical scans 301–325**. Use uploaded `kavi6.md` only after content-anchor alignment. Its first body paragraph `அது கண்ட பார்வதி கொதித் தெழுந்து...` matches attached `part_013` page 1 / scan 301, and its ending `மாறப்போகும் மனிதன் எடுக்கப் போகும் - ஜென்மம்தானே?..` matches attached `part_013` page 25 / scan 325, so its full 25-page body range is aligned to C13. Preserve/reconcile already verified scans **310** and **317**. Do not begin C14, Phase 3, canonical assembly or translation in the same activity.
