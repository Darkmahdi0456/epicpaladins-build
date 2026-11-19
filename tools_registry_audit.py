#!/usr/bin/env python3
"""Static audit of Epic Paladins Fabric port registry IDs (no game launch)."""
from pathlib import Path
import re
p=Path("src/main/java/net/veroxuniverse/epicpaladins/fabric/ContentRegistry.java")
s=p.read_text(encoding="utf-8")
def ids(name):
 m=re.search(rf"{name}\s*=\s*\{{(.*?)\}};", s, re.S)
 if not m: raise SystemExit(f"Missing {name}")
 return re.findall(r'"([a-z0-9_]+)"', m.group(1))
items, blocks=ids("ITEM_IDS"), ids("BLOCK_IDS")
for label, values in (("items",items),("blocks",blocks)):
 dup=sorted({x for x in values if values.count(x)>1})
 if dup: raise SystemExit(f"Duplicate {label}: {dup}")
overlap=sorted(set(items)&set(blocks))
if overlap: raise SystemExit(f"Item/block ID overlap: {overlap}")
print(f"PASS: {len(items)} item IDs and {len(blocks)} block IDs; no duplicates or overlaps.")
print("NOTE: static registry audit only; does not compile or launch Minecraft.")
