# Stage 38 — Weapon model and texture resource audit

Inspected the original 1.21.1 NeoForge JAR's compiled `AngelSwordModel`, `CryoriumAxeModel`, and `MoonlightGlaiveModel` using `javap -p -c`.

| Weapon | Geo model | Texture | Animation method |
|---|---|---|---|
| Angel Sword | `geo/angel_sword.geo.json` | `textures/item/angel_sword.png` | returns `null` |
| Cryorium Axe | `geo/cryorium_axe.geo.json` | `textures/item/cryorium_battle_axe.png` | returns `null` |
| Moonlight Glaive | `geo/moonlight_glaive.geo.json` | `textures/item/moonlight_glaive.png` | returns `null` |

All three model JSON files parse, and all three exact texture paths exist in the extracted assets. In particular, the Cryorium Axe texture path is `cryorium_battle_axe.png` (not `cryorium_axe.png`); that file is present.

No animation JSON is referenced by these three model classes: each `getAnimationResource(...)` returns `null`. This is evidence that these GeoModels do not supply an animation resource, not proof that the held weapon has no other behavior.

The audit script is `tools_stage38_weapon_resource_audit.py`. This is a resource-path audit only. It does not implement Fabric renderer registration, compile the project, or test rendering in Minecraft.
