# Stage 15 — first wearable armor implementation

Implemented a first pass of 8 wearable armor sets (Arclight, Angel, Cryorium, Jade, Moonlight, Bloodstone, Sculk, Steel), replacing the generic placeholder registrations for those 32 item IDs with `ArmorItem` instances. Added 1.21.4 `ArmorMaterial` definitions, equipment slot defense maps, durability scaling, equipment asset keys, and item repair tags. `ContentRegistry` now skips those IDs during generic-item registration and registers the armor pieces instead.

## Important limits
- This is source code, not an installable mod JAR.
- It has NOT been compiled or tested in Minecraft. The exact 1.21.4 mappings and runtime behavior still need a Gradle build and game test.
- Armor durability multipliers and enchantability are provisional balancing values, not confirmed original values.
- Sculk repair ingredient is unresolved; its repair tag is intentionally empty.
- Assassin and Knight armor remain generic placeholders because no corresponding material data was verified in this stage.
- Original armor textures are GeckoLib/geo assets. Standard 1.21.4 equipment texture/model definitions are not yet connected, so the vanilla wearable renderer may not display the intended appearance yet.
