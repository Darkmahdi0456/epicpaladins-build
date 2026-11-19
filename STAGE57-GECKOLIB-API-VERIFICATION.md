# Epic Paladins Stage 57 — GeckoLib 4.8 API verification

## Scope
This stage verifies the target library/API boundary before adding armor renderer code. It does **not** claim that armor is rendered in-game.

## Verified target
- Minecraft: 1.21.4
- Loader: Fabric
- GeckoLib dependency in `build.gradle`: `software.bernie.geckolib:geckolib-fabric-1.21.4:4.8`
- The published GeckoLib 4.8 release explicitly targets Fabric 1.21.4.

## Verified GeckoLib 4.8 source API
The GeckoLib 1.21.4 source branch confirms:
- `GeoModel<T extends GeoAnimatable>` requires `getModelResource(T, GeoRenderer<T>)`, `getTextureResource(T, GeoRenderer<T>)`, and `getAnimationResource(T)`.
- `GeoArmorRenderer<T extends Item & GeoItem>` is the armor-specific renderer base class.
- `GeoArmorRenderer` expects standard bone names such as `armorHead`, `armorBody`, `armorRightArm`, `armorLeftArm`, `armorRightLeg`, `armorLeftLeg`, `armorRightBoot`, and `armorLeftBoot` unless overridden.

## Important compatibility finding
The source API shape in GeckoLib 4.8 is not interchangeable with current GeckoLib 5 examples. Do not copy GeckoLib 5 `HumanoidRenderState` examples into this 1.21.4 project.

## Blocker before implementation
The GeckoLib 4.8 binary dependency is not present in the local Gradle cache in this environment, and Gradle/build tooling is unavailable. Therefore the Fabric-side `GeoRenderProvider` registration signatures and item integration cannot be compiled/verified here. This stage intentionally does not add speculative imports or renderer hooks that could break the project.

## Existing project state
- The nine original armor Geo JSON files and their texture atlases remain in `src/main/resources/assets/epicpaladins/`.
- `ArmorItemsRegistry` still creates vanilla `ArmorItem` instances; they do not yet implement `GeoItem`.
- Armor rendering remains incomplete and must not be described as working.

## References
- GeckoLib 4.8 release page: https://modrinth.com/mod/geckolib/version/4.8
- GeckoLib 1.21.4 `GeoArmorRenderer.java`: https://raw.githubusercontent.com/bernie-g/geckolib/1.21.4/common/src/main/java/software/bernie/geckolib/renderer/GeoArmorRenderer.java
- GeckoLib 1.21.4 `GeoModel.java`: https://raw.githubusercontent.com/bernie-g/geckolib/1.21.4/common/src/main/java/software/bernie/geckolib/model/GeoModel.java
