# Stage 56 — Original armor registry correction

- Inspected the original uploaded 1.21.1 JAR, not just the port's asset folders.
- The original contains exactly nine armor item implementation classes: Angel, Arclight, Assassin, Bloodstone, Cryorium, Jade, Knight, Moonlight, and Sculk.
- Corrected the Fabric armor registry to register those nine sets only. Removed the invented Steel armor set and its unused equipment asset. Steel ingot, nugget, template, and block content remain unchanged.
- Corrected the wearable-item exclusion list so it matches the nine registered armor sets.
- Added `tools_stage56_original_armor_registry_check.py`; it compares the original JAR classes, Fabric registrations, and Geo manifest. Result: PASS for all nine sets.
- This is a source/asset consistency correction. It does not implement GeckoLib rendering, and does not establish a successful Gradle build or in-game test.
