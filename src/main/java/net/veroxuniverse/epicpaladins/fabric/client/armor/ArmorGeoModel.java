package net.veroxuniverse.epicpaladins.fabric.client.armor;

import net.fabricmc.api.EnvType;
import net.fabricmc.api.Environment;

import net.minecraft.item.Item;
import net.minecraft.util.Identifier;
import org.jetbrains.annotations.Nullable;
import software.bernie.geckolib.animatable.GeoItem;
import software.bernie.geckolib.model.GeoModel;
import software.bernie.geckolib.renderer.GeoRenderer;
import net.veroxuniverse.epicpaladins.fabric.port.ArmorGeoResources;

@Environment(EnvType.CLIENT)
/** GeckoLib 4 model adapter for one of the original Epic Paladins armor sets. */
public final class ArmorGeoModel<T extends Item & GeoItem> extends GeoModel<T> {
    private static final Identifier EMPTY_ANIMATION = Identifier.of(
            "epicpaladins", "animations/armor/empty.animation.json");

    private final Identifier geometry;
    private final Identifier texture;

    public ArmorGeoModel(String armorSetId) {
        ArmorGeoResources.Entry entry = ArmorGeoResources.get(armorSetId);
        this.geometry = Identifier.of(entry.model());
        this.texture = Identifier.of(entry.texture());
    }

    @Override
    public Identifier getModelResource(T animatable, @Nullable GeoRenderer<T> renderer) {
        return this.geometry;
    }

    @Override
    public Identifier getTextureResource(T animatable, @Nullable GeoRenderer<T> renderer) {
        return this.texture;
    }

    @Override
    public Identifier getAnimationResource(T animatable) {
        return EMPTY_ANIMATION;
    }
}
