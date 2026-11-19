# Stage 37 — Weapon renderer bytecode audit

Source inspected: original `epicpaladins-1.4.3-1.21.1.jar` using `javap -p -c`.

## Confirmed renderer chain

| Item | NeoForge item extension | Geo item renderer | Geo model |
|---|---|---|---|
| Angel Sword | `AngelSwordItem$1` | `AngelSwordRenderer` | `AngelSwordModel` |
| Cryorium Axe | `CryoriumAxeItem$1` | `CryoriumAxeRenderer` | `CryoriumAxeModel` |
| Moonlight Glaive | `MoonlightGlaiveItem$1` | `MoonlightGlaiveRenderer` | `MoonlightGlaiveModel` |

Each renderer constructor creates its corresponding model and passes it to `GeoItemRenderer`'s constructor. Each NeoForge extension lazily creates and returns the renderer from `getCustomRenderer()`.

## Porting implication

The renderer/model classes are not themselves NeoForge extensions, but the item-side `initializeClient` bridge is NeoForge-specific. Fabric needs a client initializer and Fabric/GeckoLib-supported item renderer registration. Do not copy `IClientItemExtensions` or `getCustomRenderer()` into the Fabric source set.

## Not yet confirmed

This audit does not inspect every model method's resource locations or prove compatibility with GeckoLib 4.7.3 / Minecraft 1.21.4. It also does not implement renderer registration, compile the project, or test rendering in-game.

## Next implementation task

Inspect the three `*Model` classes' `getModelResource`, `getTextureResource`, and `getAnimationResource` methods; verify each referenced asset exists; then implement Fabric client-side renderer registration against the exact GeckoLib 4.7.3 Fabric API available to this project.
