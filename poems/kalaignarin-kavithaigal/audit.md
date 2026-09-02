# Audit — கலைஞரின் கவிதைகள்

## Source identity

`TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf` — 465 physical pages, 486,369,088 bytes, SHA-256 `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`.

## Page-layer status

- Phase 1: **COMPLETE — 465/465**;
- Phase 2 source coverage: **COMPLETE — 465/465**;
- Phase 2 clearance: **COMPLETE — C01–C19**;
- final page status: **0 partial / 0 needs-review / 465 verified**;
- contiguous verified boundary: **1–465**.

## Phase 3 Gate 1 audit — COMPLETE / PASS

Scope: **physical scan ↔ printed-page reconciliation only**.

- scan 1 — front cover, unpaginated;
- scans 2–17 — logical Roman I–XVI;
- scans 18–464 — logical Arabic 1–447, invariant `logical printed page = scan_page - 17`;
- scan 465 — back cover, unpaginated.

No physical scan is outside these ranges; no range overlaps another. The verified page-record `printed_page` remains a source-visible numeral witness only; reconciled but suppressed numerals are not backfilled. Full evidence is in `PHASE3_STRUCTURE_AUDIT.md`.

## Phase 3 Gate 2 audit — COMPLETE / PASS

Scope: **boundary / page-join certification only**.

- physical scans covered: **465/465**;
- physical adjacent transitions covered: **464/464**;
- missing physical pages: **none**;
- duplicated physical pages: **none**;
- source-order normalization/reordering: **none**;
- verified page-text changes: **none**.

High-risk joins locked by Gate 2 include 236→237→238→239 intentional interposition, 370→371→372→373→374 close/blank/divider/verso/opening sequence, 397→398→399→400 item boundaries, 424→425→426, 450→451→452→453 and final 464→465 cover closure. Full evidence is in `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

## Phase 3 Gate 3 audit — COMPLETE / PASS

Scope: **title-witness reconciliation only**.

`PHASE3_TITLE_WITNESS_RECONCILIATION.md` compares verified contents witnesses on scans 15–17 with verified section-divider/title/opening witnesses.

### Complete accounting

- contents/group/item title witnesses: **81**;
- exact title-string matches after collapsing display line breaks: **51**;
- source-valid variant relationships: **30**;
- unresolved title witnesses: **none**;
- hybrid/normalized title constructions: **none**;
- verified page-text changes: **none**.

### Authority locked for later assembly

- dedicated section-divider or item title/opening witness controls the canonical section/item title;
- contents witness remains preserved exactly and is not silently corrected;
- no canonical title may combine pieces of two source witnesses;
- punctuation, spacing, quotation marks and lexical wording come wholly from the authoritative divider/opening witness.

### High-risk title variants locked

- contents `உடன்பிறப்பின் பற்று` → opening `உடைமைகள் பத்து`;
- contents section `கண்ணீர்க் கவிதை` → divider `கண்ணீர்த் துளிகள்`;
- contents `அருமருந்தே! அன்புறவு உடன்பிறப்பே!` → opening `அருமருந்தே! அன்பழக உடன்பிறப்பே!`;
- contents `விதையாய் முளைத்து விழுதுகள் விட்டோம்` → opening `விதையாய் முளைத்து விழுதுகள் விடட்டும்!`;
- contents `சூரியனைப் பனிக்கட்டி என்கிறாய்!` → opening `சூரியனைப் பனிக்கட்டி என்கின்றார்!`;
- contents `கொள்ளை போதும்மா தமிழ்நாடு` → opening `கொள்ளை போகுதம்மா தமிழ்நாடு`;
- contents `முடியுமா? கிழித்தெறிவோம் வாரீர்!` → opening `முகமூடி கிழித்தெறிவோம் வாரீர்!`.

Gate 3 also records a source locator anomaly without altering the contents transcription: contents scan 16 gives page **279** for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்`, while the verified dedicated opening is scan **293 / printed page 276** and the item continues through printed page 279.

### Gate result

The verified page layer remains **465/465 verified** and unchanged. **Gate 3 PASS.**

## Next audit gate

**Phase 3 Gate 4 — canonical Tamil assembly only.** Build canonical section/item files strictly from verified page records, preserve physical source order and scan provenance, and apply Gate-3 authoritative divider/opening titles without normalizing source text. Gate 5 assembly/source-completeness review, Tamil final clearance and translation remain blocked until their ordered turn.
