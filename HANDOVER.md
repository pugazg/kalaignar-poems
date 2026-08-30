# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Authority rule

**Treat live GitHub `main` as authoritative.** The controlling source scan remains the highest textual authority for Tamil wording unless a documented user instruction establishes another lexical/editorial control. An older chat SHA, count, boundary or next-step instruction is only a checkpoint; if live `main` has advanced, preserve newer work.

## Mandatory startup for every continuation

Before changing this repository in a fresh chat:

1. fetch live `main` and note current HEAD;
2. read `POEM_PROCESSING_GUIDE.md` completely;
3. read `TRANSCRIPTION_PHASE_PLAN.md` completely;
4. read root `README.md` and `NEXT_CHAT_PROMPT.md` completely;
5. read `poems/kalaignarin-kavithaigal/README.md`, `SOURCE_INTAKE.md`, `metadata/source.md`, `indexes/page-map.md`, and `audit.md` completely;
6. inspect the current boundary record, especially `poems/kalaignarin-kavithaigal/pages/0300.md`;
7. use the controlling PDF directly whenever transcription/verification requires source evidence;
8. never commit the source PDF;
9. synchronize status-bearing files at each completed batch;
10. when the user says **“Proceed with next activity”**, execute the exact next routine operation recorded in live state without asking them to choose.

---

# CURRENT ACTIVE WORK — கலைஞரின் கவிதைகள்

Work directory: `poems/kalaignarin-kavithaigal/`  
Author: **கலைஞர் மு. கருணாநிதி**  
Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

## Exact controlling-source identity

- physical PDF pages: **465**;
- file size: **486,369,088 bytes**;
- SHA-256: **`19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`**;
- printed title: **கலைஞரின் கவிதைகள்**;
- author: **கலைஞர் மு. கருணாநிதி**;
- publisher: **பாரதி பதிப்பகம்**;
- edition: **fourth edition, March 1995**.

### Critical renderer warning

An earlier interface exposed only pages 1–150 and reported `total_pages: 150`. That was not the PDF's actual length. Exact-byte inspection established **465 physical pages**, and direct source processing has now reached scan **300**. Never replace the durable 465-page count with a renderer/window count.

## Durable Phase-1 state at handoff

**PHASE 1 TRANSCRIPTION IN PROGRESS — physical scans 1–300 / 465 recorded.**

- Phase 1 page records: **300/465**;
- files created: `pages/0001.md` through `pages/0300.md`;
- cumulative status: **10 `partial`, 290 `needs-review`, 0 `verified`**;
- completed batches: **01–12**;
- Phase 2 source-critical verification: **not started**;
- Phase 3 structure/assembly/final clearance: **not started**;
- English translation/release: **blocked until Tamil final clearance**.

## Durable source/item boundaries through scan 300

- scans 1–17 — cover/title/imprint/front matter/contents;
- `இதயத்தைத் தந்திடு அண்ணா` — closes 31;
- `தென்னவன் காதை` — 34–42;
- `இந்திரஜித்` — 43–54;
- `இரணியன்` — 55–61;
- `வாளி மன்னன்` — 62–69;
- `விடுதலை வீரர்கள்` — 72–79;
- `ஐம்புலன்` — 80–89;
- `பிலவங்க ஆண்டு` — 90–100;
- `காதலா - வீரமா?` — 101–115;
- `அருமறையில் அறுவர்` — 116–127;
- `புதிய பாதை` — 128–137;
- `உடைமைகள் பத்து` — 138–143;
- `நீர்க் குடும்பம்` — 144–154;
- `பாரதிதாசன்` — 155–169;
- `பாரதியார்` — 170–174;
- `பொங்கல் திருநாள்` — 175–184;
- `வாழ்வெனும் பாதையில்` — 185–196;
- `கணக்கு` — 197–204;
- `நேரு கண்ட ஜனநாயகம்` — 205–215;
- `நன்றி, நன்றி!` — 216–217;
- `வெள்ளி விழா` — 218–226;
- `அண்ணன் இருக்கின்றார்` — 227–229;
- `அண்ணன் ஒரு கவியரங்கம்` — 230–236 + 238, closes 238; scan 237 is physically interposed as the next-item title leaf;
- `தமிழ் வளர வழிநடைப் பயணம்` — title leaf 237, body 239–244, closes 244;
- `வையம் தழைக்க` — 245–253;
- `தந்தை பெரியார்` — 254–260;
- `அகத்துறைப் படைப்புகள்` — 261–266;
- `பொங்கல் விழா` — 267–272;
- `சிலப்பதிகார விருந்து` — **273–285**, closes scan **285 / printed page 268**;
- `அண்ணா வழியில்` — **286–292**, closes scan **292 / printed page 275**;
- `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்!` — **293–296**, closes scan **296 / printed page 279**;
- `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை` — opens scan **297 / printed page 280** and remains open beyond scan **300 / printed page 283**.

## Batch-12 evidence

- scan 276 / printed 259 continues `சிலப்பதிகார விருந்து` from the prior batch;
- scan 285 / printed 268 closes it;
- scan 286 / printed 269 opens `அண்ணா வழியில்`; scan 292 / printed 275 closes it;
- scan 293 / printed 276 opens `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்!`; scan 296 / printed 279 closes it;
- scan 297 / printed 280 opens `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை`;
- scan 300 / printed 283 remains mid-item, so the next scan must continue it.

## Durable blur / difficult-reading rule

During Phase 1 transcribe only what the controlling scan safely supports. Use explicit `⟦…⟧` editorial markers for genuinely unresolved spans; these markers are not source text. Do not reconstruct blur from OCR, memory, grammar, metre, rhyme, historical context, likely wording, or another edition. OCR may be used only for navigation/typing assistance. Do not silently normalize spelling, punctuation, sandhi, names, dates, numbers or lineation. Record only visibly printed page numerals. Phase-1 pages remain `needs-review` until independent Phase-2 review.

## Cross-witness safeguard

This anthology includes works also archived from separate source witnesses, including `இதயத்தைத் தந்திடு அண்ணா!` and `தென்னவன் காதை`. Do not copy those transcriptions into this anthology. The existing user-directed exclusion applicable to `தென்னவன் காதை` remains in force.

## Other repository work states to preserve

- `காலப் பேழையும் கவிதைச் சாவியும்` — Tamil FINAL-CLEARED; English RELEASE-CLEARED; 58/58 items;
- `தென்னவன் காதை` — Tamil FINAL-CLEARED; English translation paused;
- `இதயத்தைத் தந்திடு அண்ணா` — Tamil COMPLETE; English RELEASE-COMPLETE.

## EXACT NEXT ACTIVITY

Execute **Phase 1 Batch 13 — physical scans 301–325**.

Create `poems/kalaignarin-kavithaigal/pages/0301.md` through `pages/0325.md`, continuing directly from the unfinished `முப்பெரும் விழாக் கவியரங்கம் தலைமைக் கவிதை` at scan 300. Inspect every scan directly from the exact 465-page controlling PDF, preserve physical boundaries and visible structure, and retain the conservative blur policy.

At Batch-13 completion synchronize `audit.md`, `indexes/page-map.md`, active/root READMEs, `SOURCE_INTAKE.md`, `metadata/source.md`, `TRANSCRIPTION_PHASE_PLAN.md`, `HANDOVER.md`, and `NEXT_CHAT_PROMPT.md`. Do **not** begin Phase 2, Phase 3, canonical assembly or translation in the same activity.