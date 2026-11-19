#!/usr/bin/env python3
"""Validate that every prepared armor Geo model points to an existing texture and parses."""
import json
from pathlib import Path
from PIL import Image
ROOT = Path('src/main/resources/assets/epicpaladins')
manifest = json.loads((ROOT/'geo/armor_render_manifest.json').read_text())
errors=[]; rows=[]
for name, entry in manifest['sets'].items():
    geo_rel = entry['geometry'].split(':',1)[1]
    tex_rel = entry['texture'].split(':',1)[1]
    geo_path = ROOT/geo_rel
    tex_path = ROOT/tex_rel
    if not geo_path.is_file(): errors.append(f'{name}: missing geometry {geo_path}'); continue
    if not tex_path.is_file(): errors.append(f'{name}: missing texture {tex_path}'); continue
    try:
        geo=json.loads(geo_path.read_text())
        geometry=geo['minecraft:geometry'][0]
        desc=geometry['description']
        bones=geometry['bones']
        with Image.open(tex_path) as im: tex_size=im.size
        declared=(desc['texture_width'], desc['texture_height'])
        if not bones: errors.append(f'{name}: no bones')
        rows.append((name, desc.get('identifier','?'), len(bones), declared, tex_size))
    except Exception as exc:
        errors.append(f'{name}: invalid data: {exc}')
if errors:
    print('\n'.join('FAIL '+e for e in errors)); raise SystemExit(1)
print(f'PASS: {len(rows)} armor geometry/texture pairs exist and parse.')
for name, ident, bones, declared, actual in rows:
    note='MATCH' if declared==actual else f'SCALE/UV REVIEW (geo {declared}, png {actual})'
    print(f'{name}: id={ident}; bones={bones}; {note}')
