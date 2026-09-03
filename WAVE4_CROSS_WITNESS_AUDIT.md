# Wave 4 — All-Poems Cross-Witness Identity Audit

## Purpose

This audit exists to support the Kalaignar Digital Library Wave-4 goal of covering **every top-level work workspace in `pugazg/kalaignar-poems`** without creating duplicate canonical works merely because the repository preserves more than one source witness for the same poem.

The audit is source-side only. It changes no Tamil text, English translation, page record, canonical assembly, title witness, or Digital Library implementation.

## Audited evidence boundary

Repository: `pugazg/kalaignar-poems`

Corrected pre-audit source commit:

`f11726f035f1304c54eac04f99124c720152af90`

Tree:

`33cd982b3c6c8fa1760b235e89b32f122f4c3f10`

This checkpoint already contains the Wave-4 source-identity corrections for `மறத்தி`, `தென்னவன் காதை`, and `அணையா விளக்கு அண்ணா`.

## Repository scope

Top-level work workspaces: **6/6**

1. `poems/anaiya-vilakku-anna`
2. `poems/idhayathai-thanthidu-anna`
3. `poems/kaalap-pezhaiyum-kavithai-saaviyum`
4. `poems/kalaignarin-kavithaigal`
5. `poems/marathi`
6. `poems/thennan-kathai`

The two multi-item publication workspaces contain:

- `காலப் பேழையும் கவிதைச் சாவியும்` — **58** canonical numbered poem/item units;
- `கலைஞரின் கவிதைகள்` — **77** canonical poem/item units.

The other four workspaces preserve standalone source witnesses.

## Identity rules

1. **Canonical poem identity and source-witness identity are different facts.** One canonical poem may legitimately have more than one printed/source witness.
2. **Title equality is evidence to inspect, not authority to deduplicate.** No work is merged, suppressed or redirected from title matching alone.
3. **Title inequality is not proof of unrelated identity.** Variants, punctuation and edition wording may differ; any future relationship claim requires source-backed review.
4. **Publication membership is not canonical-work identity.** A poem appearing inside an anthology/publication remains a member reading unit of that publication even if another source witness is preserved in a standalone workspace.
5. **Witness text is never silently reconciled.** Edition/source-specific wording, punctuation, lineation and archival exceptions remain attached to the witness that establishes them.
6. This audit does **not** turn the 58 + 77 internal publication units into 135 top-level `LibraryWork` records. That is a later Digital Library modelling decision; the source archive continues to preserve each publication and its internal item structure.

## Inventory comparison

### `காலப் பேழையும் கவிதைச் சாவியும்` — 58-item inventory

The complete canonical/display title inventory in `poems/kaalap-pezhaiyum-kavithai-saaviyum/indexes/item-title-map.md` was compared against:

- all 77 canonical titles in `கலைஞரின் கவிதைகள்`;
- the four standalone workspace titles.

Result:

- exact canonical-title intersection with the 77-item `கலைஞரின் கவிதைகள்` inventory: **0**;
- exact match for standalone `இதயத்தைத் தந்திடு அண்ணா`: **0**;
- exact match for standalone `தென்னவன் காதை`: **0**;
- exact match for standalone `அணையா விளக்கு அண்ணா`: **0**;
- exact match for standalone `மறத்தி`: **0**.

This is an exact-title census only. It does not claim that no future source-backed conceptual or variant-title relationship could ever be established.

### `கலைஞரின் கவிதைகள்` — 77-item inventory

The complete canonical inventory in `poems/kalaignarin-kavithaigal/indexes/canonical-source-map.md` contains two exact-title matches to standalone workspaces:

| Canonical poem identity | Standalone witness | Publication witness | Audit decision |
|---|---|---|---|
| `இதயத்தைத் தந்திடு அண்ணா` | `poems/idhayathai-thanthidu-anna/` | `கலைஞரின் கவிதைகள்`, item 01 | same canonical poem / alternate source witness |
| `தென்னவன் காதை` | `poems/thennan-kathai/` | `கலைஞரின் கவிதைகள்`, item 02 | same canonical poem / alternate source witness |

No exact title match was found for standalone `அணையா விளக்கு அண்ணா` or `மறத்தி` in the 77-item inventory.

## Witness finding 1 — `இதயத்தைத் தந்திடு அண்ணா`

Compared source-side canonical assemblies:

- standalone: `poems/idhayathai-thanthidu-anna/sections/idhayathai-thanthidu-anna.md`;
- publication witness: `poems/kalaignarin-kavithaigal/sections/01.md`.

The identity is not inferred from title alone. Both witnesses establish the same poem through their shared source context and sustained body correspondence: the 9 February 1969 Chennai Radio context, the elegiac address to Perarignar Anna, and the same extended poetic sequence are present across the two canonical source layers.

At the same time, the witnesses retain edition/source-specific typography, punctuation, spacing and wording. They are therefore **alternate source witnesses of the same canonical poem**, not interchangeable files.

Durable rule:

- preserve the existing standalone witness and its stable identity;
- preserve `கலைஞரின் கவிதைகள்` item 01 as the publication's own witness/member unit;
- do not overwrite either source layer with the other;
- do not create a second canonical top-level work merely because the anthology witness exists.

The standalone work tree at the audited checkpoint remains exactly:

`a92fb5ff742aa1c5ae11039fc55a9ffa4bdafc63`

This is the same work tree previously pinned by the already-live Digital Library poem integration; the Wave-4 source hygiene work did not alter it.

## Witness finding 2 — `தென்னவன் காதை`

Compared source-side canonical assemblies:

- standalone: `poems/thennan-kathai/sections/thennan-kathai.md`;
- publication witness: `poems/kalaignarin-kavithaigal/sections/02.md`.

Again, the identity is not title-only. The two layers share the same poem opening and sustained narrative/body sequence while preserving source-specific spelling, punctuation, layout and textual witness differences.

Decision: **same canonical poem / alternate source witness**.

The standalone witness is the 1956 `முரசொலி-பொங்கல் மலர்` source, now frozen to the complete 218-page `TVA_PRL_0007090_முரசொலி.pdf`, with work range 145–152. The later `கலைஞரின் கவிதைகள்` item 02 remains a separate publication witness.

The documented scan-151 editorial omission belongs specifically to the standalone archival derivative under the user's explicit instruction. It must **not** be projected onto, used to rewrite, or treated as evidence about the separate `கலைஞரின் கவிதைகள்` witness.

Durable rule:

- preserve both source witnesses;
- do not normalize one against the other;
- model their common canonical identity separately from witness provenance in any future Digital Library implementation.

## No other confirmed duplicate canonical identity

Within the scope inspected for this freeze:

- the 58-item and 77-item publication inventories have **0 exact canonical-title intersections**;
- standalone `அணையா விளக்கு அண்ணா` has no exact item-title match in either multi-item publication;
- standalone `மறத்தி` has no exact item-title match in either multi-item publication;
- no additional same-canonical-poem relationship is asserted without source-backed evidence.

This is deliberately conservative. Future evidence may add a witness relationship, but absence of present evidence is never converted into a stronger negative historical claim.

## Source-work tree census at corrected pre-audit boundary

| Workspace | Tree SHA |
|---|---|
| `anaiya-vilakku-anna` | `bddc54f0493dbc38e53f9ec9fe5162e0c4e49464` |
| `idhayathai-thanthidu-anna` | `a92fb5ff742aa1c5ae11039fc55a9ffa4bdafc63` |
| `kaalap-pezhaiyum-kavithai-saaviyum` | `07a2d3cba65a1eb10b887dac3c83ce993f94a710` |
| `kalaignarin-kavithaigal` | `6489ab3d4fdf21a1442aa46d7a7aa1a08071be7e` |
| `marathi` | `fda18674b928f7934f66c695ba494208344a6814` |
| `thennan-kathai` | `a63a171ffee75d12e6ef612c41b36262e5562a78` |

## Historical renderer/auxiliary-source note

For `தென்னவன் காதை`, older README/assembly prose may mention separately supplied page-151 and page-152 extracts because those extracts were used when an earlier renderer appeared to stop at page 150. Current source-freeze authority is `poems/thennan-kathai/metadata/source.md` plus `SOURCE_COMPLETENESS_REVIEW.md`: exact-byte inspection establishes one 218-page controlling PDF containing pages 145–152. The separate extracts remain historical verification witnesses only.

## Audit result

**PASS — no cross-witness identity blocker remains for an all-poems Wave-4 source freeze.**

The repository can be frozen for 6/6 top-level workspaces while preserving the two confirmed alternate-witness relationships. The audit authorizes no Digital Library implementation by itself; it establishes only the source identity/provenance boundary to be consumed by a later explicitly authorised implementation phase.