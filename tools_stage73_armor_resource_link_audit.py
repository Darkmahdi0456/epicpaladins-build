#!/usr/bin/env python3
"""Static path/reference audit for Epic Paladins armor resources."""
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'src/main/resources/assets/epicpaladins'
JAVA = ROOT / 'src/main/java/net/veroxuniverse/epicpaladins/fabric'
sets = ['arclight','assassin','knight','angel','cryorium','jade','moonlight','bloodstone','sculk']
slots = ['helmet','chestplate','leggings','boots']
errors=[]; checks=0

def require(ok, msg):
    global checks
    checks += 1
    if not ok: errors.append(msg)

# Item special-model references must resolve to the matching ordinary item model.
for armor_set in sets:
    for slot in slots:
        item_id=f'{armor_set}_{slot}'
        special=ASSETS/'items'/f'{item_id}.json'
        base=ASSETS/'models/item'/f'{item_id}.json'
        require(special.is_file(), f'missing special item definition: {special}')
        require(base.is_file(), f'missing base item model: {base}')
        if special.is_file():
            try:
                data=json.loads(special.read_text())
                model=data['model']
                require(model.get('type')=='minecraft:special', f'{item_id}: wrong wrapper type')
                require(model.get('base')==f'epicpaladins:item/{item_id}', f'{item_id}: wrong base model id')
                require(model.get('model',{}).get('type')=='geckolib:geckolib', f'{item_id}: wrong special renderer type')
            except Exception as exc: errors.append(f'{item_id}: invalid JSON/schema ({exc})')
            checks += 1

# Geo model and texture files must resolve for each registered armor set.
resources=(JAVA/'port/ArmorGeoResources.java').read_text()
for armor_set in sets:
    geo=ASSETS/'geo'/f'{armor_set}_armor.geo.json'
    require(geo.is_file(), f'missing geo model: {geo.name}')
    match=re.search(r'add\(sets,\s*"'+re.escape(armor_set)+r'",\s*"([^"]+)"\)', resources)
    require(match is not None, f'{armor_set}: no texture mapping in ArmorGeoResources')
    if match:
        texture=ASSETS/'textures/armor'/f'{match.group(1)}.png'
        require(texture.is_file(), f'{armor_set}: missing mapped texture {texture.name}')
        require('\"epicpaladins:geo/\" + id + \"_armor.geo.json\"' in resources, f'{armor_set}: geo path builder missing')

# Registered set ids and resource map should be the same nine-set collection.
registry=(JAVA/'ArmorItemsRegistry.java').read_text()
registered=set(re.findall(r'addSet\("([a-z]+)"', registry))
mapped=set(re.findall(r'add\(sets,\s*"([a-z]+)"', resources))
require(registered==set(sets), f'registered set mismatch: {sorted(registered)}')
require(mapped==set(sets), f'resource set mismatch: {sorted(mapped)}')

print(f'Armor resource-link audit: {checks} checks, {len(errors)} errors')
for err in errors: print('ERROR:',err)
sys.exit(1 if errors else 0)
