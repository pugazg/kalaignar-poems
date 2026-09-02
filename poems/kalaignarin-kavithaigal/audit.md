# Audit — கலைஞரின் கவிதைகள்

## Current state

**PHASE 1 COMPLETE — 465/465 records. PHASE 2 SOURCE-COVERAGE PASS COMPLETE — ALL 465 PHYSICAL SCANS HAVE BEEN REREAD. PAGE CLEARANCE REMAINS IN PROGRESS. C01–C11 COMPLETE. C12 PARTIAL.**

- controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`;
- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: **`19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`**;
- cumulative page status: **0 `partial`, 169 `needs-review`, 296 `verified`**;
- verified pages: **0001–0275, 0285, 0292–0300, 0310, 0317, 0328, 0332, 0371, 0372, 0373, 0392, 0393, 0447, 0465**;
- unresolved backlog: **169 `needs-review` pages**;
- durable contiguous verified boundary: **scans 1–275**;
- Phase 3 / canonical assembly / English translation: **blocked**.

## Completed clearance history

- C01–C03: scans **1–75**;
- C04: **76–100** supplied Gemini lexical control;
- C05: **101–125** supplied lexical control;
- C06: **126–150** supplied lexical control;
- C07: **151–175** supplied lexical control;
- C08: **176–200** `kavi1.md`;
- C09: **201–225** `kavi2.md`;
- C10: **226–250** `kavi3.md`;
- C11: **251–275** `kavi4.md`.

All completed ranges retain supplied lexical words while source-established structure controls page placement, punctuation, quotations, speaker/performance-note boundaries, lineation and non-body separation.

## Clearance C12 — PARTIAL

Target physical window: **276–300**.

### Supplied-control integrity check

Uploaded `kavi5.md` states that it is word-for-word text extracted from:

`TVA_BOK_0064091_கலைஞரின்_கவிதைகள்_part_012_pages_276-300.pdf`

But the actual attached Markdown payload does not contain the full declared range. It begins with printed page **276** and ends with printed page **283**. Under the already established page map:

- printed 276 = physical scan **293**;
- printed 283 = physical scan **300**.

No lexical transcription is present in `kavi5.md` for physical scans **276–292** / printed pages **259–275**.

### Safe C12 actions completed

- scans **293–300** were reconciled to the supplied `kavi5.md` words;
- scan **296** retained its pre-existing verified status while being reconciled;
- scans **293, 294, 295, 297, 298, 299, 300** were newly promoted to `verified`;
- pre-existing verified scans **285** and **292** were preserved;
- scans **276–284 and 286–291** remain `needs-review` because the user-designated lexical text for them is missing;
- no absent lexical wording was reconstructed from grammar, context, scan-derived alternatives or another transcription.

### Supplied lexical forms retained on 293–300

Examples include `உடன் பிறப்பே`, `சோதரிகள்`, `குறளையும்`, `உதடசைக்கு`, `எழுபத்தி`, `உலைக்களத்துக்`, `கை நிறைய`, `காலனியாய்`, `நாடாகக்`, `இந்தி வெறியர்களின்`, `கறுப்பு`, `சூளூரை`, `அணுப் பொழுதுமின்றி`, `நாடதிர`, `எங்குதித்த`, `கங்குகரை`, `கனல் கிளம்ப`, `கலிங்கத்துப்`, `பழம்பாட்டே`, `சூளுரை`, `வைதீகபுரியை`, `செல்லுபடியானதில்லை`, `சினந்து`, `புதுமைக் காளைகள்`, `இந்நாட்டான்`, `கொழித்து விட்ட உமிகள்`, `உதித்துவிட்ட`, `உயர்ஜாதிக்காரர்`, `கடவுளரின்`, `நடத்துகின்றீர்`, `ஆனகதி`, `சிவனாரும்`.

### Non-body/extraction handling

- running `கலைஞரின்` / `கவிதைகள்` headers excluded;
- printed page numerals excluded;
- `mimage A` and stray non-Tamil extraction text excluded;
- page and item boundaries remain those already source-established in the page layer.

### C12 result so far

- newly promoted pages: **7**;
- cumulative moved from **0 / 176 / 289** to **0 / 169 / 296**;
- contiguous boundary remains **1–275** because scan 276 is still unresolved under the intended lexical-control workflow;
- C12 is **PARTIAL**, not complete.

## Verification safeguards

- live GitHub `main` is authoritative for durable project state;
- exact source identity remains 465 physical pages regardless of the current renderer's old 150-page window;
- supplied lexical controls are applied only to text actually present in the supplied file;
- missing supplied text is never silently filled;
- Phase 3 remains blocked while Phase 2 clearance is incomplete.

## Exact next activity

Recover/re-attach the missing word-for-word transcription for **physical scans 276–292 / printed pages 259–275** from the intended `part_012_pages_276-300` range, then complete C12. Preserve verified scans **285** and **292**. Do not begin C13, Phase 3, canonical assembly or translation before C12 closure.
