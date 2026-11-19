# Stage 58 — Armor bone compatibility audit

## Scope
This stage is limited to the nine existing armor GeoJSON models. It does not implement or claim a working in-game renderer.

## Findings
- All nine models contain the eight core armor bone names used by the GeckoLib armor model convention: `armorHead`, `armorBody`, both arms, both legs, and both boots.
- `angel_armor.geo.json` has a custom wing/decorative bone hierarchy and no `biped*` reference bones; it will need a dedicated renderer/model check rather than assuming the same alignment as the other sets.
- `knight_armor.geo.json` includes additional `bone*` decoration bones that must be preserved when mapping body parts.
- `moonlight_armor.geo.json` assigns `armorRightLeg` beneath `bipedLeftLeg` and `armorLeftLeg` beneath `bipedRightLeg`. This is a left/right hierarchy mismatch to correct or explicitly compensate for before final rendering.

## Validation
`python tools_stage58_armor_bone_audit.py` passed: all nine models include the eight required armor bone names.

## Not yet verified
No Gradle build, GeckoLib runtime, or in-game render test was possible in this environment. The current `ArmorItemsRegistry` still creates vanilla `ArmorItem` instances; no claim is made that 3D armor rendering is connected.
