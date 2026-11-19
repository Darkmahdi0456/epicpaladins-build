# Epic Paladins Fabric 1.21.4 — Stage 3

This is an unofficial work-in-progress port scaffold. Stage 3 adds Fabric registry code for the item and block identifiers recovered from the original NeoForge JAR.

**Important limitations:** this stage registers generic placeholder items and blocks only. It does NOT yet reproduce original armor stats/models, tool tiers/behaviors, weapon attacks, effects, world generation, loot tables, recipes correctness, GeckoLib animations, or the original creative tab. Do not treat this as a complete or tested replacement mod.

Target: Minecraft 1.21.4, Fabric Loader, Fabric API, Java 21.

Build with a compatible Gradle installation using `gradle build`.


## Stage 6
Run `python3 tools_resource_audit.py` from the project root to validate JSON and item/block model texture references. See `STAGE6-REPORT.md`. This is an asset validation step, not a completed or tested mod build.


## Stage 7
Bytecode inspection report added as `STAGE7-REPORT.md`. This is reverse-engineering research only; no armor gameplay or renderer implementation is claimed, and no successful build has been verified.

## Stage 14 status
An initial ArmorMaterialRegistry scaffold has been added. It is not yet wired to armor item IDs and has not been compiled or tested. Armor stats and repair ingredients are placeholders.
