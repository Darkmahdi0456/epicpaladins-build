# Stage 39 — GeckoLib weapon asset audit

This stage adds a repeatable static audit for the three known animated weapon assets.

Checked pairs:
- Angel Sword: `geo/angel_sword.geo.json` + `textures/items/angel_sword.png`
- Cryorium Axe: `geo/cryorium_axe.geo.json` + `textures/items/cryorium_battle_axe.png`
- Moonlight Glaive: `geo/moonlight_glaive.geo.json` + `textures/items/moonlight_glaive.png`

The audit parses each Geo JSON, verifies a non-empty `minecraft:geometry` array, geometry identifiers and bone arrays, and checks that the referenced texture files exist.

**Limitations:** This does not implement a GeckoLib renderer, attach it to registered item instances, or prove the models render in Minecraft. No Gradle build or in-game test was run. The project must not be described as a working mod yet.

Run from the project root:

```bash
python tools_stage39_geckolib_weapon_audit.py
```
