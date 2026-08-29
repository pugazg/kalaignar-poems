# Phase 3 structural audit — காலப் பேழையும் கவிதைச் சாவியும்

## Scope

Phase 3 begins only after completion of Phase 2 across all **306/306 physical scans**. The verified page records remain the textual authority layer; this audit concerns structure, completeness, joins and assembly readiness.

## Activity 1 — physical scan ↔ printed-page reconciliation

**Status: COMPLETE.**

The exact reconciliation is recorded in `indexes/page-map.md`.

- scans **1–4**: unnumbered preliminaries;
- scans **5–299**: uninterrupted numbered-pagination block corresponding to printed pages **4–298**, with `printed page = physical scan - 1`;
- scans **300–305**: six unnumbered blank `குறிப்புகள்` pages;
- scan **306**: unnumbered image-only back cover.

All **306 physical scans** are structurally accounted for. All **58** contents start pages match their observed title scans by `observed title scan = contents start page + 1`.

## Activity 2 — 58-item boundary and within-item page-join continuity audit

**Status: IN PROGRESS — items 1–13 / 58 fully certified; item 14 audited through scan 74.**

Detailed evidence is recorded in `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

### Iteration size

Routine Phase-3 continuation is now performed in **25-physical-scan iterations**. The completed iteration covered **scans 50–74**. If an iteration ends inside an item, that item remains partial until the next iteration completes its remaining joins and closing boundary.

| Item | Title | Range | Internal joins | Result |
|---:|---|---|---:|---|
| 1 | `பொது உலகம்` | scans 10–11 / pp. 9–10 | 1/1 | PASS |
| 2 | `படிமுறை வளர்ச்சி` | scans 12–15 / pp. 11–14 | 3/3 | PASS |
| 3 | `‘காந்தக்கல்’ கதையொன்று!` | scans 16–19 / pp. 15–18 | 3/3 | PASS |
| 4 | `அன்றிருந்த கற்காலம் - இனி அமையாவிடின் நற்காலம்!` | scans 20–24 / pp. 19–23 | 4/4 | PASS |
| 5 | `தங்க மனம் வேண்டும்; அது தந்திடும் அன்பு வேண்டும்!` | scans 25–28 / pp. 24–27 | 3/3 | PASS |
| 6 | `கத்தி பகைவுடையது; இரத்தம் நாம் தருவது!` | scans 29–34 / pp. 28–33 | 5/5 | PASS |
| 7 | `வரலாற்றுக் காலத்தின் கோலம்!` | scans 35–39 / pp. 34–38 | 4/4 | PASS |
| 8 | `நெற்றி வியர்வை உதிர; நெஞ்செலும்பு ஒடிய!` | scans 40–43 / pp. 39–42 | 3/3 | PASS |
| 9 | `உரையாடல் உணர்த்திடும் உண்மை என்ன?` | scans 44–49 / pp. 43–48 | 5/5 | PASS |
| 10 | `பழந்தமிழர் பன்னாட்டுத் தொடர்பு!` | scans 50–53 / pp. 49–52 | 3/3 | PASS |
| 11 | `ஆங்காங்கு அடையாள முத்திரைகள்!` | scans 54–57 / pp. 53–56 | 3/3 | PASS |
| 12 | `வரலாற்றுப் பூங்காவில் வள்ளித் திருமணம்!` | scans 58–63 / pp. 57–62 | 5/5 | PASS |
| 13 | `காரவேலன் கண்டு நடுங்கிய கட்டுக்குலையாக் கூட்டணி!` | scans 64–67 / pp. 63–66 | 3/3 | PASS |
| 14 | `கனக விஜயர் கல் சுமந்த வரலாறு!` | scans 68–77 / pp. 67–76 | 6/9 audited through scan 74 | PARTIAL |

### Scans 50–74 result

- items **10–13** passed their opening boundaries, every internal join, and closing boundaries;
- item **14** passed its opening boundary and joins **68→69, 69→70, 70→71, 71→72, 72→73, 73→74**;
- scan 74 ends mid-sentence at `பறி போகலாம்! ஆனால் கனல்`, so item 14 is intentionally left open for the next iteration;
- no dropped or duplicated source text was detected;
- no new contents/title-page witness discrepancy was found in items 10–14;
- source-level wording, punctuation, dialogue structure and physical line splits were preserved.

### Assembly-readiness metadata correction

Item 12 contained one non-textual structural inconsistency: scan 58 used the title-derived section id `item-12-varalattrup-poongaavil-vallith-thirumanam`, while scans 59–63 used `item-12-valli-thirumanam`. The `section` front matter on scans **59–63** was aligned to the scan-58 id so one source item cannot be split during later assembly. **No source transcription was changed.**

## Remaining Phase-3 activities

1. continue the **58-item boundary certification and within-item page-join continuity audit** in 25-scan iterations;
2. **title-witness reconciliation record** — preserve contents and title-page variants as witnesses; do not silently normalize them;
3. **canonical Tamil assembly** — only after structural and join audits pass;
4. **assembly/source-completeness review and Tamil final clearance**.

## Exact next activity

Process physical scans **75–99** as the next 25-scan iteration, beginning with the pending item-14 join **74→75**. Canonical Tamil assembly remains blocked until the full boundary/join audit is complete.