package net.veroxuniverse.epicpaladins.fabric.client.armor;

import net.fabricmc.api.EnvType;
import net.fabricmc.api.Environment;

import net.minecraft.item.Item;
import software.bernie.geckolib.animatable.GeoItem;
import software.bernie.geckolib.renderer.GeoArmorRenderer;

@Environment(EnvType.CLIENT)
/** Shared GeckoLib 4 armor renderer; the set-specific model supplies its own geometry and texture. */
public final class ArmorGeoRenderer<T extends Item & GeoItem> extends GeoArmorRenderer<T> {
    public ArmorGeoRenderer(String armorSetId) {
        super(new ArmorGeoModel<>(armorSetId));
    }
}
