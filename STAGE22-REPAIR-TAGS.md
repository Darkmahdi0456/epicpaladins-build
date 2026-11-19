# Stage 22 — Armor repair tags

Added one Minecraft item tag per armor material, matching `repairs_<id>` used by `ArmorMaterialRegistry`.

## Provisional choices
The repair ingredients for angel, assassin, knight, and sculk are not confirmed from original game behavior. They are provisional mappings and must be verified before calling the port faithful. Other tags use the matching gem/ingot ID.

## Scope
This stage adds data JSON only. It does not implement GeckoLib armor rendering, equipment asset JSON, or prove the mod builds. Run Gradle build and in-game tests before installation.
