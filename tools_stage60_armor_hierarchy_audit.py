import json, pathlib, sys
root = pathlib.Path('src/main/resources/assets/epicpaladins/geo')
files = sorted(root.glob('*_armor.geo.json'))
expected = {
 'armorHead':'bipedHead','armorBody':'bipedBody','armorLeftArm':'bipedLeftArm',
 'armorRightArm':'bipedRightArm','armorLeftLeg':'bipedLeftLeg','armorRightLeg':'bipedRightLeg',
 'armorLeftBoot':'bipedLeftLeg','armorRightBoot':'bipedRightLeg'
}
errors=[]; summaries=[]
for path in files:
    data=json.loads(path.read_text(encoding='utf-8'))
    geometries=data.get('minecraft:geometry')
    if not isinstance(geometries,list) or not geometries:
        errors.append(f'{path.name}: missing minecraft:geometry'); continue
    bones=geometries[0].get('bones',[])
    names=[b.get('name') for b in bones]
    if len(names)!=len(set(names)):
        errors.append(f'{path.name}: duplicate bone names')
    mapping={b.get('name'):b.get('parent') for b in bones}
    for name,parent in mapping.items():
        if parent and parent not in mapping:
            errors.append(f'{path.name}: {name} references missing parent {parent}')
        seen=set(); cur=name
        while cur in mapping and mapping[cur]:
            if cur in seen:
                errors.append(f'{path.name}: parent cycle at {cur}'); break
            seen.add(cur); cur=mapping[cur]
    if path.name == 'angel_armor.geo.json':
        # Angel uses a distinct wing/body-root layout; preserve and report it separately.
        required={'armorBody','Wings','armorLeftArm','armorRightArm','armorHead','armorLeftLeg','armorRightLeg'}
        missing=required-set(names)
        if missing: errors.append(f'{path.name}: missing special bones {sorted(missing)}')
        mode='special Angel hierarchy (wings)'
    else:
        for name,parent in expected.items():
            if name not in mapping: errors.append(f'{path.name}: missing {name}')
            elif mapping[name] != parent: errors.append(f'{path.name}: {name} parent is {mapping[name]!r}, expected {parent!r}')
        for name in ('bipedHead','bipedBody','bipedLeftArm','bipedRightArm','bipedLeftLeg','bipedRightLeg'):
            if name not in mapping: errors.append(f'{path.name}: missing anchor {name}')
        mode='standard humanoid hierarchy'
    summaries.append(f'- {path.stem}: {len(bones)} bones; {mode}')
report=['# Stage 60 — Armor hierarchy audit','',f'Geo armor files found: {len(files)}','',*summaries,'','## Validation',f'- Parent references and cycles checked for all {len(files)} files.',f'- Standard hierarchy checked for {len(files)-1} sets.', '- Angel checked with a separate wing-aware expected-bone set.','']
if errors:
    report += ['## Findings (not all passed)',*['- '+e for e in errors]]
else:
    report += ['- PASS: no missing parent references, duplicate names, or hierarchy cycles.','- PASS: all eight standard armor sets match their expected left/right body-bone parents.','- PASS: Angel special wing/body structure contains its expected key bones.']
report += ['', '## Limitations','This is a structural JSON audit only. It does not prove GeckoLib rendering, Java compilation, or in-game alignment.']
pathlib.Path('STAGE60-ARMOR-HIERARCHY-AUDIT.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('\n'.join(report))
if errors: sys.exit(1)
