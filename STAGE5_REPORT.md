# Epic Paladins Fabric 1.21.4 — Stage 5

## What changed
- Merged the extracted original `assets/epicpaladins` resource tree into `src/main/resources`.
- Preserved the existing Fabric project skeleton and data files from Stage 4.
- Preserved original model, animation, texture, item, blockstate, and related resource files where present in the extraction.

## Important status
This is a resource-integration stage, NOT a completed port and NOT a tested mod JAR.
The current Java registry still uses placeholder `Item` and `Block` instances. Armor equipment behavior, tool stats/behaviors, custom GeckoLib renderers, entity/weapon animation hooks, world generation, and any NeoForge-specific runtime logic still require porting.

## Next technical work
1. Inspect and port the original item/armor/tool registrations and their exact stats.
2. Implement Fabric-compatible armor materials/equipment definitions and tool materials for Minecraft 1.21.4.
3. Add item model JSONs and verify every texture/model path resolves.
4. Port GeckoLib renderers/animatable classes against the exact Fabric GeckoLib version.
5. Run Gradle compilation and test in a clean 1.21.4 Fabric instance before producing any installable JAR.

## License
Check the original mod's license and permissions before redistributing a modified build. This project is an unofficial compatibility effort.
