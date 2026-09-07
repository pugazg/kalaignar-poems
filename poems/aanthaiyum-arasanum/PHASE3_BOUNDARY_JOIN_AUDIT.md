# Phase 3 Gate 2 — boundary / page-join audit — ஆந்தையும் அரசனும்

Date: **2026-09-07**.

Controlling source: `TVA_PRL_0001631_முரசொலி_ பொங்கல் மலர்_ 1965.pdf` — **102 physical pages / 381,558,891 bytes / SHA-256 `523a038dcd391f5cbe48f564d2ecac566fd0065066e05d29fc5b738aa4964819`**.

Active work range: physical scans **18–25**.

Prerequisites:

- Phase 1: **COMPLETE — 8/8 lexically complete**;
- Phase 2: **PASS — 8/8 verified / 0 unresolved**;
- Phase 3 Gate 1: **PASS — pagination reconciled**.

## Gate rule

This gate certifies the physical opening, every internal scan join, source-visible separator/quotation/poetic-line continuity, and the physical closing boundary. It does not rewrite verified lexical text or smooth source punctuation.

At assembly time a page boundary must not create or delete a stanza, separator, quotation mark, punctuation mark, or continuation line.

## Boundary results

| Boundary | Result | Source-critical finding |
|---|---|---|
| scan 17 → 18 opening | **PASS** | scan 17 is unrelated prose; scan 18 is the decorated poem opening with direct title `ஆந்தையும் அரசனும்!` and author `மு.கருணாநிதி`; no text is carried into the poem from scan 17 |
| 18 → 19 | **PASS — direct poetic continuation** | scan 18 ends `வாழிய செந்தமிழ் என்றே மன்னர்`; scan 19 begins `வாளை உருவிக் காத்தனர் முன்னே—`; the poetic sentence continues across the physical page break with no inserted heading/separator |
| 19 → 20 | **PASS** | scan 19 closes `தக்கோர் வாழ்ந்தனர் தணியாநட்புடன்!`; scan 20 begins `கருவூர் சதுக்கப் பூதநாதர்`; no source separator or punctuation needs to be invented at the page boundary |
| 20 → 21 | **PASS** | scan 20 closes `கற்புடை நட்பு மிளிர்ந்தது நன்று.`; scan 21 begins `கண்டு கேட்டுண்டுயிர்த்து—பூச்`; preserve the physical page transition without adding a separator or normalizing the verse flow |
| 21 → 22 | **PASS — new quotation begins on scan 22** | scan 21 closes `...இருதரப்பும் இறைஞ்சி / நின்றார்.`; scan 22 begins the source-visible opening quotation `“வண்டாடும் பூப்போன்ற மாதரிடம்`; the quotation is not carried from scan 21 and must remain attached to scan 22 |
| 22 → 23 | **PASS — quotation carry-over** | scan 22 opens `“இமிழ் கடல் வேலித் தமிழ் நிலந்தன்னில்...` and ends `கமழ்ந்திடும் வெற்றி, களிப்பைத் தருமோ?` without closing the quotation; scan 23 continues `கொற்றவனே!...` and closes the same quotation at `உண்மையிது உணர்க!”`; no quote mark may be inserted at the physical join |
| 23 → 24 | **PASS — sentence carry-over** | scan 23 ends the quoted question `“எப்போதும் உளமிருந்த பிசிராந்தை / இப்போது வருவாரா காண்பதற்கு?”`; scan 24 begins `எனக் கேட்டார் அருகிருந்தோர்.`; the speech tag continues the sentence across the page break, so no separator belongs between them |
| 24 → 25 | **PASS — separator-owned transition** | scan 24 closes `ஊமையானார் உழுவலன்பர்.` and contains the source-visible separator before the next unit; scan 25 begins `புலவர் பொத்தியாரும் வந்துவிட்டார்`; retain the separator once on scan 24 and do not duplicate or move it to scan 25 |
| scan 25 → 26 closing | **PASS** | scan 25 closes the poem with `ஆண்டுகள் கோடி வாழ்கின்றாரே!` followed by the source-visible decorative closing ornament; scan 26 is an unrelated cartoon, so no poem text continues beyond scan 25 |

## Join accounting

- opening boundary: **1/1 PASS**;
- internal joins: **7/7 PASS**;
- quotation carry-over joins: **1 identified / 1 PASS (22→23)**;
- sentence/attribution carry-over joins: **2 identified / 2 PASS (18→19 and 23→24)**;
- separator-owned transition joins: **1 identified / 1 PASS (24→25)**;
- closing boundary: **1/1 PASS**;
- missing physical scans: **0**;
- duplicated physical scans: **0**;
- page-layer corrections required by Gate 2: **0**;
- unresolved boundary holds: **0**.

## Gate result

**PHASE 3 GATE 2 PASS — OPENING 1/1 / INTERNAL JOINS 7/7 / CLOSING 1/1 / 0 UNRESOLVED / 0 PAGE-TEXT CHANGES.**

All eight page records remain `verified`. Gate 2 changes only the durable structural certification state.

Exact next activity: **Phase 3 Gate 3 — title-witness reconciliation**. Reconcile the bibliographic title `ஆந்தையும் அரசனும்` with the direct decorated scan-18 witness `ஆந்தையும் அரசனும்!`, record the assembly authority explicitly, and do not create a hybrid/normalized title. Canonical Tamil assembly remains blocked until Gate 3 passes.
