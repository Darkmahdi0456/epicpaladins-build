# Stage 8 — Recovering original registry definitions

This stage adds raw `javap -c -p` disassembly from the supplied original Epic Paladins 1.4.3 / Minecraft 1.21.1 JAR for the item, tool, block, and armor-material registries.

## Why this matters

The previous Fabric project used placeholder `Item` instances for armor and tools. That is not a faithful port. Before replacing placeholders, we need to recover the original armor material defense values, toughness/knockback resistance, repair ingredients, tool tier values, and exact item registrations from the original bytecode.

## Files added

- `reverse_engineering/original_bytecode/ArmorMaterialsRegistry.javap.txt`
- `reverse_engineering/original_bytecode/ItemsRegistry.javap.txt`
- `reverse_engineering/original_bytecode/ToolsRegistry.javap.txt`
- `reverse_engineering/original_bytecode/BlocksRegistry.javap.txt`

These are reference/disassembly files only. They are not Java source and are not compiled into the mod.

## Status

- Original registry bytecode extraction: completed for classes present in the supplied JAR.
- Mapping every lambda method back to each named material: still requires careful cross-reference with the static initializer and fields.
- Fabric armor/tool implementation: not yet implemented in this stage.
- Build/test: not run; no claim of a working JAR.

Next: map each original material and tier's exact stats, then implement Fabric-native armor and tool classes against Yarn 1.21.4 mappings.
