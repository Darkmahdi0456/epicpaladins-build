package net.veroxuniverse.epicpaladins.fabric.item;

import net.minecraft.item.Item;

/** Dedicated item type for Epic Paladins' three GeckoLib weapon assets.
 * Rendering and special combat behavior are intentionally registered separately.
 */
public final class EpicWeaponItem extends Item {
    private final String weaponId;

    public EpicWeaponItem(String weaponId, Settings settings) {
        super(settings);
        this.weaponId = weaponId;
    }

    public String getWeaponId() {
        return weaponId;
    }
}
