from pathlib import Path
import re
root = Path(__file__).parent
build = (root / 'build.gradle').read_text(encoding='utf-8')
assert "geckolib-fabric-1.21.4:4.8" in build, 'Unexpected GeckoLib dependency'
geo = root / 'src/main/resources/assets/epicpaladins/geo'
textures = root / 'src/main/resources/assets/epicpaladins/textures/armor'
sets = ['angel','arclight','assassin','bloodstone','cryorium','jade','knight','moonlight','sculk']
for name in sets:
    model = geo / f'{name}_armor.geo.json'
    texture = textures / f'{name}_armor_textures.png'
    assert model.is_file(), f'Missing model: {model}'
    assert texture.is_file(), f'Missing texture: {texture}'
    raw = model.read_text(encoding='utf-8-sig')
    for bone in ('armorHead','armorBody','armorRightArm','armorLeftArm','armorRightLeg','armorLeftLeg'):
        assert f'"name": "{bone}"' in raw, f'{name}: missing expected bone {bone}'
print('PASS: GeckoLib dependency is 4.8 for Fabric 1.21.4')
print(f'PASS: {len(sets)} armor model/texture pairs exist')
print('PASS: expected humanoid armor bones exist in every model')
print('NOT TESTED: Java compilation, renderer registration, in-game rendering')
