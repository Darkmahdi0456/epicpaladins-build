#!/usr/bin/env python3
"""Audit Epic Paladins datapack recipes for JSON syntax and referenced mod IDs."""
import json, pathlib, re
ROOT = pathlib.Path(__file__).parent
DATA = ROOT / 'src/main/resources/data/epicpaladins'
ASSETS = ROOT / 'src/main/resources/assets/epicpaladins'
recipes = sorted((DATA/'recipe').rglob('*.json')) if (DATA/'recipe').exists() else []
errors=[]; refs=[]
for p in recipes:
    try: obj=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append(f'{p.relative_to(ROOT)}: invalid JSON: {e}'); continue
    if not isinstance(obj,dict) or 'type' not in obj:
        errors.append(f'{p.relative_to(ROOT)}: missing top-level recipe type')
    for s in re.findall(r'epicpaladins:[a-z0-9_./-]+', json.dumps(obj)):
        refs.append((p,s))
missing=[]
for p,s in refs:
    name=s.split(':',1)[1]
    # Items/blocks are represented by model or blockstate assets in this port.
    if not ((ASSETS/'models/item'/f'{name}.json').exists() or (ASSETS/'blockstates'/f'{name}.json').exists()):
        # Tags are allowed to be datapack references, not direct assets.
        if '/tags/' not in name and not name.startswith('tags/'):
            missing.append(f'{p.relative_to(ROOT)} -> {s}')
report=[f'Recipe files found: {len(recipes)}',f'Valid JSON recipes: {len(recipes)-len(errors)}',f'Internal epicpaladins references: {len(refs)}',f'Potential missing asset references: {len(missing)}',f'Errors: {len(errors)}']
report += ['','Potential missing references:'] + (missing[:100] or ['None detected by this limited asset check.'])
report += ['','JSON/type errors:'] + (errors or ['None'])
(ROOT/'STAGE27-RECIPE-AUDIT.txt').write_text('\n'.join(report)+'\n',encoding='utf-8')
print('\n'.join(report[:5]))
