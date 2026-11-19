#!/usr/bin/env python3
"""Static contract checks for Epic Paladins Fabric 1.21.4 armor rendering."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
JAVA = ROOT / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/item/GeoArmorItem.java'
RENDERER = ROOT / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/client/armor/ArmorGeoRenderer.java'
MODEL = ROOT / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/client/armor/ArmorGeoModel.java'
ITEMS = ROOT / 'src/main/resources/assets/epicpaladins/items'
MODELS = ROOT / 'src/main/resources/assets/epicpaladins/models'

item = JAVA.read_text()
renderer = RENDERER.read_text()
model = MODEL.read_text()
checks = []
def check(name, condition):
    checks.append((name, bool(condition)))

check('GeoItem implementation', 'implements GeoItem' in item)
check('GeckoLib 1.21+ createGeoRenderer hook', 'void createGeoRenderer(Consumer<GeoRenderProvider> consumer)' in item)
check('GeoRenderProvider override', 'getGeoArmorRenderer(' in item and '@Override' in item.split('getGeoArmorRenderer(')[0][-120:])
check('Renderer is lazily cached', 'private GeoArmorRenderer<?> renderer;' in item and 'if (this.renderer == null)' in item)
check('Renderer prepared for current equipment pass', 'prepForRender(livingEntity, itemStack, equipmentSlot, original)' in item)
check('Animatable cache exposed', 'getAnimatableInstanceCache()' in item)
check('Controller registration implemented', 'registerControllers(AnimatableManager.ControllerRegistrar controllers)' in item)
check('Renderer is client-only', '@Environment(EnvType.CLIENT)' in renderer)
check('Model is client-only', '@Environment(EnvType.CLIENT)' in model)
check('Set-specific model and texture lookup', 'ArmorGeoResources.get(armorSetId)' in model)

special_files = sorted(ITEMS.glob('*.json'))
check('36 special item definitions', len(special_files) == 36)
valid_special = 0
for path in special_files:
    try:
        data = json.loads(path.read_text())
        spec = data['model']
        valid = spec.get('type') == 'minecraft:special' and spec.get('model', {}).get('type') == 'geckolib:geckolib'
        base = spec.get('base', '')
        base_path = MODELS / (base.split(':', 1)[-1] + '.json')
        valid = valid and base_path.is_file()
        valid_special += int(valid)
    except Exception:
        pass
check('36 special definitions point to existing base models', valid_special == 36)

for name, ok in checks:
    print(('PASS' if ok else 'FAIL') + ' | ' + name)
print(f'SUMMARY | {sum(ok for _, ok in checks)}/{len(checks)} checks passed')
raise SystemExit(0 if all(ok for _, ok in checks) else 1)
