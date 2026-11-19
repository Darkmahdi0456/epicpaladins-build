#!/usr/bin/env bash
set -euo pipefail
JAR="${1:?Usage: tools_stage35_special_feature_audit.sh /path/to/original.jar}"
for CLASS in \
  net.veroxuniverse.epicpaladins.common.items.weapons.AngelSwordItem \
  net.veroxuniverse.epicpaladins.common.items.weapons.CryoriumAxeItem \
  net.veroxuniverse.epicpaladins.common.items.weapons.MoonlightGlaiveItem \
  net.veroxuniverse.epicpaladins.common.items.summonItems.ArclightCrown; do
  echo "===== $CLASS ====="
  javap -classpath "$JAR" -p "$CLASS"
done
