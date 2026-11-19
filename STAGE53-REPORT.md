# Stage 53 — Equipment asset definitions

- Added Minecraft 1.21.4 equipment asset JSON files for all 10 registered armor material IDs.
- Each asset defines both `humanoid` and `humanoid_leggings` layers, matching the material asset keys used by `ArmorMaterialRegistry`.
- The layer texture deliberately uses the vanilla `minecraft:diamond` armor texture as a temporary fallback so the asset IDs resolve without pretending the Geo atlases are vanilla armor UV textures.
- Static validation passed for all 10 JSON files.

## Not completed
- This does not connect the original 3D Geo armor models or GeckoLib renderers.
- Assassin/Knight stats remain provisional.
- Gradle build and in-game verification were not run.
