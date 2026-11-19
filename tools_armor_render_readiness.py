#!/usr/bin/env python3
"""Audit Epic Paladins armor Geo models and texture atlases before renderer work."""
import json, pathlib, re, sys
root = pathlib.Path(__file__).parent
assets = root / 'src/main/resources/assets/epicpaladins'
geo_dir = assets / 'geo'
tex_dir = assets / 'textures/armor'
models = sorted(geo_dir.glob('*_armor.geo.json'))
lines = ['Epic Paladins armor render readiness audit', '']
errors = []
for model in models:
    try:
        data = json.loads(model.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{model.name}: invalid JSON: {exc}')
        continue
    name = model.name.removesuffix('_armor.geo.json')
    texture_candidates = [tex_dir / f'{name}_armor_textures.png', tex_dir / f'{name}_armor.png']
    found = [p for p in texture_candidates if p.exists()]
    geo_format = data.get('format_version', 'unknown')
    geometry = data.get('minecraft:geometry', [])
    bone_count = sum(len(g.get('bones', [])) for g in geometry if isinstance(g, dict))
    lines.append(f'{name}: JSON OK; format={geo_format}; geometries={len(geometry)}; bones={bone_count}; texture=' + (', '.join(p.name for p in found) if found else 'MISSING'))
    if not found:
        errors.append(f'{name}: no matching armor atlas found')
lines += ['', f'Models checked: {len(models)}', f'Problems: {len(errors)}']
if errors:
    lines += [''] + ['- ' + e for e in errors]
(root / 'STAGE21-ARMOR-RENDER-AUDIT.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines))
sys.exit(1 if errors else 0)
