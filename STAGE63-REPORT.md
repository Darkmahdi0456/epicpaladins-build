# Stage 63 — GeckoLib-aware armor item registration

## Implemented
- Added `GeoArmorItem`, an `ArmorItem` subclass implementing GeckoLib `GeoItem`.
- Added a per-item `AnimatableInstanceCache` and the required controller registration hook.
- Changed all 36 armor pieces across the nine original sets to use `GeoArmorItem`.
- Stored the armor-set ID on each piece so the later client renderer binding can select the correct geometry and texture.
- Kept renderer creation out of common initialization to avoid loading client renderer classes on a dedicated server.

## Validation
- Static source audit confirms all 36 registered armor pieces use `GeoArmorItem`.
- Static source audit confirms nine armor-set registrations and the model/texture lookup ID is derived from each registered piece ID.

## Not completed
- The GeckoLib `GeoRenderProvider` has not yet been attached to the item instances.
- No Gradle compilation or in-game test was run; dependency resolution is unavailable in this environment.
- Therefore this stage makes the items GeckoLib-aware but does not yet make the 3D armor render in-game.
