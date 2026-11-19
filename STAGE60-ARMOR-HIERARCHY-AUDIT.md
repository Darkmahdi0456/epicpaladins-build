# Stage 60 — Armor hierarchy audit

Geo armor files found: 9

- angel_armor.geo: 20 bones; special Angel hierarchy (wings)
- arclight_armor.geo: 14 bones; standard humanoid hierarchy
- assassin_armor.geo: 14 bones; standard humanoid hierarchy
- bloodstone_armor.geo: 14 bones; standard humanoid hierarchy
- cryorium_armor.geo: 14 bones; standard humanoid hierarchy
- jade_armor.geo: 14 bones; standard humanoid hierarchy
- knight_armor.geo: 20 bones; standard humanoid hierarchy
- moonlight_armor.geo: 14 bones; standard humanoid hierarchy
- sculk_armor.geo: 14 bones; standard humanoid hierarchy

## Validation
- Parent references and cycles checked for all 9 files.
- Standard hierarchy checked for 8 sets.
- Angel checked with a separate wing-aware expected-bone set.

- PASS: no missing parent references, duplicate names, or hierarchy cycles.
- PASS: all eight standard armor sets match their expected left/right body-bone parents.
- PASS: Angel special wing/body structure contains its expected key bones.

## Limitations
This is a structural JSON audit only. It does not prove GeckoLib rendering, Java compilation, or in-game alignment.
