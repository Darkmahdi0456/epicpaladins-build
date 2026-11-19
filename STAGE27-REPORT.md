# Stage 27 — Recipe datapack audit

This stage adds `tools_recipe_audit.py` and its generated report. It scans the original Epic Paladins recipe JSON files, parses their JSON syntax, checks for a top-level recipe `type`, and performs a limited check that direct `epicpaladins:` references have corresponding item model or blockstate assets.

This is an audit only. It does **not** convert NeoForge biome modifiers, prove that recipe serializers/ingredients are valid on Fabric 1.21.4, or test recipes in-game. The project remains an uncompiled development source tree.
