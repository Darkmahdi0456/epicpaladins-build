# Stage 64 — Connect GeckoLib armor renderer

## Implemented
- `GeoArmorItem` now supplies a lazy `GeoRenderProvider` through GeckoLib's 1.21.1+ armor hook.
- Each armor item creates the shared `ArmorGeoRenderer` with its own armor-set id, so the nine sets resolve their own geometry and texture through `ArmorGeoResources`.
- The renderer remains lazy and is not instantiated during common item registration.

## Scope
This stage changes armor rendering only. No weapon behavior or assets were changed.

## Verification
- Static source audit: provider hook, lazy renderer cache, set-id routing, and all nine registered armor sets are present.
- Build and in-game rendering were not verified because the required Gradle dependency repository is unavailable in this environment. The new GeckoLib/Yarn method signature therefore still needs a real Gradle compile check.
