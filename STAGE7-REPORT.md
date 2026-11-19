# Stage 7 — Recovering original gameplay definitions

This stage inspects the original compiled Java bytecode using `javap`. It does not claim to implement or compile the port. The goal is to recover original material and registration definitions before replacing placeholder registrations.

## Confirmed from original bytecode

- Armor material registry contains: Arclight, Angel, Cryorium, Jade, Moonlight, Bloodstone, Sculk, Steel.
- Tool tier registry contains: Steel, Jade, Arclight, Moonlight, Sculk, Bloodstone, Cryorium.
- Original block registry declares 14 blocks: ore/deepslate ore/storage block families for Arclight, Cryorium, Bloodstone, Jade, Moonlight, and Steel storage block.
- Armor renderer/model classes exist for Angel, Arclight, Assassin, Bloodstone, Cryorium, Jade, Knight, Moonlight, and Sculk.
- Special weapon renderer/model classes exist for Angel Sword, Cryorium Battle Axe, and Moonlight Glaive.

## Decompiled registry bytecode

The following is technical reference output from the original JAR, not source code suitable for direct compilation.

### net.veroxuniverse.epicpaladins.common.registries.items.ArmorMaterialsRegistry

```text
Compiled from "ArmorMaterialsRegistry.java"
public class net.veroxuniverse.epicpaladins.common.registries.items.ArmorMaterialsRegistry {
  public static final net.neoforged.neoforge.registries.DeferredRegister<net.minecraft.world.item.ArmorMaterial> ARMOR_MATERIALS;

  public static net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.ArmorMaterial, net.minecraft.world.item.ArmorMaterial> ARCLIGHT;

  public static net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.ArmorMaterial, net.minecraft.world.item.ArmorMaterial> ANGEL;

  public static net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.ArmorMaterial, net.minecraft.world.item.ArmorMaterial> CRYORIUM;

  public static net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.ArmorMaterial, net.minecraft.world.item.ArmorMaterial> JADE;

  public static net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.ArmorMaterial, net.minecraft.world.item.ArmorMaterial> MOONLIGHT;

  public static net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.ArmorMaterial, net.minecraft.world.item.ArmorMaterial> BLOODSTONE;

  public static net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.ArmorMaterial, net.minecraft.world.item.ArmorMaterial> SCULK;

  public static net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.ArmorMaterial, net.minecraft.world.item.ArmorMaterial> STEEL;

  public net.veroxuniverse.epicpaladins.common.registries.items.ArmorMaterialsRegistry();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void register(net.neoforged.bus.api.IEventBus);
    Code:
       0: getstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
       3: aload_0
       4: invokevirtual #13                 // Method net/neoforged/neoforge/registries/DeferredRegister.register:(Lnet/neoforged/bus/api/IEventBus;)V
       7: return

  private static net.minecraft.world.item.ArmorMaterial lambda$static$23();
    Code:
       0: new           #19                 // class net/minecraft/world/item/ArmorMaterial
       3: dup
       4: new           #21                 // class java/util/EnumMap
       7: dup
       8: ldc           #23                 // class net/minecraft/world/item/ArmorItem$Type
      10: invokespecial #25                 // Method java/util/EnumMap."<init>":(Ljava/lang/Class;)V
      13: invokedynamic #28,  0             // InvokeDynamic #0:accept:()Ljava/util/function/Consumer;
      18: invokestatic  #32                 // Method net/minecraft/Util.make:(Ljava/lang/Object;Ljava/util/function/Consumer;)Ljava/lang/Object;
      21: checkcast     #38                 // class java/util/Map
      24: bipush        20
      26: getstatic     #40                 // Field net/minecraft/sounds/SoundEvents.ARMOR_EQUIP_DIAMOND:Lnet/minecraft/core/Holder;
      29: invokedynamic #46,  0             // InvokeDynamic #1:get:()Ljava/util/function/Supplier;
      34: new           #50                 // class net/minecraft/world/item/ArmorMaterial$Layer
      37: dup
      38: ldc           #54                 // String epicpaladins
      40: ldc           #56                 // String steel
      42: invokestatic  #58                 // Method net/minecraft/resources/ResourceLocation.fromNamespaceAndPath:(Ljava/lang/String;Ljava/lang/String;)Lnet/minecraft/resources/ResourceLocation;
      45: invokespecial #64                 // Method net/minecraft/world/item/ArmorMaterial$Layer."<init>":(Lnet/minecraft/resources/ResourceLocation;)V
      48: invokestatic  #67                 // InterfaceMethod java/util/List.of:(Ljava/lang/Object;)Ljava/util/List;
      51: ldc           #73                 // float 1.5f
      53: ldc           #74                 // float 0.2f
      55: invokespecial #75                 // Method net/minecraft/world/item/ArmorMaterial."<init>":(Ljava/util/Map;ILnet/minecraft/core/Holder;Ljava/util/function/Supplier;Ljava/util/List;FF)V
      58: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$22();
    Code:
       0: iconst_1
       1: anewarray     #78                 // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #80                 // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.STEEL_INGOT:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #86                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #78                 // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #91                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static void lambda$static$21(java.util.EnumMap);
    Code:
       0: aload_0
       1: getstatic     #96                 // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
       4: iconst_3
       5: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
       8: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      11: pop
      12: aload_0
      13: getstatic     #110                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      16: iconst_4
      17: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      20: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      23: pop
      24: aload_0
      25: getstatic     #113                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      28: bipush        6
      30: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      33: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      36: pop
      37: aload_0
      38: getstatic     #116                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      41: iconst_3
      42: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      45: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      48: pop
      49: return

  private static net.minecraft.world.item.ArmorMaterial lambda$static$20();
    Code:
       0: new           #19                 // class net/minecraft/world/item/ArmorMaterial
       3: dup
       4: new           #21                 // class java/util/EnumMap
       7: dup
       8: ldc           #23                 // class net/minecraft/world/item/ArmorItem$Type
      10: invokespecial #25                 // Method java/util/EnumMap."<init>":(Ljava/lang/Class;)V
      13: invokedynamic #119,  0            // InvokeDynamic #2:accept:()Ljava/util/function/Consumer;
      18: invokestatic  #32                 // Method net/minecraft/Util.make:(Ljava/lang/Object;Ljava/util/function/Consumer;)Ljava/lang/Object;
      21: checkcast     #38                 // class java/util/Map
      24: bipush        20
      26: getstatic     #40                 // Field net/minecraft/sounds/SoundEvents.ARMOR_EQUIP_DIAMOND:Lnet/minecraft/core/Holder;
      29: invokedynamic #120,  0            // InvokeDynamic #3:get:()Ljava/util/function/Supplier;
      34: new           #50                 // class net/minecraft/world/item/ArmorMaterial$Layer
      37: dup
      38: ldc           #54                 // String epicpaladins
      40: ldc           #121                // String sculk
      42: invokestatic  #58                 // Method net/minecraft/resources/ResourceLocation.fromNamespaceAndPath:(Ljava/lang/String;Ljava/lang/String;)Lnet/minecraft/resources/ResourceLocation;
      45: invokespecial #64                 // Method net/minecraft/world/item/ArmorMaterial$Layer."<init>":(Lnet/minecraft/resources/ResourceLocation;)V
      48: invokestatic  #67                 // InterfaceMethod java/util/List.of:(Ljava/lang/Object;)Ljava/util/List;
      51: ldc           #123                // float 5.0f
      53: ldc           #124                // float 0.1f
      55: invokespecial #75                 // Method net/minecraft/world/item/ArmorMaterial."<init>":(Ljava/util/Map;ILnet/minecraft/core/Holder;Ljava/util/function/Supplier;Ljava/util/List;FF)V
      58: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$19();
    Code:
       0: iconst_1
       1: anewarray     #78                 // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #125                // Field net/minecraft/world/item/Items.ECHO_SHARD:Lnet/minecraft/world/item/Item;
       9: aastore
      10: invokestatic  #91                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      13: areturn

  private static void lambda$static$18(java.util.EnumMap);
    Code:
       0: aload_0
       1: getstatic     #96                 // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
       4: bipush        6
       6: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
       9: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      12: pop
      13: aload_0
      14: getstatic     #110                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        8
      19: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      22: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      25: pop
      26: aload_0
      27: getstatic     #113                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      30: bipush        9
      32: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      35: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      38: pop
      39: aload_0
      40: getstatic     #116                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      43: iconst_5
      44: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      47: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      50: pop
      51: return

  private static net.minecraft.world.item.ArmorMaterial lambda$static$17();
    Code:
       0: new           #19                 // class net/minecraft/world/item/ArmorMaterial
       3: dup
       4: new           #21                 // class java/util/EnumMap
       7: dup
       8: ldc           #23                 // class net/minecraft/world/item/ArmorItem$Type
      10: invokespecial #25                 // Method java/util/EnumMap."<init>":(Ljava/lang/Class;)V
      13: invokedynamic #131,  0            // InvokeDynamic #4:accept:()Ljava/util/function/Consumer;
      18: invokestatic  #32                 // Method net/minecraft/Util.make:(Ljava/lang/Object;Ljava/util/function/Consumer;)Ljava/lang/Object;
      21: checkcast     #38                 // class java/util/Map
      24: bipush        20
      26: getstatic     #40                 // Field net/minecraft/sounds/SoundEvents.ARMOR_EQUIP_DIAMOND:Lnet/minecraft/core/Holder;
      29: invokedynamic #132,  0            // InvokeDynamic #5:get:()Ljava/util/function/Supplier;
      34: new           #50                 // class net/minecraft/world/item/ArmorMaterial$Layer
      37: dup
      38: ldc           #54                 // String epicpaladins
      40: ldc           #133                // String bloodstone
      42: invokestatic  #58                 // Method net/minecraft/resources/ResourceLocation.fromNamespaceAndPath:(Ljava/lang/String;Ljava/lang/String;)Lnet/minecraft/resources/ResourceLocation;
      45: invokespecial #64                 // Method net/minecraft/world/item/ArmorMaterial$Layer."<init>":(Lnet/minecraft/resources/ResourceLocation;)V
      48: invokestatic  #67                 // InterfaceMethod java/util/List.of:(Ljava/lang/Object;)Ljava/util/List;
      51: ldc           #135                // float 4.0f
      53: ldc           #136                // float 0.3f
      55: invokespecial #75                 // Method net/minecraft/world/item/ArmorMaterial."<init>":(Ljava/util/Map;ILnet/minecraft/core/Holder;Ljava/util/function/Supplier;Ljava/util/List;FF)V
      58: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$16();
    Code:
       0: iconst_1
       1: anewarray     #78                 // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #137                // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.BLOODSTONE_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #86                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #78                 // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #91                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static void lambda$static$15(java.util.EnumMap);
    Code:
       0: aload_0
       1: getstatic     #96                 // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
       4: iconst_5
       5: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
       8: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      11: pop
      12: aload_0
      13: getstatic     #110                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      16: bipush        8
      18: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      21: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      24: pop
      25: aload_0
      26: getstatic     #113                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      29: bipush        10
      31: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      34: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      37: pop
      38: aload_0
      39: getstatic     #116                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      42: iconst_5
      43: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      46: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      49: pop
      50: return

  private static net.minecraft.world.item.ArmorMaterial lambda$static$14();
    Code:
       0: new           #19                 // class net/minecraft/world/item/ArmorMaterial
       3: dup
       4: new           #21                 // class java/util/EnumMap
       7: dup
       8: ldc           #23                 // class net/minecraft/world/item/ArmorItem$Type
      10: invokespecial #25                 // Method java/util/EnumMap."<init>":(Ljava/lang/Class;)V
      13: invokedynamic #140,  0            // InvokeDynamic #6:accept:()Ljava/util/function/Consumer;
      18: invokestatic  #32                 // Method net/minecraft/Util.make:(Ljava/lang/Object;Ljava/util/function/Consumer;)Ljava/lang/Object;
      21: checkcast     #38                 // class java/util/Map
      24: bipush        20
      26: getstatic     #40                 // Field net/minecraft/sounds/SoundEvents.ARMOR_EQUIP_DIAMOND:Lnet/minecraft/core/Holder;
      29: invokedynamic #141,  0            // InvokeDynamic #7:get:()Ljava/util/function/Supplier;
      34: new           #50                 // class net/minecraft/world/item/ArmorMaterial$Layer
      37: dup
      38: ldc           #54                 // String epicpaladins
      40: ldc           #142                // String moonlight
      42: invokestatic  #58                 // Method net/minecraft/resources/ResourceLocation.fromNamespaceAndPath:(Ljava/lang/String;Ljava/lang/String;)Lnet/minecraft/resources/ResourceLocation;
      45: invokespecial #64                 // Method net/minecraft/world/item/ArmorMaterial$Layer."<init>":(Lnet/minecraft/resources/ResourceLocation;)V
      48: invokestatic  #67                 // InterfaceMethod java/util/List.of:(Ljava/lang/Object;)Ljava/util/List;
      51: ldc           #144                // float 4.5f
      53: ldc           #124                // float 0.1f
      55: invokespecial #75                 // Method net/minecraft/world/item/ArmorMaterial."<init>":(Ljava/util/Map;ILnet/minecraft/core/Holder;Ljava/util/function/Supplier;Ljava/util/List;FF)V
      58: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$13();
    Code:
       0: iconst_1
       1: anewarray     #78                 // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #145                // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.MOONLIGHT_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #86                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #78                 // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #91                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static void lambda$static$12(java.util.EnumMap);
    Code:
       0: aload_0
       1: getstatic     #96                 // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
       4: iconst_5
       5: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
       8: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      11: pop
      12: aload_0
      13: getstatic     #110                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      16: bipush        8
      18: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      21: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      24: pop
      25: aload_0
      26: getstatic     #113                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      29: bipush        10
      31: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      34: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      37: pop
      38: aload_0
      39: getstatic     #116                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      42: iconst_5
      43: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      46: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      49: pop
      50: return

  private static net.minecraft.world.item.ArmorMaterial lambda$static$11();
    Code:
       0: new           #19                 // class net/minecraft/world/item/ArmorMaterial
       3: dup
       4: new           #21                 // class java/util/EnumMap
       7: dup
       8: ldc           #23                 // class net/minecraft/world/item/ArmorItem$Type
      10: invokespecial #25                 // Method java/util/EnumMap."<init>":(Ljava/lang/Class;)V
      13: invokedynamic #148,  0            // InvokeDynamic #8:accept:()Ljava/util/function/Consumer;
      18: invokestatic  #32                 // Method net/minecraft/Util.make:(Ljava/lang/Object;Ljava/util/function/Consumer;)Ljava/lang/Object;
      21: checkcast     #38                 // class java/util/Map
      24: bipush        20
      26: getstatic     #40                 // Field net/minecraft/sounds/SoundEvents.ARMOR_EQUIP_DIAMOND:Lnet/minecraft/core/Holder;
      29: invokedynamic #149,  0            // InvokeDynamic #9:get:()Ljava/util/function/Supplier;
      34: new           #50                 // class net/minecraft/world/item/ArmorMaterial$Layer
      37: dup
      38: ldc           #54                 // String epicpaladins
      40: ldc           #150                // String jade
      42: invokestatic  #58                 // Method net/minecraft/resources/ResourceLocation.fromNamespaceAndPath:(Ljava/lang/String;Ljava/lang/String;)Lnet/minecraft/resources/ResourceLocation;
      45: invokespecial #64                 // Method net/minecraft/world/item/ArmorMaterial$Layer."<init>":(Lnet/minecraft/resources/ResourceLocation;)V
      48: invokestatic  #67                 // InterfaceMethod java/util/List.of:(Ljava/lang/Object;)Ljava/util/List;
      51: ldc           #152                // float 3.5f
      53: ldc           #153                // float 0.5f
      55: invokespecial #75                 // Method net/minecraft/world/item/ArmorMaterial."<init>":(Ljava/util/Map;ILnet/minecraft/core/Holder;Ljava/util/function/Supplier;Ljava/util/List;FF)V
      58: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$10();
    Code:
       0: iconst_1
       1: anewarray     #78                 // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #154                // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.JADE_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #86                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #78                 // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #91                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static void lambda$static$9(java.util.EnumMap);
    Code:
       0: aload_0
       1: getstatic     #96                 // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
       4: iconst_5
       5: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
       8: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      11: pop
      12: aload_0
      13: getstatic     #110                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      16: bipush        8
      18: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      21: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      24: pop
      25: aload_0
      26: getstatic     #113                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      29: bipush        10
      31: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      34: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      37: pop
      38: aload_0
      39: getstatic     #116                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      42: iconst_5
      43: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      46: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      49: pop
      50: return

  private static net.minecraft.world.item.ArmorMaterial lambda$static$8();
    Code:
       0: new           #19                 // class net/minecraft/world/item/ArmorMaterial
       3: dup
       4: new           #21                 // class java/util/EnumMap
       7: dup
       8: ldc           #23                 // class net/minecraft/world/item/ArmorItem$Type
      10: invokespecial #25                 // Method java/util/EnumMap."<init>":(Ljava/lang/Class;)V
      13: invokedynamic #157,  0            // InvokeDynamic #10:accept:()Ljava/util/function/Consumer;
      18: invokestatic  #32                 // Method net/minecraft/Util.make:(Ljava/lang/Object;Ljava/util/function/Consumer;)Ljava/lang/Object;
      21: checkcast     #38                 // class java/util/Map
      24: bipush        20
      26: getstatic     #40                 // Field net/minecraft/sounds/SoundEvents.ARMOR_EQUIP_DIAMOND:Lnet/minecraft/core/Holder;
      29: invokedynamic #158,  0            // InvokeDynamic #11:get:()Ljava/util/function/Supplier;
      34: new           #50                 // class net/minecraft/world/item/ArmorMaterial$Layer
      37: dup
      38: ldc           #54                 // String epicpaladins
      40: ldc           #159                // String cryorium
      42: invokestatic  #58                 // Method net/minecraft/resources/ResourceLocation.fromNamespaceAndPath:(Ljava/lang/String;Ljava/lang/String;)Lnet/minecraft/resources/ResourceLocation;
      45: invokespecial #64                 // Method net/minecraft/world/item/ArmorMaterial$Layer."<init>":(Lnet/minecraft/resources/ResourceLocation;)V
      48: invokestatic  #67                 // InterfaceMethod java/util/List.of:(Ljava/lang/Object;)Ljava/util/List;
      51: ldc           #135                // float 4.0f
      53: ldc           #74                 // float 0.2f
      55: invokespecial #75                 // Method net/minecraft/world/item/ArmorMaterial."<init>":(Ljava/util/Map;ILnet/minecraft/core/Holder;Ljava/util/function/Supplier;Ljava/util/List;FF)V
      58: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$7();
    Code:
       0: iconst_1
       1: anewarray     #78                 // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #161                // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.CRYORIUM_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #86                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #78                 // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #91                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static void lambda$static$6(java.util.EnumMap);
    Code:
       0: aload_0
       1: getstatic     #96                 // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
       4: iconst_5
       5: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
       8: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      11: pop
      12: aload_0
      13: getstatic     #110                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      16: bipush        8
      18: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      21: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      24: pop
      25: aload_0
      26: getstatic     #113                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      29: bipush        10
      31: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      34: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      37: pop
      38: aload_0
      39: getstatic     #116                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      42: iconst_5
      43: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      46: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      49: pop
      50: return

  private static net.minecraft.world.item.ArmorMaterial lambda$static$5();
    Code:
       0: new           #19                 // class net/minecraft/world/item/ArmorMaterial
       3: dup
       4: new           #21                 // class java/util/EnumMap
       7: dup
       8: ldc           #23                 // class net/minecraft/world/item/ArmorItem$Type
      10: invokespecial #25                 // Method java/util/EnumMap."<init>":(Ljava/lang/Class;)V
      13: invokedynamic #164,  0            // InvokeDynamic #12:accept:()Ljava/util/function/Consumer;
      18: invokestatic  #32                 // Method net/minecraft/Util.make:(Ljava/lang/Object;Ljava/util/function/Consumer;)Ljava/lang/Object;
      21: checkcast     #38                 // class java/util/Map
      24: bipush        20
      26: getstatic     #40                 // Field net/minecraft/sounds/SoundEvents.ARMOR_EQUIP_DIAMOND:Lnet/minecraft/core/Holder;
      29: invokedynamic #165,  0            // InvokeDynamic #13:get:()Ljava/util/function/Supplier;
      34: new           #50                 // class net/minecraft/world/item/ArmorMaterial$Layer
      37: dup
      38: ldc           #54                 // String epicpaladins
      40: ldc           #166                // String angel
      42: invokestatic  #58                 // Method net/minecraft/resources/ResourceLocation.fromNamespaceAndPath:(Ljava/lang/String;Ljava/lang/String;)Lnet/minecraft/resources/ResourceLocation;
      45: invokespecial #64                 // Method net/minecraft/world/item/ArmorMaterial$Layer."<init>":(Lnet/minecraft/resources/ResourceLocation;)V
      48: invokestatic  #67                 // InterfaceMethod java/util/List.of:(Ljava/lang/Object;)Ljava/util/List;
      51: ldc           #123                // float 5.0f
      53: ldc           #136                // float 0.3f
      55: invokespecial #75                 // Method net/minecraft/world/item/ArmorMaterial."<init>":(Ljava/util/Map;ILnet/minecraft/core/Holder;Ljava/util/function/Supplier;Ljava/util/List;FF)V
      58: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$4();
    Code:
       0: iconst_1
       1: anewarray     #78                 // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #168                // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.ARCLIGHT_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #86                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #78                 // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #91                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static void lambda$static$3(java.util.EnumMap);
    Code:
       0: aload_0
       1: getstatic     #96                 // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
       4: bipush        7
       6: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
       9: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      12: pop
      13: aload_0
      14: getstatic     #110                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        9
      19: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      22: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      25: pop
      26: aload_0
      27: getstatic     #113                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      30: bipush        14
      32: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      35: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      38: pop
      39: aload_0
      40: getstatic     #116                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      43: bipush        8
      45: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      48: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      51: pop
      52: return

  private static net.minecraft.world.item.ArmorMaterial lambda$static$2();
    Code:
       0: new           #19                 // class net/minecraft/world/item/ArmorMaterial
       3: dup
       4: new           #21                 // class java/util/EnumMap
       7: dup
       8: ldc           #23                 // class net/minecraft/world/item/ArmorItem$Type
      10: invokespecial #25                 // Method java/util/EnumMap."<init>":(Ljava/lang/Class;)V
      13: invokedynamic #171,  0            // InvokeDynamic #14:accept:()Ljava/util/function/Consumer;
      18: invokestatic  #32                 // Method net/minecraft/Util.make:(Ljava/lang/Object;Ljava/util/function/Consumer;)Ljava/lang/Object;
      21: checkcast     #38                 // class java/util/Map
      24: bipush        20
      26: getstatic     #40                 // Field net/minecraft/sounds/SoundEvents.ARMOR_EQUIP_DIAMOND:Lnet/minecraft/core/Holder;
      29: invokedynamic #172,  0            // InvokeDynamic #15:get:()Ljava/util/function/Supplier;
      34: new           #50                 // class net/minecraft/world/item/ArmorMaterial$Layer
      37: dup
      38: ldc           #54                 // String epicpaladins
      40: ldc           #173                // String arclight
      42: invokestatic  #58                 // Method net/minecraft/resources/ResourceLocation.fromNamespaceAndPath:(Ljava/lang/String;Ljava/lang/String;)Lnet/minecraft/resources/ResourceLocation;
      45: invokespecial #64                 // Method net/minecraft/world/item/ArmorMaterial$Layer."<init>":(Lnet/minecraft/resources/ResourceLocation;)V
      48: invokestatic  #67                 // InterfaceMethod java/util/List.of:(Ljava/lang/Object;)Ljava/util/List;
      51: ldc           #135                // float 4.0f
      53: ldc           #74                 // float 0.2f
      55: invokespecial #75                 // Method net/minecraft/world/item/ArmorMaterial."<init>":(Ljava/util/Map;ILnet/minecraft/core/Holder;Ljava/util/function/Supplier;Ljava/util/List;FF)V
      58: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$1();
    Code:
       0: iconst_1
       1: anewarray     #78                 // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #168                // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.ARCLIGHT_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #86                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #78                 // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #91                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static void lambda$static$0(java.util.EnumMap);
    Code:
       0: aload_0
       1: getstatic     #96                 // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
       4: iconst_5
       5: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
       8: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      11: pop
      12: aload_0
      13: getstatic     #110                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      16: bipush        8
      18: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      21: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      24: pop
      25: aload_0
      26: getstatic     #113                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      29: bipush        10
      31: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      34: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      37: pop
      38: aload_0
      39: getstatic     #116                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      42: iconst_5
      43: invokestatic  #100                // Method java/lang/Integer.valueOf:(I)Ljava/lang/Integer;
      46: invokevirtual #106                // Method java/util/EnumMap.put:(Ljava/lang/Enum;Ljava/lang/Object;)Ljava/lang/Object;
      49: pop
      50: return

  static {};
    Code:
       0: getstatic     #175                // Field net/minecraft/core/registries/Registries.ARMOR_MATERIAL:Lnet/minecraft/resources/ResourceKey;
       3: ldc           #54                 // String epicpaladins
       5: invokestatic  #181                // Method net/neoforged/neoforge/registries/DeferredRegister.create:(Lnet/minecraft/resources/ResourceKey;Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredRegister;
       8: putstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
      11: getstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
      14: ldc           #173                // String arclight
      16: invokedynamic #185,  0            // InvokeDynamic #16:get:()Ljava/util/function/Supplier;
      21: invokevirtual #186                // Method net/neoforged/neoforge/registries/DeferredRegister.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredHolder;
      24: putstatic     #189                // Field ARCLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
      27: getstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
      30: ldc           #166                // String angel
      32: invokedynamic #193,  0            // InvokeDynamic #17:get:()Ljava/util/function/Supplier;
      37: invokevirtual #186                // Method net/neoforged/neoforge/registries/DeferredRegister.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredHolder;
      40: putstatic     #194                // Field ANGEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
      43: getstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
      46: ldc           #159                // String cryorium
      48: invokedynamic #197,  0            // InvokeDynamic #18:get:()Ljava/util/function/Supplier;
      53: invokevirtual #186                // Method net/neoforged/neoforge/registries/DeferredRegister.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredHolder;
      56: putstatic     #198                // Field CRYORIUM:Lnet/neoforged/neoforge/registries/DeferredHolder;
      59: getstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
      62: ldc           #150                // String jade
      64: invokedynamic #201,  0            // InvokeDynamic #19:get:()Ljava/util/function/Supplier;
      69: invokevirtual #186                // Method net/neoforged/neoforge/registries/DeferredRegister.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredHolder;
      72: putstatic     #202                // Field JADE:Lnet/neoforged/neoforge/registries/DeferredHolder;
      75: getstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
      78: ldc           #142                // String moonlight
      80: invokedynamic #205,  0            // InvokeDynamic #20:get:()Ljava/util/function/Supplier;
      85: invokevirtual #186                // Method net/neoforged/neoforge/registries/DeferredRegister.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredHolder;
      88: putstatic     #206                // Field MOONLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
      91: getstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
      94: ldc           #133                // String bloodstone
      96: invokedynamic #209,  0            // InvokeDynamic #21:get:()Ljava/util/function/Supplier;
     101: invokevirtual #186                // Method net/neoforged/neoforge/registries/DeferredRegister.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredHolder;
     104: putstatic     #210                // Field BLOODSTONE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     107: getstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
     110: ldc           #121                // String sculk
     112: invokedynamic #213,  0            // InvokeDynamic #22:get:()Ljava/util/function/Supplier;
     117: invokevirtual #186                // Method net/neoforged/neoforge/registries/DeferredRegister.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredHolder;
     120: putstatic     #214                // Field SCULK:Lnet/neoforged/neoforge/registries/DeferredHolder;
     123: getstatic     #7                  // Field ARMOR_MATERIALS:Lnet/neoforged/neoforge/registries/DeferredRegister;
     126: ldc           #56                 // String steel
     128: invokedynamic #217,  0            // InvokeDynamic #23:get:()Ljava/util/function/Supplier;
     133: invokevirtual #186                // Method net/neoforged/neoforge/registries/DeferredRegister.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredHolder;
     136: putstatic     #218                // Field STEEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
     139: return
}

```

### net.veroxuniverse.epicpaladins.common.registries.items.ItemMaterialsRegistry

```text
Compiled from "ItemMaterialsRegistry.java"
public class net.veroxuniverse.epicpaladins.common.registries.items.ItemMaterialsRegistry {
  public static final net.minecraft.world.item.Tier STEEL;

  public static final net.minecraft.world.item.Tier JADE;

  public static final net.minecraft.world.item.Tier ARCLIGHT;

  public static final net.minecraft.world.item.Tier MOONLIGHT;

  public static final net.minecraft.world.item.Tier SCULK;

  public static final net.minecraft.world.item.Tier BLOODSTONE;

  public static final net.minecraft.world.item.Tier CRYORIUM;

  public net.veroxuniverse.epicpaladins.common.registries.items.ItemMaterialsRegistry();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$6();
    Code:
       0: iconst_1
       1: anewarray     #7                  // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #9                  // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.CRYORIUM_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #15                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #7                  // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #21                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$5();
    Code:
       0: iconst_1
       1: anewarray     #7                  // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #27                 // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.BLOODSTONE_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #15                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #7                  // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #21                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$4();
    Code:
       0: iconst_1
       1: anewarray     #7                  // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #30                 // Field net/minecraft/world/item/Items.ECHO_SHARD:Lnet/minecraft/world/item/Item;
       9: aastore
      10: invokestatic  #21                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      13: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$3();
    Code:
       0: iconst_1
       1: anewarray     #7                  // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #36                 // Field net/minecraft/world/item/Items.DIAMOND:Lnet/minecraft/world/item/Item;
       9: aastore
      10: invokestatic  #21                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      13: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$2();
    Code:
       0: iconst_1
       1: anewarray     #7                  // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #39                 // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.ARCLIGHT_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #15                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #7                  // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #21                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$1();
    Code:
       0: iconst_1
       1: anewarray     #7                  // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #42                 // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.JADE_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #15                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #7                  // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #21                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  private static net.minecraft.world.item.crafting.Ingredient lambda$static$0();
    Code:
       0: iconst_1
       1: anewarray     #7                  // class net/minecraft/world/level/ItemLike
       4: dup
       5: iconst_0
       6: getstatic     #45                 // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.STEEL_INGOT:Lnet/neoforged/neoforge/registries/DeferredItem;
       9: invokevirtual #15                 // Method net/neoforged/neoforge/registries/DeferredItem.get:()Ljava/lang/Object;
      12: checkcast     #7                  // class net/minecraft/world/level/ItemLike
      15: aastore
      16: invokestatic  #21                 // Method net/minecraft/world/item/crafting/Ingredient.of:([Lnet/minecraft/world/level/ItemLike;)Lnet/minecraft/world/item/crafting/Ingredient;
      19: areturn

  static {};
    Code:
       0: new           #48                 // class net/veroxuniverse/epicpaladins/common/registries/CustomTier
       3: dup
       4: iconst_3
       5: ldc           #50                 // float 12.0f
       7: fconst_0
       8: bipush        12
      10: getstatic     #51                 // Field net/minecraft/tags/BlockTags.NEEDS_IRON_TOOL:Lnet/minecraft/tags/TagKey;
      13: invokedynamic #57,  0             // InvokeDynamic #0:get:()Ljava/util/function/Supplier;
      18: invokespecial #60                 // Method net/veroxuniverse/epicpaladins/common/registries/CustomTier."<init>":(IFFILnet/minecraft/tags/TagKey;Ljava/util/function/Supplier;)V
      21: putstatic     #63                 // Field STEEL:Lnet/minecraft/world/item/Tier;
      24: new           #48                 // class net/veroxuniverse/epicpaladins/common/registries/CustomTier
      27: dup
      28: iconst_4
      29: ldc           #50                 // float 12.0f
      31: fconst_0
      32: bipush        25
      34: getstatic     #51                 // Field net/minecraft/tags/BlockTags.NEEDS_IRON_TOOL:Lnet/minecraft/tags/TagKey;
      37: invokedynamic #69,  0             // InvokeDynamic #1:get:()Ljava/util/function/Supplier;
      42: invokespecial #60                 // Method net/veroxuniverse/epicpaladins/common/registries/CustomTier."<init>":(IFFILnet/minecraft/tags/TagKey;Ljava/util/function/Supplier;)V
      45: putstatic     #70                 // Field JADE:Lnet/minecraft/world/item/Tier;
      48: new           #48                 // class net/veroxuniverse/epicpaladins/common/registries/CustomTier
      51: dup
      52: iconst_4
      53: ldc           #50                 // float 12.0f
      55: fconst_0
      56: bipush        25
      58: getstatic     #51                 // Field net/minecraft/tags/BlockTags.NEEDS_IRON_TOOL:Lnet/minecraft/tags/TagKey;
      61: invokedynamic #73,  0             // InvokeDynamic #2:get:()Ljava/util/function/Supplier;
      66: invokespecial #60                 // Method net/veroxuniverse/epicpaladins/common/registries/CustomTier."<init>":(IFFILnet/minecraft/tags/TagKey;Ljava/util/function/Supplier;)V
      69: putstatic     #74                 // Field ARCLIGHT:Lnet/minecraft/world/item/Tier;
      72: new           #48                 // class net/veroxuniverse/epicpaladins/common/registries/CustomTier
      75: dup
      76: iconst_4
      77: ldc           #50                 // float 12.0f
      79: ldc           #77                 // float 5.0f
      81: bipush        30
      83: getstatic     #51                 // Field net/minecraft/tags/BlockTags.NEEDS_IRON_TOOL:Lnet/minecraft/tags/TagKey;
      86: invokedynamic #78,  0             // InvokeDynamic #3:get:()Ljava/util/function/Supplier;
      91: invokespecial #60                 // Method net/veroxuniverse/epicpaladins/common/registries/CustomTier."<init>":(IFFILnet/minecraft/tags/TagKey;Ljava/util/function/Supplier;)V
      94: putstatic     #79                 // Field MOONLIGHT:Lnet/minecraft/world/item/Tier;
      97: new           #48                 // class net/veroxuniverse/epicpaladins/common/registries/CustomTier
     100: dup
     101: iconst_4
     102: ldc           #50                 // float 12.0f
     104: fconst_0
     105: bipush        25
     107: getstatic     #51                 // Field net/minecraft/tags/BlockTags.NEEDS_IRON_TOOL:Lnet/minecraft/tags/TagKey;
     110: invokedynamic #82,  0             // InvokeDynamic #4:get:()Ljava/util/function/Supplier;
     115: invokespecial #60                 // Method net/veroxuniverse/epicpaladins/common/registries/CustomTier."<init>":(IFFILnet/minecraft/tags/TagKey;Ljava/util/function/Supplier;)V
     118: putstatic     #83                 // Field SCULK:Lnet/minecraft/world/item/Tier;
     121: new           #48                 // class net/veroxuniverse/epicpaladins/common/registries/CustomTier
     124: dup
     125: iconst_4
     126: ldc           #50                 // float 12.0f
     128: fconst_0
     129: bipush        25
     131: getstatic     #51                 // Field net/minecraft/tags/BlockTags.NEEDS_IRON_TOOL:Lnet/minecraft/tags/TagKey;
     134: invokedynamic #86,  0             // InvokeDynamic #5:get:()Ljava/util/function/Supplier;
     139: invokespecial #60                 // Method net/veroxuniverse/epicpaladins/common/registries/CustomTier."<init>":(IFFILnet/minecraft/tags/TagKey;Ljava/util/function/Supplier;)V
     142: putstatic     #87                 // Field BLOODSTONE:Lnet/minecraft/world/item/Tier;
     145: new           #48                 // class net/veroxuniverse/epicpaladins/common/registries/CustomTier
     148: dup
     149: iconst_4
     150: ldc           #50                 // float 12.0f
     152: fconst_0
     153: bipush        25
     155: getstatic     #51                 // Field net/minecraft/tags/BlockTags.NEEDS_IRON_TOOL:Lnet/minecraft/tags/TagKey;
     158: invokedynamic #90,  0             // InvokeDynamic #6:get:()Ljava/util/function/Supplier;
     163: invokespecial #60                 // Method net/veroxuniverse/epicpaladins/common/registries/CustomTier."<init>":(IFFILnet/minecraft/tags/TagKey;Ljava/util/function/Supplier;)V
     166: putstatic     #91                 // Field CRYORIUM:Lnet/minecraft/world/item/Tier;
     169: return
}

```

### net.veroxuniverse.epicpaladins.common.registries.ItemsRegistry

```text
Compiled from "ItemsRegistry.java"
public class net.veroxuniverse.epicpaladins.common.registries.ItemsRegistry {
  public static final net.neoforged.neoforge.registries.DeferredRegister$Items ITEMS;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> ARCLIGHT_GEM;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> MOONLIGHT_GEM;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> JADE_GEM;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> BLOODSTONE_GEM;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> CRYORIUM_GEM;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> STEEL_INGOT;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> STEEL_NUGGET;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> ARCLIGHT_TEMPLATE;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> BLOODSTONE_TEMPLATE;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> CRYORIUM_TEMPLATE;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> JADE_TEMPLATE;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> MOONLIGHT_TEMPLATE;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> SCULK_TEMPLATE;

  public static final net.neoforged.neoforge.registries.DeferredItem<net.minecraft.world.item.Item> ANGEL_FEATHER;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ARCLIGHT_HELMET;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ARCLIGHT_CHESTPLATE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ARCLIGHT_LEGGINGS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ARCLIGHT_BOOTS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ANGEL_HELMET;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ANGEL_CHESTPLATE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ANGEL_LEGGINGS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ANGEL_BOOTS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ASSASSIN_HELMET;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ASSASSIN_CHESTPLATE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ASSASSIN_LEGGINGS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ASSASSIN_BOOTS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> BLOODSTONE_HELMET;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> BLOODSTONE_CHESTPLATE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> BLOODSTONE_LEGGINGS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> BLOODSTONE_BOOTS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_HELMET;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_CHESTPLATE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_LEGGINGS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_BOOTS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> JADE_HELMET;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> JADE_CHESTPLATE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> JADE_LEGGINGS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> JADE_BOOTS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> KNIGHT_HELMET;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> KNIGHT_CHESTPLATE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> KNIGHT_LEGGINGS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> KNIGHT_BOOTS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_HELMET;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_CHESTPLATE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_LEGGINGS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_BOOTS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> SCULK_HELMET;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> SCULK_CHESTPLATE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> SCULK_LEGGINGS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> SCULK_BOOTS;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ARCLIGHT_SWORD;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ARCLIGHT_PICKAXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ARCLIGHT_AXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ARCLIGHT_SHOVEL;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ARCLIGHT_HOE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> JADE_SWORD;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> JADE_PICKAXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> JADE_AXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> JADE_SHOVEL;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> JADE_HOE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_SWORD;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_PICKAXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_AXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_SHOVEL;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_HOE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> BLOODSTONE_SWORD;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> BLOODSTONE_PICKAXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> BLOODSTONE_AXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> BLOODSTONE_SHOVEL;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> BLOODSTONE_HOE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_SWORD;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_PICKAXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_AXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_SHOVEL;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_HOE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> SCULK_SWORD;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> SCULK_PICKAXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> SCULK_AXE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> SCULK_SHOVEL;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> SCULK_HOE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> ANGEL_SWORD;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> MOONLIGHT_GLAIVE;

  public static final net.neoforged.neoforge.registries.DeferredHolder<net.minecraft.world.item.Item, net.minecraft.world.item.Item> CRYORIUM_BATTLE_AXE;

  public net.veroxuniverse.epicpaladins.common.registries.ItemsRegistry();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  public static void register(net.neoforged.bus.api.IEventBus);
    Code:
       0: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
       3: aload_0
       4: invokevirtual #13                 // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Lnet/neoforged/bus/api/IEventBus;)V
       7: return

  private static net.minecraft.world.item.Item lambda$static$69();
    Code:
       0: new           #19                 // class net/veroxuniverse/epicpaladins/common/items/weapons/CryoriumAxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #30                 // float 12.0f
      19: ldc           #31                 // float -3.0f
      21: invokestatic  #32                 // Method net/minecraft/world/item/AxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: getstatic     #42                 // Field net/minecraft/world/item/Rarity.EPIC:Lnet/minecraft/world/item/Rarity;
      30: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      33: invokespecial #52                 // Method net/veroxuniverse/epicpaladins/common/items/weapons/CryoriumAxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      36: areturn

  private static net.minecraft.world.item.Item lambda$static$68();
    Code:
       0: new           #55                 // class net/veroxuniverse/epicpaladins/common/items/weapons/MoonlightGlaiveItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: bipush        10
      19: ldc           #57                 // float -2.5f
      21: invokestatic  #58                 // Method net/minecraft/world/item/SwordItem.createAttributes:(Lnet/minecraft/world/item/Tier;IF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: getstatic     #42                 // Field net/minecraft/world/item/Rarity.EPIC:Lnet/minecraft/world/item/Rarity;
      30: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      33: invokespecial #63                 // Method net/veroxuniverse/epicpaladins/common/items/weapons/MoonlightGlaiveItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      36: areturn

  private static net.minecraft.world.item.Item lambda$static$67();
    Code:
       0: new           #64                 // class net/veroxuniverse/epicpaladins/common/items/weapons/AngelSwordItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: bipush        10
      19: ldc           #66                 // float -2.1f
      21: invokestatic  #58                 // Method net/minecraft/world/item/SwordItem.createAttributes:(Lnet/minecraft/world/item/Tier;IF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: getstatic     #42                 // Field net/minecraft/world/item/Rarity.EPIC:Lnet/minecraft/world/item/Rarity;
      30: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      33: invokespecial #67                 // Method net/veroxuniverse/epicpaladins/common/items/weapons/AngelSwordItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      36: areturn

  private static net.minecraft.world.item.Item lambda$static$66();
    Code:
       0: new           #68                 // class net/minecraft/world/item/HoeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: fconst_2
      18: ldc           #70                 // float 0.5f
      20: invokestatic  #71                 // Method net/minecraft/world/item/HoeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        2000
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #79                 // Method net/minecraft/world/item/HoeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$65();
    Code:
       0: new           #80                 // class net/minecraft/world/item/ShovelItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #82                 // float 6.0f
      19: ldc           #83                 // float -2.2f
      21: invokestatic  #84                 // Method net/minecraft/world/item/ShovelItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #85                 // Method net/minecraft/world/item/ShovelItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$64();
    Code:
       0: new           #33                 // class net/minecraft/world/item/AxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #86                 // float 9.0f
      19: ldc           #87                 // float -2.8f
      21: invokestatic  #32                 // Method net/minecraft/world/item/AxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #88                 // Method net/minecraft/world/item/AxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$63();
    Code:
       0: new           #89                 // class net/minecraft/world/item/PickaxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #91                 // float 5.0f
      19: ldc           #57                 // float -2.5f
      21: invokestatic  #92                 // Method net/minecraft/world/item/PickaxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #93                 // Method net/minecraft/world/item/PickaxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$62();
    Code:
       0: new           #59                 // class net/minecraft/world/item/SwordItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: iconst_4
      18: ldc           #83                 // float -2.2f
      20: invokestatic  #58                 // Method net/minecraft/world/item/SwordItem.createAttributes:(Lnet/minecraft/world/item/Tier;IF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        1750
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #94                 // Method net/minecraft/world/item/SwordItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$61();
    Code:
       0: new           #68                 // class net/minecraft/world/item/HoeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: fconst_2
      18: ldc           #70                 // float 0.5f
      20: invokestatic  #71                 // Method net/minecraft/world/item/HoeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        1750
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #79                 // Method net/minecraft/world/item/HoeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$60();
    Code:
       0: new           #80                 // class net/minecraft/world/item/ShovelItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #82                 // float 6.0f
      19: ldc           #83                 // float -2.2f
      21: invokestatic  #84                 // Method net/minecraft/world/item/ShovelItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #85                 // Method net/minecraft/world/item/ShovelItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$59();
    Code:
       0: new           #33                 // class net/minecraft/world/item/AxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #86                 // float 9.0f
      19: ldc           #87                 // float -2.8f
      21: invokestatic  #32                 // Method net/minecraft/world/item/AxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #88                 // Method net/minecraft/world/item/AxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$58();
    Code:
       0: new           #89                 // class net/minecraft/world/item/PickaxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #91                 // float 5.0f
      19: ldc           #57                 // float -2.5f
      21: invokestatic  #92                 // Method net/minecraft/world/item/PickaxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #93                 // Method net/minecraft/world/item/PickaxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$57();
    Code:
       0: new           #59                 // class net/minecraft/world/item/SwordItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: iconst_4
      18: ldc           #83                 // float -2.2f
      20: invokestatic  #58                 // Method net/minecraft/world/item/SwordItem.createAttributes:(Lnet/minecraft/world/item/Tier;IF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        1750
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #94                 // Method net/minecraft/world/item/SwordItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$56();
    Code:
       0: new           #68                 // class net/minecraft/world/item/HoeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: fconst_2
      18: ldc           #70                 // float 0.5f
      20: invokestatic  #71                 // Method net/minecraft/world/item/HoeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        1750
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #79                 // Method net/minecraft/world/item/HoeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$55();
    Code:
       0: new           #80                 // class net/minecraft/world/item/ShovelItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #82                 // float 6.0f
      19: ldc           #83                 // float -2.2f
      21: invokestatic  #84                 // Method net/minecraft/world/item/ShovelItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #85                 // Method net/minecraft/world/item/ShovelItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$54();
    Code:
       0: new           #33                 // class net/minecraft/world/item/AxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #86                 // float 9.0f
      19: ldc           #87                 // float -2.8f
      21: invokestatic  #32                 // Method net/minecraft/world/item/AxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #88                 // Method net/minecraft/world/item/AxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$53();
    Code:
       0: new           #89                 // class net/minecraft/world/item/PickaxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #91                 // float 5.0f
      19: ldc           #57                 // float -2.5f
      21: invokestatic  #92                 // Method net/minecraft/world/item/PickaxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #93                 // Method net/minecraft/world/item/PickaxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$52();
    Code:
       0: new           #59                 // class net/minecraft/world/item/SwordItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: iconst_4
      18: ldc           #83                 // float -2.2f
      20: invokestatic  #58                 // Method net/minecraft/world/item/SwordItem.createAttributes:(Lnet/minecraft/world/item/Tier;IF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        1750
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #94                 // Method net/minecraft/world/item/SwordItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$51();
    Code:
       0: new           #68                 // class net/minecraft/world/item/HoeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: fconst_2
      18: ldc           #70                 // float 0.5f
      20: invokestatic  #71                 // Method net/minecraft/world/item/HoeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        1750
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #79                 // Method net/minecraft/world/item/HoeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$50();
    Code:
       0: new           #80                 // class net/minecraft/world/item/ShovelItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #82                 // float 6.0f
      19: ldc           #83                 // float -2.2f
      21: invokestatic  #84                 // Method net/minecraft/world/item/ShovelItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #85                 // Method net/minecraft/world/item/ShovelItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$49();
    Code:
       0: new           #33                 // class net/minecraft/world/item/AxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #86                 // float 9.0f
      19: ldc           #87                 // float -2.8f
      21: invokestatic  #32                 // Method net/minecraft/world/item/AxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #88                 // Method net/minecraft/world/item/AxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$48();
    Code:
       0: new           #89                 // class net/minecraft/world/item/PickaxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #91                 // float 5.0f
      19: ldc           #57                 // float -2.5f
      21: invokestatic  #92                 // Method net/minecraft/world/item/PickaxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #93                 // Method net/minecraft/world/item/PickaxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$47();
    Code:
       0: new           #59                 // class net/minecraft/world/item/SwordItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: iconst_4
      18: ldc           #83                 // float -2.2f
      20: invokestatic  #58                 // Method net/minecraft/world/item/SwordItem.createAttributes:(Lnet/minecraft/world/item/Tier;IF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        1750
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #94                 // Method net/minecraft/world/item/SwordItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$46();
    Code:
       0: new           #68                 // class net/minecraft/world/item/HoeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: fconst_2
      18: ldc           #70                 // float 0.5f
      20: invokestatic  #71                 // Method net/minecraft/world/item/HoeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        1750
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #79                 // Method net/minecraft/world/item/HoeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$45();
    Code:
       0: new           #80                 // class net/minecraft/world/item/ShovelItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #82                 // float 6.0f
      19: ldc           #83                 // float -2.2f
      21: invokestatic  #84                 // Method net/minecraft/world/item/ShovelItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #85                 // Method net/minecraft/world/item/ShovelItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$44();
    Code:
       0: new           #33                 // class net/minecraft/world/item/AxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #86                 // float 9.0f
      19: ldc           #87                 // float -2.8f
      21: invokestatic  #32                 // Method net/minecraft/world/item/AxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #88                 // Method net/minecraft/world/item/AxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$43();
    Code:
       0: new           #89                 // class net/minecraft/world/item/PickaxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #91                 // float 5.0f
      19: ldc           #57                 // float -2.5f
      21: invokestatic  #92                 // Method net/minecraft/world/item/PickaxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: sipush        1750
      30: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      33: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      36: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      39: invokespecial #93                 // Method net/minecraft/world/item/PickaxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      42: areturn

  private static net.minecraft.world.item.Item lambda$static$42();
    Code:
       0: new           #59                 // class net/minecraft/world/item/SwordItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: iconst_4
      18: ldc           #83                 // float -2.2f
      20: invokestatic  #58                 // Method net/minecraft/world/item/SwordItem.createAttributes:(Lnet/minecraft/world/item/Tier;IF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: sipush        1750
      29: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      32: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      35: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      38: invokespecial #94                 // Method net/minecraft/world/item/SwordItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      41: areturn

  private static net.minecraft.world.item.Item lambda$static$41();
    Code:
       0: new           #68                 // class net/minecraft/world/item/HoeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: fconst_2
      18: ldc           #70                 // float 0.5f
      20: invokestatic  #71                 // Method net/minecraft/world/item/HoeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      29: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      32: invokespecial #79                 // Method net/minecraft/world/item/HoeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      35: areturn

  private static net.minecraft.world.item.Item lambda$static$40();
    Code:
       0: new           #80                 // class net/minecraft/world/item/ShovelItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #82                 // float 6.0f
      19: ldc           #83                 // float -2.2f
      21: invokestatic  #84                 // Method net/minecraft/world/item/ShovelItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      30: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      33: invokespecial #85                 // Method net/minecraft/world/item/ShovelItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      36: areturn

  private static net.minecraft.world.item.Item lambda$static$39();
    Code:
       0: new           #33                 // class net/minecraft/world/item/AxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #86                 // float 9.0f
      19: ldc           #87                 // float -2.8f
      21: invokestatic  #32                 // Method net/minecraft/world/item/AxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      30: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      33: invokespecial #88                 // Method net/minecraft/world/item/AxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      36: areturn

  private static net.minecraft.world.item.Item lambda$static$38();
    Code:
       0: new           #89                 // class net/minecraft/world/item/PickaxeItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: ldc           #91                 // float 5.0f
      19: ldc           #57                 // float -2.5f
      21: invokestatic  #92                 // Method net/minecraft/world/item/PickaxeItem.createAttributes:(Lnet/minecraft/world/item/Tier;FF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      24: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      27: getstatic     #95                 // Field net/minecraft/world/item/Rarity.UNCOMMON:Lnet/minecraft/world/item/Rarity;
      30: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      33: invokespecial #93                 // Method net/minecraft/world/item/PickaxeItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      36: areturn

  private static net.minecraft.world.item.Item lambda$static$37();
    Code:
       0: new           #59                 // class net/minecraft/world/item/SwordItem
       3: dup
       4: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
       7: new           #27                 // class net/minecraft/world/item/Item$Properties
      10: dup
      11: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      14: getstatic     #21                 // Field net/minecraft/world/item/Tiers.NETHERITE:Lnet/minecraft/world/item/Tiers;
      17: iconst_4
      18: ldc           #83                 // float -2.2f
      20: invokestatic  #58                 // Method net/minecraft/world/item/SwordItem.createAttributes:(Lnet/minecraft/world/item/Tier;IF)Lnet/minecraft/world/item/component/ItemAttributeModifiers;
      23: invokevirtual #38                 // Method net/minecraft/world/item/Item$Properties.attributes:(Lnet/minecraft/world/item/component/ItemAttributeModifiers;)Lnet/minecraft/world/item/Item$Properties;
      26: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      29: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      32: invokespecial #94                 // Method net/minecraft/world/item/SwordItem."<init>":(Lnet/minecraft/world/item/Tier;Lnet/minecraft/world/item/Item$Properties;)V
      35: areturn

  private static net.minecraft.world.item.Item lambda$static$36();
    Code:
       0: new           #98                 // class net/veroxuniverse/epicpaladins/common/items/armorItems/SculkArmorItem
       3: dup
       4: getstatic     #100                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.SCULK:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #121                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/SculkArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$35();
    Code:
       0: new           #98                 // class net/veroxuniverse/epicpaladins/common/items/armorItems/SculkArmorItem
       3: dup
       4: getstatic     #100                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.SCULK:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #121                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/SculkArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$34();
    Code:
       0: new           #98                 // class net/veroxuniverse/epicpaladins/common/items/armorItems/SculkArmorItem
       3: dup
       4: getstatic     #100                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.SCULK:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #121                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/SculkArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$33();
    Code:
       0: new           #98                 // class net/veroxuniverse/epicpaladins/common/items/armorItems/SculkArmorItem
       3: dup
       4: getstatic     #100                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.SCULK:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #121                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/SculkArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$32();
    Code:
       0: new           #133                // class net/veroxuniverse/epicpaladins/common/items/armorItems/MoonlightArmorItem
       3: dup
       4: getstatic     #135                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.MOONLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #138                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/MoonlightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$31();
    Code:
       0: new           #133                // class net/veroxuniverse/epicpaladins/common/items/armorItems/MoonlightArmorItem
       3: dup
       4: getstatic     #135                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.MOONLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #138                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/MoonlightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$30();
    Code:
       0: new           #133                // class net/veroxuniverse/epicpaladins/common/items/armorItems/MoonlightArmorItem
       3: dup
       4: getstatic     #135                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.MOONLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #138                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/MoonlightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$29();
    Code:
       0: new           #133                // class net/veroxuniverse/epicpaladins/common/items/armorItems/MoonlightArmorItem
       3: dup
       4: getstatic     #135                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.MOONLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #138                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/MoonlightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$28();
    Code:
       0: new           #139                // class net/veroxuniverse/epicpaladins/common/items/armorItems/KnightArmorItem
       3: dup
       4: getstatic     #141                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.STEEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #144                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/KnightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$27();
    Code:
       0: new           #139                // class net/veroxuniverse/epicpaladins/common/items/armorItems/KnightArmorItem
       3: dup
       4: getstatic     #141                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.STEEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #144                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/KnightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$26();
    Code:
       0: new           #139                // class net/veroxuniverse/epicpaladins/common/items/armorItems/KnightArmorItem
       3: dup
       4: getstatic     #141                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.STEEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #144                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/KnightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$25();
    Code:
       0: new           #139                // class net/veroxuniverse/epicpaladins/common/items/armorItems/KnightArmorItem
       3: dup
       4: getstatic     #141                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.STEEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #144                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/KnightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$24();
    Code:
       0: new           #145                // class net/veroxuniverse/epicpaladins/common/items/armorItems/JadeArmorItem
       3: dup
       4: getstatic     #147                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.JADE:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #150                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/JadeArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$23();
    Code:
       0: new           #145                // class net/veroxuniverse/epicpaladins/common/items/armorItems/JadeArmorItem
       3: dup
       4: getstatic     #147                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.JADE:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #150                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/JadeArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$22();
    Code:
       0: new           #145                // class net/veroxuniverse/epicpaladins/common/items/armorItems/JadeArmorItem
       3: dup
       4: getstatic     #147                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.JADE:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #150                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/JadeArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$21();
    Code:
       0: new           #145                // class net/veroxuniverse/epicpaladins/common/items/armorItems/JadeArmorItem
       3: dup
       4: getstatic     #147                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.JADE:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #150                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/JadeArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$20();
    Code:
       0: new           #151                // class net/veroxuniverse/epicpaladins/common/items/armorItems/CryoriumArmorItem
       3: dup
       4: getstatic     #153                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.CRYORIUM:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #156                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/CryoriumArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$19();
    Code:
       0: new           #151                // class net/veroxuniverse/epicpaladins/common/items/armorItems/CryoriumArmorItem
       3: dup
       4: getstatic     #153                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.CRYORIUM:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #156                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/CryoriumArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$18();
    Code:
       0: new           #151                // class net/veroxuniverse/epicpaladins/common/items/armorItems/CryoriumArmorItem
       3: dup
       4: getstatic     #153                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.CRYORIUM:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #156                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/CryoriumArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$17();
    Code:
       0: new           #151                // class net/veroxuniverse/epicpaladins/common/items/armorItems/CryoriumArmorItem
       3: dup
       4: getstatic     #153                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.CRYORIUM:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #156                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/CryoriumArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$16();
    Code:
       0: new           #157                // class net/veroxuniverse/epicpaladins/common/items/armorItems/BloodstoneArmorItem
       3: dup
       4: getstatic     #159                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.BLOODSTONE:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #162                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/BloodstoneArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$15();
    Code:
       0: new           #157                // class net/veroxuniverse/epicpaladins/common/items/armorItems/BloodstoneArmorItem
       3: dup
       4: getstatic     #159                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.BLOODSTONE:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #162                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/BloodstoneArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$14();
    Code:
       0: new           #157                // class net/veroxuniverse/epicpaladins/common/items/armorItems/BloodstoneArmorItem
       3: dup
       4: getstatic     #159                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.BLOODSTONE:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #162                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/BloodstoneArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$13();
    Code:
       0: new           #157                // class net/veroxuniverse/epicpaladins/common/items/armorItems/BloodstoneArmorItem
       3: dup
       4: getstatic     #159                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.BLOODSTONE:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #162                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/BloodstoneArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$12();
    Code:
       0: new           #163                // class net/veroxuniverse/epicpaladins/common/items/armorItems/AssassinArmorItem
       3: dup
       4: getstatic     #141                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.STEEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #165                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/AssassinArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$11();
    Code:
       0: new           #163                // class net/veroxuniverse/epicpaladins/common/items/armorItems/AssassinArmorItem
       3: dup
       4: getstatic     #141                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.STEEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #165                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/AssassinArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$10();
    Code:
       0: new           #163                // class net/veroxuniverse/epicpaladins/common/items/armorItems/AssassinArmorItem
       3: dup
       4: getstatic     #141                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.STEEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #165                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/AssassinArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$9();
    Code:
       0: new           #163                // class net/veroxuniverse/epicpaladins/common/items/armorItems/AssassinArmorItem
       3: dup
       4: getstatic     #141                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.STEEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #165                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/AssassinArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$8();
    Code:
       0: new           #166                // class net/veroxuniverse/epicpaladins/common/items/armorItems/AngelArmorItem
       3: dup
       4: getstatic     #168                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.ANGEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #42                 // Field net/minecraft/world/item/Rarity.EPIC:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #171                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/AngelArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$7();
    Code:
       0: new           #166                // class net/veroxuniverse/epicpaladins/common/items/armorItems/AngelArmorItem
       3: dup
       4: getstatic     #168                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.ANGEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #42                 // Field net/minecraft/world/item/Rarity.EPIC:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #171                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/AngelArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$6();
    Code:
       0: new           #166                // class net/veroxuniverse/epicpaladins/common/items/armorItems/AngelArmorItem
       3: dup
       4: getstatic     #168                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.ANGEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #42                 // Field net/minecraft/world/item/Rarity.EPIC:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #171                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/AngelArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$5();
    Code:
       0: new           #166                // class net/veroxuniverse/epicpaladins/common/items/armorItems/AngelArmorItem
       3: dup
       4: getstatic     #168                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.ANGEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #42                 // Field net/minecraft/world/item/Rarity.EPIC:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #171                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/AngelArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$4();
    Code:
       0: new           #172                // class net/veroxuniverse/epicpaladins/common/items/armorItems/ArclightArmorItem
       3: dup
       4: getstatic     #174                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.ARCLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #106                // Field net/minecraft/world/item/ArmorItem$Type.BOOTS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #177                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/ArclightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$3();
    Code:
       0: new           #172                // class net/veroxuniverse/epicpaladins/common/items/armorItems/ArclightArmorItem
       3: dup
       4: getstatic     #174                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.ARCLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #124                // Field net/minecraft/world/item/ArmorItem$Type.LEGGINGS:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #177                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/ArclightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$2();
    Code:
       0: new           #172                // class net/veroxuniverse/epicpaladins/common/items/armorItems/ArclightArmorItem
       3: dup
       4: getstatic     #174                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.ARCLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #127                // Field net/minecraft/world/item/ArmorItem$Type.CHESTPLATE:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #177                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/ArclightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$1();
    Code:
       0: new           #172                // class net/veroxuniverse/epicpaladins/common/items/armorItems/ArclightArmorItem
       3: dup
       4: getstatic     #174                // Field net/veroxuniverse/epicpaladins/common/registries/items/ArmorMaterialsRegistry.ARCLIGHT:Lnet/neoforged/neoforge/registries/DeferredHolder;
       7: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      10: iconst_1
      11: invokestatic  #112                // Method net/veroxuniverse/epicpaladins/common/registries/ItemPropertiesHelper.equipment:(I)Lnet/minecraft/world/item/Item$Properties;
      14: getstatic     #130                // Field net/minecraft/world/item/ArmorItem$Type.HELMET:Lnet/minecraft/world/item/ArmorItem$Type;
      17: bipush        22
      19: invokevirtual #117                // Method net/minecraft/world/item/ArmorItem$Type.getDurability:(I)I
      22: invokevirtual #72                 // Method net/minecraft/world/item/Item$Properties.durability:(I)Lnet/minecraft/world/item/Item$Properties;
      25: getstatic     #76                 // Field net/minecraft/world/item/Rarity.RARE:Lnet/minecraft/world/item/Rarity;
      28: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      31: invokespecial #177                // Method net/veroxuniverse/epicpaladins/common/items/armorItems/ArclightArmorItem."<init>":(Lnet/minecraft/core/Holder;Lnet/minecraft/world/item/ArmorItem$Type;Lnet/minecraft/world/item/Item$Properties;)V
      34: areturn

  private static net.minecraft.world.item.Item lambda$static$0();
    Code:
       0: new           #178                // class net/minecraft/world/item/Item
       3: dup
       4: new           #27                 // class net/minecraft/world/item/Item$Properties
       7: dup
       8: invokespecial #29                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      11: getstatic     #42                 // Field net/minecraft/world/item/Rarity.EPIC:Lnet/minecraft/world/item/Rarity;
      14: invokevirtual #48                 // Method net/minecraft/world/item/Item$Properties.rarity:(Lnet/minecraft/world/item/Rarity;)Lnet/minecraft/world/item/Item$Properties;
      17: invokespecial #180                // Method net/minecraft/world/item/Item."<init>":(Lnet/minecraft/world/item/Item$Properties;)V
      20: areturn

  static {};
    Code:
       0: ldc           #185                // String epicpaladins
       2: invokestatic  #187                // Method net/neoforged/neoforge/registries/DeferredRegister.createItems:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
       5: putstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
       8: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
      11: ldc           #193                // String arclight_gem
      13: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
      16: putstatic     #199                // Field ARCLIGHT_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
      19: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
      22: ldc           #203                // String moonlight_gem
      24: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
      27: putstatic     #205                // Field MOONLIGHT_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
      30: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
      33: ldc           #208                // String jade_gem
      35: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
      38: putstatic     #210                // Field JADE_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
      41: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
      44: ldc           #213                // String bloodstone_gem
      46: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
      49: putstatic     #215                // Field BLOODSTONE_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
      52: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
      55: ldc           #218                // String cryorium_gem
      57: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
      60: putstatic     #220                // Field CRYORIUM_GEM:Lnet/neoforged/neoforge/registries/DeferredItem;
      63: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
      66: ldc           #223                // String steel_ingot
      68: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
      71: putstatic     #225                // Field STEEL_INGOT:Lnet/neoforged/neoforge/registries/DeferredItem;
      74: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
      77: ldc           #228                // String steel_nugget
      79: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
      82: putstatic     #230                // Field STEEL_NUGGET:Lnet/neoforged/neoforge/registries/DeferredItem;
      85: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
      88: ldc           #233                // String arclight_template
      90: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
      93: putstatic     #235                // Field ARCLIGHT_TEMPLATE:Lnet/neoforged/neoforge/registries/DeferredItem;
      96: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
      99: ldc           #238                // String bloodstone_template
     101: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
     104: putstatic     #240                // Field BLOODSTONE_TEMPLATE:Lnet/neoforged/neoforge/registries/DeferredItem;
     107: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     110: ldc           #243                // String cryorium_template
     112: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
     115: putstatic     #245                // Field CRYORIUM_TEMPLATE:Lnet/neoforged/neoforge/registries/DeferredItem;
     118: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     121: ldc           #248                // String jade_template
     123: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
     126: putstatic     #250                // Field JADE_TEMPLATE:Lnet/neoforged/neoforge/registries/DeferredItem;
     129: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     132: ldc           #253                // String moonlight_template
     134: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
     137: putstatic     #255                // Field MOONLIGHT_TEMPLATE:Lnet/neoforged/neoforge/registries/DeferredItem;
     140: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     143: ldc_w         #258                // String sculk_template
     146: invokevirtual #195                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.registerSimpleItem:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredItem;
     149: putstatic     #260                // Field SCULK_TEMPLATE:Lnet/neoforged/neoforge/registries/DeferredItem;
     152: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     155: ldc_w         #263                // String angel_feather
     158: invokedynamic #265,  0            // InvokeDynamic #0:get:()Ljava/util/function/Supplier;
     163: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     166: putstatic     #272                // Field ANGEL_FEATHER:Lnet/neoforged/neoforge/registries/DeferredItem;
     169: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     172: ldc_w         #275                // String arclight_helmet
     175: invokedynamic #277,  0            // InvokeDynamic #1:get:()Ljava/util/function/Supplier;
     180: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     183: putstatic     #278                // Field ARCLIGHT_HELMET:Lnet/neoforged/neoforge/registries/DeferredHolder;
     186: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     189: ldc_w         #281                // String arclight_chestplate
     192: invokedynamic #283,  0            // InvokeDynamic #2:get:()Ljava/util/function/Supplier;
     197: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     200: putstatic     #284                // Field ARCLIGHT_CHESTPLATE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     203: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     206: ldc_w         #287                // String arclight_leggings
     209: invokedynamic #289,  0            // InvokeDynamic #3:get:()Ljava/util/function/Supplier;
     214: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     217: putstatic     #290                // Field ARCLIGHT_LEGGINGS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     220: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     223: ldc_w         #293                // String arclight_boots
     226: invokedynamic #295,  0            // InvokeDynamic #4:get:()Ljava/util/function/Supplier;
     231: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     234: putstatic     #296                // Field ARCLIGHT_BOOTS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     237: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     240: ldc_w         #299                // String angel_helmet
     243: invokedynamic #301,  0            // InvokeDynamic #5:get:()Ljava/util/function/Supplier;
     248: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     251: putstatic     #302                // Field ANGEL_HELMET:Lnet/neoforged/neoforge/registries/DeferredHolder;
     254: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     257: ldc_w         #305                // String angel_chestplate
     260: invokedynamic #307,  0            // InvokeDynamic #6:get:()Ljava/util/function/Supplier;
     265: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     268: putstatic     #308                // Field ANGEL_CHESTPLATE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     271: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     274: ldc_w         #311                // String angel_leggings
     277: invokedynamic #313,  0            // InvokeDynamic #7:get:()Ljava/util/function/Supplier;
     282: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     285: putstatic     #314                // Field ANGEL_LEGGINGS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     288: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     291: ldc_w         #317                // String angel_boots
     294: invokedynamic #319,  0            // InvokeDynamic #8:get:()Ljava/util/function/Supplier;
     299: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     302: putstatic     #320                // Field ANGEL_BOOTS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     305: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     308: ldc_w         #323                // String assassin_helmet
     311: invokedynamic #325,  0            // InvokeDynamic #9:get:()Ljava/util/function/Supplier;
     316: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     319: putstatic     #326                // Field ASSASSIN_HELMET:Lnet/neoforged/neoforge/registries/DeferredHolder;
     322: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     325: ldc_w         #329                // String assassin_chestplate
     328: invokedynamic #331,  0            // InvokeDynamic #10:get:()Ljava/util/function/Supplier;
     333: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     336: putstatic     #332                // Field ASSASSIN_CHESTPLATE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     339: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     342: ldc_w         #335                // String assassin_leggings
     345: invokedynamic #337,  0            // InvokeDynamic #11:get:()Ljava/util/function/Supplier;
     350: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     353: putstatic     #338                // Field ASSASSIN_LEGGINGS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     356: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     359: ldc_w         #341                // String assassin_boots
     362: invokedynamic #343,  0            // InvokeDynamic #12:get:()Ljava/util/function/Supplier;
     367: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     370: putstatic     #344                // Field ASSASSIN_BOOTS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     373: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     376: ldc_w         #347                // String bloodstone_helmet
     379: invokedynamic #349,  0            // InvokeDynamic #13:get:()Ljava/util/function/Supplier;
     384: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     387: putstatic     #350                // Field BLOODSTONE_HELMET:Lnet/neoforged/neoforge/registries/DeferredHolder;
     390: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     393: ldc_w         #353                // String bloodstone_chestplate
     396: invokedynamic #355,  0            // InvokeDynamic #14:get:()Ljava/util/function/Supplier;
     401: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     404: putstatic     #356                // Field BLOODSTONE_CHESTPLATE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     407: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     410: ldc_w         #359                // String bloodstone_leggings
     413: invokedynamic #361,  0            // InvokeDynamic #15:get:()Ljava/util/function/Supplier;
     418: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     421: putstatic     #362                // Field BLOODSTONE_LEGGINGS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     424: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     427: ldc_w         #365                // String bloodstone_boots
     430: invokedynamic #367,  0            // InvokeDynamic #16:get:()Ljava/util/function/Supplier;
     435: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     438: putstatic     #368                // Field BLOODSTONE_BOOTS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     441: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     444: ldc_w         #371                // String cryorium_helmet
     447: invokedynamic #373,  0            // InvokeDynamic #17:get:()Ljava/util/function/Supplier;
     452: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     455: putstatic     #374                // Field CRYORIUM_HELMET:Lnet/neoforged/neoforge/registries/DeferredHolder;
     458: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     461: ldc_w         #377                // String cryorium_chestplate
     464: invokedynamic #379,  0            // InvokeDynamic #18:get:()Ljava/util/function/Supplier;
     469: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     472: putstatic     #380                // Field CRYORIUM_CHESTPLATE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     475: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     478: ldc_w         #383                // String cryorium_leggings
     481: invokedynamic #385,  0            // InvokeDynamic #19:get:()Ljava/util/function/Supplier;
     486: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     489: putstatic     #386                // Field CRYORIUM_LEGGINGS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     492: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     495: ldc_w         #389                // String cryorium_boots
     498: invokedynamic #391,  0            // InvokeDynamic #20:get:()Ljava/util/function/Supplier;
     503: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     506: putstatic     #392                // Field CRYORIUM_BOOTS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     509: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     512: ldc_w         #395                // String jade_helmet
     515: invokedynamic #397,  0            // InvokeDynamic #21:get:()Ljava/util/function/Supplier;
     520: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     523: putstatic     #398                // Field JADE_HELMET:Lnet/neoforged/neoforge/registries/DeferredHolder;
     526: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     529: ldc_w         #401                // String jade_chestplate
     532: invokedynamic #403,  0            // InvokeDynamic #22:get:()Ljava/util/function/Supplier;
     537: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     540: putstatic     #404                // Field JADE_CHESTPLATE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     543: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     546: ldc_w         #407                // String jade_leggings
     549: invokedynamic #409,  0            // InvokeDynamic #23:get:()Ljava/util/function/Supplier;
     554: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     557: putstatic     #410                // Field JADE_LEGGINGS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     560: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     563: ldc_w         #413                // String jade_boots
     566: invokedynamic #415,  0            // InvokeDynamic #24:get:()Ljava/util/function/Supplier;
     571: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     574: putstatic     #416                // Field JADE_BOOTS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     577: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     580: ldc_w         #419                // String knight_helmet
     583: invokedynamic #421,  0            // InvokeDynamic #25:get:()Ljava/util/function/Supplier;
     588: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     591: putstatic     #422                // Field KNIGHT_HELMET:Lnet/neoforged/neoforge/registries/DeferredHolder;
     594: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     597: ldc_w         #425                // String knight_chestplate
     600: invokedynamic #427,  0            // InvokeDynamic #26:get:()Ljava/util/function/Supplier;
     605: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     608: putstatic     #428                // Field KNIGHT_CHESTPLATE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     611: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     614: ldc_w         #431                // String knight_leggings
     617: invokedynamic #433,  0            // InvokeDynamic #27:get:()Ljava/util/function/Supplier;
     622: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     625: putstatic     #434                // Field KNIGHT_LEGGINGS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     628: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     631: ldc_w         #437                // String knight_boots
     634: invokedynamic #439,  0            // InvokeDynamic #28:get:()Ljava/util/function/Supplier;
     639: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     642: putstatic     #440                // Field KNIGHT_BOOTS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     645: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     648: ldc_w         #443                // String moonlight_helmet
     651: invokedynamic #445,  0            // InvokeDynamic #29:get:()Ljava/util/function/Supplier;
     656: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     659: putstatic     #446                // Field MOONLIGHT_HELMET:Lnet/neoforged/neoforge/registries/DeferredHolder;
     662: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     665: ldc_w         #449                // String moonlight_chestplate
     668: invokedynamic #451,  0            // InvokeDynamic #30:get:()Ljava/util/function/Supplier;
     673: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     676: putstatic     #452                // Field MOONLIGHT_CHESTPLATE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     679: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     682: ldc_w         #455                // String moonlight_leggings
     685: invokedynamic #457,  0            // InvokeDynamic #31:get:()Ljava/util/function/Supplier;
     690: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     693: putstatic     #458                // Field MOONLIGHT_LEGGINGS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     696: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     699: ldc_w         #461                // String moonlight_boots
     702: invokedynamic #463,  0            // InvokeDynamic #32:get:()Ljava/util/function/Supplier;
     707: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     710: putstatic     #464                // Field MOONLIGHT_BOOTS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     713: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     716: ldc_w         #467                // String sculk_helmet
     719: invokedynamic #469,  0            // InvokeDynamic #33:get:()Ljava/util/function/Supplier;
     724: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     727: putstatic     #470                // Field SCULK_HELMET:Lnet/neoforged/neoforge/registries/DeferredHolder;
     730: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     733: ldc_w         #473                // String sculk_chestplate
     736: invokedynamic #475,  0            // InvokeDynamic #34:get:()Ljava/util/function/Supplier;
     741: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     744: putstatic     #476                // Field SCULK_CHESTPLATE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     747: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     750: ldc_w         #479                // String sculk_leggings
     753: invokedynamic #481,  0            // InvokeDynamic #35:get:()Ljava/util/function/Supplier;
     758: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     761: putstatic     #482                // Field SCULK_LEGGINGS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     764: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     767: ldc_w         #485                // String sculk_boots
     770: invokedynamic #487,  0            // InvokeDynamic #36:get:()Ljava/util/function/Supplier;
     775: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     778: putstatic     #488                // Field SCULK_BOOTS:Lnet/neoforged/neoforge/registries/DeferredHolder;
     781: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     784: ldc_w         #491                // String arclight_sword
     787: invokedynamic #493,  0            // InvokeDynamic #37:get:()Ljava/util/function/Supplier;
     792: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     795: putstatic     #494                // Field ARCLIGHT_SWORD:Lnet/neoforged/neoforge/registries/DeferredHolder;
     798: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     801: ldc_w         #497                // String arclight_pickaxe
     804: invokedynamic #499,  0            // InvokeDynamic #38:get:()Ljava/util/function/Supplier;
     809: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     812: putstatic     #500                // Field ARCLIGHT_PICKAXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     815: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     818: ldc_w         #503                // String arclight_axe
     821: invokedynamic #505,  0            // InvokeDynamic #39:get:()Ljava/util/function/Supplier;
     826: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     829: putstatic     #506                // Field ARCLIGHT_AXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     832: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     835: ldc_w         #509                // String arclight_shovel
     838: invokedynamic #511,  0            // InvokeDynamic #40:get:()Ljava/util/function/Supplier;
     843: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     846: putstatic     #512                // Field ARCLIGHT_SHOVEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
     849: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     852: ldc_w         #515                // String arclight_hoe
     855: invokedynamic #517,  0            // InvokeDynamic #41:get:()Ljava/util/function/Supplier;
     860: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     863: putstatic     #518                // Field ARCLIGHT_HOE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     866: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     869: ldc_w         #521                // String jade_sword
     872: invokedynamic #523,  0            // InvokeDynamic #42:get:()Ljava/util/function/Supplier;
     877: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     880: putstatic     #524                // Field JADE_SWORD:Lnet/neoforged/neoforge/registries/DeferredHolder;
     883: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     886: ldc_w         #527                // String jade_pickaxe
     889: invokedynamic #529,  0            // InvokeDynamic #43:get:()Ljava/util/function/Supplier;
     894: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     897: putstatic     #530                // Field JADE_PICKAXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     900: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     903: ldc_w         #533                // String jade_axe
     906: invokedynamic #535,  0            // InvokeDynamic #44:get:()Ljava/util/function/Supplier;
     911: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     914: putstatic     #536                // Field JADE_AXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     917: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     920: ldc_w         #539                // String jade_shovel
     923: invokedynamic #541,  0            // InvokeDynamic #45:get:()Ljava/util/function/Supplier;
     928: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     931: putstatic     #542                // Field JADE_SHOVEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
     934: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     937: ldc_w         #545                // String jade_hoe
     940: invokedynamic #547,  0            // InvokeDynamic #46:get:()Ljava/util/function/Supplier;
     945: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     948: putstatic     #548                // Field JADE_HOE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     951: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     954: ldc_w         #551                // String moonlight_sword
     957: invokedynamic #553,  0            // InvokeDynamic #47:get:()Ljava/util/function/Supplier;
     962: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     965: putstatic     #554                // Field MOONLIGHT_SWORD:Lnet/neoforged/neoforge/registries/DeferredHolder;
     968: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     971: ldc_w         #557                // String moonlight_pickaxe
     974: invokedynamic #559,  0            // InvokeDynamic #48:get:()Ljava/util/function/Supplier;
     979: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     982: putstatic     #560                // Field MOONLIGHT_PICKAXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
     985: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
     988: ldc_w         #563                // String moonlight_axe
     991: invokedynamic #565,  0            // InvokeDynamic #49:get:()Ljava/util/function/Supplier;
     996: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
     999: putstatic     #566                // Field MOONLIGHT_AXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1002: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1005: ldc_w         #569                // String moonlight_shovel
    1008: invokedynamic #571,  0            // InvokeDynamic #50:get:()Ljava/util/function/Supplier;
    1013: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1016: putstatic     #572                // Field MOONLIGHT_SHOVEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1019: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1022: ldc_w         #575                // String moonlight_hoe
    1025: invokedynamic #577,  0            // InvokeDynamic #51:get:()Ljava/util/function/Supplier;
    1030: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1033: putstatic     #578                // Field MOONLIGHT_HOE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1036: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1039: ldc_w         #581                // String bloodstone_sword
    1042: invokedynamic #583,  0            // InvokeDynamic #52:get:()Ljava/util/function/Supplier;
    1047: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1050: putstatic     #584                // Field BLOODSTONE_SWORD:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1053: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1056: ldc_w         #587                // String bloodstone_pickaxe
    1059: invokedynamic #589,  0            // InvokeDynamic #53:get:()Ljava/util/function/Supplier;
    1064: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1067: putstatic     #590                // Field BLOODSTONE_PICKAXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1070: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1073: ldc_w         #593                // String bloodstone_axe
    1076: invokedynamic #595,  0            // InvokeDynamic #54:get:()Ljava/util/function/Supplier;
    1081: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1084: putstatic     #596                // Field BLOODSTONE_AXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1087: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1090: ldc_w         #599                // String bloodstone_shovel
    1093: invokedynamic #601,  0            // InvokeDynamic #55:get:()Ljava/util/function/Supplier;
    1098: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1101: putstatic     #602                // Field BLOODSTONE_SHOVEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1104: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1107: ldc_w         #605                // String bloodstone_hoe
    1110: invokedynamic #607,  0            // InvokeDynamic #56:get:()Ljava/util/function/Supplier;
    1115: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1118: putstatic     #608                // Field BLOODSTONE_HOE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1121: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1124: ldc_w         #611                // String cryorium_sword
    1127: invokedynamic #613,  0            // InvokeDynamic #57:get:()Ljava/util/function/Supplier;
    1132: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1135: putstatic     #614                // Field CRYORIUM_SWORD:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1138: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1141: ldc_w         #617                // String cryorium_pickaxe
    1144: invokedynamic #619,  0            // InvokeDynamic #58:get:()Ljava/util/function/Supplier;
    1149: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1152: putstatic     #620                // Field CRYORIUM_PICKAXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1155: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1158: ldc_w         #623                // String cryorium_axe
    1161: invokedynamic #625,  0            // InvokeDynamic #59:get:()Ljava/util/function/Supplier;
    1166: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1169: putstatic     #626                // Field CRYORIUM_AXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1172: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1175: ldc_w         #629                // String cryorium_shovel
    1178: invokedynamic #631,  0            // InvokeDynamic #60:get:()Ljava/util/function/Supplier;
    1183: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1186: putstatic     #632                // Field CRYORIUM_SHOVEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1189: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1192: ldc_w         #635                // String cryorium_hoe
    1195: invokedynamic #637,  0            // InvokeDynamic #61:get:()Ljava/util/function/Supplier;
    1200: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1203: putstatic     #638                // Field CRYORIUM_HOE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1206: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1209: ldc_w         #641                // String sculk_sword
    1212: invokedynamic #643,  0            // InvokeDynamic #62:get:()Ljava/util/function/Supplier;
    1217: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1220: putstatic     #644                // Field SCULK_SWORD:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1223: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1226: ldc_w         #647                // String sculk_pickaxe
    1229: invokedynamic #649,  0            // InvokeDynamic #63:get:()Ljava/util/function/Supplier;
    1234: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1237: putstatic     #650                // Field SCULK_PICKAXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1240: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1243: ldc_w         #653                // String sculk_axe
    1246: invokedynamic #655,  0            // InvokeDynamic #64:get:()Ljava/util/function/Supplier;
    1251: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1254: putstatic     #656                // Field SCULK_AXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1257: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1260: ldc_w         #659                // String sculk_shovel
    1263: invokedynamic #661,  0            // InvokeDynamic #65:get:()Ljava/util/function/Supplier;
    1268: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1271: putstatic     #662                // Field SCULK_SHOVEL:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1274: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1277: ldc_w         #665                // String sculk_hoe
    1280: invokedynamic #667,  0            // InvokeDynamic #66:get:()Ljava/util/function/Supplier;
    1285: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1288: putstatic     #668                // Field SCULK_HOE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1291: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1294: ldc_w         #671                // String angel_sword
    1297: invokedynamic #673,  0            // InvokeDynamic #67:get:()Ljava/util/function/Supplier;
    1302: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1305: putstatic     #674                // Field ANGEL_SWORD:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1308: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1311: ldc_w         #677                // String moonlight_glaive
    1314: invokedynamic #679,  0            // InvokeDynamic #68:get:()Ljava/util/function/Supplier;
    1319: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1322: putstatic     #680                // Field MOONLIGHT_GLAIVE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1325: getstatic     #7                  // Field ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
    1328: ldc_w         #683                // String cryorium_battle_axe
    1331: invokedynamic #685,  0            // InvokeDynamic #69:get:()Ljava/util/function/Supplier;
    1336: invokevirtual #269                // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
    1339: putstatic     #686                // Field CRYORIUM_BATTLE_AXE:Lnet/neoforged/neoforge/registries/DeferredHolder;
    1342: return
}

```

### net.veroxuniverse.epicpaladins.common.registries.BlocksRegistry

```text
Compiled from "BlocksRegistry.java"
public class net.veroxuniverse.epicpaladins.common.registries.BlocksRegistry {
  public static final net.neoforged.neoforge.registries.DeferredRegister$Blocks BLOCKS;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> DEEPSLATE_ARCLIGHT_ORE;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> ARCLIGHT_ORE;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> ARCLIGHT_BLOCK;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> DEEPSLATE_CRYORIUM_ORE;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> CRYORIUM_ORE;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> CRYORIUM_BLOCK;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> DEEPSLATE_BLOODSTONE_ORE;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> BLOODSTONE_ORE;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> BLOODSTONE_BLOCK;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> JADE_ORE;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> JADE_BLOCK;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> MOONLIGHT_ORE;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> MOONLIGHT_BLOCK;

  public static final net.neoforged.neoforge.registries.DeferredBlock<net.minecraft.world.level.block.Block> STEEL_BLOCK;

  public net.veroxuniverse.epicpaladins.common.registries.BlocksRegistry();
    Code:
       0: aload_0
       1: invokespecial #1                  // Method java/lang/Object."<init>":()V
       4: return

  private static <T extends net.minecraft.world.level.block.Block> net.neoforged.neoforge.registries.DeferredBlock<T> registerBlock(java.lang.String, java.util.function.Supplier<T>);
    Code:
       0: getstatic     #7                  // Field BLOCKS:Lnet/neoforged/neoforge/registries/DeferredRegister$Blocks;
       3: aload_0
       4: aload_1
       5: invokevirtual #13                 // Method net/neoforged/neoforge/registries/DeferredRegister$Blocks.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
       8: astore_2
       9: aload_0
      10: aload_2
      11: invokestatic  #19                 // Method registerBlockItem:(Ljava/lang/String;Lnet/neoforged/neoforge/registries/DeferredBlock;)V
      14: aload_2
      15: areturn

  private static <T extends net.minecraft.world.level.block.Block> net.neoforged.neoforge.registries.DeferredBlock<T> registerBlockWithoutItem(java.lang.String, java.util.function.Supplier<T>);
    Code:
       0: getstatic     #7                  // Field BLOCKS:Lnet/neoforged/neoforge/registries/DeferredRegister$Blocks;
       3: aload_0
       4: aload_1
       5: invokevirtual #13                 // Method net/neoforged/neoforge/registries/DeferredRegister$Blocks.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
       8: areturn

  private static java.util.function.ToIntFunction<net.minecraft.world.level.block.state.BlockState> litBlockEmission(int);
    Code:
       0: iload_0
       1: invokedynamic #23,  0             // InvokeDynamic #0:applyAsInt:(I)Ljava/util/function/ToIntFunction;
       6: areturn

  private static <T extends net.minecraft.world.level.block.Block> void registerBlockItem(java.lang.String, net.neoforged.neoforge.registries.DeferredBlock<T>);
    Code:
       0: getstatic     #27                 // Field net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.ITEMS:Lnet/neoforged/neoforge/registries/DeferredRegister$Items;
       3: aload_0
       4: aload_1
       5: invokedynamic #33,  0             // InvokeDynamic #1:get:(Lnet/neoforged/neoforge/registries/DeferredBlock;)Ljava/util/function/Supplier;
      10: invokevirtual #37                 // Method net/neoforged/neoforge/registries/DeferredRegister$Items.register:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredItem;
      13: pop
      14: return

  public static void register(net.neoforged.bus.api.IEventBus);
    Code:
       0: getstatic     #7                  // Field BLOCKS:Lnet/neoforged/neoforge/registries/DeferredRegister$Blocks;
       3: aload_0
       4: invokevirtual #42                 // Method net/neoforged/neoforge/registries/DeferredRegister$Blocks.register:(Lnet/neoforged/bus/api/IEventBus;)V
       7: return

  private static net.minecraft.world.item.BlockItem lambda$registerBlockItem$15(net.neoforged.neoforge.registries.DeferredBlock);
    Code:
       0: new           #45                 // class net/minecraft/world/item/BlockItem
       3: dup
       4: aload_0
       5: invokevirtual #47                 // Method net/neoforged/neoforge/registries/DeferredBlock.get:()Ljava/lang/Object;
       8: checkcast     #52                 // class net/minecraft/world/level/block/Block
      11: new           #54                 // class net/minecraft/world/item/Item$Properties
      14: dup
      15: invokespecial #56                 // Method net/minecraft/world/item/Item$Properties."<init>":()V
      18: invokespecial #57                 // Method net/minecraft/world/item/BlockItem."<init>":(Lnet/minecraft/world/level/block/Block;Lnet/minecraft/world/item/Item$Properties;)V
      21: areturn

  private static int lambda$litBlockEmission$14(int, net.minecraft.world.level.block.state.BlockState);
    Code:
       0: aload_1
       1: getstatic     #60                 // Field net/minecraft/world/level/block/state/properties/BlockStateProperties.LIT:Lnet/minecraft/world/level/block/state/properties/BooleanProperty;
       4: invokevirtual #66                 // Method net/minecraft/world/level/block/state/BlockState.getValue:(Lnet/minecraft/world/level/block/state/properties/Property;)Ljava/lang/Comparable;
       7: checkcast     #72                 // class java/lang/Boolean
      10: invokevirtual #74                 // Method java/lang/Boolean.booleanValue:()Z
      13: ifeq          20
      16: iload_0
      17: goto          21
      20: iconst_0
      21: ireturn

  private static net.minecraft.world.level.block.Block lambda$static$13();
    Code:
       0: new           #52                 // class net/minecraft/world/level/block/Block
       3: dup
       4: getstatic     #78                 // Field net/minecraft/world/level/block/Blocks.DIAMOND_BLOCK:Lnet/minecraft/world/level/block/Block;
       7: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      10: ldc           #90                 // float 4.0f
      12: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      15: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      18: invokespecial #99                 // Method net/minecraft/world/level/block/Block."<init>":(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      21: areturn

  private static net.minecraft.world.level.block.Block lambda$static$12();
    Code:
       0: new           #52                 // class net/minecraft/world/level/block/Block
       3: dup
       4: getstatic     #78                 // Field net/minecraft/world/level/block/Blocks.DIAMOND_BLOCK:Lnet/minecraft/world/level/block/Block;
       7: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      10: ldc           #90                 // float 4.0f
      12: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      15: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      18: invokespecial #99                 // Method net/minecraft/world/level/block/Block."<init>":(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      21: areturn

  private static net.minecraft.world.level.block.Block lambda$static$11();
    Code:
       0: new           #102                // class net/minecraft/world/level/block/DropExperienceBlock
       3: dup
       4: iconst_3
       5: bipush        7
       7: invokestatic  #104                // Method net/minecraft/util/valueproviders/UniformInt.of:(II)Lnet/minecraft/util/valueproviders/UniformInt;
      10: getstatic     #110                // Field net/minecraft/world/level/block/Blocks.DIAMOND_ORE:Lnet/minecraft/world/level/block/Block;
      13: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      16: ldc           #90                 // float 4.0f
      18: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      21: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      24: invokespecial #113                // Method net/minecraft/world/level/block/DropExperienceBlock."<init>":(Lnet/minecraft/util/valueproviders/IntProvider;Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      27: areturn

  private static net.minecraft.world.level.block.Block lambda$static$10();
    Code:
       0: new           #52                 // class net/minecraft/world/level/block/Block
       3: dup
       4: getstatic     #78                 // Field net/minecraft/world/level/block/Blocks.DIAMOND_BLOCK:Lnet/minecraft/world/level/block/Block;
       7: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      10: ldc           #90                 // float 4.0f
      12: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      15: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      18: invokespecial #99                 // Method net/minecraft/world/level/block/Block."<init>":(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      21: areturn

  private static net.minecraft.world.level.block.Block lambda$static$9();
    Code:
       0: new           #102                // class net/minecraft/world/level/block/DropExperienceBlock
       3: dup
       4: iconst_3
       5: bipush        7
       7: invokestatic  #104                // Method net/minecraft/util/valueproviders/UniformInt.of:(II)Lnet/minecraft/util/valueproviders/UniformInt;
      10: getstatic     #110                // Field net/minecraft/world/level/block/Blocks.DIAMOND_ORE:Lnet/minecraft/world/level/block/Block;
      13: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      16: ldc           #90                 // float 4.0f
      18: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      21: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      24: invokespecial #113                // Method net/minecraft/world/level/block/DropExperienceBlock."<init>":(Lnet/minecraft/util/valueproviders/IntProvider;Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      27: areturn

  private static net.minecraft.world.level.block.Block lambda$static$8();
    Code:
       0: new           #52                 // class net/minecraft/world/level/block/Block
       3: dup
       4: getstatic     #78                 // Field net/minecraft/world/level/block/Blocks.DIAMOND_BLOCK:Lnet/minecraft/world/level/block/Block;
       7: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      10: ldc           #90                 // float 4.0f
      12: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      15: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      18: invokespecial #99                 // Method net/minecraft/world/level/block/Block."<init>":(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      21: areturn

  private static net.minecraft.world.level.block.Block lambda$static$7();
    Code:
       0: new           #102                // class net/minecraft/world/level/block/DropExperienceBlock
       3: dup
       4: iconst_3
       5: bipush        7
       7: invokestatic  #104                // Method net/minecraft/util/valueproviders/UniformInt.of:(II)Lnet/minecraft/util/valueproviders/UniformInt;
      10: getstatic     #110                // Field net/minecraft/world/level/block/Blocks.DIAMOND_ORE:Lnet/minecraft/world/level/block/Block;
      13: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      16: ldc           #90                 // float 4.0f
      18: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      21: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      24: invokespecial #113                // Method net/minecraft/world/level/block/DropExperienceBlock."<init>":(Lnet/minecraft/util/valueproviders/IntProvider;Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      27: areturn

  private static net.minecraft.world.level.block.Block lambda$static$6();
    Code:
       0: new           #102                // class net/minecraft/world/level/block/DropExperienceBlock
       3: dup
       4: iconst_3
       5: bipush        7
       7: invokestatic  #104                // Method net/minecraft/util/valueproviders/UniformInt.of:(II)Lnet/minecraft/util/valueproviders/UniformInt;
      10: getstatic     #110                // Field net/minecraft/world/level/block/Blocks.DIAMOND_ORE:Lnet/minecraft/world/level/block/Block;
      13: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      16: ldc           #90                 // float 4.0f
      18: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      21: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      24: invokespecial #113                // Method net/minecraft/world/level/block/DropExperienceBlock."<init>":(Lnet/minecraft/util/valueproviders/IntProvider;Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      27: areturn

  private static net.minecraft.world.level.block.Block lambda$static$5();
    Code:
       0: new           #52                 // class net/minecraft/world/level/block/Block
       3: dup
       4: getstatic     #78                 // Field net/minecraft/world/level/block/Blocks.DIAMOND_BLOCK:Lnet/minecraft/world/level/block/Block;
       7: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      10: ldc           #90                 // float 4.0f
      12: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      15: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      18: invokespecial #99                 // Method net/minecraft/world/level/block/Block."<init>":(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      21: areturn

  private static net.minecraft.world.level.block.Block lambda$static$4();
    Code:
       0: new           #102                // class net/minecraft/world/level/block/DropExperienceBlock
       3: dup
       4: iconst_3
       5: bipush        7
       7: invokestatic  #104                // Method net/minecraft/util/valueproviders/UniformInt.of:(II)Lnet/minecraft/util/valueproviders/UniformInt;
      10: getstatic     #110                // Field net/minecraft/world/level/block/Blocks.DIAMOND_ORE:Lnet/minecraft/world/level/block/Block;
      13: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      16: ldc           #90                 // float 4.0f
      18: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      21: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      24: invokespecial #113                // Method net/minecraft/world/level/block/DropExperienceBlock."<init>":(Lnet/minecraft/util/valueproviders/IntProvider;Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      27: areturn

  private static net.minecraft.world.level.block.Block lambda$static$3();
    Code:
       0: new           #102                // class net/minecraft/world/level/block/DropExperienceBlock
       3: dup
       4: iconst_3
       5: bipush        7
       7: invokestatic  #104                // Method net/minecraft/util/valueproviders/UniformInt.of:(II)Lnet/minecraft/util/valueproviders/UniformInt;
      10: getstatic     #110                // Field net/minecraft/world/level/block/Blocks.DIAMOND_ORE:Lnet/minecraft/world/level/block/Block;
      13: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      16: ldc           #90                 // float 4.0f
      18: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      21: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      24: invokespecial #113                // Method net/minecraft/world/level/block/DropExperienceBlock."<init>":(Lnet/minecraft/util/valueproviders/IntProvider;Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      27: areturn

  private static net.minecraft.world.level.block.Block lambda$static$2();
    Code:
       0: new           #52                 // class net/minecraft/world/level/block/Block
       3: dup
       4: getstatic     #78                 // Field net/minecraft/world/level/block/Blocks.DIAMOND_BLOCK:Lnet/minecraft/world/level/block/Block;
       7: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      10: ldc           #90                 // float 4.0f
      12: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      15: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      18: invokespecial #99                 // Method net/minecraft/world/level/block/Block."<init>":(Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      21: areturn

  private static net.minecraft.world.level.block.Block lambda$static$1();
    Code:
       0: new           #102                // class net/minecraft/world/level/block/DropExperienceBlock
       3: dup
       4: iconst_3
       5: bipush        7
       7: invokestatic  #104                // Method net/minecraft/util/valueproviders/UniformInt.of:(II)Lnet/minecraft/util/valueproviders/UniformInt;
      10: getstatic     #110                // Field net/minecraft/world/level/block/Blocks.DIAMOND_ORE:Lnet/minecraft/world/level/block/Block;
      13: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      16: ldc           #90                 // float 4.0f
      18: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      21: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      24: invokespecial #113                // Method net/minecraft/world/level/block/DropExperienceBlock."<init>":(Lnet/minecraft/util/valueproviders/IntProvider;Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      27: areturn

  private static net.minecraft.world.level.block.Block lambda$static$0();
    Code:
       0: new           #102                // class net/minecraft/world/level/block/DropExperienceBlock
       3: dup
       4: iconst_3
       5: bipush        7
       7: invokestatic  #104                // Method net/minecraft/util/valueproviders/UniformInt.of:(II)Lnet/minecraft/util/valueproviders/UniformInt;
      10: getstatic     #110                // Field net/minecraft/world/level/block/Blocks.DIAMOND_ORE:Lnet/minecraft/world/level/block/Block;
      13: invokestatic  #84                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.ofFullCopy:(Lnet/minecraft/world/level/block/state/BlockBehaviour;)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      16: ldc           #90                 // float 4.0f
      18: invokevirtual #91                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.strength:(F)Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      21: invokevirtual #95                 // Method net/minecraft/world/level/block/state/BlockBehaviour$Properties.requiresCorrectToolForDrops:()Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;
      24: invokespecial #113                // Method net/minecraft/world/level/block/DropExperienceBlock."<init>":(Lnet/minecraft/util/valueproviders/IntProvider;Lnet/minecraft/world/level/block/state/BlockBehaviour$Properties;)V
      27: areturn

  static {};
    Code:
       0: ldc           #118                // String epicpaladins
       2: invokestatic  #120                // Method net/neoforged/neoforge/registries/DeferredRegister.createBlocks:(Ljava/lang/String;)Lnet/neoforged/neoforge/registries/DeferredRegister$Blocks;
       5: putstatic     #7                  // Field BLOCKS:Lnet/neoforged/neoforge/registries/DeferredRegister$Blocks;
       8: ldc           #126                // String deepslate_arclight_ore
      10: invokedynamic #128,  0            // InvokeDynamic #2:get:()Ljava/util/function/Supplier;
      15: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
      18: putstatic     #134                // Field DEEPSLATE_ARCLIGHT_ORE:Lnet/neoforged/neoforge/registries/DeferredBlock;
      21: ldc           #138                // String arclight_ore
      23: invokedynamic #140,  0            // InvokeDynamic #3:get:()Ljava/util/function/Supplier;
      28: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
      31: putstatic     #141                // Field ARCLIGHT_ORE:Lnet/neoforged/neoforge/registries/DeferredBlock;
      34: ldc           #144                // String arclight_block
      36: invokedynamic #146,  0            // InvokeDynamic #4:get:()Ljava/util/function/Supplier;
      41: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
      44: putstatic     #147                // Field ARCLIGHT_BLOCK:Lnet/neoforged/neoforge/registries/DeferredBlock;
      47: ldc           #150                // String deepslate_cryorium_ore
      49: invokedynamic #152,  0            // InvokeDynamic #5:get:()Ljava/util/function/Supplier;
      54: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
      57: putstatic     #153                // Field DEEPSLATE_CRYORIUM_ORE:Lnet/neoforged/neoforge/registries/DeferredBlock;
      60: ldc           #156                // String cryorium_ore
      62: invokedynamic #158,  0            // InvokeDynamic #6:get:()Ljava/util/function/Supplier;
      67: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
      70: putstatic     #159                // Field CRYORIUM_ORE:Lnet/neoforged/neoforge/registries/DeferredBlock;
      73: ldc           #162                // String cryorium_block
      75: invokedynamic #164,  0            // InvokeDynamic #7:get:()Ljava/util/function/Supplier;
      80: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
      83: putstatic     #165                // Field CRYORIUM_BLOCK:Lnet/neoforged/neoforge/registries/DeferredBlock;
      86: ldc           #168                // String deepslate_bloodstone_ore
      88: invokedynamic #170,  0            // InvokeDynamic #8:get:()Ljava/util/function/Supplier;
      93: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
      96: putstatic     #171                // Field DEEPSLATE_BLOODSTONE_ORE:Lnet/neoforged/neoforge/registries/DeferredBlock;
      99: ldc           #174                // String bloodstone_ore
     101: invokedynamic #176,  0            // InvokeDynamic #9:get:()Ljava/util/function/Supplier;
     106: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
     109: putstatic     #177                // Field BLOODSTONE_ORE:Lnet/neoforged/neoforge/registries/DeferredBlock;
     112: ldc           #180                // String bloodstone_block
     114: invokedynamic #182,  0            // InvokeDynamic #10:get:()Ljava/util/function/Supplier;
     119: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
     122: putstatic     #183                // Field BLOODSTONE_BLOCK:Lnet/neoforged/neoforge/registries/DeferredBlock;
     125: ldc           #186                // String jade_ore
     127: invokedynamic #188,  0            // InvokeDynamic #11:get:()Ljava/util/function/Supplier;
     132: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
     135: putstatic     #189                // Field JADE_ORE:Lnet/neoforged/neoforge/registries/DeferredBlock;
     138: ldc           #192                // String jade_block
     140: invokedynamic #194,  0            // InvokeDynamic #12:get:()Ljava/util/function/Supplier;
     145: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
     148: putstatic     #195                // Field JADE_BLOCK:Lnet/neoforged/neoforge/registries/DeferredBlock;
     151: ldc           #198                // String moonlight_ore
     153: invokedynamic #200,  0            // InvokeDynamic #13:get:()Ljava/util/function/Supplier;
     158: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
     161: putstatic     #201                // Field MOONLIGHT_ORE:Lnet/neoforged/neoforge/registries/DeferredBlock;
     164: ldc           #204                // String moonlight_block
     166: invokedynamic #206,  0            // InvokeDynamic #14:get:()Ljava/util/function/Supplier;
     171: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
     174: putstatic     #207                // Field MOONLIGHT_BLOCK:Lnet/neoforged/neoforge/registries/DeferredBlock;
     177: ldc           #210                // String steel_block
     179: invokedynamic #212,  0            // InvokeDynamic #15:get:()Ljava/util/function/Supplier;
     184: invokestatic  #131                // Method registerBlock:(Ljava/lang/String;Ljava/util/function/Supplier;)Lnet/neoforged/neoforge/registries/DeferredBlock;
     187: putstatic     #213                // Field STEEL_BLOCK:Lnet/neoforged/neoforge/registries/DeferredBlock;
     190: return
}

```
