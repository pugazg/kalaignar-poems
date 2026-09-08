# Phase 3 Gate 3 — Title-Witness Reconciliation — தலைகேட்டான் தம்பி

Date: **2026-09-08**

## Scope

Work: **தலைகேட்டான் தம்பி**

Controlling source: `TVA_PRL_0001662_முரசொலி_பொங்கல் மலர்_1966.pdf` — **75 physical scans / 30,952,719 bytes / SHA-256 pending exact-byte hash**.

Phase prerequisites:

- Phase 2: **6/6 VERIFIED / 0 unresolved**;
- Phase 3 Gate 1: **PASS**;
- Phase 3 Gate 2: **PASS**;
- scan-18 structural-role correction: **COMPLETE**.

The exact SHA-256 remains an open provenance field because checksum execution has repeatedly failed. No hash is inferred or invented. Gate 3 is limited to reconciliation of already established title/author witnesses from the same controlling scan and bibliographic record; **Gate 4 canonical assembly remains blocked until the checksum is durably locked**.

## Witnesses

### Bibliographic witness

**`தலைகேட்டான் தம்பி`**

Bibliographic author: **கலைஞர் மு. கருணாநிதி**.

### Direct scan-18 witness

Complete direct title: **`தலைகேட்டான் தம்பி`**.

Source-layout provenance:

- upper decorated title element: **`தலைகேட்டான்`**;
- lower decorated title element: **`தம்பி`**;
- direct source-position author attribution: **`கருணாநிதி`**.

The source-visible `தம்பி` is title material, not poem-body text. `கருணாநிதி` is author attribution, not poem-body text. This role distinction is already locked in `POST_PHASE2_STRUCTURAL_CORRECTION.md` and `pages/0018.md`.

## Reconciliation

The two title witnesses agree **lexically and in word order**:

- bibliographic: `தலைகேட்டான் தம்பி`;
- direct scan: `தலைகேட்டான் தம்பி`.

There is therefore:

- lexical title conflict: **0**;
- punctuation title conflict: **0**;
- word-order conflict: **0**;
- need for a hybrid title: **none**.

The spatial split on scan 18 is layout provenance only. It must not be converted into two separate work titles, and the lower `தம்பி` must not be duplicated into the poem body.

## Canonical assembly authority

When Gate 4 is eventually permitted, the canonical Tamil file must use exactly:

`# தலைகேட்டான் தம்பி`

The canonical heading is therefore governed by the **direct scan-18 complete title witness**, which is identical to the bibliographic title. The scan-specific decorated upper/lower layout and direct author attribution remain provenance metadata rather than duplicated canonical body text.

No exclamation mark, punctuation variant, modernized spelling, expanded author form, or hybrid title is to be introduced into the canonical heading.

## Gate result

**PHASE 3 GATE 3 — PASS.**

- bibliographic title witness preserved: **yes**;
- direct title witness preserved: **yes**;
- author attribution preserved separately: **yes**;
- lexical title conflicts: **0**;
- canonical title authority locked: **`தலைகேட்டான் தம்பி`**;
- page-text changes required by Gate 3: **0**;
- unresolved title issues: **0**.

## Remaining provenance hold / exact next activity

The source SHA-256 is still pending and remains the final source-identity hold before canonical assembly.

1. Compute and durably record the exact SHA-256 from the same 75-page / 30,952,719-byte PDF.
2. Only after that lock, proceed to **Phase 3 Gate 4 — canonical Tamil assembly** from verified `pages/0018.md`–`0023.md`.
3. Preserve the Gate-2 join decisions, especially direct **22→23** carry with no inserted separator.
