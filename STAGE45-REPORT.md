# Stage 45 — Dedicated special weapon item type

## Changes
- Added `EpicWeaponItem`, a dedicated item subclass that retains the registered weapon ID.
- Changed registration so `angel_sword`, `moonlight_glaive`, and `cryorium_battle_axe` use this subclass; other non-armor items remain ordinary `Item` instances.
- Kept the combat attributes, Epic rarity, and 2031 durability settings established in Stage 44.

## Scope and limitations
- This separates the three special weapons from generic placeholder items and provides a stable type for later renderer/behavior registration.
- It does **not** yet implement GeckoLib's `GeoItem` interface, a renderer, animations, or weapon abilities.
- Build and in-game launch have not been verified in this environment. Do not install this development ZIP as a finished mod.
