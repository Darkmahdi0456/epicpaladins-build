# Stage 65 — GeckoLib armor item model definitions

- Added 36 Minecraft 1.21.4 item model definition JSON files under `assets/epicpaladins/items/` for the nine armor sets.
- Each definition selects Minecraft's special model with GeckoLib's `geckolib:geckolib` renderer type.
- Updated the 36 corresponding display model JSON files to use `builtin/entity` and the matching item particle texture.
- Existing armor geo models and armor textures were left unchanged.

Validation: parsed all 72 generated JSON files successfully and verified the expected 9 × 4 armor-piece coverage. Gradle compilation and in-game rendering were not run in this environment.
