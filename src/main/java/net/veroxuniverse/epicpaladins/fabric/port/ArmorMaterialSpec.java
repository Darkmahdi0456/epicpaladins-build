package net.veroxuniverse.epicpaladins.fabric.port;

/**
 * Recovered source-independent armor data from the original Epic Paladins
 * 1.21.1 bytecode. This is a data specification only; it is deliberately
 * separate from Minecraft's version-specific ArmorMaterial API.
 */
public record ArmorMaterialSpec(
        String id,
        int bootsDefense,
        int leggingsDefense,
        int chestplateDefense,
        int helmetDefense,
        float toughness,
        float knockbackResistance,
        String repairIngredientId
) {
    public static final ArmorMaterialSpec[] ALL = {
        new ArmorMaterialSpec("arclight", 5, 8, 10, 5, 4.0f, 0.2f, "arclight_gem"),
        new ArmorMaterialSpec("angel", 7, 9, 14, 8, 5.0f, 0.3f, "arclight_gem"),
        new ArmorMaterialSpec("cryorium", 5, 8, 10, 5, 4.0f, 0.2f, "cryorium_gem"),
        new ArmorMaterialSpec("jade", 5, 8, 10, 5, 3.5f, 0.5f, "jade_gem"),
        new ArmorMaterialSpec("moonlight", 5, 8, 10, 5, 4.5f, 0.1f, "moonlight_gem"),
        new ArmorMaterialSpec("bloodstone", 5, 8, 10, 5, 4.0f, 0.3f, "bloodstone_gem"),
        new ArmorMaterialSpec("sculk", 6, 8, 9, 5, 5.0f, 0.1f, "minecraft:echo_shard"),
        new ArmorMaterialSpec("steel", 3, 4, 6, 3, 1.5f, 0.2f, "steel_ingot")
    };
}
