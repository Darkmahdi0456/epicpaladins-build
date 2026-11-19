import json
from pathlib import Path
root = Path(__file__).parent / 'src/main/resources/assets/epicpaladins'
geo_dir = root / 'geo'
tex_dir = root / 'textures/armor'
models = sorted(geo_dir.glob('*_armor.geo.json'))
lines = ['Epic Paladins Stage 47 - Armor asset audit', '']
missing = []
for model in models:
    data = json.loads(model.read_text(encoding='utf-8'))
    geometries = data.get('minecraft:geometry', [])
    bones = sum(len(g.get('bones', [])) for g in geometries)
    stem = model.name.replace('.geo.json', '')
    candidates = [tex_dir / f'{stem}_textures.png', tex_dir / f'{stem}.png']
    found = next((p for p in candidates if p.is_file()), None)
    status = found.relative_to(root).as_posix() if found else 'MISSING TEXTURE'
    if not found:
        missing.append(stem)
    lines.append(f'{stem}: valid JSON; geometries={len(geometries)}; bones={bones}; texture={status}')
lines += ['', f'Model files checked: {len(models)}', f'Missing matching textures: {len(missing)}']
if missing:
    lines.append('Missing: ' + ', '.join(missing))
report = '\n'.join(lines) + '\n'
(Path(__file__).parent / 'STAGE47-ARMOR-ASSET-AUDIT.txt').write_text(report, encoding='utf-8')
(Path(__file__).parent / 'STAGE47-REPORT.md').write_text('''# Stage 47 — Armor asset audit\n\nThis stage audits armor GeoModel JSON resources and matching armor textures. It does not implement combat behavior or weapon features.\n\n'''+report, encoding='utf-8')
print(report)
