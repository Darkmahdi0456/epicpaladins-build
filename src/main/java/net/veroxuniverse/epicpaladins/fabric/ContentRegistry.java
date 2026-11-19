package net.veroxuniverse.epicpaladins.fabric;

import net.veroxuniverse.epicpaladins.fabric.item.EpicWeaponItem;
import net.minecraft.block.Block;
import net.minecraft.block.AbstractBlock;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.util.Rarity;
import net.minecraft.entity.attribute.EntityAttributeModifier;
import net.minecraft.entity.attribute.EntityAttributes;
import net.minecraft.component.type.AttributeModifiersComponent;
import net.minecraft.entity.EquipmentSlotGroup;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

/** First Fabric content pass. Items are placeholders until armor/tool behaviors are ported. */
public final class ContentRegistry {
 private ContentRegistry() {}
 public static final java.util.Map<String, Item> ITEMS = new java.util.LinkedHashMap<>();
 public static final java.util.Map<String, Block> BLOCKS = new java.util.LinkedHashMap<>();
 private static final String[] ITEM_IDS = {
        "arclight_gem",
        "moonlight_gem",
        "jade_gem",
        "bloodstone_gem",
        "cryorium_gem",
        "steel_ingot",
        "steel_nugget",
        "steel_template",
        "arclight_template",
        "bloodstone_template",
        "cryorium_template",
        "jade_template",
        "moonlight_template",
        "sculk_template",
        "angel_feather",
        "arclight_helmet",
        "arclight_chestplate",
        "arclight_leggings",
        "arclight_boots",
        "angel_helmet",
        "angel_chestplate",
        "angel_leggings",
        "angel_boots",
        "assassin_helmet",
        "assassin_chestplate",
        "assassin_leggings",
        "assassin_boots",
        "bloodstone_helmet",
        "bloodstone_chestplate",
        "bloodstone_leggings",
        "bloodstone_boots",
        "cryorium_helmet",
        "cryorium_chestplate",
        "cryorium_leggings",
        "cryorium_boots",
        "jade_helmet",
        "jade_chestplate",
        "jade_leggings",
        "jade_boots",
        "knight_helmet",
        "knight_chestplate",
        "knight_leggings",
        "knight_boots",
        "moonlight_helmet",
        "moonlight_chestplate",
        "moonlight_leggings",
        "moonlight_boots",
        "sculk_helmet",
        "sculk_chestplate",
        "sculk_leggings",
        "sculk_boots",
        "arclight_sword",
        "arclight_pickaxe",
        "arclight_axe",
        "arclight_shovel",
        "arclight_hoe",
        "jade_sword",
        "jade_pickaxe",
        "jade_axe",
        "jade_shovel",
        "jade_hoe",
        "moonlight_sword",
        "moonlight_pickaxe",
        "moonlight_axe",
        "moonlight_shovel",
        "moonlight_hoe",
        "bloodstone_sword",
        "bloodstone_pickaxe",
        "bloodstone_axe",
        "bloodstone_shovel",
        "bloodstone_hoe",
        "cryorium_sword",
        "cryorium_pickaxe",
        "cryorium_axe",
        "cryorium_shovel",
        "cryorium_hoe",
        "sculk_sword",
        "sculk_pickaxe",
        "sculk_axe",
        "sculk_shovel",
        "sculk_hoe",
        "angel_sword",
        "moonlight_glaive",
        "cryorium_battle_axe"
 };
 private static final String[] BLOCK_IDS = {
        "deepslate_arclight_ore",
        "arclight_ore",
        "arclight_block",
        "deepslate_cryorium_ore",
        "cryorium_ore",
        "cryorium_block",
        "deepslate_bloodstone_ore",
        "bloodstone_ore",
        "bloodstone_block",
        "jade_ore",
        "jade_block",
        "moonlight_ore",
        "moonlight_block",
        "steel_block"
 };

 private static boolean isSpecialWeapon(String id) {
  return "angel_sword".equals(id) || "moonlight_glaive".equals(id) || "cryorium_battle_axe".equals(id);
 }

 /** Recreates the original 1.21.1 special-weapon combat values on Fabric 1.21.4.
  * Damage amounts are the modifier amounts passed to the original attribute factories;
  * vanilla player base attack damage is applied separately by Minecraft.
  */
 private static Item.Settings specialWeaponSettings(String id) {
  double damage;
  double speed;
  if ("angel_sword".equals(id)) {
   damage = 10.0D; speed = -2.1D;
  } else if ("moonlight_glaive".equals(id)) {
   damage = 10.0D; speed = -2.5D;
  } else if ("cryorium_battle_axe".equals(id)) {
   damage = 12.0D; speed = -3.0D;
  } else {
   return new Item.Settings();
  }
  AttributeModifiersComponent attributes = AttributeModifiersComponent.builder()
    .add(EntityAttributes.ATTACK_DAMAGE,
      new EntityAttributeModifier(Identifier.of(EpicPaladinsFabric.MOD_ID, id + "_attack_damage"), damage, EntityAttributeModifier.Operation.ADD_VALUE),
      EquipmentSlotGroup.MAINHAND)
    .add(EntityAttributes.ATTACK_SPEED,
      new EntityAttributeModifier(Identifier.of(EpicPaladinsFabric.MOD_ID, id + "_attack_speed"), speed, EntityAttributeModifier.Operation.ADD_VALUE),
      EquipmentSlotGroup.MAINHAND)
    .build();
  // Netherite tier durability is 2031; preserve Epic rarity from the original registrations.
  return new Item.Settings().maxDamage(2031).rarity(Rarity.EPIC).attributeModifiers(attributes);
 }

 public static void register() {
  java.util.Set<String> wearableArmor = new java.util.HashSet<>();
  for (String set : new String[]{"arclight", "angel", "assassin", "bloodstone", "cryorium", "jade", "knight", "moonlight", "sculk"}) {
   for (String part : new String[]{"_helmet", "_chestplate", "_leggings", "_boots"}) wearableArmor.add(set + part);
  }
  for (String id : ITEM_IDS) {
   if (wearableArmor.contains(id)) continue;
   Item.Settings settings = specialWeaponSettings(id);
   Item item = Registry.register(Registries.ITEM, Identifier.of(EpicPaladinsFabric.MOD_ID, id),
     isSpecialWeapon(id) ? new EpicWeaponItem(id, settings) : new Item(settings));
   ITEMS.put(id, item);
  }
  ArmorItemsRegistry.register();
  for (String id : BLOCK_IDS) {
   Block block = Registry.register(Registries.BLOCK, Identifier.of(EpicPaladinsFabric.MOD_ID, id), new Block(AbstractBlock.Settings.copy(net.minecraft.block.Blocks.IRON_BLOCK)));
   BLOCKS.put(id, block);
   Registry.register(Registries.ITEM, Identifier.of(EpicPaladinsFabric.MOD_ID, id), new BlockItem(block, new Item.Settings()));
  }
 }
}
