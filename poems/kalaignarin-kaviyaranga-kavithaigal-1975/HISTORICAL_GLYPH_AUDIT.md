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
| 13 | Anna cross-witness continuation | `மாற்றார்`, `நன்றென்றார்` (`றா`); `அண்ணா` (`ணா`); `அன்னை` (`னை`) | full historical-form screen applied; no reform-family ambiguity retained | `partial` |
| 14 | Anna cross-witness continuation | `அண்ணல்` / `அண்ணா` / `அண்ணன்` (`ணா`); `மாறி` (`றா`); `கண்ணீர்` cluster | full screen applied; edition wording retained independently of later witnesses | `partial` |
| 15 | Anna cross-witness continuation | `அண்ணா` / `அண்ணன்` (`ணா`); `நின்றார்`, `பல்லாவரத்தார்` (`றா` contexts) | full screen applied; no reform-family ambiguity retained | `partial` |
| 16 | Anna cross-witness continuation | `அண்ணன்` (`ணா`); `அன்னை` (`னை`); `மண்ணில்` cluster; `இருந்திட்டார்` (`றா` context) | full screen applied; no reform-family ambiguity retained | `partial` |
| 17 | Anna cross-witness continuation | `மாறிற்றுத்`, `நடத்திட்டார்`, `என்றான்` (`றா` contexts); `தமிழன்னை` (`னை`) | full screen applied; no reform-family ambiguity retained | `partial` |
| 18 | Anna cross-witness continuation | `அண்ணனாக` (`ணா`); `மன்னனாக` (`னா`); `தென்றலாய்ப்`, `பெற்றார்` (`றா`); `அன்னையென்பார்` (`னை`) | reform-family identities pass; one separate short source word remains unresolved and is not filled from another edition | `needs-review` |
| 19 | Anna cross-witness continuation | `அண்ணா` / `அண்ணன்` / `அண்ணனுக்கோர்` (`ணா`); `அன்னை` (`னை`); `நின்றார்` (`றா` context) | full screen applied; no reform-family ambiguity retained | `partial` |
| 20 | Anna cross-witness conclusion | `ஏதண்ணா`, `போதுமண்ணா`, `அண்ணா`, `தந்திடண்ணா` (`ணா`); `காற்று` (`றா`) | full screen applied; no reform-family ambiguity retained | `partial` |

## Anna cross-witness first-pass result

- scans **9–20** have now received the historical-glyph first-pass;
- every Tamil page in this block received the full 13-family screen;
- historical-glyph unresolved clusters: **0**;
- separate ordinary-source unresolved reading: **1** — scan 18, one short right-aligned word after `இனிமேலே எனப்`;
- no page is `verified`; Phase 2 remains a separate independent visual gate.

## Separation from ordinary textual review

Historical-glyph decisions are kept separate from edition wording and punctuation differences. The existing release-cleared Anna poem may be consulted only as a secondary cross-witness to locate comparison points; it does not override the 1975 scan. In particular, later-edition wording was **not** used to fill the unresolved scan-18 word or to insert lines not visibly present in this 1975 witness.

Phase 2 will independently recheck these pages from source pixels before any `verified` status is assigned.
