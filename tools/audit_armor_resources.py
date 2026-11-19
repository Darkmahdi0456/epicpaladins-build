#!/usr/bin/env python3
"""Static integrity audit for Epic Paladins armor assets (no Minecraft runtime)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src/main/resources/assets/epicpaladins"
SETS = ("arclight", "angel", "assassin", "bloodstone", "cryorium", "jade", "knight", "moonlight", "sculk")
PARTS = ("helmet", "chestplate", "leggings", "boots")
errors = []
checks = 0

def require(path, label):
    global checks
    checks += 1
    if not path.is_file():
        errors.append(f"Missing {label}: {path}")

for armor_set in SETS:
    geo = ROOT / "geo" / f"{armor_set}_armor.geo.json"
    texture = ROOT / "textures" / "armor" / f"{armor_set}_armor_textures.png"
    require(geo, f"geometry for {armor_set}")
    require(texture, f"texture for {armor_set}")
    if geo.is_file():
        try:
            data = json.loads(geo.read_text(encoding="utf-8"))
            checks += 1
            if not isinstance(data.get("minecraft:geometry"), list) or not data["minecraft:geometry"]:
                errors.append(f"Invalid geometry root: {geo}")
        except Exception as exc:
            errors.append(f"Invalid geometry JSON {geo}: {exc}")
    for part in PARTS:
        name = f"{armor_set}_{part}"
        item_json = ROOT / "items" / f"{name}.json"
        base_model = ROOT / "models" / "item" / f"{name}.json"
        require(item_json, f"special item definition {name}")
        require(base_model, f"base item model {name}")
        if item_json.is_file():
            try:
                data = json.loads(item_json.read_text(encoding="utf-8"))
                checks += 1
                model = data["model"]
                if model.get("type") != "minecraft:special" or model.get("model", {}).get("type") != "geckolib:geckolib":
                    errors.append(f"Unexpected special model schema: {item_json}")
                expected = f"epicpaladins:item/{name}"
                if model.get("base") != expected:
                    errors.append(f"Wrong base model id in {item_json}: {model.get('base')}")
            except Exception as exc:
                errors.append(f"Invalid item JSON {item_json}: {exc}")

empty_anim = ROOT / "animations" / "armor" / "empty.animation.json"
require(empty_anim, "empty armor animation")
if empty_anim.is_file():
    try:
        json.loads(empty_anim.read_text(encoding="utf-8"))
        checks += 1
    except Exception as exc:
        errors.append(f"Invalid empty animation JSON: {exc}")

print(f"Checks: {checks}")
print(f"Errors: {len(errors)}")
for error in errors:
    print("ERROR:", error)
raise SystemExit(1 if errors else 0)
