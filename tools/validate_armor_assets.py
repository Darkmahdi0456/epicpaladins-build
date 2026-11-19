#!/usr/bin/env python3
"""Static integrity check for Epic Paladins armor assets (no game/runtime required)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / 'src/main/resources/assets/epicpaladins'
JAVA = ROOT / 'src/main/java/net/veroxuniverse/epicpaladins/fabric'
SETS = ('arclight', 'assassin', 'knight', 'angel', 'cryorium', 'jade', 'moonlight', 'bloodstone', 'sculk')
PARTS = ('helmet', 'chestplate', 'leggings', 'boots')
errors = []
checks = 0

def require(ok, message):
    global checks
    checks += 1
    if not ok:
        errors.append(message)

registry = (JAVA / 'ArmorItemsRegistry.java').read_text(encoding='utf-8')
resources = (JAVA / 'port/ArmorGeoResources.java').read_text(encoding='utf-8')
for armor_set in SETS:
    require(f'addSet("{armor_set}"' in registry, f'missing registered armor set: {armor_set}')
    model = RES / 'geo' / f'{armor_set}_armor.geo.json'
    texture = RES / 'textures/armor' / f'{armor_set}_armor_textures.png'
    require(model.is_file(), f'missing geometry: {model.relative_to(ROOT)}')
    require(texture.is_file(), f'missing texture: {texture.relative_to(ROOT)}')
    require(f'add(sets, "{armor_set}", "{armor_set}_armor_textures")' in resources,
            f'ArmorGeoResources mapping mismatch: {armor_set}')
    if model.is_file():
        try:
            data = json.loads(model.read_text(encoding='utf-8'))
            require(bool(data.get('minecraft:geometry')), f'geometry has no minecraft:geometry: {armor_set}')
        except Exception as exc:
            errors.append(f'invalid geometry JSON {armor_set}: {exc}')
    for part in PARTS:
        item = f'{armor_set}_{part}'
        special = RES / 'items' / f'{item}.json'
        vanilla = RES / 'models/item' / f'{item}.json'
        require(special.is_file(), f'missing GeckoLib item definition: {item}')
        require(vanilla.is_file(), f'missing base item model: {item}')
        if special.is_file():
            try:
                data = json.loads(special.read_text(encoding='utf-8'))
                node = data.get('model', {})
                require(node.get('type') == 'minecraft:special', f'wrong special model type: {item}')
                require(node.get('model', {}).get('type') == 'geckolib:geckolib', f'wrong GeckoLib model type: {item}')
                require(node.get('base') == f'epicpaladins:item/{item}', f'wrong base model reference: {item}')
            except Exception as exc:
                errors.append(f'invalid item JSON {item}: {exc}')

print(f'Armor asset checks: {checks}')
print(f'Armor sets: {len(SETS)}; armor pieces expected: {len(SETS)*len(PARTS)}')
if errors:
    print(f'FAIL: {len(errors)} issue(s)')
    for error in errors:
        print(' -', error)
    sys.exit(1)
print('PASS: all armor registration, geometry, texture, special-item and base-model links are present.')
