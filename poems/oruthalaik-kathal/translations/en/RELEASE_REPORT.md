# Phase 4 Release Report — One-Sided Love

Work: **ஒருதலைக் காதல்**  
English title: **One-Sided Love**  
Review date: **2026-09-05**

Controlling source: `TVA_BOK_0065554_ஒருதலைக்_காதல்.pdf` — **101 scans**, **200,800,237 bytes**, SHA-256 `a9b0ff45820155a4775074f630e791a8304073a90e5e36ab793bdf702ec33184`.

Tamil final-clearance checkpoint: `0c6b3d19625a9478441f0f654584d8343163ba37`.  
Live `main` reviewed at the start of this release gate: `059d138cf1b9a8e5501e1417f2ce62197ea81c3e` (tree `2a6b6a9c98be6a8a79ba24ee51d28349c543c920`).

## Final result

**PHASE 4 FINAL SOURCE-COVERAGE / RELEASE-INTEGRITY REVIEW: PASS**

**PHASE 4 COMPLETE — RELEASE-CLEARED**

Unresolved release issues: **0**.

## 1. Reviewed translation units

Result: **PASS**.

All six governing batch records remain present and reviewed PASS:

| Batch | Sections | Physical scans | Result |
|---:|---:|---:|---|
| 01 | 01–02 | 6–20 | PASS |
| 02 | 03–04 | 21–38 | PASS |
| 03 | 05–06 | 39–55 | PASS |
| 04 | 07–08 | 56–73 | PASS |
| 05 | 09 | 74–82 | PASS |
| 06 | 10–11 | 83–100 | PASS |

Current reviewed English section blobs remain exactly those recorded by `SOURCE_MAP.md`:

| Section | Git blob |
|---:|---|
| 01 | `3355c03411984ad763b8d127be82149a50edb403` |
| 02 | `8409bcfe9b8edc9b5dd31611b6b3484a3ee9ac0f` |
| 03 | `1442f9d6c551e4d96e1c29a8da61ce5cbfdb4191` |
| 04 | `36a620c42bc944855d091ea16dd6fd4d2fffe993` |
| 05 | `e353ce248c7837aaa9df0822be3306016e3f8f7b` |
| 06 | `ab396e298de1f57a3fac662f1c1b66af62ffa077` |
| 07 | `3a74cb3fb65a2f160a03c56643622eb92c585206` |
| 08 | `13862162e0934907b2f854bbd52b37ba0252564f` |
| 09 | `78dba20abd4a65177d950ac7e7b2c77f97b4c70e` |
| 10 | `c24bc7038116ceb8adb9031da74d2e2fade1dba4` |
| 11 | `b76b515baab32cb8b179d89aa6bcee940e8c1d3c` |

Thus all **11/11** reviewed standalone English sections remain synchronized with the post-batch review checkpoint.

## 2. Reader-facing assembly integrity

Result: **PASS**.

Current reader-facing assembly:

- file: `oruthalaik-kathal-en.md`;
- Git blob: `012a3bdaf330bb9b2db66d229c0be2a87d3f46f6`;
- size: **89,457 bytes**;
- line count: **3,004**;
- source sections: **11/11 in source order**.

The current blob is identical to the blob independently certified by `EDITORIAL_CONSISTENCY_REVIEW.md`. Therefore the final gate revalidates, without introducing a new assembly edit, the certified provenance structure:

- physical scan markers **6–100 = 95/95 exactly once**;
- composition **84 text-bearing + 11 illustration-only scans**;
- no missing or duplicate source-section ranges;
- front/back exclusions **1–5 and 101** remain outside the poem-body translation.

## 3. Illustration and section-boundary witnesses

Result: **PASS**.

All eleven full-page illustrations remain neutral provenance markers, with no invented captions:

`8, 16, 22, 32, 40, 48, 58, 66, 76, 84, 94`.

All ten numbered-section closing three-diamond witnesses remain represented:

`13, 20, 30, 38, 45, 55, 63, 73, 82, 92`.

Source-internal separators remain internal rather than being promoted to false section endings, including the certified transitions on scans **7, 87 and 90**.

## 4. Quotation / explanation structure and final close

Result: **PASS**.

Classical quotations remain visibly distinct from their attributions and from separate **Source explanation** blocks. The source-distinct literary layers remain intact, including *Purananuru*, *Natrinai*, *Akananuru* and *Kuruntokai* witnesses.

The final scan-100 structure remains:

*Akananuru* 252 quotation → attribution → **Source explanation** → **(The End)** → final `♦ ♦ ♦`.

Direct visual inspection of the controlling source during this final gate reconfirmed scan **100 / printed page 95** contains the source explanation, printed `(முற்றும்)` and the final three diamonds. Scan **101** is the back cover and contains no continuation of the poem body.

## 5. Title, names, terms and refrain continuity

Result: **PASS**.

The final assembly remains synchronized with the established Phase-4 locks, including:

- **One-Sided Love**;
- **Source explanation**;
- **Kavarpentu**;
- **war-sword / flower-petal**;
- **Karantai battle**;
- ***Natrinai***, ***Akananuru*** and ***Kuruntokai***;
- **Palver Katti**;
- narrative **Uraiyur** versus quotation-form **Uranthai**;
- **Attani council hall / Attani hall** and source-controlled **day-court**;
- source-distinct `பாணி` versus `ஆளி` / **yali**;
- scan-92 **fire of cosmic destruction**;
- **anicham flower**;
- source `(முற்றும்)` represented structurally as **(The End)**.

The post-batch English-only correction is synchronized: section 3 and the reader-facing assembly both use **Karantai battle**, not `karantai battle`. Tamil remains unchanged.

## 6. Reader-facing cleanliness

Result: **PASS**.

The reader-facing assembly contains no standalone section YAML and no batch-review control fields. The explicit `## Section 1` … `## Section 11` headings are reader-navigation labels; scan-page comments remain provenance markers.

## 7. Tamil final-clearance protection

Result: **PASS**.

Git comparison from Tamil final-clearance checkpoint `0c6b3d19625a9478441f0f654584d8343163ba37` to the live `main` reviewed by this gate shows:

- changed files under `poems/oruthalaik-kathal/pages/`: **0**;
- changed files under `poems/oruthalaik-kathal/sections/`: **0**.

No English editorial preference reopened the final-cleared Tamil page or canonical layer. Tamil therefore remains **FINAL-CLEARED — 101/101 verified pages, 11/11 canonical sections, 95/95 main-work scans, unresolved Tamil/source issues 0**.

`poems/kalaignarin-kavithaigal/` remains RELEASE-CLEARED and was not modified by this activity.

## Release decision

All required Phase-4 final checks pass. Source coverage, translation-unit synchronization, structural witnesses, reader-facing assembly integrity, terminology continuity, source exclusions and Tamil-layer protection all reconcile with **0 unresolved release issues**.

**Release clearance is granted: PHASE 4 COMPLETE — RELEASE-CLEARED.**

No further Phase-4 production activity is pending for this work. Any future textual change must be justified by genuine source evidence and must follow the repository reopening/audit policy rather than silently changing a final-cleared or release-cleared layer.
