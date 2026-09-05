# Phase 4 Release Report — Nehru, the Noble Leader

Work: **குணநாயகர் நேரு**  
English title: **Nehru, the Noble Leader**  
Review date: **2026-09-05**

Controlling source: `TVA_BOK_0065713_குணநாயகர்_நேரு.pdf` — **10 scans**, **27,006,676 bytes**, SHA-256 `efc8efb14d45e8cb7cbf2dc232732b7a54e778c1fd1957ad64e198072829e07c`.

Tamil final-clearance checkpoint: `80bc2b30dbe7630a68ff01df4ad782fa8e6aa962`.  
Live `main` reviewed at the start of this T4 gate: `1e01ebe257c446b5898ae7ff6ee4a0c37bf1781c`.

## Final result

**PHASE 4 FINAL SOURCE-COVERAGE / RELEASE-INTEGRITY REVIEW: PASS**

**PHASE 4 COMPLETE — RELEASE-CLEARED**

Unresolved release issues: **0**.

## 1. Translation-unit integrity

Result: **PASS**.

The only canonical Tamil unit and its reviewed English translation remain synchronized:

| Unit | Tamil source | Tamil blob | Reviewed English | English blob | Scans |
|---:|---|---|---|---|---:|
| 01 | `../../sections/01.md` | `56ec1cf593d20c69f50a7b4bb7b69529bcc413e6` | `sections/01.md` | `499f9ebf05d78df10143cd6161ebf0f8501750cc` | 3–7 |

`sections/01.md` remains `reviewed-pass`; T2 unresolved English translation issues remain **0**.

## 2. Reader-facing assembly integrity

Result: **PASS**.

Current reader-facing assembly:

- file: `gunanayagar-nehru-en.md`;
- Git blob: `c11b7d11ed3be642cca734b0bdcb16ae1f5b1c0e`;
- size: **8,454 bytes**;
- reviewed sections represented: **1/1**;
- canonical scan markers: **3, 4, 5, 6, 7 — 5/5 exactly once**;
- missing / duplicate markers: **0 / 0**.

The assembly blob is identical to the blob independently certified by `EDITORIAL_CONSISTENCY_REVIEW.md` (T3 PASS). No new English body edit was introduced in T4.

## 3. Source-boundary / exclusion integrity

Result: **PASS**.

The certified Tamil verse scope remains scans **3–7** only. The reader-facing assembly contains no provenance marker for scans **1, 2, 8, 9 or 10**.

The following non-body/source-witness material remains excluded from translated verse:

- scan 1 cover;
- scan 2 `பதிப்புரை`;
- scan-7 performance note dated `14.11.1970`;
- scans 8–9 source-supplied English witness **BEAUTY ROSE WEPT** / `Translation: Dr. Krishna Srinivas`;
- witness-specific **Maha Meru** wording;
- scan 10 uncaptained photograph/back matter.

Direct current-assembly checks found none of `14.11.1970`, `BEAUTY ROSE WEPT`, `Dr. Krishna Srinivas`, or `Maha Meru` in the reader-facing body.

## 4. Title, byline, names and terminology

Result: **PASS**.

The release assembly preserves the reviewed controls:

- `குணநாயகர் நேரு` → **Nehru, the Noble Leader**;
- source attribution `முதல்வர் கலைஞர்` → **Chief Minister Kalaignar**;
- catalog identity `கலைஞர் மு. கருணாநிதி` is not substituted into the source byline;
- `மல்லிகை` → **Jasmine**;
- `செண்பகம்` → **Champak**;
- `சாமந்தி` → **Samanthi**;
- `முல்லை` → **Mullai**;
- `ரோஜா` → **Rose**;
- `கர்த்தபம்` → **donkey**;
- `நேரு மாமா` → **Uncle Nehru**;
- `கலிங்கத்துப் பரணி` → ***Kalingattu Parani***;
- `பூங்குன்றனார்` → **Pungundranar** in the reviewed context.

Historical-witness divergences remain comparison evidence only. Deliberate witness-driven wording adoptions remain **0**.

## 5. Rhetoric, quotation and wordplay integrity

Result: **PASS**.

The T2/T3-reviewed treatment remains unchanged in the release assembly:

- `நேர்` / `நேரு` is represented semantically without invented English rhyme;
- `காலக் குரங்கின் கை ‘மாலை’` remains the **monkey-hand of Time / ‘garland’ in its grasp** image;
- the scan-6/7 `சீனக் கள்ளி` / `விடி வெள்ளி` / `பகை கிள்ளி` chain remains structurally continuous across the scan marker;
- `யாதும் ஊரே யாவரும் கேளிர்` remains visibly quoted;
- the *Kalingattu Parani* passage remains a separate block quotation;
- the Puduvai-poet stanza remains a separate block quotation;
- the closing `ஜனநாயகம் / தனிநாயகம் / பணநாயகம் / குணநாயகர்` progression remains **democracy / autocracy / rule of money / Noble Leader**.

## 6. Historical English witness boundary

Result: **PASS**.

Scans **8–9**, headed **BEAUTY ROSE WEPT** and credited to **Dr. Krishna Srinivas**, remain a secondary historical witness only. T2 documented their selective/condensed nature and material divergences from the Tamil source.

T4 confirms:

- witness heading used as repository title: **0**;
- witness omissions imported into repository coverage: **0**;
- witness-specific `Maha Meru` imported: **0**;
- witness overrides of Tamil: **0**;
- deliberate witness-driven wording adoptions: **0**.

## 7. Tamil final-clearance protection

Result: **PASS**.

Git comparison from Tamil final-clearance checkpoint `80bc2b30dbe7630a68ff01df4ad782fa8e6aa962` to the live `main` reviewed at the start of T4 shows:

- changed files under `poems/gunanayagar-nehru/pages/`: **0**;
- changed files under the final-cleared Tamil `poems/gunanayagar-nehru/sections/`: **0**.

Tamil therefore remains **FINAL-CLEARED — 10/10 verified page records, 1/1 canonical section, scans 3–7 exactly once, unresolved Tamil/source issues 0**.

`poems/oruthalaik-kathal/` and `poems/kalaignarin-kavithaigal/` remain RELEASE-CLEARED and were not modified by this T4 activity.

## Release decision

All required final checks pass. Translation-unit synchronization, reader-facing assembly integrity, canonical source coverage, exclusions, title/byline/terminology controls, quotation and wordplay treatment, historical-witness boundaries, and Tamil-layer protection reconcile with **0 unresolved release issues**.

**Release clearance is granted: PHASE 4 COMPLETE — RELEASE-CLEARED.**

No further Phase-4 production activity is pending for **குணநாயகர் நேரு**. Any future textual change must be supported by genuine source evidence and follow the repository reopening/audit policy rather than silently altering a final-cleared or release-cleared layer.
