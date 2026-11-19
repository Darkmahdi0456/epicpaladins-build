#!/usr/bin/env python3
"""Cross-check registered Epic Paladins IDs against Fabric-facing resources."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent
SRC = ROOT/'src/main/java/net/veroxuniverse/epicpaladins/fabric/ContentRegistry.java'
ASSETS = ROOT/'src/main/resources/assets/epicpaladins'
DATA = ROOT/'src/main/resources/data/epicpaladins'
s = SRC.read_text(encoding='utf-8')
def array(name):
    m = re.search(rf'{name}\s*=\s*\{{(.*?)\}};', s, re.S)
    if not m: raise SystemExit(f'Cannot locate {name}')
    return re.findall(r'"([a-z0-9_]+)"', m.group(1))
items, blocks = array('ITEM_IDS'), array('BLOCK_IDS')
models = {p.stem for p in (ASSETS/'models/item').glob('*.json')}
blockstates = {p.stem for p in (ASSETS/'blockstates').glob('*.json')}
block_models = {p.stem for p in (ASSETS/'models/block').glob('*.json')}
loot = {p.stem for p in (DATA/'loot_table/blocks').glob('*.json')}
langs = {lang: json.loads((ASSETS/'lang'/f'{lang}.json').read_text(encoding='utf-8')) for lang in ('en_us','fa_ir')}
missing_item_models = sorted(set(items)-models)
missing_lang = {lang: sorted('item.epicpaladins.'+i for i in items if 'item.epicpaladins.'+i not in data) for lang,data in langs.items()}
missing_blockstates = sorted(set(blocks)-blockstates)
missing_block_models = sorted(set(blocks)-block_models)
missing_loot = sorted(set(blocks)-loot)
report = {
 'registered_items':len(items), 'registered_blocks':len(blocks),
 'item_models_found':len(set(items)&models), 'missing_item_models':missing_item_models,
 'english_item_names_found':len(items)-len(missing_lang['en_us']),
 'persian_item_names_found':len(items)-len(missing_lang['fa_ir']),
 'missing_english_names':missing_lang['en_us'], 'missing_persian_names':missing_lang['fa_ir'],
 'blockstates_found':len(set(blocks)&blockstates), 'missing_blockstates':missing_blockstates,
 'block_models_found':len(set(blocks)&block_models), 'missing_block_models':missing_block_models,
 'block_loot_tables_found':len(set(blocks)&loot), 'missing_block_loot_tables':missing_loot,
}
(ROOT/'STAGE50-REGISTRY-ASSET-AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
