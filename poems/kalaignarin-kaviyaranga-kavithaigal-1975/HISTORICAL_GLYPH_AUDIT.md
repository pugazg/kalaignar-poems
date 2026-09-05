# Historical Tamil glyph audit — கலைஞரின் கவியரங்கக் கவிதைகள் (1975)

This work uses the user-supplied `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` as a **verification aid** for older Tamil typeforms.

The controlling authority remains the pixels of `TVA_BOK_0064169_கலைஞரின்_கவியரங்கக்_கவிதைகள்.pdf`. The guide is used to identify historical character identity; it is not authority to modernize spelling, grammar, vocabulary, punctuation or lineation.

## Required screen

Every Tamil text page is checked for the full known historical/reform-sensitive set:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Rules:

- identify the historical character first, then encode that identity in normal Unicode;
- inspect the complete cluster, not the nearest modern-looking shape;
- compare repeated forms within this 1975 edition whenever needed;
- source wording remains untouched apart from proven glyph-identity decoding;
- no global replacement;
- unresolved clusters remain `needs-review`;
- this glyph pass does **not** by itself promote a Phase-1 page to `verified`.

## Batch audit

| Scan | Source role | Representative checked forms | First-pass result | Page status |
|---:|---|---|---|---|
| 9 | Anna cross-witness opening | `அண்ணா` (`ணா`), `அன்னை` (`னை`) | historical-form screen applied; no unresolved reform-family identity retained | `partial` |
| 10 | Anna cross-witness continuation | full 13-family screen; repeated same-edition letterforms compared against neighboring pages | no unresolved reform-family identity retained | `partial` |
| 11 | Anna cross-witness continuation | `அண்ணா` / `அண்ணாவானார்` (`ணா`), `நினைவுண்டா` (`னை`) | historical-form screen applied; no unresolved reform-family identity retained | `partial` |
| 12 | Anna cross-witness continuation | `அண்ணா` (`ணா`), `மாற்றான்` (`றா`) | historical-form screen applied; `றா` decoded by character identity rather than modern visual resemblance | `partial` |

## Separation from ordinary textual review

Historical-glyph decisions are kept separate from edition wording and punctuation differences. The existing release-cleared Anna poem may be consulted only as a secondary cross-witness to locate comparison points; it does not override the 1975 scan.

Phase 2 will independently recheck these pages from source pixels before any `verified` status is assigned.
