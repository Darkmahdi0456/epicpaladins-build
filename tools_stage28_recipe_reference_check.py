import json, re
from pathlib import Path
root = Path(__file__).resolve().parent
src = (root/'src/main/java/net/veroxuniverse/epicpaladins/fabric/ContentRegistry.java').read_text()
ids = set(re.findall(r'"([a-z0-9_]+)"', src))
recipes = list((root/'src/main/resources/data/epicpaladins/recipe').rglob('*.json'))
refs = set()
def walk(x):
    if isinstance(x, dict):
        for k,v in x.items():
            if k in ('item','id') and isinstance(v,str) and v.startswith('epicpaladins:'):
                refs.add(v.split(':',1)[1])
            walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
for f in recipes: walk(json.loads(f.read_text()))
missing = sorted(refs-ids)
print(f'Recipes parsed: {len(recipes)}')
print('Unregistered Epic Paladins recipe references:', missing)
raise SystemExit(bool(missing))
