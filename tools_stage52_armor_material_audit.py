#!/usr/bin/env python3
"""Static audit for armor values recovered from original Epic Paladins bytecode."""
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parent
reg=(root/'src/main/java/net/veroxuniverse/epicpaladins/fabric/ArmorItemsRegistry.java').read_text()
mat=(root/'src/main/java/net/veroxuniverse/epicpaladins/fabric/ArmorMaterialRegistry.java').read_text()
spec=(root/'src/main/java/net/veroxuniverse/epicpaladins/fabric/port/ArmorMaterialSpec.java').read_text()
expected={
'arclight':(20,5,10,8,5,20,4.0,0.2),
'angel':(20,8,14,9,7,20,5.0,0.3),
'cryorium':(20,5,10,8,5,20,4.0,0.2),
'jade':(20,5,10,8,5,20,3.5,0.5),
'moonlight':(20,5,10,8,5,20,4.5,0.1),
'bloodstone':(20,5,10,8,5,20,4.0,0.3),
'sculk':(20,5,9,8,6,20,5.0,0.1),
'steel':(20,3,6,4,3,20,1.5,0.2),
}
errors=[]
for name, vals in expected.items():
    pat=rf'addSet\("{name}",\s*([^;]+)\);'
    m=re.search(pat,reg)
    if not m:
        errors.append(f'{name}: missing addSet')
        continue
    got=tuple(float(x.strip().rstrip('f')) for x in m.group(1).split(','))
    if got != vals: errors.append(f'{name}: expected {vals}, got {got}')
if 'SoundEvents.ITEM_ARMOR_EQUIP_DIAMOND' not in mat: errors.append('wrong armor equip sound')
if 'minecraft:echo_shard' not in spec: errors.append('Sculk repair ingredient missing from recovered spec')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('8 original armor material definitions checked: PASS')
print('Durability factor: 20 for all 8')
print('Equip sound: diamond')
print('Sculk repair ingredient: minecraft:echo_shard')
