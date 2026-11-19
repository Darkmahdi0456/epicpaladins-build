# Stage 51 — Correct Sculk armor repair ingredient

## Verified source behavior
The original NeoForge 1.21.1 `ArmorMaterialsRegistry` bytecode was inspected with `javap`. Its Sculk material repair ingredient is `Items.ECHO_SHARD` (not a custom `sculk_gem`).

## Change
Updated `data/epicpaladins/tags/item/repairs_sculk.json` to use `minecraft:echo_shard`, matching the original mod's repair ingredient. The previous tag referenced `epicpaladins:sculk_gem`, which is not registered and has no item texture/model in this port.

## Validation
`tools_stage51_repair_tag_audit.py` ran successfully and checked all ten armor repair tags against the project registry and the verified vanilla echo shard ID.

## Limits
This is a data/tag correction plus static validation. No Gradle build or in-game test was performed. The port remains unfinished; GeckoLib armor and weapon rendering are still outstanding.
