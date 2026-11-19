#!/usr/bin/env python3
import json
from pathlib import Path
root = Path(__file__).parent
model = root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/client/armor/ArmorGeoModel.java'
renderer = root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/client/armor/ArmorGeoRenderer.java'
anim = root / 'src/main/resources/assets/epicpaladins/animations/armor/empty.animation.json'
resources = root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/port/ArmorGeoResources.java'
assert model.is_file() and renderer.is_file() and resources.is_file()
json.loads(anim.read_text())
m = model.read_text(); r = renderer.read_text()
for signature in ('getModelResource', 'getTextureResource', 'getAnimationResource'):
    assert signature in m
assert 'ArmorGeoResources.get(armorSetId)' in m
assert 'extends GeoArmorRenderer<T>' in r
assert 'new ArmorGeoModel<>(armorSetId)' in r
ids = ['arclight','angel','assassin','bloodstone','cryorium','jade','knight','moonlight','sculk']
for set_id in ids:
    geo = root / f'src/main/resources/assets/epicpaladins/geo/{set_id}_armor.geo.json'
    assert geo.is_file(), geo
print(f'PASS: shared GeoModel/GeoArmorRenderer source scaffold and {len(ids)} original armor geometry files')
print('PASS: empty animation resource JSON')
print('NOTE: item GeoItem integration and runtime rendering are not part of this stage')
