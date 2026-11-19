# Stage 74 — Armor renderer contract audit

- Added `tools_stage74_armor_renderer_contract.py` to validate the static wiring between `GeoArmorItem`, the GeckoLib render provider, the cached `ArmorGeoRenderer`, and per-set geometry/texture lookup.
- Verified the nine registered armor sets and all 36 special item JSON definitions.
- The audit checks source structure and JSON syntax only. It does not prove Java compilation, GeckoLib binary/API compatibility, or in-game rendering.
- A Gradle build could not be run in this environment: no Gradle executable or Gradle wrapper is present in the project directory.
