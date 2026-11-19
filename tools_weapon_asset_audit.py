import json
from pathlib import Path
root=Path(__file__).parent/'src/main/resources/assets/epicpaladins'
geo=root/'geo'; tex=root/'textures/item'
report=[]
for name in ('angel_sword','cryorium_axe','moonlight_glaive'):
 p=geo/(name+'.geo.json')
 if not p.exists(): report.append(f'{name}: GEO MISSING'); continue
 try:
  d=json.loads(p.read_text(encoding='utf-8'))
  geos=d.get('minecraft:geometry',[])
  bones=sum(len(g.get('bones',[])) for g in geos)
  cubes=sum(len(b.get('cubes',[])) for g in geos for b in g.get('bones',[]))
  report.append(f'{name}: JSON OK; geometries={len(geos)}; bones={bones}; cubes={cubes}')
 except Exception as e: report.append(f'{name}: JSON ERROR: {e}')
for name in ('angel_sword','cryorium_axe','moonlight_glaive','arclight_axe','bloodstone_axe'):
 p=tex/(name+'.png')
 report.append(f'{name} item texture: '+('FOUND' if p.exists() else 'MISSING'))
out='\n'.join(report)+'\n'
(Path(__file__).parent/'STAGE23-WEAPON-ASSET-AUDIT.txt').write_text(out,encoding='utf-8')
print(out)
