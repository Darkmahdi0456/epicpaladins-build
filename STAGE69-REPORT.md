# Stage 69 — Client-only armor rendering boundary

- Marked `GeoArmorItem.createGeoRenderer` as `@Environment(EnvType.CLIENT)` so the GeckoLib armor-render provider is explicitly client-only.
- Marked `ArmorGeoRenderer` and `ArmorGeoModel` as client-only classes.
- Kept item registration, armor-set identifiers, geometry/texture mapping, and armor attributes in common code.
- This narrows the dedicated-server classloading surface without changing armor assets or gameplay data.

Validation performed:
- Source-level checks confirm the client annotations are present on the provider method and both renderer/model classes.
- Static resource validation from Stage 68 remains available.

Limitations:
- Gradle compilation and dedicated-server/in-game execution were not possible in this environment because the GeckoLib Maven dependency could not be resolved here. This stage is not a claim of successful runtime verification.
