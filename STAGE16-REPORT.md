# Stage 16 — Complete armor registration coverage

## Changes
- Added Assassin and Knight armor sets to `ArmorItemsRegistry`.
- Updated the wearable-ID filter so their four pieces are not registered first as generic items.
- Steel armor pieces continue to be registered by the armor registry.

## Important limitations
- Assassin and Knight armor stats are provisional placeholders, not verified original balance values.
- Armor texture/equipment rendering is not connected yet. The original assets include GeckoLib geo/animation resources; ordinary ArmorItem does not automatically render those custom models.
- This stage has not been compiled or tested in Minecraft. It is source-project progress, not an installable mod JAR.
