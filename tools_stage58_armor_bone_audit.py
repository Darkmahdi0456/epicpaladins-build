import json, glob, os, sys
root='src/main/resources/assets/epicpaladins/geo'
files=sorted(glob.glob(os.path.join(root,'*_armor.geo.json')))
required={'armorHead','armorBody','armorLeftArm','armorRightArm','armorLeftLeg','armorRightLeg','armorLeftBoot','armorRightBoot'}
rows=[]
failed=[]
for path in files:
    data=json.load(open(path,encoding='utf-8'))
    geometry=data.get('minecraft:geometry') or []
    bones=geometry[0].get('bones',[]) if geometry else []
    names={b.get('name') for b in bones}
    missing=sorted(required-names)
    extras=sorted(n for n in names if n and n.startswith('bone'))
    rows.append((os.path.basename(path),len(names),missing,extras))
    if missing: failed.append(os.path.basename(path))
print(f'Armor geo files: {len(files)}')
for name,count,missing,extras in rows:
    print(f'{name}: bones={count}; missing={missing}; unnamed-decoration-bones={extras}')
if len(files)!=9 or failed:
    print('FAIL')
    sys.exit(1)
print('PASS: all nine models contain the eight core armor bone names')
