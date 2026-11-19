# Stage 59 — Moonlight armor hierarchy correction

## Changes
- Corrected `armorLeftLeg` parent from `bipedRightLeg` to `bipedLeftLeg`.
- Corrected `armorRightLeg` parent from `bipedLeftLeg` to `bipedRightLeg`.
- Kept the left and right boot parents aligned with their matching body legs.
- No geometry cubes, pivots, UVs, or textures were intentionally changed.

## Validation
- Parsed the edited GeoJSON successfully.
- Asserted left leg and left boot are parented to `bipedLeftLeg`.
- Asserted right leg and right boot are parented to `bipedRightLeg`.

## Limitations
This is a structural JSON validation only. GeckoLib rendering, Gradle compilation, and in-game appearance are not verified in this environment. Stage 60 should inspect all nine models for parent/child hierarchy consistency before implementing renderer code.
