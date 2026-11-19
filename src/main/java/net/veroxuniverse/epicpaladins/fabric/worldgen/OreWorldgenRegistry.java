package net.veroxuniverse.epicpaladins.fabric.worldgen;

import net.fabricmc.fabric.api.biome.v1.BiomeModifications;
import net.fabricmc.fabric.api.biome.v1.BiomeSelectors;
import net.minecraft.registry.RegistryKey;
import net.minecraft.registry.RegistryKeys;
import net.minecraft.util.Identifier;
import net.minecraft.world.gen.GenerationStep;
import net.minecraft.world.gen.feature.PlacedFeature;

/** Fabric biome injection for Epic Paladins ore placed features. */
public final class OreWorldgenRegistry {
    private OreWorldgenRegistry() {}

    private static RegistryKey<PlacedFeature> placed(String path) {
        return RegistryKey.of(RegistryKeys.PLACED_FEATURE, Identifier.of("epicpaladins", path));
    }

    public static void register() {
        BiomeModifications.addFeature(BiomeSelectors.foundInOverworld(),
                GenerationStep.Feature.UNDERGROUND_ORES, placed("arclight_ore_placed"));
        BiomeModifications.addFeature(BiomeSelectors.foundInOverworld(),
                GenerationStep.Feature.UNDERGROUND_ORES, placed("bloodstone_ore_placed"));
        BiomeModifications.addFeature(BiomeSelectors.foundInOverworld(),
                GenerationStep.Feature.UNDERGROUND_ORES, placed("cryorium_ore_placed"));
        BiomeModifications.addFeature(BiomeSelectors.foundInTheNether(),
                GenerationStep.Feature.UNDERGROUND_ORES, placed("moonlight_ore_placed"));
        BiomeModifications.addFeature(BiomeSelectors.foundInTheEnd(),
                GenerationStep.Feature.UNDERGROUND_ORES, placed("jade_ore_placed"));
    }
}
