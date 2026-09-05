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
| 21 | Nehru cross-witness opening | `அண்ணன்` / `அன்னை`; event-heading names | full screen applied; no reform-family ambiguity retained | `partial` |
| 22 | Nehru cross-witness continuation | `முன்னை`, `பின்னர்`; flower-name clusters | full screen applied; 1975 spacing retained independently | `partial` |
| 23 | Nehru cross-witness continuation | `பூமானே`, `கோமானே`, `நானிலம்`, `அன்றுமுதல்` | full screen applied; later-witness variants not substituted | `partial` |
| 24 | Nehru cross-witness continuation | `நனைத்து`, `மன்னரவர்`, `கண்ணீரை` | full screen applied; unusual `குரங்கின்கை` passage retained as this witness | `partial` |
| 25 | Nehru cross-witness continuation | `அண்ணல்`, `எண்ணெயிட்ட`, `பணமலை`, `குணமலை`, `நேரு வானார்` | reform-family identities pass; one separate bracketed line remains unread | `needs-review` |
| 26 | Nehru cross-witness continuation | `நானிலம்`, `பூங்குன்றனார்`, `கர்த்தபம்` | reform-family identities pass; separate lower-middle line(s) remain unread | `needs-review` |
| 27 | Nehru cross-witness continuation | `கள்ளி`, `வெள்ளி`, `கிள்ளி`; Kalinga passage | full screen applied; distinct clusters kept separate | `partial` |
| 28 | Nehru conclusion + S. D. Sundaram intro | `தனிநாயகம்`, `குண நாயகர்`, `பெண்ணுரிமை`, `மண்ணுரிமை` | reform-family identities pass; one `பண நாயகம்` line remains unread | `needs-review` |
| 29 | poet introductions | `கொத்தமங்கலம்`, `பண்பாட்டின்`, `எழுத்துரிமை` | reform-family identities pass; one `அன்பர் சுப்பு...` line remains unread | `needs-review` |
| 30 | poet introductions | `சூரியனும்`, `முருகு சுந்தரத்தைக்`, `ரகுமான்`, `வாக்குரிமை` | full screen applied; no reform-family ambiguity retained | `partial` |
| 31 | poet introductions | `வாக்குரிமை`, `கண்ணதாசன்`, `மாற்றார்`, `குயில்` | `மாற்றார்` checked as `றா`; first Kannadasan lines remain separately unread | `needs-review` |
| 32 | event conclusion | `சொத்துரிமை`, `பிள்ளைகள்`, `நல்லுரிமை`, `முழுமனிதன்` | full screen applied; no reform-family ambiguity retained | `partial` |

## Cross-witness first-pass results

### Anna block — scans 9–20

- historical-glyph first-pass: **12/12 complete**;
- historical-glyph unresolved clusters: **0**;
- separate ordinary-source unresolved reading: **1** — scan 18.

### Nehru block — scans 21–32

- historical-glyph first-pass: **12/12 complete**;
- historical-glyph unresolved clusters: **0**;
- separate ordinary-source unresolved page records: **5** — scans 25, 26, 28, 29 and 31;
- the later `கலைஞரின் கவிதைகள்` witness and the standalone Nehru source may be consulted only to locate comparison points; neither may fill unread 1975 text during Phase 1.

## Separation from ordinary textual review

Historical-glyph decisions are kept separate from edition wording and punctuation differences. Existing release-cleared poem witnesses may be consulted only as secondary cross-witnesses; they do not override the 1975 scan.

Phase 2 will independently recheck these pages from source pixels before any `verified` status is assigned.