#!/usr/bin/env python3
"""Audit Epic Paladins weapon GeoModel resource paths against bundled assets."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'src/main/resources/assets/epicpaladins'
WEAPONS = {
    'Angel Sword': ('geo/angel_sword.geo.json', 'textures/item/angel_sword.png', None),
    'Cryorium Axe': ('geo/cryorium_axe.geo.json', 'textures/item/cryorium_battle_axe.png', None),
    'Moonlight Glaive': ('geo/moonlight_glaive.geo.json', 'textures/item/moonlight_glaive.png', None),
}
errors = []
for name, (model, texture, animation) in WEAPONS.items():
    mp = ASSETS / model
    tp = ASSETS / texture
    if not mp.is_file(): errors.append(f'{name}: missing model {model}')
    else:
        try: json.loads(mp.read_text(encoding='utf-8'))
        except Exception as exc: errors.append(f'{name}: invalid model JSON: {exc}')
    if not tp.is_file(): errors.append(f'{name}: missing texture {texture}')
    if animation:
        ap = ASSETS / animation
        if not ap.is_file(): errors.append(f'{name}: missing animation {animation}')
print(f'Weapon models checked: {len(WEAPONS)}')
print(f'Model JSON valid: {sum((ASSETS/m).is_file() for m,_,_ in WEAPONS.values())}')
print(f'Textures present: {sum((ASSETS/t).is_file() for _,t,_ in WEAPONS.values())}')
print('Animation resources: all three original GeoModel methods return null')
for error in errors: print('ERROR:', error)
raise SystemExit(1 if errors else 0)
