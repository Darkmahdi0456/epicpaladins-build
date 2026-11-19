# Stage 9 — Armor material reverse-engineering map

This stage records the armor material definitions recovered from the original JAR's `ArmorMaterialsRegistry` bytecode. It does **not** yet implement armor items in Fabric.

## Confirmed material-to-factory mapping

The class static initializer assigns these factory methods to the corresponding fields:

| Material field | Factory method | Recovered toughness | Recovered knockback resistance |
|---|---:|---:|---:|
| ARCLIGHT | lambda$static$23 | 1.5 | 0.2 |
| ANGEL | lambda$static$20 | 5.0 | 0.1 |
| CRYORIUM | lambda$static$17 | 4.0 | 0.3 |
| JADE | lambda$static$14 | 4.5 | 0.1 |
| MOONLIGHT | lambda$static$11 | 3.5 | 0.5 |
| BLOODSTONE | lambda$static$8 | 4.0 | 0.2 |
| SCULK | lambda$static$5 | 5.0 | 0.3 |
| STEEL | lambda$static$2 | 4.0 | 0.2 |

All eight factory methods use the `epicpaladins` namespace and armor equip diamond sound in the recovered bytecode. Defense values per armor slot and repair ingredients still need to be transcribed and checked against the full method bodies before coding.

## Important correction / status

Earlier stages created a preliminary Fabric project with placeholder `Item` registrations and copied resource files. That is not a complete port. The current `ContentRegistry` still registers armor and tools as generic items, so they do not behave as wearable armor or functional tools. Several earlier bytecode extraction attempts also produced empty/error files; only `ArmorMaterialsRegistry.javap.txt` is confirmed non-empty in the current Stage 8 workspace.

## Next implementation work

1. Recover exact defense maps and repair ingredients for all eight materials.
2. Implement Fabric/Yarn 1.21.4 `ArmorMaterial` definitions and actual `ArmorItem` instances.
3. Add armor item models, layer textures and client renderer registration as needed.
4. Compile with Gradle and fix mapping/API errors.
5. Test in a clean 1.21.4 Fabric instance before calling any JAR installable.

No build or in-game test is claimed in this stage.
