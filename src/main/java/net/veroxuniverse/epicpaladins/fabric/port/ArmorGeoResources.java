package net.veroxuniverse.epicpaladins.fabric.port;

import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Canonical resource mapping for the original Epic Paladins Geo armor assets.
 *
 * This class deliberately contains resource identifiers only. Client-side
 * GeckoLib renderer registration is kept separate so common item registration
 * does not eagerly load client rendering classes on a dedicated server.
 */
public final class ArmorGeoResources {
    public record Entry(String model, String texture) {}

    private static final Map<String, Entry> SETS;

    static {
        Map<String, Entry> sets = new LinkedHashMap<>();
        add(sets, "arclight", "arclight_armor_textures");
        add(sets, "angel", "angel_armor_textures");
        add(sets, "assassin", "assassin_armor_textures");
        add(sets, "bloodstone", "bloodstone_armor_textures");
        add(sets, "cryorium", "cryorium_armor_textures");
        add(sets, "jade", "jade_armor_textures");
        add(sets, "knight", "knight_armor_textures");
        add(sets, "moonlight", "moonlight_armor_textures");
        add(sets, "sculk", "sculk_armor_textures");
        SETS = Collections.unmodifiableMap(sets);
    }

    private ArmorGeoResources() {}

    private static void add(Map<String, Entry> sets, String id, String textureName) {
        sets.put(id, new Entry(
                "epicpaladins:geo/" + id + "_armor.geo.json",
                "epicpaladins:textures/armor/" + textureName + ".png"));
    }

    public static Entry get(String armorSetId) {
        Entry entry = SETS.get(armorSetId);
        if (entry == null)
            throw new IllegalArgumentException("Unknown Epic Paladins armor set: " + armorSetId);
        return entry;
    }

    public static Map<String, Entry> all() {
        return SETS;
    }
}
