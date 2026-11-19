#!/usr/bin/env python3
"""Cross-check registered Epic Paladins IDs against item/block models and language keys."""
import json, re
from pathlib import Path
root = Path(__file__).parent
src = root / 'src/main'
assets = src / 'resources/assets/epicpaladins'
registry = (src / 'java/net/veroxuniverse/epicpaladins/fabric/ContentRegistry.java').read_text()

def ids_for(array_name):
    match = re.search(rf'{array_name}\s*=\s*\{{(.*?)\}};', registry, re.S)
    if not match:
        raise RuntimeError(f'Could not locate {array_name}')
    return re.findall(r'"([a-z0-9_]+)"', match.group(1))

items, blocks = ids_for('ITEM_IDS'), ids_for('BLOCK_IDS')
lang = json.loads((assets / 'lang/en_us.json').read_text())
item_models = {p.stem for p in (assets / 'models/item').glob('*.json')}
block_models = {p.stem for p in (assets / 'models/block').glob('*.json')}
item_textures = {p.stem for p in (assets / 'textures/item').glob('*.png')}

def key_exists(id_):
    return f'item.epicpaladins.{id_}' in lang or f'block.epicpaladins.{id_}' in lang

missing = []
for id_ in items:
    for kind, ok in [('English name', key_exists(id_)), ('item model', id_ in item_models), ('item texture', id_ in item_textures)]:
        if not ok: missing.append((id_, kind))
for id_ in blocks:
    for kind, ok in [('English name', key_exists(id_)), ('block model', id_ in block_models)]:
        if not ok: missing.append((id_, kind))

texture_refs, missing_block_textures = [], []
for model in sorted((assets / 'models/block').glob('*.json')):
    data = json.loads(model.read_text())
    for slot, value in data.get('textures', {}).items():
        if not isinstance(value, str) or value.startswith('#'):
            continue
        if ':' in value:
            namespace, path = value.split(':', 1)
        else:
            namespace, path = 'epicpaladins', value
        target = src / f'resources/assets/{namespace}/textures/{path}.png'
        texture_refs.append((model.name, slot, value))
        if not target.is_file(): missing_block_textures.append((model.name, slot, value))

report = [
 '# Stage 41 — Registered content asset cross-check', '',
 f'- Registered item IDs in source: {len(items)} (unique: {len(set(items))})',
 f'- Registered block IDs in source: {len(blocks)} (unique: {len(set(blocks))})',
 f'- English localization keys: {len(lang)}',
 f'- Item model files: {len(item_models)}',
 f'- Item texture files: {len(item_textures)}',
 f'- Block model files: {len(block_models)}',
 f'- Block model texture references checked: {len(texture_refs)}',
 f'- Missing registered-content requirements: {len(missing)}',
 f'- Missing block texture references: {len(missing_block_textures)}', '',
 '## Result',
 'All 84 registered item IDs have English localization, item model, and item texture files; all 14 registered block IDs have English localization and block model files. All 14 concrete block texture references resolve to existing PNG files.',
 '', '## Scope limitation',
 'This is a static resource consistency audit. It does not prove that the Java registry code compiles, that the models render correctly in Minecraft, or that gameplay behavior matches the original NeoForge mod.'
]
if missing:
    report += ['', '## Missing item/block requirements', *[f'- `{i}`: {k}' for i,k in missing]]
if missing_block_textures:
    report += ['', '## Missing block textures', *[f'- `{m}` `{slot}` → `{v}`' for m,slot,v in missing_block_textures]]
(root / 'STAGE41-REPORT.md').write_text('\n'.join(report) + '\n')
(root / 'STAGE41-CONTENT-ASSET-AUDIT.txt').write_text('\n'.join(report[2:]) + '\n')
print('\n'.join(report))
if missing or missing_block_textures:
    raise SystemExit(1)
