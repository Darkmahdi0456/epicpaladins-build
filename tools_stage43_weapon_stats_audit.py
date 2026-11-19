#!/usr/bin/env python3
"""Verify the original jar has the audited weapon registry classes and report."""
from pathlib import Path
import zipfile
root = Path(__file__).resolve().parent
jar = Path('/mnt/data/epicpaladins-1.4.3-1.21.1.jar')
assert jar.is_file(), f'Original jar missing: {jar}'
classes = [
 'net/veroxuniverse/epicpaladins/common/registries/ItemsRegistry.class',
 'net/veroxuniverse/epicpaladins/common/registries/items/ItemMaterialsRegistry.class',
]
with zipfile.ZipFile(jar) as z:
    for name in classes:
        data = z.read(name)
        assert data[:4] == b'\xca\xfe\xba\xbe', f'Invalid class: {name}'
report = (root / 'STAGE43-WEAPON-STATS-AUDIT.md').read_text()
for token in ('10, -2.1F', '10, -2.5F', '12.0F, -3.0F', 'EPIC', 'Tiers.NETHERITE'):
    assert token in report, f'Missing audited value: {token}'
print('Stage 43 checks passed: original registry bytecode files valid; all audited weapon values present.')
