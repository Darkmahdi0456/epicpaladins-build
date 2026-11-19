#!/usr/bin/env python3
"""Static resource audit for Epic Paladins armor assets (Fabric 1.21.4)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent / "src/main/resources/assets/epicpaladins"
ERRORS = []
CHECKS = 0

for item_json in sorted((ROOT / "items").glob("*.json")):
    try:
        data = json.loads(item_json.read_text(encoding="utf-8"))
        CHECKS += 1
    except Exception as exc:
        ERRORS.append(f"Invalid JSON {item_json}: {exc}")
        continue
    model = data.get("model", {})
    if model.get("type") != "minecraft:special":
        ERRORS.append(f"Unexpected item model type: {item_json}")
    if model.get("model", {}).get("type") != "geckolib:geckolib":
        ERRORS.append(f"Missing GeckoLib special model: {item_json}")
    base = model.get("base", "")
    if not base.startswith("epicpaladins:item/"):
        ERRORS.append(f"Invalid base model identifier: {item_json}: {base}")
        continue
    name = base.split(":", 1)[1].split("/", 1)[1]
    base_model = ROOT / "models/item" / f"{name}.json"
    CHECKS += 1
    if not base_model.is_file():
        ERRORS.append(f"Missing base model: {base_model}")
        continue
    try:
        base_data = json.loads(base_model.read_text(encoding="utf-8"))
        CHECKS += 1
    except Exception as exc:
        ERRORS.append(f"Invalid base model JSON {base_model}: {exc}")
        continue
    for texture_id in base_data.get("textures", {}).values():
        if isinstance(texture_id, str) and texture_id.startswith("epicpaladins:"):
            texture_path = ROOT / "textures" / (texture_id.split(":", 1)[1] + ".png")
            CHECKS += 1
            if not texture_path.is_file():
                ERRORS.append(f"Missing referenced item texture: {texture_path}")

mapping = Path("src/main/java/net/veroxuniverse/epicpaladins/fabric/port/ArmorGeoResources.java").read_text(encoding="utf-8")
sets = re.findall(r'add\(sets, "([a-z]+)", "([a-z_]+)"\)', mapping)
for set_id, texture_name in sets:
    for relative in (f"geo/{set_id}_armor.geo.json", f"textures/armor/{texture_name}.png"):
        CHECKS += 1
        if not (ROOT / relative).is_file():
            ERRORS.append(f"Missing mapped armor resource: {relative}")
item_count = len(list((ROOT / "items").glob("*.json")))
if item_count != 36:
    ERRORS.append(f"Expected 36 armor item definitions, found {item_count}")

print(f"Armor resource checks: {CHECKS}")
print(f"Armor sets mapped: {len(sets)}")
print(f"Item definitions: {item_count}")
print(f"Errors: {len(ERRORS)}")
for error in ERRORS:
    print(f"ERROR: {error}")
sys.exit(1 if ERRORS else 0)
