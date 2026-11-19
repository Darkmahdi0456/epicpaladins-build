#!/usr/bin/env python3
"""Audit Epic Paladins recipe JSON syntax and internal item references."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent
RECIPE_DIR = ROOT / 'src/main/resources/data/epicpaladins/recipe'
MODEL_DIR = ROOT / 'src/main/resources/assets/epicpaladins/models/item'
JAVA_DIR = ROOT / 'src/main/java'
known = {p.stem for p in MODEL_DIR.glob('*.json')}
source = '\n'.join(p.read_text(errors='ignore') for p in JAVA_DIR.rglob('*.java'))
known.update(re.findall(r'"([a-z0-9_]+)"', source))
errors, types = [], {}
files = sorted(RECIPE_DIR.rglob('*.json'))
for path in files:
    try:
        data = json.loads(path.read_text())
    except Exception as exc:
        errors.append(f'{path.relative_to(RECIPE_DIR)}: invalid JSON: {exc}')
        continue
    recipe_type = data.get('type', 'MISSING')
    types[recipe_type] = types.get(recipe_type, 0) + 1
    for key in ('ingredient', 'addition', 'base', 'template'):
        value = data.get(key)
        if isinstance(value, dict):
            item = value.get('item')
            if item and item.startswith('epicpaladins:') and item.split(':', 1)[1] not in known:
                errors.append(f'{path.relative_to(RECIPE_DIR)}: unresolved {key} {item}')
    result = data.get('result')
    if isinstance(result, dict):
        item = result.get('id') or result.get('item')
        if item and item.startswith('epicpaladins:') and item.split(':', 1)[1] not in known:
            errors.append(f'{path.relative_to(RECIPE_DIR)}: unresolved result {item}')
print(f'Recipe files: {len(files)}')
for key, value in sorted(types.items()): print(f'{key}: {value}')
print(f'Errors: {len(errors)}')
for error in errors: print(error)
