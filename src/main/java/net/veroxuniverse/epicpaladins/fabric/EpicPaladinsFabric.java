package net.veroxuniverse.epicpaladins.fabric;
import net.fabricmc.api.ModInitializer;
import net.veroxuniverse.epicpaladins.fabric.worldgen.OreWorldgenRegistry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
public final class EpicPaladinsFabric implements ModInitializer {
 public static final String MOD_ID = "epicpaladins";
 public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);
 @Override public void onInitialize() { ContentRegistry.register();
  CreativeTabRegistry.register();
  OreWorldgenRegistry.register();
  LOGGER.info("Epic Paladins Fabric port: registered {} placeholder items and {} blocks.", ContentRegistry.ITEMS.size(), ContentRegistry.BLOCKS.size()); }
}
