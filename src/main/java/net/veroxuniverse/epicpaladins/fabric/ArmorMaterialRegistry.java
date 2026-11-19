package net.veroxuniverse.epicpaladins.fabric;

import net.minecraft.item.equipment.ArmorMaterial;
import net.minecraft.item.equipment.EquipmentType;
import net.minecraft.item.Item;
import net.minecraft.item.Items;
import net.minecraft.item.equipment.EquipmentAsset;
import net.minecraft.registry.RegistryKey;
import net.minecraft.registry.RegistryKeys;
import net.minecraft.registry.tag.TagKey;
import net.minecraft.sound.SoundEvents;
import net.minecraft.util.Identifier;

import java.util.EnumMap;
import java.util.Map;

/** Minecraft 1.21.4 armor material definitions. Core values recovered from original 1.21.1 bytecode. */
public final class ArmorMaterialRegistry {
    private ArmorMaterialRegistry() {}

    public static ArmorMaterial create(String id, int durability, int helmet, int chest,
            int legs, int boots, int enchantability, float toughness, float knockback) {
        Map<EquipmentType, Integer> defense = new EnumMap<>(EquipmentType.class);
        defense.put(EquipmentType.HELMET, helmet);
        defense.put(EquipmentType.CHESTPLATE, chest);
        defense.put(EquipmentType.LEGGINGS, legs);
        defense.put(EquipmentType.BOOTS, boots);
        Identifier identifier = Identifier.of(EpicPaladinsFabric.MOD_ID, id);
        RegistryKey<EquipmentAsset> assetKey = RegistryKey.of(RegistryKeys.EQUIPMENT_ASSET, identifier);
        TagKey<Item> repairTag = TagKey.of(RegistryKeys.ITEM,
                Identifier.of(EpicPaladinsFabric.MOD_ID, "repairs_" + id));
        return new ArmorMaterial(durability, defense, enchantability,
                SoundEvents.ITEM_ARMOR_EQUIP_DIAMOND, toughness, knockback, repairTag, assetKey);
    }
}
