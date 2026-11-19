from pathlib import Path
import re, zipfile
root=Path(__file__).resolve().parent
jar=Path('/mnt/data/epicpaladins-1.4.3-1.21.1.jar')
reg=(root/'src/main/java/net/veroxuniverse/epicpaladins/fabric/ArmorItemsRegistry.java').read_text()
sets=re.findall(r'addSet\("([a-z0-9_]+)"',reg)
with zipfile.ZipFile(jar) as z:
    names=z.namelist()
    original=sorted(Path(n).stem.replace('ArmorItem','').lower() for n in names if n.startswith('net/veroxuniverse/epicpaladins/common/items/armorItems/') and n.endswith('ArmorItem.class') and '$' not in n and '/geckolib/' not in n)
    # exact original armor item implementation classes, excluding shared GeckoLib base class
expected=sorted(x for x in original if x not in {'paladin'})
assets=root/'src/main/resources/assets/epicpaladins'
manifest=(assets/'geo/armor_render_manifest.json').read_text()
manifest_sets=re.findall(r'"([a-z]+)"\s*:\s*\{\s*"geometry"',manifest)
print('Original armor item classes:', ', '.join(expected))
print('Fabric registered sets:', ', '.join(sets))
print('Geo manifest sets:', ', '.join(manifest_sets))
assert set(sets)==set(expected), f'Registry mismatch: missing={set(expected)-set(sets)}, extra={set(sets)-set(expected)}'
assert set(manifest_sets)==set(expected), f'Asset mismatch: missing={set(expected)-set(manifest_sets)}, extra={set(manifest_sets)-set(expected)}'
assert not (assets/'equipment/steel.json').exists()
print(f'PASS: all {len(expected)} original armor item classes match Fabric registrations and Geo assets; Steel remains an ingot/block material, not a fabricated armor set.')
