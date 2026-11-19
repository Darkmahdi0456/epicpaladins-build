# Stage 76 — Armor resource reference audit

- Added `tools_stage76_armor_resource_audit.py` for repeatable static validation.
- Parsed all 36 GeckoLib special item-definition JSON files.
- Verified all 36 base item-model references and their particle texture files.
- Verified all 9 armor geometry paths and all 9 armor texture paths listed in `ArmorGeoResources`.
- Result: 162 checks, 0 missing references or malformed JSON files.

Scope: armor resources only. This is a static file audit, not a Java/Gradle build or an in-game rendering test. No claim of runtime success is made.
