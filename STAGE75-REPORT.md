# Stage 75 — GeckoLib armor API contract audit

- Added `tools_stage75_geckolib_api_audit.py` to check the armor item's GeckoLib 1.21+ provider hook, lazy renderer creation, `prepForRender` call, animation cache/controller methods, and client-only renderer/model annotations.
- Rechecked all 36 `minecraft:special` item definitions, their `geckolib:geckolib` model type, and the existence of each corresponding base item model.
- This is a source/resource contract audit only. It does not establish Java compilation, binary compatibility against the resolved GeckoLib JAR, or successful rendering in Minecraft.
- Build remains unverified because this environment has no Gradle wrapper/executable and dependency access is unavailable.
