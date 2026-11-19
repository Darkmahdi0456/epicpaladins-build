package net.veroxuniverse.epicpaladins.fabric;

import net.veroxuniverse.epicpaladins.fabric.item.GeoArmorItem;
import net.minecraft.item.Item;
import net.minecraft.item.equipment.ArmorMaterial;
import net.minecraft.item.equipment.EquipmentType;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

import java.util.LinkedHashMap;
import java.util.Map;

/** Registers the nine original armor sets recovered from the source mod. */
public final class ArmorItemsRegistry {
    private ArmorItemsRegistry() {}
    public static final Map<String, ArmorMaterial> MATERIALS = new LinkedHashMap<>();

    public static void register() {
        addSet("arclight", 20, 5, 10, 8, 5, 20, 4.0f, 0.2f);
        // Provisional balance: original values for these two sets are not yet confirmed.
        addSet("assassin", 25, 4, 8, 7, 4, 12, 3.0f, 0.2f);
        addSet("knight", 30, 6, 12, 9, 6, 10, 3.5f, 0.1f);
        addSet("angel", 20, 8, 14, 9, 7, 20, 5.0f, 0.3f);
        addSet("cryorium", 20, 5, 10, 8, 5, 20, 4.0f, 0.2f);
        addSet("jade", 20, 5, 10, 8, 5, 20, 3.5f, 0.5f);
        addSet("moonlight", 20, 5, 10, 8, 5, 20, 4.5f, 0.1f);
        addSet("bloodstone", 20, 5, 10, 8, 5, 20, 4.0f, 0.3f);
        addSet("sculk", 20, 5, 9, 8, 6, 20, 5.0f, 0.1f);
    }

    private static void addSet(String id, int durability, int helmet, int chest, int legs,
            int boots, int enchantability, float toughness, float knockback) {
        ArmorMaterial material = ArmorMaterialRegistry.create(id, durability, helmet, chest,
                legs, boots, enchantability, toughness, knockback);
        MATERIALS.put(id, material);
        registerPiece(id + "_helmet", material, EquipmentType.HELMET);
        registerPiece(id + "_chestplate", material, EquipmentType.CHESTPLATE);
        registerPiece(id + "_leggings", material, EquipmentType.LEGGINGS);
        registerPiece(id + "_boots", material, EquipmentType.BOOTS);
    }

    private static void registerPiece(String id, ArmorMaterial material, EquipmentType type) {
        Item.Settings settings = new Item.Settings().maxDamage(type.getMaxDamage(material.durability()));
        Item item = new GeoArmorItem(material, type, settings, id.substring(0, id.lastIndexOf('_')));
        Registry.register(Registries.ITEM, Identifier.of(EpicPaladinsFabric.MOD_ID, id), item);
        ContentRegistry.ITEMS.put(id, item);
    }
}
