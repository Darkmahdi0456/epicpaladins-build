# Stage 68 — Armor resource-link validation

- Added `tools/validate_armor_assets.py`, a repeatable static validator for the armor rendering resource chain.
- The validator checks all 9 registered armor sets and all 36 armor pieces.
- It verifies each set's geometry JSON and texture file, the `ArmorGeoResources` mapping, and each piece's GeckoLib special item JSON plus vanilla base item model.
- It also parses JSON files and validates the expected `minecraft:special`, `geckolib:geckolib`, and base-model references.

Result: **225 checks passed**.

Limitations: this is a static resource audit only. It does not prove Gradle compilation, GeckoLib runtime compatibility, or in-game rendering. Those still require a successful dependency-resolved build and Minecraft test.
