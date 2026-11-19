# Stage 10 — Armor data recovery (corrected from original bytecode)

This stage recovers the actual armor material values from the original `ArmorMaterialsRegistry` bytecode. It is reverse-engineering data, not yet a Fabric implementation or a successful build.

## Important correction to Stage 9

The Stage 9 table paired several material names with the wrong lambda factories. The correct mapping is established by the `static {}` initializer and the factory method's armor-layer name:

| Material | Armor layer id | Defense (boots / leggings / chestplate / helmet) | Toughness | Knockback resistance | Repair ingredient reference |
|---|---|---:|---:|---:|---|
| Arclight | `arclight` | 5 / 8 / 10 / 5 | 4.0 | 0.2 | `ARCLIGHT_GEM` |
| Angel | `angel` | 7 / 9 / 14 / 8 | 5.0 | 0.3 | `ARCLIGHT_GEM` |
| Cryorium | `cryorium` | 5 / 8 / 10 / 5 | 4.0 | 0.2 | `CRYORIUM_GEM` |
| Jade | `jade` | 5 / 8 / 10 / 5 | 3.5 | 0.5 | `JADE_GEM` |
| Moonlight | `moonlight` | 5 / 8 / 10 / 5 | 4.5 | 0.1 | `MOONLIGHT_GEM` |
| Bloodstone | `bloodstone` | 5 / 8 / 10 / 5 | 4.0 | 0.3 | `BLOODSTONE_GEM` |
| Sculk | `sculk` | 6 / 8 / 9 / 5 | 5.0 | 0.1 | Not yet confirmed from the extracted snippet; inspect lambda 19 |
| Steel | `steel` | 3 / 4 / 6 / 3 | 1.5 | 0.2 | `STEEL_INGOT` |

All recovered material factories use `ARMOR_EQUIP_DIAMOND`. The armor layer namespace is `epicpaladins`.

## What this establishes

- Eight armor materials are defined in the original bytecode.
- Exact defense values per slot are recovered.
- Toughness and knockback resistance are recovered.
- Repair ingredient references are recovered for seven materials; Sculk still needs confirmation.

## Still not implemented

- Fabric `ArmorMaterial` registration for 1.21.4.
- Four real wearable `ArmorItem`s per material.
- Armor layer/model rendering and texture validation in-game.
- Special armor effects, recipes, loot, and full gameplay parity.
- A successful Gradle build or Minecraft launch test.

## Next step

Implement the eight `ArmorMaterial` entries using the target project's exact 1.21.4 Yarn API, then register the wearable armor pieces. Verify the mapping against the actual 1.21.4 Fabric API before compiling.
