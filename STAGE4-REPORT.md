# Epic Paladins Fabric port — Stage 4 (asset/model pass)

Target: Minecraft 1.21.4 / Fabric.

This is still a development project, NOT an installable mod JAR.

## Work done
- Added missing generated-item model JSON files for 0 registered item IDs where a matching texture exists.
- Reused the original extracted item/block textures; no texture art was fabricated.
- Preserved stage 3 source, recipes, tags, models, geo files, and textures.

## Items still missing a matching texture/model
None detected in this pass.

## Important remaining work
- Replace placeholder Item registrations with actual armor, tool, and weapon classes and correct stats.
- Implement armor materials, custom abilities/effects, and special weapon behavior.
- Port GeckoLib armor/weapon renderers and animations.
- Audit recipes, loot/world generation, tags, sounds, translations, and all original behaviors.
- Build with Gradle and test on Minecraft 1.21.4 Fabric.

No successful compile or in-game test is claimed.
