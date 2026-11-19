Epic Paladins Stage 48 - Armor portability audit

This is a read-only audit; no armor rendering code was changed.

angel: GeoModel valid; bones=20; texture=angel_armor_textures.png; dimensions=512x512 RGBA
arclight: GeoModel valid; bones=14; texture=arclight_armor_textures.png; dimensions=256x256 RGBA
assassin: GeoModel valid; bones=14; texture=assassin_armor_textures.png; dimensions=256x256 RGBA
bloodstone: GeoModel valid; bones=14; texture=bloodstone_armor_textures.png; dimensions=256x256 RGBA
cryorium: GeoModel valid; bones=14; texture=cryorium_armor_textures.png; dimensions=256x256 RGBA
jade: GeoModel valid; bones=14; texture=jade_armor_textures.png; dimensions=256x256 RGBA
knight: GeoModel valid; bones=20; texture=knight_armor_textures.png; dimensions=176x176 RGBA
moonlight: GeoModel valid; bones=14; texture=moonlight_armor_textures.png; dimensions=256x256 RGBA
sculk: GeoModel valid; bones=14; texture=sculk_armor_textures.png; dimensions=128x128 RGBA

Conclusion:
- Nine armor sets have GeckoLib geometry and matching high-resolution atlas textures.
- These atlas PNGs are not standard vanilla 64x32/64x64 armor-layer textures (dimensions vary).
- The current Fabric ArmorItemsRegistry creates vanilla ArmorItem instances. Those items do not automatically render the GeckoLib geometry.
- Do not create vanilla equipment-layer JSON by simply pointing at these atlases; that would be an unverified/incompatible mapping.
- Next correct implementation requires GeckoLib GeoArmorItem/GeoArmorRenderer classes and client-side renderer registration for the exact GeckoLib 4.8 Fabric API.
