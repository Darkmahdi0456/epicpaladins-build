# Stage 36 — Bytecode behavior inspection

Inspected the original `epicpaladins-1.4.3-1.21.1.jar` with `javap -p -c`.

## Confirmed findings

- `ArclightCrown` is currently an empty class: its only constructor calls `Object.<init>` and returns. There is no summon/ability behavior in this class to port.
- `AngelSwordItem`, `CryoriumAxeItem`, and `MoonlightGlaiveItem` all extend `SwordItem` and implement GeckoLib `GeoItem`.
- Each weapon constructor creates a `SingletonAnimatableInstanceCache`.
- Each `registerControllers(...)` method is empty (`return` immediately). Therefore no GeckoLib animation controller/attack animation is defined in these three item classes.
- Each `initializeClient(...)` creates a NeoForge client extension (inner class `$1`). This is the NeoForge-specific renderer hookup and cannot be copied directly into Fabric.

## Corrections to earlier assumptions

The earlier wording “Arclight Crown summon behavior” was speculative. The inspected class has no behavior. Also, while the weapons use GeckoLib and have client renderer extensions, their own controller-registration methods are empty; do not claim custom weapon animations exist based on these classes alone.

## Porting work still required

1. Inspect each inner `$1` class to identify the renderer/model resource paths and translate the renderer hookup to Fabric GeckoLib.
2. Implement Fabric-side `GeoItem` classes and client renderer registration.
3. Verify the weapon model JSON/animation files are compatible with the GeckoLib version chosen for Minecraft 1.21.4.
4. Compile and test in Minecraft before claiming the feature works.

This stage is a bytecode inspection/report only. No runtime behavior was implemented or tested.
