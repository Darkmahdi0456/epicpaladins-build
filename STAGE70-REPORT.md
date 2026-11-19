# Stage 70 — Armor resource compatibility audit

- Added `tools/audit_armor_resources.py` to validate the nine armor geometry/texture pairs, all 36 GeckoLib special item definitions, their base item model files, and the shared empty animation resource.
- Confirmed every special item definition points to its matching `epicpaladins:item/<armor_piece>` base model and uses the expected `minecraft:special` / `geckolib:geckolib` structure.
- Ran the audit: **137 checks, 0 errors**.

Limitations:
- This is a static resource audit only. It does not establish successful Java compilation, GeckoLib runtime compatibility, or in-game rendering. Gradle compilation remains unverified in this environment.
- This stage changes no gameplay or weapon behavior; it only adds armor-resource validation tooling.
