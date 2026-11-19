import json
from pathlib import Path
root=Path(__file__).parent
sets=['arclight','assassin','knight','angel','cryorium','jade','moonlight','bloodstone','sculk','steel']
base=root/'src/main/resources/assets/epicpaladins/equipment'
for name in sets:
    p=base/f'{name}.json'
    assert p.is_file(), f'missing {p}'
    data=json.loads(p.read_text())
    assert set(data['layers']) == {'humanoid','humanoid_leggings'}
    assert data['layers']['humanoid'][0]['texture']=='minecraft:diamond'
    assert data['layers']['humanoid_leggings'][0]['texture']=='minecraft:diamond'
print(f'PASS: {len(sets)} equipment assets are valid JSON and cover body + leggings layers.')
print('NOTE: vanilla diamond texture is a temporary fallback; original Geo/GeckoLib armor rendering is not connected.')
