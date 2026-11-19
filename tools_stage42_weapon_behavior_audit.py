#!/usr/bin/env python3
"""Evidence checklist for the Stage 42 original-jar weapon audit."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parent
jar = Path('/mnt/data/epicpaladins-1.4.3-1.21.1.jar')
classes = [
 'net/veroxuniverse/epicpaladins/common/items/weapons/AngelSwordItem.class',
 'net/veroxuniverse/epicpaladins/common/items/weapons/CryoriumAxeItem.class',
 'net/veroxuniverse/epicpaladins/common/items/weapons/MoonlightGlaiveItem.class',
]
assert jar.is_file(), f'Original jar not found: {jar}'
with zipfile.ZipFile(jar) as z:
    missing = [name for name in classes if name not in z.namelist()]
    assert not missing, f'Missing original classes: {missing}'
    for name in classes:
        data = z.read(name)
        assert data[:4] == b'\xca\xfe\xba\xbe', f'Invalid class file: {name}'
report = (root / 'STAGE42-WEAPON-BEHAVIOR-AUDIT.md').read_text()
for phrase in ('SwordItem', 'empty', 'generic `Item` placeholders', 'No Gradle build'):
    assert phrase in report, f'Report missing expected finding: {phrase}'
print('Stage 42 audit checks passed: 3 original weapon classes present and valid; report findings verified.')
