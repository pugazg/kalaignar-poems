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

Verified page records now exist for **scans 1–12**:

- `pages/0001.md` — cover
- `pages/0002.md` — donation/book-list advertisement
- `pages/0003.md` — captioned photograph
- `pages/0004.md` — portrait page
- `pages/0005.md` through `pages/0010.md` — complete `என்னுரை` by குறிஞ்சி சுப்பிரமணியன்
- `pages/0011.md` — rotated captioned photograph, printed date 8.11.1960
- `pages/0012.md` — rotated captioned photograph, printed date 15.8.1975

Current counts:

- physical scans verified: **12 / 28**
- physical scans not started: **16 / 28**
- front matter scans 1–12: **complete / verified**
- poem-body scans verified: **0 / 14**
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

## Exact next activity

Begin the poem with **scans 13–18 / printed pages 11–16**.

1. Re-open scans 13–18 directly before transcription.
2. Create `pages/0013.md` through `pages/0018.md`.
3. On scan 13, transcribe the title and parenthetical contextual note separately from the poem verse.
4. Preserve exact poetic lineation, indentation, stanza spacing, dashes, quotation marks, ellipses, repeated words and unusual source spellings.
5. Do not use OCR output, metre, remembered versions or web text as authority.
6. If a reading is difficult, follow the difficult-reading protocol in `POEM_PROCESSING_GUIDE.md` rather than guessing.
7. Update `indexes/page-map.md`, `audit.md`, work/root README and this handover after the batch.
8. Do not yet assemble `sections/idhayathai-thanthidu-anna.md` unless all included poem pages are verified and the assembly scope is explicitly reached.

After scans 13–18, continue with scans **19–26** as the next poem batch.

## Translation

English translation is **intentionally deferred**. Do not start translation until:

- all poem-body scans 13–26 are source-reviewed;
- the assembled Tamil poem exists;
- source audit is stable.
