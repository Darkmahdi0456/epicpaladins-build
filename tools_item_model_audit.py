#!/usr/bin/env python3
"""Audit Epic Paladins item model JSON files and referenced local textures."""
import json
from pathlib import Path
ROOT = Path(__file__).parent
ASSETS = ROOT / 'src/main/resources/assets'
models = sorted(ASSETS.glob('*/models/item/*.json'))
errors, refs = [], 0
for model in models:
    try:
        data = json.loads(model.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{model}: invalid JSON: {exc}')
        continue
    textures = data.get('textures', {})
    if not isinstance(textures, dict):
        errors.append(f'{model}: textures is not an object')
        continue
    for key, value in textures.items():
        if not isinstance(value, str) or ':' not in value or value.startswith('#'):
            continue
        namespace, path = value.split(':', 1)
        texture = ASSETS / namespace / 'textures' / (path + '.png')
        refs += 1
        if not texture.is_file():
            errors.append(f'{model}: missing texture {value} ({texture})')
print(f'Item model JSON files: {len(models)}')
print(f'Local texture references checked: {refs}')
print(f'Errors: {len(errors)}')
for error in errors:
    print('ERROR:', error)
raise SystemExit(1 if errors else 0)
