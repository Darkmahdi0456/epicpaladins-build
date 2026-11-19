#!/usr/bin/env python3
"""Audit English localization keys against registered Epic Paladins content IDs."""
import json, re
from pathlib import Path
root = Path(__file__).parent
src = root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/ContentRegistry.java'
lang = root / 'src/main/resources/assets/epicpaladins/lang/en_us.json'
text = src.read_text(encoding='utf-8')
data = json.loads(lang.read_text(encoding='utf-8'))
# Extract literal IDs from the two registry arrays.
item_section = text.split('private static final String[] ITEM_IDS = {',1)[1].split('};',1)[0]
block_section = text.split('private static final String[] BLOCK_IDS = {',1)[1].split('};',1)[0]
items = re.findall(r'"([a-z0-9_]+)"', item_section)
blocks = re.findall(r'"([a-z0-9_]+)"', block_section)
expected = {f'item.epicpaladins.{x}' for x in items} | {f'block.epicpaladins.{x}' for x in blocks}
# Include creative tab key.
expected.add('itemGroup.epicpaladins.main')
missing = sorted(expected - data.keys())
extra = sorted(data.keys() - expected)
report = [f'Registered item IDs scanned: {len(items)}', f'Registered block IDs scanned: {len(blocks)}', f'Expected English keys: {len(expected)}', f'Existing English keys: {len(data)}', f'Missing keys: {len(missing)}']
if missing: report += ['','MISSING:'] + missing
report += ['', f'Extra English keys: {len(extra)}']
if extra: report += ['','EXTRA:'] + extra
(root/'STAGE33-LOCALIZATION-AUDIT.txt').write_text('\n'.join(report)+'\n', encoding='utf-8')
print('\n'.join(report))
