from pathlib import Path

path = Path("poems/kalaignarin-kavithaigal/translations/en/batches/batch-10.md")
text = path.read_text(encoding="utf-8")
old = "Final reviewed blob SHAs will be appended after mechanical certification."
new = """## Final reviewed item blob witnesses

These are the exact item blobs certified after `status` promotion to `batch-reviewed`:

- item 36 final blob: `e5879a1691cdfaec5327604ad1500bf039742c50`;
- item 37 final blob: `908b7f985a5f235bf6b6642253775415dcd3ea65`;
- item 38 final blob: `7c41cfaf10317e99751dd22a53bd52a58e6b214a`;
- item 39 final blob: `76ee0a21530df9c8bdc5e8e943c205aeeebcf097`;
- item 40 final blob: `27768a59b175118f75b5eeaaec66dec7e07d828b`."""
if old not in text:
    raise SystemExit("Batch 10 final-blob placeholder not found")
for sha in [
    "e5879a1691cdfaec5327604ad1500bf039742c50",
    "908b7f985a5f235bf6b6642253775415dcd3ea65",
    "7c41cfaf10317e99751dd22a53bd52a58e6b214a",
    "76ee0a21530df9c8bdc5e8e943c205aeeebcf097",
    "27768a59b175118f75b5eeaaec66dec7e07d828b",
]:
    if len(sha) != 40:
        raise SystemExit("invalid blob SHA length")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
