#!/usr/bin/env python3
"""Compare registered armor sets with available Geo armor model/texture assets."""
import json, re, sys
from pathlib import Path
root = Path('src/main/resources/assets/epicpaladins')
java = Path('src/main/java/net/veroxuniverse/epicpaladins/fabric/ArmorItemsRegistry.java').read_text()
registered = set(re.findall(r'addSet\("([a-z0-9_]+)"', java))
manifest_path = root/'geo/armor_render_manifest.json'
manifest = json.loads(manifest_path.read_text())
listed = set(manifest['sets'])
errors=[]; missing=[]; extra=[]
for name in sorted(registered):
    geo = root/'geo'/f'{name}_armor.geo.json'
    tex = root/'textures/armor'/f'{name}_armor_textures.png'
    if name not in listed or not geo.is_file() or not tex.is_file():
        missing.append(name)
for name in sorted(listed-registered): extra.append(name)
for name, entry in manifest['sets'].items():
    for field in ('geometry','texture'):
        namespace, rel = entry[field].split(':',1)
        if namespace != 'epicpaladins': errors.append(f'{name}: unexpected namespace {namespace}')
        if not (root/rel).is_file(): errors.append(f'{name}: missing {field} {rel}')
print(f'Registered armor sets: {len(registered)} ({", ".join(sorted(registered))})')
print(f'Geo manifest sets: {len(listed)} ({", ".join(sorted(listed))})')
print('Missing model coverage: ' + (', '.join(missing) if missing else 'none'))
print('Manifest entries not registered: ' + (', '.join(extra) if extra else 'none'))
if errors:
    print('\n'.join('FAIL '+e for e in errors)); sys.exit(1)
if missing or extra: sys.exit(2)
print('PASS: every registered set has a manifest entry and both assets.')
