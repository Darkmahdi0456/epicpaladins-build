# Stage 43 — Original special-weapon stats audit

## Scope
Inspected the original Epic Paladins 1.4.3 / Minecraft 1.21.1 NeoForge `ItemsRegistry` and `ItemMaterialsRegistry` bytecode using `javap -p -c`. This stage records values passed by the original registration code; it does not claim that the Fabric items have been implemented or tested.

## Confirmed registration values

| Weapon | Tier passed to constructor | Attribute factory call | Rarity |
|---|---|---|---|
| Angel Sword | `Tiers.NETHERITE` | `SwordItem.createAttributes(NETHERITE, 10, -2.1F)` | `EPIC` |
| Moonlight Glaive | `Tiers.NETHERITE` | `SwordItem.createAttributes(NETHERITE, 10, -2.5F)` | `EPIC` |
| Cryorium Battle Axe | `Tiers.NETHERITE` | `AxeItem.createAttributes(NETHERITE, 12.0F, -3.0F)` | `EPIC` |

All three constructors receive the Netherite tier and the resulting properties. This is notable for Cryorium: its Java class extends `SwordItem`, but its registered attribute modifiers are created with `AxeItem.createAttributes`.

## Netherite tier baseline

The original registrations pass vanilla `Tiers.NETHERITE`, not the mod's custom `ItemMaterialsRegistry` tiers. The vanilla tier therefore supplies durability, mining speed, mining level, enchantability and repair baseline. The mod's custom tiers (Steel, Jade, Arclight, Moonlight, Sculk, Bloodstone, Cryorium) are separate and should not be substituted for these three special weapons.

## Porting decision

1. Preserve the three exact attribute factory parameter sets above.
2. Preserve `EPIC` rarity.
3. Keep Cryorium's original `SwordItem` inheritance while retaining its axe-style attribute factory values; do not silently convert its class to `AxeItem`.
4. This stage is an audit only. No Fabric item registration code was changed because exact 1.21.4 Yarn API wiring and renderer implementation still need a separate verified implementation pass.

## Verification

- Original jar contains `ItemsRegistry.class` and `ItemMaterialsRegistry.class`.
- `javap` bytecode shows the three constructor calls, attribute factory arguments, and rarity calls listed above.
- No Gradle build or in-game test is claimed.
