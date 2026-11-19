# Stage 49 — Armor implementation audit (Minecraft 1.21.4 Fabric)

## Verified against the original Epic Paladins 1.4.3 JAR

The original mod contains nine GeckoLib armor model/renderer pairs:
- Angel
- Arclight
- Assassin
- Bloodstone
- Cryorium
- Jade
- Knight
- Moonlight
- Sculk

The original shared base class is `common/items/armorItems/geckolib/PaladinArmorItem`, which extends `ArmorItem` and implements `GeoItem`. Each armor renderer extends `GeoArmorRenderer<SpecificArmorItem>`.

The Steel set is not among the nine GeckoLib armor model/renderer pairs in the original JAR. Do not incorrectly force it through the GeoArmorRenderer path.

## Current Fabric-port gap (verified from project source)

`ArmorItemsRegistry` currently registers every armor piece as vanilla `ArmorItem`. That means the nine custom armor models cannot appear, even though their geo JSON and textures exist. The current `ArmorMaterialRegistry` creates vanilla 1.21.4 materials, but does not provide the original per-set item subclasses or GeoArmorRenderer supply methods.

## Required implementation order

1. Port the shared `PaladinArmorItem` behavior to Fabric 1.21.4, implementing GeckoLib `GeoItem` and its renderer provider.
2. Port the nine armor subclasses and their model/renderer classes, preserving special behavior found in original bytecode (notably Angel flight and Sculk effects) only after those methods are fully audited.
3. Keep Steel on the vanilla armor path unless original bytecode proves otherwise.
4. Replace the nine sets' vanilla registrations with the matching custom item subclasses.
5. Compile against the exact GeckoLib Fabric 1.21.4 artifact and run a client test before calling this complete.

## Status

This stage is an audit and implementation map, not a completed renderer port. No claim of compilation or in-game testing is made. A local Gradle executable and cached GeckoLib artifact are not available in this environment, so exact GeckoLib API compilation cannot honestly be verified here.
