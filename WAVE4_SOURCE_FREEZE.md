# Wave 4 — All-Poems Source Freeze

## Status

**FROZEN FOR SOURCE INTAKE — 6/6 TOP-LEVEL WORKSPACES**

This record freezes the source-side boundary for the Kalaignar Digital Library's intended all-poems Wave 4. It does **not** itself modify or authorize Digital Library implementation.

## Audited source boundary

Repository: `pugazg/kalaignar-poems`

Audited source commit:

`f887f9b19eedbb2e00351e81515ac888e5ea1907`

Audited source tree:

`bcea43a808f274dfaac8a66d4ca7a70c1332d3e7`

Cross-witness audit:

`WAVE4_CROSS_WITNESS_AUDIT.md`

The commit that adds this freeze document is a documentation wrapper around the audited boundary above. The **six work-tree SHAs below are the source payload pins**. A later documentation-only commit does not alter those work trees.

## Scope

All current top-level workspaces under `poems/` are included in the source freeze:

| # | Workspace | Source payload tree | Source/release state |
|---:|---|---|---|
| 1 | `anaiya-vilakku-anna` | `bddc54f0493dbc38e53f9ec9fe5162e0c4e49464` | Tamil complete; English release-complete |
| 2 | `idhayathai-thanthidu-anna` | `a92fb5ff742aa1c5ae11039fc55a9ffa4bdafc63` | Tamil complete; English release-complete; already integrated in Digital Library |
| 3 | `kaalap-pezhaiyum-kavithai-saaviyum` | `07a2d3cba65a1eb10b887dac3c83ce993f94a710` | 58/58 Tamil final-cleared; 58/58 English release-cleared |
| 4 | `kalaignarin-kavithaigal` | `6489ab3d4fdf21a1442aa46d7a7aa1a08071be7e` | 77/77 Tamil final-cleared; 77/77 English release-cleared |
| 5 | `marathi` | `fda18674b928f7934f66c695ba494208344a6814` | Tamil complete; English release-complete |
| 6 | `thennan-kathai` | `a63a171ffee75d12e6ef612c41b36262e5562a78` | Tamil complete; English release-complete |

No source workspace is excluded from the all-poems Wave-4 source boundary.

## Controlling source identities

### 1. அணையா விளக்கு அண்ணா

- file: `TVA_BOK_0065770_அணையா_விளக்கு_அண்ணா(1).pdf`
- SHA-256: `f68ec53dc87f3b331397fe3c6d686613fb22fcb0af717b022513867cf6d030f4`
- bytes: **109,709,692**
- physical scans: **19**
- verified poem/text-body scans: **7–17**
- source-boundary status: verified, not preliminary

### 2. இதயத்தைத் தந்திடு அண்ணா

- file: `TVA_BOK_0064132_இதயத்தைத்_தந்திடு_அண்ணா.pdf`
- SHA-256: `152cfb251a2049662102a2296487220f6f227f243657c9456df34105520676fe`
- bytes: **26,816,066**
- physical scans: **28**
- poem scans: **13–26**
- standalone source-work tree remains exactly the previously integrated tree `a92fb5ff742aa1c5ae11039fc55a9ffa4bdafc63`

### 3. காலப் பேழையும் கவிதைச் சாவியும்

- file: `TVA_BOK_0063593_காலப்_பேழையும்_கவிதைச்_சாவியும்.pdf`
- SHA-256: `ad5a6a4b4d2b111120f99baa4aff4ab639cf1a9f9c71a6899e0c3d2c4a08bcc3`
- bytes: **336,148,702**
- physical scans: **306**
- canonical numbered poem/items: **58/58**
- English items: **58/58 release-cleared**

### 4. கலைஞரின் கவிதைகள்

- file: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`
- SHA-256: `19ee85eea737d3ddac5736db8acd8d4453c9328926fb04256dba4ec9c7b2468e`
- bytes: **486,369,088**
- physical scans: **465**
- canonical poem/items: **77/77**
- English items: **77/77 release-cleared**
- anthology group/divider structure remains source provenance and must not be flattened into invented standalone publication facts

### 5. மறத்தி

- file: `TVA_PRL_0033129_முரசொலி_பொங்கல்_மலர்_1955.pdf`
- SHA-256: `9fc83ec0da9925d4af87074014dca7d5e0bb73e10d4310e8bfcdb21572d9e60c`
- bytes: **220,351,424**
- physical PDF pages: **248**
- exact work range: **58–61**
- page 58: title/image page
- pages 59–61: poem body
- page 62: different item; positive closing boundary

### 6. தென்னவன் காதை

- controlling file: `TVA_PRL_0007090_முரசொலி.pdf`
- SHA-256: `a9252bcb0931366c61497d55a354964b1450a8254d2ca3f119c5f6b1c680a643`
- bytes: **246,184,679**
- physical PDF pages: **218**
- exact work range: **145–152**
- page 153: different work; positive closing boundary
- earlier apparent 150-page limit: renderer/preview limitation, **not** source length
- separately supplied page-151/page-152 one-page PDFs: retained only as historical auxiliary verification extracts; not separate controlling-source members
- user-directed scan-151 editorial omission: remains a witness-specific documented exception and must not be silently restored or propagated to another witness

## Cross-witness identity result

The complete 58-item `காலப் பேழையும் கவிதைச் சாவியும்` title inventory and complete 77-item `கலைஞரின் கவிதைகள்` canonical inventory were audited together with all four standalone workspace titles and, for identified overlaps, their canonical Tamil source layers.

Confirmed alternate-witness relationships:

1. `இதயத்தைத் தந்திடு அண்ணா`
   - standalone witness: `poems/idhayathai-thanthidu-anna/`
   - publication witness: `கலைஞரின் கவிதைகள்`, item 01
   - result: **same canonical poem / alternate source witness**

2. `தென்னவன் காதை`
   - standalone 1956 `முரசொலி-பொங்கல் மலர்` witness: `poems/thennan-kathai/`
   - publication witness: `கலைஞரின் கவிதைகள்`, item 02
   - result: **same canonical poem / alternate source witness**

Other audit results:

- exact canonical-title intersection between the 58-item and 77-item publication inventories: **0**;
- `அணையா விளக்கு அண்ணா`: no exact item-title match in either multi-item publication;
- `மறத்தி`: no exact item-title match in either multi-item publication;
- no other duplicate canonical identity is asserted without source-backed evidence.

Title-only deduplication is forbidden. Canonical poem identity, source witness, and publication membership remain separate concepts.

## Digital Library intake implications

This source freeze establishes **100% source-repository workspace coverage** for Wave 4, but it does not prescribe a lossy catalogue model.

Source-side facts to preserve during later implementation:

- the six top-level source workspaces remain represented;
- `இதயத்தைத் தந்திடு அண்ணா` is already live and must not be duplicated;
- `காலப் பேழையும் கவிதைச் சாவியும்` is one publication workspace with **58 internal poem/item units**;
- `கலைஞரின் கவிதைகள்` is one publication workspace with **77 internal poem/item units**;
- the 58 + 77 internal units are not automatically 135 new top-level catalogue works;
- the two confirmed same-poem relationships must preserve both source witnesses;
- source-witness differences must not be normalized away;
- source dates, edition facts and publication claims must be carried only where explicitly established by the corresponding source.

## Freeze rule

The six work-tree SHAs in this document are the Wave-4 source payload pins.

A future source-backed correction may legitimately advance one of those trees, but doing so **reopens this source freeze for the affected work**. The later Digital Library implementation must not silently consume a newer work tree while claiming this freeze.

Documentation-only changes outside the six workspaces do not change the frozen source payload unless they explicitly supersede this record.

## Final source readiness decision

**PASS — ALL 6/6 TOP-LEVEL POEMS WORKSPACES ARE SOURCE-READY FOR THE INTENDED ALL-POEMS WAVE 4.**

Cross-witness audit: **PASS**.

Outstanding source-completeness blockers: **0**.

Digital Library implementation performed by this source-freeze activity: **none**.