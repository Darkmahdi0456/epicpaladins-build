# Armor renderer mapping notes

| Armor set | Core armor bones | Special handling |
|---|---|---|
| Arclight | Head, body, arms, legs, boots | Standard humanoid hierarchy |
| Assassin | Head, body, arms, legs, boots | Standard humanoid hierarchy |
| Bloodstone | Head, body, arms, legs, boots | Standard humanoid hierarchy |
| Cryorium | Head, body, arms, legs, boots | Standard humanoid hierarchy |
| Jade | Head, body, arms, legs, boots | Standard humanoid hierarchy |
| Moonlight | Head, body, arms, legs, boots | Left/right leg hierarchy is swapped; investigate before rendering |
| Sculk | Head, body, arms, legs, boots | Standard humanoid hierarchy |
| Knight | Head, body, arms, legs, boots | Preserve extra decorative `bone*` groups |
| Angel | Head, body, arms, legs, boots | Wings and extra decorative groups; dedicated alignment check needed |

The mapping is based on the actual bone names in the GeoJSON files. It is not a claim that GeckoLib has rendered these models successfully.
