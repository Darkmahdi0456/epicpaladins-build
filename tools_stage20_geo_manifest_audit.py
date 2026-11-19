import json
from pathlib import Path
root = Path(__file__).parent / 'src/main/resources/assets'
manifest = json.loads((root/'epicpaladins/geo/armor_render_manifest.json').read_text())
missing=[]
for name, entry in manifest['sets'].items():
    for key in ('geometry','texture'):
        rel=entry[key].split(':',1)[1]
        p=root/'epicpaladins'/rel
        if not p.is_file(): missing.append(f'{name}: missing {key} {p}')
        elif key == 'geometry':
            try: json.loads(p.read_text())
            except Exception as e: missing.append(f'{name}: invalid geo JSON: {e}')
print(f"Armor sets in manifest: {len(manifest['sets'])}")
print(f"Missing/invalid references: {len(missing)}")
for item in missing: print(item)
raise SystemExit(1 if missing else 0)
