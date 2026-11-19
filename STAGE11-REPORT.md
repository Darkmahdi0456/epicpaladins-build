# Stage 11 — Armor data model prepared

## Added
- `ArmorMaterialSpec.java`: a Java 21 record containing the eight recovered armor-material definitions.
- The data is kept independent of Minecraft classes so it can be checked before binding it to the exact Yarn 1.21.4 API.

## Recovered values
Defense order in the data record is boots / leggings / chestplate / helmet.

| Material | Defense | Toughness | Knockback resistance | Repair item |
|---|---:|---:|---:|---|
| Arclight | 5 / 8 / 10 / 5 | 4.0 | 0.2 | arclight_gem |
| Angel | 7 / 9 / 14 / 8 | 5.0 | 0.3 | arclight_gem |
| Cryorium | 5 / 8 / 10 / 5 | 4.0 | 0.2 | cryorium_gem |
| Jade | 5 / 8 / 10 / 5 | 3.5 | 0.5 | jade_gem |
| Moonlight | 5 / 8 / 10 / 5 | 4.5 | 0.1 | moonlight_gem |
| Bloodstone | 5 / 8 / 10 / 5 | 4.0 | 0.3 | bloodstone_gem |
| Sculk | 6 / 8 / 9 / 5 | 5.0 | 0.1 | not confirmed |
| Steel | 3 / 4 / 6 / 3 | 1.5 | 0.2 | steel_ingot |

## Important limits
- This stage does **not** register wearable armor items yet.
- The Sculk repair ingredient remains explicitly unconfirmed.
- The project has not been compiled or launched in Minecraft. No installable JAR is produced.
- Previous stages are preparation/reverse-engineering artifacts; they should not be described as a finished or tested port.

## Next stage
Bind these records to Minecraft 1.21.4's `ArmorMaterial` and `ArmorItem` APIs, then verify against the exact Yarn mappings and run a Gradle build. Only after a successful build should an in-game test be attempted.
