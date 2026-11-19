"""Audit Geo armor model JSON and source texture dimensions for Stage 17."""
import json
from pathlib import Path
from PIL import Image
root = Path(__file__).parent / 'src/main/resources/assets/epicpaladins'
for model in sorted((root / 'geo').glob('*.json')):
    data = json.loads(model.read_text(encoding='utf-8'))
    geos = data.get('minecraft:geometry', [])
    print(f'{model.name}: valid JSON; geometries={len(geos)}')
for texture in sorted((root / 'textures/armor').glob('*.png')):
    with Image.open(texture) as image:
        print(f'{texture.name}: {image.width}x{image.height}')
