# Phase 3 Canonical Tamil Assembly — Gate 4

Work: **கலைஞரின் கவிதைகள்**
Controlling source: `TVA_BOK_0064091_கலைஞரின்_கவிதைகள்.pdf`

## Scope

This record closes **Phase 3 Gate 4 — canonical Tamil assembly only**. It does not perform Gate 5 assembly/source-completeness review, Tamil final clearance, translation or release work.

## Result

**PASS — canonical Tamil poem-body assembly generated mechanically from the verified page layer.**

- page layer checked: **465/465 `verified`**;
- canonical body scan interval: **18–464** (**447 physical scans**), in exact physical source order;
- canonical output: `sections/kalaignarin-kavithaigal.md`;
- provenance map: `indexes/canonical-source-map.md`;
- explicit `scan_page` marker coverage: **447/447**;
- marker-only/non-edition-text body scans retained as physical provenance: **6**;
- physical section runs recorded: **83**;
- Gate-3 title variants retained in source-map metadata: **30/30**;
- canonical file SHA-256: `ee021de215f2dcca176afe31959f07fdd6ed2b1b2926ff6d3cf91c43d986f57d`.

## Gate-4 conflict handling

The first assembly exposed stale title metadata in six otherwise verified records. Per the Gate-4 rule, the affected page records were reopened before final assembly:

- scan 406: canonical/dedicated title synchronized to `கேட்டுண்டோ?`; the poem line `பாரத வீரா! நீ கேட்டதுண்டோ?` remains unchanged;
- scan 409: canonical/dedicated title synchronized to `இன்றுமா கூச்சல்?`; the poem line `இளித்த வாயரே இன்னுமா கூச்சல்?` remains unchanged;
- scans 457–460: section/title metadata synchronized to Gate-3 authoritative `சில நாடுகள் இருக்கின்றன!`; source-facing poem wording was already correct.

The affected neighboring joins (405→406→407, 408→409→410, and 456→457→458→459→460→461) remain valid item boundaries/continuations. **Poem-body lexical changes: 0.** All six reopened records remain `verified`.

## Locked invariants applied

- only `verified` page records were eligible;
- 236→237→238→239 remains in physical order with its intentional A→B→A→B interposition;
- 370→371→372→373→374 remains in certified physical order, including blank/divider versos;
- dedicated divider/opening title forms remain authoritative;
- contents variants remain separate provenance witnesses in `indexes/canonical-source-map.md`;
- the page-293 opening for `நடந்திடுவேன் நமது அய்யா, அண்ணா வழியில்!` controls canonical provenance despite the contents page-279 locator;
- source-facing text is copied from verified page records; verification/physical-review/archive notes are not promoted into canonical Tamil text;
- no partial canonical item was emitted: the complete body interval was assembled in one Gate-4 pass.

## Gate closure

**Phase 3 Gate 4 is COMPLETE / PASS.**

## Exact next gate

Proceed to **Phase 3 Gate 5 — assembly/source-completeness review only**. Review the generated canonical output and provenance map against the verified page layer for one-time coverage, exclusions, title authority, source-order fidelity and silent-normalization risk. Do not grant Tamil final clearance or begin translation/release work in that same activity.
