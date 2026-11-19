#!/usr/bin/env python3
"""Audit Epic Paladins resource JSON and model texture references."""
import os, json, sys
root=sys.argv[1] if len(sys.argv)>1 else "src/main/resources/assets/epicpaladins"
errors=[]; count=0; refs=0
for dp,_,fs in os.walk(root):
 for fn in fs:
  if not fn.endswith(".json"): continue
  p=os.path.join(dp,fn); count+=1
  try: obj=json.load(open(p,encoding="utf-8"))
  except Exception as e: errors.append(f"Invalid JSON: {p}: {e}"); continue
  if "/models/" in p.replace("\\","/") and isinstance(obj,dict):
   for key,val in obj.get("textures",{}).items():
    if isinstance(val,str) and val.startswith("epicpaladins:"):
     refs+=1; rel=val.split(":",1)[1]+".png"; tex=os.path.join(root,"textures",rel)
     if not os.path.isfile(tex): errors.append(f"Missing texture: {p} -> {val}")
print(f"JSON files: {count}; texture refs: {refs}; problems: {len(errors)}")
for e in errors: print(e)
sys.exit(1 if errors else 0)
