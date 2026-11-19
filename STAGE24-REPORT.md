# Stage 24 — Vanilla item-model fallback for signature weapons

## Changes
- Added/normalized vanilla `handheld` item model JSON for `angel_sword`, `cryorium_axe`, and `moonlight_glaive`.
- Each model points to its existing `textures/item/<id>.png` texture.
- Original Geo model files remain in `geo/`; these are preserved for a future GeckoLib renderer.

## Scope and limitations
- This gives the three signature weapons a conventional 2D handheld item-model fallback in inventory/hand, where the Minecraft item renderer can use it.
- It does NOT implement custom 3D Geo rendering, attack animations, special abilities, or verify original damage/speed values.
- The project has not been compiled or launched in Minecraft. Resource JSON syntax was checked only.
