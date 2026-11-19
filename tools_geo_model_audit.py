#!/usr/bin/env python3
"""Validate basic structure of Epic Paladins armor geometry JSON files."""
import json
from pathlib import Path
root = Path(__file__).parent / 'src/main/resources/assets/epicpaladins/geo'
files = sorted(root.glob('*_armor.geo.json'))
errors = []
for path in files:
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
        geometries = data.get('minecraft:geometry')
        if not isinstance(geometries, list) or not geometries:
            errors.append(f'{path.name}: missing minecraft:geometry array'); continue
        for index, geometry in enumerate(geometries):
            desc = geometry.get('description', {})
            if not desc.get('identifier'):
                errors.append(f'{path.name}[{index}]: missing geometry identifier')
            if not isinstance(geometry.get('bones'), list) or not geometry['bones']:
                errors.append(f'{path.name}[{index}]: missing bones')
    except Exception as exc:
        errors.append(f'{path.name}: {exc}')
print(f'Armor geometry files checked: {len(files)}')
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print('Basic JSON/geometry structure: OK')
