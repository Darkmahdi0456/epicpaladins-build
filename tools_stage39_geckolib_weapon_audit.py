#!/usr/bin/env python3
"""Static audit of Epic Paladins weapon Geo assets; does not compile or render them."""
import json
from pathlib import Path
ROOT = Path(__file__).parent
ASSETS = ROOT / 'src/main/resources/assets/epicpaladins'
WEAPONS = {
    'Angel Sword': ('geo/angel_sword.geo.json', 'textures/item/angel_sword.png'),
    'Cryorium Axe': ('geo/cryorium_axe.geo.json', 'textures/item/cryorium_battle_axe.png'),
    'Moonlight Glaive': ('geo/moonlight_glaive.geo.json', 'textures/item/moonlight_glaive.png'),
}
errors=[]
for name,(geo,texture) in WEAPONS.items():
    gp,tp=ASSETS/geo,ASSETS/texture
    if not gp.is_file(): errors.append(f'{name}: missing {geo}')
    else:
        try:
            data=json.loads(gp.read_text(encoding='utf-8'))
            geometries=data.get('minecraft:geometry')
            if not isinstance(geometries,list) or not geometries: errors.append(f'{name}: no minecraft:geometry array')
            else:
                for i,g in enumerate(geometries):
                    if not g.get('description',{}).get('identifier'): errors.append(f'{name}: geometry {i} has no identifier')
                    if not isinstance(g.get('bones'),list): errors.append(f'{name}: geometry {i} has no bones array')
        except Exception as e: errors.append(f'{name}: invalid JSON: {e}')
    if not tp.is_file(): errors.append(f'{name}: missing texture {texture}')
print('Epic Paladins weapon Geo asset audit')
print('Scope: static file/JSON checks only; no Fabric renderer or runtime test.')
for name in WEAPONS: print(f'- {name}: checked')
print(f'Errors: {len(errors)}')
for e in errors: print('ERROR:',e)
raise SystemExit(1 if errors else 0)
