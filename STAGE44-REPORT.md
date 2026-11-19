# Stage 44 — Special weapon attribute port

## Changes
- The three special weapon IDs now receive dedicated Fabric 1.21.4 item settings rather than generic placeholder settings.
- Applied the values confirmed by Stage 43:
  - `angel_sword`: attack damage modifier +10.0, attack speed modifier -2.1
  - `moonlight_glaive`: attack damage modifier +10.0, attack speed modifier -2.5
  - `cryorium_battle_axe`: attack damage modifier +12.0, attack speed modifier -3.0
- Applied Epic rarity and 2031 durability (vanilla Netherite-tier durability baseline).
- All other item registrations remain unchanged.

## Important scope limits
- This is an attribute/settings port only. The three entries are still ordinary `Item` instances, not yet their original specialized item classes or GeckoLib animatable items.
- Cryorium's original AxeItem attribute factory behavior is represented by its exact attack values; original Java inheritance is not yet recreated.
- No Gradle build or in-game test is claimed. Yarn 1.21.4 API compatibility must be confirmed by the next compile pass.
