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

### Complete accounting

- physical scans covered: **465/465**;
- physical adjacent transitions covered: **464/464**;
- missing physical pages: **none**;
- duplicated physical pages: **none**;
- source-order normalization/reordering: **none**;
- verified page-text changes: **none**.

Every source adjacency is accounted for as an internal continuation, item close/open, speaker/performance-note or quotation carry-over, separator/ornament boundary, blank/verso/divider transition, cover transition, or an intentional physical-order exception.

### High-risk joins locked

- **236→237→238→239** — intentional physical interposition; do not reorder.
- **370→371→372→373→374** — poem close → blank/show-through verso → `கண்ணீர்த் துளிகள்` divider → divider verso → `பன்னீர்ச்செல்வமே!` opening; show-through is not edition text.
- **397→398→399→400** — clean close/open boundaries across three items.
- **424→425→426** — previous item closes; `ஒரு சொட்டுத் தேன்!` opens on 425 and continues on 426.
- **450→451→452→453** — one item continues and closes on 452; `திசை திருப்பல் நியாயம்தானா?` opens on 453.
- **464→465** — final poem closes on 464; 465 is the back cover with no body-text continuation.

Full evidence and policy are in `PHASE3_BOUNDARY_JOIN_AUDIT.md`.

### Gate result

The verified page layer remains **465/465 verified** and unchanged. **Gate 2 PASS.**

## Next audit gate

**Phase 3 Gate 3 — title-witness reconciliation.** Compare contents-page, section-divider/title-page and other relevant title witnesses; preserve every source form exactly and record explicit later-assembly authority decisions where variants differ. Never create a hybrid title. Canonical assembly, Tamil final clearance and translation remain blocked until their ordered turn.
