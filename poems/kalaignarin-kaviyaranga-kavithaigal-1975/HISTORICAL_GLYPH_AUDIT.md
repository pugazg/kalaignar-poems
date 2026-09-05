# Historical Tamil glyph audit — கலைஞரின் கவியரங்கக் கவிதைகள் (1975)

This work uses the user-supplied `HISTORICAL_TAMIL_GLYPH_TRANSCRIPTION_GUIDE.md` as a verification aid for older Tamil typeforms.

The controlling authority remains the pixels of `TVA_BOK_0064169_கலைஞரின்_கவியரங்கக்_கவிதைகள்.pdf`. The guide identifies historical character identity; it is not authority to modernize spelling, grammar, vocabulary, punctuation or lineation.

## Required screen

Every **new-item Tamil target page** is checked for the full known historical/reform-sensitive set:

`ணா / ணை / ணொ / ணோ / லை / ளை / றா / றொ / றோ / னா / னை / னொ / னோ`

Rules:

- identify historical character identity first, then encode that identity in normal Unicode;
- inspect the complete cluster, not the nearest modern-looking shape;
- source wording remains untouched apart from proven glyph-identity decoding;
- no global replacement;
- unresolved clusters remain unresolved / `needs-review`;
- the glyph screen does **not** itself promote a Phase-1 page to `verified`.

## Processing-scope correction

The user has directed that already represented anthology blocks are to be marked existing and skipped rather than retranscribed. Therefore the historical-glyph production audit now follows only the four new Kalaignar blocks: **46–57, 58–65, 66, 67–68**.

Earlier glyph-audit records for scans 9–32 remain valid archival notes but no further cross-witness ranges are to be processed unless explicitly requested.

## New-item audit

| Scan | Item | Source role | First-pass result | Page status |
|---:|---:|---|---|---|
| 46 | 01 | event heading + poem opening | full historical-family screen required; no global replacement or modernization used; ordinary dense source text remains partly unread, so no uncertain glyph/text was guessed | `needs-review` |

### Scan 46 established witnesses

The page visibly establishes the event heading `புரட்சிக் கவிஞர் பாட்டரங்கில்`, printed attribution `முதல்வர் கலைஞர் தலைமைக் கவிதை`, date `29-4-71`, Bharathidasan 80th-birthday context, and Puduvai location. Clearly legible opening fragments were encoded conservatively. Unclear intervening lines remain unresolved.

## Exact next glyph activity

Apply the same full screen to **scan 47**, continuing NEW ITEM 01 only. Do not return to duplicate scan ranges.