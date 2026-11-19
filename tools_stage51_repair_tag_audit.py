#!/usr/bin/env python3
"""Validate armor repair tags against registered project items and vanilla IDs."""
import json, re
from pathlib import Path
root = Path(__file__).parent
src = root / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/ContentRegistry.java'
s = src.read_text(encoding='utf-8')
def ids(name):
    m = re.search(rf'{name}\s*=\s*\{{(.*?)\}};', s, re.S)
    if not m: raise SystemExit(f'Missing {name}')
    return set(re.findall(r'"([a-z0-9_]+)"', m.group(1)))
registered = ids('ITEM_IDS') | ids('BLOCK_IDS')
# Armor pieces are registered by ArmorItemsRegistry rather than ITEM_IDS.
for armor in ('arclight','angel','assassin','bloodstone','cryorium','jade','knight','moonlight','sculk','steel'):
    registered.update(armor + part for part in ('_helmet','_chestplate','_leggings','_boots'))
vanilla_known = {'echo_shard'}
errors=[]
files=sorted((root/'src/main/resources/data/epicpaladins/tags/item').glob('repairs_*.json'))
for p in files:
    data=json.loads(p.read_text(encoding='utf-8'))
    for value in data.get('values',[]):
        ns, name = value.split(':',1) if ':' in value else ('minecraft',value)
        if ns == 'epicpaladins' and name not in registered:
            errors.append(f'{p.name}: unregistered {value}')
        elif ns == 'minecraft' and name not in vanilla_known:
            errors.append(f'{p.name}: vanilla ID needs source verification: {value}')
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'PASS: {len(files)} armor repair tags; every project item is registered and vanilla echo_shard is recognized.')
