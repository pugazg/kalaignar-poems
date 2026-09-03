from pathlib import Path

p = Path('HANDOVER.md')
s = p.read_text()

assert '## Durable state after Phase 4 Batch 04' in s
s = s.replace('## Durable state after Phase 4 Batch 04', '## Durable state after Phase 4 Batch 05', 1)

start = s.index('## Phase 4 durable result — Batch 04')
end = s.index('## Phase 4 durable result — Batch 05', start)
block = s[start:end]
assert '- reviewed batches: **5**;' in block
assert '- reviewed English items: **15/77**;' in block
assert '- reviewed item-assigned source scans: **153/439**;' in block
block = block.replace('- reviewed batches: **5**;', '- reviewed batches: **4**;', 1)
block = block.replace('- reviewed English items: **15/77**;', '- reviewed English items: **10/77**;', 1)
block = block.replace('- reviewed item-assigned source scans: **153/439**;', '- reviewed item-assigned source scans: **106/439**;', 1)
s = s[:start] + block + s[end:]

assert 'the latest reviewed translation batch record (`translations/en/batches/batch-04.md`)' in s
s = s.replace('the latest reviewed translation batch record (`translations/en/batches/batch-04.md`)', 'the latest reviewed translation batch record (`translations/en/batches/batch-05.md`)', 1)

p.write_text(s)

# Make the completed Batch-05 certificate read as completed rather than prospective.
bp = Path('poems/kalaignarin-kavithaigal/translations/en/batches/batch-05.md')
b = bp.read_text()
b = b.replace('The finalizer must verify exact marker sequences:', 'The finalizer verified these exact marker sequences:', 1)
b = b.replace('It must also confirm:', 'It also confirmed:', 1)
bp.write_text(b)

# Scope and durable-history checks.
s = p.read_text()
assert '## Durable state after Phase 4 Batch 05' in s
start = s.index('## Phase 4 durable result — Batch 04')
end = s.index('## Phase 4 durable result — Batch 05', start)
block = s[start:end]
assert '- reviewed batches: **4**;' in block
assert '- reviewed English items: **10/77**;' in block
assert '- reviewed item-assigned source scans: **106/439**;' in block
assert 'batch-05.md' in s[s.index('## Mandatory startup'):]
assert 'items 16–20' in s[s.index('## EXACT NEXT ACTIVITY'):]

for q in [Path('.github/workflows/batch05-doc-fix.yml'), Path('scripts/batch05_doc_fix.py')]:
    if q.exists():
        q.unlink()
