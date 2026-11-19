# Stage 35 — Audit of special weapon/armor features

## Evidence inspected
The original NeoForge 1.21.1 JAR was inspected with `jar tf` and `javap -p`.

## Confirmed class-level findings
- `AngelSwordItem`, `CryoriumAxeItem`, and `MoonlightGlaiveItem` extend Minecraft `SwordItem` and implement GeckoLib `GeoItem`.
- Each of those three classes declares a GeckoLib animation cache, `initializeClient(...)`, `registerControllers(...)`, and `getAnimatableInstanceCache()`.
- `ArclightCrown` exists as a class under `common/items/summonItems`, but its public class signature exposes no methods. Its actual behavior needs bytecode inspection before implementing it.
- Armor item classes exist for Angel, Arclight, Assassin, Bloodstone, Cryorium, Jade, Knight, Moonlight, and Sculk. Separate client model/renderer classes exist for these sets (PaladinArmorModel is a shared base/model class).

## Porting consequences
1. These weapons are animated GeckoLib items in the original, not merely vanilla sword items.
2. The current Fabric port's generic item placeholders do not reproduce their original animation behavior.
3. Fabric-side GeckoLib renderer/controller registration is still missing; do not claim the original 3D held-item appearance is working.
4. The crown/summoning behavior is not inferred from the class name. Inspect its bytecode and related entity/registry classes before implementing.

## Scope of this stage
This is a bytecode-backed audit only. It does not implement abilities, animation controllers, or summon behavior, and it does not claim compilation or in-game testing.
