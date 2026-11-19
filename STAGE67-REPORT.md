# Stage 67 — Per-frame armor renderer preparation

- Updated `GeoArmorItem` so its cached `GeoArmorRenderer` receives `prepForRender(livingEntity, itemStack, equipmentSlot, original)` on every armor-model request.
- This supplies the current wearer, stack, equipment slot, and original biped model to GeckoLib before the renderer is returned.
- Kept the renderer lazily instantiated and cached per armor item's provider.
- Scope is limited to armor rendering.

Static source audit: PASS — the provider still lazily creates the set-specific renderer and now prepares it before returning it.

Limitations: Gradle compilation and in-game rendering were not run in this environment, so mapped method compatibility and visual output remain unverified.
