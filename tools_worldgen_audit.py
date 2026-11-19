#!/usr/bin/env python3
"""Audit Epic Paladins ore worldgen JSON before Fabric biome injection."""
import json, re
from pathlib import Path
ROOT = Path(__file__).parent
DATA = ROOT / 'src/main/resources/data/epicpaladins'
REG = ROOT / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/ContentRegistry.java'
source = REG.read_text(encoding='utf-8')
registered = set(re.findall(r'"([a-z0-9_]+)"', source))
errors=[]; rows=[]
for p in sorted((DATA/'worldgen/configured_feature').glob('*.json')):
    try: obj=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{p.name}: invalid JSON: {e}'); continue
    cfg=obj.get('config',{})
    targets=cfg.get('targets',[])
    blocks=[]
    for t in targets:
        name=t.get('state',{}).get('Name','')
        if name.startswith('epicpaladins:'):
            bid=name.split(':',1)[1]; blocks.append(bid)
            if bid not in registered: errors.append(f'{p.name}: block not found in ContentRegistry: {bid}')
    rows.append((p.stem, ', '.join(blocks), cfg.get('size','?')))
for p in sorted((DATA/'worldgen/placed_feature').glob('*.json')):
    try: obj=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{p.name}: invalid JSON: {e}'); continue
    feature=obj.get('feature','')
    if feature.startswith('epicpaladins:') and not (DATA/'worldgen/configured_feature'/ (feature.split(':',1)[1]+'.json')).exists():
        errors.append(f'{p.name}: configured feature missing: {feature}')
mods=list((DATA/'neoforge/biome_modifier').glob('*.json'))
print(f'Configured ores: {len(rows)}')
for name,blocks,size in rows: print(f'- {name}: size={size}; blocks={blocks}')
print(f'Placed features: {len(list((DATA/"worldgen/placed_feature").glob("*.json")))}')
print(f'NeoForge biome modifiers (not Fabric hooks): {len(mods)}')
for e in errors: print('ERROR:',e)
raise SystemExit(1 if errors else 0)
