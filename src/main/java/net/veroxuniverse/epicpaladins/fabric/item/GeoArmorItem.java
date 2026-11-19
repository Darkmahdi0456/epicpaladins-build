package net.veroxuniverse.epicpaladins.fabric.item;

import net.minecraft.item.ArmorItem;
import net.fabricmc.api.EnvType;
import net.fabricmc.api.Environment;
import net.minecraft.client.render.entity.model.BipedEntityModel;
import net.minecraft.entity.EquipmentSlot;
import net.minecraft.entity.LivingEntity;
import net.minecraft.item.ItemStack;
import org.jetbrains.annotations.Nullable;
import software.bernie.geckolib.renderer.GeoArmorRenderer;
import software.bernie.geckolib.renderer.GeoRenderProvider;
import net.veroxuniverse.epicpaladins.fabric.client.armor.ArmorGeoRenderer;

import java.util.function.Consumer;
import net.minecraft.item.equipment.ArmorMaterial;
import net.minecraft.item.equipment.EquipmentType;
import software.bernie.geckolib.animatable.GeoItem;
import software.bernie.geckolib.animatable.instance.AnimatableInstanceCache;
import software.bernie.geckolib.animation.AnimatableManager;
import software.bernie.geckolib.util.GeckoLibUtil;

/**
 * Armor item that participates in GeckoLib's animatable-item lifecycle.
 * The per-set renderer provider is intentionally attached in the client-only
 * client renderer is created lazily through GeckoLib's dynamic render provider.
 */
public final class GeoArmorItem extends ArmorItem implements GeoItem {
    private final String armorSetId;
    private final AnimatableInstanceCache cache = GeckoLibUtil.createInstanceCache(this);

    public GeoArmorItem(ArmorMaterial material, EquipmentType type, Settings settings, String armorSetId) {
        super(material, type, settings);
        this.armorSetId = armorSetId;
    }

    public String getArmorSetId() {
        return this.armorSetId;
    }

    /** Supplies the set-specific GeckoLib armor renderer lazily on the client. */
    @Override
    @Environment(EnvType.CLIENT)
    public void createGeoRenderer(Consumer<GeoRenderProvider> consumer) {
        consumer.accept(new GeoRenderProvider() {
            private GeoArmorRenderer<?> renderer;

            @Override
            public <T extends LivingEntity> BipedEntityModel<?> getGeoArmorRenderer(
                    @Nullable T livingEntity,
                    ItemStack itemStack,
                    @Nullable EquipmentSlot equipmentSlot,
                    @Nullable BipedEntityModel<T> original) {
                if (this.renderer == null) {
                    this.renderer = new ArmorGeoRenderer<>(GeoArmorItem.this.armorSetId);
                }
                // Sync the renderer with the entity, stack, slot, and vanilla model
                // for this render pass. GeckoLib requires this before returning it.
                this.renderer.prepForRender(livingEntity, itemStack, equipmentSlot, original);
                return this.renderer;
            }
        });
    }

    @Override
    public void registerControllers(AnimatableManager.ControllerRegistrar controllers) {
        // The original armor models have no active animation controllers.
    }

    @Override
    public AnimatableInstanceCache getAnimatableInstanceCache() {
        return this.cache;
    }
}
