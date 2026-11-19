# Stage 54 — Geo armor/texture integrity audit

- Added a repeatable audit for the nine armor Geo models referenced by the render manifest.
- The audit parses each Geo JSON, confirms its geometry/bone structure, and verifies that the referenced PNG exists and can be opened.
- It reports the Geo-declared UV canvas and actual PNG dimensions separately. A dimension difference is flagged for UV review rather than silently resizing a source texture.
- This stage does not register GeckoLib renderers and does not claim in-game armor rendering is complete.
- Run from the project root: `python3 tools_stage54_geo_texture_audit.py` (requires Pillow).
