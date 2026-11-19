# Stage 13 — Creative tab integration

## Implemented
- Added a dedicated Fabric creative item group (`epicpaladins:main`).
- Added all currently registered item entries and block entries to the group.
- Connected the group registration to the mod initializer after content registration.
- Added the English display name.

## Important limitations
- This is a development source project, not a tested mod JAR.
- The existing registered armor/tools are still placeholder `Item` instances; this stage does not make them wearable or give tool stats.
- GeckoLib renderers, armor materials, recipes, loot tables, and ore world generation still require implementation/validation.
- Gradle compilation and in-game testing have not been run in this environment.

## Next stage
Implement and compile the first real wearable armor set against Minecraft 1.21.4 Yarn mappings, then test before scaling to the remaining sets.
