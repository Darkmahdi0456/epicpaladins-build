# Stage 42 — Original weapon behavior audit

## Scope
Inspected the original Epic Paladins 1.4.3 / Minecraft 1.21.1 NeoForge bytecode with `javap -p -c`. This stage is an evidence-based audit, not a claim that the Fabric port is complete.

## Confirmed findings
| Weapon | Original superclass | GeckoLib | Controllers | Client hook |
|---|---|---|---|---|
| Angel Sword | `net.minecraft.world.item.SwordItem` | `GeoItem` | `registerControllers` is empty | NeoForge `initializeClient` |
| Cryorium Axe | `net.minecraft.world.item.SwordItem` | `GeoItem` | `registerControllers` is empty | NeoForge `initializeClient` |
| Moonlight Glaive | `net.minecraft.world.item.SwordItem` | `GeoItem` | `registerControllers` is empty | NeoForge `initializeClient` |

Each constructor accepts a `Tier` and `Item.Properties`, calls the `SwordItem` constructor, and creates a `SingletonAnimatableInstanceCache`. Each class has a `getAnimatableInstanceCache()` accessor.

## Porting implications
1. These three named weapons are implemented as `SwordItem` in the original jar, including Cryorium Battle Axe. Do not silently substitute vanilla `AxeItem` behavior in the port.
2. Their original GeckoLib controller registration is empty. Their 3D appearance is supplied through custom GeoItem renderers, not through a controller animation setup visible in these classes.
3. Their `initializeClient` methods are NeoForge-specific and cannot be copied into Fabric. Fabric needs a separate client-side renderer registration path.
4. The current Fabric `ContentRegistry` still registers `angel_sword`, `moonlight_glaive`, and `cryorium_battle_axe` as generic `Item` placeholders. Therefore their combat behavior and GeoItem renderer chain are not yet ported.
5. Original `Tier` values and the registry's tier construction have not been fully mapped in this stage. Do not guess damage, speed, durability, or mining stats.

## Stage result
This audit establishes the correct behavioral baseline for implementing the three special weapons without inventing their original combat class. No weapon source classes were changed in this stage. No Gradle build or in-game test is claimed.
