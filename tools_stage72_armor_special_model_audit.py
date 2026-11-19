#!/usr/bin/env python3
"""Static audit for GeckoLib special item-model definitions of armor pieces."""
from pathlib import Path
import json, re
ROOT = Path(__file__).resolve().parent
ASSET = ROOT / 'src/main/resources/assets/epicpaladins'
REG = (ROOT / 'src/main/java/net/veroxuniverse/epicpaladins/fabric/ArmorItemsRegistry.java').read_text(encoding='utf-8')
sets = re.findall(r'addSet\("([a-z0-9_]+)"', REG)
suffixes = ('helmet', 'chestplate', 'leggings', 'boots')
checks = []
expected = {f'{s}_{p}' for s in sets for p in suffixes}
actual = {p.stem for p in (ASSET/'items').glob('*.json')}
checks.append(('9 sets generate exactly 36 expected special item definitions', len(sets)==9 and expected <= actual and len(expected)==36))
checks.append(('no unexpected special armor item definitions', actual == expected))
for name in sorted(expected):
    p = ASSET/'items'/f'{name}.json'
    model = ASSET/'models/item'/f'{name}.json'
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
        spec = data['model']
        ok = (spec['type']=='minecraft:special' and
              spec['base']==f'epicpaladins:item/{name}' and
              spec['model']['type']=='geckolib:geckolib' and model.is_file())
    except Exception:
        ok = False
    checks.append((f'{name}: special definition + base model', ok))
print('Stage 72 — armor special item model audit')
for label, ok in checks:
    print(('PASS ' if ok else 'FAIL ')+label)
print(f'SUMMARY {sum(ok for _,ok in checks)}/{len(checks)}')
if not all(ok for _,ok in checks):
    raise SystemExit(1)
