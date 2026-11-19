# Stage 14 — Armor material implementation scaffold

- Added an ArmorMaterialRegistry source file targeting Minecraft 1.21.4 Yarn/Fabric APIs.
- The registry helper creates namespaced armor material registry entries and layer identifiers.
- This is a source-code scaffold only. It has NOT been compiled or launched.
- It does not yet replace placeholder armor item registrations in ContentRegistry.
- Defense points, enchantability, repair ingredients and layer texture conventions are provisional and must be verified against original bytecode/assets before claiming parity.
- Next: wire each armor set's four ArmorItems to its material, verify API signatures with Gradle/Loom, then add item models and test in-game.
