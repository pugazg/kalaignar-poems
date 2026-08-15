# HANDOVER — Kalaignar Poems Archive

## Repository

`pugazg/kalaignar-poems`  
Branch: `main`

## Mandatory startup for every continuation

1. Read `POEM_PROCESSING_GUIDE.md` completely.
2. Read root `README.md`.
3. Read the target work's `README.md`, `metadata/source.md`, `indexes/page-map.md`, and `audit.md`.
4. Inspect existing `pages/` before creating anything; continue existing work and do not duplicate page records.
5. Re-open the supplied scan page directly before marking any page `verified`.
6. The attached/source scan remains controlling; do not silently normalize Tamil or poem lineation.
7. Do not commit source PDFs.

## Current work

Slug: `poems/idhayathai-thanthidu-anna/`  
Tamil title: **இதயத்தைத் தந்திடு அண்ணா**  
Source file: `TVA_BOK_0064132_இதயத்தைத்_தந்திடு_அண்ணா.pdf`  
SHA-256: `152cfb251a2049662102a2296487220f6f227f243657c9456df34105520676fe`  
Scan pages: **28**

## Source-supported poem context

Scan 13 states that on **9.2.1969**, on **சென்னை வானொலி**, **கலைஞர் மு. கருணாநிதி** offered **இதயத்தைத் தந்திடு அண்ணா** as a **கண்ணீர்க் கவிதாஞ்சலி** to **பேரறிஞர் அண்ணா**.

Do not replace this wording with an inferred venue/event description.

## Completed activities

Repository initialized with the permanent processing guide, source metadata, page map, audit, work README and handover.

Verified page records now exist for **scans 1–18**:

- `pages/0001.md` — cover
- `pages/0002.md` — donation/book-list advertisement
- `pages/0003.md` — captioned photograph
- `pages/0004.md` — portrait page
- `pages/0005.md` through `pages/0010.md` — complete `என்னுரை` by குறிஞ்சி சுப்பிரமணியன்
- `pages/0011.md` — rotated captioned photograph, printed date 8.11.1960
- `pages/0012.md` — rotated captioned photograph, printed date 15.8.1975
- `pages/0013.md` through `pages/0018.md` — first poem batch, printed pages 11–16

Current counts:

- physical scans verified: **18 / 28**
- physical scans not started: **10 / 28**
- front matter scans 1–12: **complete / verified**
- poem-body scans verified: **6 / 14**
- poem-body scans not started: **8 / 14**
- poem `needs-review`: **0**
- poem `blocked`: **0**
- poem-body mapped range: **13–26**

## Important source-fidelity notes already established

### Scan 3

Direct rotation-and-visual inspection confirmed that the caption refers to **ரூபாய் 3 இலட்சம் பங்குத் தொகையாக** வழங்கியபோது for the **“பெரியார்” திரைப்படக் காவியம்**, dated **22.9.2006**. Do not reuse the discarded earlier working description about three lakh books.

### Scan 6 → scan 7

The physical page split is `ஆலடி` at the bottom of scan 6 and `அருணா` at the top of scan 7. Do not move the continuation between page records.

### Scan 8

Source forms such as `அய்ஏஎஸ்` and `அப்துல்ரகுமான்` are deliberately retained.

### Scan 9

The large bordered prose passage in the `என்னுரை` is retained separately as boxed printed text. It is not poem text.

### Scan 10

High-resolution source review confirmed:

- `மொழிபெயர்ப்பு செய்யப்பட்டு` — do not insert an editorial `ச்`;
- the later title occurrence is `“இதயத்தை தந்திடு அண்ணா”`, without the `த்` present in other occurrences.

Both are intentional source transcriptions, not errors to normalize.

### Scan 13

Keep the printed parenthetical 9.2.1969 / சென்னை வானொலி context separate from the poem verse. Scan 13 ends `உமைத்`, continuing onto scan 14.

### Scan 14

Direct source review retained unusual forms including `தங்கு சனி வேல்`, `வேது`, `பொருதடக்கை`, `கலவி மடவீர் கழற்சென்னி`, and `களப்பரணி..`.

### Scan 15

Retain `அரு மூன்று எழுத்தாலே` and the visibly printed `அய்ம்பத்திரண்டுதனில்`.

### Scan 16

The repeated source form is `முன்றெழுத்து`, not a normalized replacement. Also retain `எடெல்லாம் வீடெல்லாம் தமிழ்`. The page's stepped indentation is represented in the poem record.

### Scan 17

Retain `சாலை யோரத்திலே`, `வேலையற்றதுகள்`, `பனுவல்`, `நாலைந்து`, and the source punctuation `மாண்பே! .`. The final line continues to scan 18.

### Scan 18

Retain source readings including `பனிமலர் வீழ் தும்பியதாய்த்`, `கோலற்ற குருடர்`, and `தீர் அண்ணா திராவிடர் கழகமெனும்`. Scan 18 ends `அன்புறு காந்தியின் அருளால் இன்று`, continuing onto scan 19.

## Exact next activity

Continue the poem with **scans 19–26**.

1. Re-open scans 19–26 directly before transcription.
2. Create `pages/0019.md` through `pages/0026.md`.
3. Preserve exact poetic lineation, indentation, stanza spacing, dashes, quotation marks, ellipses, repeated words and unusual source spellings.
4. Follow page-boundary continuations explicitly; scan 19 begins by continuing the final line/context from scan 18.
5. Do not use OCR output, metre, remembered versions or web text as authority.
6. If a reading is difficult, follow the difficult-reading protocol in `POEM_PROCESSING_GUIDE.md` rather than guessing.
7. On scan 26, keep the poem conclusion and printer imprint as distinct source layers within the physical page record.
8. Update `indexes/page-map.md`, `audit.md`, work/root README and this handover after the batch.
9. After all poem scans 13–26 are verified, create `sections/idhayathai-thanthidu-anna.md` only from verified page records and perform a page-to-assembly source review.

## Assembly

`sections/idhayathai-thanthidu-anna.md` has **not** been created intentionally. Do not assemble yet unless scans **19–26** have been source-reviewed and the poem body is complete.

## Translation

English translation is **intentionally deferred**. Do not start translation until:

- all poem-body scans 13–26 are source-reviewed;
- the assembled Tamil poem exists;
- source audit and assembly review are stable.
