# Stage 62 — GeckoLib armor model and renderer classes

## Implemented
- Added a generic GeckoLib 4 `ArmorGeoModel<T extends Item & GeoItem>` adapter.
- The model resolves geometry and texture through the canonical nine-set `ArmorGeoResources` map.
- Added a shared `ArmorGeoRenderer<T>` extending GeckoLib's `GeoArmorRenderer<T>`.
- Added a valid empty animation resource because the original armor models do not define armor animations.
- Kept these classes under a client package; common item registration is unchanged.

## Validation
- Static audit passed for all nine geometry files.
- Empty animation JSON parsed successfully.
- Source signatures and resource map references checked.

## Not completed
- Armor item classes do not yet implement `GeoItem`.
- The renderer provider is not yet attached to registered armor items.
- No Gradle compilation or in-game rendering test was possible in this environment. Treat this as renderer-class scaffolding, not working in-game armor rendering.
