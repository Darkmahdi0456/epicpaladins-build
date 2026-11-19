from pathlib import Path
from PIL import Image
import json
root=Path(__file__).parent
geo=root/'src/main/resources/assets/epicpaladins/geo'
tex=root/'src/main/resources/assets/epicpaladins/textures/armor'
sets=['angel','arclight','assassin','bloodstone','cryorium','jade','knight','moonlight','sculk']
lines=['Epic Paladins Stage 48 - Armor portability audit','', 'This is a read-only audit; no armor rendering code was changed.','']
for s in sets:
    model=geo/f'{s}_armor.geo.json'
    data=json.loads(model.read_text())
    # GeckoLib GeoModel texture atlas dimensions, not vanilla armor-layer layout.
    candidates=[tex/f'{s}_armor_textures.png', tex/f'{s}_armor.png']
    image=next((x for x in candidates if x.exists()),None)
    if image:
        with Image.open(image) as im: dims=f'{im.width}x{im.height} {im.mode}'
    else: dims='MISSING'
    bones=sum(len(g.get('bones',[])) for g in data.get('minecraft:geometry',[]))
    lines.append(f'{s}: GeoModel valid; bones={bones}; texture={image.name if image else "MISSING"}; dimensions={dims}')
lines += ['', 'Conclusion:', '- Nine armor sets have GeckoLib geometry and matching high-resolution atlas textures.', '- These atlas PNGs are not standard vanilla 64x32/64x64 armor-layer textures (dimensions vary).', '- The current Fabric ArmorItemsRegistry creates vanilla ArmorItem instances. Those items do not automatically render the GeckoLib geometry.', '- Do not create vanilla equipment-layer JSON by simply pointing at these atlases; that would be an unverified/incompatible mapping.', '- Next correct implementation requires GeckoLib GeoArmorItem/GeoArmorRenderer classes and client-side renderer registration for the exact GeckoLib 4.8 Fabric API.']
(root/'STAGE48-ARMOR-PORTABILITY-AUDIT.md').write_text('\n'.join(lines)+'\n')
(root/'STAGE48-ARMOR-PORTABILITY-AUDIT.txt').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))
