# Stage 71 — Armor equipment-slot wiring audit

Scope: safe armor-rendering work only.

- Audited all nine registered armor sets and the four equipment categories.
- Confirmed the registry uses HELMET, CHESTPLATE, LEGGINGS, and BOOTS for the corresponding pieces.
- Confirmed each generated armor item receives its parent set id.
- Confirmed the GeckoLib provider passes the living entity, stack, equipment slot, and original biped model to `prepForRender` before returning the renderer.
- Added `tools_stage71_armor_slot_audit.py` for repeatable static checks.

Static audit: 11/11 checks passed. This is source inspection only; it does not prove Java compilation or in-game rendering. Gradle compilation and Minecraft runtime testing remain unverified.
