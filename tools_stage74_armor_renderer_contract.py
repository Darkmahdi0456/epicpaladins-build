#!/usr/bin/env python3
"""Static contract checks for Epic Paladins GeckoLib armor renderer wiring."""
from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parent
java = root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric'
item_src = (java / 'item/GeoArmorItem.java').read_text()
renderer_src = (java / 'client/armor/ArmorGeoRenderer.java').read_text()
model_src = (java / 'client/armor/ArmorGeoModel.java').read_text()
registry_src = (java / 'ArmorItemsRegistry.java').read_text()
checks = []
def check(name, ok):
    checks.append((name, bool(ok)))

check('GeoArmorItem implements GeoItem', 'extends ArmorItem implements GeoItem' in item_src)
check('Geo renderer provider implemented', 'void createGeoRenderer(Consumer<GeoRenderProvider> consumer)' in item_src)
check('Renderer lazily cached', 'private GeoArmorRenderer<?> renderer' in item_src and 'if (this.renderer == null)' in item_src)
check('Renderer prepared for each armor render', 'this.renderer.prepForRender(livingEntity, itemStack, equipmentSlot, original)' in item_src)
check('Animatable cache exposed', 'getAnimatableInstanceCache()' in item_src)
check('Armor renderer is client-only', '@Environment(EnvType.CLIENT)' in renderer_src)
check('Armor model is client-only', '@Environment(EnvType.CLIENT)' in model_src)
check('Renderer uses set-specific model', 'new ArmorGeoModel<>(armorSetId)' in renderer_src)
check('Model resolves geometry and texture', 'ArmorGeoResources.get(armorSetId)' in model_src and 'entry.model()' in model_src and 'entry.texture()' in model_src)
check('All nine sets registered', len(re.findall(r'addSet\("[a-z]+"', registry_src)) == 9)
items_dir = root / 'src/main/resources/assets/epicpaladins/items'
json_files = sorted(items_dir.glob('*.json'))
check('36 special item definitions exist', len(json_files) == 36)
valid_json = True
for f in json_files:
    try: json.loads(f.read_text())
    except Exception: valid_json = False
check('All special item definitions are valid JSON', valid_json)

for name, ok in checks:
    print(('PASS' if ok else 'FAIL') + ' | ' + name)
print(f'SUMMARY: {sum(ok for _, ok in checks)}/{len(checks)} passed')
sys.exit(0 if all(ok for _, ok in checks) else 1)
