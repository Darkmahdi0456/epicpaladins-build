# Stage 26 — Item model and texture reference audit

This stage adds `tools_item_model_audit.py`, a repeatable local audit for item-model JSON files and their explicit namespaced texture references.

The audit checks JSON parsing, that `textures` is an object, and that every explicit local texture reference resolves to a PNG under the matching asset namespace. It does not validate Minecraft rendering, parent-model inheritance, GeckoLib rendering, item registration, or runtime behavior.

See `STAGE26-ITEM-MODEL-AUDIT.txt` for the result produced on this project snapshot. The project has not yet been compiled or tested in Minecraft.
