from pathlib import Path
root = Path(__file__).parent
item = (root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/item/GeoArmorItem.java').read_text()
renderer = (root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/client/armor/ArmorGeoRenderer.java').read_text()
model = (root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/client/armor/ArmorGeoModel.java').read_text()
checks = {
    'provider method client-only': '@Environment(EnvType.CLIENT)' in item and 'void createGeoRenderer' in item,
    'renderer class client-only': '@Environment(EnvType.CLIENT)' in renderer,
    'model class client-only': '@Environment(EnvType.CLIENT)' in model,
    'common item still implements GeoItem': 'implements GeoItem' in item,
    'common armor resource map remains independent': (root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/port/ArmorGeoResources.java').exists(),
}
for label, ok in checks.items():
    print(('PASS' if ok else 'FAIL') + ': ' + label)
if not all(checks.values()):
    raise SystemExit(1)
print(f'{len(checks)} checks passed')
