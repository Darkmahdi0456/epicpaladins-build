package net.veroxuniverse.epicpaladins.fabric;

import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;

/** Adds the port's currently registered placeholder content to its own creative tab. */
public final class CreativeTabRegistry {
    private CreativeTabRegistry() {}
    public static void register() {
        ItemGroup group = FabricItemGroup.builder()
            .icon(() -> new ItemStack(ContentRegistry.ITEMS.get("bloodstone_gem")))
            .displayName(Text.translatable("itemGroup.epicpaladins.main"))
            .entries((context, entries) -> {
                ContentRegistry.ITEMS.values().forEach(entries::add);
                ContentRegistry.BLOCKS.values().forEach(block -> entries.add(block));
            })
            .build();
        Registry.register(Registries.ITEM_GROUP, Identifier.of(EpicPaladinsFabric.MOD_ID, "main"), group);
    }
}
