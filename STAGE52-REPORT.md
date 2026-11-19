# Stage 52 — Correct recovered armor material values

## Actual code changes
- Corrected the eight original material durability factors to `20`, matching each `ArmorMaterial` constructor in the original NeoForge 1.21.1 bytecode.
- Corrected the shared armor equip sound from iron to diamond, matching the original material factories.
- Updated the recovered Sculk material specification to record `minecraft:echo_shard` as its repair ingredient, confirmed by the original bytecode and Stage 51 audit.
- Preserved the per-material defense, toughness, and knockback values recovered earlier.

## Validation
`tools_stage52_armor_material_audit.py` passed for all eight original material definitions.

## Important limits
The audit is static. No Gradle build or in-game test was performed. Assassin and Knight entries in the port are not among the eight original `ArmorMaterialsRegistry` materials and remain provisional pending inspection of their original item registration paths. GeckoLib armor rendering and special armor effects remain unimplemented.
