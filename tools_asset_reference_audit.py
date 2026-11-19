#!/usr/bin/env python3
"""Check Epic Paladins JSON syntax and in-namespace model/texture references."""
import json
from pathlib import Path

ASSETS = Path(__file__).parent / 'src/main/resources/assets/epicpaladins'
errors = []
json_count = 0

def walk(value, source):
    if isinstance(value, dict):
        parent = value.get('parent')
        if isinstance(parent, str) and ':' in parent:
            namespace, path = parent.split(':', 1)
            if namespace == 'epicpaladins' and not (ASSETS / 'models' / f'{path}.json').is_file():
                errors.append(f'{source}: missing model parent {parent}')
        textures = value.get('textures')
        if isinstance(textures, dict):
            for texture in textures.values():
                if isinstance(texture, str) and ':' in texture:
                    namespace, path = texture.split(':', 1)
                    if namespace == 'epicpaladins' and not (ASSETS / 'textures' / f'{path}.png').is_file():
                        errors.append(f'{source}: missing texture {texture}')
        for child in value.values():
            walk(child, source)
    elif isinstance(value, list):
        for child in value:
            walk(child, source)

for file in ASSETS.rglob('*.json'):
    json_count += 1
    try:
        data = json.loads(file.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{file}: invalid JSON: {exc}')
        continue
    walk(data, file)

print(f'JSON files checked: {json_count}')
print(f'Reference/parse errors: {len(errors)}')
for error in errors:
    print(error)
raise SystemExit(1 if errors else 0)
