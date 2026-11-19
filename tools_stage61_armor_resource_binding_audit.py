#!/usr/bin/env python3
"""Validate the canonical Geo armor resource map against packaged assets."""
import re
from pathlib import Path

ROOT = Path(__file__).parent
JAVA = ROOT / "src/main/java/net/veroxuniverse/epicpaladins/fabric/port/ArmorGeoResources.java"
text = JAVA.read_text(encoding="utf-8")
entries = re.findall(r'add\(sets, "([a-z]+)", "([a-z_]+)"\);', text)
assert len(entries) == 9, f"Expected 9 original sets, found {len(entries)}"
assert len({name for name, _ in entries}) == 9, "Duplicate armor set id"
for armor_id, texture_name in entries:
    model = ROOT / f"src/main/resources/assets/epicpaladins/geo/{armor_id}_armor.geo.json"
    texture = ROOT / f"src/main/resources/assets/epicpaladins/textures/armor/{texture_name}.png"
    assert model.is_file(), f"Missing model: {model}"
    assert texture.is_file(), f"Missing texture: {texture}"
print(f"PASS: {len(entries)} armor resource mappings resolve to existing GeoJSON + PNG assets")
print("PASS: unique set IDs; model paths and texture paths use the expected assets namespace")
