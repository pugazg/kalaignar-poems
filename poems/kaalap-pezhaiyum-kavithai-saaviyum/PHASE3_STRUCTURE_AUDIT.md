# Phase 3 structural audit — காலப் பேழையும் கவிதைச் சாவியும்

## Scope

Phase 3 begins only after completion of Phase 2 across all **306/306 physical scans**. The verified page records remain the textual authority layer; this audit concerns structure, completeness, title-witness handling, assembly readiness and Tamil final clearance.

## Activity 1 — physical scan ↔ printed-page reconciliation

**Status: COMPLETE.**

The exact reconciliation is recorded in `indexes/page-map.md`.

- scans **1–4**: unnumbered preliminaries;
- scans **5–299**: uninterrupted numbered-pagination block corresponding to printed pages **4–298**, with `printed page = physical scan - 1`;
- scans **300–305**: six unnumbered blank `குறிப்புகள்` pages;
- scan **306**: unnumbered image-only back cover.

All **306 physical scans** are structurally accounted for. All **58** contents start pages match their observed title scans by `observed title scan = contents start page + 1`.

## Activity 2 — 58-item boundary and within-item page-join continuity audit

**Status: COMPLETE — items 1–58 / 58 fully certified.**

Detailed evidence is recorded in `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

The final boundary/join iteration covered **scans 275–299** and completed the numbered-item sequence. Closing boundary **299→300** also passed, separating the completed first part from the `குறிப்புகள்` end matter.

### Certified ranges through completion

| Items | Physical scans | Result |
|---:|---|---|
| 1–9 | 10–49 | CERTIFIED |
| 10–13 | 50–67 | CERTIFIED |
| 14–18 | 68–98 | CERTIFIED |
| 19–24 | 99–123 | CERTIFIED |
| 25–30 | 124–147 | CERTIFIED |
| 31 | 148–151 | CERTIFIED; contents/title comma witness differs |
| 32 | 152–156 | CERTIFIED; contents/title wording witness differs |
| 33–36 | 157–178 | CERTIFIED |
| 37 | 179–185 | CERTIFIED; title witness differs and title page prints item number `36` |
| 38–39 | 186–194 | CERTIFIED |
| 40 | 195–199 | CERTIFIED; title page omits contents final `!` |
| 41–43 | 200–210 | CERTIFIED |
| 44 | 211–215 | CERTIFIED; title page omits contents comma after `தூணும்` |
| 45 | 216–219 | CERTIFIED |
| 46 | 220–225 | CERTIFIED; title page adds final `!` |
| 47 | 226–235 | CERTIFIED |
| 48 | 236–240 | CERTIFIED |
| 49 | 241–245 | CERTIFIED |
| 50 | 246–251 | CERTIFIED; title witness differs substantially |
| 51 | 252–256 | CERTIFIED |
| 52 | 257–262 | CERTIFIED |
| 53 | 263–270 | CERTIFIED |
| 54 | 271–276 | CERTIFIED; title joins `செரு` + `வென்றான்` |
| 55 | 277–284 | CERTIFIED |
| 56 | 285–288 | CERTIFIED |
| 57 | 289–295 | CERTIFIED |
| 58 | 296–299 | CERTIFIED; title joins `பகை வாள்` and adds final `!` |

### Final Activity-2 result

- numbered items certified: **58/58**;
- closing boundary from numbered sequence to end matter: **299→300 PASS**;
- dropped/duplicated text found: **none**;
- unresolved structural joins: **none**;
- Tamil transcription changes during final structural iteration: **none**.

## Activity 3 — title-witness reconciliation

**Status: COMPLETE — 14/14 documented discrepancy cases resolved as separate witnesses.**

The governing record is `PHASE3_TITLE_WITNESS_RECONCILIATION.md`.

Documented discrepant items:

**18, 22, 25, 26, 29, 31, 32, 37, 40, 44, 46, 50, 54 and 58.**

### Reconciliation rule

The source contains two legitimate title contexts:

- **contents witness** — retained exactly in the contents/index layer;
- **item-opening title-page witness** — retained exactly in the verified first-page record for the item.

No witness is silently corrected into the other.

For canonical Tamil assembly:

- the **title-page witness controls the assembled item's displayed title**;
- the title-page witness is the textual basis for any later **title-derived filename**, before only mechanical filesystem-safe escaping;
- the **contents witness remains preserved** as the contents/index witness and as alternate source metadata for discrepant items;
- no hybrid or editorially normalized third title may be created;
- stable item identity/order remains the certified contents sequence **1–58**.

### Item 37 anomaly

Scan **179** visibly prints item number **`36`**, although the certified contents sequence makes it item **37**.

Resolution:

- stable sequence identity remains **item 37**;
- printed number **36** remains explicitly preserved as a source anomaly;
- items 38–58 are not shifted;
- assembled title uses title-page wording `அன்பால் அவனை விலைகொள்ள முடியுமோ?`, while the contents witness `அன்பால் அவனை விலை கொள்ள முடியுமா?` remains separately preserved.

### Title-witness gate result

- discrepancy cases reconciled: **14/14**;
- contents witnesses retained: **14/14**;
- title-page witnesses retained: **14/14**;
- hybrid/normalized titles created: **none**;
- unresolved title-witness decisions: **none**;
- canonical assembly title authority: **title-page witness**;
- contents/index title authority: **contents witness**;
- item-37 source numbering anomaly: **preserved**.

The title-witness gate therefore **PASSES**.

## Durable assembly-readiness notes

- source-level abrupt transition **31→32** remains preserved rather than editorially repaired;
- source-level rhetorical transition **222→223** in item 46 remains preserved; there is no pagination or physical-scan gap;
- item 12 section metadata was previously unified across scans 58–63 without changing Tamil text;
- the complete title-witness discrepancy set is recorded in `PHASE3_TITLE_WITNESS_RECONCILIATION.md`;
- item 37's title page visibly prints item number **36** although it remains item 37 in the canonical sequence;
- source-sensitive Phase-2 readings remain unchanged; Phase 3 has not normalized source spelling, punctuation, word division or lexical forms.

## Remaining Phase-3 activities

1. **canonical Tamil assembly** — assemble **58 separate item files** from verified page records, preserving verified lineation, item order, source separators/notes and the title-authority decisions in `PHASE3_TITLE_WITNESS_RECONCILIATION.md`;
2. perform **assembly/source-completeness review** against the verified page layer and controlling scan structure;
3. grant **Tamil final clearance** only after the assembly review passes.

Phase 4 translation remains blocked until Tamil final clearance.

## Exact next activity

Begin **canonical Tamil assembly** for the 58 certified items.

Assembly must be generated from the verified `pages/NNNN.md` records in certified physical-page order. Each item remains a separate work unit. For the 14 discrepant titles, use the **title-page witness** as the assembled title and filename basis while retaining the **contents witness** as alternate source metadata. Preserve item 37's printed `36` only as a source anomaly; its stable sequence identity remains item 37.

Do **not** begin Phase 4 translation.