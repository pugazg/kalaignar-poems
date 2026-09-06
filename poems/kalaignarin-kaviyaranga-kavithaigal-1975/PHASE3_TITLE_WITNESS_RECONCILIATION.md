# Phase 3 Title-Witness Reconciliation — Gate 3

Work: **கலைஞரின் கவியரங்கக் கவிதைகள் (1975) — new-item-only Kalaignar intake**  
Controlling source: `TVA_BOK_0064169_கலைஞரின்_கவியரங்கக்_கவிதைகள்.pdf`

- physical PDF scans: **84**;
- file size: **93,307,011 bytes**;
- SHA-256: `d9b70fd65f913c2c4377c25675e115555987bb9d9a4c22681b13ebae98afd168`.

Prerequisites:

- `PHASE3_STRUCTURE_AUDIT.md` — **Gate 1 COMPLETE / PASS**;
- `PHASE3_BOUNDARY_JOIN_AUDIT.md` — **Gate 2 COMPLETE / PASS**.

## Gate 3 scope

This record performs **Phase 3 Gate 3 only: title-witness reconciliation** for the three genuinely new Kalaignar blocks:

- NEW ITEM 01 — scans **46–57**;
- NEW ITEM 02 — scans **58–65**;
- NEW ITEM 04 — scans **67–68**.

The task is to distinguish direct item headings from event/provenance prose, contextual editorial labels and publication-level titles; preserve every applicable witness exactly; and record the title authority that later canonical assembly must use.

This gate does **not** alter verified page text, assemble canonical Tamil, perform final completeness review, grant Tamil clearance or begin translation.

## Publication-level witness inventory

The publication preliminaries do **not** supply an item-level contents witness for these three active items.

- scan 1 cover: `கவியரங்கக் கவிதைகள்`;
- scan 2 title page: `கலைஞரின் / கவியரங்கக் கவிதைகள்`;
- scans 3–8 are edition/price detail, handwriting, preface, bleed-through/verso, publisher note and bleed-through/verso records;
- scan 9 begins the first poem witness.

Therefore there is **no printed contents-page title witness** to reconcile against Items 01, 02 or 04. The cover/title-page wording is publication-level metadata only and must not be promoted into an item title.

## NEW ITEM 01 — scans 46–57

### Direct item-heading witness — scan 46

```text
புரட்சிக் கவிஞர் பாட்டரங்கில்
முதல்வர் கலைஞர் தலைமைக் கவிதை
```

### Event/provenance witness — scan 46

```text
29-4-71 புரட்சிக் கவிஞர் பாரதிதாசன் அவர்களின்
80-வது பிறந்தநாளை ஒட்டி நடைபெற்ற
கவியரங்கு

இடம்:— புதுவை
```

### Reconciliation / assembly authority

**RESOLVED / PASS.** There is no competing contents or alternate title-heading witness. The dated Bharathidasan-birthday wording and `இடம்:— புதுவை` are event/provenance text, not a replacement title.

Later canonical assembly must use the **exact two-line direct heading block from scan 46** as the title authority. It must not synthesize a new one-line title by inserting a dash, colon or other punctuation between the two printed lines.

## NEW ITEM 02 — scans 58–65

### Direct item-heading witness — scan 58

```text
பறம்புமலைப் பாரி வள்ளல் விழாக்
கவியரங்கில்
முதல்வர் கலைஞரின் தலைமைக் கவிதை
```

### Event/provenance witness — scan 58

```text
பறம்பு மலையில் 5—5—71 அன்று நடந்த பாரி வள்ளல்
விழாவை யொட்டிய கவியரங்கில் முதலமைச்சர் கலைஞர் கருணாநிதி
அவர்கள் கவியரங்கத்திற்குத் தலைமை தாங்கிப் பாடிய தலைமைக்
கவிதை.
```

### Reconciliation / assembly authority

**RESOLVED / PASS.** The explanatory prose is event/provenance text and is not an alternate item title.

A prior repository convenience label compressed the source heading to `பறம்புமலைப் பாரி வள்ளல் விழாக் கவியரங்கு`. That form is **not** the controlling source heading: the scan visibly prints `பறம்புமலைப் பாரி வள்ளல் விழாக் / கவியரங்கில்` before `முதல்வர் கலைஞரின் தலைமைக் கவிதை`. Status/intake labels are corrected in this Gate-3 commit; verified page text is unchanged.

Later canonical assembly must use the **exact three-line direct heading block from scan 58** as title authority. It must not normalize `கவியரங்கில்` to `கவியரங்கு`, collapse the heading into a synthetic one-line title, or import punctuation absent from the source.

## Scan 66 / NEW ITEM 04 title relationship

Scan 66 is non-Kalaignar Rajaji context and remains excluded from Kalaignar canonical text. Its closing editorial note says:

```text
[இக் கவிதைக்கு முதல்வர் செப்டம்பர் 17-ல் ஈரோட்டில்
பெரியார் சிலை திறப்பு விழாவில்—மறுப்புக் கவிதை பாடினார்]
```

This gives a contextual/editorial descriptor **`மறுப்புக் கவிதை`** for the response that follows.

## NEW ITEM 04 — scans 67–68

### Direct item-heading witness — scan 67

```text
“முதல்வர் கலைஞரின் பதில் கவிதை”
```

### Event/provenance witness — scan 67

```text
செப்டம்பர் 17-ல் ஈரோட்டில் பெரியார் சிலை திறப்பு
விழாவில் பாடியது.
```

### Body-reference note

The poem body begins with `“சாராய சகாப்த” மென்று ஓர் கவிதை`. This is body text referring to the Rajaji controversy; it is **not** an item-title witness and must not be promoted to the canonical title.

### Reconciliation / assembly authority

**RESOLVED / PASS.** The source contains a real terminology difference:

- scan 66 editorial/context note: `மறுப்புக் கவிதை`;
- scan 67 direct item heading: `“முதல்வர் கலைஞரின் பதில் கவிதை”`.

The **direct item heading on scan 67 controls the canonical title**. Scan 66's `மறுப்புக் கவிதை` remains preserved as contextual provenance only. Later assembly must not substitute `மறுப்புக் கவிதை`, remove the printed quotation marks, or create a hybrid such as `பதில் / மறுப்புக் கவிதை`.

## Gate 3 closure ledger

- active new Kalaignar items examined: **3/3**;
- direct item-heading authorities resolved: **3/3**;
- printed contents-page item-title witnesses: **0** — no contents page in the publication preliminaries;
- event/provenance witnesses classified without title substitution: **3/3**;
- explicit competing terminology requiring a decision: **1** — Item 04 `மறுப்புக் கவிதை` vs `பதில் கவிதை`, **resolved** in favour of the direct scan-67 heading;
- repository convenience-heading normalization corrected: **Item 02** only;
- unresolved title-witness conflicts: **0**;
- verified page-text changes in Gate 3: **none**;
- page-status changes in Gate 3: **none**;
- canonical Tamil item files created in Gate 3: **0/3**;
- existing release-cleared poem-tree changes: **none**.

**Phase 3 Gate 3 is COMPLETE / PASS.**

## Exact next gate

Proceed to **Phase 3 Gate 4 — canonical Tamil assembly only** for Items 01, 02 and 04.

Assembly must use only the already verified page records and the title authorities fixed in this document; preserve certified page joins, quotation state, separators, source punctuation and scan provenance; exclude scan 66 from Kalaignar canonical text.

Do not begin Gate 5 assembly/source-completeness review, Tamil final clearance or translation in the same activity.
